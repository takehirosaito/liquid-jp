# liquid-jp.jp Phase 1 サンプル50件レポート (v3: 後処理+キャッシュ活性化版)

生成日時: 2026-05-13 21:06 ／ モデル: `claude-haiku-4-5-20251001`

## サマリ

- 件数: **50件**（成功 50 / 失敗 0）
  - コミュニティスニペット: **40件**
  - 公式リファレンス（theme-liquid-docs）: **10件**
- 処理時間: 36.3秒（並列 8）
- API コスト: **$0.2282**（入力 46,679 tok ＋ 出力 23,983 tok、cache_read 182,196 tok)

### カテゴリ分布

| カテゴリ | 件数 |
|---|---:|
| ページテンプレート | 10 |
| テーマ基盤 | 5 |
| ヘッダー/フッター/ナビゲーション | 5 |
| UI部品 | 4 |
| コレクション/検索 | 4 |
| リファレンス/フィルター | 4 |
| API連携/JSON出力/JS統合 | 3 |
| SEO/構造化データ | 3 |
| リファレンス/タグ | 3 |
| リファレンス/オブジェクト | 3 |
| 商品表示 | 2 |
| ユーティリティ | 2 |
| 顧客アカウント | 1 |
| メタフィールド/メタオブジェクト | 1 |

### 難易度分布

| 難易度 | 件数 |
|---|---:|
| 初級 | 31 |
| 中級 | 15 |
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

1. **日本語訳の品質** — 自然な日本語か、誤訳・直訳が残っていないか
2. **カテゴリ分類** — 新カテゴリ体系で適切に分類できているか、誤分類がないか
3. **タイトルフォーマット** — リファレンスは「名前 種別（用途）」、スニペットは「スニペット」「セクション」後置なしを守れているか
4. **タグの命名規則** — 小文字ハイフン区切り・単数形・同義語正規化が効いているか、category と重複していないか
5. **caveats の品質** — 「〜が必要です」連発がないか、①前提→②落とし穴→③応用注意の構成か、具体策が書けているか
6. **include / render 対応** — 原文が include を使っているスニペットで render 推奨の注記が入っているか

---

## 📘 公式リファレンス サンプル

### 1. 📘 リファレンス sort_by フィルター(コレクションURL にソート条件を追加)

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `collection` `filter` `sort` `url` `parameter` `title-too-long`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** コレクション URL に sort_by パラメータを追加し、商品の並び順を指定する。手動・売上・価格・作成日時などの条件でソート可能。

**用途:** コレクションページでユーザーが「価格が安い順」「新着順」などのソートオプションをクリックしたとき、URL にソート条件を含めて遷移させるリンク構築に使う。

**設置場所:** コレクションテンプレートやセクション内で `{{ collection.url | sort_by: 'price-ascending' }}` の形で使用。ソート選択肢のリンクに埋め込む。

**注意点:** このフィルターは `collection.url` オブジェクトプロパティに対してのみ適用可能。指定できる値は `manual`・`best-selling`・`title-ascending`・`title-descending`・`price-ascending`・`price-descending`・`created-ascending`・`created-descending` の8種類に限定される。`url_for_type` や `url_for_vendor` フィルターと組み合わせることで、特定カテゴリ・ベンダーのソート URL も生成できる。

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


### 2. 📘 リファレンス escape フィルター(HTML特殊文字をエスケープ)

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `escape` `security` `xss` `html` `string`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** 文字列内の HTML 特殊文字(&<>シングルクォート、アンパサンド等)をエスケープシーケンスに変換し、XSS 対策や HTML 出力を安全にする。

**用途:** ユーザー入力やメタフィールドの値を HTML として出力するとき、意図しない HTML タグが実行されるのを防ぐ。

**設置場所:** Liquid テンプレート内で `{{ value | escape }}` の形で使用。例えば `{{ product.metafields.custom.user_note | escape }}` のように、ユーザー入力を含む変数の直前に記述する。

**注意点:** 既にエスケープ済みの文字列に重複適用するとダブルエスケープ(%26lt; のような意図しない表示)になるため注意。JSON-LD や JavaScript コード内の文字列には escape ではなく `json` フィルターを使う。通常の商品名や説明文は Shopify が自動的にエスケープするため、手動適用が必須なのはカスタムメタフィールドやフォーム入力値に限られる。

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


### 3. 📘 リファレンス floor フィルター(数値を切り下げ)

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `math` `number` `rounding` `integer`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** 小数を含む数値を最も近い整数に切り下げるフィルター。1.2 は 1 に、2.9 は 2 になる。

**用途:** 商品の数量計算で小数を避けたいときや、在庫管理で端数を切り捨てる必要があるシーンで使用。

**設置場所:** Liquid テンプレート内で `{{ 数値 | floor }}` の形で使う。例：`{{ product.price | divided_by: 2.0 | floor }}` で価格を半額にして切り下げ。

**注意点:** 負の数にも対応しており、-1.5 は -2 になる点に注意。整数は影響を受けないため無害。計算精度が必要な場合は事前に `| round` で丸めてから `floor` を使うと予期しない四捨五入を避けられる。

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


### 4. 📘 リファレンス link_to_type フィルター(商品タイプのコレクションページへのリンク生成)

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `filter` `link` `product-type` `collection` `html` `title-too-long`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、48行）
- **ファイル:** `data/filters.json`

**説明:** 商品タイプ名を HTML の `<a>` タグに変換し、そのタイプの商品をすべて表示するコレクションページへのリンクを生成するフィルター。

**用途:** 商品詳細ページやコレクション内で商品タイプをクリック可能なリンク化したいときに使用。例えば「Health」というタイプをクリックすると、Health カテゴリの全商品が表示されるコレクションページに遷移する。

**設置場所:** 任意のテンプレート・セクション・スニペット内で `{{ '商品タイプ名' | link_to_type }}` の形で使用。HTML 属性(class など)を追加したい場合は `{{ 'Health' | link_to_type: class: 'link-class' }}` のように指定できる。

**注意点:** このフィルターは商品タイプ名の正確な文字列入力を前提とするため、タイプ名の大文字小文字や完全一致を確認する必要がある。生成されるリンク先は Shopify が自動生成する商品タイプコレクションページであり、管理画面で明示的に作成したコレクションではなく、存在しないタイプ名を指定するとリンク先が 404 になる可能性がある。対応する HTML 属性は MDN の標準属性に準拠し、カスタム属性(data-* など)も指定できる。

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


### 5. 📘 リファレンス decrement タグ(変数を1ずつ減らす)

**カテゴリ:** リファレンス/タグ ／ **難易度:** 初級 ／ **タグ:** `variable` `counter` `decrement` `loop`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、28行）
- **ファイル:** `data/tags.json`

**説明:** 新しい変数を作成し、初期値を -1 とした後、呼び出すたびに 1 ずつ減少させるタグ。increment の逆動作。

**用途:** ループ処理で負の番号カウンターが必要なとき、または逆順カウントダウンが必要なシーンで使う。

**設置場所:** Liquid 内で `{% decrement variable_name %}` の形で記述。変数はレイアウト・テンプレート・セクション内で有効で、同じファイル内のスニペットと共有される。

**注意点:** decrement と increment は同じ変数名で共有されるため、同一ファイル内で両タグを混在させると予期しない結果になる。assign / capture で作成した変数とは独立している。Liquid の定義済みオブジェクト名(product、collection など)と同じ変数名を使うとオブジェクトがオーバーライドされるため、一意の変数名を付ける。

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


### 6. 📘 リファレンス for タグ(配列をループ処理)

**カテゴリ:** リファレンス/タグ ／ **難易度:** 初級 ／ **タグ:** `loop` `iteration` `array` `limit` `offset`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、113行）
- **ファイル:** `data/tags.json`

**説明:** 配列内のすべての要素に対して式を繰り返し実行するタグ。limit・offset・range・reversed パラメータで反復回数や順序を制御できる。

**用途:** コレクションの全商品をループして商品カードを並べたり、特定数だけ表示したい、または逆順で表示したいときに使用する。

**設置場所:** Liquid テンプレート内で `{% for 変数 in 配列 %}...{% endfor %}` の形で記述。collection.products / cart.items など配列を持つオブジェクトをループする際の基本的なタグ。

**注意点:** 1 回のループで最大 50 回の反復が制限されており、それ以上の項目をループする場合は `paginate` タグで複数ページに分割する必要がある。limit パラメータで件数制限するより、paginate で本来取得するデータ量自体を減らすほうがサーバー性能上好ましい。offset パラメータは 1 ベースのインデックス指定のため、offset: 1 は最初の 1 要素をスキップする。

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


