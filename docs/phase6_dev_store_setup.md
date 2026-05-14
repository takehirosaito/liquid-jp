# Phase 6β 開発ストア セットアップ手順

22 セクションを実機で確認 + スクショ撮影するため、Shopify Partners で開発ストアを作成して
Admin API トークンを発行する手順。

作業時間目安: 約 15 分

---

## 1. Shopify Partners アカウントの確認

すでに Partners アカウントを持っているなら、<https://partners.shopify.com> にログイン。

未取得なら:
1. <https://www.shopify.com/jp/partners> から無料登録
2. メール認証
3. 会社情報入力(ALSEL の情報で OK)

---

## 2. 開発ストア作成

1. Partners ダッシュボード → 左メニュー「ストア」
2. 「ストアを追加」→「**開発ストアを作成**」を選択
3. 設定:
   - ストア名: `alsel-liquid-jp-dev`(例)
   - 目的: 「アプリやテーマを構築するため」を選択
   - 開発ストアタイプ: 「**テーマやアプリのテスト**」
   - パスワード: 任意の強いパスワード
4. 作成完了後、URL は `alsel-liquid-jp-dev.myshopify.com` のような形式になる

---

## 3. テーマの確認

新規開発ストアにはデフォルトで Shopify 公式テーマ(Dawn 等)が main として入っている。
本作業は **Dawn 上に sections/*.liquid を追加投入する**形で行う(Dawn のセクション群と
ALSEL 監修セクションが共存する構成)。

> ⚠️ **注意**: 本プロジェクトの方針として「Dawn は再配布不可」だが、**開発ストア内でのテスト利用は許容範囲**
> (Theme Store 経由の正規 Dawn なので、ライセンス上問題なし)。あくまで実機テスト用途で、
> Dawn 自体を配布・改変するわけではない。

代替: Skeleton Theme(MIT、純粋)を Theme Store からインストールして main にする選択肢もある。
プレビュー品質が高い Dawn のほうがスクショ映えするので Dawn 推奨。

---

## 4. Admin API トークン発行(Custom App)

1. 開発ストア管理画面 → 設定 → アプリと販売チャネル → 「**アプリ開発**」を有効化
2. 「アプリを作成」→「**カスタム App を作成**」
3. App 名: `liquid-jp-uploader`
4. App 作成後、「Configuration」タブ →「**Admin API integration**」を構成
5. **必要な API スコープ**(以下のみ ON):
   - `write_themes` ✅(テーマアセットの書き込み)
   - `read_themes` ✅(テーマ一覧の取得)
   - `read_files` ✅(画像アセット用、任意)
6. 「保存」→「**インストール**」→「Admin API アクセストークンをコピー」(`shpat_...` 形式)

> ⚠️ Admin API トークンは **一度しか表示されない**。すぐに `~/liquid-jp/.env` に追記すること。

---

## 5. `.env` への追記

```bash
cat >> ~/liquid-jp/.env <<'EOF'

# Shopify 開発ストア(Phase 6β 実機検証用)
DEV_STORE_DOMAIN=alsel-liquid-jp-dev.myshopify.com
DEV_STORE_ADMIN_TOKEN=shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# DEV_STORE_THEME_ID は省略可(空ならスクリプトが自動で main を選択)
EOF
chmod 600 ~/liquid-jp/.env
```

---

## 6. 投入動作確認

```bash
cd ~/liquid-jp

# テーマ一覧を取得して main theme の id を確認
.venv/bin/python scripts/upload_to_dev_store.py --list-themes
# 出力例:
#   👑 id=149285896389 role=main         name='Dawn'

# 投入前にドライランで対象ファイル確認(API 叩かない)
.venv/bin/python scripts/upload_to_dev_store.py --dry-run

# 1 ファイルだけテスト投入(hero-fv-lp)
.venv/bin/python scripts/upload_to_dev_store.py --slugs hero-fv-lp

# 全 22 件投入
.venv/bin/python scripts/upload_to_dev_store.py
```

---

## 7. 投入確認(管理画面)

1. 開発ストア管理画面 → オンラインストア → テーマ → main theme(Dawn)
2. 「アクション」→「コードを編集」
3. 左サイドバーの `Sections` フォルダを開く
4. `alsel-section-*` のような ALSEL 監修セクション 22 個が並んでいることを確認
5. テーマカスタマイザーで「セクションを追加」→「ALSEL監修 / ...」のプリセットが出るかも確認

---

## 8. スクショ撮影への接続(Phase 6β-D)

`scripts/screenshot_sections.py`(Playwright スクリプト、別途準備)が以下の URL に対し
ヘッドレスでフルページスクショを撮影:

- 各セクションを 1 個ずつトップページに追加した状態の URL(プレビューモード)
- 開発ストアパスワード認証を Playwright でバイパス
- 出力: `~/liquid-jp/output/section_screenshots/{slug}.png`

---

## トラブルシュート

### `401 Unauthorized` が返る
- `DEV_STORE_ADMIN_TOKEN` が間違っているか、スコープ不足
- Custom App の `write_themes` スコープを確認 → 再保存 → 再インストール

### `404 Not Found - theme not found`
- `DEV_STORE_THEME_ID` が間違っている
- `--list-themes` で main theme の id を再取得して `.env` に書き直す

### `422 Unprocessable Entity - schema syntax error`
- セクションの `{% schema %}` の JSON が壊れている
- ローカルで `shopify theme check` を再実行(Theme Check の docs/phase6_check_report.md は clean のはず)

### 投入後にカスタマイザーでプリセットが出ない
- セクションファイルに `presets` が定義されていれば「セクションを追加」→「自分のセクション」配下に表示される
- ハードリロード(Cmd+Shift+R)で表示されることがある
