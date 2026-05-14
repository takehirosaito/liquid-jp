# Phase 3 ブロック3: title_too_long 自動仕分け

対象: 128 件 / 所要 17.1秒 / モデル claude-haiku-4-5-20251001

- **A: 短縮適用** … **36件**(自動で `title_ja` を更新、`title-too-long` タグ除去)
- **B: 短縮困難で維持** … **92件**
- **C: 人間レビュー対象** … **0件**

## A: 短縮適用済み

| # | Before(字数) | After(字数) | id |
|---:|---|---|---|
| 1 | Prettier Liquid プラグインの括弧配置設定テスト (31) | **Prettier Liquid プラグイン括弧配置設定テスト** (30) | `comm-Shopify-theme-tools-d68d2a71da` |
| 2 | Prettier Liquid プラグイン設定テスト（括弧位置） (32) | **Prettier Liquid プラグイン括弧位置テスト** (28) | `comm-Shopify-theme-tools-b5bcdb5fb4` |
| 3 | increment・decrement タグ（カウンタ変数の増減） (33) | **increment・decrement タグ（変数の増減）** (29) | `comm-Shopify-theme-tools-3e8310202b` |
| 4 | cycle タグの書式テスト（Prettier フォーマッタ検証） (33) | **cycle タグの書式テスト（Prettier検証）** (26) | `comm-Shopify-theme-tools-af4bebb9bd` |
| 5 | Prettier Liquid プラグインのホワイトスペース処理テスト (35) | **Prettier Liquid ホワイトスペース処理テスト** (29) | `comm-Shopify-theme-tools-dfd2c8351d` |
| 6 | Liquid と JavaScript の混在時のインデント制御 (32) | **Liquid と JavaScript のインデント制御** (28) | `comm-Shopify-theme-tools-30cb3ea8ea` |
| 7 | Prettier フォーマット無視コメント（Liquid・HTML） (34) | **Prettier フォーマット無視コメント** (21) | `comm-Shopify-theme-tools-58733aa625` |
| 8 | render タグのフォーマット規則（prettier プラグインテスト） (37) | **render タグのフォーマット規則** (18) | `comm-Shopify-theme-tools-c6a4410259` |
| 9 | assign タグのフォーマット規則（Prettier プラグイン） (34) | **assign タグのフォーマット規則（Prettier）** (28) | `comm-Shopify-theme-tools-b93ffaecde` |
| 10 | Prettier による Liquid コードのフォーマット（HTML タグ整形） (41) | **Prettier による Liquid コードのフォーマット** (30) | `comm-Shopify-theme-tools-24b2d052db` |
| 11 | asset_url フィルター（テーマアセットのCDN URLを取得） (35) | **asset_url フィルター（CDN URLを取得）** (27) | `ref-filters-asset_url` |
| 12 | avatar フィルター（顧客アバター画像の HTML 生成） (31) | **avatar フィルター（顧客アバター画像HTML生成）** (28) | `ref-filters-avatar` |
| 13 | blake3 フィルター（文字列をBLAKE3ハッシュに変換） (31) | **blake3 フィルター（BLAKE3ハッシュ変換）** (26) | `ref-filters-blake3` |
| 14 | color_brightness フィルター（色の明るさを数値で取得） (35) | **color_brightness フィルター（明るさ取得）** (29) | `ref-filters-color_brightness` |
| 15 | color_desaturate フィルター（色の彩度を下げる） (32) | **color_desaturate フィルター（彩度低下）** (28) | `ref-filters-color_desaturate` |
| 16 | color_mix フィルター（2色をブレンドして中間色を生成） (32) | **color_mix フィルター（色のブレンド）** (23) | `ref-filters-color_mix` |
| 17 | currency_selector フィルター（通貨選択ドロップダウン生成） (38) | **currency_selector フィルター（通貨選択）** (29) | `ref-filters-currency_selector` |
| 18 | default フィルター（空値・false・nil をデフォルト値に置き換え） (40) | **default フィルター（空値をデフォルト値に置き換え）** (29) | `ref-filters-default` |
| 19 | escape_once フィルター（HTML エスケープ済み文字を二重エスケープしない） (44) | **escape_once フィルター（二重エスケープ防止）** (28) | `ref-filters-escape_once` |
| 20 | file_url フィルター（ファイルのCDN URLを取得） (31) | **file_url フィルター（ファイルCDN URL取得）** (29) | `ref-filters-file_url` |
| 21 | font_modify フィルター（フォントのウェイト・スタイルを変更） (36) | **font_modify フィルター（フォント装飾変更）** (27) | `ref-filters-font_modify` |
| 22 | image_tag フィルター（画像を HTML img タグで出力） (35) | **image_tag フィルター（画像をHTMLタグ化）** (27) | `ref-filters-image_tag` |
| 23 | image_url フィルター（画像のリサイズ URL 生成） (31) | **image_url フィルター（画像リサイズ URL 生成）** (30) | `ref-filters-image_url` |
| 24 | link_to_tag フィルター（タグでフィルタリングされたページへのリンク生成） (42) | **link_to_tag フィルター（タグでフィルタリング）** (29) | `ref-filters-link_to_tag` |
| 25 | metafield_tag フィルター（メタフィールドを HTML タグに変換） (40) | **metafield_tag フィルター（HTMLタグ変換）** (29) | `ref-filters-metafield_tag` |
| 26 | money_amount フィルター（価格を小数点形式で整形） (31) | **money_amount フィルター（価格形式に整形）** (27) | `ref-filters-money_amount` |
| 27 | payment_button フィルター（決済ボタンのコンテナ生成） (34) | **payment_button フィルター（決済ボタン生成）** (29) | `ref-filters-payment_button` |
| 28 | pluralize フィルター（数に応じて単数・複数形を切り替え） (33) | **pluralize フィルター（単数・複数形の切り替え）** (28) | `ref-filters-pluralize` |
| 29 | sort_by フィルター（コレクション URL にソート条件を追加） (35) | **sort_by フィルター（URL にソート条件を追加）** (28) | `ref-filters-sort_by` |
| 30 | sort_natural フィルター（配列を自然な文字順でソート） (33) | **sort_natural フィルター（自然な文字順でソート）** (30) | `ref-filters-sort_natural` |
| 31 | truncatewords フィルター（文字列を単語数で切詰める） (33) | **truncatewords フィルター（単語数で切詰め）** (28) | `ref-filters-truncatewords` |
| 32 | translate フィルター（多言語テキストを翻訳キーから取得） (33) | **translate フィルター（翻訳キーから取得）** (25) | `ref-filters-translate` |
| 33 | url_decode フィルター（URL エンコード文字列をデコード） (35) | **url_decode フィルター（URL デコード）** (26) | `ref-filters-url_decode` |
| 34 | url_escape フィルター（URL 安全文字にエスケープ） (32) | **url_escape フィルター（URL エスケープ）** (27) | `ref-filters-url_escape` |
| 35 | javascript タグ（セクション・ブロック内の JavaScript コード） (42) | **javascript タグ（セクション・ブロック内のコード）** (30) | `ref-tags-javascript` |
| 36 | stylesheet タグ（セクション・ブロック・スニペットのCSS定義） (37) | **stylesheet タグ（CSS定義）** (20) | `ref-tags-stylesheet` |

