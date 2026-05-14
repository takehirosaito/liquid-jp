# liquid-jp.jp Phase 1 サンプル50件レポート

生成日時: 2026-05-13 20:36 ／ モデル: `claude-haiku-4-5-20251001`

## サマリ

- 件数: **50件**（成功 50 / 失敗 0）
  - コミュニティスニペット: **40件**
  - 公式リファレンス（theme-liquid-docs）: **10件**
- 処理時間: 28.4秒（並列8）
- API コスト: **$0.1679**（入力 69,828 tok ＋ 出力 19,617 tok）

### カテゴリ分布

| カテゴリ | 件数 |
|---|---:|
| レイアウト/ナビ | 19 |
| 商品表示 | 4 |
| コレクション/検索 | 4 |
| フィルター | 4 |
| その他 | 3 |
| ユーティリティ | 3 |
| SEO/構造化データ | 3 |
| タグ | 3 |
| オブジェクト | 3 |
| API連携/JS | 2 |
| メタフィールド | 2 |

### 難易度分布

| 難易度 | 件数 |
|---|---:|
| 初級 | 30 |
| 中級 | 16 |
| 上級 | 4 |

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

以下を確認してください:

1. **日本語訳の品質** — 自然な日本語か、誤訳・直訳が残っていないか
2. **カテゴリ分類** — カテゴリ候補の粒度が妥当か、分類ミスがないか
3. **caveats（注意点）の有用性** — 実務で役立つ具体性があるか、汎用的すぎないか
4. **タグの一貫性** — 同じ概念で表記揺れがないか（例: `product` vs `products`）
5. **リファレンスとスニペットの書き分け** — 用途・設置場所の説明が両者で適切か

修正指示があれば、`scripts/translate.py` の `SYSTEM_PROMPT` を調整して再生成します。

---

## 📘 公式リファレンス サンプル（10件）

### 1. 📘 リファレンス sort_by フィルター

**カテゴリ:** フィルター ／ **難易度:** 初級 ／ **タグ:** `collection` `sort` `url` `filter`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** コレクション URL にソート条件を追加するフィルター。手動・売上順・タイトル・価格・作成日時などで並び替え可能な URL を生成します。

**用途:** コレクションページで「売上順」「価格が安い順」などのソートリンクを作成する際に使用。ユーザーが異なる並び順で商品を閲覧できるようにします。

**設置場所:** Liquid テンプレート内で `{{ collection.url | sort_by: 'best-selling' }}` のように使用。URL パラメータとして機能するため、リンク href や form action に埋め込みます。

**注意点:** このフィルターは collection.url オブジェクトプロパティにのみ適用可能。パラメータ値は 'manual'、'best-selling'、'title-ascending'、'title-descending'、'price-ascending'、'price-descending'、'created-ascending'、'created-descending' から選択必須。url_for_type・url_for_vendor フィルターと組み合わせて使用できます。

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


### 2. 📘 リファレンス escape フィルター

**カテゴリ:** フィルター ／ **難易度:** 初級 ／ **タグ:** `string` `security` `xss` `html` `escape`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** HTML の特殊文字（&、<、>、' など）をエスケープシーケンスに変換するフィルター。ユーザー入力やデータベースの値を安全に表示する際に使用します。

**用途:** ユーザーが入力したテキストやコメント、商品説明などを HTML として解釈されないように表示したい場合。XSS 対策が必要な箇所で活用します。

**設置場所:** Liquid テンプレート内で `{{ 変数 | escape }}` の形式で使用。商品詳細、レビュー表示、カート内など、外部データを出力する箇所に記述します。

**注意点:** 既に HTML エンティティでエンコード済みの値に重ねて使用すると二重エスケープになります。JSON 文字列が含まれる場合は別途対応が必要。日本語を含むテキストも正常に処理されます。

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


### 3. 📘 リファレンス floor フィルター(数値を切り捨て)

**カテゴリ:** フィルター ／ **難易度:** 初級 ／ **タグ:** `math` `number` `rounding`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** 数値を小数点以下で切り捨て、最も近い整数に丸めるフィルターです。

**用途:** 商品の在庫数や割引率など、整数値が必要な場面で小数の計算結果を処理する際に使用します。

**設置場所:** Liquid テンプレート内で `{{ 数値 | floor }}` の形で使用します。

**注意点:** 負の数にも対応しており、-1.5 は -2 に丸められます。計算精度が必要な場合は事前に検証してください。

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


### 4. 📘 リファレンス 商品タイプへのリンクを生成するフィルター

**カテゴリ:** フィルター ／ **難易度:** 初級 ／ **タグ:** `collection` `product` `link` `filter`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、48行）
- **ファイル:** `data/filters.json`

**説明:** 指定した商品タイプの全商品を一覧表示するコレクションページへのリンク（`<a>` タグ）を生成します。HTML属性のカスタマイズにも対応しています。

**用途:** 商品詳細ページやコレクションページで「この商品タイプの他の商品を見る」というリンクを表示したい場合に使用します。

**設置場所:** Liquid テンプレート内で `{{ '商品タイプ名' | link_to_type }}` または `{{ '商品タイプ名' | link_to_type: class: 'css-class' }}` の形で使用します。

**注意点:** 入力値は文字列型である必要があります。出力は HTML 文字列です。クラス名など HTML 属性を追加する場合は、フィルターのパラメータで属性名とその値を指定してください。

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


### 5. 📘 リファレンス decrement タグ

**カテゴリ:** タグ ／ **難易度:** 初級 ／ **タグ:** `variable` `counter` `increment` `scope`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、28行）
- **ファイル:** `data/tags.json`

**説明:** 変数を -1 で初期化し、呼び出すたびに 1 ずつ減少させるタグ。`increment` と変数を共有し、`assign` や `capture` とは独立している。

**用途:** カウンター機能やループ内で逆順のインデックスが必要なとき、複数セクションで共有するカウント値を管理する場合に使用。

**設置場所:** Liquid テンプレート内で `{% decrement 変数名 %}` の形で使用。宣言したレイアウト・テンプレート・セクションファイル内および includeされたスニペット内で有効。

**注意点:** predefined Liquid オブジェクト(product, cart など)と同じ名前の変数を作ると上書きされ、Liquid オブジェクトにアクセスできなくなる。`increment` と変数を共有するため、同じ変数名で両方を使う場合は挙動を把握する必要がある。

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


### 6. 📘 リファレンス for タグ：配列をループで繰り返す

**カテゴリ:** タグ ／ **難易度:** 初級 ／ **タグ:** `iteration` `array` `loop` `limit` `offset` `range`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、113行）
- **ファイル:** `data/tags.json`

**説明:** 配列の全要素または指定条件に基づいて要素をループ処理し、各要素に対して式を繰り返し実行するタグです。1ループで最大50回の反復に対応します。

**用途:** 商品一覧・コレクション・カート内の複数アイテムを順番に表示する際、または数値範囲でカウントしたい場合に使用します。

