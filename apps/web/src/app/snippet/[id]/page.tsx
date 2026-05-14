import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import hljs from "highlight.js";
import {
  getSnippetById,
  getRelatedSnippets,
  CATEGORY_ICONS,
  categoryToSlug,
} from "@/lib/meilisearch";
import { SnippetCard } from "@/components/SnippetCard";

export const revalidate = 86400;

type Params = Promise<{ id: string }>;

export async function generateMetadata({
  params,
}: {
  params: Params;
}): Promise<Metadata> {
  const { id } = await params;
  const snippet = await getSnippetById(decodeURIComponent(id));
  if (!snippet) {
    return { title: "見つかりません" };
  }
  const title = snippet.title_ja || snippet.name;
  const desc = snippet.description_ja || `${snippet.name} のリファレンス`;
  return {
    title,
    description: desc.slice(0, 160),
    openGraph: {
      title,
      description: desc.slice(0, 160),
      type: "article",
    },
  };
}

function highlightCode(code: string, language: string): string {
  // Liquid は highlight.js に専用言語定義がないため、HTML として解析する
  // (Liquid タグ `{% %}` や Liquid 出力 `{{ }}` も HTML 内のテキストとして表示される)
  const lang = language === "json" ? "json" : "html";
  try {
    return hljs.highlight(code, { language: lang }).value;
  } catch {
    return code
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }
}

export default async function SnippetDetailPage({
  params,
}: {
  params: Params;
}) {
  const { id } = await params;
  const snippet = await getSnippetById(decodeURIComponent(id));
  if (!snippet) notFound();

  const related = await getRelatedSnippets(snippet.category, snippet.id, 6);
  const icon = CATEGORY_ICONS[snippet.category] ?? "📦";
  const codeLang = snippet.code_language || "html";
  const highlighted = highlightCode(snippet.code, codeLang);

  // JSON-LD Article
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: snippet.title_ja || snippet.name,
    description: snippet.description_ja,
    author: { "@type": "Organization", name: snippet.repo_owner },
    publisher: {
      "@type": "Organization",
      name: "ALSEL",
      logo: { "@type": "ImageObject", url: "https://liquid-jp.jp/logo.svg" },
    },
    inLanguage: "ja",
    isAccessibleForFree: true,
    license: snippet.license,
    url: `https://liquid-jp.jp/snippet/${encodeURIComponent(snippet.id)}`,
  };

  return (
    <main className="max-w-4xl mx-auto px-6 py-10">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />

      {/* パンくず */}
      <nav className="text-sm text-slate-500 mb-6 flex items-center gap-2 flex-wrap">
        <Link href="/" className="hover:text-violet-700">ホーム</Link>
        <span>/</span>
        <Link
          href={`/category/${categoryToSlug(snippet.category)}`}
          className="hover:text-violet-700"
        >
          {snippet.category}
        </Link>
        <span>/</span>
        <span className="text-slate-700">{snippet.name}</span>
      </nav>

      {/* ヘッダー */}
      <header className="mb-8">
        <div className="flex items-center gap-2 mb-3 flex-wrap">
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
        <h1 className="text-3xl md:text-4xl font-bold tracking-tight text-slate-900 mb-3">
          {snippet.title_ja || snippet.name}
        </h1>
        <p className="text-lg text-slate-700 leading-relaxed">
          {snippet.description_ja}
        </p>
      </header>

      {/* メタ情報グリッド */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8 p-4 bg-slate-50 rounded-lg text-sm">
        <div>
          <div className="text-xs text-slate-500 mb-1">用途</div>
          <div className="text-slate-800">{snippet.use_case_ja || "—"}</div>
        </div>
        <div>
          <div className="text-xs text-slate-500 mb-1">設置場所</div>
          <div className="text-slate-800">{snippet.where_to_paste_ja || "—"}</div>
        </div>
        <div>
          <div className="text-xs text-slate-500 mb-1">注意点</div>
          <div className="text-slate-800">{snippet.caveats_ja || "—"}</div>
        </div>
      </section>

      {/* タグ */}
      {snippet.tags && snippet.tags.length > 0 && (
        <section className="mb-8 flex items-center gap-2 flex-wrap">
          <span className="text-xs text-slate-500">タグ:</span>
          {snippet.tags.map((t) => (
            <span
              key={t}
              className="text-xs px-2 py-0.5 bg-violet-50 text-violet-700 rounded-full"
            >
              {t}
            </span>
          ))}
        </section>
      )}

      {/* コード */}
      <section className="mb-8">
        <div className="flex items-baseline justify-between mb-2">
          <h2 className="text-lg font-bold text-slate-900">
            {snippet.is_reference ? "仕様" : "コード"}
          </h2>
          <span className="text-xs text-slate-500">
            {snippet.line_count} 行 / {codeLang}
          </span>
        </div>
        <pre className="hljs"><code dangerouslySetInnerHTML={{ __html: highlighted }} /></pre>
      </section>

      {/* 出典・ライセンス */}
      <section className="mb-12 p-4 border border-slate-200 rounded-lg bg-white">
        <h2 className="text-sm font-bold text-slate-900 mb-3">出典・ライセンス</h2>
        <dl className="text-sm space-y-2">
          <div className="flex gap-2 flex-wrap">
            <dt className="text-slate-500 w-24 shrink-0">Source:</dt>
            <dd>
              <a
                href={snippet.raw_url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-violet-700 hover:underline break-all"
              >
                {snippet.repo_owner}/{snippet.repo_name}/{snippet.file_path}
              </a>
            </dd>
          </div>
          <div className="flex gap-2 flex-wrap">
            <dt className="text-slate-500 w-24 shrink-0">Repository:</dt>
            <dd>
              <a
                href={snippet.repo_url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-violet-700 hover:underline"
              >
                {snippet.repo_url}
              </a>
            </dd>
          </div>
          <div className="flex gap-2 flex-wrap">
            <dt className="text-slate-500 w-24 shrink-0">License:</dt>
            <dd className="text-slate-800">{snippet.license}</dd>
          </div>
        </dl>
        <p className="text-xs text-slate-500 mt-4 leading-relaxed">
          このコードは {snippet.repo_owner} 著作の MIT ライセンスソースです。
          原本の著作権は {snippet.repo_owner} が保有します。日本語訳は ALSEL によるものです。
        </p>
      </section>

      {/* 関連スニペット */}
      {related.length > 0 && (
        <section>
          <h2 className="text-2xl font-bold mb-4">関連項目</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {related.map((s) => (
              <SnippetCard key={s.id} snippet={s} />
            ))}
          </div>
        </section>
      )}
    </main>
  );
}
