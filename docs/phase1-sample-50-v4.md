# liquid-jp.jp Phase 1 サンプル50件レポート (v4: 日本語スタイル整備版)

生成日時: 2026-05-13 21:24 ／ モデル: `claude-haiku-4-5-20251001`

## サマリ

- 件数: **50件**（成功 50 / 失敗 0）
  - コミュニティスニペット: **40件**
  - 公式リファレンス（theme-liquid-docs）: **10件**
- 処理時間: 37.7秒（並列 8）
- API コスト: **$0.2402**（入力 46,679 tok ＋ 出力 23,678 tok、cache_read 277,772 tok)

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
| 初級 | 28 |
| 中級 | 17 |
| 上級 | 5 |

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

### 1. 📘 リファレンス sort_by フィルター（コレクションURL にソート条件を付与）

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `sort` `collection` `url` `filter` `title-too-long`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** コレクション URL にソートパラメータを追加するフィルター。人気順、タイトル昇降順、価格昇降順、作成日昇降順など8種類の並び順に対応する。

**用途:** コレクションページで複数のソート条件をリンク化して提供するとき。例えば「価格が安い順」「新着順」といったドロップダウンやボタンで、クリック時に対応する URL へ遷移させる。

**設置場所:** collection.liquid などコレクションテンプレート内で、`{{ collection.url | sort_by: 'best-selling' }}` のように `collection.url` に対して適用する。ソート条件を持つ URL 文字列が返るので、a タグの href 属性に設定する。

**注意点:** sort_by フィルターは collection.url プロパティに対してのみ適用できる。指定できる値は manual（コレクション設定のデフォルト順）、best-selling（売上順）、title-ascending/descending（タイトル昇降順）、price-ascending/descending（価格昇降順）、created-ascending/descending（作成日昇降順）の8種類に限定される。url_for_type フィルターや url_for_vendor フィルターと組み合わせることで、ベンダーやタイプ別ページでのソート機能も実装できる。

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

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `escape` `security` `html` `xss-prevention`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** HTML特殊文字（<、>、&、シングルクォート）をエスケープシーケンスに変換する。ユーザー入力やメタフィールドの値を画面に出力するときに、スクリプトインジェクション対策として機能する。

**用途:** 顧客名・商品説明・レビューコメントなどのユーザー入力を商品ページやカートに表示するとき、悪意あるコード埋め込みを防ぐため。

**設置場所:** Liquid 内で `{{ 変数 | escape }}` の形で使う。例: `{{ customer.name | escape }}` とすることで、顧客名に含まれる HTML 特殊文字が安全に変換される。

**注意点:** escape フィルターはすでにエスケープされた文字（例：`&lt;` として格納されている値）に対しては二重エスケープされるため、出力元が既にエスケープ済みか確認する必要がある。対応する文字が存在しない場合はそのまま出力される。

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


### 3. 📘 リファレンス floor フィルター（数値を切り下げ）

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `math` `number` `rounding` `integer`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、30行）
- **ファイル:** `data/filters.json`

**説明:** 小数点以下を切り下げ、数値を最も近い整数に丸める。1.2 は 1、2.9 は 2 になる。

**用途:** 商品の個数計算や在庫表示、割引率の端数処理など、常に下向きに丸めたい数値演算で使う。

**設置場所:** Liquid テンプレート内で `{{ 価格 | floor }}` または `{{ 数量 | floor }}` の形で、小数を含む変数に対して適用する。

**注意点:** 負の数を渡した場合、-1.5 は -2 になる点に注意（0 に向かって丸まるのではなく、より小さい整数に丸まる）。金額計算に使う場合は先に通貨換算を済ませ、型が数値であることを `| times: 1` で明示する。

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


### 4. 📘 リファレンス link_to_type フィルター（商品タイプ別コレクションへのリンク生成）

**カテゴリ:** リファレンス/フィルター ／ **難易度:** 初級 ／ **タグ:** `link-to-type` `filter` `collection` `product-type` `html-attribute` `title-too-long`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/filters.json) （ライセンス: MIT、48行）
- **ファイル:** `data/filters.json`

**説明:** 商品タイプを指定して、そのタイプに属する全商品を表示するコレクションページへのリンク HTML を生成するフィルター。`<a>` タグを返す。

**用途:** 商品詳細ページやコレクションで「同じタイプの他の商品を見る」リンクを出すときや、サイドバーのタイプフィルター一覧をリンク化するとき。

**設置場所:** Liquid テンプレート内で `{{ '商品タイプ名' | link_to_type }}` または `{{ '商品タイプ名' | link_to_type: class: 'link-class' }}` の形で使う。class などの HTML 属性をパラメータで指定できる。

**注意点:** フィルターの引数は商品タイプの文字列であり、ハンドル名ではなく管理画面に登録された商品タイプ名そのものを指定する必要がある。生成されるリンク href は `/collections/types?q=商品タイプ名` 形式の自動URL になるため、ストアのコレクションテンプレートが対応していることが前提。HTML 属性は `attribute: value` の形で複数指定可能だが、属性値に特殊文字が含まれる場合は引用符で囲む。

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


### 5. 📘 リファレンス decrement タグ（変数を1ずつ減らす）

**カテゴリ:** リファレンス/タグ ／ **難易度:** 初級 ／ **タグ:** `variable` `decrement` `counter` `loop`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、28行）
- **ファイル:** `data/tags.json`

**説明:** 新しい変数を作成し、初期値 -1 から始まって、呼び出すたびに 1 ずつ減らす。同じレイアウト・テンプレート・セクション内で宣言された変数は、そのファイルに含まれるすべてのスニペットで共有される。

**用途:** 商品リストやループ内でカウントダウンが必要な場合、例えば在庫をカウントダウンしたり、逆順での番号付けをしたりするときに使う。

**設置場所:** Liquid テンプレート内で `{% decrement 変数名 %}` の形で使う。呼び出すたびに変数の値が 1 減り、その値がページに出力される。

**注意点:** decrement で作成した変数は assign や capture で作成した変数とは独立しているが、increment との間では変数を共有する。Liquid の組み込みオブジェクト（product、cart など）と同じ名前の変数を作ると上書きされるため、変数名は被らないように注意する。

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


### 6. 📘 リファレンス for タグ（配列の要素をループ）

**カテゴリ:** リファレンス/タグ ／ **難易度:** 初級 ／ **タグ:** `loop` `iteration` `array` `forloop`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、113行）
- **ファイル:** `data/tags.json`

**説明:** 配列内のすべての要素に対して式をレンダリングするループタグ。limit、offset、range、reversed パラメータで反復の範囲や順序を制御できる。

**用途:** 商品一覧やコレクションを画面に表示するときに、商品の個数分だけ HTML を繰り返し出力する。ページネーション対応や数値範囲の生成にも使う。

**設置場所:** Liquid テンプレート内で `{% for variable in array %} ... {% endfor %}` の形で使用する。collection.products、shop.blogs、metafield の配列など、任意の配列オブジェクトを反復できる。

**注意点:** 単一の for ループは最大 50 回の反復に制限されるため、それ以上の項目がある場合は paginate タグでページ分割する。limit パラメータよりも paginate による分割がサーバー側パフォーマンスの観点で推奨される。ループ内では forloop オブジェクト（index、first、last など）が自動で利用可能。

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

**カテゴリ:** リファレンス/タグ ／ **難易度:** 初級 ／ **タグ:** `loop` `iteration` `fallback` `for` `conditional`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/tags.json) （ライセンス: MIT、40行）
- **ファイル:** `data/tags.json`

**説明:** for ループの配列が空（要素ゼロ）のとき、代わりに実行する式を指定する。ループ本体が一度も実行されない場合のフォールバック処理に使う。

**用途:** コレクション内に商品がない、検索結果がない、など配列が空のシーンで「該当なし」メッセージを画面に表示したいとき。

**設置場所:** {% for %} タグの閉じる直前に {% else %} を挿入し、その後にフォールバック時の Liquid コードを書く。例えば product カード描画の場合、{% for product in collection.products %} の後ろに配置する。

**注意点:** else は for ループの直下にのみ使える。if や case などの条件タグには対応していない。ループが 1 回以上実行される場合は else 以降は実行されないため、フォールバック時のロジックのみを記述する。

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

**カテゴリ:** リファレンス/オブジェクト ／ **難易度:** 中級 ／ **タグ:** `metafield` `measurement` `product` `dimension` `weight` `volume`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、86行）
- **ファイル:** `data/objects.json`