**設置場所:** Liquid テンプレート内で `{% for variable in array %} 〜 {% endfor %}` の形で、配列を繰り返したい箇所に記述します。

**注意点:** 単一ループで50回を超える反復が必要な場合は `paginate` タグを使用してください。`limit` パラメータは大量データ取得の性能低下につながるため、ページ分割可能な配列には `paginate` を推奨します。ループ内で `forloop` オブジェクトにより現在のインデックスなど情報にアクセス可能です。

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


### 7. 📘 リファレンス else タグ（ループ空時の処理）

**カテゴリ:** タグ ／ **難易度:** 初級 ／ **タグ:** `for` `loop` `conditional` `empty`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、40行）
- **ファイル:** `data/tags.json`

**説明:** for ループが 0 件の場合に実行するデフォルト処理を指定するタグです。ループ対象が空の配列のときに代わりに表示する内容を定義できます。

**用途:** 商品がないコレクション、カートが空のとき、検索結果がないときなど、ループ対象が存在しない場合に「該当なし」メッセージを表示する。

**設置場所:** {% for %} タグ内で、{% endfor %} の直前に {% else %} ～ {% endfor %} の形で Liquid テンプレート内に記述します。

**注意点:** else は for ループ専用です。if タグの else とは異なります。ループが 1 件以上あれば else 内の処理は実行されません。

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

**カテゴリ:** オブジェクト ／ **難易度:** 中級 ／ **タグ:** `metafield` `measurement` `product` `dimension` `weight` `volume`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、86行）
- **ファイル:** `data/objects.json`

**説明:** メタフィールドの寸法・容積・重量タイプから取得する、計測値・単位・種類を保持するオブジェクト。数値と単位をセットで扱える。

**用途:** 商品の容量（ml）、重さ（kg）、サイズ（cm）などをメタフィールドで管理し、テンプレートに表示する際に使用。

**設置場所:** metafield.value から取得できる。例: `{{ product.metafields.details.milk_container_volume.value.value }}` で数値、`{{ product.metafields.details.milk_container_volume.value.unit }}` で単位を参照。

**注意点:** measurement オブジェクトは metafield タイプが dimension / volume / weight のときだけ使用可。他の metafield タイプでは異なる構造。value（数値）と unit（単位）は文字列型ではなく number と string なため、計算や比較時は型チェックが必要。

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

**カテゴリ:** オブジェクト ／ **難易度:** 初級 ／ **タグ:** `3d` `model` `media` `product` `cdn`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、74行）
- **ファイル:** `data/objects.json`

**説明:** 3D モデルのソースファイル情報を保持するオブジェクト。ファイル形式、MIME タイプ、CDN URL にアクセスできます。

**用途:** 商品ページで 3D モデルを表示する際に、{{ product.featured_media.sources[0].format }}、{{ product.featured_media.sources[0].mime_type }}、{{ product.featured_media.sources[0].url }} などで、モデルファイルの詳細情報を参照して動的に処理します。

**設置場所:** Liquid テンプレート内で {{ model_source.format }}、{{ model_source.mime_type }}、{{ model_source.url }} の形式で参照。通常は product.featured_media.sources の配列要素として利用します。

**注意点:** このオブジェクトは model オブジェクト内の sources 配列に格納され、単独では利用できません。format には glb、usdz などのファイル形式が、mime_type には model/gltf-binary などの値が入ります。CDN URL は自動生成され、Shopify CDN から配信されます。

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

**カテゴリ:** オブジェクト ／ **難易度:** 中級 ／ **タグ:** `remote_product` `multivendor` `shop_info` `liquid_reference`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、69行）
- **ファイル:** `data/objects.json`

**説明:** リモートソースから取得したオブジェクト（他店舗の商品など）の供給元情報を扱うオブジェクト。オブジェクトがどこから提供されたか、供給元の店舗情報にアクセスできます。

**用途:** マルチベンダーマーケットプレイスやストアフロント連携で、他店舗から取得した商品の出品元情報や提供形態を表示する際に使用します。

**設置場所:** remote_product オブジェクトの直下で `{{ remote_product.remote_details.type }}` または `{{ remote_product.remote_details.shop }}` の形で参照します。

**注意点:** グローバルには利用できず、remote_product から派生したデータのみでアクセス可能。現在 type は「seller」のみサポートされており、将来拡張の可能性あり。shop プロパティは remote_shop オブジェクト型。

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

### 1. 🧩 スニペット 固定ページ用セクション（約ページ・お問合せ）

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `page` `template` `section` `basic`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/page.liquid) （ライセンス: MIT、18行）
- **ファイル:** `sections/page.liquid`

**説明:** ページテンプレートから呼び出される基本セクション。ページタイトルと本文コンテンツを表示します。Skeleton Theme の標準的な実装です。

**用途:** Shopify管理画面で作成した固定ページ（アバウトページ、利用規約、プライバシーポリシーなど）を、シンプルにフロントエンドに表示する場合に使用します。

**設置場所:** sections/page.liquid として新規作成、または page.liquid テンプレート内で {% section 'page' %} として呼び出します。

**注意点:** このセクションは最小限の実装のため、スタイリング（CSSクラス）が別途必要です。page.contentはAdminから管理されるHTMLをそのまま出力するため、XSS対策は必須です。schema設定がないため、エディタでのカスタマイズオプションは追加できません。

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


### 2. 🧩 スニペット アクセスしたドメインで表示内容を切り替える

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `request` `domain` `multiregion` `conditional` `asset`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Get current domain name with Liquid/request_host.liquid) （ライセンス: MIT、15行）
- **ファイル:** `Get current domain name with Liquid/request_host.liquid`

**説明:** 複数ドメインで運営されているストアで、request.host を使ってドメインを判定し、ドメイン固有のバナー画像や表示内容を動的に変更できます。マルチリージョン・マルチブランド運営時に活躍します。

**用途:** 複数国・複数リージョンの独立ドメイン（例：.com.au、.com）で同じストアシステムを運用する場合、ドメインごとにバナーテキスト・ナビゲーション・プロモーション内容を変えたいシーン。

**設置場所:** theme.liquid の <body> 直下、または header.liquid・sections/header.liquid など、全ページで共通表示させたい箇所。店舗ロゴやナビゲーション付近が最適。

**注意点:** request.host は開発ストア（*.myshopify.com）では機能しないため、カスタムドメイン設定が必須。条件分岐が増えると可読性が低下するため、3ドメイン以上の場合は Shopify Functions や Settings で管理の検討を推奨。

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


### 3. 🧩 スニペット 商品ページ区切り線ブロック

**カテゴリ:** 商品表示 ／ **難易度:** 初級 ／ **タグ:** `product` `section-block` `separator` `styling` `bootstrap`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-block-separator.liquid) （ライセンス: MIT、15行）
- **ファイル:** `snippets/product-block-separator.liquid`

**説明:** 商品ページセクションに区切り線を挿入するブロック。上下の余白、色、透明度、高さをカスタマイズ可能です。

**用途:** 商品詳細ページの複数セクション間に視覚的な区切りを追加する際に使用。セクションエディタでブロックとして設置します。

