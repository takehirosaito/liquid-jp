// Meilisearch クライアント & 検索ヘルパ(liquid-jp.jp 用)
//
// agent-skills.jp の lib/meilisearch.ts を参考に、liquid-jp スキーマ向けに新規実装。
// すべてサーバサイドのみで呼ばれる前提なので、LIQUID_PROD_MEILI_MASTER_KEY を直接使用
// (NEXT_PUBLIC_ プレフィックスなし、ブラウザに露出させない)

import { Meilisearch } from "meilisearch";

const host =
  process.env.LIQUID_PROD_MEILI_HOST ??
  process.env.MEILI_URL ??
  "http://127.0.0.1:7700";
const apiKey =
  process.env.LIQUID_PROD_MEILI_MASTER_KEY ??
  process.env.MEILI_MASTER_KEY ??
  "";

const client = new Meilisearch({ host, apiKey });
const index = client.index("liquid_jp");

export type Snippet = {
  id: string;
  slug: string;
  name: string;
  title_ja: string;
  description_ja: string;
  use_case_ja: string;
  where_to_paste_ja: string;
  caveats_ja: string;
  code: string;
  code_language: string;
  category: string;
  difficulty: string;
  tags: string[];
  repo_owner: string;
  repo_name: string;
  repo_url: string;
  raw_url: string;
  file_path: string;
  license: string;
  source_kind: string;
  is_reference: boolean;
  reference_kind?: string;
  reference_name?: string;
  line_count: number;
  qc_title_too_long?: boolean;
};

/** カテゴリのアイコン(絵文字、UI 用) */
export const CATEGORY_ICONS: Record<string, string> = {
  "リファレンス/フィルター": "🔧",
  "リファレンス/タグ": "🏷️",
  "リファレンス/オブジェクト": "📦",
  "ページテンプレート": "📄",
  "ヘッダー/フッター/ナビゲーション": "🧭",
  "テーマ基盤": "🏗️",
  "商品表示": "🛍️",
  "コレクション/検索": "🔍",
  "カート/チェックアウト": "🛒",
  "顧客アカウント": "👤",
  "メタフィールド/メタオブジェクト": "🧬",
  "SEO/構造化データ": "🌐",
  "UI部品": "✨",
  "API連携/JSON出力/JS統合": "🔌",
  "ユーティリティ": "🧰",
};