**説明:** メタフィールドの measurement 型から取得した寸法・容量・重量の値と単位を扱うオブジェクト。type、value、unit の3つのプロパティで構成される。

**用途:** 商品ページで牛乳パックの容量（例：1L）や衣料品のサイズ（例：幅30cm）、重量（例：500g）をメタフィールドから取得して表示するとき。

**設置場所:** 商品メタフィールドを `product.metafields.{namespace}.{key}.value` で取得した measurement オブジェクトに対して、Liquid テンプレート内で `{{ measurement.type }}`、`{{ measurement.value }}`、`{{ measurement.unit }}` の形で各プロパティを参照する。

**注意点:** measurement オブジェクトは Shopify 管理画面でメタフィールド型を「寸法」「容量」「重量」に明示的に設定したときのみ利用可能。value は数値型だが、Liquid 内で計算を行う場合は `| times: 1` で数値化を確実にする。unit と value の組み合わせはメタフィールド設定時の単位系（cm/m、ml/l、g/kg など）に依存するため、ストア側で統一しておくこと。

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

**カテゴリ:** リファレンス/オブジェクト ／ **難易度:** 中級 ／ **タグ:** `model` `3d` `media` `cdn` `product`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、74行）
- **ファイル:** `data/objects.json`

**説明:** 3D モデルのソースファイル情報を参照するオブジェクト。ファイル形式、MIME タイプ、CDN URL にアクセスできる。

**用途:** 商品の 3D モデルを Liquid テンプレートで操作するとき。`product.featured_media.sources` 配列内の各ソースファイルの詳細（形式、タイプ、URL）を取得する。

**設置場所:** Liquid テンプレート内で `{{ product.featured_media.sources[0].format }}` のように model_source のプロパティ（format / mime_type / url）を参照する。sources は配列なので、ループ `{% for source in product.featured_media.sources %}` で複数形式に対応できる。

**注意点:** model_source は `product.featured_media` が 3D モデルメディアのときのみ利用可能。画像やビデオなど他のメディアタイプでは sources が空になる。複数の 3D ファイル形式（glb、usdz など）がある場合は sources[0]、sources[1] 等で形式を区別して参照する。

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

**カテゴリ:** リファレンス/オブジェクト ／ **難易度:** 上級 ／ **タグ:** `remote-product` `multi-store` `marketplace` `object-property`

- **出典:** [`Shopify/theme-liquid-docs`](https://raw.githubusercontent.com/Shopify/theme-liquid-docs/main/data/objects.json) （ライセンス: MIT、69行）
- **ファイル:** `data/objects.json`

**説明:** 他のストアから取得した商品など、リモートソースから参照されるオブジェクトの出所情報を提供する。オブジェクトがどのストアから、どのような経路で取得されたかを示すプロパティを持つ。

**用途:** Shopify Markets やマーケットプレイス連携など、複数ストア間で商品を共有・参照する際、その商品の出元ストアや取得経路をストア上に表示したいとき。

**設置場所:** remote_product オブジェクトを通じて `{{ remote_product.remote_details.type }}` や `{{ remote_product.remote_details.shop }}` の形で参照する。

**注意点:** remote_details は remote_product からのみアクセス可能であり、通常の product オブジェクトには存在しないため、リモートソース対応の実装でのみ利用される。type プロパティの値は現在「seller」のみだが、将来拡張される可能性があるため、値による条件分岐が後で追加される可能性を見越して実装する。

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

### 1. 🧩 スニペット 固定ページの本文表示

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `page` `template` `content` `static-page` `section`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/page.liquid) （ライセンス: MIT、18行）
- **ファイル:** `sections/page.liquid`

**説明:** Shopify 管理画面で作成した固定ページ（利用規約、特定商取引法など）のタイトルと本文をストアに表示するセクション。ページテンプレートの基本構造を提供する。

**用途:** 「このサイトについて」「お問い合わせ」「利用規約」など、商品以外の静的コンテンツページを構築するときに使う。

**設置場所:** sections/page.liquid に配置し、templates/page.liquid で `{% section 'page' %}` と呼び出すと、管理画面で作成したページのタイトルと本文がそのまま表示される。

**注意点:** page.content は HTML をそのまま出力するため、管理画面での編集時に意図しないタグが混入していないか確認する必要がある。ページタイトル直下に自動的に h1 を出力するので、タイトルの二重表示を避けるため schema 側に追加設定がない仕様。CSS でタイトルと本文の余白やフォントを調整し、テーマ全体の視覚階層に統一する。

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

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `request` `domain` `multidomain` `conditional` `asset`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Get current domain name with Liquid/request_host.liquid) （ライセンス: MIT、15行）
- **ファイル:** `Get current domain name with Liquid/request_host.liquid`

**説明:** アクセスしたドメインを判定して、異なるバナー画像を表示するスニペット。request.host を使ってドメイン別に asset_url で画像を出し分ける。

**用途:** 日本・オーストラリア・グローバルなど複数ドメインで Shopify を運用しているとき、ドメインごとに異なるバナーやロゴを表示したい。

**設置場所:** snippets/request_host.liquid として配置し、theme.liquid のヘッダー内または section 内の画像表示部分で `{% render 'request_host' %}` で呼び出す。条件分岐のドメイン名を自店舗のカスタムドメインに置き換える。

**注意点:** request.host は開発ストア(*.myshopify.com)では正常に機能しないため、カスタムドメイン設定が前提となる。条件分岐が3ドメイン以上になると可読性が低下するため、Shopify Markets や theme settings の選択肢ベースに切り替えるとよい。プレビュー環境では request.host が本番と異なる可能性があるため、本番ドメイン確定後に検証してからリリースする。

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


### 3. 🧩 スニペット 商品セクション間の区切り線

**カテゴリ:** 商品表示 ／ **難易度:** 初級 ／ **タグ:** `product` `block` `separator` `divider` `ui-component`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-block-separator.liquid) （ライセンス: MIT、15行）
- **ファイル:** `snippets/product-block-separator.liquid`

**説明:** 商品詳細ページのセクション間に水平線を挿入するブロックコンポーネント。上下の余白、線の高さ、色、透明度をテーマカスタマイザーから調整できる。

**用途:** 商品ページで「説明」「スペック」「レビュー」など複数セクションを視覚的に分離したいとき。ブロック型セクションとして商品ページに追加して使う。

**設置場所:** snippets/product-block-separator.liquid に配置し、sections/main-product.liquid または商品ページ用セクションの blocks ループ内で `{% render 'product-block-separator', block: block %}` で呼び出す。Online Store 2.0 のブロック構造に対応。

**注意点:** block.settings の pt、pb、bg_color、bg_opacity、height はセクション JSON で事前定義が前提となる。line-height やマージンなしに <hr> の高さだけで見栄えが決まるため、デバイス幅によって線が崩れないよう CSS でいくつかのブレークポイントを用意するとよい。テーマカスタマイザーで opacity を 100% 近くに設定すると背景色が濃すぎるので、70～90% の範囲で運用するのが推奨。

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


### 4. 🧩 スニペット クイズ結果データのJSON生成

**カテゴリ:** API連携/JSON出力/JS統合 ／ **難易度:** 上級 ／ **タグ:** `json-output` `quiz` `product-filtering` `javascript-integration` `section-data`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/Quiz/snippets/quiz-data.liquid) （ライセンス: MIT、93行）
- **ファイル:** `Quiz/snippets/quiz-data.liquid`

**説明:** クイズセクションの回答フィルター条件と商品データを JSON 形式で集約し、JavaScript で結果判定・フィルタリングができるようにする。価格・タグ・タイプ・ベンダー・オプションなどで商品を絞り込む。

**用途:** クイズ型のセクションで、ユーザーの回答に応じて該当商品を絞り込んで表示するとき。管理画面で設定した複数の判定条件を JSON データ構造に変換し、フロントエンド JavaScript に渡す。

**設置場所:** snippets/quiz-data.liquid に配置し、quiz-section.liquid 内で `{% render 'quiz-data' %}` で呼び出す。出力された JSON を <script type="application/json"> タグで埋め込むか、JavaScript の fetch で読み込む。

**注意点:** img_url フィルターの image_max_width 変数が定義されていることが前提。section.settings.filter_collection が存在するコレクションハンドルであることを確認し、存在しない場合は空の商品配列が出力されてしまう。price_filter_operator や各フィルター設定値がセクションブロック側の JSON で定義されていないと null 出力になるため、テーマカスタマイザーで条件設定を完成させてから運用する。

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