**設置場所:** snippets/product-block-separator.liquid として保存し、商品セクション内で {% include 'product-block-separator' %} で呼び出します。

**注意点:** block.settings の値（pt, pb, bg_color, bg_opacity, height）はセクション側で定義が必須。BootstrapのCSSクラス（pt-*, my-0）に依存しており、テーマに同等のスペーシングクラスがない場合はスタイルが反映されません。bg_opacity は%単位で設定してください。

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


### 4. 🧩 スニペット クイズ形式での商品フィルタリング用データ生成

**カテゴリ:** API連携/JS ／ **難易度:** 上級 ／ **タグ:** `quiz` `filter` `json` `collection` `product`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/Quiz/snippets/quiz-data.liquid) （ライセンス: MIT、93行）
- **ファイル:** `Quiz/snippets/quiz-data.liquid`

**説明:** クイズの回答に基づいて商品を絞り込むため、コレクション内の全商品データと条件別フィルタ設定をJSON化して準備します。価格・タグ・タイプ・ベンダー・オプション値による複数条件フィルタに対応。

**用途:** クイズセクション内で、ユーザーの選択に応じて該当商品を動的に表示する際に使用。診断系のセクション構築で活用。

**設置場所:** snippets/quiz-data.liquid として作成し、クイズセクション（sections/quiz.liquid など）から include で呼び出す。

**注意点:** section.settings.filter_collection の値が実在するコレクションハンドルである必要があります。250件以上の商品がある場合はページネーション対応済みですが、大規模コレクションではLiquid処理が重くなる可能性があります。フロントエンド側でJavaScriptでJSON解析・フィルタ実行が必須。

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


### 5. 🧩 スニペット 階層付きナビゲーションメニュー

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `navigation` `menu` `header` `liquid` `snippet`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/snippets/layout-menu.liquid) （ライセンス: MIT、19行）
- **ファイル:** `shopify/snippets/layout-menu.liquid`

**説明:** Shopify の メインメニューをLoop して、1階層目と2階層目（サブメニュー）を表示します。カスタムクラスやインラインスタイルに対応した柔軟な構造です。

**用途:** ヘッダーやフッターのナビゲーションメニュー表示に使用します。プロダクトカテゴリや情報ページの階層化したメニューを実装する際に活用できます。

**設置場所:** snippets/layout-menu.liquid として作成し、header.liquid や theme.liquid の nav 要素内で {% include 'layout-menu' %} で呼び出します。

**注意点:** linklists.main-menu は Shopify管理画面で「メインメニュー」という名前のメニューが必須です。サブメニューは1階層のみ対応（3階層以上は表示されません）。class と style パラメータはオプション引数として呼び出し時に {{ 'layout-menu' | include: class: 'nav-class', style: 'color: red;' }} で渡します。

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


### 6. 🧩 スニペット 404エラーページ（ファイルなし）

**カテゴリ:** その他 ／ **難易度:** 初級 ／ **タグ:** `template` `error-page` `404` `redirect`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/404.liquid) （ライセンス: MIT、16行）
- **ファイル:** `templates/404.liquid`

**説明:** ページが見つからない場合に表示するテンプレート。訪問者に対して分かりやすく「ページが存在しない」ことを通知します。

**用途:** 存在しないURL（削除されたページ、リンク切れ）にアクセスした時に自動的に表示されます。

**設置場所:** templates/404.liquid として設置済みテンプレート（変更不可、Shopifyが自動適用）

**注意点:** このファイルはShopifyが自動的に認識するため、ファイル名・ロケーションの変更は不可。デザイン修正はHTMLやCSSの部分のみ可能。リダイレクト設定は管理画面「ナビゲーション」タブから行う必要があります。

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


### 7. 🧩 スニペット 成功チェックマークアイコン

**カテゴリ:** ユーティリティ ／ **難易度:** 初級 ／ **タグ:** `icon` `svg` `ui` `success` `accessibility`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/snippets/icon-success.liquid) （ライセンス: MIT、6行）
- **ファイル:** `snippets/icon-success.liquid`

**説明:** 完了・成功状態を表すチェックマークアイコンです。緑色の円形背景に白いチェック記号を配置した SVG で、注文完了画面やメッセージ表示に使えます。

**用途:** 注文確認画面、決済完了メッセージ、フォーム送信成功時、ポップアップ通知など、ユーザーに成功状態を視覚的に伝えたいシーンで使用します。

**設置場所:** snippets/icon-success.liquid として配置し、{% include 'icon-success' %} で他のテンプレートから呼び出して使用します。

**注意点:** SVG の fill・stroke 色が固定値(#428445 と white)なので、テーマカラーに合わせたい場合は色値を変更が必要です。aria-hidden="true" が設定されているため、スクリーンリーダーには読み上げられません。

<details><summary>コード(6行)を見る</summary>

```liquid
<svg aria-hidden="true" focusable="false" role="presentation" class="icon icon-success" viewBox="0 0 13 13">
  <path d="M6.5 12.35C9.73087 12.35 12.35 9.73086 12.35 6.5C12.35 3.26913 9.73087 0.65 6.5 0.65C3.26913 0.65 0.65 3.26913 0.65 6.5C0.65 9.73086 3.26913 12.35 6.5 12.35Z" fill="#428445" stroke="white" stroke-width="0.7"/>
  <path d="M5.53271 8.66357L9.25213 4.68197" stroke="white"/>
  <path d="M4.10645 6.7688L6.13766 8.62553" stroke="white">
</svg>
```

</details>


### 8. 🧩 スニペット ランダム数値を生成するスニペット

**カテゴリ:** ユーティリティ ／ **難易度:** 初級 ／ **タグ:** `utility` `random` `snippet` `javascript-free` `performance`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/random-number.liquid) （ライセンス: MIT、13行）
- **ファイル:** `random-number.liquid`

**説明:** 指定した範囲内のランダムな整数を生成します。デフォルトは0〜9999999の範囲で、コード内で数字を変更することで任意の範囲に調整できます。

**用途:** A/Bテスト、ランダム表示切り替え、くじ引き機能、ランダム割引コードの生成などに使用できます。

**設置場所:** snippets/random-number.liquid として保存し、ランダム値が必要な箇所（例：sections/ や theme.liquid）から {% render 'random-number' %} で呼び出します。

**注意点:** 現在の秒単位タイムスタンプを使用しているため、同一秒内に複数回レンダリングされると同じ値になる可能性があります。min と max の値（8行目・9行目）を変更して範囲をカスタマイズしてください。

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


### 9. 🧩 スニペット テーマのCSS変数（フォント・カラー・幅）を一括設定

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `css-variables` `theme-settings` `typography` `design-tokens` `performance`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/snippets/css-variables.liquid) （ライセンス: MIT、19行）
- **ファイル:** `snippets/css-variables.liquid`

**説明:** Shopify テーマ設定から読み込んだフォント・色・ページ幅などをCSS変数（:root）として定義し、全ページで統一的に利用できるようにします。フォントの複数ウェイトとスタイルも同時に読み込みます。