## B: 維持(短縮困難) — 92件

| # | タイトル(字数) | 理由 | id |
|---:|---|---|---|
| 1 | prettier-plugin-liquid のフォーマット検証 (32) | AI 短縮版も 32 字: prettier-plugin-liquid のフォーマット検証 | `comm-Shopify-theme-tools-11c44e5bb0` |
| 2 | Prettier Liquid プラグインのドキュメント段落テスト (33) | AI 短縮版も 32 字: Prettier Liquid プラグインドキュメント段落テスト | `comm-Shopify-theme-tools-ecf040ee73` |
| 3 | Liquid コード整形（else タグのホワイトスペース制御） (32) | AI 短縮版も 87 字: Liquid コード整形（else タグのホワイトスペース制御）

このタイトルは既に32字のため、短縮が必要です。

**短縮案:**
else タグのホワイトスペース制御 | `comm-Shopify-theme-tools-d8730940dd` |
| 4 | Prettier Liquid プラグインの末尾空白処理テスト (31) | AI 短縮版も 31 字: Prettier Liquid プラグインの末尾空白処理テスト | `comm-Shopify-theme-tools-1652a7193c` |
| 5 | content_for タグ（レイアウトへのコンテンツ埋め込み） (32) | AI 短縮版も 32 字: content_for タグ（レイアウトへのコンテンツ埋め込み） | `comm-Shopify-theme-tools-4d6a4abff3` |
| 6 | Liquid と JavaScript のインデント整形ルール (31) | AI 短縮版も 31 字: Liquid と JavaScript のインデント整形ルール | `comm-Shopify-theme-tools-f592dbb05b` |
| 7 | Organization・WebSite・Product・Article構造化データ (42) | AI 短縮版も 120 字: Organization・WebSite・Product・Article構造化データ