**説明:** Shopify 管理画面の「メインメニュー」リンクリストをループして、トップレベルのメニュー項目と1階層のサブメニューを描画するスニペット。リンクテキストは自動的に HTML エスケープされる。

**用途:** ストア共通のグローバルナビゲーションをヘッダーに出すときに使用。トップレベル + 1階層のサブメニューに対応している。

**設置場所:** shopify/snippets/layout-menu.liquid に配置し、theme.liquid のヘッダー内で `{% render 'layout-menu', class: 'header-menu', style: 'display: flex;' %}` のように呼び出す。class と style はオプションで、デフォルト値は空になる。

**注意点:** Shopify 管理画面で「メインメニュー」ハンドルのリンクリストが作成されていることが前提となる。サブメニューは1階層のみの対応であり、3階層以上の深いメニューが必要な場合は再帰的な実装に書き換える必要がある。モバイル表示ではドロップダウンメニューが画面外に出ないよう、CSS で position と overflow を調整する。

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


### 6. 🧩 スニペット 404 ページ（ページが見つかりません）

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `error-page` `404` `template` `user-experience`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/404.liquid) （ライセンス: MIT、16行）
- **ファイル:** `templates/404.liquid`

**説明:** 存在しないページにアクセスしたときに表示するエラーページテンプレート。404 エラーメッセージを中央配置で示す。

**用途:** ストア内に存在しないパスや削除されたページへのアクセスを受けたとき、ユーザーに対してページが見つからないことを伝える。

**設置場所:** templates/404.liquid として配置される。ストアへのアクセスで 404 エラーが発生すると Shopify が自動的にこのテンプレートを呼び出す。

**注意点:** このテンプレートは Shopify が自動マッピングするため、ファイル名と配置場所を変更しないこと。ユーザーを正しいページへ導くため、メッセージの下にホームリンクやおすすめ商品へのナビゲーション追加を推奨する。旧 URL から新 URL への恒久的なリダイレクトが必要な場合は、Shopify 管理画面の「ナビゲーション」タブ内のリダイレクト設定機能を使う。

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

**カテゴリ:** UI部品 ／ **難易度:** 初級 ／ **タグ:** `icon` `svg` `success` `checkmark` `ui-component`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/snippets/icon-success.liquid) （ライセンス: MIT、6行）
- **ファイル:** `snippets/icon-success.liquid`

**説明:** 緑の丸背景に白いチェックマークを配置した成功状態を示すアイコン。SVG で描画され、複数の UI パターンで再利用可能。

**用途:** フォーム送信完了、注文確認、エラー解決など、ユーザーアクションの成功を視覚的に伝えるとき。

**設置場所:** snippets/icon-success.liquid に配置し、確認メッセージやサクセススクリーン上で `{% render 'icon-success' %}` で呼び出す。CSS で width/height を指定してサイズ調整する。

**注意点:** SVG の viewBox は 0 0 13 13 で固定されており、外部の CSS で幅・高さを設定しないと描画されない。stroke-width="0.7" はストロークの太さが viewBox スケールに依存するため、表示サイズを大きく変更する場合は stroke-width の値も再調整する。aria-hidden="true" が付いているため、スクリーンリーダーには読み上げられない。

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

**カテゴリ:** ユーティリティ ／ **難易度:** 初級 ／ **タグ:** `random` `utility` `logic` `variable` `date`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/random-number.liquid) （ライセンス: MIT、13行）
- **ファイル:** `random-number.liquid`

**説明:** 現在時刻のナノ秒を利用して、指定した範囲内のランダム数値を生成する。min・max 値を編集することで範囲をカスタマイズできる。

**用途:** A/B テスト、くじ引き企画、動的なコンテンツ表示の確率制御など、ストア内で疑似乱数が必要なときに使う。

**設置場所:** snippets/random-number.liquid に配置し、ランダム数値が必要な section / snippet 内で `{% render 'random-number' %}` で呼び出し、その直後に `{{ random_number }}` で値を参照する。

**注意点:** 現在時刻のナノ秒を利用しているため、同一秒内に複数回呼び出すと同じ値が返される可能性がある。サーバーサイドで生成されるため、ページ読み込みのたびに値が変わり、JavaScript の Math.random() との組み合わせを期待してはいけない。0～9999999 の範囲がデフォルトだが、商品数が少ない場合は max を商品数に合わせて小さくするとよい。

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


### 9. 🧩 スニペット CSS カスタムプロパティの管理

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `css-variable` `font` `theme-setting` `custom-property` `root`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/snippets/css-variables.liquid) （ライセンス: MIT、19行）
- **ファイル:** `snippets/css-variables.liquid`

**説明:** テーマ設定で指定したフォント、色、レイアウト幅などを CSS カスタムプロパティ(:root)として定義し、サイト全体で統一的に使用できるようにする。フォントは複数ウェイト・スタイルを font_modify で組み立て、font_display: swap で高速読み込みに対応。

**用途:** サイト全体で使うデザイントークン（フォントファミリ、背景色、前景色、ボーダー角度など）を一元管理したいとき。CSS や Liquid 内でカスタムプロパティを参照すれば、テーマカスタマイザーの変更が全ページに即座に反映される。

**設置場所:** snippets/css-variables.liquid に配置し、theme.liquid の <head> 内で `{% render 'css-variables' %}` で呼び出す。または theme.liquid の <head> 内に直接 {% style %} ブロックとして埋め込んでもよい。

**注意点:** settings.type_primary_font は管理画面で「フォント」型のテーマ設定が作成されていることが前提。font_modify で複数ウェイト・スタイル組み合わせを出力する際、Google Fonts など Web フォントサービスではサポートされているバリエーションのみが読み込まれるため、管理画面で存在しないウェイト（例: weight 300）を指定しないよう確認する。カスタムプロパティは CSS 変数のため、Liquid フィルタで動的に計算した値（例: サムネイル幅）を代入する場合は {{ 変数 }} を直接埋め込み、数値単位（px、rem など）を明示する。

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


### 10. 🧩 スニペット ギフトカード券面に価格別バリアント画像を表示

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `gift-card` `variant` `image` `product` `linklist`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Use variant image on Gift Card template/capture-image.liquid) （ライセンス: MIT、16行）
- **ファイル:** `Use variant image on Gift Card template/capture-image.liquid`

**説明:** ギフトカードテンプレートで、カード金額に紐付いた商品バリアントの画像を自動取得して券面に表示するスニペット。金額が一致するバリアントから画像を抽出し、見つからない場合はデフォルト画像にフォールバックする。

**用途:** ギフトカード商品で複数の券面デザインを金額（1,000円版、5,000円版など）ごとに出し分けたいとき。バリアント画像を活用して管理画面から柔軟に券面を変更できるようにする。

**設置場所:** gift-card.liquid テンプレートの先頭に capture-image.liquid を貼り付けるか、`{% render 'capture-image' %}` で呼び出す。その後、画像表示部分で `src="{{ customImage }}"` に置き換える。

**注意点:** Shopify 管理画面の「ギフトカード」セクションで商品が指定されており、かつそれが「admin-gift-card」というハンドルのリンクリストの第1リンクとして登録されていることが前提。バリアント画像が未設定の場合はデフォルト画像（'gift-card/card.jpg'）で表示されるため、金額ごとのバリアント画像を事前に登録しておく必要がある。img_url フィルタの '949x' パラメータはテーマ側の券面サイズに合わせて調整する。

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

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `logo` `navbar` `header` `image` `responsive`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/navbar-logo.liquid) （ライセンス: MIT、18行）
- **ファイル:** `snippets/navbar-logo.liquid`

**説明:** ストアロゴをナビゲーションバーのトップに表示するコンポーネント。ロゴ画像が設定されていればそれを表示し、未設定ならストア名をテキストで表示する。

**用途:** ヘッダーのナビゲーションバーにブランドロゴを配置し、クリックでトップページに遷移するリンクとして機能させたいとき。

**設置場所:** snippets/navbar-logo.liquid に配置し、ナビゲーションバーコンポーネント内で `{% render 'navbar-logo' %}` で呼び出す。block.settings でテーマカスタマイザーから logo と logo_height を受け取る。

