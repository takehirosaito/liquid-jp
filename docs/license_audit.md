# 緊急ライセンス監査レポート

作成日時: 2026-05-13 23:00 ／ 対象: liquid-jp Phase 1〜3 で取得した全 685件の出典リポジトリ

> **判定基準(たけさん指示)**: 「迷ったらアウト側に倒す。グレーだが大丈夫そうは採用しない」

---

## 🚨 エグゼクティブサマリ

| 結論 | 件数 |
|---|---:|
| **アウト確定(LICENSE 本文に Shopify 制限句あり)** | **22件**(`Shopify/skeleton-theme` 1リポジトリ) |
| **要レビュー(SPDX 不一致だが本文は MIT 文言)** | **23件**(`freakdesign/shopify-code-snippets` 1リポジトリ) |
| **クリーン(LICENSE 本文が標準 MIT、制限句なし)** | **640件**(残り 10リポジトリ) |

**最重要発見:**
1. **`Shopify/skeleton-theme` は Dawn と完全に同一の制限句を含む**(Phase 1 で「MIT」と分類したのは GitHub SPDX 判定のみで、本文未確認だった)
2. **`Shopify/refresh` / `sense` / `craft` / `studio` / `origin` は GitHub にリポジトリ自体が公開されていない**(Theme Store の有料テーマで、ソースは Theme Store 内のみ。代替候補から除外)
3. **`Shopify/mcliquid-theme`、`Shopify/liquid`、`Shopify/theme-tools`、`Shopify/theme-liquid-docs` の 4本は LICENSE 本文に Shopify 制限句なし**、純粋 MIT 文言で安全

**推奨アクション(優先順):**
1. **`Shopify/skeleton-theme` の 22件を即削除**(本文の制限句が明確)
2. **`freakdesign/shopify-code-snippets` の 23件は たけさん判断**(SPDX NOASSERTION、ただし本文は標準 MIT。「迷ったらアウト」基準を厳格適用するなら削除推奨)
3. Phase 4 着手前に、上記削除を Meilisearch と translated_full.jsonl に反映
4. 代替候補は Shopify 公式テーマ(Refresh / Sense 等)を含めず、サードパーティ MIT/Apache 2.0 のみで再選定(Phase 4 で実調査)

---

## 1. 採用 12 リポジトリの判定結果

### 1.1 ❌ RESTRICTED: 削除対象

#### `Shopify/skeleton-theme`(取得 22 件、`MIT` ではない)

- ライセンス本文URL: <https://github.com/Shopify/skeleton-theme/blob/main/LICENSE.md>
- SPDX: `NOASSERTION`(GitHub の SPDX 検出が「カスタム制限あり」として MIT 判定を回避)
- 著作権者: Copyright (c) 2018-present Shopify Inc.

**該当条文(引用、強調は監査側):**

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software **without restriction**, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, sell and/or create derivative works of the Software or any part thereof, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> **The rights granted above may only be exercised to develop themes that integrate or interoperate with Shopify software or services, and, if applicable, to distribute, offer for sale or otherwise make available any such themes via the Shopify Theme Store. All other uses of the Software are strictly prohibited.**

**判定根拠:**
- 「Shopify ソフトウェアと統合するテーマ開発」と「Shopify Theme Store を通じた配布」のみが許諾範囲
- それ以外の用途は明示的に禁止(`strictly prohibited`)
- **第三者がリファレンスカタログとして再配布する用途は明確に禁止対象**
- Dawn と完全に同一の文言。Phase 1 で除外した Dawn と同等の扱いが正しい

**判定: ❌ アウト確定、22件 全件削除対象**

### 1.2 ⚠️ REVIEW: たけさん判断仰ぐ

#### `freakdesign/shopify-code-snippets`(取得 23 件、SPDX NOASSERTION)

- ライセンス本文URL: <https://github.com/freakdesign/shopify-code-snippets/blob/master/LICENSE>
- SPDX: `NOASSERTION`(GitHub の SPDX 検出が認識できないフォーマット)
- 著作権者: Copyright (c) **Jason Bowman**(個人)

