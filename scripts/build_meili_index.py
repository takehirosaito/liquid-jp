#!/usr/bin/env python
"""
translated jsonl から Meilisearch インポート用 JSON Lines を生成。
agent-skills.jp のスキーマと似た形式で、Liquid 用に最適化。
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# slug 生成用: 英数字とハイフンのみ、最大 80 文字
_SLUG_BAD = re.compile(r"[^a-z0-9]+")


def make_slug(rec):
    """Meilisearch 表示用の URL スラッグ"""
    rid = rec.get("id", "")
    # ref-filters-money / comm-Shopify-skeleton-theme-1a3fea12 → 短く整える
    if rid.startswith("ref-"):
        return rid.lower()
    # comm- は repo + sha 部分
    repo = (rec.get("repo_name", "") or "").lower()
    file_name = (rec.get("file_name", "") or "").lower()
    base = f"{repo}/{file_name}"
    base = _SLUG_BAD.sub("-", base).strip("-")
    return base[:80] or rid.lower()


def to_meili_doc(rec):
    """1レコードを Meilisearch ドキュメントに変換"""
    t = rec.get("translation") or {}
    error = rec.get("error")
    if error or not t:
        return None  # 翻訳失敗は除外

    is_ref = rec["source_kind"].startswith("reference")
    tags = t.get("tags", []) or []
    if not isinstance(tags, list):
        tags = [tags]
    tags = [x for x in tags if isinstance(x, str)]

    qc_flag = "title-too-long" in tags
    display_tags = [t for t in tags if t != "title-too-long"]

    doc = {
        # 識別
        "id": rec["id"].replace(".", "-").replace("/", "-"),  # Meilisearch ID は ASCII+_-
        "slug": make_slug(rec),
        # 表示
        "name": rec.get("file_name", ""),
        "title_ja": t.get("title_ja", ""),
        "description_ja": t.get("description_ja", ""),
        "use_case_ja": t.get("use_case_ja", ""),
        "where_to_paste_ja": t.get("where_to_paste_ja", ""),
        "caveats_ja": t.get("caveats_ja", ""),
        "code": rec.get("code", ""),
        "code_language": "json" if is_ref else "liquid",
        # 分類
        "category": t.get("category", ""),
        "difficulty": t.get("difficulty", ""),
        "tags": display_tags,
        # 出典
        "repo_owner": rec.get("repo_owner", ""),
        "repo_name": rec.get("repo_name", ""),
        "repo_url": rec.get("repo_url", ""),
        "raw_url": rec.get("raw_url", ""),
        "file_path": rec.get("file_path", ""),
        "license": rec.get("license", ""),
        # ソース種別
        "source_kind": rec.get("source_kind", ""),
        "is_reference": is_ref,
        "reference_kind": rec.get("reference_kind", ""),
        "reference_name": rec.get("reference_name", ""),
        # 指標
        "line_count": rec.get("line_count", 0),
        "size_bytes": rec.get("size_bytes", 0),
        # QC フラグ(Phase 2 完了後の手動レビュー用)
        "qc_title_too_long": qc_flag,
    }
    return doc


# 検索設定(push_to_meili.py で適用するため別出力)
SETTINGS = {
    "searchableAttributes": [
        "title_ja",
        "description_ja",
        "use_case_ja",
        "caveats_ja",
        "name",
        "category",
        "tags",
        "reference_name",
    ],
    "filterableAttributes": [
        "category",
        "difficulty",
        "tags",
        "license",
        "source_kind",
        "is_reference",
        "reference_kind",
        "repo_name",
        "repo_owner",
        "qc_title_too_long",
    ],
    "sortableAttributes": [
        "line_count",
        "size_bytes",
    ],
    "rankingRules": [
        "words",
        "typo",
        "proximity",
        "attribute",
        "sort",
        "exactness",
    ],
    "displayedAttributes": [
        "id",
        "slug",
        "name",
        "title_ja",
        "description_ja",
        "use_case_ja",
        "where_to_paste_ja",
        "caveats_ja",
        "code",
        "code_language",
        "category",
        "difficulty",
        "tags",
        "repo_owner",
        "repo_name",
        "repo_url",
        "raw_url",
        "file_path",
        "license",
        "source_kind",
        "is_reference",
        "reference_kind",
        "reference_name",
        "line_count",
        "qc_title_too_long",
    ],
    "synonyms": {
        # 検索シノニム(agent-skills.jp と整合)
        "ec": ["e-commerce", "ecommerce", "イーコマース"],
        "shopify": ["ショッピファイ", "Shopify"],
        "liquid": ["Liquid", "リキッド"],
        "filter": ["フィルター", "フィルタ"],
        "tag": ["タグ"],
        "object": ["オブジェクト"],
        "snippet": ["スニペット"],
        "section": ["セクション"],
        "cart": ["カート", "ショッピングカート"],
        "checkout": ["チェックアウト"],
        "metafield": ["メタフィールド"],
        "metaobject": ["メタオブジェクト"],
        "json-ld": ["jsonld", "structured-data", "構造化データ"],
        "seo": ["SEO", "検索最適化"],
    },
    "typoTolerance": {
        "enabled": True,
        "minWordSizeForTypos": {"oneTypo": 4, "twoTypos": 8},
    },
    "pagination": {
        "maxTotalHits": 10000,
    },
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="translated jsonl path")
    parser.add_argument("--out", required=True, help="meili index jsonl output")
    parser.add_argument(
        "--settings-out",
        default=None,
        help="検索設定 JSON 出力先(default: <out>.settings.json)",
    )
    args = parser.parse_args()
    src = ROOT / args.src
    out = ROOT / args.out
    settings_out = (
        ROOT / args.settings_out
        if args.settings_out
        else out.with_suffix(".settings.json")
    )
    out.parent.mkdir(parents=True, exist_ok=True)

    total = 0
    written = 0
    skipped_error = 0
    id_counts: dict = {}
    id_collisions: list = []
    with src.open(encoding="utf-8") as fin, out.open("w", encoding="utf-8") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            total += 1
            doc = to_meili_doc(rec)
            if doc is None:
                skipped_error += 1
                continue
            # id 衝突時は連番付与(2回目以降を -2, -3 ...)
            base_id = doc["id"]
            n = id_counts.get(base_id, 0) + 1
            id_counts[base_id] = n
            if n > 1:
                doc["id"] = f"{base_id}-{n}"
                doc["slug"] = f"{doc.get('slug', base_id)}-{n}"
                id_collisions.append({"base_id": base_id, "new_id": doc["id"]})
            fout.write(json.dumps(doc, ensure_ascii=False) + "\n")
            written += 1

    if id_collisions:
        print(
            f"[meili] id collisions resolved with suffix: {len(id_collisions)}",
            file=sys.stderr,
        )
        for c in id_collisions:
            print(f"  - {c['base_id']} → {c['new_id']}", file=sys.stderr)

    settings_out.write_text(
        json.dumps(SETTINGS, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        f"[meili] total={total} written={written} skipped_error={skipped_error}",
        file=sys.stderr,
    )
    print(f"[meili] wrote -> {out}", file=sys.stderr)
    print(f"[meili] settings -> {settings_out}", file=sys.stderr)


if __name__ == "__main__":
    main()