**注意点:** block.settings.logo_height が未設定またはゼロの場合、幅の計算で不正な値が発生するため、テーマカスタマイザーで最小値（例: 30px）を設定する。高解像度ディスプレイ対応に logo_height を 2 倍で画像取得しているため、アスペクト比計算が正確に動作することが前提。ロゴの URL が CDN 経由で返されるため、キャッシュクリア後に反映タイムラグが生じる可能性がある。

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


### 12. 🧩 スニペット FAQ アコーディオン

**カテゴリ:** UI部品 ／ **難易度:** 中級 ／ **タグ:** `accordion` `faq` `json-ld` `schema-org` `rich-result`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/FAQ/sections/faq.liquid) （ライセンス: MIT、352行）
- **ファイル:** `FAQ/sections/faq.liquid`

**説明:** 質問と回答をアコーディオン形式で表示するセクション。ブロックごとに質問タイトルと本文を追加でき、クリックで開閉する。Google の FAQPage 構造化データにも対応。

**用途:** ストアの FAQ ページや商品ページの下部に、よくある質問をアコーディオン形式で配置したいとき。検索結果でのリッチリザルト表示も狙える。

**設置場所:** sections/faq.liquid に配置し、テーマカスタマイザーから「FAQ」セクションを追加して各質問を入力する。JavaScript ファイル faq.js も同じ assets/ フォルダに用意する必要がある。

**注意点:** JavaScript の faq.js がない場合、アコーディオンが動作せず常時開きの状態になる。ブロック内の「タイトル」「内容」の両方が空でないことが表示の前提なため、どちらか一方を削除すると該当ブロックは非表示になる。FAQPage スキーマを有効にすると、HTML タグが本文から strip_html で削除されるため、検索結果に表示される内容がテーマ上の見た目と異なる場合がある。

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


### 13. 🧩 スニペット フッター

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `footer` `linklists` `navigation` `section` `layout`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/footer.liquid) （ライセンス: MIT、25行）
- **ファイル:** `shopify/sections/footer.liquid`

**説明:** ストア共通のフッター領域を表示するセクション。管理画面で設定したフッターメニュー（リンクリスト）をループして出力し、下部にコピーライト表記を追加する。

**用途:** theme.liquid の </body> 直前、またはページテンプレートの下部にフッター領域として配置。サイト全体で統一されたフッターナビゲーションを表示するとき。

**設置場所:** shopify/sections/footer.liquid に配置し、theme.liquid または各ページテンプレートで {% section 'footer' %} として呼び出す。

**注意点:** Shopify 管理画面で「フッター」ハンドルのリンクリストが作成されていることが前提。リンク数が多い場合はカラムレイアウト CSS を追加して複数列表示に対応させる。モバイル表示では <div> の横並びが画面幅で崩れないよう flex または grid で調整する。

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


### 14. 🧩 スニペット 検索結果ページのカテゴリ分類表示

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `search` `pagination` `collection` `filter` `product-grid`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/search.liquid) （ライセンス: MIT、17行）
- **ファイル:** `templates/search.liquid`

**説明:** 検索結果の商品を一覧表示し、商品が属する最も詳細なカテゴリ（自動コレクションの末端）を特定して、カテゴリページへのリンクを生成する。featured_image とタイトルで商品カードを表現。

**用途:** 検索ページで商品一覧を表示するとき、単純なグリッド表示ではなく、商品の属するカテゴリ階層を活用した詳細カテゴリページへ導線を作りたい場合。

**設置場所:** templates/search.liquid に貼り付ける。商品のコレクション構造が「hardware-building-consumables > hardware-building-consumables--solder-flux」のような親子階層を持つことが前提。カテゴリページのパス（/pages/category/）とハンドル削除ルール（remove_first: 'hardware-'）を自店舗の構造に合わせて調整する。

**注意点:** このコードは Shopify の自動コレクション機能を前提とするため、カスタムコレクションのみ運用している場合は動作しない。複数商品が同じコレクションに属する場合、もっとも長いハンドルのコレクションを「最も詳細」と見なすが、階層の深さと実際のビジネス分類が一致しない場合は修正が必要。ページネーション（24件ごと）は表示パフォーマンスに応じて調整する。

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


### 15. 🧩 スニペット ギフトカードの表示ページ

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `gift-card` `qr-code` `template` `email` `responsive`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/templates/gift_card.liquid) （ライセンス: MIT、204行）
- **ファイル:** `templates/gift_card.liquid`

**説明:** ギフトカードの金額、QRコード、カード番号をメールリンク経由で表示するテンプレート。有効期限切れの判定、残高表示、コードのコピー機能に対応する。

**用途:** ギフトカード購入後、顧客がメールで受け取ったリンクからアクセスして、カード番号を確認・コピーし、QRコードをスキャンして利用するページ。

**設置場所:** templates/gift_card.liquid に配置する。Shopify 管理画面でギフトカード機能を有効にすると、自動的にこのテンプレートが呼び出される。CSS は assets/template-giftcard.css として別ファイルで用意する。

**注意点:** Storefront API ではギフトカードオブジェクトが未サポートのため、このテンプレートは REST API/管理画面経由でのアクセスに限定される。QRコード生成には Shopify が提供する vendor/qrcode.js を使用しており、このアセットが削除されるとコード表示が動作しなくなる。gift_card.enabled または gift_card.expired の判定ロジックはテーマ側で実装するため、有効期限の管理は Shopify 管理画面で正確に設定しておく。

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


### 16. 🧩 スニペット 検索機能のWebSite構造化データ

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `json-ld` `schema-org` `search` `seo` `rich-result`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/json-ld-search.liquid) （ライセンス: MIT、17行）
- **ファイル:** `json-ld-search.liquid`

**説明:** ストア上の検索機能を schema.org の WebSite 型で構造化データ化し、Google 検索結果に検索ボックスを表示させる JSON-LD。

**用途:** Google の「サイトリンク検索ボックス」表示を狙うとき。検索結果ページからユーザーが直接検索できるようになり、クリック数の増加につながる。

**設置場所:** snippets/json-ld-search.liquid に配置し、theme.liquid の `</head>` 直前で `{% render 'json-ld-search' %}` で呼び出す。または templates/search.liquid 内に埋め込みでもよい。

**注意点:** Google にサイトリンク検索ボックスが表示されるには、構造化データが正しい以上に、ストアが十分に認知度が高く、十分なトラフィックがないと表示されない場合がある。shop.url が HTTPS で正しくリダイレクトされていることが前提。Google Search Console の「URL 検査」ツールで構造化データのエラーが出ていないか確認し、本番リリース後も検索パフォーマンスレポートで表示状況を監視する。

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

**カテゴリ:** テーマ基盤 ／ **難易度:** 初級 ／ **タグ:** `layout` `password-protect` `critical-css` `meta-tags` `theme-structure`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/layout/password.liquid) （ライセンス: MIT、20行）
- **ファイル:** `layout/password.liquid`

**説明:** ストアがパスワード保護中に表示されるページのレイアウトテンプレート。CSS 変数、クリティカル CSS、メタタグを読み込み、最小限の HTML 構造でページを構築する。

**用途:** ストア立ち上げ前やメンテナンス期間中に、訪問者に対してパスワード入力画面を表示するときに使用する。

**設置場所:** layout/password.liquid として Shopify テーマに配置される固定ファイル。管理画面の「オンラインストア > テーマ > アクション > 現在のテーマを編集」からレイアウトツリーで自動的に読み込まれる。

**注意点:** このテンプレートは Shopify が自動認識する予約済みレイアウトファイルのため、手動で layout/ に配置しても theme.json で明示的に指定する必要がある場合がある。css-variables と meta-tags スニペットが存在することが前提なので、削除するとスタイルやメタタグが失われる。パスワード保護時の入力フォームは別途 sections/ に実装し、`content_for_layout` の内側に組み込む。

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


### 18. 🧩 スニペット 検索結果ページの検索タイプ判定

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `search` `url-parameter` `conditional` `type-detection` `query-string`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Detect search type used in searches/show-search-type.liquid) （ライセンス: MIT、17行）
- **ファイル:** `Detect search type used in searches/show-search-type.liquid`

**説明:** 検索結果ページの URL から検索タイプ（product / page / article）を抽出し、どのコンテンツ種別で検索されたかを判定する。タイプ値を取得して条件分岐に活用できる。

**用途:** 検索結果ページで「商品のみ検索」「記事のみ検索」など、検索タイプごとに異なるレイアウトやメッセージを出し分けたいとき。