**用途:** theme.liquid または layout/theme.liquid の <head> 内に組み込み、テーマ全体のデザイン変数を一元管理するシーン。カスタマイザー設定との同期を自動化したいとき。

**設置場所:** snippets/css-variables.liquid として作成し、theme.liquid の <head> 内で {% include 'css-variables' %} で読み込む。

**注意点:** settings.type_primary_font、settings.max_page_width など、テーマ設定ファイル（config/settings_schema.json）に対応するキーが必要。font_face と font_modify フィルタは Shopify Liquid 標準提供（他の外部フォントツールは不要）。CSS変数の値が空の場合は fallback_families や font_name の設定確認が必須。

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


### 10. 🧩 スニペット ギフトカード金額に応じた商品画像を自動表示

**カテゴリ:** 商品表示 ／ **難易度:** 中級 ／ **タグ:** `gift-card` `variant` `image` `dynamic` `linklists`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Use variant image on Gift Card template/capture-image.liquid) （ライセンス: MIT、16行）
- **ファイル:** `Use variant image on Gift Card template/capture-image.liquid`

**説明:** ギフトカード金額と同じ価格の商品バリアントから画像を取得し、テンプレートに動的に反映させます。バリアントに画像がない場合はデフォルト画像を使用します。

**用途:** ギフトカードテンプレートで、購入金額ごとに異なるデザイン画像を表示したい場合に使います。

**設置場所:** gift_card.liquid またはギフトカード表示用のセクション内の、画像タグの直前に配置します。

**注意点:** admin-gift-card リンクリストが設定されていることが必須です。バリアント価格がギフトカード金額と完全に一致する必要があり、小数点以下の誤差があると認識されません。img_url フィルタの '949x' サイズは環境に応じて変更してください。

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


### 11. 🧩 スニペット ナビゲーションバーのロゴ表示

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `header` `logo` `image` `responsive`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/navbar-logo.liquid) （ライセンス: MIT、18行）
- **ファイル:** `snippets/navbar-logo.liquid`

**説明:** ショップロゴをナビゲーションバーに表示するコンポーネントです。ロゴ画像が設定されていない場合は、ショップ名を代替表示します。

**用途:** テーマのヘッダー・ナビゲーション内のロゴエリアに配置。ホームページへのリンク付きロゴを実装します。

**設置場所:** snippets/navbar-logo.liquid として保存するか、sections/ 配下のヘッダーセクションから include で呼び込んでください。

**注意点:** block.settings.logo と block.settings.logo_height がテーマ設定に存在する必要があります。アスペクト比の自動計算に logo.aspect_ratio を使用しているため、Shopify 提供の画像オブジェクトが必須です。

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


### 12. 🧩 スニペット FAQ アコーディオン（リッチスキーマ対応）

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 中級 ／ **タグ:** `faq` `accordion` `schema` `seo` `animation` `js`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/FAQ/sections/faq.liquid) （ライセンス: MIT、352行）
- **ファイル:** `FAQ/sections/faq.liquid`

**説明:** 質問と回答をアコーディオン形式で表示し、タップで開閉できるセクション。Google検索結果に対応したFAQスキーマも自動生成します。

**用途:** 商品ページやサイトフッター、専用ページで顧客からのよくある質問を整理して表示。SEO評価の向上にも役立ちます。

**設置場所:** sections/faq.liquid として保存し、theme.json で section として登録。対応するアセット faq.js も併せて asset フォルダに配置が必要。

**注意点:** faq.js ファイルが asset フォルダに必須。JavaScriptで動作・アニメーションを制御するため、JS無効環境では全FAQ が常に表示。モバイル・デスクトップで異なるフォントサイズに対応していますが、clamp() CSS非対応ブラウザでは固定値になる可能性があります。

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


### 13. 🧩 スニペット フッターナビゲーションと著作権表示

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `footer` `navigation` `linklist` `section`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/footer.liquid) （ライセンス: MIT、25行）
- **ファイル:** `shopify/sections/footer.liquid`

**説明:** フッターメニュー(リンクリスト)と著作権表記を表示するセクション。Shopify管理画面からリンク設定を変更できます。

**用途:** 全ページ共通のフッター領域に配置し、サイトマップ的なナビゲーションと企業情報を表示する場面で使用。

**設置場所:** sections/footer.liquid として新規作成、または既存フッターセクションに統合。

**注意点:** footer というリンクリストが管理画面で事前作成されていないと、リンクが表示されません。メニュー設定 > リンクリストから『Footer』を作成し、リンクを追加してください。著作権年号は固定値のため、動的に更新する場合は JavaScript か Liquid フィルタ(今年の年号取得)の追加が必要です。

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


### 14. 🧩 スニペット 検索結果を最下層カテゴリ別に表示

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `search` `collection` `pagination` `liquid-filter` `category-hierarchy`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/search.liquid) （ライセンス: MIT、17行）
- **ファイル:** `templates/search.liquid`

**説明:** 検索結果の商品を、自動生成コレクションの最下層カテゴリでグループ化して表示します。商品ごとに最も詳細なカテゴリへのリンクを自動生成し、画像とタイトルで一覧表示します。

**用途:** 検索ページで商品を階層化されたカテゴリリンク経由で表示したい場合。ユーザーが検索結果から最も関連度の高いカテゴリページへアクセスできるようにします。

**設置場所:** templates/search.liquid の検索結果ループ部分に設置します。既存のコレクション自動分類に依存する場合はそのまま使用、カスタムコレクション構造の場合は modified_handle の処理を調整してください。

**注意点:** product.collections はハンドルの長さでソートされているため、コレクション命名規則が『hardware-カテゴリ名』の形式であることが前提です。/pages/category/ ページが存在し、アンカーリンク (#product.handle) で正しくスクロール位置が指定される必要があります。カテゴリ構造が3階層以上ない場合は最下層とならないため、実装前に自動コレクションの生成ルールを確認してください。

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


### 15. 🧩 スニペット ギフトカード購入画面テンプレート

**カテゴリ:** その他 ／ **難易度:** 中級 ／ **タグ:** `gift-card` `qrcode` `template` `checkout`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/templates/gift_card.liquid) （ライセンス: MIT、204行）
- **ファイル:** `templates/gift_card.liquid`

**説明:** Shopify のギフトカード購入完了ページを表示するテンプレート。QRコード生成、カード番号の表示・コピー機能、残高表示などを実装しています。Storefront API 非対応のため独立したテンプレートとして構成されています。

**用途:** 顧客がギフトカードを購入後に表示される専用ページで使用。QRコードで読み取れるようにしたり、ギフトカードコードをコピーして共有できるようにします。

**設置場所:** templates/gift_card.liquid に配置。テーマ全体の layout none で独立したドキュメント構造を持つため、既存のテーマレイアウトを継承しません。

