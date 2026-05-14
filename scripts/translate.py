#!/usr/bin/env python
"""
Claude Haiku 4.5 で Liquid スニペットを日本語化。
入力: data/sample_50.jsonl (default)
出力:
  - data/translated_50.jsonl (default)
  - .meta.json サイドカー(モデル・トークン・コスト・キャッシュヒット率)
  - .post_log.json サイドカー(後処理ログ:末尾削除・30字超・タグ正規化)
"""
import argparse
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

MODEL = "claude-haiku-4-5-20251001"
PARALLEL = 8
MAX_RETRIES = 2

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# ---- カテゴリ ----
REF_CATEGORY = {
    "filters": "リファレンス/フィルター",
    "tags": "リファレンス/タグ",
    "objects": "リファレンス/オブジェクト",
}
REF_KIND_JA = {"filters": "フィルター", "tags": "タグ", "objects": "オブジェクト"}
REF_INLINE = {
    "filters": "Liquid 内で `{{ value | フィルター名 }}` の形で使う",
    "tags": "Liquid 内で `{% タグ名 %}` の形で使う",
    "objects": "Liquid 内で `{{ オブジェクト名.プロパティ }}` の形で参照する",
}

SNIPPET_CATEGORIES = [
    "ページテンプレート",
    "ヘッダー/フッター/ナビゲーション",
    "テーマ基盤",
    "商品表示",
    "コレクション/検索",
    "カート/チェックアウト",
    "顧客アカウント",
    "メタフィールド/メタオブジェクト",
    "SEO/構造化データ",
    "UI部品",
    "API連携/JSON出力/JS統合",
    "ユーティリティ",
]

# ---- タグ同義語正規化(SYSTEM_PROMPT のルールと一致させる) ----
TAG_SYNONYMS = {
    "giftcard": "gift-card",
    "gift_card": "gift-card",
    "jsonld": "json-ld",
    "json_ld": "json-ld",
    "structured-data": "json-ld",
    "structured_data": "json-ld",
    "paginate": "pagination",
    "paginated": "pagination",
}

# ---- 既知の複数形 → 単数形 ----
PLURAL_TO_SINGULAR = {
    "products": "product",
    "articles": "article",
    "collections": "collection",
    "variants": "variant",
    "blocks": "block",
    "filters": "filter",
    "tags": "tag",
    "objects": "object",
    "components": "component",
    "icons": "icon",
    "metafields": "metafield",
}
# 単数化対象外(Shopify オブジェクト名・固有名詞)
PLURAL_EXEMPT = {"linklists", "success", "customer_accounts", "accounts"}

# ---- タイトル末尾の不要語句 ----
TRAILING_NOISE_WORDS = ["スニペット", "セクション", "ブロック"]
TITLE_MAX_LEN = 30

# ---- include 検出 ----
# 末尾のクオート要求を撤廃: `{% include 'foo' %}` も `{% include foo %}` も両方マッチさせる
INCLUDE_RE = re.compile(r"\{\%-?\s*include\s+")
INCLUDE_NOTE = (
    "原文では `{% include %}` を使用していますが、Shopify Online Store 2.0 以降では "
    "`{% render %}` が推奨されます。新規実装時は render を使用してください。"
)

# ---- 日本語スタイル後処理 ----
# 液体 → Liquid(Liquid 以外の理科系文脈は除外)
LIQUID_COMPOUNDS = ["液体テンプレート", "液体タグ", "液体オブジェクト", "液体構文", "液体ファイル", "液体エンジン"]
LIQUID_EXCLUDE_PATTERNS = re.compile(r"液体(?=窒素|酸素|水素|クロマト|燃料|金属|金|ヘリウム|冷却|肥料)")
# 日本語の文字種(ひらがな・カタカナ・漢字・長音符・々)
JP_CHAR = r"[ぁ-んァ-ヶー一-龯々]"
JP_GAP_RE = re.compile(rf"({JP_CHAR})\s+({JP_CHAR})")
# 半角括弧の中身判定用
PAREN_CONTENT_RE = re.compile(r"\(([^()]*)\)")
HAS_JP_RE = re.compile(JP_CHAR)


def normalize_japanese_style(text: str) -> str:
    """日本語スタイルの確定的後処理(AI の揺れを吸収)"""
    if not text or not isinstance(text, str):
        return text
    # 1) 「液体タグ」等の複合語を Liquid に置換
    for compound in LIQUID_COMPOUNDS:
        if compound in text:
            text = text.replace(compound, compound.replace("液体", "Liquid "))
    # 2) 単独の「液体」(理科系除外) を Liquid に
    #    まず除外パターン位置を保護(プレースホルダ化)
    placeholders: dict = {}
    def protect(m):
        key = f"__LIQEXCLUDE{len(placeholders)}__"
        placeholders[key] = m.group(0)
        return key
    text = LIQUID_EXCLUDE_PATTERNS.sub(lambda m: protect(m), text)
    text = re.sub(r"液体", "Liquid", text)
    for k, v in placeholders.items():
        text = text.replace(k, v)
    # 3) 日本語文字の間の半角スペースを削除(連続適用で安定化)
    prev = None
    while prev != text:
        prev = text
        text = JP_GAP_RE.sub(r"\1\2", text)
    # 4) 連続半角スペース → 1つ
    text = re.sub(r" {2,}", " ", text)
    # 5) 日本語を含む半角括弧 → 全角括弧化(（ = 全角開, ） = 全角閉)
    def to_zenkaku(m):
        content = m.group(1)
        if HAS_JP_RE.search(content):
            return "（" + content + "）"
        return m.group(0)
    # 入れ子は考慮しない(最内側のみ)
    prev = None
    while prev != text:
        prev = text
        text = PAREN_CONTENT_RE.sub(to_zenkaku, text)
    return text