### 7. 📘 リファレンス else タグ(ループが空のときの分岐)

**カテゴリ:** リファレンス/タグ ／ **難易度:** 初級 ／ **タグ:** `loop` `for` `iteration` `conditional` `empty-state`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、40行）
- **ファイル:** `data/tags.json`

**説明:** for ループの配列が空(長さ0)のとき、デフォルト表示を指定するタグ。ループ内で1つも要素がない場合の代替表示を書ける。

**用途:** コレクションに商品がない、検索結果が0件、カートが空など、配列が空のケースで「該当なし」メッセージを表示したいとき。

**設置場所:** for ループの直後に `{% else %}` を書き、その後に空のときの表示内容を記述。末尾は `{% endfor %}` で閉じる。

**注意点:** else は for ループ専用であり、if タグの else とは異なる。ループの配列要素が1個以上ある場合は else 以下の内容は実行されないため、空判定は `if array.size == 0` と別で書く必要はない。

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

**カテゴリ:** リファレンス/オブジェクト ／ **難易度:** 中級 ／ **タグ:** `metafield` `measurement` `dimension` `weight` `volume`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、86行）
- **ファイル:** `data/objects.json`

**説明:** メタフィールドの measurement 型（寸法・容量・重量）から取得した計測値オブジェクト。type（種類）、value（数値）、unit（単位）の3プロパティを持つ。

**用途:** 商品の寸法・容積・重量をメタフィールドで管理しているとき、テンプレートで「幅 10cm」「容量 500ml」のように構造化データとして表示する。

**設置場所:** テンプレート内で `{{ product.metafields.カスタムネームスペース.メタフィールド名.value.value }}` で数値、`{{ product.metafields.カスタムネームスペース.メタフィールド名.value.unit }}` で単位を参照する。

**注意点:** measurement オブジェクトは metafield.value 経由でのみアクセス可能で、直接グローバルには使えない。type は dimension/volume/weight のいずれかの文字列値となり、metafield 型の設定時に固定される。unit は Shopify が定義した標準単位（cm、ml、kg など）に限定されるため、独自単位が必要な場合はメタフィールドの custom_definition で事前に設定する。

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

**カテゴリ:** リファレンス/オブジェクト ／ **難易度:** 中級 ／ **タグ:** `model` `3d` `media` `cdn` `source`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、74行）
- **ファイル:** `data/objects.json`

**説明:** 3D モデルのソースファイル情報を格納するオブジェクト。ファイル形式、MIME タイプ、CDN URL を参照できる。

**用途:** 商品に紐付いた 3D モデル(GLB / USDZ など)を Web ページで表示するとき、ファイルの URL や形式を取得して動的に組み込む。

**設置場所:** Liquid テンプレート内で `{{ product.featured_media.sources[0].format }}` や `{{ product.featured_media.sources[0].url }}` の形で参照する。

**注意点:** model_source は `product.featured_media.sources` 配列に含まれるため、sources が空でないことを事前に確認する必要がある。url は Shopify CDN 経由の完全パスなので、外部の CDN へのリダイレクトは不要。MIME タイプ(model/gltf-binary など)と format(glb、usdz など)は異なる値を返すため、クライアント側の 3D ビューアが対応している形式を事前に確認しておく。

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

**カテゴリ:** リファレンス/オブジェクト ／ **難易度:** 中級 ／ **タグ:** `remote-product` `multistore` `cross-store` `object-property`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、69行）
- **ファイル:** `data/objects.json`

**説明:** 他のストアから取得した商品などのリモートオブジェクトの出所情報を扱うオブジェクト。取得元ストア情報と、どのような方法でそのオブジェクトが表示されたのかを記録している。

**用途:** Shopify の複数ストア連携機能で、別ストアの商品情報を現在のストアに表示するときに、その商品がどのストアから来たのかを判定したり出所を表記したりする。

**設置場所:** remote_product オブジェクトのプロパティとして `{{ remote_product.remote_details.type }}` または `{{ remote_product.remote_details.shop }}` の形で Liquid 内で参照する。

**注意点:** remote_details にアクセスするには親オブジェクトが remote_product である必要があり、通常のストア内商品の product オブジェクトには remote_details プロパティは存在しない。type の値は現在「seller」のみサポートされているが将来拡張される可能性があるため、値の比較ではなく存在確認程度に留めるとよい。

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

### 1. 🧩 スニペット 固定ページの基本

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `page` `template` `section` `content` `static-page`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/page.liquid) （ライセンス: MIT、18行）
- **ファイル:** `sections/page.liquid`

**説明:** Shopify の固定ページ(About、Contact など)を表示するセクション。ページタイトルとコンテンツを出力する最小限の実装。

**用途:** 管理画面で作成した固定ページを Web に公開するとき。about.liquid、contact.liquid などのページテンプレートで使う。

**設置場所:** sections/page.liquid に配置し、templates/page.liquid 内で `{% section 'page' %}` で呼び出す。Shopify の既定パターンなので通常は編集不要。

**注意点:** このセクションは schema タグが空(settings なし)のため、テーマカスタマイザーでカスタマイズできない。ページの背景色やパディングを変えたい場合は settings に color / spacing の定義を追加する必要がある。page.content は管理画面のエディタで記入した HTML がそのまま出力されるため、JavaScript 埋め込みやスタイル崩れがないか事前に確認する。

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

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `request` `multidomain` `conditional` `asset`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Get current domain name with Liquid/request_host.liquid) （ライセンス: MIT、15行）
- **ファイル:** `Get current domain name with Liquid/request_host.liquid`

**説明:** アクセスしたドメインを判定し、ドメインごとに異なるバナー画像を表示するスニペット。request.host を用いて複数ドメイン間での画像出し分けに対応。

**用途:** 日本・オーストラリア・グローバルなど複数ドメインで Shopify を運用しているとき、ドメインごとに地域別のバナーやコンテンツを切り替えて表示したいシーン。

**設置場所:** snippets/request_host.liquid として配置し、theme.liquid のヘッダーまたはバナー表示箇所で `{% render 'request_host' %}` で呼び出す。または任意のセクション内に直接貼り付けても可。

**注意点:** request.host は開発ストア(*.myshopify.com)では機能しないため、カスタムドメイン設定が前提。プレビュー環境(preview.example.com など)では値が異なるため、本番ドメインで十分にテストしてからリリースする。条件分岐が増えると可読性が落ちるため、3ドメイン以上になる場合は theme settings で地域選択をさせるか Shopify Markets 設定に切り替えるのが管理上ベター。

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


### 3. 🧩 スニペット 商品ページの区切り線

**カテゴリ:** 商品表示 ／ **難易度:** 初級 ／ **タグ:** `block` `separator` `product` `ui-component` `customization`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-block-separator.liquid) （ライセンス: MIT、15行）
- **ファイル:** `snippets/product-block-separator.liquid`

**説明:** 商品詳細ページで複数セクション間に配置する装飾的な水平線。上下マージン・色・透明度・高さをテーマカスタマイザーから自由に調整できる。

**用途:** 商品情報、説明文、レビューなど複数ブロック間で視覚的な区切りを作りたいとき。Online Store 2.0 のセクション設定で他ブロックと並べて使う。

**設置場所:** snippets/product-block-separator.liquid に配置し、商品ページ用セクション(sections/main-product.liquid 等)の blocks ループ内で `{% render 'product-block-separator', block: block %}` で呼び出す。もしくはセクションの block type として登録して Theme Customizer から挿入できる構成にする。

**注意点:** pt / pb クラス名はテーマの Bootstrap/Tailwind ユーティリティ命名に依存するため、実装テーマのパディング定義を確認してから block.settings の値を設定する。bg_opacity は CSS 変数 `--bs-bg-opacity` で制御されており、テーマ側で bg_color クラス(bg-primary など)が定義されていないと色が反映されない。height は px 単位で直接指定するため、レスポンシブ対応が必要な場合は CSS メディアクエリを別途追加する。

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


### 4. 🧩 スニペット クイズ結果フィルタリング用データセット

**カテゴリ:** API連携/JSON出力/JS統合 ／ **難易度:** 上級 ／ **タグ:** `quiz` `product-filter` `json` `dynamic-data` `javascript`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/Quiz/snippets/quiz-data.liquid) （ライセンス: MIT、93行）
- **ファイル:** `Quiz/snippets/quiz-data.liquid`

**説明:** コレクション内の商品を価格・タグ・タイプ・ベンダー・オプションで絞り込むためのデータを JSON 形式で生成するスニペット。クイズ回答に応じて動的に商品をフィルタリングするための基盤データを構築します。