**設置場所:** templates/search.liquid または section / snippet 内で、`{% render 'show-search-type' %}` として呼び出し、取得した searchType 変数で後続の表示内容を切り替える。

**注意点:** 検索パラメータ `type=` が URL に含まれていることが前提となる。Shopify のデフォルト検索フォームでは type パラメータが付かない場合があるため、フォーム側で `<input name="type" value="product">` のように明示的に指定する必要がある。URL に複数の type パラメータが含まれる場合は最初の値のみを抽出するため、クエリ文字列の構成を確認してから使用する。

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


### 19. 🧩 スニペット 支払い方法アイコン

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `payment-method` `footer` `accessibility` `icon` `bootstrap`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/payment-icons.liquid) （ライセンス: MIT、18行）
- **ファイル:** `snippets/payment-icons.liquid`

**説明:** ストアで有効な支払い方法のアイコンを一覧表示する。各アイコンにはツールチップで支払い方法名が表示され、セキュリティメッセージを下部に追加する。

**用途:** フッターやチェックアウトページ上部で、利用可能な決済手段（クレジットカード、PayPal など）を視覚的に表示したいとき。

**設置場所:** snippets/payment-icons.liquid に配置し、footer.liquid またはチェックアウトセクション内で `{% render 'payment-icons' %}` で呼び出す。

**注意点:** shop.enabled_payment_types は Shopify 管理画面の支払い設定から自動取得されるため、事前に有効な支払い方法を設定しておく必要がある。ツールチップ表示には Bootstrap（data-bs-toggle など）が依存するため、テーマに Bootstrap が読み込まれていることを確認する。payment_type_svg_tag フィルターは Shopify 公式フィルターで、カスタムテーマの場合は対応状況を確認する。

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


### 20. 🧩 スニペット 画像上のツールチップ表示

**カテゴリ:** UI部品 ／ **難易度:** 中級 ／ **タグ:** `image-annotation` `hotspot` `tooltip` `interactive` `responsive` `accessibility`

- **出典:** [`mirceapiturca/Sections`](https://raw.githubusercontent.com/mirceapiturca/Sections/master/Tooltips/sections/tooltips.liquid) （ライセンス: MIT、452行）
- **ファイル:** `Tooltips/sections/tooltips.liquid`

**説明:** 画像にホットスポット（ポイント）を配置し、クリックで説明文をポップアップ表示するセクション。レスポンシブ対応で、モバイルではリスト、デスクトップではオーバーレイ表示に切り替わる。

**用途:** 製品画像の各部位・機能を説明したいとき、チュートリアル画像で手順を提示したいとき。インタラクティブな説明を画像上に実装できる。

**設置場所:** sections/tooltips.liquid として配置する。テーマ側で section スキーマ（画像、背景色、フォーカス色、レスポンシブ breakpoint の設定）と block スキーマ（各ツールチップの位置、タイトル、説明）を定義する必要があり、管理画面のカスタマイズ画面から設定可能にする。

**注意点:** セクション全体と各ブロックのスキーマ定義（JSON）がコード末尾に含まれていないため、settings と block.settings を参照している部分をスキーマに追加する必要がある。画像のアスペクト比が異なるとホットスポット位置がずれるため、`image_aspect_ratio` をスキーマで固定値に設定するか、管理画面で明示的に入力させること。JavaScript がない場合（noscript）は小数点リスト表示に fallback するが、aria-expanded 属性による開閉状態の管理はクライアント側スクリプトで実装する。

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


### 21. 🧩 スニペット ストアのグローバルヘッダー

**カテゴリ:** ヘッダー/フッター/ナビゲーション ／ **難易度:** 初級 ／ **タグ:** `header` `navigation` `customer-account` `menu` `cart`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/header.liquid) （ライセンス: MIT、37行）
- **ファイル:** `shopify/sections/header.liquid`

**説明:** ロゴ、メインメニュー、顧客アカウント機能、カートへのリンクを配置するヘッダーセクション。顧客ログイン状態を判定して表示内容を切り替える。

**用途:** すべてのページ上部に共通で表示されるグローバルナビゲーション。顧客アカウントの有効化状態に応じて、ログイン・登録・マイアカウントへのリンクを出し分ける。

**設置場所:** shopify/sections/header.liquid に配置し、theme.liquid の layout セクションで `{% section 'header' %}` として呼び出す。logo テキストは store ロゴ画像パスに、'layout-menu' スニペットパスを確認して相対パスを調整する。

**注意点:** shop.customer_accounts_enabled が false の場合、顧客アカウント周りのリンクすべてが非表示になるため、Shopify 管理画面で「顧客アカウント」機能が有効化されていることが前提。routes.root_url や routes.account_url は Shopify が自動提供するため、ハードコード不要。モバイル表示ではメニューが画面外に出ないよう親コンテナの overflow-x を制御し、レスポンシブ対応の CSS を別途用意する。

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

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `collection` `pagination` `product-list` `template` `vendor`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/templates/collection.liquid) （ライセンス: MIT、41行）
- **ファイル:** `templates/collection.liquid`

**説明:** コレクション内の商品を一覧表示し、ページネーション対応で20件ずつ分割表示するテンプレート。商品画像、タイトル、説明文、価格をテーブル形式でレイアウトする。

**用途:** ストアのカテゴリ・コレクションページで、商品の概要を一覧で見せたいとき。ページネーション機能で大量商品に対応する。

**設置場所:** templates/collection.liquid に配置するだけで、Shopify が自動的にコレクションページ表示時に読み込む。管理画面でコレクションが作成されていることが前提。

**注意点:** ページネーションは collection.liquid テンプレート内の `{% paginate %}` タグでのみ動作するため、他のテンプレートへの移設は避ける。product.description は HTML タグが含まれるため `strip_html` で除去されるが、レスポンシブ対応がないので画面幅に応じて CSS で table を flex や grid にリセットしたほうがよい。product.featured_image が未設定の場合は 50×50px の空白画像が表示されるため、ダミー画像 URL の指定を検討する。

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


### 23. 🧩 スニペット 顧客ログイン・パスワードリセット

**カテゴリ:** 顧客アカウント ／ **難易度:** 中級 ／ **タグ:** `customer-login` `account` `form` `password-reset` `error-handling`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/sections/main-login.liquid) （ライセンス: MIT、238行）
- **ファイル:** `sections/main-login.liquid`

**説明:** 顧客がメールアドレスとパスワードでログインするフォーム、パスワードをリセットするフォーム、ゲストチェックアウト入口をまとめたセクション。エラーメッセージと成功メッセージの出し分けに対応する。

**用途:** accounts/login テンプレートページで、顧客がアカウントにサインインしたり、パスワードを忘れたときにリセットリンクを受け取ったりするとき。

**設置場所:** sections/main-login.liquid に配置し、templates/customers/login.liquid または accounts/login.liquid テンプレートで `{% section 'main-login' %}` で呼び出す。

**注意点:** `settings.multipass_login` が true の場合はセクション全体が表示されないため、Shopify 管理画面の「シングルサインオン」設定と整合させておく必要がある。`settings.storefront_hostname` がロゴリンク先のドメインになるため、カスタムドメイン環境では shop.permanent_domain や手動設定で置き換える。パスワードフォームは `form.password_needed` の条件で表示/非表示が切り替わるため、Liquid の form オブジェクトの状態に依存する。

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


### 24. 🧩 スニペット Organization構造化データ

**カテゴリ:** SEO/構造化データ ／ **難易度:** 初級 ／ **タグ:** `json-ld` `schema-org` `organization` `seo` `branding`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/json-ld-organization.liquid) （ライセンス: MIT、22行）
- **ファイル:** `json-ld-organization.liquid`

**説明:** ストア全体の組織情報を schema.org の Organization 型で JSON-LD として埋め込む。ロゴ URL とソーシャルメディアリンクを Google に伝え、検索結果でのブランド表示強化に対応させる。

**用途:** ストアのロゴ・企業情報・SNS アカウントを Google や検索エンジンに正式に伝えたいとき。Knowledge Panel 表示や Knowledge Graph との連携を狙う場合に活用する。

**設置場所:** snippets/json-ld-organization.liquid に配置し、theme.liquid の </head> 直前で `{% render 'json-ld-organization' %}` で呼び出す。または layout/theme.liquid 内に直接埋め込んでもよい。