# 後処理を適用するテキストフィールド
JP_TEXT_FIELDS = (
    "title_ja",
    "description_ja",
    "use_case_ja",
    "where_to_paste_ja",
    "caveats_ja",
)

# ---- 後処理ログ(thread-safe な list.append のみ使用) ----
POST_LOG: list = []
POST_LOG_LOCK = threading.Lock()


SYSTEM_PROMPT = """あなたは Shopify Liquid スニペットの日本語カタログを編集する EC エキスパートです。
日本の Shopify マーチャント、構築会社、フリーランス向けに、英語のオープンソース素材を自然な日本語に翻訳・要約します。

# 出力ルール(全件共通)
- 必ず JSON 形式で出力する(前置き・``` フェンス禁止)
- 翻訳は意訳でよい。直訳ではなく日本語として自然な文に
- コードから読み取れない情報は書かない(嘘・憶測禁止)
- 日本市場のマーチャント目線で実務的に
- 文末の冗長表現を避け、簡潔に

# 出力フィールド(すべて必須)
- title_ja: タイトル(フォーマット規定あり、下記参照)
- description_ja: 説明(2〜3文、何を解決するコードか)
- use_case_ja: 用途(どのページ・どんなシーンで使うか、1〜2文)
- where_to_paste_ja: 設置場所(具体的なファイルパス＋呼び出しコード、1〜2文)
- caveats_ja: 注意点(品質ルールあり、下記参照)
- category: 下記カテゴリ体系から1つ
- difficulty: "初級" / "中級" / "上級"
- tags: タグ配列(命名規則あり、下記参照)

# タイトル(title_ja)フォーマット(厳守)
- リファレンス/フィルター: "{フィルター名} フィルター({30字以内の用途})"
  例: "money フィルター(金額をストア通貨で整形)"
- リファレンス/タグ: "{タグ名} タグ({30字以内の用途})"
  例: "if タグ(条件分岐)"
- リファレンス/オブジェクト: "{オブジェクト名} オブジェクト"(カッコ書き不要)
  例: "product オブジェクト"
- スニペット系: 30字以内の機能名のみ。末尾に「スニペット」「セクション」「ブロック」を付けない
  例: "商品カードのバリアント切替"(NG: "商品カードのバリアント切替スニペット")

# カテゴリ(category)体系
リファレンス系(ソースが theme-liquid-docs の場合、ユーザー指示で固定):
- "リファレンス/フィルター"(data/filters.json 由来)
- "リファレンス/タグ"(data/tags.json 由来)
- "リファレンス/オブジェクト"(data/objects.json 由来)

スニペット系(ファイルパスを最優先で判定):
- "ページテンプレート"(templates/ 配下)
- "ヘッダー/フッター/ナビゲーション"
- "テーマ基盤"(layout/ 配下、css-variables、meta-tags 等)
- "商品表示"
- "コレクション/検索"
- "カート/チェックアウト"
- "顧客アカウント"
- "メタフィールド/メタオブジェクト"
- "SEO/構造化データ"
- "UI部品"(アイコン、区切り線、ロゴ等)
- "API連携/JSON出力/JS統合"
- "ユーティリティ"

判定優先順位: ① ソースリポジトリ(reference 系か否か) > ② ファイルパス > ③ 内容の意味解釈

# タグ(tags)命名規則
- 英小文字、ハイフン区切り(アンダースコア禁止: `gift_card` ではなく `gift-card`)
- 単数形原則: `product`(NG: `products`)、`tag`(NG: `tags`)、`block`(NG: `blocks`)
- 同義語正規化:
  - giftcard / gift_card → "gift-card"
  - jsonld / structured-data → "json-ld"
  - paginate / paginated → "pagination"
  - 404 ページ関連は "error-page" と "404" の両方を併記する
- 個数: 3〜6個
- category と完全一致する名前のタグは禁止(例: category が "商品表示" なら "商品表示" タグを付けない)

# 注意点(caveats_ja)の品質ルール
- 「〜が必要です」を3回以上連続で使わない。言い回しを変えて重複を避ける
- 構成: ① 前提条件 → ② 落とし穴 → ③ 応用時の注意 の順で書く
- 抽象的禁止: "型チェックが必要" のような曖昧表現は使わず、具体策を書く
  例: "数値計算する前に `| times: 1` で明示的に数値化する"
- 1〜3文、実務で役立つ具体性を確保

# 日本語スタイルルール(厳守)

1. **文体は常体(である調)で統一する**
   - NG: 「〜構築します」「〜機能します」「〜対応します」「〜実装します」「〜表示します」
   - OK: 「〜構築する」「〜機能する」「〜対応する」「〜実装する」「〜表示する」
   - 例外: caveats_ja の文末で「〜が必要」「〜推奨」「〜が前提」は許容(言い切りの常体扱い)
   - description_ja / use_case_ja / where_to_paste_ja は厳格に常体

2. **英日混在の不自然なカタカナ語を避ける**
   - 「hardcoded」「ハードコード」(英語まま/中途半端カタカナ) → 「ハードコードされている」「直接記述されている」
   - 「break する」「break」 → 「正しく適用されない」「指定が崩れる」「動かない」
   - 「API 的に」 → 「API のように」「API として」
   - 「データ層」(漠然) → 「データ基盤」「データ受け渡し」(文脈に応じて)
   - 「○○ する」(英単語 + する) は最小限に。和訳できるものは和訳する

3. **Liquid は固有名詞として常に英字「Liquid」と表記する**
   - NG: 「液体テンプレート」「液体タグ」「液体オブジェクト」「液体構文」
   - OK: 「Liquid テンプレート」「Liquid タグ」「Liquid オブジェクト」「Liquid 構文」
   - 「液体」単独で出てくる場合も Liquid を意図しているなら必ず「Liquid」

4. **記号の列挙は読点で区切る**
   - NG: 「HTML 特殊文字(&<>シングルクォート等)」(連続して読みにくい)
   - OK: 「HTML 特殊文字(<、>、&、シングルクォートなど)」(読点で明確に区切る)

5. **「Web に」「Web で」のような中途半端な表現を避ける**
   - NG: 「Web に公開」「Web で見える」
   - OK: 「Web 上で公開」「ストア上で公開」「サイトに公開」「サイト上で表示」

6. **「展開収縮」「展開縮小」のような不自然な熟語を避ける**
   - NG: 「アコーディオンが展開収縮する」「メニューが展開縮小する」
   - OK: 「アコーディオンが開閉する」「メニューが開く・閉じる」

7. **「○○ことを通知する」のような曖昧な指示語を避け、主語と目的語を明示する**
   - NG: 「ユーザーに見つからないことを通知する」(何が見つからないか不明)
   - OK: 「ページが見つからないことをユーザーに伝える」「該当商品がないことを画面に表示する」

---
【出力品質の参考例】

これらは Phase 1 で品質が高かった実例。同程度の具体性・構成を目指してください。

例1: 入力 = freakdesign の request_host.liquid(マルチドメイン分岐スニペット)
ファイルパス: Get current domain name with Liquid/request_host.liquid
コードの骨子: `{% if request.host == 'foo.example.com' %} ... {% elsif request.host == 'bar.example.com' %} ... {% endif %}` の形でアクセスしているドメインに応じて表示内容や画像 URL を切り替える。
理想出力(抜粋):
{
  "title_ja": "ドメイン判定で画像を切り替え",
  "category": "テーマ基盤",
  "difficulty": "中級",
  "tags": ["request", "multidomain", "conditional", "asset"],
  "use_case_ja": "日本・US・EU など複数ドメインで Shopify を運用しているとき、ドメインごとに別画像やバナーを出し分ける。",
  "where_to_paste_ja": "theme.liquid の <head> 内、または出し分けたい画像直前の section / snippet 内に貼り付け、`request.host` の比較値を自店舗のドメインに置き換える。",
  "caveats_ja": "request.host は開発ストア(*.myshopify.com)では機能しないため、カスタムドメイン設定が前提となる。条件分岐が増えると可読性が低下するため、3ドメイン以上になる場合は Shopify Markets 設定や theme settings の選択肢ベースに切り替えるとよい。プレビュー環境(preview.example.com など)では値が変わるので、本番ドメインを確定させてからリリースする。"
}

例2: 入力 = uicrooks の layout-menu.liquid(階層付きナビゲーションメニュー)
ファイルパス: shopify/snippets/layout-menu.liquid
コードの骨子: Shopify 管理画面の「メインメニュー」リンクリストをループし、`link.links` の有無で1階層のサブメニューを描画する。
理想出力(抜粋):
{
  "title_ja": "メインメニューのナビゲーション",
  "category": "ヘッダー/フッター/ナビゲーション",
  "difficulty": "初級",
  "tags": ["navigation", "menu", "linklists", "header", "dropdown"],
  "use_case_ja": "ストア共通のグローバルナビをヘッダーに出すとき。トップレベル + 1階層のサブメニューに対応。",
  "where_to_paste_ja": "shopify/snippets/layout-menu.liquid に配置し、`theme.liquid` のヘッダー内で `{% render 'layout-menu' %}` で呼び出す。",
  "caveats_ja": "Shopify 管理画面で「メインメニュー」ハンドルのリンクリストが作成されていることが前提。サブメニューは1階層のみの対応なので、3階層以上の深いメニューが必要なときは再帰実装に書き換える。モバイル表示ではドロップダウンが画面外に出ないよう CSS で位置を調整する。"
}

例3: 入力 = freakdesign の badge.liquid(商品カード上の SALE / 新商品バッジ)
ファイルパス: Badges/badge.liquid
コードの骨子: `{% if product.compare_at_price > product.price %}` で SALE バッジ、`{% if product.created_at > 30.days.ago %}` 的なロジックで「新商品」バッジを商品カードの左上にオーバーレイ表示する。
理想出力(抜粋):
{
  "title_ja": "商品カードのSALE・新商品バッジ",
  "category": "商品表示",
  "difficulty": "初級",
  "tags": ["product", "badge", "sale", "new-arrival", "overlay"],
  "description_ja": "商品カードの隅に SALE バッジと NEW バッジを条件付きで表示するスニペット。compare_at_price が price より大きい場合に SALE、新着商品に NEW を出す。",
  "use_case_ja": "コレクションページや関連商品の商品カードで、価格訴求や新商品アピールを視覚的に強化したいとき。",
  "where_to_paste_ja": "snippets/badge.liquid に配置し、product-card.liquid の画像コンテナ内で `{% render 'badge', product: product %}` で呼び出す。",
  "caveats_ja": "compare_at_price が未設定だと `nil` 比較で常に false になるため、Shopify 管理画面で各バリアントに比較価格を入力しておく前提。新商品判定の閾値(30日など)はストア商材の入荷頻度に合わせて調整する。バッジ画像と CSS の重なり順は z-index と position: absolute を商品カード側に揃えて指定する。"
}

例4: 入力 = pgrimaud の json-ld-product.liquid(商品ページの構造化データ)
ファイルパス: snippets/json-ld-product.liquid
コードの骨子: `<script type="application/ld+json">` 内で product の name / image / offers(price, availability, priceCurrency)を schema.org の Product 型として出力する。
理想出力(抜粋):
{
  "title_ja": "商品ページのProduct構造化データ",
  "category": "SEO/構造化データ",
  "difficulty": "中級",
  "tags": ["json-ld", "schema-org", "product", "seo", "rich-result"],
  "description_ja": "商品詳細ページに schema.org の Product 型 JSON-LD を埋め込み、Google 検索のリッチリザルト(価格・在庫・レビュー)に対応させる。",
  "use_case_ja": "商品ページで Google の「商品スニペット」表示を狙うときに必須。価格・在庫・通貨が検索結果に出るようになる。",
  "where_to_paste_ja": "snippets/json-ld-product.liquid に配置し、templates/product.liquid または sections/main-product.liquid 内の `</body>` 直前で `{% render 'json-ld-product', product: product %}` で呼び出す。",
  "caveats_ja": "price は数値である必要があるため、`product.price | money_without_currency` の通貨記号付き形式は使えず `product.price | divided_by: 100.0` のように円/ドル単位に変換する。priceCurrency はストア通貨(`shop.currency`)を入れ、配送地域ごとに違う場合は配送設定と整合させる。Google Search Console の URL 検査ツールで構造化データのエラーが出ていないか必ず確認する。"
}

これら4例の caveats のように、抽象表現ではなく具体的な「設定名・関数名・閾値・代替手段」を書いてください。

# スタイル違反例(必ず避けるべき悪い例 → 改善した良い例)

悪い例A(避けるべき):
"商品データとフィルタ条件を JavaScript に渡すデータ層として機能します。回答が展開収縮し、Google 検索結果のリッチリザルト対応のため、カラーが hardcoded(#428445)で font-family が break する設定。"

良い例A(目指すべき):
"商品データとフィルタ条件を JavaScript に渡すデータ基盤として機能する。回答が開閉し、Google 検索結果でのリッチリザルト表示に対応する。色は #428445 にハードコードされ、font-family の指定が崩れる設定。"

悪い例A の問題点:
- 「機能します」「対応します」が敬体(NG: 常体で統一)
- 「データ層」が漠然(OK: 「データ基盤」「データ受け渡し」)
- 「展開収縮」が不自然な熟語(OK: 「開閉」)
- 「hardcoded」が英語まま(OK: 「ハードコードされている」)
- 「break する」が中途半端(OK: 「指定が崩れる」)

悪い例B(避けるべき):
"液体テンプレートでメタフィールドを Web に出力します。エラー時はユーザーに見つからないことを通知し、HTML 特殊文字(&<>)をエスケープします。"

良い例B(目指すべき):
"Liquid テンプレートでメタフィールドをストア上に出力する。エラー時はページが見つからないことをユーザーに伝え、HTML 特殊文字(<、>、&)をエスケープする。"

悪い例B の問題点:
- 「液体テンプレート」が誤訳(OK: 「Liquid テンプレート」、Liquid は固有名詞)
- 「Web に」が中途半端(OK: 「ストア上に」「サイトに」)
- 「ユーザーに見つからないことを通知」が主語曖昧(OK: 「ページが見つからないことをユーザーに伝える」)
- 記号列挙「&<>」が読みにくい(OK: 「<、>、&」と読点で区切る)
- 「出力します」「エスケープします」が敬体(NG: 常体で統一)

悪い例C(避けるべき):
"font_modify で ウェイト・スタイルを変更。商品のメタフィールドから テキストと色を読み込み、(#428445 の緑色)を使用する。"

良い例C(目指すべき):
"font_modify でウェイト・スタイルを変更する。商品のメタフィールドからテキストと色を読み込み、（#428445 の緑色）を使用する。"

悪い例C の問題点:
- 「で ウェイト」「から テキスト」「または メンテナンス」のような日本語間に挟まる不要な半角スペースを入れない
- 日本語文字を含む括弧は全角「（）」を使う(英数字のみの括弧は半角「()」のまま OK、例: `(#428445)` `(default: 0)`)
- 「変更」「読み込み」など連用形で文を切らず、必要なら言い切りの「変更する」で締める

# Shopify 専門用語の日本語表記ガイド
- "snippet" → 「スニペット」(タイトル末尾には使わない)
- "section" → 「セクション」(タイトル末尾には使わない)
- "linklist" / "link list" → 「リンクリスト」または「メニュー」(管理画面ラベルに準拠)
- "metafield" → 「メタフィールド」
- "metaobject" → 「メタオブジェクト」
- "variant" → 「バリアント」(商品の色・サイズ等のバリエーション)
- "compare_at_price" → 「比較価格」または「定価」(セール元価格)
- "collection" → 「コレクション」(商品グループ)
- "checkout" → 「チェックアウト」
- "request.host" → 「リクエストホスト」より「アクセスしたドメイン」のほうが伝わりやすい
- "Online Store 2.0" → そのまま「Online Store 2.0」(または「OS 2.0」)、訳さない
- "Shopify Functions" → そのまま「Shopify Functions」、訳さない
- "Shopify Markets" → そのまま「Shopify Markets」、訳さない
- "Theme Customizer" → 「テーマカスタマイザー」または「管理画面のカスタマイズ画面」
- "linklist handle" → 「リンクリストのハンドル」
- "product handle" → 「商品ハンドル」(管理画面の URL スラッグ)
- "cart drawer" → 「カートドロワー」(画面横から出てくるミニカート)
- "rich result" / "rich snippet" → 「リッチリザルト」(Google 検索結果の拡張表示)
- "headless" → 「ヘッドレス」(Storefront API / Hydrogen 等を使う構成)

これらの表記を守って、日本のマーチャント・構築会社が現場で使う語彙に近づけてください。

# 最後の注意
- 出力は必ず JSON オブジェクトの中身のみ(前後のテキスト・``` フェンス・コメント禁止)
- すべてのフィールドを埋めること。`null` や空文字を返さない
- 上記4例の品質を最低基準とし、それを下回らないこと
"""