**注意点:** Storefront API では未サポートのため theme.liquid の layout を使用できず、独自の HTML 構造が必要。qrcode.js(Shopify アセット)の読み込みが必須。gift_card オブジェクト（qr_identifier、code、initial_value など）はこのテンプレートでのみ利用可能。currency_code_enabled、colors_*、type_*_font などの settings は管理画面設定に依存。

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


### 16. 🧩 スニペット WebSite検索アクション構造化データ

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `seo` `json-ld` `schema` `search` `structured-data`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/json-ld-search.liquid) （ライセンス: MIT、17行）
- **ファイル:** `json-ld-search.liquid`

**説明:** Google検索結果に店舗の検索機能を表示するための構造化データ(JSON-LD)を出力します。Googleサイトリンク検索ボックスの表示条件を満たします。

**用途:** theme.liquid または layout/theme.liquid に設置し、全ページで検索スキーマを有効化する場合に使用します。SEO効果で検索結果ページに検索ボックスが表示される可能性が高まります。

**設置場所:** theme.liquid の <head> タグ内、または snippets/json-ld-search.liquid として作成後に {% render 'json-ld-search' %} で呼び出し

**注意点:** 構造化データの存在だけでは Google が検索ボックス機能を表示するとは限らず、サイトのトラフィック・評判も考慮されます。複数の JSON-LD スクリプトがある場合は重複チェックが必要です。

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


### 17. 🧩 スニペット パスワード保護ページのHTMLレイアウト

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `layout` `password-page` `meta` `css`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/layout/password.liquid) （ライセンス: MIT、20行）
- **ファイル:** `layout/password.liquid`

**説明:** メンテナンス中やプライベートセール時に表示するパスワード保護ページの基本構造。CSS変数、クリティカルCSS、メタタグを組み込み、SEO対応のHTML骨組みを提供します。

**用途:** ストア全体をパスワード保護する際、Shopifyのパスワードページ用レイアウトとして使用。メンテナンス期間中の来訪者に対してブランド統一された画面を表示します。

**設置場所:** layout/password.liquid に配置。Shopifyの専用レイアウトファイルで、パスワード保護モード時に自動的に適用されます。

**注意点:** content_for_header と content_for_layout は Shopify 予約変数のため置換不可。css-variables と meta-tags スニペットが theme に存在する必要があります。critical.css アセットが事前にアップロードされていないと 404 エラーになります。

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


### 18. 🧩 スニペット 検索タイプを判定して表示

**カテゴリ:** コレクション/検索 ／ **難易度:** 初級 ／ **タグ:** `search` `url-parameter` `detection` `conditional`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Detect search type used in searches/show-search-type.liquid) （ライセンス: MIT、17行）
- **ファイル:** `Detect search type used in searches/show-search-type.liquid`

**説明:** 検索URLから検索タイプ(商品/ページ/記事)を抽出し、該当する場合のみ検索対象を表示します。不正なタイプはフィルタリングされます。

**用途:** 検索結果ページ(search.liquid)で、ユーザーが実施した検索の種類を検出して、結果上部に「この検索は商品です」といった案内を表示する際に使用します。

**設置場所:** search.liquid または searches/show-search-type.liquid(検索結果テンプレート内の結果表示上部)

**注意点:** URLパラメータ type= が存在する場合のみ動作します。URLパラメータが存在しない環境では何も出力されません。許可リスト内('product,page,article')にないタイプは出力されないため、カスタム検索タイプがある場合は allowedTypes を編集が必要です。

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


### 19. 🧩 スニペット 支払い方法アイコン表示

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `payment` `icons` `footer` `accessibility` `bootstrap`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/payment-icons.liquid) （ライセンス: MIT、18行）
- **ファイル:** `snippets/payment-icons.liquid`

**説明:** ストアで利用可能な支払い方法をアイコンで視覚的に表示します。各アイコンにはツールチップで支払い方法名が表示されます。セキュアな決済であることを示す説明文も表示できます。

**用途:** フッターやチェックアウトページ、商品ページなど、顧客に対応している支払い方法を明示したい場所で使用します。

**設置場所:** snippets/payment-icons.liquid として新規作成、または footer.liquid、product.liquid などで include タグで呼び込んで使用します。

**注意点:** payment_type_svg_tag フィルターは Shopify 標準フィルターですが、テーマによっては CSS/JS(Bootstrap のツールチップ機能)が必要です。type 変数の値は shop.enabled_payment_types から自動取得されるため、手動変更不可です。翻訳キー 'general.accessibility.payment_methods' と 'general.payment_icons.secure' は theme.json の翻訳ファイルに存在する必要があります。

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


### 20. 🧩 スニペット 画像上にインタラクティブなツールチップを配置

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 上級 ／ **タグ:** `section` `interactive` `responsive` `animation` `accessibility`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/Tooltips/sections/tooltips.liquid) （ライセンス: MIT、452行）
- **ファイル:** `Tooltips/sections/tooltips.liquid`

**説明:** 画像上の特定位置に番号付きボタンを配置し、クリックするとツールチップが展開して詳細情報を表示するセクション。レスポンシブ対応で、モバイルではリスト表示、デスクトップではホバー時にポップアップ表示。

**用途:** 商品の使用方法を図解したい場合や、インフォグラフィック・図表に注釈をつけたい場合に使用。説明書や解説ページの説明箇所を視覚的に指し示す。

**設置場所:** sections/ ディレクトリに tooltips.liquid として保存。theme.json のセクション定義に登録後、ページビルダーで利用可能。

**注意点:** JavaScriptが必須（aria-expanded制御のため、コード後続部に実装必要）。ツールチップの位置は block.settings.top と block.settings.left で画像のアスペクト比に応じて計算されるため、画像によって位置調整が必要。ブレークポイントは section.settings.breakpoint で指定可能だが、デフォルト値がコードに記載されていない。

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


### 21. 🧩 スニペット ヘッダーセクション（ロゴ・ナビ・ユーザーメニュー）

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `header` `navigation` `account` `cart` `layout`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/header.liquid) （ライセンス: MIT、37行）
- **ファイル:** `shopify/sections/header.liquid`

**説明:** ストアのヘッダーを構成するセクション。ロゴ、ナビゲーションメニュー、ログイン/ログアウト、カートリンクを一つのコンポーネントにまとめています。

**用途:** theme.liquid または index.liquid のセクション領域で使用。ストア全体のトップナビゲーション部分として機能します。

**設置場所:** shopify/sections/header.liquid に配置。theme.liquid の {% section 'header' %} で呼び出します。

**注意点:** layout-menu スニペットが別途必要です。顧客アカウント機能は店舗設定で有効化が必須。t: で始まるキーは translation ファイル(locales/ja.json など)に定義が必要。カートリンクの表示状態を CSS で制御する場合、cart_count なども別途追加検討が推奨。

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


### 22. 🧩 スニペット コレクションページ商品一覧（ページネーション付き）

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `collection` `pagination` `product-list` `liquid` `template`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/collection.liquid) （ライセンス: MIT、41行）
- **ファイル:** `templates/collection.liquid`

