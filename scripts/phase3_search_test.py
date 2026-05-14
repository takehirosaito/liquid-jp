#!/usr/bin/env python
"""
Phase 3 ブロック1: Railway Meilisearch に 10 クエリを投げて品質を実機確認。
各クエリ TOP5 を「日本語タイトル / 英ファイル名 / カテゴリ / スコア」で出力。
"""
import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import requests

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

URL = os.environ["LIQUID_PROD_MEILI_HOST"]
KEY = os.environ["LIQUID_PROD_MEILI_MASTER_KEY"]
INDEX = "liquid_jp"

QUERIES = [
    "カート",
    "コレクション内ソート",
    "商品バリエーション",
    "カスタム404",
    "ページネーション",
    "在庫切れ",
    "日付フォーマット",
    "ヘッダー",
    "検索ボックス",
    "メタフィールド",
]


def search(q):
    r = requests.post(
        f"{URL}/indexes/{INDEX}/search",
        headers={
            "Authorization": f"Bearer {KEY}",
            "Content-Type": "application/json",
        },
        json={"q": q, "limit": 5, "showRankingScore": True},
        timeout=20,
    )
    r.raise_for_status()
    return r.json()


def main():
    out = ROOT / "docs" / "phase3_search_quality.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    lines.append("# Phase 3 ブロック1: 検索品質の実機確認")
    lines.append("")
    lines.append(f"対象: Meilisearch on Railway / index `{INDEX}` / 投入 683 docs")
    lines.append("")
    raw_results = []
    for q in QUERIES:
        try:
            res = search(q)
        except Exception as e:
            lines.append(f"## クエリ: `{q}`\n\nERROR: {e}\n")
            raw_results.append({"query": q, "error": str(e), "hits": []})
            continue
        hits = res.get("hits", [])
        total = res.get("estimatedTotalHits", 0)
        print(f"=== `{q}` ({len(hits)} hits, ~{total} estimated) ===", file=sys.stderr)
        lines.append(f"## クエリ: `{q}` (推定 {total} 件)")
        lines.append("")
        if not hits:
            lines.append("**ヒットなし**")
            lines.append("")
        else:
            lines.append("| # | スコア | 日本語タイトル | ファイル名 | カテゴリ |")
            lines.append("|---|---:|---|---|---|")
            for i, h in enumerate(hits[:5], 1):
                score = h.get("_rankingScore", 0.0)
                title = h.get("title_ja", "")
                name = h.get("name", "")
                cat = h.get("category", "")
                lines.append(f"| {i} | {score:.3f} | {title} | `{name}` | {cat} |")
                print(f"  [{i}] {score:.3f} {title} ({name}) - {cat}", file=sys.stderr)
            lines.append("")
        raw_results.append({"query": q, "hits": hits, "total": total})

    out.write_text("\n".join(lines), encoding="utf-8")
    raw_out = ROOT / "data" / "phase3_search_raw.json"
    raw_out.write_text(
        json.dumps(raw_results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\n[search] wrote -> {out}", file=sys.stderr)
    print(f"[search] raw -> {raw_out}", file=sys.stderr)


if __name__ == "__main__":
    main()