USER_TEMPLATE_COMMUNITY = """以下は Shopify Liquid のスニペットです。日本語化してください。

# メタ情報
- ファイル名: {file_name}
- ファイルパス: {file_path}  ← カテゴリ判定の最優先シグナル
- リポジトリ: {repo_owner}/{repo_name}
- ライセンス: {license}
- 行数: {line_count}

# コード
```liquid
{code}
```
{include_directive}
# カテゴリ候補(必ずこの中から1つ選ぶ)
{categories}

JSON のみで回答してください。"""


USER_TEMPLATE_REFERENCE = """以下は Shopify Liquid の公式仕様(theme-liquid-docs)からのエントリです。日本語化してください。

# 種別とカテゴリ(固定)
- 種別: {kind_ja}
- カテゴリ: "{category_fixed}"(category フィールドには必ずこの値を入れる)

# メタ情報
- 名前: {name}
- リポジトリ: {repo_owner}/{repo_name}
- ライセンス: {license}

# 仕様 JSON
```json
{code}
```

# 補足
- description_ja: 「何のフィルター/タグ/オブジェクトか」を簡潔に
- use_case_ja: 典型的な使用シーン
- where_to_paste_ja: {kind_inline}という書き方で
- caveats_ja: 型・廃止予定・代替フィルターなど仕様上の注意があれば記載

JSON のみで回答してください。"""