**用途:** Shopify 上で診断クイズセクションを実装し、ユーザーの回答に基づいて関連商品を自動抽出・表示するときに必須。商品データとフィルタ条件を JavaScript に渡すデータ層として機能します。

**設置場所:** snippets/quiz-data.liquid に配置し、sections/quiz.liquid などのクイズセクション内で `{% render 'quiz-data' %}` で呼び出す。出力された JSON データを `<script>` タグで window オブジェクトに格納し、フロントエンド JavaScript でクイズロジックに利用します。

**注意点:** コレクションハンドル(section.settings.filter_collection)と Answer ブロックの設定が正確に入力されていることが前提。price_filter は整数(円単位)で入力し、tags_filter / type_filter / vendor_filter はカンマ区切りで、空白を含めないで入力する。option_filter はメタフィールド名、option_filter_values は対応する値をカンマ区切りで指定し、不要なフィルタ条件は管理画面で削除すると JSON が余分な要素を持たなくなる。

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

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `navigation` `menu` `linklist` `header` `dropdown`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/snippets/layout-menu.liquid) （ライセンス: MIT、19行）
- **ファイル:** `shopify/snippets/layout-menu.liquid`

**説明:** Shopify 管理画面の「メインメニュー」リンクリストをループし、トップレベル + 1階層のサブメニューを描画するスニペット。カスタム CSS クラスとインラインスタイルに対応。

**用途:** ストア共通のグローバルナビをヘッダーに出すとき。トップレベル + 1階層のサブメニューに対応し、カスタマイズ性を持たせたい場合に使用。

**設置場所:** shopify/snippets/layout-menu.liquid に配置し、theme.liquid のヘッダー内で `{% render 'layout-menu', class: 'navbar', style: 'display: flex;' %}` のように呼び出す。class と style パラメータでコンテナのスタイリングを制御できる。

**注意点:** Shopify 管理画面で「メインメニュー」ハンドルのリンクリストが作成されていることが前提。サブメニューは1階層のみの対応であり、3階層以上の深いメニューが必要な場合は link.links をネストさせて拡張する。ドロップダウンメニューの表示・非表示は CSS(`:hover` または `aria-expanded`)とスクリプトで別途実装が必要。

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


### 6. 🧩 スニペット 404エラーページ

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `404` `error-page` `template` `user-experience`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/404.liquid) （ライセンス: MIT、16行）
- **ファイル:** `templates/404.liquid`

**説明:** ページが見つからない場合に表示するエラーページテンプレート。シンプルなエラーメッセージを中央に配置し、ユーザーに見つからないことを通知する。

**用途:** 存在しない URL にアクセスされたとき、404 エラーページを表示する。古いリンクや間違ったURL からの流入を適切に処理し、ユーザー体験を損なわないようにする。

**設置場所:** templates/404.liquid として配置される Shopify の自動認識テンプレート。カスタマイズが必要な場合、管理画面の「オンラインストア > ページ」から編集するか、このテンプレート内の HTML を修正してホームリンクやおすすめ商品を追加する。

**注意点:** 404.liquid は Shopify が自動で認識する予約済みファイルであり、名前やパスを変更すると機能しなくなる。よく流入される存在しないURL については、管理画面の「ナビゲーション > URL リダイレクト」で事前にリダイレクト設定するとより良い。ユーザーがストアに戻れるよう、ホームページリンクやコレクションリンクを追加することで離脱防止に繋がる。

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

**カテゴリ:** UI部品 ／ **難易度:** 初級 ／ **タグ:** `icon` `svg` `success` `feedback` `ui-component`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/snippets/icon-success.liquid) （ライセンス: MIT、6行）
- **ファイル:** `snippets/icon-success.liquid`

**説明:** 緑色の円形背景に白いチェックマークを描画した SVG アイコン。注文完了やフォーム送信成功などのポジティブなフィードバックを表示する。

**用途:** 注文完了ページ、問い合わせフォーム送信後、パスワード変更成功メッセージなど、ユーザーアクションの成功状態を視覚的に伝えたいシーン。

**設置場所:** snippets/icon-success.liquid に配置し、必要なテンプレートやセクション内で `{% render 'icon-success' %}` で呼び出す。CSS クラス `.icon-success` でサイズ(width、height)と表示位置をカスタマイズ可能。

**注意点:** SVG の viewBox は 13×13 に固定されているため、異なるサイズで表示する場合は CSS の `width` と `height` で調整する。カラーが hardcoded(#428445 の緑色)なため、テーマカスタマイザーから色を変えたい場合は stroke・fill 属性を Liquid 変数化する必要がある。スクリーンリーダーに対して `aria-hidden="true"` で非表示にしているため、アイコンの意味は前後のテキスト(「完了しました」など)で補足する。

<details><summary>コード(6行)を見る</summary>

```liquid
<svg aria-hidden="true" focusable="false" role="presentation" class="icon icon-success" viewBox="0 0 13 13">
  <path d="M6.5 12.35C9.73087 12.35 12.35 9.73086 12.35 6.5C12.35 3.26913 9.73087 0.65 6.5 0.65C3.26913 0.65 0.65 3.26913 0.65 6.5C0.65 9.73086 3.26913 12.35 6.5 12.35Z" fill="#428445" stroke="white" stroke-width="0.7"/>
  <path d="M5.53271 8.66357L9.25213 4.68197" stroke="white"/>
  <path d="M4.10645 6.7688L6.13766 8.62553" stroke="white">
</svg>
```

</details>


### 8. 🧩 スニペット ランダム数値の生成

**カテゴリ:** ユーティリティ ／ **難易度:** 初級 ／ **タグ:** `random` `utility` `date-filter` `variable` `modulo`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/random-number.liquid) （ライセンス: MIT、13行）
- **ファイル:** `random-number.liquid`

**説明:** 現在時刻を利用して指定範囲内のランダム整数を生成するユーティリティ。min と max を編集することで任意の範囲に対応できる。

**用途:** A/B テストの割り振り、くじ引き企画の抽選、ランダムな商品推奨、セッションごとのバリエーション表示など、疑似乱数が必要な場面で使用。

**設置場所:** snippets/random-number.liquid に配置し、必要な箇所で `{% render 'random-number' %}` で呼び出すと `random_number` 変数が使用可能になる。

**注意点:** 現在時刻のナノ秒部分を利用しているため、同一ミリ秒内に複数回実行すると同じ値が返される可能性がある。くじ引きなど厳密なランダム性が必要な場面では JavaScript の Math.random() との併用を検討する。範囲を 0～99 など小さい値にすると、特定の数値の出現確率が高くなる傾向があるため、テスト後に分布を確認するとよい。

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


### 9. 🧩 スニペット CSS変数でテーマの基本デザイン設定を統一管理

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `css-variables` `font-face` `theme-settings` `design-tokens` `swap`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/snippets/css-variables.liquid) （ライセンス: MIT、19行）
- **ファイル:** `snippets/css-variables.liquid`

**説明:** テーマカスタマイザーで設定したフォント・色・幅などの値を CSS 変数（カスタムプロパティ）として :root に登録し、全体で再利用できるようにする。フォントの複数ウェイト・スタイルも font_face フィルタで同時に読み込む。

**用途:** テーマ全体で統一されたデザイントークン（フォント、色、スペーシング）を管理したいときに、theme.liquid の <head> 内に配置して一元管理する。

**設置場所:** snippets/css-variables.liquid に配置し、theme.liquid の <head> セクション内で {% render 'css-variables' %} で呼び出す。設定値は Shopify 管理画面のテーマ設定で type_primary_font、background_color などを事前に定義しておく必要がある。

**注意点:** settings で定義されたテーマ設定が存在することが前提。font_modify で ウェイト・スタイルを変更する際、元フォントが対応ウェイト・スタイルを持たない場合は正しく読み込まれないため、Google Fonts など可変フォント対応サービスを使うか複数フォントファイルを確保する。CSS 変数の値が空になると font-family が break するため、settings で fallback_families と fallback を明示的に指定しておく。

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


### 10. 🧩 スニペット ギフトカードのバリアント画像取得

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `gift-card` `variant` `image` `conditional` `linklists`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Use variant image on Gift Card template/capture-image.liquid) （ライセンス: MIT、16行）
- **ファイル:** `Use variant image on Gift Card template/capture-image.liquid`

**説明:** ギフトカードの金額に応じて、対応するバリアントの画像を自動取得して表示するスニペット。金額がマッチするバリアントから画像 URL を抽出し、デフォルト画像との切り替えに対応。

