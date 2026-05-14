import Link from "next/link";
import { SearchBar } from "@/components/SearchBar";
import { SnippetCard } from "@/components/SnippetCard";
import {
  getStats,
  getFeaturedSnippets,
  CATEGORY_ICONS,
  categoryToSlug,
} from "@/lib/meilisearch";

export const revalidate = 300;

export default async function HomePage() {
  const [stats, featured] = await Promise.all([
    getStats(),
    getFeaturedSnippets(9),
  ]);

  // カテゴリは facet 件数の多い順に並べる
  const categories = Object.entries(stats.byCategory)
    .sort(([, a], [, b]) => b - a)
    .map(([name, count]) => ({
      name,
      count,
      icon: CATEGORY_ICONS[name] ?? "📦",
    }));

  return (
    <main>
      {/* ヒーロー */}
      <section className="bg-gradient-to-b from-violet-50 to-white py-20 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <p className="text-sm tracking-widest text-violet-700 mb-4 uppercase font-semibold">
            Liquid Snippets by ALSEL
          </p>
          <h1 className="text-4xl md:text-6xl font-bold tracking-tight mb-6 leading-tight">
            日本初の <span className="text-violet-700">Shopify Liquid</span>
            <br className="hidden md:inline" />
            日本語リファレンス。
          </h1>
          <p className="text-lg text-slate-600 mb-10 max-w-3xl mx-auto leading-relaxed">
            Shopify 公式ドキュメントを完全カバーする、検索可能な日本語リファレンス。
            フィルター・タグ・オブジェクトの仕様から、コミュニティの実装例まで網羅。
          </p>
          <SearchBar />
          <div className="mt-8 flex justify-center gap-6 flex-wrap text-sm text-slate-600">
            <div className="flex items-center gap-2">
              <span className="inline-block w-2 h-2 rounded-full bg-violet-600"></span>
              公式仕様 完全カバー
            </div>
            <div className="flex items-center gap-2">
              <span className="inline-block w-2 h-2 rounded-full bg-violet-600"></span>
              全件 MIT ライセンスでクリーン
            </div>
            <div className="flex items-center gap-2">
              <span className="inline-block w-2 h-2 rounded-full bg-violet-600"></span>
              横断検索可能
            </div>
          </div>
        </div>
      </section>

      {/* カテゴリから探す */}
      {categories.length > 0 && (
        <section className="py-16 px-6">
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-bold mb-8">カテゴリから探す</h2>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
              {categories.map((cat) => (
                <Link
                  key={cat.name}
                  href={`/category/${categoryToSlug(cat.name)}`}
                  className="block p-5 border border-slate-200 rounded-lg hover:shadow-md hover:border-violet-300 transition bg-white"
                >
                  <div className="text-2xl mb-2">{cat.icon}</div>
                  <div className="font-bold text-slate-900 text-sm leading-tight">
                    {cat.name}
                  </div>
                  <div className="text-xs text-slate-500 mt-1">
                    {cat.count} 件
                  </div>
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* 注目スニペット */}
      {featured.length > 0 && (
        <section className="py-16 px-6 bg-slate-50">
          <div className="max-w-6xl mx-auto">
            <div className="flex items-baseline justify-between mb-8">
              <h2 className="text-3xl font-bold">注目のスニペット</h2>
              <Link
                href="/search?q="
                className="text-sm text-violet-700 hover:underline"
              >
                すべて見る →
              </Link>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {featured.map((s) => (
                <SnippetCard key={s.id} snippet={s} />
              ))}
            </div>
          </div>
        </section>
      )}

      {/* About 案内 */}
      <section className="py-16 px-6">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-4">Liquid Snippets について</h2>
          <p className="text-slate-600 leading-relaxed">
            Shopify Liquid は、Shopify Inc. が開発したテンプレート言語です。
            本サイトは MIT ライセンスのオープンソースリポジトリから収集した
            Liquid コードのリファレンス・スニペットを、日本語で検索・参照できる
            データベースです。
          </p>
          <div className="mt-8 flex gap-4 justify-center flex-wrap">
            <Link
              href="/about"
              className="px-6 py-3 bg-violet-700 text-white rounded-lg hover:bg-violet-800"
            >
              詳しく見る
            </Link>
            <Link
              href="/category"
              className="px-6 py-3 border border-slate-300 rounded-lg hover:bg-slate-100"
            >
              カテゴリ一覧
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}