/** カテゴリ → URL slug 用変換(/category/[slug]) */
export function categoryToSlug(category: string): string {
  return encodeURIComponent(category.replace(/\//g, "--"));
}
export function slugToCategory(slug: string): string {
  return decodeURIComponent(slug).replace(/--/g, "/");
}

export type Stats = {
  total: number;
  byCategory: Record<string, number>;
  byDifficulty: Record<string, number>;
  byRepo: Record<string, number>;
  referenceCount: number;
  snippetCount: number;
};

export async function getStats(): Promise<Stats> {
  try {
    const facets = await index.search("", {
      facets: ["category", "difficulty", "repo_name", "is_reference"],
      limit: 0,
    });
    const byCategory = (facets.facetDistribution?.category ?? {}) as Record<string, number>;
    const byDifficulty = (facets.facetDistribution?.difficulty ?? {}) as Record<string, number>;
    const byRepo = (facets.facetDistribution?.repo_name ?? {}) as Record<string, number>;
    const isRefDist = (facets.facetDistribution?.is_reference ?? {}) as Record<string, number>;
    const total = facets.estimatedTotalHits ?? Object.values(byCategory).reduce((a, b) => a + b, 0);
    return {
      total,
      byCategory,
      byDifficulty,
      byRepo,
      referenceCount: isRefDist["true"] ?? 0,
      snippetCount: isRefDist["false"] ?? 0,
    };
  } catch {
    return {
      total: 0,
      byCategory: {},
      byDifficulty: {},
      byRepo: {},
      referenceCount: 0,
      snippetCount: 0,
    };
  }
}

export async function searchSnippets(
  query: string,
  opts: {
    category?: string;
    difficulty?: string;
    isReference?: boolean;
    limit?: number;
    offset?: number;
  } = {},
) {
  const filters: string[] = [];
  if (opts.category) filters.push(`category = "${opts.category.replace(/"/g, '\\"')}"`);
  if (opts.difficulty) filters.push(`difficulty = "${opts.difficulty}"`);
  if (typeof opts.isReference === "boolean") {
    filters.push(`is_reference = ${opts.isReference}`);
  }
  try {
    const res = await index.search(query, {
      filter: filters.length ? filters : undefined,
      facets: ["category", "difficulty", "is_reference"],
      limit: opts.limit ?? 30,
      offset: opts.offset ?? 0,
      matchingStrategy: "all",
      attributesToHighlight: ["title_ja", "description_ja"],
      highlightPreTag: "<mark>",
      highlightPostTag: "</mark>",
    });
    return {
      hits: res.hits as unknown as Snippet[],
      total: res.estimatedTotalHits ?? 0,
      facets: res.facetDistribution ?? {},
    };
  } catch {
    return { hits: [] as Snippet[], total: 0, facets: {} as Record<string, Record<string, number>> };
  }
}

export async function getSnippetById(id: string): Promise<Snippet | null> {
  // Meilisearch の id 属性は filterable ではないため、getDocument で直接取得
  try {
    const doc = await index.getDocument(id);
    return doc as unknown as Snippet;
  } catch {
    return null;
  }
}

export async function listSnippetsByCategory(
  category: string,
  opts: { limit?: number; offset?: number } = {},
) {
  try {
    const res = await index.search("", {
      filter: [`category = "${category.replace(/"/g, '\\"')}"`],
      sort: ["line_count:asc"],
      limit: opts.limit ?? 50,
      offset: opts.offset ?? 0,
    });
    return {
      hits: res.hits as unknown as Snippet[],
      total: res.estimatedTotalHits ?? 0,
    };
  } catch {
    return { hits: [] as Snippet[], total: 0 };
  }
}

export async function getFeaturedSnippets(limit: number): Promise<Snippet[]> {
  try {
    // 注目カテゴリ(リファレンス/フィルター)を中心に、行数の少ない実装例を優先
    const [refs, snippets] = await Promise.all([
      index.search("", {
        filter: [`is_reference = true`],
        sort: ["line_count:asc"],
        limit: Math.ceil(limit / 2),
      }),
      index.search("", {
        filter: [`is_reference = false`],
        sort: ["line_count:asc"],
        limit: Math.floor(limit / 2),
      }),
    ]);
    return [
      ...(refs.hits as unknown as Snippet[]),
      ...(snippets.hits as unknown as Snippet[]),
    ].slice(0, limit);
  } catch {
    return [];
  }
}

/** sitemap 用: 全件の id を取得 (ページネーション付き) */
export async function getAllSnippetIds(): Promise<{ id: string }[]> {
  const ids: { id: string }[] = [];
  const PAGE = 1000;
  try {
    for (let offset = 0; offset < 10000; offset += PAGE) {
      const res = await index.search("", {
        limit: PAGE,
        offset,
        attributesToRetrieve: ["id"],
      });
      const hits = res.hits as Array<{ id: string }>;
      ids.push(...hits.map((h) => ({ id: h.id })));
      if (hits.length < PAGE) break;
    }
  } catch {
    // sitemap 生成失敗時は空配列(静的ページのみ)
  }
  return ids;
}

export async function getRelatedSnippets(
  category: string,
  excludeId: string,
  limit: number,
): Promise<Snippet[]> {
  // id は filterable ではないので、+1 取得してクライアント側で除外する
  try {
    const res = await index.search("", {
      filter: [`category = "${category.replace(/"/g, '\\"')}"`],
      sort: ["line_count:asc"],
      limit: limit + 1,
    });
    const all = res.hits as unknown as Snippet[];
    return all.filter((s) => s.id !== excludeId).slice(0, limit);
  } catch {
    return [];
  }
}
