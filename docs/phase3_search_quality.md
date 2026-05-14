# Phase 3 ブロック1: 検索品質の実機確認

対象: Meilisearch on Railway / index `liquid_jp` / 投入 683 docs

## クエリ: `カート` (推定 452 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 0.999 | カートページの | `cart.liquid` | カート/チェックアウト |
| 2 | 0.999 | カートページテンプレート | `cart.liquid` | ページテンプレート |
| 3 | 0.999 | カートドロワー | `offcanvas-cart.liquid` | カート/チェックアウト |
| 4 | 0.999 | カート注文備考欄 | `cart-note.liquid` | カート/チェックアウト |
| 5 | 0.999 | カートフッターの割引・小計・チェックアウト | `cart-footer.liquid` | カート/チェックアウト |

## クエリ: `コレクション内ソート` (推定 121 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 0.976 | コレクション商品を在庫数でソート | `sort-shopify-collection-products-by-inventory.liquid` | コレクション/検索 |
| 2 | 0.975 | コレクション商品をメタフィールドで並べ替え | `sort-shopify-collection-products-by-metafield-value.liquid` | コレクション/検索 |
| 3 | 0.975 | メタフィールド値で商品を並べ替え | `sort-shopify-collection-products-by-metafield-value-commentless.liquid` | コレクション/検索 |
| 4 | 0.975 | collection オブジェクト | `collection` | リファレンス/オブジェクト |
| 5 | 0.864 | コレクションページの商品一覧 | `collection.liquid` | コレクション/検索 |

## クエリ: `商品バリエーション` (推定 283 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 0.995 | swatch オブジェクト | `swatch` | リファレンス/オブジェクト |
| 2 | 0.649 | カートページの商品一覧と数量更新 | `cart.liquid` | ページテンプレート |
| 3 | 0.649 | カートページの商品一覧・チェックアウト | `cart.liquid` | ページテンプレート |
| 4 | 0.647 | Organization・WebSite・Product・Article構造化データ | `rich-snippets.liquid` | SEO/構造化データ |
| 5 | 0.645 | divided_by フィルター（数値を割算） | `divided_by` | リファレンス/フィルター |

## クエリ: `カスタム404` (推定 99 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 0.988 | template オブジェクト | `template` | リファレンス/オブジェクト |
| 2 | 0.966 | メタフィールド値で商品を並べ替え | `sort-shopify-collection-products-by-metafield-value-commentless.liquid` | コレクション/検索 |
| 3 | 0.906 | 複数商品のレビュー一覧表示 | `get-reviews.liquid` | API連携/JSON出力/JS統合 |
| 4 | 0.902 | Liquidコード整形テストケース集 | `fixed.liquid` | ユーティリティ |
| 5 | 0.895 | お問い合わせフォーム | `contact-form.liquid` | ページテンプレート |

## クエリ: `ページネーション` (推定 306 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 1.000 | ページネーション | `pagination.liquid` | コレクション/検索 |
| 2 | 1.000 | ページネーションの表示 | `pagination-tabs.liquid` | コレクション/検索 |
| 3 | 1.000 | ページネーションの現在位置表示 | `pagination-count.liquid` | コレクション/検索 |
| 4 | 1.000 | ページネーション件数のカート属性による動的変更 | `dynamic-pagination.liquid` | コレクション/検索 |
| 5 | 1.000 | ページネーション件数の動的セレクトボックス | `dynamic-pagination-select.liquid` | コレクション/検索 |

## クエリ: `在庫切れ` (推定 33 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 0.993 | コレクション商品を在庫数でソート | `sort-shopify-collection-products-by-inventory.liquid` | コレクション/検索 |
| 2 | 0.988 | 商品バリアントのラジオボタン | `index.liquid` | 商品表示 |
| 3 | 0.987 | break タグ（ループの中断） | `break` | リファレンス/タグ |
| 4 | 0.987 | break タグ（ループ脱出） | `index.liquid` | ユーティリティ |
| 5 | 0.702 | ceil フィルター（数値を切り上げ） | `ceil` | リファレンス/フィルター |

## クエリ: `日付フォーマット` (推定 75 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 0.998 | 日付文字列の多言語翻訳 | `date-translate.liquid` | ユーティリティ |
| 2 | 0.986 | ブログページのテンプレート | `blog.liquid` | ページテンプレート |
| 3 | 0.963 | time_tag フィルター（タイムスタンプをHTMLの時刻要素に変換） | `time_tag` | リファレンス/フィルター |
| 4 | 0.955 | gift_card オブジェクト | `gift_card` | リファレンス/オブジェクト |
| 5 | 0.906 | date フィルター（日付を指定形式でフォーマット） | `date` | リファレンス/フィルター |

## クエリ: `ヘッダー` (推定 90 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 0.999 | ストアヘッダーのレイアウト | `header.liquid` | ヘッダー/フッター/ナビゲーション |
| 2 | 0.999 | デスクトップヘッダーのアイコンメニュー | `navbar-desktop-icons.liquid` | ヘッダー/フッター/ナビゲーション |
| 3 | 0.999 | ストアヘッダー | `header.liquid` | ヘッダー/フッター/ナビゲーション |
| 4 | 0.999 | ヘッダーのレイアウト構造 | `fixed.liquid` | ヘッダー/フッター/ナビゲーション |
| 5 | 0.990 | セクション共通ヘッダー（タイトル・説明文） | `section-header.liquid` | UI部品 |

## クエリ: `検索ボックス` (推定 226 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 0.997 | サイト検索のWebSite構造化データ | `json-ld-search.liquid` | SEO/構造化データ |
| 2 | 0.996 | 予測検索結果の表示 | `predictive-search.liquid` | コレクション/検索 |
| 3 | 0.993 | predictive_search オブジェクト | `predictive_search` | リファレンス/オブジェクト |
| 4 | 0.899 | filter オブジェクト | `filter` | リファレンス/オブジェクト |
| 5 | 0.895 | ページネーション件数の動的セレクトボックス | `dynamic-pagination-select.liquid` | コレクション/検索 |

## クエリ: `メタフィールド` (推定 88 件)

| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |
|---|---:|---|---|---|
| 1 | 1.000 | 商品バッジの色付けメタフィールド表示 | `product-custom-badge.liquid` | メタフィールド/メタオブジェクト |
| 2 | 1.000 | メタフィールドから関連記事を取得・表示 | `related-articles.liquid` | メタフィールド/メタオブジェクト |
| 3 | 1.000 | メタフィールド値で商品を並べ替え | `sort-shopify-collection-products-by-metafield-value-commentless.liquid` | コレクション/検索 |
| 4 | 1.000 | metafield_tag フィルター（メタフィールドを HTML タグに変換） | `metafield_tag` | リファレンス/フィルター |
| 5 | 1.000 | metafield_text フィルター（メタフィールドをテキスト形式で抽出） | `metafield_text` | リファレンス/フィルター |