**用途:** ギフトカードテンプレートで、購入金額（1,000円、5,000円など）ごとに異なるデザイン画像を表示したいとき。

**設置場所:** snippets/capture-image.liquid に配置し、templates/gift_card.liquid の `<img>` タグが出力される箇所で `{% render 'capture-image' %}` で呼び出す。その後、上記コード内の `<img>` タグをテンプレート内に配置するか、変数 `{{ customImage }}` を既存画像の `src` に置き換える。

**注意点:** Shopify 管理画面で「ギフトカード商品」が作成され、「admin-gift-card」というハンドルのリンクリストに紐付けられていることが前提。バリアントの価格（`variant.price`）は整数の円単位で管理され、`gift_card.initial_value` と完全一致する値が必要なため、両者の形式に誤差がないか確認する。バリアント画像が設定されていない場合はデフォルト画像（`gift-card/card.jpg`）が表示される仕様となっている。

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


### 11. 🧩 スニペット ナビゲーションバーのロゴ

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `logo` `navbar` `header` `navigation` `responsive-image`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/navbar-logo.liquid) （ライセンス: MIT、18行）
- **ファイル:** `snippets/navbar-logo.liquid`

**説明:** ストアロゴをナビゲーションバーのホームリンクとして表示するスニペット。ロゴ画像が設定されていない場合は店舗名をテキストで代替表示する。

**用途:** テーマのヘッダーセクションでナビゲーションバーを構築するとき、クリックでホームページに戻れるロゴを配置する。

**設置場所:** snippets/navbar-logo.liquid に配置し、ヘッダーセクション内で `{% render 'navbar-logo' %}` で呼び出す。ロゴサイズは block.settings.logo_height をテーマカスタマイザーで調整可能。

**注意点:** block.settings でロゴ画像を参照しているため、親セクションで logo と logo_height の設定フィールドが定義されていることが前提。Retina ディスプレイ対応で画像高さを2倍にしているが、元画像が十分な解像度(最低 logo_height の2倍)でないとぼやけるため、アップロード時に確認する。aspect_ratio プロパティは Shopify 管理画面で画像アップロード後に自動計算されるため、手動での値入力は不要。

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


### 12. 🧩 スニペット FAQ アコーディオン(リッチスキーマ対応)

**カテゴリ:** UI部品 ／ **難易度:** 中級 ／ **タグ:** `faq` `accordion` `json-ld` `collapsible` `rich-result`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/FAQ/sections/faq.liquid) （ライセンス: MIT、352行）
- **ファイル:** `FAQ/sections/faq.liquid`

**説明:** よくある質問をアコーディオン形式で表示するセクション。質問をクリックすると回答が展開収縮し、schema.org の FAQPage 型の構造化データを自動出力して Google 検索結果のリッチリザルト対応。

**用途:** 商品ページやフッターに FAQ セクションを配置し、顧客の一般的な質問を整理して提示したいとき。Google の FAQ リッチリザルト表示を狙う場合に必須。

**設置場所:** sections/faq.liquid に配置し、Online Store 2.0 のテーマカスタマイザーから「セクション追加」で FAQ ブロックを挿入し、管理画面で質問・回答文を入力する。別途 faq.js をアセットフォルダに配置して、スクリプトソースを指定する。

**注意点:** アコーディオンの開閉アニメーションは faq.js に依存するため、外部スクリプトの読み込み遅延が生じないよう確認する。リッチスキーマ出力時に block.settings.content の HTML タグは strip_html で除去されるため、回答に装飾が必要な場合はスキーマ用に別フィールド設置を検討する。モバイル表示ではアイコンサイズが clamp() で 12px〜20px に自動調整されるため、デバイス幅が狭い環境での文字折れを CSS で確認する。

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


### 13. 🧩 スニペット フッターナビゲーション

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `footer` `linklists` `navigation` `section` `layout`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/footer.liquid) （ライセンス: MIT、25行）
- **ファイル:** `shopify/sections/footer.liquid`

**説明:** ストア共通のフッターセクション。Shopify 管理画面の「フッターメニュー」リンクリストをループして表示し、著作権表記を下部に配置する。

**用途:** すべてのページ下部に表示するグローバルフッター。利用規約・プライバシーポリシー・お問い合わせなどのリンクをまとめるのに使う。

**設置場所:** shopify/sections/footer.liquid に配置し、theme.liquid の </body> 直前で `{% section 'footer' %}` で呼び出す。

**注意点:** Shopify 管理画面で「フッターメニュー」ハンドルのリンクリストが作成されていることが前提。リンクが設定されていない場合、フッター領域は空白になるため管理画面での設定を確認する。複数列レイアウトが必要な場合は div を追加して CSS Grid や Flexbox で列分けする。

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

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `search` `pagination` `product-grid` `collection` `category`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/search.liquid) （ライセンス: MIT、17行）
- **ファイル:** `templates/search.liquid`

**説明:** 検索結果を商品カード形式で24件ずつページネーション表示するテンプレート。各商品を最も詳細なカテゴリ（階層の深いコレクション）にリンクさせ、アンカーで該当商品にジャンプさせる。

**用途:** ストアの検索機能で結果一覧を表示するページ。カテゴリ階層が複雑なストア（電子部品など）で、ユーザーが検索後に関連カテゴリページに遷移できるようにしたいとき。

**設置場所:** templates/search.liquid に配置する。Shopify 管理画面から検索すると自動的にこのテンプレートが呼び出される。カテゴリページのパス（/pages/category/）と product handle をストア構成に合わせて調整すること。

**注意点:** コレクション名に 'hardware-' プレフィックスが付いていることを前提としており、他の命名規則の場合は `remove_first` の値を変更する必要がある。複数コレクションに属する商品は handle の文字数が最長のコレクション（最も詳細と想定）が選ばれるため、命名規則で親→子の階層を文字数で表現していないと誤分類される。/pages/category/〇〇 というカスタムページが存在しないと 404 になるため、事前にカテゴリページの作成か、リンク先を product.collections.first.url に変更するなど対応する。

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

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `gift-card` `template` `qr-code` `standalone-page` `customer`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/templates/gift_card.liquid) （ライセンス: MIT、204行）
- **ファイル:** `templates/gift_card.liquid`

**説明:** ギフトカードの金額、QRコード、カード番号を表示する専用ページテンプレート。Shopify 管理画面から送信されたギフトカードメールのリンク先として機能し、顧客がカード番号をコピーできるUI を備える。

**用途:** ギフトカード購入後、顧客が受け取るメール内のリンク先ページ。カード番号の確認・コピーと QR コードスキャンに対応。

**設置場所:** templates/gift_card.liquid として配置（Shopify が自動認識）。`layout none` で独立した HTML を出力し、Storefront API 未対応の gift_card オブジェクトに直接アクセスする。

**注意点:** Storefront API ではギフトカード情報が取得できないため、このテンプレートは REST API または Shopify 管理画面からのメール送信時にのみ動作する。ヘッドレス構成では Shopify が提供する公式ギフトカードページへのリダイレクトが必要。`gift_card.qr_identifier` は QR コード生成用のデータで、JavaScript(qrcode.js)で動的に描画される。currency_code_enabled 設定が有効な場合は通貨記号を付けて表示するため、shop.currency と settings.currency_code_enabled の整合性を確認する。

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


### 16. 🧩 スニペット ストア検索のWebSite構造化データ

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `json-ld` `schema-org` `search` `seo` `rich-result`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/json-ld-search.liquid) （ライセンス: MIT、17行）
- **ファイル:** `json-ld-search.liquid`

**説明:** ストア検索機能を schema.org の WebSite 型で構造化データ化し、Google にサイト内検索の URL パターンを認識させる。検索ボックスが Google 検索結果に「このサイト内で検索」として表示されるようになる。

**用途:** Google 検索結果に「このサイト内で検索」ボックスを表示させたいとき、またはサイト検索の SEO 評価を高めたいとき。

**設置場所:** snippets/json-ld-search.liquid に配置し、theme.liquid または sections/main-header.liquid 内の `</head>` 直前で `{% render 'json-ld-search' %}` で呼び出す。

**注意点:** SearchAction の target URL は実際の検索クエリ URL と完全に一致していること(/search?q= パラメータ名)が重要。カスタム検索ページを使っている場合は URL 形式を修正する必要がある。Google Search Console で URL 検査ツール > リッチリザルト で構造化データエラーが出ていないか確認し、本番リリース前に実装を検証する。

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


### 17. 🧩 スニペット パスワード保護ページのレイアウト

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `layout` `password-protection` `meta-tag` `css-variables` `theme-structure`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/layout/password.liquid) （ライセンス: MIT、20行）
- **ファイル:** `layout/password.liquid`

