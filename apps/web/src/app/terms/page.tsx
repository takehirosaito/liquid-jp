import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "利用規約",
  description: "Liquid Snippets by ALSEL の利用規約。",
};

export default function TermsPage() {
  return (
    <main className="max-w-3xl mx-auto px-6 py-10 prose prose-slate max-w-none">
      <h1>利用規約</h1>
      <p className="text-sm text-slate-500">最終更新: 2026-05-14</p>

      <h2>1. 本サービスについて</h2>
      <p>
        Liquid Snippets by ALSEL (以下「本サイト」)は、株式会社 ALSEL (以下「当社」)が運営する、
        Shopify Liquid テンプレート言語のリファレンス・コミュニティスニペットの日本語データベースである。
      </p>

      <h2>2. 掲載コードの権利・ライセンス</h2>
      <ul>
        <li>
          本サイトに掲載されているコードは、すべて MIT ライセンスのオープンソースリポジトリから収集している。
          原本の著作権は各著作者が保有する
        </li>
        <li>
          各コードの利用にあたっては、原本リポジトリの LICENSE ファイルに従うこと。
          各スニペット詳細ページに Source URL と License を明記している
        </li>
        <li>
          日本語訳テキストは ALSEL の著作物として、クリエイティブ・コモンズ 表示 4.0 国際 (CC BY 4.0) で公開する。
          再利用の際は出典として liquid-jp.jp を明示すること
        </li>
      </ul>

      <h2>3. 動作・正確性の保証</h2>
      <ul>
        <li>掲載コードの動作・互換性は保証しない</li>
        <li>日本語訳の正確性についても保証しない。誤訳の指摘は歓迎する</li>
        <li>
          本サイトの情報に基づいて利用者が行った行為について、当社は一切の責任を負わない
        </li>
      </ul>

      <h2>4. 禁止事項</h2>
      <ul>
        <li>本サイトの運営を妨害する行為</li>
        <li>本サイトの内容を改ざんしての再配布(出典明記は CC BY 4.0 の条件)</li>
        <li>自動化された大量アクセス(API のレート制限を遵守すること)</li>
        <li>その他、法令・公序良俗に反する行為</li>
      </ul>

      <h2>5. 商標</h2>
      <p>
        Liquid および Shopify は Shopify Inc. の商標または登録商標である。
        本サイトは Shopify Inc. の公式サイトではなく、関係もない。
      </p>

      <h2>6. 削除依頼</h2>
      <p>
        掲載リポジトリの著作者から削除依頼があった場合、または法令違反等が判明した場合、
        当社は速やかに該当コンテンツを削除する。削除依頼は{" "}
        <a href="mailto:info@alsel.co.jp">info@alsel.co.jp</a> まで。
      </p>

      <h2>7. 変更</h2>
      <p>
        本規約は事前通知なく変更する場合がある。変更後の内容は本ページに掲載した時点から有効となる。
      </p>

      <h2>8. 準拠法・管轄</h2>
      <p>
        本規約は日本法に準拠し、本サービスに関する一切の紛争は東京地方裁判所を第一審の専属的合意管轄裁判所とする。
      </p>

      <p>
        <Link href="/">← ホームに戻る</Link>
      </p>
    </main>
  );
}
