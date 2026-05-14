import Link from "next/link";
import type { Metadata } from "next";
import { getStats, CATEGORY_ICONS, categoryToSlug } from "@/lib/meilisearch";

export const revalidate = 300;

export const metadata: Metadata = {
  title: "カテゴリ一覧",
  description: "Shopify Liquid のリファレンス・スニペットをカテゴリから探す。",
};

export default async function CategoryIndexPage() {
  const stats = await getStats();
  const categories = Object.entries(stats.byCategory)
    .sort(([, a], [, b]) => b - a)
    .map(([name, count]) => ({
      name,
      count,
      icon: CATEGORY_ICONS[name] ?? "📦",
    }));

  return (
    <main className="max-w-6xl mx-auto px-6 py-10">
      <header className="mb-10">
        <h1 className="text-3xl font-bold mb-2">カテゴリ一覧</h1>
        <p className="text-slate-600">
          公式リファレンス(フィルター・タグ・オブジェクト)とコミュニティ実装例を、カテゴリから探す。
        </p>
      </header>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {categories.map((cat) => (
          <Link
            key={cat.name}
            href={`/category/${categoryToSlug(cat.name)}`}
            className="block p-6 border border-slate-200 rounded-lg hover:shadow-md hover:border-violet-300 transition bg-white"
          >
            <div className="text-3xl mb-3">{cat.icon}</div>
            <div className="font-bold text-slate-900 leading-tight mb-1">
              {cat.name}
            </div>
            <div className="text-sm text-slate-500">{cat.count} 件</div>
          </Link>
        ))}
      </div>
    </main>
  );
}