**説明:** コレクション内の商品を表形式で一覧表示し、ページネーション機能を備えたテンプレートです。商品画像、ベンダー名、価格、説明文を見やすくレイアウトします。

**用途:** Shopifyのコレクションページで、複数商品を整理して表示したい場合に使用します。20件ずつページ分割し、顧客が閲覧しやすくします。

**設置場所:** templates/collection.liquid に配置します（テーマのコレクションテンプレートファイル）。

**注意点:** paginate タグで20件固定のため、件数変更時は数値を編集が必要です。featured_image が存在しない商品は表示されません。asset_img_url フィルタはテーマの画像サイズ設定に依存します。表形式のため、モバイルレスポンシブ対応は別途CSSが必須です。

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


### 23. 🧩 スニペット 顧客ログイン・パスワードリセットセクション

**カテゴリ:** ユーティリティ ／ **難易度:** 中級 ／ **タグ:** `customer` `login` `form` `password` `section`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/sections/main-login.liquid) （ライセンス: MIT、238行）
- **ファイル:** `sections/main-login.liquid`

**説明:** Shopify 標準のログイン・パスワードリセット・ゲスト購入フォームを実装するセクション。ロゴ画像とパディング設定に対応し、エラー・成功メッセージを表示します。

**用途:** accounts/login ページにメインコンテンツとして配置。顧客のログイン、パスワード忘却時のリセット、ゲスト購入を一画面で提供します。

**設置場所:** sections/main-login.liquid として新規作成し、accounts/login.liquid テンプレートに {% section 'main-login' %} で呼び出します。

**注意点:** multipass_login 設定が true の場合は非表示になります。ロゴ表示時は section.settings.logo.aspect_ratio に依存するため、画像アップロード必須です。エラーメッセージは Shopify 標準の翻訳キーを使用しており、言語設定で自動変換されます。

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


### 24. 🧩 スニペット 組織情報の構造化データ(JSON-LD)

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `seo` `json-ld` `structured-data` `organization` `schema`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/json-ld-organization.liquid) （ライセンス: MIT、22行）
- **ファイル:** `json-ld-organization.liquid`

**説明:** Shopify ストアの組織情報(ロゴ、URL、SNS アカウント)を JSON-LD 形式で記述し、Google などの検索エンジンに正確に認識させます。SEO 効果を高めるための基本的なマークアップです。

**用途:** theme.liquid の <head> セクション内に設置し、検索結果やナレッジグラフに ストア情報を表示させたい場合に使用します。

**設置場所:** theme.liquid の </head> タグ直前、またはヘッダーセクションの最後に配置するのが一般的です。

**注意点:** 11 行目の 'logo.png' と 13～18 行目の settings.social_* は、テーマの設定に合わせて変数名を置換が必須です。SNS リンクが未設定の場合は空配列が出力されるため、テーマ側で正しく設定されているか事前確認が必要です。

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


### 25. 🧩 スニペット 404エラーページセクション

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `404` `error-page` `template` `navigation`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/404.liquid) （ライセンス: MIT、24行）
- **ファイル:** `sections/404.liquid`

**説明:** 存在しないページにアクセスした顧客向けのエラー画面を表示します。404テンプレート用のセクションで、エラーメッセージと全商品ページへのリンクを提供します。

**用途:** 404.liquidテンプレートで無効なストアURLにアクセスした顧客に対して表示され、ユーザーを全商品ページに誘導します。

**設置場所:** sections/404.liquidとして新規ファイルを作成、または既存の404セクションとして使用。404.liquidテンプレートからアサインしてください。

**注意点:** 翻訳文は'404.title'、'404.not_found'、'404.back_to_shopping'というキーで多言語対応されています。必ず言語ファイル(locales/ja.json等)に該当キーを追加してください。routes.all_products_collection_urlは自動生成されるため、カスタマイズ不要です。

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


### 26. 🧩 スニペット カート属性でコレクション表示件数を動的変更

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `collection` `pagination` `cart-attributes` `liquid`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Dynamic pagination without alternate templates/dynamic-pagination.liquid) （ライセンス: MIT、20行）
- **ファイル:** `Dynamic pagination without alternate templates/dynamic-pagination.liquid`

**説明:** コレクションページの1ページあたりの表示件数を、カート属性に保存された値から動的に変更します。デフォルト値は40件で、ユーザーが選択した件数があればそれを優先します。

**用途:** コレクションページで、ユーザーが「20件表示」「40件表示」「60件表示」などを選べるUI実装時に使用します。選択した表示件数を記憶して次回訪問時にも反映させたい場合に有効です。

**設置場所:** collection.liquid の paginate タグ前に配置します。または、コレクションテンプレートの商品一覧ループの直前に挿入します。

**注意点:** cart.attributes.pagination には数値文字列が格納されること前提です。JavaScriptで事前にこの属性を設定する仕組みが別途必要です。負の値は abs フィルタで絶対値に変換されるため、入力値の妥当性チェックは別途実装してください。

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


### 27. 🧩 スニペット 商品カスタムバッジ表示（メタフィールド連動）

**カテゴリ:** メタフィールド ／ **難易度:** 中級 ／ **タグ:** `product` `metafield` `badge` `custom-fields`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-custom-badge.liquid) （ライセンス: MIT、19行）
- **ファイル:** `snippets/product-custom-badge.liquid`

**説明:** 商品のメタフィールドから取得したテキストと色でカスタムバッジを表示します。パイプ区切りのメタフィールド値から自動的に色を抽出し、ダイナミックなバッジデザインを実現できます。

**用途:** 商品ページやコレクション一覧で「新商品」「セール」「限定」など動的なバッジを表示したい場合に使用します。管理画面からメタフィールドで簡単に更新可能です。

**設置場所:** snippets/product-custom-badge.liquid として作成し、商品テンプレートや商品カードスニペット内の適切な場所で {% include 'product-custom-badge' %} で呼び出します。

**注意点:** メタフィールド名は settings.product_custom_badge_metafield で設定済みであることが前提です（形式：namespace.key）。カラー値は16進数カラーコードで入力してください。color_darken フィルタはテーマに含まれることを確認してください。

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


### 28. 🧩 スニペット Shopify テーマの基本レイアウトテンプレート

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `layout` `html` `meta` `seo` `header` `footer`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/layout/theme.liquid) （ライセンス: MIT、42行）
- **ファイル:** `shopify/layout/theme.liquid`

**説明:** HTML5 ドキュメント構造、メタタグ、CSS/JS バンドル、ヘッダー・フッターセクションを一括定義するテーマの土台。SEO 対応や Shopify プラグイン統合に対応済み。

**用途:** すべてのページで使用されるルートレイアウトファイル。言語設定、ファビコン、スタイルシート、スクリプト、ナビゲーションを一元管理する場合に活用。

**設置場所:** theme.liquid（layout フォルダ直下）。既存ファイルを置き換える形で使用。