**該当条文(引用):**

> Copyright (c) Jason Bowman
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software **without restriction**, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**判定根拠:**
- 本文は標準的な MIT ライセンス文言と完全一致(`without restriction`、`copy`、`modify`、`distribute`、`sublicense`、`sell` を許諾)
- 制限句なし、Shopify 制限なし
- SPDX が NOASSERTION なのは、年表記の欠落(`Copyright (c) Jason Bowman` だけで年がない)が原因と推定
- **法的には実質 MIT、再配布可能**

**判定の難しさ:**
- 「迷ったらアウト」基準を厳格適用するなら、SPDX 不一致は不採用要因。23件削除推奨
- 本文重視なら、これは MIT 相当で再配布可。残置 OK

**両論併記、たけさん判断仰ぐ:**
- **保守的判断(削除)**: 「SPDX が公式に MIT と認識していない」事実をもって除外。ALSEL 信用毀損リスク最小化
- **本文重視判断(残置)**: LICENSE 本文の意思は明確に MIT。Jason Bowman 個人著作で訴訟リスクも限定的

私の推奨は **削除側**(「迷ったらアウト」基準の精神)。

### 1.3 ✅ OK: クリーンな MIT(残置)

すべて LICENSE 本文に制限句なし、標準 MIT 文言。

| リポジトリ | 取得件数 | SPDX | 著作権者 | 備考 |
|---|---:|---|---|---|
| `Shopify/mcliquid-theme` | 9 | MIT | Shopify Inc. (2024-present) | Shopify 公式の Liquid 学習用ミニマルテーマ。Dawn とは別系統、純粋 MIT |
| `Shopify/liquid` | 35 | MIT | **Tobias Luetke** (2005, 2006) | Liquid エンジンの元祖。著作権者が Shopify Inc. ではなく Tobias 個人 |
| `Shopify/theme-tools` | 179 | MIT | Shopify Inc. (2022-present) | Liquid パーサー・リンター。fixtures に Liquid サンプル多数 |
| `Shopify/theme-liquid-docs` | 320 | MIT | Shopify Inc. (2022-present) | **本サイトのリファレンス根幹**(filters/tags/objects JSON)。MIT 純粋 |
| `kondasoft/ks-bootshop` | 73 | MIT | kondasoft | Bootstrap 5 ベースの完成テーマ |
| `mirceapiturca/Sections` | 5 | MIT | mirceapiturca | FAQ / Quiz / Tooltips 等の section 集 |
| `vikrantnegi/shopify-code-snippets` | 2 | MIT | vikrantnegi | pagination 系 2件のみ |
| `pgrimaud/shopify-snippets` | 7 | MIT | pgrimaud | SEO/JSON-LD 系 |
| `instantcommerce/shopify-headless-theme` | 5 | MIT | Instant Commerce | headless 用途 |
| `uicrooks/shopify-theme-lab` | 5 | MIT | uicrooks | テーマ開発フレーム |

**合計 OK: 640 件**

#### Shopify 公式リポでも残置できる根拠

`Shopify/mcliquid-theme`、`Shopify/liquid`、`Shopify/theme-tools`、`Shopify/theme-liquid-docs` は Shopify Inc. が著作権者だが、LICENSE 本文に **Shopify 制限句が含まれていない**。「Shopify 公式」というブランドではなく、**LICENSE 本文が法的拘束力を持つ**ため、これらは安全。

ただし、Phase 4 のフロントエンドで以下を明記する必要:
- 出典として「Shopify Inc. の MIT ライセンスソースを含む」を表示
- 各カード/ページに `repo_url` と `license` を表示(既に Meilisearch に保存済み)

---

## 2. 参考調査結果

### 2.1 既知の RESTRICTED(Phase 1 で除外済み、改めて確認)

| リポジトリ | LICENSE 状態 | 該当条文 |
|---|---|---|
| `Shopify/dawn` | RESTRICTED | skeleton-theme と完全に同一の制限句 |
| `Shopify/horizon` | RESTRICTED | skeleton-theme と完全に同一の制限句 |

