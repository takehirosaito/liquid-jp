#!/usr/bin/env python
"""
22 セクションを Meilisearch 投入用 JSONL に変換。

- id プレフィックス「alsel-」
- category「ALSEL監修セクション(ベータ)」
- difficulty「★★★(中)」
- license「ALSEL Original」
- セクション冒頭の {% comment %} ブロックから用途・設置場所・カスタマイズポイント・注意点を抽出

出力:
  data/alsel_index.jsonl
  data/alsel_index.settings.json(既存 build_meili_index.py の SETTINGS 流用)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS_DIR = ROOT / "sections"
DATA_DIR = ROOT / "data"

CATEGORY = "ALSEL監修セクション(ベータ)"
LICENSE = "ALSEL Original"
DIFFICULTY = "中級"  # 「素人でも導入可能」レベル、表記★★★


def load_slug_map():
    """data/section_slugs.json から slug→{number,name_ja,desc_ja} を返す"""
    data = json.loads((DATA_DIR / "section_slugs.json").read_text(encoding="utf-8"))
    return {d["slug"]: d for d in data}


COMMENT_BLOCK_RE = re.compile(r"\{%\s*comment\s*%\}([\s\S]*?)\{%\s*endcomment\s*%\}", re.S)
KV_RE = re.compile(r"^\s*([^:\n]+?):\s*(.+?)\s*$", re.M)
PRESET_NAME_RE = re.compile(r'"presets"\s*:\s*\[\s*\{[^}]*?"name"\s*:\s*"([^"]+)"', re.S)
TAGS_RE = re.compile(r'"blocks"\s*:\s*\[', re.S)


def parse_comment_block(content: str) -> dict:
    """冒頭 {% comment %} から構造化フィールドを抽出"""
    m = COMMENT_BLOCK_RE.search(content)
    if not m:
        return {}
    body = m.group(1)
    info = {}
    # 行ごとに「キー: 値」を抽出
    section_name = ""
    use_case = ""
    place = ""
    custom = []
    caveats = []
    version = ""
    license_ja = ""

    state = None
    for line in body.split("\n"):
        line = line.rstrip()
        if "セクション名:" in line:
            section_name = line.split("セクション名:", 1)[1].strip()
            state = None
        elif "用途:" in line:
            use_case = line.split("用途:", 1)[1].strip()
            state = "use_case"
        elif "推奨設置場所:" in line:
            place = line.split("推奨設置場所:", 1)[1].strip()
            state = "place"
        elif "カスタマイズポイント:" in line:
            state = "custom"
        elif "注意点:" in line:
            state = "caveats"
        elif "動作確認バージョン:" in line:
            version = line.split("動作確認バージョン:", 1)[1].strip()
            state = None
        elif "ライセンス:" in line:
            license_ja = line.split("ライセンス:", 1)[1].strip()
            state = None
        elif line.lstrip().startswith("- ") and state == "custom":
            custom.append(line.lstrip()[2:])
        elif line.lstrip().startswith("- ") and state == "caveats":
            caveats.append(line.lstrip()[2:])

    info["section_name"] = section_name
    info["use_case"] = use_case
    info["place"] = place
    info["custom_points"] = custom
    info["caveats"] = caveats
    info["version"] = version
    info["license_ja"] = license_ja
    return info


def build_doc(slug: str, content: str, slug_map: dict) -> dict:
    meta = slug_map.get(slug, {})
    parsed = parse_comment_block(content)
    preset_m = PRESET_NAME_RE.search(content)
    preset_name = preset_m.group(1) if preset_m else f"ALSEL監修 / {parsed.get('section_name', slug)}"
    has_blocks = bool(TAGS_RE.search(content))

    title_ja = parsed.get("section_name") or meta.get("name_ja") or slug
    desc_ja = parsed.get("use_case") or meta.get("desc_ja") or ""

    return {
        "id": f"alsel-{slug}",
        "slug": f"alsel-{slug}",
        "name": f"{slug}.liquid",
        "title_ja": title_ja,
        "description_ja": desc_ja,
        "use_case_ja": parsed.get("use_case", ""),
        "where_to_paste_ja": parsed.get("place", ""),
        "caveats_ja": " / ".join(parsed.get("caveats", [])),
        "custom_points": parsed.get("custom_points", []),
        "code": content,
        "code_language": "liquid",
        "category": CATEGORY,
        "difficulty": DIFFICULTY,
        "tags": ["alsel-original", "shopify-section", "online-store-2"]
        + (["with-blocks"] if has_blocks else []),
        "repo_owner": "ALSEL",
        "repo_name": "liquid-jp",
        "repo_url": "https://github.com/takehirosaito/liquid-jp",
        "raw_url": f"https://github.com/takehirosaito/liquid-jp/blob/main/sections/{slug}.liquid",
        "file_path": f"sections/{slug}.liquid",
        "license": LICENSE,
        "source_kind": "alsel_section",
        "is_reference": False,
        "reference_kind": "",
        "reference_name": "",
        "line_count": content.count("\n") + 1,
        "size_bytes": len(content.encode("utf-8")),
        "preset_name": preset_name,
        "compatible_version": parsed.get("version", "Online Store 2.0"),
        "qc_title_too_long": len(title_ja) > 30,
        "is_alsel_original": True,
    }


def main():
    slug_map = load_slug_map()
    sections = sorted(SECTIONS_DIR.glob("*.liquid"))
    print(f"[alsel-index] {len(sections)} 件を処理", file=sys.stderr)

    out = DATA_DIR / "alsel_index.jsonl"
    settings_out = DATA_DIR / "alsel_index.settings.json"
    docs = []
    with out.open("w", encoding="utf-8") as f:
        for p in sections:
            content = p.read_text(encoding="utf-8")
            doc = build_doc(p.stem, content, slug_map)
            docs.append(doc)
            f.write(json.dumps(doc, ensure_ascii=False) + "\n")

    # settings は既存 build_meili_index.py の SETTINGS を流用(同じ index に投入する想定)
    try:
        import build_meili_index as bmi  # type: ignore
        sys.path.insert(0, str(ROOT / "scripts"))
        settings_out.write_text(
            json.dumps(bmi.SETTINGS, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    except Exception:
        pass

    print(f"[alsel-index] wrote {len(docs)} -> {out}", file=sys.stderr)
    # 簡易サマリ
    cats = set(d["category"] for d in docs)
    blocks = sum(1 for d in docs if "with-blocks" in d["tags"])
    too_long = sum(1 for d in docs if d["qc_title_too_long"])
    print(f"  categories: {cats}", file=sys.stderr)
    print(f"  with blocks: {blocks}", file=sys.stderr)
    print(f"  title-too-long: {too_long}", file=sys.stderr)


if __name__ == "__main__":
    main()
