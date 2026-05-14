# liquid-jp.jp フロントエンド

Next.js 16 + Tailwind 4 + Meilisearch で構築。

- 本番ドメイン: <https://liquid-jp.jp>(取得待ち)
- 検索バックエンド: Railway Meilisearch (`liquid_jp` インデックス、640 件)
- ホスティング: Vercel
- 親リポジトリ: <https://github.com/takehirosaito/liquid-jp>(予定)

## 開発環境

```bash
# 依存インストール
npm install

# 環境変数(リポジトリ直下の .env.local を読む)
# 必須:
#   LIQUID_PROD_MEILI_HOST=https://<railway>.up.railway.app
#   LIQUID_PROD_MEILI_MASTER_KEY=<key>
# (現状は ~/agent-skills.jp/agent-skills-jp/.env への symlink で共有)

# dev サーバ
PORT=3100 npm run dev
# → http://localhost:3100
```

## 主要パス

| パス | 役割 |
|---|---|
| `/` | トップ(ヒーロー + カテゴリ + 注目スニペット) |
| `/search?q=<q>` | 検索結果 |
| `/snippet/[id]` | 個別詳細(コード + Source/License + 関連項目) |
| `/category` | カテゴリ一覧 |
| `/category/[slug]` | カテゴリ別スニペット一覧 |
| `/about` `/privacy` `/terms` | 静的ページ |
| `/api/search` | JSON 検索 API(CORS 対応、外部ツールから利用可) |
| `/sitemap.xml` `/robots.txt` `/opengraph-image` | SEO |

## ディレクトリ構成

```
apps/web/
├── package.json
├── tsconfig.json / next.config.ts / postcss.config.mjs / eslint.config.mjs
├── vercel.json
├── public/
│   ├── logo.svg          ヘッダーロゴ(液滴 + {{}} + Liquid Snippets)
│   └── icon.svg          favicon / apple-touch-icon
└── src/
    ├── app/
    │   ├── layout.tsx    ヘッダー/フッター/メタ
    │   ├── page.tsx      トップ
    │   ├── globals.css   Tailwind 4 + brand variables + hljs テーマ
    │   ├── search/page.tsx
    │   ├── snippet/[id]/page.tsx
    │   ├── category/page.tsx
    │   ├── category/[slug]/page.tsx
    │   ├── about/page.tsx
    │   ├── privacy/page.tsx
    │   ├── terms/page.tsx
    │   ├── not-found.tsx
    │   ├── sitemap.ts
    │   ├── robots.ts
    │   ├── opengraph-image.tsx
    │   └── api/search/route.ts
    ├── components/
    │   ├── SearchBar.tsx
    │   └── SnippetCard.tsx
    └── lib/
        └── meilisearch.ts  検索クライアント + Snippet 型
```

## Vercel デプロイ手順(ドメイン取得後)

`docs/vercel_deploy_guide.md` を参照。

## トンマナ

- 紫系(violet-600〜800)を基調、agent-skills.jp(青系)とは差別化しつつ姉妹サイト感
- ロゴは液滴形 + `{{}}` で「Liquid 言語のスニペット集」を象徴
- 商標配慮: フッター・Terms に「本サイトは Shopify Inc. の公式サイトではない」明記

## ライセンス

- フロントエンドソース: 本リポジトリ独自(後日 LICENSE 確定)
- 掲載 Liquid コード: 各リポジトリの MIT ライセンスに基づく(各詳細ページで明示)
- 日本語訳テキスト: CC BY 4.0(出典として liquid-jp.jp 明示)