両方とも Phase 1 で除外済み。今回の 685件には含まれていない(再確認 OK)。

### 2.2 公開されていない Shopify 公式テーマ

| リポジトリ | 状態 |
|---|---|
| `Shopify/refresh` | **GitHub に存在しない**(Theme Store の有料テーマ、ソース非公開) |
| `Shopify/sense` | 同上 |
| `Shopify/craft` | 同上 |
| `Shopify/studio` | 同上 |
| `Shopify/origin` | 同上 |

→ **これらはそもそも代替候補にならない**(取得手段なし)。たけさんが「Shopify 公式テーマは全部除外することを前提に」と書いた背景はおそらく Dawn / Horizon 経路と同じ制限句があることを想定していたが、それ以前にソース自体が非公開。

---

## 3. 影響度評価

### 3.1 削除パターン別の件数

| 削除パターン | 削除件数 | 残り件数 |
|---|---:|---:|
| **(A) skeleton-theme のみ削除** | 22 | **663** |
| **(B) skeleton-theme + freakdesign 両方削除(保守的)** | 45 | **640** |
| (現状維持・対応なし) | 0 | 685 (法的アウト) |

### 3.2 カテゴリ別の偏り(削除前後)

skeleton-theme 22件のカテゴリ内訳:
- ページテンプレート: 7
- テーマ基盤: 6
- コレクション/検索: 3
- UI部品: 2
- ヘッダー/フッター/ナビゲーション: 2
- カート/チェックアウト: 1
- 商品表示: 1

freakdesign 23件のカテゴリ内訳:
- コレクション/検索: 8(`sort-shopify-collection-products-by-inventory` 等の独創的実装例)
- ページテンプレート: 5
- API連携/JSON出力/JS統合: 4
- ユーティリティ: 2
- テーマ基盤: 2
- メタフィールド/メタオブジェクト: 1
- カート/チェックアウト: 1

**(A) パターン後の上位カテゴリ:**
- リファレンス/フィルター: 153
- ユーティリティ: 137
- リファレンス/オブジェクト: 137
- ページテンプレート: 49 ← skeleton 削除で 56→49
- テーマ基盤: 39 ← skeleton 削除で 45→39
- リファレンス/タグ: 30
- コレクション/検索: 28
- UI部品: 23
- 商品表示: 20
- ヘッダー/フッター/ナビゲーション: 15

### 3.3 「日本初の Shopify Liquid 日本語リファレンス」として公開する場合の影響

**(A) 22件削除のみ**(663件残):
- 影響軽微。リファレンス(filters/tags/objects)+ theme-tools の fixture が中心の構成は維持される
- 公式の最小テーマサンプル(page.liquid、cart.liquid 等)が一部欠ける
- 代替: `kondasoft/ks-bootshop`(73件)、`Shopify/mcliquid-theme`(9件)で類似機能をカバー可能
- **欠落領域: なし(致命的なものはない)**

**(B) 45件削除**(640件残、freakdesign も削除):
- ギフトカード金額別画像、複数404キャッシュ、マルチドメイン分岐などの**独創的実装例が消える**
- ただし「公式リファレンス + コミュニティ完成テーマ」という基本構造は維持される
- **欠落領域**: 「実務でよくある独創的 Tips」のセクションが薄くなる(主に freakdesign が担っていた)

### 3.4 公開判断

**(A) パターンで 663件公開は十分実現可能。** リファレンス系 320件、theme-tools の fixture 179件、コミュニティテーマ 100件超の構成で「日本初の Shopify Liquid 日本語リファレンス」を名乗るに足る。Phase 4 で追加リポを選定すれば 700〜800件規模に増強可能。

---

## 4. 次の方針提案

### 4.1 即時対応(Phase 4 着手前)

