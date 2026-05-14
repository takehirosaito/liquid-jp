# liquid-jp.jp Phase 1 サンプル50件レポート (v2: プロンプト改修版)

生成日時: 2026-05-13 20:54 ／ モデル: `claude-haiku-4-5-20251001`

## サマリ

- 件数: **50件**（成功 50 / 失敗 0）
  - コミュニティスニペット: **40件**
  - 公式リファレンス（theme-liquid-docs）: **10件**
- 処理時間: 34.8秒（並列 8）
- API コスト: **$0.2280**（入力 122,429 tok ＋ 出力 21,116 tok)

### カテゴリ分布

| カテゴリ | 件数 |
|---|---:|
| ページテンプレート | 10 |
| UI部品 | 5 |
| ヘッダー/フッター/ナビゲーション | 4 |
| テーマ基盤 | 4 |
| リファレンス/フィルター | 4 |
| ユーティリティ | 3 |
| 商品表示 | 3 |
| API連携/JSON出力/JS統合 | 3 |
| SEO/構造化データ | 3 |
| コレクション/検索 | 3 |
| リファレンス/タグ | 3 |
| リファレンス/オブジェクト | 3 |
| 顧客アカウント | 1 |
| メタフィールド/メタオブジェクト | 1 |

### 難易度分布

| 難易度 | 件数 |
|---|---:|
| 初級 | 31 |
| 中級 | 17 |
| 上級 | 2 |

### リポジトリ別件数

| リポジトリ | 件数 |
|---|---:|
| theme-liquid-docs | 10 |
| skeleton-theme | 6 |
| shopify-code-snippets | 6 |
| ks-bootshop | 6 |
| shopify-theme-lab | 5 |
| mcliquid-theme | 5 |
| shopify-snippets | 5 |
| shopify-headless-theme | 4 |
| Sections | 3 |

## レビュー観点（たけさん向け）

1. **日本語訳の品質** — 自然な日本語か、誤訳・直訳が残っていないか
2. **カテゴリ分類** — 新カテゴリ体系で適切に分類できているか、誤分類がないか
3. **タイトルフォーマット** — リファレンスは「名前 種別（用途）」、スニペットは「スニペット」「セクション」後置なしを守れているか
4. **タグの命名規則** — 小文字ハイフン区切り・単数形・同義語正規化が効いているか、category と重複していないか
5. **caveats の品質** — 「〜が必要です」連発がないか、①前提→②落とし穴→③応用注意の構成か、具体策が書けているか
6. **include / render 対応** — 原文が include を使っているスニペットで render 推奨の注記が入っているか

---

## 📘 公式リファレンス サンプル

### 1. 📘 リファレンス sort_by フィルター（コレクションの商品ソート順序URL生成）

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `collection` `url-generation` `sorting` `liquid-filter`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** コレクションURLにソート順序パラメータを追加します。手動、売上、価格、作成日など複数のソート方法に対応しており、コレクションページのURL生成に使用します。

**用途:** コレクションページで「人気順」「価格が安い順」などのソートリンクを作成する際に使用。フィルタリングUIやソート順序切替ボタンの href 属性に組み込みます。

**設置場所:** コレクションテンプレート（collection.liquid）やコレクション関連の UI 部品で、`{{ collection.url | sort_by: 'best-selling' }}` の形で `collection.url` に対して適用します。

**注意点:** このフィルターは `collection.url` に対してのみ使用可能です。使用できるソート値は manual（コレクション設定に従う）、best-selling、title-ascending/descending、price-ascending/descending、created-ascending/descending の8種類に限定されます。`url_for_type` や `url_for_vendor` フィルターと組み合わせて使うこともできます。

<details><summary>コード(30行)を見る</summary>

```json
{
  "category": "collection",
  "deprecated": false,
  "deprecation_reason": "",
  "description": "Accepts the following values:\n\n- `manual` (as defined in the [collection settings](https://help.shopify.com/manual/products/collections/collection-layout#change-the-sort-order-for-the-products-in-a-collection))\n- `best-selling`\n- `title-ascending`\n- `title-descending`\n- `price-ascending`\n- `price-descending`\n- `created-ascending`\n- `created-descending`\n\n&gt; Tip:\n&gt; You can append the `sort_by` filter to the [`url_for_type`](/docs/api/liquid/filters/url_for_type)\n&gt; and [`url_for_vendor`](/docs/api/liquid/filters/url_for_vendor) filters.",
  "parameters": [],
  "return_type": [
    {
      "type": "string",
      "name": "",
      "description": "",
      "array_value": ""
    }
  ],
  "examples": [
    {
      "name": "",
      "description": "",
      "syntax": "",
      "path": "/collections/sale-potions",
      "raw_liquid": "{{ collection.url | sort_by: 'best-selling' }}",
      "parameter": false,
      "display_type": "text",
      "show_data_tab": true
    }
  ],
  "summary": "Generates a collection URL with the provided `sort_by` parameter appended.\nThis filter must be applied to the object property [`collection.url`](https://shopify.dev/docs/api/liquid/objects/collection#collection-url).",
  "syntax": "string | sort_by: string",
  "name": "sort_by"
}
```

</details>


### 2. 📘 リファレンス escape フィルター（HTML特殊文字をエスケープ）

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `html-escaping` `security` `string-manipulation` `xss-prevention`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** HTML の特殊文字（`<`、`>`、`&`、シングルクォート等）をエスケープシーケンスに変換します。エスケープシーケンスが存在しない文字は変換されません。

**用途:** ユーザー入力やメタデータをHTML内に安全に出力するとき、XSS対策として使用します。テンプレートで顧客情報やカスタムテキストを展開する際に有効です。

**設置場所:** Liquidテンプレート内で `{{ value | escape }}` の形で使用します。product.title、customer.name など、任意の変数やリテラル文字列に適用できます。

**注意点:** JavaScriptコンテキストやURL属性内では別途対応が必要です。このフィルターはHTML本体のテキストノード向けであり、属性値やスクリプト内での安全性は保証しません。既にエスケープ済みの文字列に再度適用するとダブルエスケープになるため注意してください。

<details><summary>コード(30行)を見る</summary>

