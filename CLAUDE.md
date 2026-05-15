# ALSEL監修 Shopify セクション 制作ルール v1.1

Phase 6β(22 セクション)実機検証後に確定したルール。Phase 6γ 以降の生成では
生成時から守ること。Claude Code / Cline はこのファイルを毎回読み込んで適用すること。

---

## ルール 1: 文体は「ですます調」で統一

`default` / `heading` / `subheading` / `empty` メッセージなどマーチャント可視のテキストは
すべて「ですます調」。コメントや `info`(技術解説)のみ「だ・である調」可。

NG → OK 例:
- `を紹介する。` → `をご紹介します。`
- `を選択する。` → `をご選択ください。`
- `効果を実感できる。` → `効果を実感できます。`
- `ぜひ一度試してみてほしい。` → `ぜひ一度お試しください。`
- `を運んでくれる。` → `を運んでくれます。`
- `自動で割引が適用される。` → `自動で割引が適用されます。`
- `わかりやすく解説する。` → `わかりやすく解説します。`
- `状態を確認する。` → `状態を確認します。`
- `定期購入をおすすめする。` → `定期購入をおすすめします。`
- `返品・交換に対応する。` → `返品・交換に対応します。`
- `一つひとつ丁寧に収穫する。` → `一つひとつ丁寧に収穫します。`
- `収穫翌日にお届けする。` → `収穫翌日にお届けします。`
- `ご注文金額から10%を割引する。` → `ご注文金額から10%を割引します。`
- `全国どこでも送料を無料にする。` → `全国どこでも送料を無料にします。`
- `人気商品のサンプルを同梱する。` → `人気商品のサンプルを同梱します。`
- `一覧表示される。` → `一覧表示されます。`

自己チェック:
```bash
grep -E '"default": "[^"]*(する|される|できる|てほしい|くれる)。"' sections/*.liquid
```
ヒットゼロを確認。

---

## ルール 2: 日付・時刻系の default は遠未来(2099年)

countdown-timer 等で「終了日時 default = 2025/12/31」を使うと、本番投入時に全件
「終了しました」表示になる。

NG → OK:
```diff
- { "type": "number", "id": "end_year", "label": "年", "default": 2025 }
+ { "type": "number", "id": "end_year", "label": "年", "default": 2099 }
```

---

## ルール 3: blocks ありセクションは必ず空フォールバックを実装

blocks ゼロ件で「ヘッダーだけ残ってカード部分が完全に空」になる問題を防ぐ。
`{%- for block in section.blocks -%}` の直前に空判定を入れる。

```liquid
<div class="alsel-{slug}__grid">
  {%- if section.blocks.size == 0 -%}
    <p class="alsel-{slug}__empty" style="text-align:center;color:#888;padding:2rem 0;">
      現在表示できる項目はありません。テーマエディタからブロックを追加してください。
    </p>
  {%- endif -%}
  {%- for block in section.blocks -%}
    <article class="alsel-{slug}__card" {{ block.shopify_attributes }}>
      ...
    </article>
  {%- endfor -%}
</div>
```

セクション種別ごとの推奨文言:
- レビュー系: `現在表示できるレビューはありません。テーマエディタからブロックを追加してください。`
- FAQ 系: `よくあるご質問はまだ登録されていません。`
- ステップ系: `手順はまだ登録されていません。`
- 受賞・実績系: `表示できる実績はまだありません。`
- 商品系 blocks: `表示する商品をテーマエディタから追加してください。`

---

## ルール 4: 画像 + テキスト 2 カラムは画像未設定時に 1 カラム化

画像なしでも左半分が空白で残る問題を防ぐ。`<section>` に条件付きクラス + CSS で
レイアウト切替。

```liquid
<section
  class="alsel-{slug}{%- if section.settings.main_image == blank %} alsel-{slug}--no-image{%- endif -%}"
  aria-label="{{ section.settings.heading | escape }}">
  ...
</section>

<style>
  .alsel-{slug}__inner {
    max-width: 1100px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: center;
  }
  .alsel-{slug}--no-image .alsel-{slug}__media { display: none; }
  .alsel-{slug}--no-image .alsel-{slug}__inner {
    grid-template-columns: 1fr;
    max-width: 800px;
    text-align: center;
  }
</style>
```