1. **`Shopify/skeleton-theme` の 22件を削除**(`docs/records_to_remove.md` に id 一覧)
2. **`freakdesign` 23件をたけさん判断で削除 or 残置**
3. 削除確定後:
   - `data/translated_full.jsonl` から該当行除去 → `.bak` で backup
   - `data/meili_index.jsonl` 再生成
   - Meilisearch reset 再投入(683件 → 663件 or 640件)
   - `docs/phase2-full.md` 再生成

### 4.2 中期対応(代替リポジトリ候補、Phase 4 開始時に再調査推奨)

Shopify 公式テーマ(Refresh / Sense / Craft / Studio / Origin)は **そもそも GitHub にソース公開されていない** ため、代替は **サードパーティの MIT/Apache 2.0 リポジトリ**から探す必要がある。私の事前知識ベースで提案できる候補:

| カテゴリ | 候補 | 想定取得件数 | 備考 |
|---|---|---:|---|
| 完成テーマ | `kondasoft/ks-eclipse`(同作者の別テーマ) | ~50 | kondasoft は ks-bootshop で MIT 確認済み、姉妹リポの可能性 |
| 完成テーマ | `archetype-themes/expanse`(要存在確認) | ~30 | Theme Forest 系老舗、ライセンス要確認 |
| スニペット集 | `csaltos/shopify-snippets`(要存在確認) | ~20 | コミュニティ作 |
| Hydrogen 例 | `Shopify/hydrogen` の demo/examples | ~10 | Liquid ではないが Storefront 連携の参考 |

**注: これらは私の事前調査ベースの推定。Phase 4 開始時に WebFetch で実物 LICENSE 確認が必須。**

### 4.3 公開時のアテンション文言(Phase 4 のサイト構築タスク)

サイトのフッター / 利用規約 / 各カード詳細ページに以下を明示する必要がある:

```
本サイトに掲載されているコードは、各リポジトリの MIT ライセンスに基づき
日本語化・再配布しています。原本の著作権は各著作者が保有します。
日本語訳テキストは ALSEL の著作物として CC-BY 4.0 で公開しています。
```

各カードに `repo_owner` / `repo_name` / `license` / `raw_url` を表示する仕様は既に Meilisearch のスキーマで対応済み(`displayedAttributes` に含む)。

---

## 5. 監査の制約・残存リスク

1. **theme-tools の fixture(179件)**: テスト用フィクスチャを「コードカタログ」として再配布することは LICENSE 上は OK だが、**「使いやすい実装例」として打ち出すには違和感**がある(理由: テストケースのため、実用品としての完成度が低い)。Phase 4 でフロントエンド側で「fixture 系はカテゴリを分けて表示」検討推奨
2. **theme-liquid-docs の filters.json 等(320件)**: Shopify Inc. 著作の公式仕様データを日本語化することは LICENSE 上 OK だが、**Shopify 公式ドキュメントとの差別化**(なぜここで日本語版を見るのか)が問われる可能性。Phase 4 で UX 設計時に意識
3. **本監査は LICENSE 本文に基づく判定で、商標・パブリシティ権・契約上の制限は別評価**。Shopify ロゴ・「Shopify」商標の表示は引き続き避ける(Phase 1 方針通り)

---

## 6. 関連ドキュメント

- `docs/records_to_remove.md` — 削除対象 id 一覧(skeleton-theme 22件、freakdesign 23件)
- `data/license_audit_raw.json` — 全リポの LICENSE 本文 raw データ(再現可能性)
- `data/translated_full.jsonl.before_license_audit.bak` — 削除前バックアップ(削除実行後に作成予定)

---

## 7. たけさん判断仰ぐ事項(朝の確認)

1. **`freakdesign/shopify-code-snippets` 23件をどうするか**
   - (a) 削除する(「迷ったらアウト」厳格適用)
   - (b) 残置(LICENSE 本文重視)
   - (c) Jason Bowman 本人に Twitter/GitHub Issue で確認(時間かかる)
2. **削除実行のタイミング**
   - (a) 即時(私が今夜中に実行可)
   - (b) 朝の判断後
3. **Phase 4 を進めるか、追加リポジトリ調査を優先するか**
   - 現状の 663件(または 640件)で Phase 4 着手し、追加リポは並行調査