**注意点:** logo パスの 'logo.png' はストアの実在するファイル名に置き換える必要があり、Assets 管理画面で確認してから指定する。sameAs 配列の SNS URL は Shopify 管理画面の「テーマ設定」の該当フィールドに入力済みが前提。空白や不正な URL が残るとバリデーションエラーになるため、未使用の SNS は配列から削除するか null チェックを追加する。

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

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `404` `error-page` `template` `routing` `translation`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/404.liquid) （ライセンス: MIT、24行）
- **ファイル:** `sections/404.liquid`

**説明:** 顧客が存在しないページにアクセスしたときに表示するセクション。ページが見つからないことを伝え、全商品ページへのリンクを提供する。

**用途:** 404 テンプレートで無効な URL にアクセスしたときのエラーページ表示に使用。

**設置場所:** sections/404.liquid に配置し、templates/404.liquid で `{% section '404' %}` として呼び出す。

**注意点:** 翻訳文字列（『404.title』『404.not_found』『404.back_to_shopping』）が theme の JSON 翻訳ファイル（locales/ja.json など）に定義されていることが前提。未定義だとキーがそのまま表示されるため、翻訳ファイルで日本語テキストを設定してからこのセクションを公開する。『routes.all_products_collection_url』が生成する URL が正しいコレクション（全商品ページ）を指していることを本番環境で確認する。

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

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `pagination` `collection` `cart-attribute` `dynamic` `products-per-page`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Dynamic pagination without alternate templates/dynamic-pagination.liquid) （ライセンス: MIT、20行）
- **ファイル:** `Dynamic pagination without alternate templates/dynamic-pagination.liquid`

**説明:** コレクションの商品一覧ページネーションを、カート属性で件数を動的に切り替えるスニペット。デフォルトは 40 件だが、顧客が「全部見る」「20 件表示」など選択すると、その設定をカート属性に保存して反映させる。

**用途:** 商品数の多いコレクションページで、ユーザーが「1ページあたりの表示件数」を選べるようにしたいときに使う。別のテンプレートを用意せず、1つのテンプレートで動的に対応できる。

**設置場所:** templates/collection.liquid 内の `{% paginate collection.products by 40 %}` を置き換えるか、別スニペット化して `{% render 'dynamic-pagination' %}` で呼び出す。呼び出し元で `...` の部分に商品カード等の内容を記述する。

**注意点:** cart.attributes は顧客が保有するカート単位の属性なので、ページ移動やブラウザをまたぐと値が消える場合がある。デバイスごと・セッションごとに値を保持したい場合は、localStorage または URL クエリパラメータ（?per_page=20）に切り替えるとよい。paginationAmount が 0 以下にならないよう `| abs` で絶対値化しているが、テーマ設定で選択肢制限すればより安全。

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


### 27. 🧩 スニペット 商品カスタムバッジ（メタフィールド連動）

**カテゴリ:** メタフィールド/メタオブジェクト ／ **難易度:** 中級 ／ **タグ:** `metafield` `product` `badge` `dynamic-content` `theme-settings`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-custom-badge.liquid) （ライセンス: MIT、19行）
- **ファイル:** `snippets/product-custom-badge.liquid`

**説明:** 商品のメタフィールドからテキストと色情報を読み込み、動的にカスタムバッジを商品カードに表示するスニペット。パイプ区切りでテキストと背景色をセットできる。

**用途:** 商品ごとに異なるバッジ（「限定」「人気」「再入荷」など）を管理画面のメタフィールドから簡単に出し分けたいとき。

**設置場所:** snippets/product-custom-badge.liquid に配置し、product-card.liquid や main-product.liquid の表示したい位置で `{% render 'product-custom-badge', product: product %}` で呼び出す。テーマ設定でメタフィールドキーと背景色クラスを指定しておく。

**注意点:** メタフィールド名は「namespace.key」形式で settings に保存する必要があり、商品ごとにメタフィールド値を入力していることが前提。カラーコード（#RRGGBB または rgb()）が正しい形式でないと style 属性が反映されないため、管理画面で色ピッカーを使わせるか入力値を検証する。color_darken フィルタで 15 段階暗くした縁取り色を生成するが、明度不足の色では暗さが足りず見えなくなる可能性があるので、濃い背景色を選ぶとよい。

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


### 28. 🧩 スニペット テーマレイアウト基盤

**カテゴリ:** テーマ基盤 ／ **難易度:** 中級 ／ **タグ:** `layout` `theme` `meta-tag` `asset` `webpack` `localization`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/layout/theme.liquid) （ライセンス: MIT、42行）
- **ファイル:** `shopify/layout/theme.liquid`

**説明:** すべてのページで読み込まれるテーマの基本レイアウト。メタタグ、favicon、CSS/JS アセットの読み込みを一元管理し、ヘッダー・フッター・メインコンテンツを配置する。

**用途:** Online Store 2.0 テーマの骨組みとして機能。localization、SEO タグ、webpack バンドルの読み込みを含む共通レイアウトが必要なとき。

**設置場所:** shopify/layout/theme.liquid に配置。全ページから自動的に読み込まれる。CSS/JS バンドル名を自店舗に合わせて変更し、favicon 設定は Shopify 管理画面の「テーマ設定」で実施する。

**注意点:** request.locale.iso_code はストアの言語設定に依存するため、多言語対応していない場合は固定値（例: 'ja'）に変更する。content_for_header は Shopify プラグインやピクセルを自動注入するため削除禁止。captcha ページでは id="app" が付かないようにしているため、JavaScript で要素選択する際は条件分岐を用意する必要がある。webpack バンドル(bundle.css/bundle.js)が存在しないと 404 エラーになるため、ビルドプロセスで確実に生成されているか確認する。

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


### 29. 🧩 スニペット カテゴリグリッドの複数列表示

**カテゴリ:** コレクション/検索 ／ **難易度:** 中級 ／ **タグ:** `metaobject` `collection` `grid` `card` `category` `preload`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/sections/category-multicolumn.liquid) （ライセンス: MIT、112行）
- **ファイル:** `sections/category-multicolumn.liquid`

**説明:** 複数のカテゴリをグリッドレイアウトでカード状に表示するセクション。各カテゴリは画像、タイトル、説明文とリンクを持ち、ホバー時にカード全体が反応するUI。

**用途:** 商品カテゴリの一覧ページや、コレクション詳細ページでサブカテゴリを視覚的に整理して表示したいとき。メタオブジェクトで階層構造を管理し、プリロード機能で次の階層イメージの読み込みを最適化する。

**設置場所:** sections/category-multicolumn.liquid として配置し、管理画面の「セクション追加」からセレクトして使用。ブロック内の各カテゴリはメタオブジェクトリストで設定し、リンク先と説明テキストを個別に指定する。

**注意点:** プリロード機能は `next_children` メタオブジェクトが正しく参照されていることが前提。メタオブジェクト型が `category_metaobject` として定義されていないと空になるため、管理画面でメタオブジェクト定義を先に作成する必要がある。タイトルが「 > 」で区切られている場合は `split: ' > ' | last` で最後の要素のみ抽出されるため、データ構造と表示形式が一致していることを確認する。グリッドの最小幅（minmax の 25rem）はコンテンツ量に応じて CSS を調整する。

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


### 30. 🧩 スニペット テーマ基盤のレイアウト・CSS変数

**カテゴリ:** テーマ基盤 ／ **難易度:** 上級 ／ **タグ:** `theme` `layout` `css-variables` `typography` `color-palette` `responsive-design` `settings`

- **出典:** [`instantcommerce/shopify-headless-theme`](https://raw.githubusercontent.com/instantcommerce/shopify-headless-theme/master/layout/theme.liquid) （ライセンス: MIT、242行）
- **ファイル:** `layout/theme.liquid`

**説明:** すべてのページの HTML 骨組みと CSS 変数を定義するレイアウトテンプレート。管理画面の設定値（フォント・色・ボタンスタイル等）を CSS custom properties に変換し、各ページやセクションで統一的に使用可能にする。

**用途:** ストアのフォント・カラーパレット・ボタン・入力欄の装飾（丸さ、影、枠線など）を一元管理したいとき。テーマカスタマイザーで設定した値がすべてのページに反映される仕組みを構築する。

**設置場所:** layout/theme.liquid がデフォルトレイアウトファイルとして機能するため、通常は変更不要。カスタマイズする場合は、CSS 変数の定義部分（`:root { ... }` ブロック）を編集して、フォント・色・間隔の計算式を自店舗仕様に調整する。

**注意点:** settings. で参照する設定キーはテーマの config.json に定義されていることが前提。font_modify フィルターはウェイトを太字で +300 上限 1000 に制限しているため、フォントが 700 以上の場合は最大値に張付くことがある。色は RGB チャンネル（red、green、blue）で分解されているため、CSS の `rgb()` 関数や透明度付き `rgba()` で活用する際は 0〜255 の数値であることを確認してから使う。page_width が 1600 のときのみ margin-left/right が 2rem 自動付与される設計なので、他の幅に変更する場合は margin 計算式も併せて修正する。

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


### 31. 🧩 スニペット ランダムに商品を選択

**カテゴリ:** ユーティリティ ／ **難易度:** 中級 ／ **タグ:** `product` `random` `collection` `utility` `timestamp`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/random-product.liquid) （ライセンス: MIT、32行）
- **ファイル:** `random-product.liquid`