INCLUDE_BLOCK = """
# ⚠️ `{% include %}` 検出
このコードは `{% include %}` を使用しています。以下を必ず満たすこと:
- caveats_ja に次の旨を含める: 「原文では `{% include %}` を使用していますが、Shopify Online Store 2.0 以降では `{% render %}` が推奨されます。新規実装時は render を使用してください。」
- where_to_paste_ja の例コードは `{% render '...' %}` 形式に書き直す
"""


def has_include_tag(code: str) -> bool:
    return bool(INCLUDE_RE.search(code))


def build_user_message(rec):
    if rec["source_kind"].startswith("reference"):
        kind = rec.get("reference_kind", "")
        return USER_TEMPLATE_REFERENCE.format(
            kind_ja=REF_KIND_JA.get(kind, kind),
            category_fixed=REF_CATEGORY.get(kind, "リファレンス/" + kind),
            kind_inline=REF_INLINE.get(kind, "Liquid 内で使用"),
            name=rec.get("reference_name", rec["file_name"]),
            repo_owner=rec["repo_owner"],
            repo_name=rec["repo_name"],
            license=rec["license"],
            code=rec["code"][:6000],
        )
    include_directive = INCLUDE_BLOCK if has_include_tag(rec["code"]) else ""
    return USER_TEMPLATE_COMMUNITY.format(
        file_name=rec["file_name"],
        file_path=rec["file_path"],
        repo_owner=rec["repo_owner"],
        repo_name=rec["repo_name"],
        license=rec["license"],
        line_count=rec["line_count"],
        code=rec["code"][:8000],
        include_directive=include_directive,
        categories="\n".join(f'- "{c}"' for c in SNIPPET_CATEGORIES),
    )