**説明:** ストアがパスワード保護モード中に表示されるレイアウトファイル。CSS変数・メタタグ・クリティカルCSSを一元管理し、パスワード入力ページを描画する基盤。

**用途:** ストアをメンテナンス中やプレビュー公開時に、パスワード入力画面を表示したいとき。Shopify 管理画面の「パスワード保護」設定時に自動適用される。

**設置場所:** layout/password.liquid として保存。パスワード保護モードが有効な場合、Shopify が自動的に password.liquid をレイアウトテンプレートとして使用する（編集不要だが、独自のメタタグやCSSを追加する際の拡張ポイント）。

**注意点:** {{ content_for_header }} と {{ content_for_layout }} は Shopify が自動注入するため、削除や移動はできない。CSS変数とメタタグは ssl_protocol / shop.name など全レイアウト共通で必要なため、password.liquid に限定して変更を加える場合は theme.liquid との差分を最小化する。パスワード入力フォーム自体は Shopify 側で生成されるため、このレイアウト内にカスタムフォームHTMLを記述しても表示されない（theme.liquid 側の password section で管理する）。

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

**カテゴリ:** コレクション/検索 ／ **難易度:** 初級 ／ **タグ:** `search` `url-parameter` `filter` `query-string` `conditional`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Detect search type used in searches/show-search-type.liquid) （ライセンス: MIT、17行）
- **ファイル:** `Detect search type used in searches/show-search-type.liquid`

**説明:** 検索 URL のクエリパラメータ `type=` から検索対象(商品/ページ/ブログ記事)を抽出し、該当タイプのみ表示。Shopify の検索フォームで複数タイプを同時検索したときに、結果ページでフィルタリング表示を実現する。

**用途:** 検索結果ページで「この検索は商品のみを対象としています」といった案内や、タイプごとにセクションを分ける表示に使う。ユーザーの検索意図を可視化し、UX を向上させる。

**設置場所:** search/show-search-type.liquid として配置し、search テンプレート内の検索結果リスト表示前に `{% render 'show-search-type' %}` で呼び出す。または検索結果の見出しセクションに直接貼り付ける。

**注意点:** クエリパラメータが URL に含まれることが前提のため、検索フォームの method が GET で type= パラメータが送信されるように設定されていないと機能しない。許可されるタイプは 'product,page,article' にハードコードされているので、カスタムサーチオブジェクトやメタオブジェクト検索に対応させるには allowedTypes 配列を追加する。canonical_url は published ページ専用なので draft 環境では動作せず、本番環境での検証が必須。

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

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `payment-method` `footer` `icon` `accessibility` `svg`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/payment-icons.liquid) （ライセンス: MIT、18行）
- **ファイル:** `snippets/payment-icons.liquid`

**説明:** ストアで有効な決済方法をアイコンで一覧表示するスニペット。SVG 形式のペイメントアイコンをループ出力し、ツールチップで決済方法名を表示する。

**用途:** フッターやチェックアウトページで「このストアは Visa・Mastercard・PayPal に対応」という信頼性表示。モバイル・デスクトップ共通で利用可能。

**設置場所:** snippets/payment-icons.liquid に配置し、footer.liquid または checkout/footer.liquid 内で `{% render 'payment-icons' %}` で呼び出す。

**注意点:** shop.enabled_payment_types は Shopify 管理画面の「設定 > 決済設定」で有効化した決済方法のみを返すため、未設定時は何も表示されない。type | payment_type_svg_tag フィルターは Online Store 2.0 以降で利用可能。ツールチップ表示には Bootstrap の data-bs-toggle が必須なため、テーマが Bootstrap に依存していることを確認する。

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


### 20. 🧩 スニペット 画像上のインタラクティブツールチップ

**カテゴリ:** UI部品 ／ **難易度:** 中級 ／ **タグ:** `image-map` `tooltip` `interactive` `responsive` `accessibility`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/Tooltips/sections/tooltips.liquid) （ライセンス: MIT、452行）
- **ファイル:** `Tooltips/sections/tooltips.liquid`

**説明:** 画像の指定位置にクリック可能なボタンを配置し、クリック時にツールチップポップアップを表示するセクション。レスポンシブ対応で、モバイルではアコーディオン、デスクトップではホバー表示に切り替わる。

**用途:** 商品の部位説明、製品スペック図解、画像マップ型のFAQなど、画像の座標に紐付けた説明情報を表示する場面で使用。

**設置場所:** sections/tooltips.liquid として配置。theme.liquid のセクション呼び出し部分に `{% section 'tooltips' %}` を追加し、テーマカスタマイザーでセクションを追加して画像とツールチップテキストを設定。

**注意点:** ツールチップの位置は top・left パーセンテージで指定するため、画像の実際のピクセル座標をパーセンテージに変換して入力する必要がある（計算例：画像幅 1000px の 300px 位置 = 30%）。画像のアスペクト比が変わるとツールチップ位置がずれるため、section.settings.image.aspect_ratio で自動調整が入るが、縦横比が大きく変わるレイアウトでは再調整が必須。JavaScript が無効な環境では リスト形式で順番表示されるため、no-js フォールバックのスタイルも合わせてテストする。

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


### 21. 🧩 スニペット ストア共通ヘッダー

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `header` `navigation` `account` `cart` `linklist`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/header.liquid) （ライセンス: MIT、37行）
- **ファイル:** `shopify/sections/header.liquid`

**説明:** ロゴ、グローバルナビメニュー、顧客アカウントリンク、カートへのアクセスをまとめたストア共通ヘッダー。顧客ログイン状態に応じてアカウント・ログアウト・ログイン・登録リンクを出し分ける。

**用途:** Online Store 2.0 テーマのすべてのページヘッダーに配置し、サイト全体の統一的なナビゲーション導線を提供する。

**設置場所:** shopify/sections/header.liquid に配置し、theme.liquid の <body> 内最上部で `{% section 'header' %}` で呼び出す。ロゴ画像パスと layout-menu スニペット、翻訳キー(locale/ja.json 等)を自店舗に合わせて調整。

**注意点:** ロゴはここでは静的な「Logo」テキストなので、実装時に `<img>` タグまたは Shopify 管理画面の settings で画像 URL を指定する形に変更する。顧客アカウント機能は shop.customer_accounts_enabled が true の場合のみ表示されるため、管理画面で「顧客アカウント」が有効になっていることを確認する。layout-menu スニペットが別ファイル(shopify/snippets/layout-menu.liquid)として存在している必要があり、メインメニューのリンクリストハンドルが正しく設定されていないとナビが表示されない。

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


### 22. 🧩 スニペット コレクションページのテンプレート

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `collection` `product-list` `pagination` `template` `table-layout`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/collection.liquid) （ライセンス: MIT、41行）
- **ファイル:** `templates/collection.liquid`

**説明:** コレクション内の商品を表形式で一覧表示するページテンプレート。商品画像・ベンダー名・価格・説明文を20件ずつページネーション表示する。

**用途:** カテゴリやタグで絞り込んだ商品一覧ページで、商品をシンプルな表形式でリスト表示したいとき。

**設置場所:** templates/collection.liquid に配置することで、Shopify は自動的にコレクションページを表示する際にこのテンプレートを使用する。テーマカスタマイザーで必要に応じてセクションを追加・削除できる。

**注意点:** product.featured_image が未設定だと画像が表示されないため、管理画面で各商品に代表画像を設定しておく必要がある。ページネーションは20件単位で固定されており、この値を変更する場合は `paginate collection.products by XX` の数字を修正する。product.description は HTML タグが含まれることがあるため strip_html と truncatewords で35語以下に制限しているが、日本語の場合は単語数では正確に切れない可能性があるので、実際の表示を確認してから運用する。

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


### 23. 🧩 スニペット 顧客ログイン・パスワード再設定

**カテゴリ:** 顧客アカウント ／ **難易度:** 初級 ／ **タグ:** `customer-login` `password-reset` `form` `account` `guest-checkout`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/sections/main-login.liquid) （ライセンス: MIT、238行）
- **ファイル:** `sections/main-login.liquid`

**説明:** 顧客アカウントのログインフォーム、パスワード再設定、ゲストチェックアウトを一つのセクションにまとめた実装。ロゴ画像やセクションパディングはテーマカスタマイザーで調整可能。

**用途:** accounts/login テンプレートページで、顧客がメールアドレス・パスワードでログインしたり、パスワードをリセットしたりする際に使用。ゲストチェックアウトが有効な場合はその選択肢も表示される。

