import Link from "next/link";
import type { Metadata } from "next";
import { getStats } from "@/lib/meilisearch";

export const revalidate = 3600;

export const metadata: Metadata = {
  title: "About — Liquid Snippets by ALSEL について",
  description:
    "Liquid Snippets by ALSEL は、Shopify Liquid のリファレンスとコミュニティスニペットを日本語で検索できるデータベースです。",
};

export default async function AboutPage() {
  const stats = await getStats();
  // license × repo 集計
  const repoEntries = Object.entries(stats.byRepo).sort(([, a], [, b]) => b - a);

  return (
    <main className="max-w-3xl mx-auto px-6 py-10 prose prose-slate max-w-none">
      <h1>Liquid Snippets by ALSEL について</h1>

      <p className="lead text-lg text-slate-700 leading-relaxed">
        本サイトは、Shopify Liquid テンプレート言語のリファレンスとコミュニティ実装例を、
        日本語で検索・参照できるオープンデータベースです。
        株式会社 ALSEL が運営しています。
      </p>

      <h2>運営理念</h2>
      <p>
        日本の EC 事業者・Shopify 構築会社・フリーランス開発者にとって、
        Shopify Liquid の情報は英語ドキュメントに依存しがちで、学習・参照のハードルが高い状況です。
        本サイトは、世界中の MIT ライセンスのオープンソースから収集した Liquid コードを、
        実務で使いやすい形で日本語化・カタログ化することで、
        「日本初の Shopify Liquid 日本語リファレンス」として公開しています。
      </p>

      <h2>サイトの構成</h2>
      <ul>
        <li>
          <strong>公式リファレンス</strong>: Shopify の `theme-liquid-docs` リポジトリから、
          フィルター・タグ・オブジェクトの仕様を日本語化しています(計 {stats.referenceCount} 件)
        </li>
        <li>
          <strong>コミュニティスニペット</strong>: 完成テーマ・スニペット集から、
          実装例として有用なコードを日本語化しています(計 {stats.snippetCount} 件)
        </li>
      </ul>

      <h2>収録ソース・ライセンス</h2>
      <p>
        本サイトに掲載されているコードは、すべて MIT ライセンスのオープンソースリポジトリから収集しています。
        日本語訳テキストは ALSEL の著作物です。
      </p>
      <table>
        <thead>
          <tr>
            <th>リポジトリ</th>
            <th>件数</th>
            <th>ライセンス</th>
          </tr>
        </thead>
        <tbody>
          {repoEntries.map(([repo, count]) => (
            <tr key={repo}>
              <td>
                <a
                  href={`https://github.com/search?q=${encodeURIComponent(repo)}&type=repositories`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {repo}
                </a>
              </td>
              <td>{count}</td>
              <td>MIT</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>免責事項</h2>
      <ul>
        <li>
          本サイトは Shopify Inc. の公式サイトではありません。Liquid および Shopify は
          Shopify Inc. の商標です
        </li>
        <li>
          掲載コードの動作は保証しません。各自の環境・バージョンで動作確認の上ご利用ください
        </li>
        <li>
          日本語訳に誤訳・誤解を招く表現が見つかった場合は、お問い合わせよりご連絡ください
        </li>
        <li>
          掲載リポジトリの著作者から削除依頼があった場合、速やかに対応します
        </li>
      </ul>

      <h2>姉妹サイト</h2>
      <p>
        ALSEL は本サイトの他、
        <a href="https://agent-skills.jp" target="_blank" rel="noopener noreferrer">
          Agent Skills by ALSEL
        </a>{" "}
        (AI エージェントのスキル日本語カタログ)を運営しています。
      </p>

      <h2>運営者・お問い合わせ</h2>
      <p>
        <strong>株式会社 ALSEL</strong>
        <br />
        E-mail:{" "}
        <a href="mailto:info@alsel.co.jp">info@alsel.co.jp</a>
      </p>

      <p>
        <Link href="/">← ホームに戻る</Link>
      </p>
    </main>
  );
}