**注意点:** bundle.css と bundle.js は assets フォルダに存在する必要あり。settings.favicon はテーマ設定で Favicon 項目があることが前提。request.page_type == 'captcha' はキャプチャページ判定のため Shopify パスワード保護テーマで効果的。webpack や外部ビルドツールと連携する場合は asset_url フィルタの出力パスを確認必須。

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


### 29. 🧩 スニペット カテゴリ複数列表示セクション

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 中級 ／ **タグ:** `category` `collection` `grid` `image` `metaobject`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/sections/category-multicolumn.liquid) （ライセンス: MIT、112行）
- **ファイル:** `sections/category-multicolumn.liquid`

**説明:** コレクション配下のカテゴリを画像付きカード形式でグリッド表示するセクション。ホバー時に視覚フィードバックがあり、カテゴリ数を自動集計します。

**用途:** ECサイトのカテゴリランディングページで、複数のサブカテゴリを見やすく並べて表示したい場合に使用。カテゴリ画像と説明文で視認性を向上させます。

**設置場所:** sections/category-multicolumn.liquid として保存し、テーマのセクションフォルダに配置。カテゴリ一覧ページのテンプレートで呼び出す。

**注意点:** ブロック内の「next_children」はカスタムメタオブジェクト「category_metaobject」に依存するため、事前にメタオブジェクト定義が必要。画像幅は150pxで固定されているため、より大きな表示が必要な場合は width 値を変更してください。モバイル表示時のレスポンシブ対応は、テーマの既存CSS フレームワークに依存します。

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


### 30. 🧩 スニペット Shopify テーマ基盤レイアウト（フォント・色・間隔設定）

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 上級 ／ **タグ:** `layout` `css-variables` `design-tokens` `theme-settings` `head`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/layout/theme.liquid) （ライセンス: MIT、242行）
- **ファイル:** `layout/theme.liquid`

**説明:** Shopify テーマの最上位レイアウトファイル。フォント、色、間隔などの設計トークンを CSS 変数として定義し、全ページで統一されたデザインを実現します。

**用途:** 全テーマページ共通のヘッダー、メタ情報、CSS 変数設定。カスタマイズ可能なテーマの基礎となり、管理画面の色設定やフォント選択がサイト全体に反映される仕組みを構築します。

**設置場所:** layout/theme.liquid（レイアウトフォルダ内のメインテンプレートファイル）。全ページが このレイアウトを継承します。

**注意点:** settings.* の色・フォント・間隔値は Shopify の theme settings に存在する必要があります。CSS 変数の値が空白の場合は CSS の フォールバック値が優先されるため、設定漏れはデザイン崩れの原因になります。カスタムフォントを使用する場合は preconnect リンクを確認し、パフォーマンスに影響しないよう検証してください。

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


### 31. 🧩 スニペット ランダム商品取得スニペット

**カテゴリ:** 商品表示 ／ **難易度:** 中級 ／ **タグ:** `product` `random` `collection` `snippet`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/random-product.liquid) （ライセンス: MIT、32行）
- **ファイル:** `random-product.liquid`

**説明:** 全商品またはコレクション内からランダムに商品を1つ選び出し、その商品オブジェクトを変数に格納します。タイムスタンプをベースとした疑似乱数生成で実装されています。

**用途:** おすすめ商品の自動表示、季節品・新着商品の露出、クロスセルバナーなど、ページ訪問時にランダムな商品を提案したいシーンで使用します。

**設置場所:** snippets/random-product.liquid として作成し、商品を表示したいセクションやテンプレートから render タグで呼び出します。

**注意点:** specific_collection パラメータはコレクションの handle を指定する必要があります（日本語ハンドルは URL エンコード対応が必要な場合あり）。また、タイムスタンプベースのため完全にランダムではなく、秒単位で結果が変わります。オンラインストア 2.0 以降での動作を想定しています。

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


### 32. 🧩 スニペット ブログ記事一覧ページの表示

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `blog` `articles` `pagination` `template` `image`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/blog.liquid) （ライセンス: MIT、36行）
- **ファイル:** `sections/blog.liquid`

**説明:** ブログテンプレート用のセクション。ブログ内の全記事を一覧表示し、アイキャッチ画像・タイトル・公開日・著者・抜粋を5件ずつページネーション表示します。

**用途:** theme.liquid から呼び出されるブログページ（/blogs/ブログハンドル）で、記事一覧を構築する際に使用。

**設置場所:** sections/blog.liquid として設置、またはブログテンプレート（templates/blog.liquid）で {% section 'blog' %} として呼び出し。

**注意点:** article.excerpt は設定によって空の場合があります。日本語で5件/ページが最適か、ビジネス要件に応じて 'paginate blog.articles by 5' の数字を調整してください。image_url と image_tag フィルターは Shopify 2.0 以降必須。

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


### 33. 🧩 スニペット SKU検索API エンドポイント

**カテゴリ:** API連携/JS ／ **難易度:** 中級 ／ **タグ:** `search` `sku` `json` `api` `ajax`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Search by SKU/search.sku.liquid) （ライセンス: MIT、23行）
- **ファイル:** `Search by SKU/search.sku.liquid`

**説明:** 検索フォームで入力されたSKUに基づいて、マッチする商品をJSON形式で返すAPIエンドポイントです。フロントエンドのAJAX処理や外部システム連携時に商品情報をプログラム的に取得できます。

**用途:** 商品検索ページやカスタム検索機能で、SKU入力時にリアルタイムで商品情報をJSON形式で取得したい場合。カートページのSKU検証やPOSシステム連携時の商品照合に利用できます。

**設置場所:** Shopify管理画面 > オンラインストア > ページ から新規ページを作成し、テンプレートをカスタムLiquidで編集して貼り付けるか、または専用のLiquidテンプレートファイル(search.sku.liquid)として保存します。

**注意点:** レイアウトなし(layout none)を指定しているため、HTML装飾なくJSON出力のみになります。検索結果は最大250件までの制限があり、それ以上の件数がある場合はページネーション対応が必要です。Shopifyの検索インデックスはSKUのキーワードマッチに依存するため、完全一致保証ではありません。

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


### 34. 🧩 スニペット 商品ページ内リッチテキストブロック

**カテゴリ:** 商品表示 ／ **難易度:** 中級 ／ **タグ:** `product` `section` `block` `richtext` `customizable`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-block-richtext.liquid) （ライセンス: MIT、22行）
- **ファイル:** `snippets/product-block-richtext.liquid`

**説明:** 商品ページに任意のテキスト・説明文を挿入するセクションブロックです。ブロックの上下余白をカスタマイズでき、商品説明文の自動挿入にも対応しています。

**用途:** 商品ページでカスタムな説明文やマーケティングテキストを、編集画面から柔軟に配置したいとき。商品説明と別にプロモーションテキストなどを挿入する場面で使用します。

**設置場所:** snippets/product-block-richtext.liquid に作成し、商品ページのセクションから呼び出します。sections/ 内の商品セクションファイルから {% include 'product-block-richtext' with block: block %} で参照してください。