**説明:** ストア内のすべての商品、または指定したコレクション内からランダムに1つの商品を選出する。タイムスタンプをハッシュ化してランダム性を持たせ、選んだ商品オブジェクトを返す。

**用途:** トップページの「ピックアップ商品」枠や、メール配信時のおすすめ商品、サイドバーの関連商品表示など、動的にランダムな商品を出したいときに使う。

**設置場所:** snippets/random-product.liquid に配置し、商品を表示したいテンプレートやセクション内で `{% render 'random-product' %}` または `{% render 'random-product' with specific_collection: 'コレクションハンドル' %}` で呼び出す。呼び出し後 `{{ random_product }}` で該当商品にアクセスできる。

**注意点:** ランダム生成は `date: "%N"` のナノ秒タイムスタンプを使うため、ページ読み込みのたびに異なる商品が表示される。collections['all'].products はストアの全商品を対象にするが、数千件の大規模ストアではループ処理の負荷が増すため、対象コレクションを明示的に指定する運用が推奨される。商品がない空コレクションを指定するとランダム選出に失敗するので、事前にコレクションに商品が入っているか確認する。

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

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `blog` `article` `pagination` `liquid` `template`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/blog.liquid) （ライセンス: MIT、36行）
- **ファイル:** `sections/blog.liquid`

**説明:** ブログページで全記事をリスト表示するセクション。記事画像、タイトル、公開日、著者、抜粋を並べ、ページネーション対応。

**用途:** Shopify のブログテンプレートで、複数の記事を一覧化して表示するときに必須。記事ごとのメタデータと画像を整理して出す。

**設置場所:** sections/blog.liquid に配置し、templates/blog.liquid 内で `{% section 'blog' %}` で呼び出す。ブログテンプレートの主コンテンツセクションとして機能。

**注意点:** 記事に画像が未設定でも表示が崩れないよう `{% if article.image %}` で条件分岐されている。ページネーションは 1 ページ 5 件で固定なので、件数を変更する場合は `by 5` の数値を置き換える。日本語化する際は `'blog.article_metadata_html'` の翻訳キーが theme 言語ファイル内に存在することを確認し、日付・著者の表示順序が英語に依存していないか確認する。

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


### 33. 🧩 スニペット SKU検索のJSON API

**カテゴリ:** API連携/JSON出力/JS統合 ／ **難易度:** 中級 ／ **タグ:** `search` `sku` `json` `api` `ajax`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Search by SKU/search.sku.liquid) （ライセンス: MIT、23行）
- **ファイル:** `Search by SKU/search.sku.liquid`

**説明:** 検索フォームに入力された SKU（商品コード）で商品を検索し、マッチした商品を JSON 形式で返すエンドポイント。JavaScript や外部システムから検索結果を取得するのに使う。

**用途:** ストアの検索機能で SKU 検索に対応させるとき、または Hydrogen・カスタムフロントエンドから AJAX で SKU 検索結果を取得したいとき。

**設置場所:** templates/search.sku.liquid として新規ファイルを作成し、管理画面で検索ページのテンプレート設定を `search.sku` に指定する。JavaScript 側から `/search?q=ABC123&type=product` のような URL にリクエストを送ると JSON が返される。

**注意点:** search.sku テンプレートが有効になるには、管理画面で検索ページのテンプレート設定が必ず `search.sku` に切り替えられていることが前提。Shopify の検索インデックスが SKU で自動に対応するわけではないため、商品の検索ワードにあらかじめ SKU を含める設定が検索カスタマイズで必要。レスポンスの JSON は配列内の商品オブジェクト末尾に必ずカンマをつけないよう forloop.last で制御するため、この部分を削除すると JSON パースが失敗する。

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

**カテゴリ:** 商品表示 ／ **難易度:** 初級 ／ **タグ:** `product` `section` `richtext` `block` `customization`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/product-block-richtext.liquid) （ライセンス: MIT、22行）
- **ファイル:** `snippets/product-block-richtext.liquid`

**説明:** 商品詳細ページに表示するカスタムテキストブロック。タイトルと説明文を表示でき、商品の説明文を追加で載せることもできる。

**用途:** 商品ページ内で、商品説明とは別のセクション（使用方法・注意点・キャンペーンテキストなど）を挿入したいとき。

**設置場所:** snippets/product-block-richtext.liquid に配置し、sections/main-product.liquid または product.liquid 内で `{% render 'product-block-richtext', block: block, product: product %}` で呼び出す。

**注意点:** block.settings.pt と block.settings.pb はパディング値を数値で指定し、自動的に Tailwind 形式（pt-4、pb-8 など）のクラス名に変換される。title_font_size と description_font_size は CSS クラス名を settings スキーマで定義しておく必要がある。product_description が true のとき、商品の本体説明文が自動で下部に追加されるため、重複を避けたい場合は無効にする。

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


### 35. 🧩 スニペット Vue コンポーネントの統合例

**カテゴリ:** API連携/JSON出力/JS統合 ／ **難易度:** 上級 ／ **タグ:** `vue` `component` `vuex` `slot` `directive` `frontend-framework`

