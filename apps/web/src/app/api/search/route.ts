// GET /api/search?q=<query>&limit=<n>&category=<c>&difficulty=<d>
//
// liquid-jp.jp の検索 JSON API。外部ツールや agent-skills 系から利用可能。

import { NextResponse } from "next/server";
import { searchSnippets } from "@/lib/meilisearch";

export const runtime = "nodejs";
export const revalidate = 60;

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

export function OPTIONS() {
  return new NextResponse(null, { headers: CORS });
}

export async function GET(req: Request) {
  const url = new URL(req.url);
  const q = url.searchParams.get("q") ?? "";
  const limit = Math.min(
    50,
    Math.max(1, parseInt(url.searchParams.get("limit") ?? "10", 10) || 10),
  );
  const category = url.searchParams.get("category") ?? undefined;
  const difficulty = url.searchParams.get("difficulty") ?? undefined;

  const result = await searchSnippets(q, { limit, category, difficulty });

  const hits = result.hits.map((s) => ({
    id: s.id,
    slug: s.slug,
    name: s.name,
    title_ja: s.title_ja,
    description_ja: s.description_ja,
    category: s.category,
    difficulty: s.difficulty,
    tags: s.tags,
    repo_owner: s.repo_owner,
    repo_name: s.repo_name,
    repo_url: s.repo_url,
    raw_url: s.raw_url,
    license: s.license,
    site_url: `https://liquid-jp.jp/snippet/${encodeURIComponent(s.id)}`,
  }));

  return NextResponse.json(
    { query: q, total: result.total, count: hits.length, hits },
    { headers: CORS },
  );
}
