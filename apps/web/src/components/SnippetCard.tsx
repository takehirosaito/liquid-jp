import Link from "next/link";
import type { Snippet } from "@/lib/meilisearch";
import { CATEGORY_ICONS } from "@/lib/meilisearch";

export function SnippetCard({ snippet }: { snippet: Snippet }) {
  const icon = CATEGORY_ICONS[snippet.category] ?? "📦";
  return (
    <Link
      href={`/snippet/${encodeURIComponent(snippet.id)}`}
      className="block p-6 border border-slate-200 rounded-lg hover:shadow-lg hover:border-violet-300 transition bg-white"
    >
      <div className="flex items-center gap-2 mb-2 flex-wrap">
        {snippet.is_reference && (
          <span className="text-xs px-2 py-0.5 rounded-full font-bold text-violet-700 bg-violet-50 border border-violet-200">
            📘 公式リファレンス
          </span>
        )}
        <span className="text-xs px-2 py-0.5 bg-slate-100 rounded-full text-slate-700">
          {icon} {snippet.category}
        </span>
        {snippet.difficulty && (
          <span className="text-xs px-2 py-0.5 bg-amber-50 text-amber-700 rounded-full">
            {snippet.difficulty}
          </span>
        )}
      </div>
      <h3 className="font-bold text-lg mb-2 line-clamp-2 text-slate-900">
        {snippet.title_ja || snippet.name}
      </h3>
      <p className="text-sm text-slate-600 line-clamp-3 leading-relaxed">
        {snippet.description_ja}
      </p>
      <div className="mt-3 text-xs text-slate-500 flex items-center gap-2 flex-wrap">
        <span>📁 {snippet.repo_name}</span>
        <span className="text-slate-300">·</span>
        <span>{snippet.license}</span>
        {snippet.line_count > 0 && (
          <>
            <span className="text-slate-300">·</span>
            <span>{snippet.line_count} 行</span>
          </>
        )}
      </div>
    </Link>
  );
}