```json
{
  "category": "string",
  "deprecated": false,
  "deprecation_reason": "",
  "description": "",
  "parameters": [],
  "return_type": [
    {
      "type": "string",
      "name": "",
      "description": "",
      "array_value": ""
    }
  ],
  "examples": [
    {
      "name": "",
      "description": "",
      "syntax": "",
      "path": "/",
      "raw_liquid": "{{ '&lt;p&gt;Text to be escaped.&lt;/p&gt;' | escape }}",
      "parameter": false,
      "display_type": "text",
      "show_data_tab": true
    }
  ],
  "summary": "Escapes special characters in HTML, such as `&lt;&gt;`, `'`, and `&amp;`, and converts characters into escape sequences. The filter doesn't effect characters within the string that don’t have a corresponding escape sequence.\".",
  "syntax": "string | escape",
  "name": "escape"
}
```

</details>


### 3. 📘 リファレンス floor フィルター（数値を下方丸めして整数化）

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `math` `number` `rounding` `filter`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** 与えられた数値を下方丸めして、以下の最も近い整数に変換します。小数点以下の値を切り捨てる必要があるときに使用します。

**用途:** 商品の在庫数や割引率など、小数が発生した数値を整数に統一する場面、または計算結果の小数部を切り捨てたい場合に活用できます。

**設置場所:** Liquid テンプレート内で `{{ 数値 | floor }}` の形で使用します。商品ページ、コレクションページ、カート画面など、数値を表示する箇所で利用できます。

**注意点:** 負の数に対しても下方丸めが適用されるため、-1.5 は -2 になります。金額計算で使う場合は四捨五入（round フィルター）との使い分けに注意してください。

<details><summary>コード(30行)を見る</summary>

```json
{
  "category": "math",
  "deprecated": false,
  "deprecation_reason": "",
  "description": "",
  "parameters": [],
  "return_type": [
    {
      "type": "number",
      "name": "",
      "description": "",
      "array_value": ""
    }
  ],
  "examples": [
    {
      "name": "",
      "description": "",
      "syntax": "",
      "path": "/",
      "raw_liquid": "{{ 1.2 | floor }}",
      "parameter": false,
      "display_type": "text",
      "show_data_tab": true
    }
  ],
  "summary": "Rounds a number down to the nearest integer.",
  "syntax": "number | floor",
  "name": "floor"
}
```

</details>


### 4. 📘 リファレンス link_to_type フィルター（商品タイプで絞られたコレクションへのリンク生成）

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `filter` `collection` `product-type` `link-generation` `html`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、48行）
- **ファイル:** `data/filters.json`

**説明:** 商品タイプを指定して、そのタイプに属するすべての商品を表示するコレクションページへのリンク（HTMLの`<a>`タグ）を生成します。

**用途:** 商品詳細ページやコレクションページで、同じ商品タイプの他の商品を閲覧できるようにリンクを表示したいとき。

**設置場所:** 商品情報を表示するセクション内（product.liquid、collection.liquid など）で `{{ 商品タイプの値 | link_to_type }}` の形で使用します。HTMLクラスなどの属性は `{{ value | link_to_type: class: 'link-class' }}` のように追加できます。

**注意点:** このフィルターは有効な商品タイプ値を渡す必要があります。HTML属性を指定する場合、属性名と値はコロン区切りで記述し、標準HTMLの属性であることを確認してください（カスタム属性は使用不可）。

<details><summary>コード(48行)を見る</summary>

```json
{
  "category": "collection",
  "deprecated": false,
  "deprecation_reason": "",
  "description": "",
  "parameters": [
    {
      "description": "attribute [string] You can specify the value of supported [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes).",
      "name": "HTML",
      "positional": true,
      "required": false,
      "types": []
    }
  ],
  "return_type": [
    {
      "type": "string",
      "name": "",
      "description": "",
      "array_value": ""
    }
  ],
  "examples": [
    {
      "name": "",
      "description": "",
      "syntax": "",
      "path": "/",
      "raw_liquid": "{{ 'Health' | link_to_type }}",
      "parameter": false,
      "display_type": "text",
      "show_data_tab": true
    },
    {
      "name": "HTML attributes",
      "description": "You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attributes) by including a parameter that matches the attribute name, and the desired value.\n",
      "syntax": "string | link_to_type: attribute: string",
      "path": "/",
      "raw_liquid": "{{ 'Health' | link_to_type: class: 'link-class' }}",
      "parameter": true,
... (以下 8 行省略)
```

</details>


### 5. 📘 リファレンス decrement タグ（変数をカウントダウン）

**カテゴリ:** リファレンス/タグ ／ **難易度:** 初級 ／ **タグ:** `variable` `counter` `decrement`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、28行）
- **ファイル:** `data/tags.json`

**説明:** 新しい変数を初期値 -1 で作成し、呼び出すたびに 1 ずつ減少させます。同じファイル内のスニペットで共有されます。

**用途:** カウンター機能が必要な場面、例えばループ内で逆順の番号を付与したい場合や、要素の減少をトラッキングする場面で使用します。

**設置場所:** テンプレートやセクションのLiquidコード内で `{% decrement 変数名 %}` の形で使用します。同じファイル内に含まれるスニペットでも同じ変数が共有されます。

**注意点:** decrement で作成した変数は assign や capture で作成したものとは独立していますが、increment タグとは変数を共有します。Liquid の定義済みオブジェクト名（product、collection など）と同じ変数名を使うとオブジェクトが上書きされるため、変数名は必ず固有のものを設定してください。

<details><summary>コード(28行)を見る</summary>

```json
{
  "category": "variable",
  "deprecated": false,
  "deprecation_reason": "",
  "description": "Variables that are declared with `decrement` are unique to the [layout](/themes/architecture/layouts), [template](/themes/architecture/templates),\nor [section](/themes/architecture/sections) file that they're created in. However, the variable is shared across\n[snippets](/themes/architecture/snippets) included in the file.\n\nSimilarly, variables that are created with `decrement` are independent from those created with [`assign`](/docs/api/liquid/tags/assign)\nand [`capture`](/docs/api/liquid/tags/capture). However, `decrement` and [`increment`](/docs/api/liquid/tags/increment) share\nvariables.",
  "parameters": [],
  "summary": "Creates a new variable, with a default value of -1, that's decreased by 1 with each subsequent call.\n\n&gt; Caution:\n&gt; Predefined Liquid objects can be overridden by variables with the same name.\n&gt; To make sure that you can access all Liquid objects, make sure that your variable name doesn't match a predefined object's name.",
  "name": "decrement",
  "syntax": "{% decrement variable_name %}",
  "syntax_keywords": [
    {
      "keyword": "variable_name",
      "description": "The name of the variable being decremented."
    }
  ],
  "examples": [
    {
      "name": "",
      "description": "",
      "syntax": "",
      "path": "/",
      "raw_liquid": "{% decrement variable %}\n{% decrement variable %}\n{% decrement variable %}",
      "parameter": false,
      "display_type": "text",
      "show_data_tab": true
    }
  ]
}
```

</details>


### 6. 📘 リファレンス for タグ（配列の要素をループ処理）

**カテゴリ:** リファレンス/タグ ／ **難易度:** 初級 ／ **タグ:** `loop` `iteration` `array` `pagination`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、113行）
- **ファイル:** `data/tags.json`

**説明:** 配列の各要素に対して式を繰り返し実行します。limit、offset、range、reversed パラメータで反復の範囲と順序を制御できます。

**用途:** 商品一覧やコレクションページで複数の商品を表示したい場合、または特定の数だけ項目を表示したい場合に使用します。

**設置場所:** Liquid テンプレート（.liquid ファイル）内で `{% for 変数 in 配列 %}～{% endfor %}` の形式で記述します。

**注意点:** 1回のループで最大50イテレーションまでの制限があります。51項目以上のデータを処理する場合は paginate タグで複数ページに分割してください。limit パラメータより paginate を使うことで、サーバー側のデータ取得を最適化できます。

<details><summary>コード(113行)を見る</summary>

```json
{
  "category": "iteration",
  "deprecated": false,
  "deprecation_reason": "",
  "description": "You can do a maximum of 50 iterations with a `for` loop. If you need to iterate over more than 50 items, then use the\n[`paginate` tag](/docs/api/liquid/tags/paginate) to split the items over multiple pages.\n\n&gt; Tip:\n&gt; Every `for` loop has an associated [`forloop` object](/docs/api/liquid/objects/forloop) with information about the loop.",
  "parameters": [
    {
      "description": "The number of iterations to perform.",
      "name": "limit",
      "positional": false,
      "required": false,
      "types": [
        "number"
      ]
    },
    {
      "description": "The 1-based index to start iterating at.",
      "name": "offset",
      "positional": false,
      "required": false,
      "types": [
        "number"
      ]
    },
    {
      "description": "A custom numeric range to iterate over.",
      "name": "range",
      "positional": true,
      "required": false,
      "types": [
        "untyped"
      ]
    },
    {
      "description": "Iterate in reverse order.",
      "name": "reversed",
      "positional": true,
      "required": false,
      "types": [
        "untyped"
... (以下 73 行省略)
```

</details>


### 7. 📘 リファレンス else タグ（ループが空の場合のフォールバック）

**カテゴリ:** リファレンス/タグ ／ **難易度:** 初級 ／ **タグ:** `control-flow` `iteration` `loop` `empty-state`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、40行）
- **ファイル:** `data/tags.json`

**説明:** for ループの配列が0件の場合に実行される条件式を指定します。商品なし、検索結果なし、などの空状態の表示を簡潔に制御できます。

**用途:** コレクション、検索結果、カート内商品一覧などで、該当データがない時にメッセージや代替コンテンツを表示する場合。

**設置場所:** {% for %} ループの内部に {% else %} ... {% endfor %} の形で記述します。メインテンプレートやセクションの Liquid コード内で使用。

**注意点:** else ブロックは for ループ全体が空（イテレーション0回）のときだけ実行されます。1回以上ループが実行された場合は無視されます。if/unless タグの else とは異なり、for のみで使用可能。

<details><summary>コード(40行)を見る</summary>

```json
{
  "category": "iteration",
  "deprecated": false,
  "deprecation_reason": "",
  "description": "",
  "parameters": [],
  "summary": "Allows you to specify a default expression to execute when a [`for` loop](/docs/api/liquid/tags/for) has zero length.",
  "name": "else",
  "syntax": "{% for variable in array %}\n  first_expression\n{% else %}\n  second_expression\n{% endfor %}",
  "syntax_keywords": [
    {
      "keyword": "variable",
      "description": "The current item in the array."
    },
    {
      "keyword": "array",
      "description": "The array to iterate over."
    },
    {
      "keyword": "first_expression",
      "description": "The expression to render for each iteration."
    },
    {
      "keyword": "second_expression",
      "description": "The expression to render if the loop has zero length."
    }
  ],
  "examples": [
    {
      "name": "",
      "description": "",
      "syntax": "",
      "path": "/collections/empty",
      "raw_liquid": "{% for product in collection.products %}\n  {{ product.title }}&lt;br&gt;\n{% else %}\n  There are no products in this collection.\n{% endfor %}",
      "parameter": false,
      "display_type": "text",
      "show_data_tab": true
    }
  ]
}
```

</details>


### 8. 📘 リファレンス measurement オブジェクト

**カテゴリ:** リファレンス/オブジェクト ／ **難易度:** 初級 ／ **タグ:** `metafield` `measurement` `product`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、86行）
- **ファイル:** `data/objects.json`

**説明:** メタフィールドの計測値型（寸法・容量・重量）から取得した計測データを保持するオブジェクト。計測値、単位、種別の3つのプロパティを備えています。

**用途:** 商品の寸法や容量、重量などを構造化データとして商品ページに表示する際に使用します。例えば牛乳パックの容量や衣料品のサイズなどを統一フォーマットで出力できます。

**設置場所:** メタフィールド値として measurement 型を設定した際に、Liquid テンプレート内で `{{ product.metafields.namespace.key.value.type }}` や `{{ product.metafields.namespace.key.value.value }}` の形式で各プロパティにアクセスします。

**注意点:** measurement オブジェクトは metafield の value プロパティを通じてのみアクセス可能です。事前に管理画面でメタフィールドの型を dimension、volume、weight のいずれかに設定する必要があります。unit プロパティの値はメタフィールド定義時に指定した単位に依存するため、出力前に想定値をテストしてください。

<details><summary>コード(86行)を見る</summary>

```json
{
  "access": {
    "global": false,
    "parents": [
      {
        "object": "metafield",
        "property": "value"
      }
    ],
    "template": []
  },
  "deprecated": false,
  "deprecation_reason": "",
  "description": "&gt; Tip:\n&gt; To learn about metafield types, refer to [Metafield types](/apps/metafields/types).",
  "properties": [
    {
      "deprecated": false,
      "deprecation_reason": "",
      "description": "",
      "examples": [],
      "return_type": [
        {
          "type": "string",
          "name": "dimension",
          "description": "",
          "array_value": ""
        },
        {
          "type": "string",
          "name": "volume",
          "description": "",
          "array_value": ""
        },
        {
          "type": "string",
          "name": "weight",
          "description": "",
          "array_value": ""
        }
      ],
... (以下 46 行省略)
```

</details>


### 9. 📘 リファレンス model_source オブジェクト

**カテゴリ:** リファレンス/オブジェクト ／ **難易度:** 中級 ／ **タグ:** `3d-model` `product` `media` `object-property`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、74行）
- **ファイル:** `data/objects.json`

**説明:** 3D モデルのソースファイル情報を表すオブジェクト。ファイル形式、MIME タイプ、CDN URL にアクセスできます。

**用途:** 商品の 3D モデルビューアを実装する際、モデルファイルの形式と URL を取得して WebGL や AR ビューアに渡すシーンで使用します。

**設置場所:** `product.featured_media.sources[0].format`、`product.featured_media.sources[0].mime_type`、`product.featured_media.sources[0].url` の形で、商品テンプレートや商品カード内で Liquid から参照します。

**注意点:** model_source は model オブジェクトの sources 配列内に格納されます。sources が存在する場合のみアクセス可能なので、事前に `if product.featured_media.sources` で存在確認してから参照してください。

<details><summary>コード(74行)を見る</summary>

```json
{
  "access": {
    "global": false,
    "parents": [
      {
        "object": "model",
        "property": ""
      }
    ],
    "template": []
  },
  "deprecated": false,
  "deprecation_reason": "",
  "description": "",
  "properties": [
    {
      "deprecated": false,
      "deprecation_reason": "",
      "description": "",
      "examples": [],
      "return_type": [
        {
          "type": "string",
          "name": "",
          "description": "",
          "array_value": ""
        }
      ],
      "summary": "The format of the model source file.",
      "name": "format"
    },
    {
      "deprecated": false,
      "deprecation_reason": "",
      "description": "",
      "examples": [],
      "return_type": [
        {
          "type": "string",
          "name": "",
... (以下 34 行省略)
```

</details>


### 10. 📘 リファレンス remote_details オブジェクト

**カテゴリ:** リファレンス/オブジェクト ／ **難易度:** 中級 ／ **タグ:** `remote-product` `multi-vendor` `marketplace` `object-property`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、69行）
- **ファイル:** `data/objects.json`

**説明:** 外部ストアから取得した商品など、リモートソースから来たオブジェクトの出典情報を保持します。出典のコンテキスト（現在は「seller」のみ）と、元のストア情報にアクセスできます。

**用途:** マルチベンダー機能やマーケットプレイス機能で、他店舗の商品を表示する際に、その商品の出元ストア情報を表示したい場合に使用します。

**設置場所:** Liquid 内で `{{ remote_product.remote_details.type }}` または `{{ remote_product.remote_details.shop }}` の形で参照します。remote_product オブジェクトがある箇所で利用可能です。

**注意点:** このオブジェクトは remote_product からのみアクセス可能で、通常の product オブジェクトからは参照できません。type プロパティは現在「seller」のみ対応していますが、将来的に値が拡張される可能性があるため、条件分岐では明示的に値をチェックするのが安全です。

<details><summary>コード(69行)を見る</summary>

```json
{
  "access": {
    "global": false,
    "parents": [
      {
        "object": "remote_product",
        "property": ""
      },
      {
        "object": "remote_product",
        "property": "remote_details"
      }
    ],
    "template": []
  },
  "deprecated": false,
  "deprecation_reason": "",
  "description": "Remote details can only be accessed on an object that comes from a remote source,\nsuch as a product from another store.",
  "properties": [
    {
      "deprecated": false,
      "deprecation_reason": "",
      "description": "",
      "examples": [],
      "return_type": [
        {
          "type": "string",
          "name": "",
          "description": "",
          "array_value": ""
        }
      ],
      "summary": "Provides context on how the remote object was surfaced.\nCurrently the only supported value is \"seller\", but this may be expanded in the future.",
      "name": "type"
    },
    {
      "deprecated": false,
      "deprecation_reason": "",
      "description": "",
      "examples": [],
... (以下 29 行省略)
```

</details>


---

## 🧩 コミュニティスニペット サンプル（40件）

### 1. 🧩 スニペット ページセクション（固定ページの基本レイアウト）

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `page` `template` `section`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/page.liquid) （ライセンス: MIT、18行）
- **ファイル:** `sections/page.liquid`

**説明:** ストアの固定ページ（About Us、Contact Us など）をレンダリングするセクション。ページタイトルと本文コンテンツを表示します。

**用途:** page テンプレートで使用される基本セクション。管理画面で作成した固定ページの内容を表示するときに使用します。

**設置場所:** sections/page.liquid として保存し、templates/page.liquid の {% section 'page' %} で呼び出します。

**注意点:** ページタイトルと本文のレイアウトが最小限のため、スタイリングは別途 CSS で定義する必要があります。メタフィールドを活用する場合は page.metafields で追加フィールドにアクセスできます。

<details><summary>コード(18行)を見る</summary>

```liquid
{% comment %}
  This section is used in the page template to render store pages like About us
  or Contact us.

  https://shopify.dev/docs/storefronts/themes/architecture/templates/page
{% endcomment %}

<h1>{{ page.title }}</h1>

{{ page.content }}

{% schema %}
{
  "name": "t:general.page",
  "settings": []
}
{% endschema %}
```

</details>


### 2. 🧩 スニペット ドメイン判定で画像を切り替え

**カテゴリ:** ユーティリティ ／ **難易度:** 初級 ／ **タグ:** `request-object` `conditional-logic` `multi-domain` `asset-management`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Get current domain name with Liquid/request_host.liquid) （ライセンス: MIT、15行）
- **ファイル:** `Get current domain name with Liquid/request_host.liquid`

**説明:** request.host を使用して、アクセス元のドメインを判定し、異なるバナー画像を表示します。複数ドメインの運用時に、ドメインごとに異なるビジュアルコンテンツを配信する際に活用できます。

**用途:** 複数国・複数ドメインで運営するストアで、ドメインに応じて異なるバナーやテキスト、ナビゲーションを表示したいシーンに使用します。

**設置場所:** layout/theme.liquid の `<header>` セクション内、または product.liquid や index.liquid などテンプレート上部に `{% include 'request-host-banner' %}` として呼び出します。

**注意点:** サブドメイン（例：jp.example.com）を含めたい場合は、`request.host` の文字列を正確に指定する必要があります。複数ドメイン指定時は、条件判定の順序が上から順に評価されるため、より厳密な条件を上に配置してください。プレビューモード（preview.example.com）では request.host が異なるため、本番環境での動作確認が必須です。

<details><summary>コード(15行)を見る</summary>

```liquid
{%- comment -%}

Very simple example showing how request.host can be used to show
a different banner image. You can take this further to show custom
text, collections, navigation, layouts, etc.

{%- endcomment -%}

{%- assign banner = "banner-default.jpg" -%}
{%- if request.host == 'freakdesign.com.au' -%}
	{%- assign banner = "banner-au.jpg" -%}
{%- elsif request.host == 'freakdesign.com' -%}
	{%- assign banner = "banner-com.jpg" -%}
{%- endif -%}
<img src="{{ banner | asset_url }}" />
```

</details>


### 3. 🧩 スニペット 商品ブロック区切り線

**カテゴリ:** 商品表示 ／ **難易度:** 初級 ／ **タグ:** `product-page` `block-separator` `ui-component` `section-block`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-block-separator.liquid) （ライセンス: MIT、15行）
- **ファイル:** `snippets/product-block-separator.liquid`

**説明:** 商品詳細ページの各ブロック間に挿入する水平線コンポーネント。パディングや線の高さ、色・透明度をブロック設定で自由に調整できます。

**用途:** 商品説明セクション、スペック表、レビューセクションなど複数のコンテンツブロックを視覚的に区切りたいときに使用します。

**設置場所:** product.liquid テンプレート内で、セクションブロック（{% section 'product-main' %} など）内に配置します。ブロック設定から上下パディング、線の高さ、色を動的に制御します。

**注意点:** ブロック設定で指定されたパディング値（pt、pb）と背景色クラスは、テーマの CSS フレームワーク（Bootstrap など）に依存するため、テーマのユーティリティクラスが定義されていることを確認してください。透明度は 0〜100 の数値で指定し、% 記号は自動付与されます。

<details><summary>コード(15行)を見る</summary>

```liquid
<div 
  class="
    product-block-separator separator-wrappe
    {{ block.settings.pt | prepend: 'pt-' }} 
    {{ block.settings.pb | prepend: 'pb-' }}
  " 
  {{ block.shopify_attributes }}>
  <hr 
    class="separator my-0 {{ block.settings.bg_color }}" 
    style="
      opacity: 1;
      --bs-bg-opacity: {{ block.settings.bg_opacity | append: '%' }};
      height: {{ block.settings.height | append: 'px' }}
    ">
</div>
```

</details>


### 4. 🧩 スニペット クイズ結果の商品データ出力

**カテゴリ:** API連携/JSON出力/JS統合 ／ **難易度:** 中級 ／ **タグ:** `json-ld` `product` `filter` `quiz` `javascript`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/Quiz/snippets/quiz-data.liquid) （ライセンス: MIT、93行）
- **ファイル:** `Quiz/snippets/quiz-data.liquid`

**説明:** コレクションの商品情報をJSON形式で構造化し、クイズの回答フィルター条件と紐付けて出力するスニペット。価格、タグ、タイプ、ベンダー、オプション値などで商品を絞り込み、JavaScript側で動的にフィルタリング可能にします。

**用途:** クイズセクションで、ユーザーの回答に応じて推奨商品を表示するシーン。セクションブロックで定義した複数の質問と選択肢に基づいて、マッチする商品だけを結果ページに表示します。

**設置場所:** Quiz/snippets/quiz-data.liquid に配置。親セクション内で {% include 'quiz-data' %} と呼び出し、`products_data`、`filters_data`、`blocks_data` の3つのキャプチャ変数をJavaScriptの data 属性に埋め込みます。

**注意点:** 価格フィルターは `times: 1.0` で明示的に数値化しないと文字列のまま処理され、比較ロジックが失敗します。また `split: ','` を使う場合、セクション設定でカンマ区切りの値が確実に入力されていることを確認してください。商品がない場合でも空の JSON 配列 `[]` が出力されるため、JavaScriptで空チェックが必要です。

<details><summary>コード(93行)を見る</summary>

```liquid
<!-- snippets/quiz-data.liquid -->
{%- assign collection = collections[section.settings.filter_collection] -%}

{%- capture 'products_data' -%}
{% paginate collection.products by 250 %}
[
{%- for product in collection.products -%}
  {%- capture 'product_html' -%}
  <div class="quiz-product">
    <a href="{{ product.url }}">
      <picture class="result-picture">
        {%- assign img = product.featured_image-%}
        <source media="(max-width: 375px)" srcset="{{ img | img_url: '375x' }}, {{ img | img_url: '375x', scale: 2 }} 2x">
        <source media="(max-width: 480px)" srcset="{{ img | img_url: '480x' }}, {{ img | img_url: '480x', scale: 2 }} 2x">
        <source media="(max-width: 640px)" srcset="{{ img | img_url: '640x' }}, {{ img | img_url: '640x', scale: 2 }} 2x">
        <img src="{{ img | img_url: image_max_width }}" srcset="{{ img | img_url: image_max_width }} 1x, {{ img | img_url: image_max_width, scale: 2 }}  2x" alt="{{ img.alt | escape }}">
      </picture>
      {{ product.title }}
    </a>
  </div>
  {%- endcapture -%}
  {
    "available": {{ product.available | json }},
    "title": {{ product.title | json }},
    "type": {{ product.type | downcase | remove: ' ' | split: ',' | json }},
    "tags": {{ product.tags | json | downcase | remove: ' ' }},
    "vendor": {{ product.vendor | json | downcase }},
    "options": {{ product.options_with_values | json | downcase }},
    "price": {{ product.price | divided_by: 100.0 | json }},
    "featured_image": {{ product.featured_image | json }},
    "url": {{ product.url | json }},
    "html": {{ product_html | json }}
  }{%- unless forloop.last -%},{%- endunless -%}
{%- endfor -%}
]
{% endpaginate %}
{%- endcapture -%}

{%- capture 'filters_data' -%}
{
... (以下 52 行省略)
```

</details>


### 5. 🧩 スニペット メインメニューのナビゲーション

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `navigation` `menu` `linklists` `header` `dropdown`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/snippets/layout-menu.liquid) （ライセンス: MIT、19行）
- **ファイル:** `shopify/snippets/layout-menu.liquid`

**説明:** Shopify の linklists.main-menu を展開し、1階層のサブメニューに対応したナビゲーションメニューを構築します。カスタムクラスとインラインスタイルで柔軟なスタイリングが可能です。

**用途:** ヘッダーやサイドバーに配置するメインナビゲーションメニュー。ドロップダウン対応の階層化メニューを簡潔に実装したい場合に活用します。

**設置場所:** layout/theme.liquid または sections/header.liquid の適切な箇所に `{% include 'layout-menu' %}` で呼び出します。クラス・スタイルをカスタマイズする場合は `{% include 'layout-menu', class: 'nav-class', style: 'display:flex;' %}` と指定します。

**注意点:** サブメニューは1階層のみ対応のため、3階層以上の深いメニューを実装する場合は再帰的なロジックに変更が必要です。Shopify 管理画面のメニュー設定で「メインメニュー」という handle のリンクリストを作成していることが前提となります。メニュー項目にアイコンやバッジを追加する場合は、コード内の `<a>` タグ内にカスタムマークアップを追加してください。

<details><summary>コード(19行)を見る</summary>

```liquid
<div class="{{ class | default: '' }}" style="{{ style | default: '' }}">
  {% for link in linklists.main-menu.links %}
    <div>
      <a href="{{ link.url }}">
        {{ link.title | escape }}
      </a>

      {% if link.levels >= 1 %}
        <div>
          {% for sub_link in link.links %}
            <a href="{{ sub_link.url }}">
              {{ sub_link.title | escape }}
            </a>
          {% endfor %}
        </div>
      {% endif %}
    </div>
  {% endfor %}
</div>
```

</details>


### 6. 🧩 スニペット 404ページテンプレート

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `error-page` `404` `page-template` `layout`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/404.liquid) （ライセンス: MIT、16行）
- **ファイル:** `templates/404.liquid`

**説明:** 存在しないページへのアクセス時に表示する404エラーページです。シンプルなエラーメッセージを中央に配置した基本レイアウトを提供します。

**用途:** テーマの404エラーハンドリング。リンク切れや削除済みページへのアクセス時に自動で表示されます。

**設置場所:** templates/404.liquid として保存します。Shopify管理画面の「オンラインストア > テーマ > コードを編集する」から配置し、404エラーが発生した際に自動で読み込まれます。

**注意点:** ナビゲーション設定でリダイレクトルールを活用すると、既知の無効URLを事前に別ページに転送できます。404ページのデザインをカスタマイズする場合は、ユーザーを売上ページに導くCTAボタンやサーチフォームの追加を推奨します。

<details><summary>コード(16行)を見る</summary>

```liquid
{% comment %}

NOTE: If there are specific nonexistent URLs which your visitors are likely 
to request on a regular basis (maybe due to old links from elsewhere on the web), 
you can set up URL redirection by clicking on your Navigation tab and following 
the link in the sidebar.

{% endcomment %}

<div class="outer">
  
  <div class="dialog" style="text-align: center;">
    <h1>Sorry, File Not Found</h1>
    
  </div>
</div>
```

</details>


### 7. 🧩 スニペット 成功アイコン

**カテゴリ:** UI部品 ／ **難易度:** 初級 ／ **タグ:** `icon` `svg` `success` `ui-component` `accessibility`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/snippets/icon-success.liquid) （ライセンス: MIT、6行）
- **ファイル:** `snippets/icon-success.liquid`

**説明:** チェックマーク付きの緑色の円形アイコン。確認完了や成功状態を視覚的に表現する SVG コンポーネント。

**用途:** 注文完了画面、在庫確保通知、フォーム送信成功メッセージなど、ポジティブな結果を表示する箇所で使用。

**設置場所:** `snippets/icon-success.liquid` に保存後、`{% include 'icon-success' %}` で呼び出す。

**注意点:** SVG は `aria-hidden="true"` で支援技術から隠れているため、アイコンの意味は隣接テキストで補う必要がある。ストアのブランドカラーに合わせて `fill="#428445"` と `stroke="white"` を編集する場合は、コントラスト比を WCAG AA 基準以上に保つ。

<details><summary>コード(6行)を見る</summary>

```liquid
<svg aria-hidden="true" focusable="false" role="presentation" class="icon icon-success" viewBox="0 0 13 13">
  <path d="M6.5 12.35C9.73087 12.35 12.35 9.73086 12.35 6.5C12.35 3.26913 9.73087 0.65 6.5 0.65C3.26913 0.65 0.65 3.26913 0.65 6.5C0.65 9.73086 3.26913 12.35 6.5 12.35Z" fill="#428445" stroke="white" stroke-width="0.7"/>
  <path d="M5.53271 8.66357L9.25213 4.68197" stroke="white"/>
  <path d="M4.10645 6.7688L6.13766 8.62553" stroke="white">
</svg>
```

</details>


### 8. 🧩 スニペット ランダム数値生成

**カテゴリ:** ユーティリティ ／ **難易度:** 初級 ／ **タグ:** `random` `number` `utility` `snippet`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/random-number.liquid) （ライセンス: MIT、13行）
- **ファイル:** `random-number.liquid`

**説明:** 現在時刻をシードに、指定範囲内のランダムな整数を生成します。キャンペーンID、抽選番号、A/Bテストの割り振りなど、軽量な疑似乱数が必要な場面で活用できます。

**用途:** ギフトコード生成、ランダムな商品推薦、抽選機能、テスト用ダミーIDの作成など、テーマ内で乱数が必要な場面全般。

**設置場所:** `snippets/random-number.liquid` として保存し、任意のテンプレートで `{% render 'random-number' %}` で呼び出します。生成された値は `{{ random_number }}` で参照できます。

**注意点:** 最小値・最大値は9行目・10行目で設定変更でき、デフォルトは0～9999999です。同一リクエスト内で複数回呼び出すと同じ値が返る可能性があります。暗号化を要する用途（決済トークン等）には不向きです。

<details><summary>コード(13行)を見る</summary>

```liquid
{%- comment -%}
    Wanna change the range, just edit line 10 & 11

    Basic usage :
    {% render 'random-test' %}
    {{ random_number }} -> here's your random number
{%- endcomment -%}

{%- assign min = 0 -%}
{%- assign max = 9999999 -%}
{%- assign diff = max | minus: min -%}
{%- assign random_number = "now" | date: "%N" | modulo: diff | plus: min -%}
```

</details>


### 9. 🧩 スニペット CSS 変数の定義と フォント読み込み

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `css-variable` `font` `theme-setting` `performance`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/snippets/css-variables.liquid) （ライセンス: MIT、19行）
- **ファイル:** `snippets/css-variables.liquid`

**説明:** テーマの設定値を CSS 変数として :root に定義し、フォント最適化（font-display: swap）を適用します。ストア全体で統一的なデザイントークンを使用できます。

**用途:** layout/theme.liquid から呼び出して、サイト全体の色・幅・フォント・角丸などの値を CSS 変数化し、各テンプレートで活用します。

**設置場所:** layout/theme.liquid の <head> 内（{% render 'css-variables' %} で呼び出す）。テーマ設定（settings_schema.json）で type_primary_font、max_page_width などが定義されている必要があります。

**注意点:** font_modify フィルターで weight・style を変更する場合、指定したバリアント が Google Fonts 等で実装されていないと表示されません。設定値の背景色・前景色が十分なコントラストを持つか確認してください。CSS 変数を上書きする場合は詳細度が同等か高い追加ルールが必要です。

<details><summary>コード(19行)を見る</summary>

```liquid
{% style %}
  {% # Loads all font variantions with display: swap %}
  {{ settings.type_primary_font | font_face: font_display: 'swap' }}
  {{ settings.type_primary_font | font_modify: 'weight', 'bold' | font_face: font_display: 'swap' }}
  {{ settings.type_primary_font | font_modify: 'weight', 'bold' | font_modify: 'style', 'italic' | font_face: font_display: 'swap' }}
  {{ settings.type_primary_font | font_modify: 'style', 'italic' | font_face: font_display: 'swap' }}

  :root {
    --font-primary--family: {{ settings.type_primary_font.family }}, {{ settings.type_primary_font.fallback_families }};
    --font-primary--style: {{ settings.type_primary_font.style }};
    --font-primary--weight: {{ settings.type_primary_font.weight }};
    --page-width: {{ settings.max_page_width }};
    --page-margin: {{ settings.min_page_margin }}px;
    --color-background: {{ settings.background_color }};
    --color-foreground: {{ settings.foreground_color }};
    --style-border-radius-inputs: {{ settings.input_corner_radius }}px;
  }
{% endstyle %}
```

</details>


### 10. 🧩 スニペット ギフトカードテンプレートの動的画像割当

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `gift-card` `image` `variant` `template` `dynamic-content`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Use variant image on Gift Card template/capture-image.liquid) （ライセンス: MIT、16行）
- **ファイル:** `Use variant image on Gift Card template/capture-image.liquid`

**説明:** ギフトカードの金額に対応するバリアント画像を自動取得し、テンプレートに反映させるスニペット。金額不一致時はデフォルト画像を使用します。

**用途:** ギフトカードテンプレート（gift_card.liquid）で、金額ごとに異なる券面デザインを表示したい場合に使用します。

**設置場所:** templates/gift_card.liquid の <img> タグ前に貼り付け、customImage 変数を画像の src 属性に指定します（例：src="{{ customImage }}"）。

**注意点:** admin-gift-card リンクリストと対応するギフトカード商品の存在が前提です。バリアント画像が未設定の場合、自動的にデフォルト画像（gift-card/card.jpg）にフォールバックします。金額マッチングは variant.price と gift_card.initial_value の完全一致で判定されるため、小数点以下の誤差がある場合は該当バリアントが見つかりません。

<details><summary>コード(16行)を見る</summary>

```liquid
{%- assign cardPrice = gift_card.initial_value -%}
{%- assign giftCardProduct = linklists.admin-gift-card.links.first.object -%}
{%- assign customImage = 'gift-card/card.jpg' | shopify_asset_url -%}
{%- for variant in giftCardProduct.variants -%}
  {%- if variant.price != cardPrice %}{% continue %}{% endif -%}
  {%- if variant.image.src == blank %}{% break %}{% endif -%}
  {%- assign customImage = variant.image | img_url:'949x' -%}
  {%- break -%}
{%- endfor -%}


{%- comment -%}
  Somewhere in your template you'll have the image shown. Instead of hard coding in
  the source, we replace that with the variable we created above.
{%- endcomment -%}
<img class="giftcard__image" src="{{ customImage }}" alt="Gift card illustration">
```

</details>


### 11. 🧩 スニペット ナビバーロゴ

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `logo` `header` `navigation` `responsive` `lazy-load`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/navbar-logo.liquid) （ライセンス: MIT、18行）
- **ファイル:** `snippets/navbar-logo.liquid`

**説明:** ストアロゴをナビゲーションバーに表示するコンポーネント。ロゴ画像が設定されていない場合はストア名をテキストで表示します。

**用途:** テーマのヘッダーセクション内でナビバーロゴを表示する際に使用。ブロック設定でロゴ画像とその高さをカスタマイズ可能。

**設置場所:** snippets/navbar-logo.liquid に配置し、header や navigation セクション内で {% include 'navbar-logo' %} で呼び出します。

**注意点:** ロゴ画像の幅は aspect_ratio 倍率から自動計算されるため、アップロード時に画像の縦横比が正確であることを確認してください。遅延読込を使用しているため、ファーストビューのロゴは必要に応じて loading="eager" に変更を検討できます。

<details><summary>コード(18行)を見る</summary>

```liquid
<a 
  class="navbar-logo" 
  href="{{ routes.root_url }}">
  {% if block.settings.logo %}
    {% assign logo_height_x2 = block.settings.logo_height | times: 2 %}
    <img
      class="img-fluid navbar-logo-default"
      src="{{ block.settings.logo | image_url: height: logo_height_x2 }}" 
      alt="{{ shop.name }}"
      width="{{ block.settings.logo_height | times: block.settings.logo.aspect_ratio | round }}" 
      height="{{ block.settings.logo_height }}"
      loading="lazy">
  {% else %}
    <span>
      {{ shop.name }}
    </span>
  {% endif %}
</a>
```

</details>


### 12. 🧩 スニペット FAQ アコーディオンセクション

**カテゴリ:** UI部品 ／ **難易度:** 中級 ／ **タグ:** `faq` `accordion` `json-ld` `animation` `section`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/FAQ/sections/faq.liquid) （ライセンス: MIT、352行）
- **ファイル:** `FAQ/sections/faq.liquid`

**説明:** 質問と回答をアコーディオン形式で表示するセクション。クリックで開閉し、FAQページ向けのリッチスキーマに対応しています。

**用途:** よくある質問（FAQ）ページやページフッターに設置して、顧客向けの質問回答を整理して表示する際に使用します。

**設置場所:** セクションファイル `sections/faq.liquid` として配置し、ページテンプレート（例：`templates/page.faq.liquid`）で `{% section 'faq' %}` で呼び出します。

**注意点:** JavaScript（faq.js）に依存するため、アセットフォルダに対応するスクリプトファイルが必要です。リッチスキーマ出力時、HTMLタグは自動削除されるため回答内容にプレーンテキストのみが記録される点に注意してください。JavaScriptが無効な環境でも、すべての回答がデフォルト表示される仕様になっています。

<details><summary>コード(352行)を見る</summary>

```liquid
{%- comment -%}
Section published at https://sections.design/blogs/shopify/faq-rich-snippets-section
Get the latest version: https://github.com/mirceapiturca/Sections/tree/master/FAQ
{%- endcomment -%}


{%- comment -%} ---------------- THE CSS ---------------- {%- endcomment -%}

{%- assign id = '#shopify-section-' | append: section.id -%}

{% style %}
  {{ id }} {
    background: {{ section.settings.background_color }};
    --panel-bg: {{ section.settings.panel_color }};
    --border-color: {{ section.settings.border_color }}; 
    --question-color: {{ section.settings.q_color }};
    --answer-color: {{ section.settings.a_color }};

    {%- assign min = section.settings.q_size_small -%}
    {%- assign max = section.settings.q_size_large -%}
    {%- assign min_rem = min | append: 'rem' -%}
    {%- assign max_rem = max | append: 'rem' -%}
    --title-font-size: clamp({{ min_rem }}, calc({{ min_rem }} + ({{ max }} - {{ min }}) * ((100vw - 25rem) / (64 - 25))), {{ max_rem }});
  }
{% endstyle %}

<style>
  .flex { display: flex }
  .items-center { align-items: center }
  .justify-between { justify-content: space-between }
  .w-full { width: 100% }
  .text-left { text-align: left }
  .m-0 { margin: 0 }
  .p-0 { padding: 0 }
  .p-4 { padding: 1rem }
  .overflow-hidden { overflow: hidden }
  .cursor-pointer { cursor: pointer }

  {{ id }} .faq-container {
    max-width: {{ section.settings.max_width }};
... (以下 311 行省略)
```

</details>


### 13. 🧩 スニペット フッターセクション

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `footer` `link-list` `navigation` `section`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/footer.liquid) （ライセンス: MIT、25行）
- **ファイル:** `shopify/sections/footer.liquid`

**説明:** フッターメニューリンクと著作権表記を表示するセクションです。リンクリストの「footer」を自動取得して描画します。

**用途:** 全ページ共通のフッター領域に設置し、サイト全体のナビゲーションと企業情報を提示します。

**設置場所:** layout/theme.liquid の閉じ body タグ前に {% section 'footer' %} で呼び出すか、Customizer から Footer セクションとして追加します。

**注意点:** footer リンクリストが Shopify 管理画面で事前に作成されていないと何も表示されません。サイトメニュー > その他メニュー で「footer」という名前のリンクリストを作成してください。著作権年の更新は手動で行うか、別途 Liquid フィルターで動的に処理する必要があります。

<details><summary>コード(25行)を見る</summary>

```liquid
<div class="container">
  <div>
    {% for link in linklists.footer.links %}
      <a href="{{ link.url }}">
        {{ link.title }}
      </a>
    {% endfor %}
  </div>

  <div>
    &copy; Shopify Theme Lab
  </div>
</div>

{% schema %}
{
  "name": "t:sections.footer.name",
  "settings": [
    {
      "type": "paragraph",
      "content": "t:sections.footer.settings.paragraph"
    }
  ]
}
{% endschema %}
```

</details>


### 14. 🧩 スニペット 検索結果ページ

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `search` `pagination` `collection` `category` `product-listing`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/search.liquid) （ライセンス: MIT、17行）
- **ファイル:** `templates/search.liquid`

**説明:** 検索結果から商品を一覧表示し、最も深いカテゴリ階層へのリンクを生成します。自動コレクションの中から最長のハンドルを検出して、リーフカテゴリへ誘導する仕組みです。

**用途:** 検索ページ（/search）で商品結果を表示する際に、カテゴリページへの詳細リンクを提供したいとき。自動生成される階層的なコレクションを活用する場合に便利です。

**設置場所:** templates/search.liquid に配置します。検索オブジェクト（search.results）が渡されるテンプレートで使用。ページネーションで24件単位で商品を表示します。

**注意点:** ハンドル末尾の 'hardware-' プレフィックス削除は固定値なため、テーマに合わせてカスタマイズが必要です。コレクションが存在しない商品は空のハンドルになるため、事前に全商品がコレクションに属していることを確認してください。カテゴリページのURLスキーム（/pages/category/{handle}）とアンカーリンク（#{product.handle}）がサイト構造と一致していることを確認してください。

<details><summary>コード(17行)を見る</summary>

```liquid
{% paginate search.results by 24 %}
  {% for product in search.results %}
    {% comment %}
      Every product is in multiple auto collections that look like this: ["building consumables", "building consumables > solder & flux", "building consumables > solder & flux > rosin flux"]
      So we search for the _longest handle_ to find the leaf category of the product and link to that.
    {% endcomment %}
    {% assign collection_with_longest_handle = product.collections | sort: 'handle.size' | last %}
    {% assign modified_handle = collection_with_longest_handle.handle | remove_first: 'hardware-' %}
    <div>
      <img src="{{ product.featured_image | image_url }}" height="100px" alt="{{ product.title }}">
      <a href="/pages/category/{{ modified_handle }}#{{ product.handle }}">
        {{ product.title }}
      </a>
    </div>
  {% endfor %}
{% endpaginate %}
```

</details>


### 15. 🧩 スニペット ギフトカード表示ページ

**カテゴリ:** ページテンプレート ／ **難易度:** 上級 ／ **タグ:** `gift-card` `qr-code` `template` `checkout`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/templates/gift_card.liquid) （ライセンス: MIT、204行）
- **ファイル:** `templates/gift_card.liquid`

**説明:** ギフトカードの券面を表示し、QRコード生成と番号コピー機能を提供するテンプレート。Shopify標準のギフトカード受け取りページとして機能します。

**用途:** 顧客がメールで受け取ったギフトカード番号を確認・利用する際に表示されるページ。QRコード読み込みまたはコード番号のコピーで利用開始できます。

**設置場所:** templates/gift_card.liquid に配置。`layout none` により独立したHTMLドキュメントとして機能するため、通常のtheme.liquid レイアウトから外れます。Shopifyが自動的にこのテンプレートをギフトカード受け取りURLに紐付けます。

**注意点:** このテンプレートはHeadless API（Storefront API）では未対応のため、サーバーサイドレンダリング環境が必須です。QRコード表示にはShopify公式の vendor/qrcode.js を読み込むため、インターネット接続が必要です。有効期限切れ・無効化されたカードは「Expired」バッジで表示しますが、UIテキストは英語固定のため、日本語対応が必要な場合は translation キーを追加して翻訳してください。

<details><summary>コード(204行)を見る</summary>

```liquid
{% comment %} Unfortunataly gift cards are not supported yet via the Storefront API {% endcomment %}
{% comment %} Based on: https://github.com/Shopify/dawn/blob/v7.0.1/templates/gift_card.liquid {% endcomment %}
{% layout none %}

<!doctype html>
<html lang="{{ request.locale.iso_code }}">
  <head>
    <script src="{{ 'vendor/qrcode.js' | shopify_asset_url }}" defer></script>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="theme-color" content="{{ settings.color_background }}">
    <link rel="canonical" href="{{ canonical_url }}">
    <link rel="preconnect" href="https://cdn.shopify.com" crossorigin>

    {%- if settings.favicon != blank -%}
      <link rel="icon" type="image/png" href="{{ settings.favicon | image_url: width: 32, height: 32 }}">
    {%- endif -%}

    {%- unless settings.type_header_font.system? -%}
      <link rel="preconnect" href="https://fonts.shopifycdn.com" crossorigin>
    {%- endunless -%}

    {%- assign formatted_initial_value = gift_card.initial_value | money_without_trailing_zeros | strip_html -%}

    <title>{{ "Here's your {{ value }} gift card for {{ shop }}!" | t: value: formatted_initial_value, shop: shop.name }}</title>

    <meta name="description" content="Your gift card">

    {{ content_for_header }}

    {%- liquid
      assign body_font_bold = settings.type_body_font | font_modify: 'weight', 'bold'
      assign body_font_italic = settings.type_body_font | font_modify: 'style', 'italic'
      assign body_font_bold_italic = body_font_bold | font_modify: 'style', 'italic'
    %}

    {% style %}
      {{ settings.type_body_font | font_face: font_display: 'swap' }}
      {{ body_font_bold | font_face: font_display: 'swap' }}
... (以下 163 行省略)
```

</details>


### 16. 🧩 スニペット 検索機能の構造化データ（JSON-LD）

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `json-ld` `seo` `search` `schema-org`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/json-ld-search.liquid) （ライセンス: MIT、17行）
- **ファイル:** `json-ld-search.liquid`

**説明:** Google検索結果に検索ボックスを表示するための構造化データをWebサイトレベルで埋め込みます。サイト内検索機能をGoogleに認識させ、検索エクスペリエンスを向上させます。

**用途:** 全ページに共通で設置して、Google検索で「キーワード + サイト名」検索時に、Google検索ボックスからダイレクトに店舗内検索ができるようにします。

**設置場所:** `theme.liquid` または `layout/theme.liquid` の `<head>` 内（推奨は`</head>` 直前）に `{% render 'json-ld-search' %}` として呼び出すか、直接ペーストします。

**注意点:** `{{ shop.url }}` と `/search?q=` のパスが店舗の実際の検索ページと一致していることを確認してください。カスタム検索ページを使っている場合は `target` の URL を修正が必要です。Google Search Console でクローールエラーがないか定期確認が推奨されます。

<details><summary>コード(17行)を見る</summary>

```liquid
{%- comment -%}
    Nothing to do, just : {% render 'json-ld-search' %}
{%- endcomment -%}

<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "url": "{{ shop.url }}",
    "potentialAction": {
      "@type": "SearchAction",
      "target": "{{ shop.url }}/search?q={search_term_string}",
      "query-input": "required name=search_term_string"
    }
  }
</script>
```

</details>


### 17. 🧩 スニペット password レイアウト（パスワード保護ページ基盤）

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `layout` `password-protection` `meta-tag` `css-asset` `theme-structure`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/layout/password.liquid) （ライセンス: MIT、20行）
- **ファイル:** `layout/password.liquid`

**説明:** ストアがパスワード保護されている場合に使用される基本レイアウト。メタタグ、CSSアセット、Shopifyスクリプトを読み込み、パスワード入力フォームを表示します。

**用途:** Shopifyのパスワード保護機能を有効にしたとき、訪問者に表示されるパスワード入力ページ全体の構造として使用されます。

**設置場所:** layout/password.liquid として保存します。password.liquid テンプレートと同階層に配置されることで、パスワード保護ページがこのレイアウトを自動的に継承します。

**注意点:** CSS変数とメタタグレンダリングは別ファイル（css-variables、meta-tags）に依存するため、これらが存在しない場合はレンダリング失敗が起きます。パスワード入力フォーム本体は content_for_layout に含まれるため、このファイルには記述しません。

<details><summary>コード(20行)を見る</summary>

```liquid
<!doctype html>
<html lang="{{ request.locale.iso_code }}">
  <head>
    {% # Inlined CSS Variables %}
    {% render 'css-variables' %}

    {% # Load and preload the critical CSS %}
    {{ 'critical.css' | asset_url | stylesheet_tag: preload: true }}

    {% # Social, title, etc. %}
    {% render 'meta-tags' %}

    {{ content_for_header }}
  </head>

  <body>
    {{ content_for_layout }}
  </body>
</html>
```

</details>


### 18. 🧩 スニペット 検索タイプの判定と表示

**カテゴリ:** コレクション/検索 ／ **難易度:** 初級 ／ **タグ:** `search` `url-parameter` `liquid-filter` `security`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Detect search type used in searches/show-search-type.liquid) （ライセンス: MIT、17行）
- **ファイル:** `Detect search type used in searches/show-search-type.liquid`

**説明:** 検索URLのクエリパラメータから検索タイプ（商品・ページ・記事）を抽出し、判定結果を表示します。許可されたタイプ以外はスキップされ、セキュリティと正確性を確保します。

**用途:** 検索結果ページで「この検索は商品を対象としています」のようなメッセージを動的に表示し、ユーザーに検索スコープを明確に伝える際に使用します。

**設置場所:** search/show.liquid テンプレートの検索結果エリア上部に貼り付け、`{% include 'show-search-type' %}` で呼び出すか、スニペット化して利用します。

**注意点:** 許可リストに登録されていないタイプ（例: 不正なクエリパラメータ）は出力されないため、意図しない値の挿入を防げます。ただし Shopify の検索フォーム仕様に依存するため、カスタム検索実装では URL パラメータ構造を確認してから流用してください。

<details><summary>コード(17行)を見る</summary>

```liquid
{%- comment -%}

  Liquid by Jason @ freakdesign.
  Questions? Ping me on twitter: @freakdesign

  Relates to blog post:
  http://freakdesign.com.au/blogs/news/detect-the-search-type-used-in-a-shopify-search-with-liquid

{%- endcomment -%}
{%- capture url %}{{ canonical_url }}{% endcapture -%}
{%- if url contains 'type=' -%}
  {%- assign allowedTypes = 'product,page,article' | split:',' -%}
  {%- assign searchType = url | split:'type=' | last | split:'&' | first | strip -%}
  {%- if allowedTypes contains searchType -%}
    This search type was for {{ searchType }}s
  {%- endif -%}
{%- endif -%}
```

</details>


### 19. 🧩 スニペット 決済方法アイコン表示

**カテゴリ:** UI部品 ／ **難易度:** 初級 ／ **タグ:** `payment-method` `footer` `icon` `accessibility` `bootstrap`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/payment-icons.liquid) （ライセンス: MIT、18行）
- **ファイル:** `snippets/payment-icons.liquid`

**説明:** ストアで有効な決済方法をアイコンで一覧表示します。アイコンにはツールチップで決済方法名を表示し、セキュリティメッセージを添えます。

**用途:** フッターやチェックアウトページで、顧客が利用可能な決済手段を視覚的に示す際に使用します。

**設置場所:** `snippets/payment-icons.liquid` として保存し、フッターセクション内またはチェックアウト関連のテンプレートで `{% include 'payment-icons' %}` で呼び出します。

**注意点:** 有効な決済方法がない場合は何も表示されません。ツールチップの表示にはBootstrapの初期化が必要です（コード内で `data-bs-toggle="tooltip"` を使用）。決済方法名の日本語翻訳は `general.payment_icons.secure` など言語ファイルで別途設定してください。

<details><summary>コード(18行)を見る</summary>

```liquid
{% unless shop.enabled_payment_types == empty %}
  <ul 
    class="payment-icons"
    aria-label="{{ 'general.accessibility.payment_methods' | t }}">
    {% for type in shop.enabled_payment_types %}
      <li 
        class="" 
        data-bs-toggle="tooltip" 
        data-bs-placement="top" 
        title="{{ type | replace: "_", " " | camelcase }}">
        {{ type | payment_type_svg_tag: class: 'icon' }}
      </li>
    {% endfor %}
  </ul>
  <small class="payment-icons-text">
    {{ 'general.payment_icons.secure' | t }}
  </small>
{% endunless %}
```

</details>


### 20. 🧩 スニペット 画像上のツールチップ

**カテゴリ:** UI部品 ／ **難易度:** 中級 ／ **タグ:** `tooltip` `interactive` `image` `accordion` `animation`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/Tooltips/sections/tooltips.liquid) （ライセンス: MIT、452行）
- **ファイル:** `Tooltips/sections/tooltips.liquid`

**説明:** 画像上の指定位置にクリッカブルなツールチップボタンを配置し、テキスト説明をポップアップ表示するセクション。モバイルではアコーディオン、デスクトップではホバー時にスケールアニメーション付きで展開します。

**用途:** 商品画像の各部位説明、機能紹介画像の詳細解説、インタラクティブなチュートリアルページなど、画像の特定エリアに対話的な補足情報を付与する場面で活用。

**設置場所:** `sections/tooltips.liquid` として保存し、テーマのセクションコレクションに登録。Shopify Admin の「セクションを追加」からページに挿入するか、テンプレートに `{% section 'tooltips' %}` で呼び出し。

**注意点:** JavaScriptハンドラ（`data-tooltip-trigger` のイベントリスナ）がコード外に別途必要。クラス名 `.tooltip-button` や `[aria-expanded]` セレクタが機能するよう外部スクリプトで状態管理が必須。アスペクト比の自動検出は画像ごとに異なるため、位置ズレを防ぐには `image.aspect_ratio` が正確に取得される環境確認が重要。

<details><summary>コード(452行)を見る</summary>

```liquid
{%- comment -%} ---------------- THE CSS --------------------- {%- endcomment -%}

{%- assign button_width_small = 28 -%}
{%- assign button_width_large = 32 -%}
{%- assign tooltip_max_width = 320 -%}
{%- assign image_aspect_ratio = section.settings.image.aspect_ratio | default: 1 -%}
{%- assign section_selector = '[data-tooltips="' | append: section.id | append: '"]'-%}

<style>
  .tooltips-section {
    position: relative;
  }
  
  .tooltips-figure {
    margin: 0;
  }
  
  .tooltips-img {
    display: block;
    width: 100%;
  }
  
  .tooltips-list {
    padding: 0 0 0 32px;
    list-style: decimal;
  }
  
  .tooltip-item {
    box-sizing: border-box;
    padding: 8px 12px;
  }
  
  .tooltip-button {
    background: transparent;
    width: 100%;
    border: 0;
    padding: 0;
    text-align: left;
    z-index: 1;
  }
... (以下 411 行省略)
```

</details>


### 21. 🧩 スニペット ヘッダーセクション（ロゴ・メニュー・顧客メニュー・カート）

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `header` `navigation` `customer-account` `cart` `responsive`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/header.liquid) （ライセンス: MIT、37行）
- **ファイル:** `shopify/sections/header.liquid`

**説明:** ストアの最上部に表示されるヘッダーセクション。ロゴ、ナビゲーションメニュー、顧客ログイン・アカウント・カートへのリンクを配置します。顧客アカウント有効時のみ認証関連のリンクを表示します。

**用途:** すべてのページの上部に固定される主要ナビゲーション領域として使用。モバイルとデスクトップの両対応が必要な場合は、レイアウトメニュー側でレスポンシブ対応を実装します。

**設置場所:** sections/header.liquid として新規作成、または既存のヘッダーセクションの内容を置き換えます。テーマの layout/theme.liquid で {% section 'header' %} として呼び出します。

**注意点:** 顧客アカウント機能は shop.customer_accounts_enabled で有効判定されるため、ストア管理画面の設定確認が必要です。ログイン・ログアウト・登録リンクは customer_login_link、customer_logout_link、customer_register_link フィルターで自動生成されるため、独自のリンク URL を指定できません。メニュー構成は 'layout-menu' スニペットに委譲されているため、ここでは実装されていません。

<details><summary>コード(37行)を見る</summary>

```liquid
<div class="container">
  <a href="{{ routes.root_url }}">
    Logo
  </a>

  {% render 'layout-menu' %}

  <div>
    {% if shop.customer_accounts_enabled %}
      {% if customer %}
        <a href="{{ routes.account_url }}">
          {{ 'action.account' | t }}
        </a>
        {{ 'action.log_out' | t | customer_logout_link }}
      {% else %}
        {{ 'action.log_in' | t | customer_login_link }}
        {{ 'action.register' | t | customer_register_link }}
      {% endif %}
    {% endif %}

    <a href="{{ routes.cart_url }}">
      {{ 'action.cart' | t }}
    </a>
  </div>
</div>

{% schema %}
{
  "name": "t:sections.header.name",
  "settings": [
    {
      "type": "paragraph",
      "content": "t:sections.header.settings.paragraph"
    }
  ]
}
{% endschema %}
```

</details>


### 22. 🧩 スニペット コレクションページテンプレート

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `collection` `product-list` `pagination` `template`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/collection.liquid) （ライセンス: MIT、41行）
- **ファイル:** `templates/collection.liquid`

**説明:** コレクション内の商品を一覧表示するテンプレートです。商品画像、価格、説明文を表示し、ページネーション機能で商品を20件ごとに分割します。

**用途:** Shopify テーマの `/collections/{collection-handle}` ページで使用します。ブランド別、カテゴリ別などの商品一覧の表示に適しています。

**設置場所:** `templates/collection.liquid` に配置します。テーマエディタで新規ファイルを作成するか、既存ファイルに置き換えてください。

**注意点:** 画像の出力サイズは `asset_img_url` フィルタで 'medium' に固定されているため、高解像度表示が必要な場合は 'large' などに変更してください。HTML テーブル構造は古いレイアウト手法のため、レスポンシブ対応には CSS Grid または Flexbox への書き換えを推奨します。`truncatewords: 35` で説明文が切り詰められるので、より長い説明を表示する場合は数値を増やしてください。

<details><summary>コード(41行)を見る</summary>

```liquid
<div id="collectionpage">
  {% paginate collection.products by 20 %}
    <div id="pagination">
      {{ paginate | default_pagination }}
    </div>

    <h2><a href="/">Collection</a> &rarr; {{ collection.title }}</h2>

    {% for product in collection.products %}
      <div class="feature">
        <h2>
          <a href="{{product.url}}">{{ product.vendor }}: {{ product.title }}</a>
        </h2>

        <table>
          <tr>
            <td>
              <a href="{{product.url}}" class="feature-image">
                <img width="50" height="50" src="{{ product.featured_image | asset_img_url: 'medium' }}" alt="{{ product.title }}"/>
              </a>
            </td>

            <td>
              <div class="feature-price tag">
                {{ product.price_min | money }}
                <span class="currency">{{ shop.currency }}</span>
              </div>

              <div class="description">{{ product.description | strip_html | truncatewords: 35 }}</div>

              <p>
                <a href="{{product.url}}"><strong>Read more...</strong></a>
              </p>
            </td>
          </tr>
        </table>
      </div>
    {% endfor %}
  {% endpaginate %}
</div>
```

</details>


### 23. 🧩 スニペット ログインページセクション

**カテゴリ:** 顧客アカウント ／ **難易度:** 中級 ／ **タグ:** `customer-account` `login-form` `password-reset` `guest-checkout` `form-validation`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/sections/main-login.liquid) （ライセンス: MIT、238行）
- **ファイル:** `sections/main-login.liquid`

**説明:** 顧客のログイン、パスワードリセット、ゲストチェックアウトを一つのセクションで実装。ロゴ表示やパディング調整もカスタマイズ可能。

**用途:** 顧客アカウントページ（/account/login）に設置して、ログイン・パスワード復旧フォームを提供する。ゲストチェックアウト有効時はその選択肢も表示。

**設置場所:** sections/main-login.liquid として保存。customers/login.liquid テンプレート内で {% section 'main-login' %} で呼び出す。

**注意点:** multipass_login が有効な場合、このセクション全体が非表示になるため、その環境ではセクション設定が反映されない。ロゴ幅を変更する際、画像のアスペクト比を考慮して高さが自動計算されるが、縦長画像では最大幅に達する前に高さ制約で切れる可能性がある。password_needed フラグがfalseのとき（ソーシャルログイン等の場合）パスワードフィールドは表示されない。

<details><summary>コード(238行)を見る</summary>

```liquid
{% comment %} Based on: https://github.com/Shopify/dawn/blob/v7.0.1/sections/main-login.liquid {% endcomment %}
{%- if settings.multipass_login != true -%}
  {{ 'customer.css' | asset_url | stylesheet_tag }}

  {%- style -%}
    .login-logo {
      max-width: {{ section.settings.logo_width }}px;
    }

    .section-{{ section.id }}-padding {
      padding-top: {{ section.settings.padding_top | times: 0.75 | round: 0 }}px;
      padding-bottom: {{ section.settings.padding_bottom | times: 0.75 | round: 0 }}px;
    }

    @media screen and (min-width: 750px) {
      .section-{{ section.id }}-padding {
        padding-top: {{ section.settings.padding_top }}px;
        padding-bottom: {{ section.settings.padding_bottom }}px;
      }
    }
  {%- endstyle -%}

  <div class="customer login section-{{ section.id }}-padding">
    {%- if section.settings.logo != blank -%}
      <a href="https://{{ settings.storefront_hostname }}/" style="margin-bottom:3rem;">
        {%- assign logo_alt = shop.name | escape -%}
        {%- assign logo_height = section.settings.logo_width | divided_by: section.settings.logo.aspect_ratio -%}
        {{ section.settings.logo | image_url: width: section.settings.width | image_tag:
          class: 'login-logo',
          widths: '50, 100, 150, 200, 250, 300, 400, 500',
          height: logo_height,
          width: section.settings.logo_width,
          alt: logo_alt
        }}
      </a>
    {%- endif -%}

    <h1 id="recover" tabindex="-1">
      Reset password
    </h1>
... (以下 197 行省略)
```

</details>


### 24. 🧩 スニペット Organization 構造化データ（ストア情報をGoogleに送信）

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `json-ld` `organization` `schema-org` `seo`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/json-ld-organization.liquid) （ライセンス: MIT、22行）
- **ファイル:** `json-ld-organization.liquid`

**説明:** ストアのロゴとSNSプロフィールをJSON-LD形式で埋め込み、検索エンジンに組織情報を認識させます。Google検索結果やナレッジパネルに表示される可能性が高まります。

**用途:** theme.liquid のヘッダー内に設置し、全ページでストアの信頼性と可視性を向上させます。特に企業サイトやブランド認知が重要なストアで効果的です。

**設置場所:** sections/header.liquid または layout/theme.liquid の <head> タグ内に記述します。{% include 'json-ld-organization' %} で呼び出してください。

**注意点:** ロゴのアセット名（デフォルト：logo.png）がテーマに存在することを確認し、必要に応じて11行目で修正してください。テーマ設定にSNS各種のURLが未入力の場合、空の値が出力されるため、settings.json で該当フィールドを定義するか、条件分岐で空値をフィルタリングしてください。

<details><summary>コード(22行)を見る</summary>

```liquid
{%- comment -%}
    You have to change the logo asset on line 11.
    Also change social links started at line 13, with as many links you need.
{%- endcomment -%}

<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "url": "{{ shop.url }}",
    "logo": "{{ 'logo.png' | asset_url }}",
    "sameAs": [
      "{{ settings.social_facebook }}",
      "{{ settings.social_instagram }}",
      "{{ settings.social_twitter }}",
      "{{ settings.social_pinterest }}",
      "{{ settings.social_linkedin }}",
      "{{ settings.social_youtube }}"
    ]
  }
</script>
```

</details>


### 25. 🧩 スニペット 404エラーページ

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `404` `error-page` `template` `redirect` `i18n`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/404.liquid) （ライセンス: MIT、24行）
- **ファイル:** `sections/404.liquid`

**説明:** 顧客が存在しないURLにアクセスした際に表示する404ページセクション。エラーメッセージと商品一覧へのリンクを提供します。

**用途:** 404テンプレートに設置し、無効なストアURLへのアクセス時にユーザーを適切なページへ誘導します。

**設置場所:** templates/404.liquid に `{% section '404' %}` で呼び出すか、またはこのコード全体を 404.liquid テンプレートに直接記述します。

**注意点:** 翻訳キー('404.title'、'404.not_found'、'404.back_to_shopping')は locale ファイルで定義が必須です。ストアの全商品コレクションが空の場合、リンク先ページが表示されないため、別の誘導先(ホームページなど)の検討を推奨します。

<details><summary>コード(24行)を見る</summary>

```liquid
{% comment %}
  This section is used in the 404 template to render page shown when customers
  enter an invalid store URL.

  https://shopify.dev/docs/storefronts/themes/architecture/templates/404
{% endcomment %}

<h1>{{ '404.title' | t }}</h1>

<p>
  {{ '404.not_found' | t }}
</p>

<a href="{{ routes.all_products_collection_url }}">
  {{ '404.back_to_shopping' | t }}
</a>

{% schema %}
{
  "name": "t:general.404",
  "settings": []
}
{% endschema %}
```

</details>


### 26. 🧩 スニペット 動的ページネーション（カート属性で件数制御）

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `pagination` `collection` `cart-attribute` `dynamic-template`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Dynamic pagination without alternate templates/dynamic-pagination.liquid) （ライセンス: MIT、20行）
- **ファイル:** `Dynamic pagination without alternate templates/dynamic-pagination.liquid`

**説明:** コレクションの商品表示件数をカート属性から動的に読み込み、複数テンプレートを用意せずにページネーションを実装できます。ユーザーが選択した件数設定を保持して表示します。

**用途:** コレクションページで「1ページあたりの表示件数」をユーザーが選択できる機能を実装する際に使用。カート属性に保存した値を再利用して、複数テンプレートの管理を避けられます。

**設置場所:** collection.liquid テンプレート内の `{% paginate collection.products by ... %}` ブロック手前に貼り付け。このコードで `paginationAmount` を計算した後、paginate タグの第2引数に指定します。

**注意点:** カート属性に保存された値は顧客ごと・セッションごとに管理されるため、別ストアやプライベートブラウジングでは初期値（40件）にリセットされます。無限スクロールを実装する場合は、AJAX での paginate 呼び出しが必要になるため、このスニペット単体では対応できません。

<details><summary>コード(20行)を見る</summary>

```liquid
{%- comment -%}

  Relates to the blog post here:
  http://freakdesign.com.au/blogs/news/167340935-paginate-a-shopify-collection-by-dynamic-amounts-without-multiple-templates

{%- endcomment -%}

{%- comment -%} Set the default pagination amount. You may want to hard code this in or use a theme setting. For simplicity we are just hard coding it. {%- endcomment -%}
{%- assign paginationAmount = 40 -%}

{%- comment -%} Check to see if we have a pagination cart attribute already set {%- endcomment -%}
{%- if cart.attributes.pagination != blank -%}

  {%- comment -%} If we do, use this value for the pagination instead {%- endcomment -%}
  {%- assign paginationAmount = cart.attributes.pagination | default:40 | abs -%}

{%- endif -%}
{%- paginate collection.products by paginationAmount -%}
  ...
{%- endpaginate -%}
```

</details>


### 27. 🧩 スニペット 商品カスタムバッジ

**カテゴリ:** 商品表示 ／ **難易度:** 中級 ／ **タグ:** `metafield` `badge` `dynamic-content` `color-customization`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-custom-badge.liquid) （ライセンス: MIT、19行）
- **ファイル:** `snippets/product-custom-badge.liquid`

**説明:** メタフィールドから取得したテキストと色情報を使い、商品に動的なバッジを表示します。パイプ区切りのメタフィールド値を解析し、カスタムカラーのバッジをレンダリングします。

**用途:** 商品カード・商品詳細ページで、新着・セール・在庫限定などのバッジを管理画面から簡単に付与したい場合に使います。

**設置場所:** `snippets/product-custom-badge.liquid` に配置し、商品表示テンプレート内で `{% include 'product-custom-badge' %}` で呼び出します。

**注意点:** メタフィールドは「namespace.key」形式で管理画面から定義し、値は「テキスト|カラーコード」（パイプ区切り）で入力します。色指定がない場合、管理画面の `product_custom_badge_bg_color` 設定が適用されます。色ダークン効果の「15」は下線用なので、調整が必要な場合は数値を変更してください。

<details><summary>コード(19行)を見る</summary>

```liquid
{% liquid 
  assign metafield_namespace = settings.product_custom_badge_metafield | split: '.' | first
  assign metafield_key = settings.product_custom_badge_metafield | split: '.' | last
  assign metafield = product.metafields[metafield_namespace][metafield_key]

  assign text = metafield | split: '|' | first
  assign color = metafield | split: '|' | last 
%}

{% if metafield != blank %}
  <span 
    class="product-custom-badge badge {{ settings.product_custom_badge_bg_color }}"
    style="{% if color != blank %}background: {{ color }} !important{% endif %}">
    {% if color != blank %}
      <span style="border-bottom-color: {{ color | strip | color_darken: 15 }}"></span>
    {% endif %}
    {{ text }}
  </span>
{% endif %}
```

</details>


### 28. 🧩 スニペット theme.liquid（テーマレイアウト基盤）

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `layout` `html-structure` `meta-tag` `asset-loading`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/layout/theme.liquid) （ライセンス: MIT、42行）
- **ファイル:** `shopify/layout/theme.liquid`

**説明:** 全ページ共通のHTML構造とメタ情報を定義するレイアウトファイル。言語設定、ファビコン、バンドルファイルの読み込み、ヘッダー・フッターセクションを統括します。

**用途:** Shopifyテーマの最上位レイアウトファイルとして、すべてのページテンプレートの親テンプレートとなります。theme.liquid を編集することで、全ページ共通の<head>タグやスクリプト・スタイルシート読み込みを制御できます。

**設置場所:** shopify/layout/theme.liquid に配置します。このファイルは自動的に全ページテンプレートをラップするため、個別のテンプレートでは呼び出し不要です。

**注意点:** request.page_type === 'captcha' の判定により、reCAPTCHAチェック画面では id="app" を出力しません。bundle.css と bundle.js は設定したアセットパス上に実在することを確認してください。settings.favicon は管理画面で設定されている場合のみ出力されるため、デフォルトファビコンが必要な場合は別途フォールバック処理を追加してください。

<details><summary>コード(42行)を見る</summary>

```liquid
<!doctype html>
<html lang="{{ request.locale.iso_code }}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">

    <link rel="preconnect" href="https://cdn.shopify.com" crossorigin>
    <link rel="preload" href="{{ 'bundle.css' | asset_url }}" as="style">
    <link rel="preload" href="{{ 'bundle.js' | asset_url }}" as="script">

    {% if settings.favicon %}
      <link rel="shortcut icon" href="{{ settings.favicon | img_url: '32x32' }}" type="image/png">
    {% endif %}

    <title>{{ page_title | escape }}</title>

    {% if page_description %}
      <meta name="description" content="{{ page_description | escape }}">
    {% endif %}

    {{ 'bundle.css' | asset_url | stylesheet_tag }}

    <!-- header hook for Shopify plugins -->
    {{ content_for_header }}
  </head>

  <body>
    <div {% unless request.page_type == 'captcha' %}id="app"{% endunless %}>
      {% section 'header' %}

      <main id="main" role="main">
        {{ content_for_layout }}
      </main>

      {% section 'footer' %}
    </div>

    <!-- webpack bundle -->
    <script src="{{ 'bundle.js' | asset_url }}" defer="defer"></script>
... (以下 2 行省略)
```

</details>


### 29. 🧩 スニペット カテゴリ多列グリッド

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `section` `collection` `grid-layout` `metaobject` `responsive-design`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/sections/category-multicolumn.liquid) （ライセンス: MIT、112行）
- **ファイル:** `sections/category-multicolumn.liquid`

**説明:** コレクションの下位カテゴリを複数列のカード形式で表示するセクション。メタオブジェクトで階層構造に対応し、プリロード機能で画像の先読みを実現します。

**用途:** ECサイトのカテゴリランディングページで、親カテゴリ配下の子カテゴリを視覚的に整列表示する場面に使用。ホバー時の背景変化で操作性を向上させます。

**設置場所:** sections/category-multicolumn.liquid として新規作成し、Shopify管理画面のテーマエディタからセクション追加でページに配置。schema定義により、各カード行のコレクション、画像、タイトル、説明文、リンクを個別に設定可能。

**注意点:** block.settings.next_children のメタオブジェクト型定義（category_metaobject）はストア側で事前に作成が必須。grid-template-columns の minmax(25rem, 1fr) は想定画像サイズに応じて調整が必要。プリロード link タグは image_url: width: 150 で指定した寸法に限定され、異なるサイズの画像をキャッシュする場合は複数行の設定が求められます。

<details><summary>コード(112行)を見る</summary>

```liquid
{% stylesheet %}
  .card {
    display: flex;
    font-size: 0.8rem;
    gap: 0.5rem;
    border: 1px solid lightgrey;
    padding: 0.5rem;
    border-radius: 0.25rem;
    text-decoration: none;
    color: black;
  }
  .card:hover {
    background-color: lightgrey;
  }
  .card:hover .card__title {
    text-decoration: underline;
  }
  .card__image {
  }
  .card__content {
    flex: 2;
  }
  .card__title {
    font-size: 0.8rem;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(25rem, 1fr));
    gap: 0.5rem;
    margin: 0.5rem;
  }
{% endstylesheet %}

{% if section.blocks.size > 0 %}
  <h1 class="sticky-header">
    All Categories >
    {{ section.settings.collection.title }} ({{ section.blocks.size }}
    {{ section.blocks.size | pluralize: 'category', 'categories' }})
  </h1>
{% endif %}
... (以下 71 行省略)
```

</details>


### 30. 🧩 スニペット theme.liquid レイアウト（テーマ基盤）

**カテゴリ:** テーマ基盤 ／ **難易度:** 中級 ／ **タグ:** `layout` `css-variable` `font-loading` `meta-tag` `responsive`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/layout/theme.liquid) （ライセンス: MIT、242行）
- **ファイル:** `layout/theme.liquid`

**説明:** Shopify テーマの基本レイアウトファイル。ページの HTML 構造、メタタグ、CSS 変数、フォント定義を一元管理します。すべてのテンプレートはこのレイアウトをベースに描画されます。

**用途:** テーマのカスタマイズやテンプレート開発の際、HTML ヘッダー部分やグローバル CSS 変数の定義を確認・編集するために参照します。

**設置場所:** layout/theme.liquid が本体です。他のテンプレートファイルは `{% layout 'theme' %}` で自動的にこのレイアウトを継承します。

**注意点:** CSS 変数の計算に `settings` から取得した値が多く使われているため、テーマ設定画面（theme.json）との一貫性を保つ必要があります。フォント読み込みは `font_modify` フィルターで bold・italic 体を生成していますが、フォント側がそのウェイトに対応していない場合は表示が崩れる可能性があります。`content_for_header` は Shopify が動的に挿入する領域のため、削除・移動厳禁です。

<details><summary>コード(242行)を見る</summary>

```liquid
<!doctype html>
<html lang="{{ request.locale.iso_code }}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="theme-color" content="">
    <link rel="canonical" href="{{ canonical_url }}">
    <link rel="preconnect" href="https://cdn.shopify.com" crossorigin>

    {%- if settings.favicon != blank -%}
      <link rel="icon" type="image/png" href="{{ settings.favicon | image_url: width: 32, height: 32 }}">
    {%- endif -%}

    {%- unless settings.type_header_font.system? and settings.type_body_font.system? -%}
      <link rel="preconnect" href="https://fonts.shopifycdn.com" crossorigin>
    {%- endunless -%}

    <title>
      {{ page_title }}
    </title>

    {% if page_description %}
      <meta name="description" content="{{ page_description | escape }}">
    {% endif %}

    {{ content_for_header }}

    {%- liquid
      assign body_font_bold = settings.type_body_font | font_modify: 'weight', 'bold'
      assign body_font_italic = settings.type_body_font | font_modify: 'style', 'italic'
      assign body_font_bold_italic = body_font_bold | font_modify: 'style', 'italic'
    %}

    {% style %}
      {{ settings.type_body_font | font_face: font_display: 'swap' }}
      {{ body_font_bold | font_face: font_display: 'swap' }}
      {{ body_font_italic | font_face: font_display: 'swap' }}
      {{ body_font_bold_italic | font_face: font_display: 'swap' }}
      {{ settings.type_header_font | font_face: font_display: 'swap' }}
... (以下 201 行省略)
```

</details>


### 31. 🧩 スニペット ランダム商品の取得

**カテゴリ:** ユーティリティ ／ **難易度:** 中級 ／ **タグ:** `product` `collection` `random` `snippet`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/random-product.liquid) （ライセンス: MIT、32行）
- **ファイル:** `random-product.liquid`

**説明:** ストール全体またはコレクション内からランダムに1つの商品を取得するスニペット。タイムスタンプをシード値とした疑似乱数で商品を選定します。

**用途:** おすすめ商品の露出、サイドバーのランダム表示、キャンペーンランディングページで異なる商品を表示させる場合に使用します。

**設置場所:** sections/ または templates/ に別ファイルとして保存後、`{%- render 'random-product' -%}` または `{%- render 'random-product' with specific_collection: 'コレクションハンドル' -%}` で呼び出します。

**注意点:** 「now」フィルターで生成する乱数は粗いため、アクセスが集中するとタイムスタンプが同じになり同じ商品が選ばれる可能性があります。より均等な分布が必要な場合は JavaScript での実装を検討してください。コレクション指定時は、ハンドルが存在しない場合エラーが発生するため、テーマ設定やアセット管理で事前に確認が必要です。

<details><summary>コード(32行)を見る</summary>

```liquid
{%- comment -%}
    Basic usage to get a random product from all your shop :
    {%- render 'random-product' -%}
    {{ random_product }} -> here's your random product

    Basic usage to get a random product from a specific collection :
    {%- render 'random-product' with specific_collection: 'sport' -%}
    {{ random_product }} -> here's your random product
{%- endcomment -%}

{%- if specific_collection -%}
    {%- assign all_products_from_collection = collections[specific_collection].products -%}
{%- else -%}
    {%- assign all_products_from_collection = collections['all'].products -%}
{%- endif -%}

{%- assign all_products_random = '' -%}

{%- for product_splitted in all_products_from_collection -%}
    {%- assign all_products_random = all_products_random | append: product_splitted.handle | append: ',' -%}
{%- endfor -%}

{%- assign all_products_random_splited = all_products_random | split: ',' -%}

{%- assign min = 0 -%}
{%- assign max = all_products_random_splited.size | minus: 1 -%}
{%- assign diff = max | minus: min -%}
{%- assign random_number = "now" | date: "%N" | modulo: diff | plus: min -%}

{%- assign random_product_slug = all_products_random_splited[random_number] -%}
{%- assign random_product = all_products[random_product_slug] -%}
```

</details>


### 32. 🧩 スニペット ブログ記事一覧

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `blog` `pagination` `article` `template` `section`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/blog.liquid) （ライセンス: MIT、36行）
- **ファイル:** `sections/blog.liquid`

**説明:** ブログテンプレートで使用するセクション。ブログ内の全記事を一覧表示し、アイキャッチ画像・タイトル・公開日・著者・抜粋テキストを含めてレンダリングします。ページネーション対応。

**用途:** ブログトップページ（/blogs/ニュース など）で、複数の記事を5件単位で表示する際に使用します。カスタマーに最新情報や企業ニュースを発信するシーンに最適。

**設置場所:** sections/blog.liquid として保存し、blog テンプレート（templates/blog.liquid）内で {% section 'blog' %} として呼び出します。

**注意点:** アイキャッチ画像が設定されていない記事は画像部分がスキップされます。ページネーション表示を変更する場合は、default_pagination の出力形式をカスタマイズするか、独自のページャーロジックを別セクション化してください。記事タイトルは自動的にリンク化されるため、URL が正常に生成されていることを確認してください。

<details><summary>コード(36行)を見る</summary>

```liquid
{% comment %}
  This section is used in the blog template to render the blog page listing all
  articles within a blog.

  https://shopify.dev/docs/storefronts/themes/architecture/templates/blog
{% endcomment %}

<h1>{{ blog.title }}</h1>

{% paginate blog.articles by 5 %}
  {% for article in blog.articles %}
    <div>
      {% if article.image %}
        {{ article.image | image_url: width: 1000 | image_tag }}
      {% endif %}
      <h2>
        {{ article.title | link_to: article.url }}
      </h2>
      {% assign date = article.published_at | time_tag: format: 'date' %}
      <p>{{ 'blog.article_metadata_html' | t: date: date, author: article.author }}</p>
      <p>{{ article.excerpt }}</p>
    </div>
  {% endfor %}

  {%- if paginate.pages > 1 -%}
    {{- paginate | default_pagination -}}
  {%- endif -%}
{% endpaginate %}

{% schema %}
{
  "name": "t:general.blog",
  "settings": []
}
{% endschema %}
```

</details>


### 33. 🧩 スニペット SKU検索エンドポイント

**カテゴリ:** API連携/JSON出力/JS統合 ／ **難易度:** 中級 ／ **タグ:** `search` `sku` `json-api` `rest-endpoint` `product`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Search by SKU/search.sku.liquid) （ライセンス: MIT、23行）
- **ファイル:** `Search by SKU/search.sku.liquid`

**説明:** 検索フォームから SKU で商品を検索し、JSON 形式で結果を返すエンドポイント。外部システムや JavaScript から API として利用できます。

**用途:** 顧客向けの SKU 検索機能や、在庫管理システムとの連携時に、検索結果を JSON で取得する必要があるシーン。

**設置場所:** templates/search.sku.liquid として新規ファイルを作成し、URL クエリパラメータ `?q=SKU番号` でアクセス。JavaScript の fetch() や外部ツールから `https://yourstore.myshopify.com/search?type=product&q={sku}` などで呼び出します。

**注意点:** このエンドポイントは layout を無視するため、テーマの CSS や JavaScript が適用されません。クエリパラメータの `q` に複数の検索ワードを指定する場合、検索結果に正確な SKU マッチが含まれるかを事前確認してください。また、Shopify の検索インデックス遅延により、新しく登録した商品の SKU が即座に検索対象にならない可能性があります。

<details><summary>コード(23行)を見る</summary>

```liquid
{%- layout none -%}
{%- comment -%}
/*
 * Simple SKU Search Endpoint
 *
 * Copyright (c) 2016 Jason Bowman (jason@freakdesign.com.au)
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/mit-license.php
 *
 *
 */ 
{%- endcomment -%}
{%- paginate search.results by 250 -%}
{%- if search.performed -%}
{"products": [
	{%- for item in search.results -%}
		{%- unless item.object_type == 'product' -%}{%- continue -%}{%- endunless -%}
		{{- item | json -}}
		{%- unless forloop.last %},{% endunless -%}
	{%- endfor -%}
]}
{%- endif -%}
{%- endpaginate -%}
```

</details>


### 34. 🧩 スニペット 商品ブロック リッチテキスト

**カテゴリ:** 商品表示 ／ **難易度:** 中級 ／ **タグ:** `section-block` `rich-text` `spacing-utility` `product-page`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-block-richtext.liquid) （ライセンス: MIT、22行）
- **ファイル:** `snippets/product-block-richtext.liquid`

**説明:** 商品ページにカスタマイズ可能なテキストブロックを追加するセクションブロック。ブロック設定から任意のタイトル・説明文を配置でき、商品説明の自動挿入にも対応しています。

**用途:** 商品詳細ページで、商品説明の前後に販売促進文やサイズガイドなどのカスタムテキストを挿入したい場合に使用します。

**設置場所:** product テンプレート内で section ブロックとして呼び出します。プレビュー側では blocks に対応したセクション設定ファイルでこのスニペットを include して使用します。

**注意点:** block.settings はセクション schema で定義されている必要があり、pt・pb の値は Bootstrap スペーシングクラス（pt-1 など）に変換されます。description_classes に入力される CSS クラスはテーマの CSS 規則に準拠していないと反映されません。product.description を自動挿入する場合、テーマの rte クラスのスタイルに依存するため、既存商品説明のレイアウト崩れを回避するため事前テストが必須です。

<details><summary>コード(22行)を見る</summary>

```liquid
{% liquid 
  assign pt = block.settings.pt | prepend: 'pt-'
  assign pb = block.settings.pb | prepend: 'pb-'
%}

<div 
  class="product-block-richtext {{ pt }} {{ pb }}" 
  {{ block.shopify_attributes }}>
  {% unless block.settings.title == blank %}
    <h2 class="title {{ block.settings.title_font_size }}">
      {{ block.settings.title }}
    </h2>
  {% endunless %}
  {% if block.settings.description != blank or block.settings.product_description != false %}
    <div class="description rte mb-0 {{ block.settings.description_font_size }} {{ block.settings.description_classes }}">
      {{ block.settings.description }}
      {% if block.settings.product_description %}
        {{ product.description }}
      {% endif %}
    </div>
  {% endif %}
</div>
```

</details>


### 35. 🧩 スニペット Vue コンポーネント統合デモ

**カテゴリ:** API連携/JSON出力/JS統合 ／ **難易度:** 上級 ／ **タグ:** `vue` `components` `vuex` `state-management` `theme-lab`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/vue-examples.liquid) （ライセンス: MIT、162行）
- **ファイル:** `shopify/sections/vue-examples.liquid`

**説明:** Shopify Theme Lab の開発環境で Vue コンポーネント、ミックスイン、ディレクティブ、Vuex ストアを実装・検証するサンプルセクション。Props、スロット、レンダーレスパターン、状態管理の実例を提供します。

**用途:** Vue ベースのテーマ開発時に、コンポーネント設計パターンや Vuex 連携の動作確認をセクションエディタ上で検証する。

**設置場所:** `sections/vue-examples.liquid` に配置し、Theme Lab の開発環境で `<render-my-component>` および `<renderless-my-component>` の構成ファイル（`src/vue/components/`、`src/vue/mixins/`、`src/vue/directives/`、`src/vue/store/`）と連動させる。

**注意点:** このセクションは Theme Lab フレームワークの存在を前提とするため、単体のテーマでは動作しません。Vue コンポーネント名のケバブケース化ルール（`MyComponent` → `<my-component>`、ファイルパスは `components/` 以下から自動生成）を理解した上で利用してください。Shopify グローバルオブジェクト（`shop.name` 等）をコンポーネント Props として渡す際は、必ずサーバーサイドで Liquid タグを用いて文字列化し、JSON シリアライズエラーを防ぐ必要があります。

<details><summary>コード(162行)を見る</summary>

```liquid
<div class="container">
  <div class="shopify-theme-lab">
    <h1 class="shopify-theme-lab__headline">
      Shopify Theme Lab 🧪
    </h1>

    <p class="shopify-theme-lab__text">
      Customizable modular development environment for blazing-fast Shopify theme creation.
    </p>

    <div class="shopify-theme-lab__examples">
      <!--
        * if "name: 'MyComponent'" is defined inside a vue file, it can be referenced as <my-component></my-component>
        * otherwise the component will be named after the file path starting from the components/ directory
        * for src/vue/components/render/my-component.vue it's: <render-my-component></render-my-component>
      -->

      <div class="shopify-theme-lab__example">
        <!-- render component example: src/vue/components/render/my-component.vue -->
        <render-my-component
          :shopify-data="{
            shopName: '{{ shop.name }}',
            shopDomain: '{{ shop.domain }}',
            shopEmail: '{{ shop.email }}',
            shopCurrency: '{{ shop.currency }}'
          }"
        >
          <div class="shopify-theme-lab__subline">
            Vue component with slots and props
          </div>
        </render-my-component>

        <!-- global mixin: src/vue/mixins/global.mixin.js -->
        <div>
          <div class="shopify-theme-lab__subline">
            Global Vue mixin
          </div>

          <div>
            NODE_ENV: {% raw %}{{ env }}{% endraw %}
... (以下 122 行省略)
```

</details>


### 36. 🧩 スニペット ホームページ カテゴリグリッド

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `metaobject` `category` `grid-layout` `homepage` `image-handling`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/sections/homepage.liquid) （ライセンス: MIT、119行）
- **ファイル:** `sections/homepage.liquid`

**説明:** メタオブジェクトで管理した商品カテゴリを階層的に表示するセクション。カテゴリ名から親階層を除去し、サムネイル付きグリッドレイアウトで整列させます。

**用途:** ホームページでカテゴリ一覧を視覚的に提示し、ユーザーのカテゴリ探索を促進したい場合に使用。サブカテゴリは親カテゴリ配下にグループ化されます。

**設置場所:** sections/homepage.liquid に配置し、ホームページテンプレート（templates/index.liquid）で {% section 'homepage' %} として呼び出します。

**注意点:** 子カテゴリの名前区切り文字が「 > 」で、かつ1階層のみ（' > ' が1回だけ）のデータ構造を前提としています。複数階層や異なる区切り文字は表示されません。メタオブジェクトの category_metaobject タイプと name、image フィールドが正しく設定されていることを確認してください。

<details><summary>コード(119行)を見る</summary>

```liquid
<style>
  .small_grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(5rem, 1fr));
    gap: 0.5rem;
    list-style: none;
    padding-left: 0;
  }

  .small_grid img {
    border: 1px solid lightgrey;
    max-width: 100%;
    object-fit: cover;
  }

  .small_grid a {
    text-decoration: none;
    color: black;
  }

  .small_grid a:hover {
    text-decoration: underline;
  }

  .small_grid a {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    text-align: center;
    font-size: 0.8rem;
  }

  .category {
    padding: 0.5rem;
  }

  .small_grid_title {
    font-size: 1.25rem;
    font-weight: normal;
... (以下 78 行省略)
```

</details>


### 37. 🧩 スニペット Twitter Card メタタグ

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `twitter-card` `meta-tag` `seo` `product` `article`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/metadata-twitter.liquid) （ライセンス: MIT、37行）
- **ファイル:** `metadata-twitter.liquid`

**説明:** 商品ページ・記事ページ・その他のページに応じて、Twitter Cardのメタタグを自動生成します。商品情報や記事内容をツイート時にリッチプレビューで表示させられます。

**用途:** layout/theme.liquid の <head> 内に挿入して、Twitter シェア時の表示を整える。商品ページでは価格・在庫、記事ページではサムネイルを自動抽出。

**設置場所:** layout/theme.liquid の <head> セクション内、その他のメタタグの下に `{% render 'metadata-twitter' %}` で呼び出す。

**注意点:** 6行目の `@twitter_handler` をストアの Twitter ハンドルに変更する必要があります。35行目の `logo-square.png` は正方形の画像アセットに置き換えてください。記事ページから画像を抽出する処理は img タグの src 属性が相対パスの場合のみ対応するため、外部 CDN の画像はツイート時に表示されない可能性があります。

<details><summary>コード(37行)を見る</summary>

```liquid
{%- comment -%}
    You have to change the Twitter handle line 6.
    You have to change the logo asset on line 35. It must be a square picture.
{%- endcomment -%}

<meta name="twitter:site" content="@twitter_handler" />

{% if template contains 'product' %}
    <meta name="twitter:card" content="product" />
    <meta name="twitter:title" content="{{ product.title | escape }}" />
    <meta name="twitter:description" content="{{ product.description | strip_html | strip_newlines | truncatewords: 60, '' | escape }}" />
    <meta name="twitter:image" content="https:{{ product.featured_image.src | product_img_url: 'large' }}" />
    <meta name="twitter:label1" content="Price" />
    <meta name="twitter:data1" content="{% if product.price_varies %}From {% endif %}{{ product.price | money_with_currency | strip_html }}" />
    {% if product.vendor == blank %}
        <meta name="twitter:label2" content="Availability" />
        <meta name="twitter:data2" content="{% if product.available %}In stock{% else %}Out of stock{% endif %}" />
    {% else %}
        <meta name="twitter:label2" content="Brand" />
        <meta name="twitter:data2" content="{{ product.vendor | escape }}" />
    {% endif %}
{% elsif template contains 'article' %}
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:title" content="{{ article.title | escape }}" />
    <meta name="twitter:description" content="{{ article.excerpt_or_content | strip_html | truncatewords: 60, '' | escape }}" />
    {% assign img_tag = '<' | append: 'img' %}
    {% if article.content contains img_tag %}
        {% assign src = article.content | split: 'src="' %}
        {% assign src = src[1] | split: '"' | first | remove: 'https:' | remove: 'http:' %}
        {% if src %}
            <meta property="twitter:image" content="http:{{ src }}" />
        {% endif %}
    {% endif %}
{% else %}
    <meta name="twitter:image" content="{{ 'logo-square.png' | asset_url }}" />
{% endif %}
```

</details>


### 38. 🧩 スニペット パスワード保護ランディングページ

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `password-protection` `landing-page` `form` `authentication`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/password.liquid) （ライセンス: MIT、36行）
- **ファイル:** `sections/password.liquid`

**説明:** ストアにパスワード保護が有効な場合に表示するランディングページセクション。訪問者がパスワードを入力してストアにアクセスできます。

**用途:** password テンプレートで使用。ストアのプレオープンやメンテナンス中に顧客をゲートする際に活用します。

**設置場所:** sections/password.liquid に配置。password.liquid テンプレートで `{% section 'password' %}` で呼び出します。

**注意点:** shop.password_message は管理画面の「オンラインストア設定」で設定したメッセージが表示されます。形式 'storefront_password' はShopifyが提供する専用フォームで、カスタム変更は非推奨です。エラーメッセージの表示は default_errors フィルターに依存するため、多言語対応時は翻訳ファイルの確認が必要です。

<details><summary>コード(36行)を見る</summary>

```liquid
{% comment %}
  This section is used in the password template to render landing page shown
  when password protection is applied to a store.

  https://shopify.dev/docs/storefronts/themes/architecture/templates/password
{% endcomment %}

<h1>{{ 'password.title' | t }}</h1>

{% if shop.password_message %}
  <p>{{ shop.password_message }}</p>
{% endif %}

{% form 'storefront_password' %}
  {% if form.errors %}
    {{ form.errors | default_errors }}
  {% endif %}

  <label for="password-input">
    {{ 'password.password' | t }}
  </label>

  <input type="password" name="password" id="password-input">

  <button type="submit">
    {{ 'password.enter' | t }}
  </button>
{% endform %}

{% schema %}
{
  "name": "t:general.password",
  "settings": []
}
{% endschema %}
```

</details>


### 39. 🧩 スニペット メタフィールド値でコレクション商品をソート

**カテゴリ:** メタフィールド/メタオブジェクト ／ **難易度:** 中級 ／ **タグ:** `metafield` `sort` `collection` `product-order`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Sort Shopify collection by metafield/sort-shopify-collection-products-by-metafield-value-commentless.liquid) （ライセンス: MIT、24行）
- **ファイル:** `Sort Shopify collection by metafield/sort-shopify-collection-products-by-metafield-value-commentless.liquid`

**説明:** コレクション内の商品を、メタフィールド（global.order）に設定した数値で自動ソートします。メタフィールドに値がない商品は末尾に配置されます。

**用途:** コレクションページで、管理画面から設定した表示順序を反映させたい場合に使用。手動でテンプレートの商品並び順を調整できます。

**設置場所:** collection.liquid や collection テンプレート内で、`collection.products` をループする箇所に置き換えます。このコードの最後の `for` ループで整列済みの商品を出力します。

**注意点:** メタフィールド `global.order` は事前に各商品に設定しておく必要があります。数値以外の値が入るとソートが不正確になるため、必ず整数値を設定してください。大量商品（100+）の場合はパフォーマンス低下の可能性があるため、テーマのページネーション機能と組み合わせて使用を推奨します。

<details><summary>コード(24行)を見る</summary>

```liquid
{% assign newArray = false %}
{% assign zeroFill = '0000' %}
{% assign zeroFillSize = zeroFill | size %}
{% for product in collection.products %}
	{% assign indexCharSize = forloop.index0 | append:'' | size %}
	{% assign toSlice = zeroFillSize | minus:indexCharSize %}
	{% assign tmpZeroFill = zeroFill | slice:0,toSlice %}
	{% assign newOrder = product.metafields.global.order | default:'999999' %}
	{% assign matrix = tmpZeroFill | append:newOrder | append:'.'  | append:forloop.index0 %}
	{% if newArray %}
		{% assign tmpIndex = matrix | split:',' %}
		{% assign newArray = newArray | concat:tmpIndex %}
	{% else %}
		{% assign newArray = matrix | split:',' %}
	{% endif %}
{% endfor %}
{% assign newArray = newArray | sort %}
{% for newArrayItem in newArray %}
	{% assign i = newArrayItem | split:'.' | last | abs %}
	<div>
		<h2>{{ collection.products[i].title }}</h2>
		<p>My original index was {{ i }}, but now it is {{ forloop.index0 }}</p>
	</div>
{% endfor %}
```

</details>


### 40. 🧩 スニペット セクションヘッダー

**カテゴリ:** UI部品 ／ **難易度:** 初級 ／ **タグ:** `section` `header` `reusable-component` `typography` `render`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/section-header.liquid) （ライセンス: MIT、24行）
- **ファイル:** `snippets/section-header.liquid`

**説明:** 複数のセクションで共通して使える見出しと説明文を表示するコンポーネント。タイトルと説明のフォントサイズをセクション設定で制御できます。

**用途:** コレクションページやランディングページの各セクションの冒頭に、統一されたヘッダーを配置する際に利用します。

**設置場所:** `snippets/section-header.liquid` に配置し、セクションファイル内で `{% render 'section-header' %}` または `{% render 'section-header', class: 'カスタムクラス' %}` で呼び出します。

**注意点:** タイトルと説明文の両方が空の場合、ヘッダー要素全体がレンダリングされません。セクション設定で `header_title_font_size` および `header_description_font_size` クラスを定義しておく必要があります。説明文には RTE（リッチテキストエディタ）クラスが適用されるため、HTML マークアップを含める際は注意してください。

<details><summary>コード(24行)を見る</summary>

```liquid
{% comment %}
  Renders a header (title and description) that is usually the same accross sections

  Accepts:
  - class: {String} (Optional) An optional class (or classes) to apply to header element

  Usage:
  {% render 'section-header' %}
{% endcomment %}

{% if section.settings.header_title != blank or section.settings.header_description != blank %}
  <header class="section-header text-center {{ class }}">
    {% unless section.settings.header_title == blank %}
      <h2 class="title {{ section.settings.header_title_font_size }}">
        {{ section.settings.header_title }}
      </h2>
    {% endunless %}
    {% unless section.settings.header_description == blank %}
      <div class="description rte opacity-70 {{ section.settings.header_description_font_size }}">
        {{ section.settings.header_description }}
      </div>
    {% endunless %}
  </header>
{% endif %}
```

</details>


---

## 比較: v1 vs v2

### 実行コスト・処理

| 項目 | v1 (旧プロンプト) | v2 (新プロンプト) | 差分 |
|---|---:|---:|---:|
| 処理時間（秒） | — | 34.8 | — |
| 入力 tokens | 69,828 | 122,429 | +52,601 |
| 出力 tokens | 19,617 | 21,116 | +1,499 |
| キャッシュ作成 tokens | 0 | 0 | 0 |
| キャッシュ読込 tokens | 0 | 0 | 0 |
| 推定コスト (USD) | $0.1679 | $0.2280 | +$0.0601 |

### カテゴリ分布の変化

| カテゴリ | v1 | v2 | 差分 |
|---|---:|---:|---:|
| レイアウト/ナビ | 19 | 0 | -19 |
| ページテンプレート | 0 | 10 | +10 |
| コレクション/検索 | 4 | 3 | -1 |
| 商品表示 | 4 | 3 | -1 |
| ユーティリティ | 3 | 3 | 0 |
| SEO/構造化データ | 3 | 3 | 0 |
| UI部品 | 0 | 5 | +5 |
| ヘッダー/フッター/ナビゲーション | 0 | 4 | +4 |
| フィルター | 4 | 0 | -4 |
| リファレンス/フィルター | 0 | 4 | +4 |
| テーマ基盤 | 0 | 4 | +4 |
| タグ | 3 | 0 | -3 |
| その他 | 3 | 0 | -3 |
| API連携/JSON出力/JS統合 | 0 | 3 | +3 |
| オブジェクト | 3 | 0 | -3 |
| リファレンス/オブジェクト | 0 | 3 | +3 |
| リファレンス/タグ | 0 | 3 | +3 |
| API連携/JS | 2 | 0 | -2 |
| メタフィールド | 2 | 0 | -2 |
| 顧客アカウント | 0 | 1 | +1 |
| メタフィールド/メタオブジェクト | 0 | 1 | +1 |

### 難易度分布の変化

| 難易度 | v1 | v2 |
|---|---:|---:|
| 初級 | 30 | 31 |
| 中級 | 16 | 17 |
| 上級 | 4 | 2 |