このタイトルは既に 42 字で、30 字以内に短縮する必要があります。

DIFFICULT: 4つの構造化データタイプの並列を30字以内に維持できない | `comm-kondasoft-ks-bootshop-d439de13e6` |
| 8 | Prettier Liquid プラグインのホワイトスペース処理テスト (35) | AI 短縮版も 118 字: Prettier Liquid プラグインのホワイトスペース処理テスト

DIFFICULT: 元タイトルが既に35字で、重要キーワード(Prettier, Liquid, プラグイン, ホワイトスペース, 処理, テスト)が多く、削除 | `comm-Shopify-theme-tools-4210b761bd` |
| 9 | Prettier Liquid プラグインのHTML要素フォーマットテスト (37) | AI 短縮版も 37 字: Prettier Liquid プラグインのHTML要素フォーマットテスト | `comm-Shopify-theme-tools-7836ef8a2d` |
| 10 | Prettier Plugin Liquid のHTML要素フォーマットテスト (39) | AI 短縮版も 38 字: Prettier Plugin Liquid HTML要素フォーマットテスト | `comm-Shopify-theme-tools-70611b9dc4` |
| 11 | Prettier Liquid プラグインの空白文字処理テスト (31) | AI 短縮版も 31 字: Prettier Liquid プラグインの空白文字処理テスト | `comm-Shopify-theme-tools-ba5da12478` |
| 12 | Prettier Liquid プラグイン：条件分岐の空白整形テスト (34) | AI 短縮版も 34 字: Prettier Liquid プラグイン：条件分岐の空白整形テスト | `comm-Shopify-theme-tools-8190e96af8` |
| 13 | Prettier Liquid プラグイン: 末尾空白の最適化テスト (34) | AI 短縮版も 31 字: Prettier Liquid プラグイン末尾空白最適化テスト | `comm-Shopify-theme-tools-cf54418c0e` |
| 14 | Prettier Liquid プラグイン・自己クローズタグのフォーマット仕様 (39) | AI 短縮版も 32 字: Prettier Liquid プラグイン・自己クローズタグ仕様 | `comm-Shopify-theme-tools-07eb4c157c` |
| 15 | Prettier Liquid プラグインのスクリプトタグ整形テスト (34) | AI 短縮版も 34 字: Prettier Liquid プラグインのスクリプトタグ整形テスト | `comm-Shopify-theme-tools-6c27a4faf1` |
| 16 | Prettier Liquid プラグインのインデント設定テスト (32) | AI 短縮版も 32 字: Prettier Liquid プラグインのインデント設定テスト | `comm-Shopify-theme-tools-17f84c4d15` |
| 17 | Prettier Liquid プラグインのフォーマットテスト (31) | AI 短縮版も 31 字: Prettier Liquid プラグインのフォーマットテスト | `comm-Shopify-theme-tools-5e087b890a` |
| 18 | Prettier Liquid プラグインの HTML 属性フォーマットテスト (39) | AI 短縮版も 31 字: Prettier Liquid HTML属性フォーマットテスト | `comm-Shopify-theme-tools-404b14aeea` |
| 19 | asset_img_url フィルター（テーマアセット画像の CDN URL 取得） (42) | AI 短縮版も 31 字: asset_img_url フィルター（CDN URL 取得） | `ref-filters-asset_img_url` |
| 20 | article_img_url フィルター（ブログ記事画像の CDN URL を取得） (43) | AI 短縮版も 38 字: article_img_url フィルター（ブログ記事画像 CDN URL） | `ref-filters-article_img_url` |
| 21 | Prettier Liquid プラグインの HTML 空要素フォーマット仕様 (39) | AI 短縮版も 36 字: Prettier Liquid プラグイン HTML 空要素フォーマット | `comm-Shopify-theme-tools-54c805bde0` |
| 22 | base64_decode フィルター（Base64 エンコード文字列をデコード） (41) | AI 短縮版も 32 字: base64_decode フィルター（Base64 デコード） | `ref-filters-base64_decode` |
| 23 | base64_url_safe_encode フィルター（URL安全なBase64エンコード） (47) | AI 短縮版も 40 字: base64_url_safe_encode フィルター（URL安全エンコード） | `ref-filters-base64_url_safe_encode` |
| 24 | base64_encode フィルター（文字列を Base64 形式にエンコード） (41) | AI 短縮版も 33 字: base64_encode フィルター（Base64 エンコード） | `ref-filters-base64_encode` |
| 25 | base64_url_safe_decode フィルター（URL安全なBase64をデコード） (47) | AI 短縮版も 46 字: base64_url_safe_decode フィルター（URL安全なBase64デコード） | `ref-filters-base64_url_safe_decode` |
| 26 | brightness_difference フィルター（色のコントラスト計算） (39) | AI 短縮版も 37 字: brightness_difference フィルター（コントラスト計算） | `ref-filters-brightness_difference` |
| 27 | collection_img_url フィルター（コレクション画像の CDN URL を取得） (47) | AI 短縮版も 41 字: collection_img_url フィルター（コレクション画像 URL 取得） | `ref-filters-collection_img_url` |
| 28 | color_contrast フィルター（2色間のコントラスト比を計算） (36) | AI 短縮版も 31 字: color_contrast フィルター（コントラスト比計算） | `ref-filters-color_contrast` |
| 29 | color_difference フィルター（2色間のコントラスト差を計算） (38) | AI 短縮版も 34 字: color_difference フィルター（色のコントラスト計算） | `ref-filters-color_difference` |
| 30 | color_to_oklch フィルター（CSS 色を OKLCH 形式に変換） (40) | AI 短縮版も 37 字: color_to_oklch フィルター（CSS色をOKLCH形式に変換） | `ref-filters-color_to_oklch` |
| 31 | color_to_hex フィルター（CSS色を16進数に変換） (32) | AI 短縮版も 32 字: color_to_hex フィルター（CSS色を16進数に変換） | `ref-filters-color_to_hex` |
| 32 | color_to_hsl フィルター（CSS色をHSL形式に変換） (33) | AI 短縮版も 33 字: color_to_hsl フィルター（CSS色をHSL形式に変換） | `ref-filters-color_to_hsl` |
| 33 | customer_logout_link フィルター（ログアウトリンク生成） (38) | AI 短縮版も 38 字: customer_logout_link フィルター（ログアウトリンク生成） | `ref-filters-customer_logout_link` |
| 34 | color_to_rgb フィルター（CSS色をRGB形式に変換） (33) | AI 短縮版も 33 字: color_to_rgb フィルター（CSS色をRGB形式に変換） | `ref-filters-color_to_rgb` |
| 35 | customer_register_link フィルター（顧客登録ページへのリンク生成） (44) | AI 短縮版も 42 字: customer_register_link フィルター（顧客登録ページリンク生成） | `ref-filters-customer_register_link` |
| 36 | default_pagination フィルター（ページネーションリンクを自動生成） (42) | AI 短縮版も 36 字: default_pagination フィルター（ページネーション生成） | `ref-filters-default_pagination` |
| 37 | file_img_url フィルター（ファイルから画像URLを取得） (34) | AI 短縮版も 33 字: file_img_url フィルター（ファイルから画像URL取得） | `ref-filters-file_img_url` |
| 38 | default_errors フィルター（フォーム送信エラーを日本語化） (36) | AI 短縮版も 35 字: default_errors フィルター（フォーム送信エラー日本語化） | `ref-filters-default_errors` |
| 39 | customer_login_link フィルター（ログインページへのリンク生成） (41) | AI 短縮版も 39 字: customer_login_link フィルター（ログインページリンク生成） | `ref-filters-customer_login_link` |
| 40 | external_video_url フィルター（外部動画の URL を生成） (39) | AI 短縮版も 35 字: external_video_url フィルター（外部動画URL生成） | `ref-filters-external_video_url` |
| 41 | hex_to_rgba フィルター（16進数カラーをRGBA形式に変換） (36) | AI 短縮版も 33 字: hex_to_rgba フィルター（16進数をRGBA形式に変換） | `ref-filters-hex_to_rgba` |
| 42 | find_index フィルター（配列内のマッチ要素インデックス取得） (35) | AI 短縮版も 34 字: find_index フィルター（配列内マッチ要素インデックス取得） | `ref-filters-find_index` |
| 43 | external_video_tag フィルター（外部動画の埋め込みタグ生成） (39) | AI 短縮版も 32 字: external_video_tag フィルター（動画埋め込み） | `ref-filters-external_video_tag` |
| 44 | font_face フィルター（フォント読み込み用の@font-face宣言を生成） (42) | AI 短縮版も 33 字: font_face フィルター（@font-face 宣言の生成） | `ref-filters-font_face` |
| 45 | format_address フィルター（住所を地域形式で整形） (32) | AI 短縮版も 32 字: format_address フィルター（住所を地域形式で整形） | `ref-filters-format_address` |
| 46 | font_url フィルター（フォント CDN URL を取得） (32) | AI 短縮版も 31 字: font_url フィルター（フォント CDN URL 取得） | `ref-filters-font_url` |
| 47 | highlight_active_tag フィルター（アクティブなタグをマーク） (40) | AI 短縮版も 40 字: highlight_active_tag フィルター（アクティブなタグをマーク） | `ref-filters-highlight_active_tag` |
| 48 | hmac_sha1 フィルター（HMAC-SHA1ハッシュ生成） (32) | AI 短縮版も 32 字: hmac_sha1 フィルター（HMAC-SHA1ハッシュ生成） | `ref-filters-hmac_sha1` |
| 49 | global_asset_url フィルター（Shopify CDN上の共有アセットのURL取得） (49) | AI 短縮版も 41 字: global_asset_url フィルター（CDN上の共有アセット URL取得） | `ref-filters-global_asset_url` |
| 50 | img_tag フィルター（廃止・image_tag への移行推奨） (34) | AI 短縮版も 31 字: img_tag フィルター（image_tag への移行推奨） | `ref-filters-img_tag` |
| 51 | hmac_sha256 フィルター（HMAC-SHA256ハッシュ化） (35) | AI 短縮版も 35 字: hmac_sha256 フィルター（HMAC-SHA256ハッシュ化） | `ref-filters-hmac_sha256` |
| 52 | inline_asset_content フィルター（アセットの内容をインライン展開） (43) | AI 短縮版も 35 字: inline_asset_content フィルター（インライン展開） | `ref-filters-inline_asset_content` |
| 53 | item_count_for_variant フィルター（カート内の特定バリアント数） (43) | AI 短縮版も 40 字: item_count_for_variant フィルター（カート内バリアント数） | `ref-filters-item_count_for_variant` |
| 54 | line_items_for フィルター（カート内の特定商品の行アイテムを抽出） (40) | AI 短縮版も 34 字: line_items_for フィルター（カート内の特定商品を抽出） | `ref-filters-line_items_for` |
| 55 | link_to_add_tag フィルター（タグフィルタリングのリンク生成） (38) | AI 短縮版も 32 字: link_to_add_tag フィルター（タグ追加リンク生成） | `ref-filters-link_to_add_tag` |
| 56 | link_to_remove_tag フィルター（タグを除外したフィルタリングリンク） (43) | AI 短縮版も 33 字: link_to_remove_tag フィルター（タグ除外リンク） | `ref-filters-link_to_remove_tag` |
| 57 | link_to_vendor フィルター（ベンダーコレクションへのリンク生成） (39) | AI 短縮版も 37 字: link_to_vendor フィルター（ベンダーコレクションリンク生成） | `ref-filters-link_to_vendor` |
| 58 | login_button フィルター（顧客ログインボタンの生成） (32) | AI 短縮版も 31 字: login_button フィルター（顧客ログインボタン生成） | `ref-filters-login_button` |
| 59 | link_to_type フィルター（商品タイプ別コレクションへのリンク生成） (39) | AI 短縮版も 31 字: link_to_type フィルター（商品タイプ別リンク生成） | `ref-filters-link_to_type` |
| 60 | media_tag フィルター（メディアを適切なHTML要素に変換） (34) | AI 短縮版も 31 字: media_tag フィルター（メディアをHTML要素に変換） | `ref-filters-media_tag` |
| 61 | metafield_text フィルター（メタフィールドをテキスト形式で抽出） (39) | AI 短縮版も 31 字: metafield_text フィルター（テキスト形式で抽出） | `ref-filters-metafield_text` |
| 62 | money_without_trailing_zeros フィルター（末尾ゼロなし金額表示） (46) | AI 短縮版も 44 字: money_without_trailing_zeros フィルター（末尾ゼロなし金額） | `ref-filters-money_without_trailing_zeros` |
| 63 | money_with_currency フィルター（金額をストア通貨記号付きで整形） (42) | AI 短縮版も 37 字: money_with_currency フィルター（通貨記号付き金額表示） | `ref-filters-money_with_currency` |
| 64 | model_viewer_tag フィルター（3D モデル表示） (32) | AI 短縮版も 32 字: model_viewer_tag フィルター（3D モデル表示） | `ref-filters-model_viewer_tag` |
| 65 | money_without_currency フィルター（金額を通貨記号なしで整形） (42) | AI 短縮版も 38 字: money_without_currency フィルター（通貨記号なし整形） | `ref-filters-money_without_currency` |
| 66 | newline_to_br フィルター（改行をHTML改行に変換） (33) | AI 短縮版も 31 字: newline_to_br フィルター（改行を<br>に変換） | `ref-filters-newline_to_br` |
| 67 | payment_terms フィルター（Shop Pay分割払いバナーを生成） (39) | AI 短縮版も 38 字: payment_terms フィルター（Shop Pay分割払いバナー生成） | `ref-filters-payment_terms` |
| 68 | placeholder_svg_tag フィルター（プレースホルダーSVGを生成） (41) | AI 短縮版も 32 字: placeholder_svg_tag フィルター（SVG生成） | `ref-filters-placeholder_svg_tag` |
| 69 | payment_type_img_url フィルター（決済方法のアイコン画像 URL を取得） (47) | AI 短縮版も 43 字: payment_type_img_url フィルター（決済方法アイコン URL 取得） | `ref-filters-payment_type_img_url` |
| 70 | product_img_url フィルター（商品画像の CDN URL 取得） (39) | AI 短縮版も 34 字: product_img_url フィルター（商品画像 URL 取得） | `ref-filters-product_img_url` |
| 71 | payment_type_svg_tag フィルター（決済方法アイコンをSVG生成） (42) | AI 短縮版も 38 字: payment_type_svg_tag フィルター（決済方法アイコン生成） | `ref-filters-payment_type_svg_tag` |
| 72 | remove_first フィルター（文字列の最初の1つを削除） (32) | AI 短縮版も 32 字: remove_first フィルター（文字列の最初の1つを削除） | `ref-filters-remove_first` |
| 73 | replace_last フィルター（文字列の最後に出現する部分文字列を置換） (39) | AI 短縮版も 34 字: replace_last フィルター（文字列末尾の部分文字列を置換） | `ref-filters-replace_last` |
| 74 | script_tag フィルター（JavaScript ファイルを <script> タグに変換） (49) | AI 短縮版も 43 字: script_tag フィルター（JavaScript を script タグに変換） | `ref-filters-script_tag` |
| 75 | structured_data フィルター（schema.org 構造化データに変換） (43) | AI 短縮版も 42 字: structured_data フィルター（schema.org 構造化データ対応） | `ref-filters-structured_data` |
| 76 | stylesheet_tag フィルター（CSS ファイルのリンクタグを生成） (39) | AI 短縮版も 33 字: stylesheet_tag フィルター（CSS リンクタグ生成） | `ref-filters-stylesheet_tag` |
| 77 | shopify_asset_url フィルター（Shopifyグローバルアセット CDN URL を取得） (53) | AI 短縮版も 40 字: shopify_asset_url フィルター（アセット CDN URL 取得） | `ref-filters-shopify_asset_url` |
| 78 | unit_price_with_measurement フィルター（単価と計量単位の表示） (45) | AI 短縮版も 42 字: unit_price_with_measurement フィルター（単価と計量単位） | `ref-filters-unit_price_with_measurement` |
| 79 | time_tag フィルター（タイムスタンプをHTMLの時刻要素に変換） (36) | AI 短縮版も 31 字: time_tag フィルター（タイムスタンプを時刻要素に変換） | `ref-filters-time_tag` |
| 80 | url_param_escape フィルター（URL パラメータ用文字列エスケープ） (42) | AI 短縮版も 38 字: url_param_escape フィルター（URL パラメータエスケープ） | `ref-filters-url_param_escape` |
| 81 | url_for_vendor フィルター（ベンダー別コレクションURL生成） (38) | AI 短縮版も 32 字: url_for_vendor フィルター（ベンダー別URL生成） | `ref-filters-url_for_vendor` |
| 82 | url_for_type フィルター（商品タイプ別URLを生成） (32) | AI 短縮版も 31 字: url_for_type フィルター（商品タイプ別URL生成） | `ref-filters-url_for_type` |
| 83 | additional_checkout_buttons オブジェクト (34) | AI 短縮版も 34 字: additional_checkout_buttons オブジェクト | `ref-objects-additional_checkout_buttons` |
| 84 | weight_with_unit フィルター（バリアント重量を単位付きで整形） (39) | AI 短縮版も 34 字: weight_with_unit フィルター（重量を単位付きで整形） | `ref-filters-weight_with_unit` |
| 85 | content_for_additional_checkout_buttons オブジェクト (46) | AI 短縮版も 46 字: content_for_additional_checkout_buttons オブジェクト | `ref-objects-content_for_additional_checkout_buttons` |
| 86 | predictive_search_resources オブジェクト (34) | AI 短縮版も 34 字: predictive_search_resources オブジェクト | `ref-objects-predictive_search_resources` |
| 87 | pending_payment_instruction_input オブジェクト (40) | AI 短縮版も 40 字: pending_payment_instruction_input オブジェクト | `ref-objects-pending_payment_instruction_input` |
| 88 | selling_plan_allocation_price_adjustment オブジェクト (47) | AI 短縮版も 47 字: selling_plan_allocation_price_adjustment オブジェクト | `ref-objects-selling_plan_allocation_price_adjustment` |
| 89 | selling_plan_price_adjustment オブジェクト (36) | AI 短縮版も 36 字: selling_plan_price_adjustment オブジェクト | `ref-objects-selling_plan_price_adjustment` |
| 90 | transaction_payment_details オブジェクト (34) | AI 短縮版も 34 字: transaction_payment_details オブジェクト | `ref-objects-transaction_payment_details` |
| 91 | selling_plan_group_option オブジェクト (32) | AI 短縮版も 32 字: selling_plan_group_option オブジェクト | `ref-objects-selling_plan_group_option` |
| 92 | selling_plan_checkout_charge オブジェクト (35) | AI 短縮版も 35 字: selling_plan_checkout_charge オブジェクト | `ref-objects-selling_plan_checkout_charge` |

## C: 人間レビュー対象 — 0件

| # | タイトル(字数) | 理由 | id |
|---:|---|---|---|

## メタ

- 入力 tokens: 60,160 / 出力 tokens: 2,917
- cache create: 0 / cache read: 0
- cache_hit_rate: 0.0%
- 推定コスト: **$0.0747**