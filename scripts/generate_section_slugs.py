#!/usr/bin/env python
"""
docs/section_100_list.md から 100件の英語 slug を一括生成 (Haiku 4.5、1リクエスト)。
出力: data/section_slugs.json (number, name_ja, desc_ja, slug)
"""
import json
import os
import re
import sys
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


SYSTEM = """あなたは Shopify テーマ開発のエキスパートです。
日本語のセクション名から、Shopify セクションファイル名として使う英語 slug を生成します。

# 要件
- 英小文字 + ハイフン区切り(snake_case 禁止、camelCase 禁止)
- 2〜4 単語、合計 6〜30 文字
- セクションの主要機能を端的に表現
- 100件すべてユニーク(重複禁止)
- Shopify の慣習に従う(例: hero-banner、product-grid、image-with-text、faq-accordion 等)
- 同種のセクションには接尾辞で区別(例: hero-fv-lp / hero-mobile / hero-seasonal 等)

# 出力形式
JSON 配列のみ出力。前置きやコードフェンス禁止:

[{"number":1,"slug":"hero-fv-lp"},{"number":2,"slug":"hero-mobile"}, ...]
"""


def load_sections():
    content = (ROOT / "docs/section_100_list.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", content, re.M)
    return [(int(n), name.strip(), desc.strip()) for n, name, desc in rows]


def main():
    sections = load_sections()
    print(f"[slugs] loaded {len(sections)} sections", file=sys.stderr)

    user_msg = "以下の 100 件すべてに対し、上記要件を満たす slug を生成してください。\n\n"
    for n, name, desc in sections:
        user_msg += f"{n}. {name} — {desc}\n"

    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=8000,
        system=SYSTEM,
        messages=[{"role": "user", "content": user_msg}],
    )
    text = "".join(b.text for b in resp.content if hasattr(b, "text")).strip()
    # JSON fence 除去
    text = re.sub(r"^```(?:json)?\s*", "", text).strip()
    text = re.sub(r"\s*```$", "", text).strip()
    data = json.loads(text)
    print(
        f"[slugs] parsed {len(data)} slugs, usage in={resp.usage.input_tokens} out={resp.usage.output_tokens}",
        file=sys.stderr,
    )

    # 重複処理
    slug_count: dict = {}
    for d in data:
        s = d["slug"]
        slug_count[s] = slug_count.get(s, 0) + 1
    dups = {s: c for s, c in slug_count.items() if c > 1}
    if dups:
        print(f"[slugs] WARN duplicates: {dups}", file=sys.stderr)
        seen: dict = {}
        for d in data:
            s = d["slug"]
            if slug_count[s] > 1:
                seen[s] = seen.get(s, 0) + 1
                d["slug"] = f"{s}-{seen[s]}"

    # name/desc を合体して保存
    sec_map = {n: (name, desc) for n, name, desc in sections}
    enriched = []
    for d in data:
        n = d["number"]
        name, desc = sec_map.get(n, ("", ""))
        enriched.append(
            {"number": n, "slug": d["slug"], "name_ja": name, "desc_ja": desc}
        )
    enriched.sort(key=lambda x: x["number"])

    out = ROOT / "data" / "section_slugs.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(enriched, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[slugs] wrote {len(enriched)} -> {out}", file=sys.stderr)
    print("\n=== 先頭10件 ===")
    for e in enriched[:10]:
        print(f"  {e['number']:>3}: {e['slug']:25s} ← {e['name_ja']}")
    print("\n=== 末尾5件 ===")
    for e in enriched[-5:]:
        print(f"  {e['number']:>3}: {e['slug']:25s} ← {e['name_ja']}")


if __name__ == "__main__":
    main()