**設置場所:** sections/main-login.liquid に配置し、templates/customers/login.liquid 内で `{% section 'main-login' %}` で呼び出す。ロゴ画像とパディングはテーマカスタマイザーで設定する。

**注意点:** マルチパス(Multipass)ログイン有効時はこのセクション全体が非表示になるため、`settings.multipass_login` が false であることが前提。パスワード再設定メール送信後の成功メッセージ表示は Shopify の `customer.recover_password.success` 翻訳キーを使用しており、各言語の多言語対応はストア管理画面で手動設定する必要がある。ロゴの縦横比が極端に異なると `divided_by` で計算した高さが不適切になるため、アップロード前に 2:1 前後の比率に調整するのが無難。

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


### 24. 🧩 スニペット サイト全体のOrganization構造化データ

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `json-ld` `schema-org` `organization` `seo` `branding`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/json-ld-organization.liquid) （ライセンス: MIT、22行）
- **ファイル:** `json-ld-organization.liquid`

**説明:** schema.org の Organization 型 JSON-LD をサイト全体に埋め込み、Google にストアの基本情報(ロゴ、URL、SNS リンク)を認識させる。ストアのブランド表示やナレッジパネルに活用される。

**用途:** Google 検索でストア名を検索したときに、サイドパネルにロゴや SNS リンク、会社情報が表示されるようにするため。theme.liquid 等に一度だけ埋め込む。

**設置場所:** snippets/json-ld-organization.liquid に配置し、theme.liquid の `</head>` 直前で `{% render 'json-ld-organization' %}` で呼び出す。または theme.liquid に直接記載する。

**注意点:** ロゴ画像ファイル名(`logo.png`)とテーマアセット内の実ファイル名を一致させておく必要があり、存在しないファイルを指定すると空 URL になる。SNS リンク(Facebook、Instagram など)は theme settings で事前に登録されている前提なので、管理画面のテーマカスタマイズで各 URL を埋めてから本スニペットが機能する。Google Search Console でリッチリザルトのエラーが出ないか確認し、実装後は数週間で Google インデックスに反映される。

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


### 25. 🧩 スニペット 404ページ

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `404` `error-page` `template` `route` `i18n`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/404.liquid) （ライセンス: MIT、24行）
- **ファイル:** `sections/404.liquid`

**説明:** 顧客が存在しないURLにアクセスしたときに表示される404エラーページ。エラーメッセージと全商品ページへのリンクを提供する。

**用途:** 無効なURL、削除された商品ページ、間違ったリンク先にアクセスされたときに、ストアを離脱させずに全商品ページへ誘導する。

**設置場所:** sections/404.liquid に配置し、Shopify 管理画面で自動的に templates/404.liquid テンプレートに紐付けられる。404 テンプレートがない場合は templates/404.liquid を新規作成してセクションを呼び出す。

**注意点:** 翻訳文字列『404.title』『404.not_found』『404.back_to_shopping』は theme の locales/ja.json に定義されていることが前提。デフォルトでは Shopify が用意した英語値が使われるため、日本語表示にするには各ストア言語ファイルに日本語訳を追加する必要がある。routes.all_products_collection_url が機能するには、管理画面で「全商品」コレクションが存在していることを確認する。

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


### 26. 🧩 スニペット ページネーション数の動的切替

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `pagination` `collection` `cart-attribute` `dynamic` `user-preference`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Dynamic pagination without alternate templates/dynamic-pagination.liquid) （ライセンス: MIT、20行）
- **ファイル:** `Dynamic pagination without alternate templates/dynamic-pagination.liquid`

**説明:** コレクションページの表示件数をカート属性で動的に変更するスニペット。デフォルト40件から、ユーザーが選択した件数に切り替えられる。

**用途:** コレクションページで「1ページあたり 20件 / 40件 / 100件表示」を切り替えるセレクトボックスを用意し、ユーザー選択を記憶させたいとき。

**設置場所:** collection.liquid または collection-grid.liquid 内の paginate タグの直前に貼り付ける。表示件数を選択するフォーム側では `<form method="post"><input type="hidden" name="attributes[pagination]" value="20"></form>` の形でカート属性に値を保存する。

**注意点:** cart.attributes.pagination は顧客がカートを編集するたびに値が保持されるため、ログアウト後も選択値が残る。複数タブ開いているとキャッシュずれが生じやすいので、AJAX でカート属性を更新する際は応答を確認してからページをリロードする。paginationAmount に負の値が入るリスクを `| abs` で防いでいるが、0 や極端な大きさ(数千件)を入力された場合のバリデーションは別途実装が必要。

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


### 27. 🧩 スニペット メタフィールドカスタムバッジ

**カテゴリ:** メタフィールド/メタオブジェクト ／ **難易度:** 中級 ／ **タグ:** `metafield` `product` `badge` `custom` `dynamic`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-custom-badge.liquid) （ライセンス: MIT、19行）
- **ファイル:** `snippets/product-custom-badge.liquid`

**説明:** 商品のメタフィールドから テキストと色を読み込み、カスタムバッジを動的に表示するスニペット。管理画面で商品ごとにバッジ内容を設定でき、セール・限定商品・在庫状況などを柔軟に表現できる。

**用途:** 商品カードや商品詳細ページで、マーチャント側が管理画面のメタフィールドで設定したバッジを表示したいとき。テーマカスタマイザーからバッジテンプレートの背景色も調整できる。

**設置場所:** snippets/product-custom-badge.liquid に配置し、product-card.liquid または main-product.liquid 内の任意の場所で `{% render 'product-custom-badge', product: product %}` で呼び出す。

**注意点:** 事前に管理画面で product メタフィールド定義(namespace.key 形式)を作成し、テーマ設定の `product_custom_badge_metafield` にそのハンドルを `namespace.key` の形で入力しておくことが必須。メタフィールド値は `テキスト|カラーコード` の形(例: `セール|#ff0000`)で入力し、パイプ記号で分割される。色指定がない場合は管理画面の `product_custom_badge_bg_color` 設定値がデフォルト背景色になり、`color_darken: 15` でボーダー色が自動的に暗くされるため、十分なコントラスト比になるか確認する。

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

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `layout` `html` `meta-tag` `asset-preload` `section`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/layout/theme.liquid) （ライセンス: MIT、42行）
- **ファイル:** `shopify/layout/theme.liquid`

**説明:** すべてのページの HTML 骨組みを定義するレイアウトファイル。言語設定、メタタグ、CSS/JS のプリロード、ヘッダー・フッターセクション、メインコンテンツ領域を統一的に出力する。

**用途:** Online Store 2.0 テーマの基盤。すべてのページで共有される HTML 構造・メタ情報・アセット読み込みを一元管理するのに用いる。

**設置場所:** shopify/layout/theme.liquid として配置（上書き不可のテーマコア）。header・footer セクション、bundle.css / bundle.js のファイルパス・ハンドルを自プロジェクトに合わせて修正。

**注意点:** content_for_header は Shopify の公式スクリプト（カート JS など）が挿入される領域のため、削除・移動は禁止。favicon は管理画面で設定されていないと img_url フィルターで nil が返るため、{% if %} で保護が必須。webpack や他ビルドツールでバンドルファイル名が変わる場合は、asset_url のハンドル（'bundle.css'・'bundle.js'）を実装に合わせて更新する。

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


### 29. 🧩 スニペット カテゴリグリッド表示(複数列)

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `section` `grid` `category` `metaobject` `collection` `card`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/sections/category-multicolumn.liquid) （ライセンス: MIT、112行）
- **ファイル:** `sections/category-multicolumn.liquid`

**説明:** コレクション配下のカテゴリを複数列グリッドで表示するセクション。各カテゴリは画像・タイトル・説明付きカードで、ホバー時に背景色が変わる。メタオブジェクトで子カテゴリのプリロード画像も指定できる。

**用途:** オンラインストアのカテゴリページ(例：ファッション → 「メンズ」「レディース」「キッズ」など)で、階層化されたカテゴリ一覧を視覚的に表示するとき。

**設置場所:** sections/category-multicolumn.liquid に配置。ページテンプレート(例：template-collection.liquid または page.liquid)で `{% section 'category-multicolumn' %}` として呼び出し、テーマカスタマイザーでコレクションと各カテゴリブロックを設定する。

**注意点:** ブロックの image_picker で画像が設定されていることが前提。metaobject_type『category_metaobject』は事前に Shopify 管理画面で定義し、子カテゴリの画像フィールドを含めておく必要がある。プリロード(`<link rel="preload">`)は次の階層の画像に限定されるため、深い階層まで高速化したい場合は JavaScript で動的に追加する。グリッドレイアウトは自動折り返し(minmax 25rem)なので、モバイルではカード幅が圧縮されるため、スマホ向けに font-size や padding をメディアクエリで調整するとよい。

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