適用対象: brand-story / producer-profile / bulk-buy-offer など、メイン画像 + テキスト
構成のセクション。

---

## ルール 5: 同種セクションは preset.name と default heading の両方で UI タイプを差別化

同種のセクションが複数あるとマーチャントが混乱する。preset 名と default 見出しの
両方でバリエーションを明示。

NG → OK:
```diff
- "name": "ALSEL監修 / お客様の声カード"
+ "name": "ALSEL監修 / お客様の声(カードグリッド)"
- "default": "お客様の声"
+ "default": "お客様の声(カードグリッド)"

- "name": "ALSEL監修 / レビュー横スクロール"
+ "name": "ALSEL監修 / お客様の声(横スクロール)"
- "default": "お客様の声"
+ "default": "お客様の声(横スクロール)"

- "default": "新商品"
+ "default": "新着商品"

- "default": "売れ筋ランキング"
+ "default": "売れ筋ランキング TOP10"
```

命名規則: `ALSEL監修 / <用途>(<UI バリエーション or 形式>)`
- UI バリエーション例: カードグリッド / 横スクロール / 表彰台型 TOP3 / アコーディオン / モーダル / スティッキー
- 形式例: TOP3 / TOP10 / 2カラム / 3カラム / 4カラム

---

## ルール 6: 短い 1 単語ラベルを単独で出さない

バッジに「期間」とだけ書いて赤背景で出すと、文章として読めなくなる。
前後関係なく単独で意味が通るレベルまで補完する。

NG → OK:
```diff
- <span class="alsel-seasonal-event__period-label">期間</span>
+ <span class="alsel-seasonal-event__period-label">期間限定</span>
```

- 「期間」→「期間限定」
- 「特典」→「特典あり」
- 「新着」→「新着商品」
- 「人気」→「人気商品」
- 「限定」→「期間限定」
- 「特集」→「特集企画」

---

## ルール 7: PC/モバイル切替系の default はガイド文に

`PC で見るキャッチコピー` のようなプレビュー前提文を default にすると、本番設置時に
違和感が出る。マーチャント向けガイド文にする。

NG → OK:
```diff
- "default": "PC で見るキャッチコピー"
+ "default": "PC 表示時のメインメッセージ"

- "default": "PC ではゆったり長めの説明文を表示できる。"
+ "default": "PC 表示時の説明文をここに入力します。"
```

---

## ルール 8: preset.blocks を必ず明示する

API 直投入(templates/index.json 経由)時に、テーマエディタの「Add section」経由で
自動展開される preset.blocks が渡されず、blocks 系セクションが「土台のみ」表示になる。

```json
{
  "presets": [
    {
      "name": "ALSEL監修 / ファーストビューLPヒーロー",
      "settings": {
        "heading": "毎日に、ちょっといいものを。",
        "subheading": "厳選された商品を、安心の品質でお届け。今だけのお得なキャンペーン実施中。"
      },
      "blocks": [
        { "type": "badge", "settings": { "value": "No.1", "label": "顧客満足度" } },
        { "type": "badge", "settings": { "value": "★4.8", "label": "平均レビュー" } },
        { "type": "badge", "settings": { "value": "10万本", "label": "累計販売実績" } }
      ]
    }
  ]
}
```

blocks ありセクションは必ず最低 2〜3 個のデモ blocks を preset に含める。

---

## Phase 6β 修正サマリ(参考)

| ルール | 影響ファイル数 | 修正内容 |
|---|---|---|
| 1. 文体「ですます」統一 | 13 | 「〜する。」→「〜します。」など 19 パターン |
| 2. 日付 default 遠未来 | 1 | countdown-timer end_year 2025→2099 |
| 3. blocks 空フォールバック | 2 | customer-review-card / review-carousel |
| 4. 画像なし時レイアウト | 1 | bulk-buy-offer に --no-image 切替 |
| 5. preset 名・default 見出し差別化 | 4 | customer-review-card / review-carousel / new-products-list / best-seller-ranking |
| 6. 短いラベル補完 | 1 | seasonal-event 「期間」→「期間限定」 |
| 7. PC/モバイル中立 default | 1 | hero-mobile PC 用見出し |
| 8. preset.blocks 明示 | 22 中該当 11 | 全 blocks ありセクションが対象 |