JSON_FENCE = re.compile(r"```(?:json)?\s*([\s\S]*?)```", re.IGNORECASE)


def parse_json_response(text):
    text = text.strip()
    m = JSON_FENCE.search(text)
    if m:
        text = m.group(1).strip()
    if not text.startswith("{"):
        s = text.find("{")
        if s >= 0:
            text = text[s:]
    if not text.endswith("}"):
        e = text.rfind("}")
        if e >= 0:
            text = text[: e + 1]
    return json.loads(text)


def normalize_tag_value(t: str) -> str:
    """小文字化・アンダースコア→ハイフン・同義語正規化"""
    s = (t or "").strip().lower().replace("_", "-")
    return TAG_SYNONYMS.get(s, s)


def singularize_tag(tag: str, unknown_log: list) -> str:
    """既知の複数形を単数形に。マップにないが複数形候補は unknown_log に記録"""
    if tag in PLURAL_EXEMPT:
        return tag
    if tag in PLURAL_TO_SINGULAR:
        return PLURAL_TO_SINGULAR[tag]
    # 不明な複数形候補(末尾 s / 末尾 ss でなく / 2文字超 / 既知例外でない)
    if (
        tag.endswith("s")
        and not tag.endswith("ss")
        and len(tag) > 2
        and tag not in PLURAL_EXEMPT
    ):
        unknown_log.append(tag)
    return tag