### 30. 🧩 スニペット テーマ全体のレイアウト・CSS変数設定

**カテゴリ:** テーマ基盤 ／ **難易度:** 上級 ／ **タグ:** `layout` `css-variables` `typography` `color` `responsive` `theme-settings`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/layout/theme.liquid) （ライセンス: MIT、242行）
- **ファイル:** `layout/theme.liquid`

**説明:** Shopify テーマの共通レイアウトファイル。フォント・色・ボタンスタイルなどの設計値を CSS カスタムプロパティ(変数)に変換し、すべてのページで統一された見た目を実現する。

**用途:** すべてのページテンプレートの基礎となるファイル。テーマカスタマイザーで変更した色やフォント設定を CSS 変数として各ページに反映させるときに必須。

**設置場所:** layout/theme.liquid はテーマの標準ファイルで、置き換えが必要な場合は Shopify Admin の「コードエディタ」で直接編集する。他のファイルから呼び出す必要はなく、すべてのテンプレートが自動的にこのレイアウトを継承する。

**注意点:** settings で参照しているテーマ設定(type_body_font、colors_text など)が theme-settings.json に定義されていることが前提。フォント weight の計算で `plus: 300 | at_most: 1000` を使っているため、元のフォント weight が700以上だと1000に上限される仕様を理解しておく。CSS 変数値に数値を含める場合(spacing、radius など)は px や rem 単位を明示的に付けないと calc() で計算できなくなるため、液体テンプレート出力時に単位を忘れずに追加する。

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


### 31. 🧩 スニペット ランダムな商品を取得

**カテゴリ:** ユーティリティ ／ **難易度:** 中級 ／ **タグ:** `product` `collection` `random` `utility` `loop`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/random-product.liquid) （ライセンス: MIT、32行）
- **ファイル:** `random-product.liquid`

**説明:** ストア内のすべての商品、または指定したコレクションからランダムに1つの商品を取得するスニペット。タイムスタンプのナノ秒をモジュロ演算で使い、疑似乱数生成する。

**用途:** トップページやサイドバーで「おすすめ商品をランダム表示」したいとき、または特定カテゴリの商品をシャッフル表示させたいシーン向け。

**設置場所:** snippets/random-product.liquid に配置し、表示させたいセクション内で `{% render 'random-product' %}` または `{% render 'random-product' with specific_collection: 'コレクションハンドル' %}` で呼び出す。呼び出し後、`{{ random_product }}` で取得した商品オブジェクトが利用可能。

**注意点:** 乱数生成は `"now" | date: "%N"` でナノ秒を取得しているため、同一秒内に複数回呼び出すと同じ商品が返る可能性がある。より強力な乱数が必要な場合は外部 JavaScript ライブラリとの連携を検討する。コレクション指定時のハンドル誤入力は無視されるため、管理画面で正確なハンドルを確認してから使用する。

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


### 32. 🧩 スニペット ブログ記事一覧ページ

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `blog` `article` `pagination` `template` `listing`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/blog.liquid) （ライセンス: MIT、36行）
- **ファイル:** `sections/blog.liquid`

**説明:** ブログテンプレートで使用する記事一覧セクション。ブログ内のすべての記事をカード形式で表示し、ページネーション対応。記事ごとに画像・タイトル・公開日・著者・抜粋文を表示する。

**用途:** Shopify 管理画面の「ブログ」セクションで作成したブログの記事一覧ページ(/blogs/news など)で、複数記事をリスト表示したいとき。

**設置場所:** sections/blog.liquid に配置し、templates/blog.liquid で `{% section 'blog' %}` で呼び出す。Shopify の blog テンプレートと自動連携される。

**注意点:** ページネーションの件数(ここでは5件)は `{% paginate blog.articles by 5 %}` の数値を変更して調整する。article.image が未設定の記事では画像が出ないため、ブログ記事投稿時にアイキャッチ画像を必ず設定する習慣をつける。日付と著者表示は `blog.article_metadata_html` の翻訳キーに依存するため、多言語対応時は Shopify 管理画面の言語設定で各言語の翻訳文を確認する。

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


### 33. 🧩 スニペット SKU検索のJSON出力エンドポイント

**カテゴリ:** API連携/JSON出力/JS統合 ／ **難易度:** 中級 ／ **タグ:** `search` `sku` `json` `api-endpoint` `liquid-json`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Search by SKU/search.sku.liquid) （ライセンス: MIT、23行）
- **ファイル:** `Search by SKU/search.sku.liquid`

**説明:** 検索フォームで入力された SKU キーワードに該当する商品を JSON 形式で返すカスタムエンドポイント。検索結果をAPI的に取得でき、外部スクリプトやモバイルアプリから商品情報にアクセスできる。

**用途:** POS連携や在庫管理システムが SKU で商品を検索する必要があるとき。またはモバイルアプリやJavaScript からストアの商品データを SKU 検索で取得したいシーン。

**設置場所:** templates/search.sku.liquid として新規作成し、Shopify 管理画面の設定で検索フォームの action を `/search.sku` に指定する。または JavaScript の `fetch('/search.sku?q=SKU_CODE')` で JSON 応答を受け取る。

**注意点:** このテンプレートは layout: none で HTML 出力を排除するため、`/search.sku?q=...` にアクセスすると JSON のみが返される。検索クエリに該当する商品がない場合は空配列 `{"products": []}` が返るので、フロント側で結果の有無をチェック。Shopify 検索は SKU 完全一致ではなく部分一致なため、複数商品ヒットの可能性がある。レート制限やボット対策が不要な場合のみ使用し、本番環境では `request.ip` チェックやアクセスログを追加する。

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


### 34. 🧩 スニペット 商品ページのリッチテキスト

**カテゴリ:** 商品表示 ／ **難易度:** 中級 ／ **タグ:** `product` `block` `richtext` `padding` `typography`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-block-richtext.liquid) （ライセンス: MIT、22行）
- **ファイル:** `snippets/product-block-richtext.liquid`

**説明:** 商品詳細ページに見出しと説明文を柔軟に配置できるブロック。タイトルの有無、カスタム説明文と商品説明の組み合わせ、上下のパディングを管理画面から制御。

**用途:** 商品ページで説明文を複数ブロックに分割して配置したい、または商品の説明を追記や別フォーマットで表示したいとき。

**設置場所:** snippets/product-block-richtext.liquid に配置し、sections/main-product.liquid 内で `{% render 'product-block-richtext', block: block, product: product %}` で呼び出す。Online Store 2.0 のブロックとして schema.json に登録することで、管理画面から動的に追加可能。

**注意点:** block.settings の pt(上パディング) / pb(下パディング) / title_font_size / description_font_size は theme.json の preset で定義済みである必要があるため、スタイル設定を管理画面に露出させておく。product.description の表示をトグルするときは、デフォルト商品説明が重複表示されないよう別途商品テンプレートで非表示にしておく。description クラスに rte が付いているため、エディタで記入したリッチテキスト(太字・リンク等)が正しくレンダリングされるよう theme.css で rte クラスのスタイルを用意する。

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


### 35. 🧩 スニペット Vue コンポーネントの実装例

**カテゴリ:** API連携/JSON出力/JS統合 ／ **難易度:** 上級 ／ **タグ:** `vue` `component` `vuex` `shopify-theme-lab` `javascript-framework`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/vue-examples.liquid) （ライセンス: MIT、162行）
- **ファイル:** `shopify/sections/vue-examples.liquid`

**説明:** Shopify Theme Lab を使った Vue コンポーネント、Vuex ストア、グローバルミックスイン・ディレクティブの実装デモ。スロット・プロップス・renderless パターンを含む複数の実装パターンを示す。

**用途:** Vue ベースのモダンテーマ開発環境を構築・学習するとき。コンポーネント設計や状態管理の実装パターンをテーマセクションで実装・確認したいとき。

**設置場所:** shopify/sections/vue-examples.liquid に配置し、テーマカスタマイザーでセクションを追加するか、テンプレート内で `{% section 'vue-examples' %}` で呼び出す。前提として Shopify Theme Lab の Vue ビルド環境(src/vue/components、src/vue/store など)が整備されていることが必須。

**注意点:** このセクションは開発用デモであり、本番テーマでは削除すること。shop オブジェクト(shop.name、shop.domain など)は Liquid テンプレート側で挿入されるため、Vue コンポーネント側で直接アクセスできないので prop 経由で渡す設計になっている。Vuex モジュール('my-module' など)はあらかじめ src/vue/store に定義されている前提のため、実際の運用では自店舗のモジュール名・アクション名に置き換える。

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


