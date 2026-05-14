# お名前.com DNS 設定手順(liquid-jp.jp)

作成日: 2026-05-14 / Vercel から DNS 設定値取得済み

---

## TL;DR(Cowork に渡す指示文・コピペ用)

> お疲れさまです。
> 新サイト `liquid-jp.jp` の DNS 設定を以下の内容でお願いします。
> ドメインは お名前.com で取得済みです。
>
> **設定内容(2 レコード):**
>
> | ホスト名 | TYPE | TTL | VALUE |
> |---|---|---|---|
> | (空欄、ルート) | A | 3600 | `76.76.21.21` |
> | www | CNAME | 3600 | `cname.vercel-dns.com.` |
>
> **手順:**
> 1. お名前.com 管理画面 → ドメイン → `liquid-jp.jp` → 「DNS 関連機能の設定」
> 2. 「DNS レコード設定を利用する」→「設定する」
> 3. 上記 2 レコードを追加 → 「確認画面へ進む」→「設定する」
>
> 設定完了したら、こちらで反映確認(数分〜数時間)した後、Vercel 側で SSL 証明書発行を確認します。
> ご不明点あればご連絡ください。

---

## 詳細手順(お名前.com 管理画面)

### 1. ログイン
1. <https://www.onamae.com/navi/login.html> にログイン
2. 上部メニュー「ドメイン」→ ドメイン一覧から `liquid-jp.jp` をクリック
3. 「ネームサーバー情報」セクションへ

### 2. ネームサーバー確認(重要)
**お名前.com デフォルトのネームサーバー(`dns1.onamae.com` / `dns2.onamae.com`)を使用したまま**で OK。
DNS レコードだけを以下で設定する。

> ⚠️ Vercel から「ネームサーバーを `ns1.vercel-dns.com` / `ns2.vercel-dns.com` に変更してもよい」と提案されますが、
> その場合 メール・サブドメインの設定も Vercel 側に移行する必要があるため、**A レコード方式(本ドキュメント)を推奨**します。

### 3. DNS レコード設定
1. 左メニュー「ネームサーバーの設定」→「DNS 関連機能の設定」
2. `liquid-jp.jp` を選択 → 「次へ」
3. 「DNS レコード設定を利用する」→「設定する」
4. 既存レコードがあれば確認(@/MX レコード等は触らない)
5. 以下の 2 レコードを追加:

| ホスト名 | TYPE | TTL | VALUE |
|---|---|---|---|
| `(空欄)` | A | 3600 | `76.76.21.21` |
| `www` | CNAME | 3600 | `cname.vercel-dns.com.` |

6. 「追加」→ 確認画面 →「設定する」

### 4. 反映確認(数分〜最大 24 時間)

```bash
# A レコード反映確認
dig liquid-jp.jp +short
# 期待値: 76.76.21.21

# www CNAME 反映確認
dig www.liquid-jp.jp +short
# 期待値: cname.vercel-dns.com.
#         76.76.21.21
```

---

## Vercel 側の確認(DNS 反映後)

1. <https://vercel.com/takehirosaito-alselcojps-projects/liquid-jp/settings/domains> を開く
2. `liquid-jp.jp` の状態確認:
   - ✅ **Valid Configuration**(DNS 反映直後、数分で)
   - ✅ **SSL Certificate Issued**(Let's Encrypt 自動発行、最大 24 時間)

CLI でも確認可:
```bash
cd ~/liquid-jp/apps/web
npx vercel domains inspect liquid-jp.jp
```

`WARNING! This domain is not configured properly` の表示が消えれば設定完了。

---

## トラブルシュート

### A レコードの IP が違うと表示される
Vercel の Anycast IP は通常 `76.76.21.21` だが、変更される可能性があります。
最新値の確認:
- <https://vercel.com/docs/projects/domains/working-with-domains>
- または `npx vercel domains inspect liquid-jp.jp`

### SSL 証明書が発行されない
- 24 時間以上待っても出ない場合、Vercel ダッシュボードで「Refresh」ボタンを押す
- DNS が正しく反映されているか `dig` で再確認
- 既存の A レコードが残っている場合、削除して再設定

### www あり/なし両対応
`www.liquid-jp.jp` から `liquid-jp.jp` への 308 リダイレクトは Vercel が自動設定(primary = `liquid-jp.jp`)。
逆方向にしたい場合は Vercel `Settings → Domains` で primary を切り替える。

### メール(@liquid-jp.jp)を使う場合
お名前.com デフォルトの MX レコードを維持していれば、Vercel 設定で影響なし(A レコード追加のみ)。
独自のメールホスティング(Google Workspace 等)を使う場合は別途 MX レコード設定が必要。

---

## 現在のステータス(2026-05-14 時点)

- ✅ Vercel プロジェクト `liquid-jp` 作成済み(team `takehirosaito-alselcojps-projects`)
- ✅ 本番デプロイ完了: `https://liquid-4v0yj5jeb-takehirosaito-alselcojps-projects.vercel.app`
- ✅ ドメイン `liquid-jp.jp` をプロジェクトに登録済み
- ⏳ **お名前.com 側の DNS 設定待ち**(本ドキュメントの手順を実行)
- ⏳ DNS 反映 + SSL 証明書発行(設定後 数分〜24 時間)

---

## 関連リソース

- Vercel ダッシュボード: <https://vercel.com/takehirosaito-alselcojps-projects/liquid-jp>
- GitHub リポジトリ: <https://github.com/takehirosaito/liquid-jp>
- Meilisearch インデックス: `liquid_jp`(Railway、640 件)
