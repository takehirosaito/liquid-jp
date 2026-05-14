import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import {
  listSnippetsByCategory,
  slugToCategory,
  categoryToSlug,
  CATEGORY_ICONS,
} from "@/lib/meilisearch";
import { SnippetCard } from "@/components/SnippetCard";

export const revalidate = 3600;

type Params = Promise<{ slug: string }>;

export async function generateMetadata({
  params,
}: {
  params: Params;
}): Promise<Metadata> {
  const { slug } = await params;
  const category = slugToCategory(slug);
  return {
    title: `${category} のスニペット一覧`,
    description: `Shopify Liquid の「${category}」カテゴリに属するリファレンス・スニペット一覧。`,
  };
}

export default async function CategoryPage({
  params,
}: {
  params: Params;
}) {
  const { slug } = await params;
  const category = slugToCategory(slug);
  const { hits, total } = await listSnippetsByCategory(category, { limit: 100 });
  if (total === 0) notFound();

  const icon = CATEGORY_ICONS[category] ?? "📦";

  return (
    <main className="max-w-6xl mx-auto px-6 py-10">
      <nav className="text-sm text-slate-500 mb-4 flex items-center gap-2 flex-wrap">
        <Link href="/" className="hover:text-violet-700">ホーム</Link>
        <span>/</span>
        <Link href="/category" className="hover:text-violet-700">カテゴリ</Link>
        <span>/</span>
        <span className="text-slate-700">{category}</span>
      </nav>
      <header className="mb-8">
        <div className="text-4xl mb-3">{icon}</div>
        <h1 className="text-3xl font-bold mb-2">{category}</h1>
        <p className="text-slate-600">{total} 件のスニペット・リファレンス</p>
      </header>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {hits.map((s) => (
          <SnippetCard key={s.id} snippet={s} />
        ))}
      </div>
      {/* SEO 用に逆参照リンクも置く(slug が同じになることの確認) */}
      <p className="sr-only">
        <Link href={`/category/${categoryToSlug(category)}`}>このページ</Link>
      </p>
    </main>
  );
}