### 36. 🧩 スニペット ホームページのカテゴリグリッド

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `homepage` `metaobject` `grid` `category` `section`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/sections/homepage.liquid) （ライセンス: MIT、119行）
- **ファイル:** `sections/homepage.liquid`

**説明:** ホームページにメタオブジェクトで管理したカテゴリを階層的に表示するセクション。複数のカテゴリグループを管理画面から追加でき、各カテゴリ配下の子カテゴリを小さいグリッド形式で一覧表示する。

**用途:** ホームページのトップに「すべてのカテゴリ」セクションを設け、サムネイル付きで商品カテゴリを見やすく並べたいとき。管理画面のカスタマイズ画面からカテゴリグループを動的に追加・並び替えできる。

**設置場所:** sections/homepage.liquid に配置し、theme.liquid の body 内で `{% section 'homepage' %}` で呼び出すか、テーマカスタマイザーのホームページセクションから「カテゴリグリッド」ブロックを追加して使う。

**注意点:** category_metaobject というメタオブジェクト型が Shopify 管理画面で事前に定義されていることが前提。メタオブジェクト内の child.name が ' > ' で区切られた階層文字列であると想定しているため、命名ルールに ' > ' が含まれていない場合は `split` フィルターを適宜修正する必要がある。また、各カテゴリメタオブジェクトに image フィールドが存在し、child.system.url が正しく設定されていることを確認してから運用を開始する。

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


### 37. 🧩 スニペット Twitterカードメタタグ(商品・記事別)

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `twitter-card` `meta-tag` `seo` `social-share` `open-graph`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/metadata-twitter.liquid) （ライセンス: MIT、37行）
- **ファイル:** `metadata-twitter.liquid`

**説明:** 商品ページと記事ページに対応した Twitter Card メタタグを自動出力するスニペット。テンプレート種別に応じて、商品情報(価格・在庫)または記事内容(サムネイル)を Twitter 共有時に表示させる。

**用途:** 商品や記事を Twitter / X でシェアされたときに、タイトル・説明・画像がプレビュー表示されるようにしたいとき。ストアのブランド認知度向上に活用。

**設置場所:** snippets/metadata-twitter.liquid に配置し、theme.liquid の <head> 内で `{% render 'metadata-twitter' %}` で呼び出す。

**注意点:** 6行目の `@twitter_handler` はストアの Twitter / X ハンドルに置き換え必須。記事ページの画像抽出は article.content 内の最初の <img> タグの src 属性を正規表現なしで分割して取得するため、画像が存在しないと表示されない。ロゴ画像(logo-square.png)は 1:1 のアスペクト比を必ず守り、アセットフォルダに配置しておく。商品の価格が複数バリアント間で異なる場合は『From ¥XXX』と表示されるが、最安値のみ出すよう `product.price` の代わりに `product.variants | map: 'price' | sort | first` に変更するとよい。

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


### 38. 🧩 スニペット パスワード保護ページ

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `password` `protection` `form` `storefront` `template`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/password.liquid) （ライセンス: MIT、36行）
- **ファイル:** `sections/password.liquid`

**説明:** ストアにパスワード保護が有効なときに表示されるランディングページ。パスワード入力フォームと管理画面で設定したメッセージを表示する。

**用途:** ストアをプレオープン状態で限定公開したいとき、または メンテナンス中に顧客アクセスを制限する際に使用。

**設置場所:** sections/password.liquid として設置し、templates/password.liquid から `{% section 'password' %}` で呼び出す。パスワードはストア管理画面の「設定 > パスワード保護」で設定する。

**注意点:** shop.password_message は Shopify 管理画面で入力されていない場合は表示されないため、テンプレートでは if 分岐で段階的に処理している。form.errors の表示は `default_errors` フィルターで Shopify のデフォルトエラーメッセージが自動出力されるため、カスタムエラー定義は不要。このセクションは password.liquid テンプレートの専用セクションであり、他のテンプレートでは使用できない。

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


### 39. 🧩 スニペット メタフィールドでコレクション商品を並替

**カテゴリ:** コレクション/検索 ／ **難易度:** 上級 ／ **タグ:** `metafield` `collection` `sort` `product` `custom-order`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Sort Shopify collection by metafield/sort-shopify-collection-products-by-metafield-value-commentless.liquid) （ライセンス: MIT、24行）
- **ファイル:** `Sort Shopify collection by metafield/sort-shopify-collection-products-by-metafield-value-commentless.liquid`

**説明:** コレクション内の商品を、メタフィールド(global.order)に保存された数値順に再ソートするスニペット。ゼロパディングと配列操作で Liquid の制限下でもカスタム順序を実現する。

**用途:** 管理画面のドラッグ&ドロップ機能がない場合や、メタフィールドで細かい表示順を制御したいとき。コレクションページや関連商品セクションで商品の並び順を完全にカスタマイズできる。

**設置場所:** sections/main-collection.liquid または sections/collection-products.liquid 内で、`{% for product in collection.products %}` ループの代わりに本スニペットに置き換える。各商品のメタフィールド(namespace: global、key: order)に1〜999999の数値を事前に設定しておく。

**注意点:** Shopify 管理画面で該当商品の global namespace のメタフィールド『order』を数値型で作成し、全商品に値を入力していることが前提。値が未設定の商品は自動的に 999999 として末尾に移動する。ゼロパディングは最大6桁の数値対応のため、100万以上の商品数や極端に大きい数値を使う場合は zeroFill の長さと除算ロジックを調整が必要。

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


### 40. 🧩 スニペット セクションのタイトル・説明文ヘッダー

**カテゴリ:** UI部品 ／ **難易度:** 初級 ／ **タグ:** `section` `header` `reusable` `typography` `settings`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/section-header.liquid) （ライセンス: MIT、24行）
- **ファイル:** `snippets/section-header.liquid`

**説明:** セクションの上部に共通で使うタイトルと説明文を表示するスニペット。セクション設定からタイトル・説明文とそのフォントサイズを取得し、条件付きで描画する。

**用途:** コレクション紹介セクション、特集セクション、ニュースレター登録セクションなど、複数のセクションで統一したヘッダー表示が必要なときに親スニペットとして使用。

**設置場所:** snippets/section-header.liquid に配置し、各セクション(sections/section-*.liquid)内で `{% render 'section-header', class: 'my-custom-class' %}` として呼び出す。セクション設定に header_title、header_description、header_title_font_size、header_description_font_size を定義しておくこと。

**注意点:** このスニペットはセクション設定(section.settings)を参照するため、呼び出し元セクションの schema で header_title、header_description、header_title_font_size、header_description_font_size の4つの設定項目が定義されていることが前提。タイトルと説明文がともに空のときは header 要素そのものがレンダリングされないので、デフォルト設定値をセクション側で用意するとよい。RTE クラスを使うため、説明文の Markdown リンク(例: [テキスト](url))は自動で <a> タグに変換される。

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
| 処理時間（秒） | 34.8 | 36.3 | — |
| 入力 tokens | 122,429 | 46,679 | -75,750 |
| 出力 tokens | 21,116 | 23,983 | +2,867 |
| キャッシュ作成 tokens | 0 | 34,704 | +34,704 |
| キャッシュ読込 tokens | 0 | 182,196 | +182,196 |
| 推定コスト (USD) | $0.2280 | $0.2282 | +$0.0002 |

### カテゴリ分布の変化

| カテゴリ | v1 | v2 | 差分 |
|---|---:|---:|---:|
| ページテンプレート | 10 | 10 | 0 |
| テーマ基盤 | 4 | 5 | +1 |
| ヘッダー/フッター/ナビゲーション | 4 | 5 | +1 |
| UI部品 | 5 | 4 | -1 |
| リファレンス/フィルター | 4 | 4 | 0 |
| コレクション/検索 | 3 | 4 | +1 |
| リファレンス/タグ | 3 | 3 | 0 |
| SEO/構造化データ | 3 | 3 | 0 |
| リファレンス/オブジェクト | 3 | 3 | 0 |
| API連携/JSON出力/JS統合 | 3 | 3 | 0 |
| ユーティリティ | 3 | 2 | -1 |
| 商品表示 | 3 | 2 | -1 |
| メタフィールド/メタオブジェクト | 1 | 1 | 0 |
| 顧客アカウント | 1 | 1 | 0 |

### 難易度分布の変化

| 難易度 | v1 | v2 |
|---|---:|---:|
| 初級 | 31 | 31 |
| 中級 | 17 | 15 |
| 上級 | 2 | 4 |