def strip_title_suffix(title: str):
    """末尾の不要語句を削除。(new_title, removed_word or None) を返す"""
    if not title:
        return title, None
    # 改行・周辺空白だけ最初にトリム(削除判定はその後)
    stripped = title.rstrip()
    for word in TRAILING_NOISE_WORDS:
        if stripped.endswith(word):
            new = stripped[: -len(word)].rstrip(" 　\t")
            return new, word
    return title, None


def post_process(rec, parsed):
    """JSON パース後の確定的後処理(AI に任せると揺れる部分をここで吸収)"""
    log_entry: dict = {"id": rec["id"], "file_name": rec.get("file_name")}

    # 0) 日本語スタイル正規化(液体→Liquid、スペース、全角括弧)
    style_changes: dict = {}
    for k in JP_TEXT_FIELDS:
        v = parsed.get(k)
        if isinstance(v, str):
            new_v = normalize_japanese_style(v)
            if new_v != v:
                style_changes[k] = {"before": v, "after": new_v}
                parsed[k] = new_v
    if style_changes:
        log_entry["style_normalized"] = list(style_changes.keys())

    # 1) リファレンスのカテゴリ強制
    if rec["source_kind"].startswith("reference"):
        kind = rec.get("reference_kind", "")
        if kind in REF_CATEGORY:
            parsed["category"] = REF_CATEGORY[kind]

    # 2) タイトル末尾の不要語句削除(スタイル正規化後の title に対して実行)
    orig_title = parsed.get("title_ja", "") or ""
    new_title, removed = strip_title_suffix(orig_title)
    if removed:
        parsed["title_ja"] = new_title
        log_entry["title_suffix_removed"] = {
            "word": removed,
            "before": orig_title,
            "after": new_title,
            "before_len": len(orig_title),
            "after_len": len(new_title),
        }

    # 3) タグ正規化(同義語 + 単数形 + 重複除去 + カテゴリ名除外)
    tags = parsed.get("tags", []) or []
    if not isinstance(tags, list):
        tags = [tags]
    unknown_plurals: list = []
    norm: list = []
    seen: set = set()
    for t in tags:
        if not isinstance(t, str):
            continue
        n = normalize_tag_value(t)
        n = singularize_tag(n, unknown_plurals)
        if not n or n in seen:
            continue
        seen.add(n)
        norm.append(n)
    cat = parsed.get("category", "")
    norm = [t for t in norm if t != cat]

    # 4) タイトル30字超フラグ(現タイトル基準、削除後の長さで判定)
    final_title = parsed.get("title_ja", "") or ""
    if len(final_title) > TITLE_MAX_LEN:
        if "title-too-long" not in norm:
            norm.append("title-too-long")
        log_entry["title_too_long"] = {"len": len(final_title), "title": final_title}

    parsed["tags"] = norm

    if unknown_plurals:
        log_entry["unknown_plurals"] = unknown_plurals

    # 5) include 検出時の caveats 補強(フェイルセーフ)
    if not rec["source_kind"].startswith("reference") and has_include_tag(rec["code"]):
        cav = (parsed.get("caveats_ja") or "").strip()
        if "render" not in cav or "include" not in cav:
            parsed["caveats_ja"] = (cav + " " + INCLUDE_NOTE).strip()
            log_entry["include_note_appended"] = True

    # 何か記録すべき情報がある場合のみログに追加
    if len(log_entry) > 2:
        with POST_LOG_LOCK:
            POST_LOG.append(log_entry)
    return parsed