**注意点:** block.settings の pt（上余白）・pb（下余白）・title_font_size などはセクションスキーマで事前に定義が必須です。product 変数は商品ページコンテキストでのみ有効なため、他のテンプレートでは product.description が機能しません。description_classes に独自の CSS クラスを指定する場合は、テーマの CSS で定義済みであることを確認してください。

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


### 35. 🧩 スニペット Vue コンポーネント統合デモセクション

**カテゴリ:** その他 ／ **難易度:** 上級 ／ **タグ:** `vue` `component` `vuex` `slot` `mixin` `directive` `demo`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/vue-examples.liquid) （ライセンス: MIT、162行）
- **ファイル:** `shopify/sections/vue-examples.liquid`

**説明:** Shopify Theme Lab の Vue コンポーネント、Vuex ストア、ディレクティブ、ミックスインなどを一堂に試せるデモセクションです。プロップス・スロット・レンダーレスコンポーネントなど Vue の実装パターンを確認できます。

**用途:** Vue ベースのテーマ開発時に、コンポーネントやストア連携が正常に動作しているか確認するデモページ。開発・ステージング環境で使用。

**設置場所:** sections/ ディレクトリに配置。セクションスキーマで管理画面から追加可能。

**注意点:** Theme Lab フレームワークが必要。src/vue/components/、src/vue/mixins/、src/vue/directives/、src/vue/store/ のディレクトリ構成に依存。コンポーネント名は `name` フィールドまたはファイルパスで自動命名されるため、パスと対応を確認必須。本番環境では削除推奨。

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


### 36. 🧩 スニペット ホームページ用カテゴリグリッド表示

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 中級 ／ **タグ:** `homepage` `category` `metaobject` `grid` `navigation`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/sections/homepage.liquid) （ライセンス: MIT、119行）
- **ファイル:** `sections/homepage.liquid`

**説明:** メタオブジェクトで管理した階層化カテゴリを、ホームページ上にグリッド状で表示します。カテゴリ画像とテキストを整理して視認性よく配置できます。

**用途:** ECサイトのホームページで商品カテゴリをビジュアル的に整理して表示したいシーン。メインナビゲーションの補完や、カテゴリ一覧ページなど。

**設置場所:** sections/homepage.liquid に新規作成、またはテーマ内のホームページセクションとして設置。

**注意点:** children_categories メタオブジェクトの name フィールドに ' > ' 区切りが含まれる階層構造を前提としており、このフォーマットがないと表示されません。また、metaobject_list の category_metaobject 型がテーマに定義されていることが必須です。画像がない場合は表示されないため、各カテゴリに画像登録が必要です。

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


### 37. 🧩 スニペット Twitter Card メタタグ自動生成

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `seo` `meta` `twitter` `product` `article`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/metadata-twitter.liquid) （ライセンス: MIT、37行）
- **ファイル:** `metadata-twitter.liquid`

**説明:** 商品ページとブログ記事に対応した Twitter Card メタタグを自動生成します。商品価格・在庫状況やブログ記事の抜粋画像を SNS シェア時に正しく表示させます。

**用途:** theme.liquid の <head> 内に設置し、Twitter でのリンク共有時に商品情報やブログ記事を視覚的にリッチに表示させたい場合に使用します。

**設置場所:** theme.liquid の <head> タグ内、または snippets/metadata-twitter.liquid として作成して theme.liquid から {% include 'metadata-twitter' %} で呼び出す

**注意点:** 6行目の @twitter_handler をストアの Twitter ハンドルに置換必須。35行目のロゴファイル名 logo-square.png はテーマに存在する正方形画像に差し替え。ブログ記事内の img タグが相対 URL の場合は http または https を自動補完しますが、CDN URL の場合は別途調整が必要な場合あり。

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


### 38. 🧩 スニペット パスワード保護ページのランディング画面

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `password` `template` `form` `liquid-form`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/password.liquid) （ライセンス: MIT、36行）
- **ファイル:** `sections/password.liquid`

**説明:** ストアにパスワード保護が設定されている際に表示するランディングページを作成します。訪問者がパスワードを入力して店舗にアクセスできるシンプルなフォームを提供します。

**用途:** password.liquid テンプレートで使用し、グランドオープン前やメンテナンス中に顧客や関係者のみに店舗をプレビューさせたいときに活用します。

**設置場所:** sections/password.liquid に配置します。password.liquid テンプレート内で {% section 'password' %} として呼び出します。

**注意点:** shop.password_message はストア設定の「パスワード保護メッセージ」フィールドを参照するため、Admin で事前に設定が必要です。翻訳キー（'password.title'、'password.password'、'password.enter'）は theme/locales/ja.json で定義すること。スタイリングがないため、theme.css で form や input タグに対するスタイルが必要です。

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


### 39. 🧩 スニペット メタフィールドで商品を並び替え

**カテゴリ:** メタフィールド ／ **難易度:** 中級 ／ **タグ:** `collection` `metafield` `sort` `liquid`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Sort Shopify collection by metafield/sort-shopify-collection-products-by-metafield-value-commentless.liquid) （ライセンス: MIT、24行）
- **ファイル:** `Sort Shopify collection by metafield/sort-shopify-collection-products-by-metafield-value-commentless.liquid`

**説明:** コレクション内の商品をメタフィールドの値に基づいて動的に並び替えます。メタフィールド(global.order)の数値を基準に、元のインデックス順を保持しながらソートが可能です。

**用途:** コレクションページで商品の表示順序をメタフィールドで管理したい場合に使用。管理画面のメタフィールド値を変更するだけで表示順が自動的に変わります。

**設置場所:** collection.liquid または sections/collection-*.liquid の商品ループ部分に貼り付け。product-item の div を出力する箇所に置き換える形で使用します。

**注意点:** メタフィールド名『global.order』が存在しない商品は『999999』として扱われ末尾に配置されます。large コレクション(1000件以上)では Liquid のループ制限に引っかかる可能性があるため、事前にフィルタリング推奨。

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


### 40. 🧩 スニペット セクションヘッダー（タイトル+説明文）

**カテゴリ:** レイアウト/ナビ ／ **難易度:** 初級 ／ **タグ:** `section` `header` `reusable` `snippet` `css`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/section-header.liquid) （ライセンス: MIT、24行）
- **ファイル:** `snippets/section-header.liquid`

**説明:** セクションのタイトルと説明文をまとめて表示するレイアウト部品です。セクション設定から取得した見出しと説明文を、条件付きで中央揃えで出力します。

**用途:** コレクションページ、プロモーションセクション、特集エリアなど、複数セクションで共通的に使用するヘッダー部分。タイトル・説明文の有無を自動判定して柔軟に表示できます。

**設置場所:** snippets/section-header.liquid として保存し、各セクション内で {% render 'section-header' %} または {% render 'section-header', class: 'カスタムクラス' %} で呼び出します。

**注意点:** section.settings.header_title、header_description、header_title_font_size、header_description_font_size がセクションスキーマで定義されていないと動作しません。rte クラスと opacity-70 は テーマの CSS に依存します。クラス引き渡し時は class 変数を確実に定義してください。

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

