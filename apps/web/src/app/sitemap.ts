import type { MetadataRoute } from "next";
import { getAllSnippetIds, getStats, categoryToSlug } from "@/lib/meilisearch";

const SITE = "https://liquid-jp.jp";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const now = new Date();

  // 静的ページ
  const staticUrls: MetadataRoute.Sitemap = [
    "",
    "/category",
    "/search",
    "/about",
    "/privacy",
    "/terms",
  ].map((p) => ({
    url: `${SITE}${p}`,
    changeFrequency: "daily" as const,
    priority: p === "" ? 1.0 : 0.7,
    lastModified: now,
  }));

  // カテゴリページ
  let categoryUrls: MetadataRoute.Sitemap = [];
  try {
    const stats = await getStats();
    categoryUrls = Object.keys(stats.byCategory).map((cat) => ({
      url: `${SITE}/category/${categoryToSlug(cat)}`,
      changeFrequency: "weekly" as const,
      priority: 0.6,
      lastModified: now,
    }));
  } catch {
    // フォールバック: カテゴリ未取得時は空
  }

  // 個別スニペット
  const ids = await getAllSnippetIds();
  const snippetUrls: MetadataRoute.Sitemap = ids.map(({ id }) => ({
    url: `${SITE}/snippet/${encodeURIComponent(id)}`,
    changeFrequency: "monthly" as const,
    priority: 0.5,
    lastModified: now,
  }));

  return [...staticUrls, ...categoryUrls, ...snippetUrls];
}
