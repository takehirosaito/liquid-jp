import { ImageResponse } from "next/og";
import { getStats } from "@/lib/meilisearch";

export const runtime = "nodejs";
export const revalidate = 300;
export const alt =
  "Liquid Snippets by ALSEL — 日本初の Shopify Liquid 日本語リファレンス";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default async function OgImage() {
  const stats = await getStats();
  const count = stats.total > 0 ? stats.total.toLocaleString() : "640";

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          background:
            "linear-gradient(135deg, #f5f3ff 0%, #ddd6fe 50%, #c4b5fd 100%)",
          fontFamily: "sans-serif",
          padding: 72,
          boxSizing: "border-box",
        }}
      >
        {/* タグライン */}
        <div
          style={{
            display: "flex",
            fontSize: 26,
            color: "#6d28d9",
            letterSpacing: "0.25em",
            marginBottom: 12,
            fontWeight: 700,
          }}
        >
          LIQUID SNIPPETS BY ALSEL
        </div>

        {/* メインコピー */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            fontSize: 72,
            fontWeight: 800,
            color: "#0f172a",
            letterSpacing: "-0.04em",
            lineHeight: 1.15,
            marginTop: 16,
          }}
        >
          <span>日本初の</span>
          <span>
            <span style={{ color: "#6d28d9" }}>Shopify Liquid</span>
          </span>
          <span>日本語リファレンス。</span>
        </div>

        {/* サブコピー */}
        <div
          style={{
            display: "flex",
            fontSize: 30,
            color: "#475569",
            marginTop: 32,
            lineHeight: 1.4,
          }}
        >
          公式ドキュメント完全カバー + コミュニティ実装例
        </div>

        {/* スペーサー */}
        <div style={{ flex: 1, display: "flex" }} />

        {/* 件数カード + URL */}
        <div
          style={{
            display: "flex",
            alignItems: "flex-end",
            justifyContent: "space-between",
            width: "100%",
          }}
        >
          <div
            style={{
              display: "flex",
              alignItems: "flex-end",
              gap: 14,
            }}
          >
            <div
              style={{
                display: "flex",
                fontSize: 84,
                fontWeight: 800,
                color: "#6d28d9",
                letterSpacing: "-0.04em",
                lineHeight: 1,
              }}
            >
              {count}
            </div>
            <div
              style={{
                display: "flex",
                fontSize: 28,
                color: "#475569",
                paddingBottom: 10,
              }}
            >
              件の検索可能データベース
            </div>
          </div>
          <div
            style={{
              display: "flex",
              fontSize: 26,
              color: "#6d28d9",
              fontWeight: 700,
              paddingBottom: 10,
            }}
          >
            liquid-jp.jp
          </div>
        </div>
      </div>
    ),
    { ...size },
  );
}
