# Vercel デプロイ手順(liquid-jp.jp)

このドキュメントは、たけさんが `liquid-jp.jp` ドメインを取得した後の
本番デプロイ手順をまとめたもの。`apps/web/` ディレクトリが Next.js アプリ。

---

## 前提

- ✅ ドメイン `liquid-jp.jp` 取得済み(お名前.com)
- ✅ Railway Meilisearch インスタンス起動済み(`liquid_jp` インデックス、640 件)
- ✅ `LIQUID_PROD_MEILI_HOST` / `LIQUID_PROD_MEILI_MASTER_KEY` を取得済み(`~/agent-skills.jp/agent-skills-jp/.env` に記載)

---

## ステップ 1: GitHub リポジトリ作成

```bash
cd ~/liquid-jp/apps/web
git init -b main

# .env.local は symlink で .gitignore 済み(コミット対象外)
git add .
git status   # .env / .env.local / node_modules / .next が除外されていることを確認

git commit -m "Initial commit: liquid-jp.jp フロントエンド(Phase 4)"

# GitHub に新規リポジトリ作成
gh repo create takehirosaito/liquid-jp \
  --public \
  --description "日本初の Shopify Liquid 日本語リファレンス" \
  --source=. \
  --remote=origin

git push -u origin main
```

ALSEL アカウントで運用したい場合は `takehirosaito/liquid-jp` を組織アカウントに置換。

> **注:** リポジトリ全体(`~/liquid-jp/`)には Phase 1〜3 のスクリプト・データ・ドキュメントも含むが、
> 本デプロイで Vercel に上げるのは `apps/web/` ディレクトリのみ。
> フロントだけを別リポジトリにしたい場合は `apps/web/` を独立 git init してもよい。

---

## ステップ 2: Vercel プロジェクト作成

1. <https://vercel.com/new> から **Import Git Repository**
2. `takehirosaito/liquid-jp` を選択
3. **Root Directory** を `apps/web` に設定
4. **Framework Preset**: Next.js(自動検出)
5. **Build & Output Settings**: `vercel.json` で定義済み(変更不要)

---

## ステップ 3: 環境変数設定(Vercel ダッシュボード)

`Settings → Environment Variables` で以下を追加:

| 変数名 | 値 | 環境 |
|---|---|---|
| `LIQUID_PROD_MEILI_HOST` | `https://getmeilimeilisearchv190-production-6830.up.railway.app` | Production / Preview / Development |
| `LIQUID_PROD_MEILI_MASTER_KEY` | (Railway で取得した master key) | Production / Preview / Development |
| `NEXT_PUBLIC_GA_ID` | (Google Analytics 設定後に追加、任意) | Production |
| `GOOGLE_SITE_VERIFICATION` | (Search Console 設定後に追加、任意) | Production |

> **セキュリティ:** `LIQUID_PROD_MEILI_MASTER_KEY` は `NEXT_PUBLIC_` プレフィックスなしで設定する
> (Server Components からのみ参照、ブラウザに露出させない設計)。

---

## ステップ 4: 初回デプロイ

「Deploy」ボタンで初回ビルド。所要 2〜3 分。

成功すると `https://<project-name>.vercel.app` にアクセス可能になる。

---

## ステップ 5: カスタムドメイン設定

1. Vercel `Settings → Domains` で `liquid-jp.jp` を追加
2. 表示される DNS レコード(A レコード or CNAME)を お名前.com の DNS 設定に追加
3. Vercel 側で自動的に SSL 証明書(Let's Encrypt)が発行される(数分〜数時間)
4. リダイレクトルール:
   - `www.liquid-jp.jp` → `liquid-jp.jp` への 308 リダイレクト(Vercel が自動設定)

---

## ステップ 6: デプロイ後の動作確認

```bash
# 主要パスを巡回
for path in / /category /about /privacy /terms /sitemap.xml /robots.txt /opengraph-image; do
  echo -n "$path → "
  curl -s -o /dev/null -w "%{http_code}\n" "https://liquid-jp.jp${path}"
done

# 検索 API
curl -s "https://liquid-jp.jp/api/search?q=カート&limit=3" | jq '.total, .count'

# 検索結果ページ
curl -s "https://liquid-jp.jp/search?q=カート" | grep -c "カートページ"
```

---

## ステップ 7: SEO 設定

### Google Search Console
1. <https://search.google.com/search-console> で `liquid-jp.jp` プロパティ追加
2. HTML タグ認証 → Vercel の `GOOGLE_SITE_VERIFICATION` 環境変数に値を設定 → 再デプロイ
3. サイトマップ送信: `https://liquid-jp.jp/sitemap.xml`

### Google Analytics(任意)
1. GA4 プロパティ作成 → 測定 ID 取得(`G-XXXXXXXXXX`)
2. Vercel の `NEXT_PUBLIC_GA_ID` 環境変数に設定
3. `layout.tsx` に `@next/third-parties` の `<GoogleAnalytics>` 組み込み(現状未実装、必要時に追加)

---

## ステップ 8: ローンチ後のモニタリング

- Vercel Analytics(ダッシュボードから無料で有効化可)
- Railway ダッシュボードで Meilisearch のレスポンスタイム・リクエスト数を確認
- Google Search Console の Coverage / Performance タブで SEO 状況確認

---

## ロールバック手順

Vercel `Deployments` タブから過去のデプロイを `Promote to Production` で即時ロールバック可能。

---

## 既知の TODO(Phase 5 以降)

- `apps/web/src/lib/meilisearch.ts` の `apiKey` を MASTER ではなく専用の検索キー(Read-only)に切り替え
  → Meilisearch で `tenant token` または `search-only key` を発行
- `@next/third-parties` で GA4 組み込み
- robots.txt の AI クローラ制御(必要に応じて GPTBot / ClaudeBot などを明示)
- Open Graph 画像のカスタマイズ(現状は動的生成、必要に応じて個別ページごとに固有画像生成)