def translate_one(rec):
    user_msg = build_user_message(rec)
    for attempt in range(MAX_RETRIES + 1):
        try:
            # NOTE: prompt caching は 2024-08 に GA 済み。古いベータヘッダー
            # `anthropic-beta: prompt-caching-2024-07-31` を付けると現行 API と
            # 衝突して cache_control が無効化される現象を確認したため未指定。
            # system プロンプトの cache_control={"type": "ephemeral"} のみで動作する。
            resp = client.messages.create(
                model=MODEL,
                max_tokens=1200,
                system=[
                    {
                        "type": "text",
                        "text": SYSTEM_PROMPT,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                messages=[{"role": "user", "content": user_msg}],
            )
            text = "".join(b.text for b in resp.content if hasattr(b, "text"))
            parsed = parse_json_response(text)
            parsed = post_process(rec, parsed)
            usage = {
                "input_tokens": resp.usage.input_tokens,
                "output_tokens": resp.usage.output_tokens,
                "cache_creation_input_tokens": getattr(
                    resp.usage, "cache_creation_input_tokens", 0
                ),
                "cache_read_input_tokens": getattr(
                    resp.usage, "cache_read_input_tokens", 0
                ),
            }
            return {**rec, "translation": parsed, "usage": usage, "error": None}
        except Exception as e:
            if attempt >= MAX_RETRIES:
                return {**rec, "translation": None, "usage": None, "error": str(e)}
            time.sleep(2 * (attempt + 1))


def _load_existing(dst_path: Path):
    """既存 jsonl を読み、(id セット, レコードリスト) を返す"""
    if not dst_path.exists():
        return set(), []
    ids = set()
    records = []
    with dst_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if "id" in r:
                ids.add(r["id"])
                records.append(r)
    return ids, records


def _aggregate(records):
    """ok/ng/トークン/コスト/cache hit_rate を集計"""
    ok = sum(1 for r in records if r.get("error") is None and r.get("translation"))
    ng = len(records) - ok
    in_tok = sum((r.get("usage") or {}).get("input_tokens", 0) for r in records)
    out_tok = sum((r.get("usage") or {}).get("output_tokens", 0) for r in records)
    cache_create = sum(
        (r.get("usage") or {}).get("cache_creation_input_tokens", 0) for r in records
    )
    cache_read = sum(
        (r.get("usage") or {}).get("cache_read_input_tokens", 0) for r in records
    )
    total_input = in_tok + cache_create + cache_read
    hit_rate = (cache_read / total_input) if total_input else 0.0
    cost = (
        in_tok * 1.0 / 1_000_000
        + out_tok * 5.0 / 1_000_000
        + cache_create * 1.25 / 1_000_000
        + cache_read * 0.1 / 1_000_000
    )
    return {
        "ok": ok,
        "ng": ng,
        "in_tok": in_tok,
        "out_tok": out_tok,
        "cache_create": cache_create,
        "cache_read": cache_read,
        "hit_rate": hit_rate,
        "cost": cost,
    }


def main():
    import signal as _signal
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="data/sample_50.jsonl")
    parser.add_argument("--dst", default="data/translated_50.jsonl")
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="既存 dst を無視して最初から再実行(既存ファイルは削除)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="チェックポイント単位(default: 100件ごとに meta/post_log を更新)",
    )
    args = parser.parse_args()
    src = ROOT / args.src
    dst = ROOT / args.dst
    dst.parent.mkdir(parents=True, exist_ok=True)

    # 全レコード読み込み
    all_records = [json.loads(l) for l in src.open(encoding="utf-8")]

    # 既存処理済み(チェックポイント)
    if args.no_resume and dst.exists():
        dst.unlink()
        meta_p = dst.with_suffix(".meta.json")
        post_p = dst.with_suffix(".post_log.json")
        if meta_p.exists():
            meta_p.unlink()
        if post_p.exists():
            post_p.unlink()
    existing_ids, existing_records = _load_existing(dst)

    # 既存 post_log を読み込んでマージ(失敗しても無視)
    post_log_path = dst.with_suffix(".post_log.json")
    if post_log_path.exists():
        try:
            POST_LOG.extend(json.loads(post_log_path.read_text(encoding="utf-8")))
        except Exception:
            pass

    pending = [r for r in all_records if r["id"] not in existing_ids]
    print(
        f"[translate] total={len(all_records)} done={len(existing_ids)} "
        f"pending={len(pending)} model={MODEL} parallel={PARALLEL}",
        file=sys.stderr,
    )

    if not pending:
        agg = _aggregate(existing_records)
        print(
            f"[translate] nothing to do. existing: ok={agg['ok']} ng={agg['ng']} "
            f"cost=${agg['cost']:.4f} hit_rate={agg['hit_rate']*100:.1f}%",
            file=sys.stderr,
        )
        return

    # SIGINT/SIGTERM ハンドラ(graceful shutdown)
    shutdown_event = threading.Event()

    def _handle_signal(signum, frame):
        if shutdown_event.is_set():
            # 2度目の Ctrl-C で強制終了
            print(f"\n[translate] forced exit on signal {signum}", file=sys.stderr)
            os._exit(130)
        print(
            f"\n[translate] received signal {signum}. "
            f"draining current batch then stopping. Ctrl-C again for force exit.",
            file=sys.stderr,
        )
        shutdown_event.set()

    _signal.signal(_signal.SIGINT, _handle_signal)
    _signal.signal(_signal.SIGTERM, _handle_signal)

    meta_path = dst.with_suffix(".meta.json")
    flush_lock = threading.Lock()
    t0 = time.time()
    new_records = []

    def _checkpoint():
        """meta.json と post_log.json を更新"""
        combined = existing_records + new_records
        agg = _aggregate(combined)
        meta = {
            "model": MODEL,
            "elapsed_seconds": round(time.time() - t0, 1),
            "parallel": PARALLEL,
            "total_records": len(combined),
            "ok": agg["ok"],
            "err": agg["ng"],
            "input_tokens": agg["in_tok"],
            "output_tokens": agg["out_tok"],
            "cache_creation_input_tokens": agg["cache_create"],
            "cache_read_input_tokens": agg["cache_read"],
            "cache_hit_rate": round(agg["hit_rate"], 4),
            "est_cost_usd": round(agg["cost"], 6),
            "checkpoint_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        meta_path.write_text(
            json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        post_log_path.write_text(
            json.dumps(POST_LOG, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    # バッチごとに submit → 完了 → flush → checkpoint
    BATCH = max(1, args.batch_size)
    batches = [pending[i:i + BATCH] for i in range(0, len(pending), BATCH)]
    completed_total = 0

    with dst.open("a", encoding="utf-8") as fout:
        with ThreadPoolExecutor(max_workers=PARALLEL) as pool:
            for batch_idx, batch in enumerate(batches):
                if shutdown_event.is_set():
                    print(
                        f"[translate] stopping before batch {batch_idx + 1}/{len(batches)}. "
                        f"remaining={len(pending) - completed_total}",
                        file=sys.stderr,
                    )
                    break
                futures = {pool.submit(translate_one, r): r for r in batch}
                for fut in as_completed(futures):
                    rec = futures[fut]
                    try:
                        result = fut.result()
                    except Exception as e:
                        result = {
                            **rec,
                            "translation": None,
                            "usage": None,
                            "error": f"future_exception: {e}",
                        }
                    new_records.append(result)
                    with flush_lock:
                        fout.write(json.dumps(result, ensure_ascii=False) + "\n")
                        fout.flush()
                    completed_total += 1
                    status = "OK " if result.get("error") is None else "ERR"
                    print(
                        f"  [{completed_total + len(existing_ids):>5}/"
                        f"{len(all_records)}] {status} {rec['id'][:60]}",
                        file=sys.stderr,
                    )
                # バッチ完了 → checkpoint
                _checkpoint()
                agg = _aggregate(existing_records + new_records)
                print(
                    f"[checkpoint] batch {batch_idx + 1}/{len(batches)} done. "
                    f"cost=${agg['cost']:.4f} hit_rate={agg['hit_rate']*100:.1f}%",
                    file=sys.stderr,
                )

    # 最終 checkpoint
    _checkpoint()
    agg = _aggregate(existing_records + new_records)
    elapsed = time.time() - t0
    print(
        f"\n[translate] done: total={len(all_records)} "
        f"newly_processed={len(new_records)} ok={agg['ok']} ng={agg['ng']} "
        f"elapsed={elapsed:.1f}s",
        file=sys.stderr,
    )
    print(
        f"  tokens: input={agg['in_tok']} output={agg['out_tok']}\n"
        f"  cache: create={agg['cache_create']} read={agg['cache_read']} "
        f"hit_rate={agg['hit_rate']*100:.1f}%\n"
        f"  est_cost: ${agg['cost']:.4f}",
        file=sys.stderr,
    )
    print(f"[translate] wrote -> {dst}", file=sys.stderr)
    print(f"[translate] meta -> {meta_path}", file=sys.stderr)
    print(
        f"[translate] post_log -> {post_log_path} ({len(POST_LOG)} entries)",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
