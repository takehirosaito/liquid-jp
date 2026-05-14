import Link from "next/link";
import { SearchBar } from "@/components/SearchBar";
import { SnippetCard } from "@/components/SnippetCard";
import { searchSnippets } from "@/lib/meilisearch";

export const revalidate = 60;

type SearchParams = Promise<{ q?: string; category?: string; difficulty?: string }>;

export default async function SearchPage({
  searchParams,
}: {
  searchParams: SearchParams;
}) {
  const params = await searchParams;
  const q = params.q ?? "";
  const result = await searchSnippets(q, {
    category: params.category,
    difficulty: params.difficulty,
    limit: 50,
  });

  return (
    <main className="max-w-6xl mx-auto px-6 py-10">
      <div className="mb-8">
        <SearchBar initial={q} size="lg" />
      </div>
      <div className="mb-6 flex items-baseline justify-between gap-4 flex-wrap">
        <h1 className="text-2xl font-bold">
          {q ? (
            <>
              <span className="text-violet-700">「{q}」</span> の検索結果
            </>
          ) : (
            "すべてのスニペット"
          )}
        </h1>
        <p className="text-sm text-slate-600">{result.total} 件</p>
      </div>
      {result.hits.length === 0 ? (
        <div className="py-20 text-center">
          <p className="text-slate-600 mb-4">該当する結果がありませんでした。</p>
          <Link href="/" className="text-violet-700 hover:underline">
            ホームに戻る
          </Link>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {result.hits.map((s) => (
            <SnippetCard key={s.id} snippet={s} />
          ))}
        </div>
      )}
    </main>
  );
}