- **出典:** [`uicrooks/shopify-theme-lab`](https://raw.githubusercontent.com/uicrooks/shopify-theme-lab/main/shopify/sections/vue-examples.liquid) （ライセンス: MIT、162行）
- **ファイル:** `shopify/sections/vue-examples.liquid`

**説明:** Shopify Theme Lab を使った Vue コンポーネント、スロット、プロップス、グローバルミックス、ディレクティブ、Vuex ストアの統合デモセクション。テーマに Vue.js 環境を組み込むときの実装パターンを示す。

**用途:** Vue.js ベースのテーマ開発環境を構築し、コンポーネント駆動の Shopify テーマ開発を進めるときに参考となる。ローカル開発から本番構築まで再利用できるコンポーネント設計の具体例。

**設置場所:** shopify/sections/vue-examples.liquid に配置し、Theme Customizer で「Vue examples」セクションをページに追加して表示確認する。src/vue/components/ 以下の実際の Vue コンポーネント（render-my-component、renderless-my-component）、src/vue/mixins/global.mixin.js、src/vue/directives/global.directive.js、src/vue/store/my-module.js が同時に存在することが前提。

**注意点:** Vue コンポーネント名はファイル名 / ディレクトリ構造に従い、スロットやプロップスの型定義は各コンポーネントファイル側で明示する。Vuex ストアの "my-module" は実装に合わせ、state / dispatch メソッドを正確にマッピングする。NODE_ENV の表示には {% raw %} タグでテンプレート処理を回避し、Vue が値を受け取るようにする。開発環境で theme build / serve 実行中のみ動作するため、本番デプロイ前に Vue バンドルの出力パスを確認する。

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

**カテゴリ:** ページテンプレート ／ **難易度:** 中級 ／ **タグ:** `homepage` `category` `metaobject` `grid` `section`

- **出典:** [`Shopify/mcliquid-theme`](https://raw.githubusercontent.com/Shopify/mcliquid-theme/main/sections/homepage.liquid) （ライセンス: MIT、119行）
- **ファイル:** `sections/homepage.liquid`

**説明:** ホームページで階層化されたカテゴリをグリッド状に表示するセクション。メタオブジェクトで定義したサブカテゴリを画像と名前付きで一覧表示し、各項目にリンク機能を持たせる。

**用途:** ストアのホームページで、複数のカテゴリグループをビジュアル的に整理して表示したいとき。特に1段階下のサブカテゴリ一覧を画像付きで出し分けたい場合に活用する。

**設置場所:** sections/homepage.liquid に配置し、Online Store 2.0 のセクション選択UI からブロックを追加してカテゴリを設定する。管理画面のテーマカスタマイザーでメタオブジェクト型の「category_metaobject」をあらかじめ作成しておく必要がある。

**注意点:** メタオブジェクトのカテゴリ名が「親カテゴリ > 子カテゴリ」のように半角スペース付き「 > 」で区切られていることが前提。区切り文字が異なると child_title_parts[1] の抽出に失敗するため、メタオブジェクト側のデータ形式を統一しておく。子カテゴリの画像が未登録だと破損画像が表示されるので、管理画面で全カテゴリに画像を設定してからリリースする。

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


### 37. 🧩 スニペット TwitterカードのメタタグOGP

**カテゴリ:** SEO/構造化データ ／ **難易度:** 中級 ／ **タグ:** `twitter` `meta-tag` `ogp` `social-sharing` `product` `article`

- **出典:** [`pgrimaud/shopify-snippets`](https://raw.githubusercontent.com/pgrimaud/shopify-snippets/main/metadata-twitter.liquid) （ライセンス: MIT、37行）
- **ファイル:** `metadata-twitter.liquid`

**説明:** 商品ページ・ブログ記事ページ・その他ページで、Twitter シェア時に表示されるカードを制御するメタタグを出力する。商品ページでは価格・在庫・ブランド、記事ページでは記事タイトル・抄録・画像を自動的に埋め込む。

**用途:** ストア URL が Twitter でシェアされたとき、タイトル・説明文・画像がリッチカード形式で表示されるようにしたい。商品ページと記事ページで情報源を切り替えて、それぞれ最適な情報を出す。

**設置場所:** theme.liquid の <head> 内、既存の OGP タグ（og:title、og:image など）の直後に貼り付ける。ファイルを snippets/metadata-twitter.liquid として分割し、`{% render 'metadata-twitter' %}` で呼び出すと管理しやすい。

**注意点:** 6行目の `@twitter_handler` は自店舗の Twitter アカウントに置き換える。ロゴ画像（logo-square.png）は正方形である必要があり、Shopify 管理画面の「テーマアセット」に事前にアップロードしておく。記事ページの画像抽出は記事本文内の最初の img タグを対象にするため、記事の HTML 構造が変わると画像が検出されなくなることがある。その場合は featured_image メタフィールドを使うように修正するとよい。

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

**カテゴリ:** ページテンプレート ／ **難易度:** 初級 ／ **タグ:** `password-protection` `form` `template` `storefront` `auth`

- **出典:** [`Shopify/skeleton-theme`](https://raw.githubusercontent.com/Shopify/skeleton-theme/main/sections/password.liquid) （ライセンス: MIT、36行）
- **ファイル:** `sections/password.liquid`

**説明:** ストアにパスワード保護を設定したときに表示されるランディングページ。パスワード入力フォームを備え、管理画面で設定したメッセージを合わせて表示する。

**用途:** ストア公開前やメンテナンス期間中に、パスワード認証を通したユーザーのみアクセスを許可したいとき。

**設置場所:** sections/password.liquid に配置する。テーマの password.liquid テンプレートから自動的に呼び出されるため、手動で設定は不要。

**注意点:** Shopify 管理画面の「オンラインストア > 設定 > パスワード保護」でパスワードと任意のメッセージを設定していることが前提。form は `storefront_password` タイプの公式フォームなため、カスタムバリデーションは不可。パスワード入力後の遷移先やエラー時の再試行ロジックは Shopify 側で自動制御される。

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


### 39. 🧩 スニペット コレクション商品をメタフィールド値で並び替え

**カテゴリ:** コレクション/検索 ／ **難易度:** 上級 ／ **タグ:** `collection` `metafield` `sort` `custom-order` `product`

- **出典:** [`freakdesign/shopify-code-snippets`](https://raw.githubusercontent.com/freakdesign/shopify-code-snippets/master/Sort Shopify collection by metafield/sort-shopify-collection-products-by-metafield-value-commentless.liquid) （ライセンス: MIT、24行）
- **ファイル:** `Sort Shopify collection by metafield/sort-shopify-collection-products-by-metafield-value-commentless.liquid`

**説明:** コレクションに属する商品を、メタフィールド(global.order)の値に基づいてカスタム順序で並び替える。Shopify の標準ソート機能では実現できない柔軟な順序付けに対応。

**用途:** コレクションページで、管理画面で設定したメタフィールドの順序値を反映させ、商品の表示順をコントロールしたいとき。おすすめ商品順やカテゴリ内での推奨順序を実装できる。

**設置場所:** sections/collection-products.liquid など、コレクション商品をループするセクション内に貼り付け、`collection.products` のループ部分をこのコードに置き換える。メタフィールド `global.order` に数値を入力した商品から順に表示される。

**注意点:** メタフィールド `global.order` が商品に設定されていないと、デフォルト値 999999 が適用され、ソート順では最後尾に移動する。このコードは Liquid の配列操作だけで実装されているため、商品数が数百件を超える場合はレンダリング時間が長くなる可能性がある。パフォーマンスが問題になる場合は JavaScript での並び替えやストレージ API への移行を検討する。

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


### 40. 🧩 スニペット セクションヘッダー（タイトル・説明文）

**カテゴリ:** UI部品 ／ **難易度:** 初級 ／ **タグ:** `section` `header` `reusable-component` `theme-settings` `typography`

- **出典:** [`kondasoft/ks-bootshop`](https://raw.githubusercontent.com/kondasoft/ks-bootshop/master/snippets/section-header.liquid) （ライセンス: MIT、24行）
- **ファイル:** `snippets/section-header.liquid`

**説明:** セクション共通のヘッダー部分を表示するスニペット。テーマ設定からセクションのタイトルと説明文を取得し、条件付きで h2 タグと説明 div を中央寄せで出力する。

**用途:** 複数のセクション（商品表示、コレクション、お知らせ等）で共通のヘッダースタイルを使うとき。セクション設定画面からテキストを管理し、統一デザインで表示できる。

**設置場所:** snippets/section-header.liquid に配置し、各セクション内（sections/ 配下の Liquid ファイル）で `{% render 'section-header', class: 'custom-class' %}` で呼び出す。タイトルと説明文は Theme Customizer のセクション設定で編集する。

**注意点:** タイトル・説明文が両方とも空欄の場合は header 要素全体が出力されないため、セクション設定で片方だけ記入するとヘッダーが表示されない。説明文は `.rte` クラス（Rich Text Editor）で Markdown 形式に対応しており、**太字**や*斜体*が表示される。フォントサイズクラス（header_title_font_size 等）は theme settings に定義済みの CSS クラス名を指定する必要があり、存在しないクラスを設定すると反映されない。

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
| 処理時間（秒） | 36.3 | 37.7 | — |
| 入力 tokens | 46,679 | 46,679 | 0 |
| 出力 tokens | 23,983 | 23,678 | -305 |
| キャッシュ作成 tokens | 34,704 | 37,878 | +3,174 |
| キャッシュ読込 tokens | 182,196 | 277,772 | +95,576 |
| 推定コスト (USD) | $0.2282 | $0.2402 | +$0.0120 |

### カテゴリ分布の変化

| カテゴリ | v1 | v2 | 差分 |
|---|---:|---:|---:|
| ページテンプレート | 10 | 10 | 0 |
| テーマ基盤 | 5 | 5 | 0 |
| ヘッダー/フッター/ナビゲーション | 5 | 5 | 0 |
| コレクション/検索 | 4 | 4 | 0 |
| UI部品 | 4 | 4 | 0 |
| リファレンス/フィルター | 4 | 4 | 0 |
| リファレンス/オブジェクト | 3 | 3 | 0 |
| SEO/構造化データ | 3 | 3 | 0 |
| API連携/JSON出力/JS統合 | 3 | 3 | 0 |
| リファレンス/タグ | 3 | 3 | 0 |
| ユーティリティ | 2 | 2 | 0 |
| 商品表示 | 2 | 2 | 0 |
| 顧客アカウント | 1 | 1 | 0 |
| メタフィールド/メタオブジェクト | 1 | 1 | 0 |

### 難易度分布の変化

| 難易度 | v1 | v2 |
|---|---:|---:|
| 初級 | 31 | 28 |
| 中級 | 15 | 17 |
| 上級 | 4 | 5 |
