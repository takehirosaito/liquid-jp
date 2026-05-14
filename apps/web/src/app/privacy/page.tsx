import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "プライバシーポリシー",
  description: "Liquid Snippets by ALSEL のプライバシーポリシー。",
};

export default function PrivacyPage() {
  return (
    <main className="max-w-3xl mx-auto px-6 py-10 prose prose-slate max-w-none">
      <h1>プライバシーポリシー</h1>
      <p className="text-sm text-slate-500">最終更新: 2026-05-14</p>

      <h2>1. 収集する情報</h2>
      <p>
        本サイト(liquid-jp.jp)では、サイト改善のため以下の匿名情報を収集する場合がある。
      </p>
      <ul>
        <li>アクセスログ(IP アドレス・User-Agent・参照元 URL・閲覧ページ)</li>
        <li>検索クエリ(個人を特定できる情報を除く)</li>
        <li>Cookie によるセッション情報・分析ツール用識別子</li>
      </ul>

      <h2>2. 利用目的</h2>
      <ul>
        <li>サイトの利用状況分析・コンテンツ改善</li>
        <li>不正アクセス・スパムの検知と防止</li>
        <li>運営に関する統計の作成(個人を特定しない形)</li>
      </ul>

      <h2>3. 第三者への提供</h2>
      <p>
        以下の場合を除き、収集した情報を第三者に提供しない。
      </p>
      <ul>
        <li>法令に基づく開示請求があった場合</li>
        <li>サイト解析・ホスティングのため、Vercel / Google Analytics 等の処理委託先に必要最小限の情報を共有する場合</li>
      </ul>

      <h2>4. Cookie の利用</h2>
      <p>
        本サイトは利便性向上のため Cookie を利用する。
        Cookie は閲覧者のブラウザ設定で無効化できる。無効化した場合、一部機能が動作しないことがある。
      </p>

      <h2>5. 解析ツール</h2>
      <p>
        本サイトは Google Analytics 等のアクセス解析ツールを利用する場合がある。
        これらのツールは Cookie を利用してトラフィックデータを匿名で収集する。
      </p>

      <h2>6. 改定</h2>
      <p>
        本ポリシーは事前通知なく改定する場合がある。改定後の内容は本ページに掲載した時点から有効となる。
      </p>

      <h2>7. お問い合わせ</h2>
      <p>
        本ポリシーに関するお問い合わせは{" "}
        <a href="mailto:info@alsel.co.jp">info@alsel.co.jp</a> まで。
      </p>

      <p>
        <Link href="/">← ホームに戻る</Link>
      </p>
    </main>
  );
}
