#!/usr/bin/env python
"""
22件の .liquid に対する機械修正:
1. image_tag フィルタの `alt: X | escape` を assign 方式に統一
2. CSS の font-family 指定を削除(テーマ継承させる)
3. CSS の font-weight 800/900 を 700 に置換

修正前のオリジナルは .pre_fix.bak で保存。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS_DIR = ROOT / "sections"

# ============================================================
# image_tag の alt: ... | escape を assign 方式に置換
# ============================================================
# 戦略: image_tag フィルタを含む {{ ... }} 出力ブロックを検出し、
# 内部の `alt: <expr> | escape` を取り出して、ブロック直前に
# {%- assign __img_alt_N = <expr> | escape -%} を挿入し、
# image_tag 内の該当部分を `alt: __img_alt_N` に置換する。

OUTPUT_BLOCK_RE = re.compile(
    r"\{\{(?P<body>(?:[^{}]|\{(?!\{)|\}(?!\}))*?)\}\}",
    re.S,
)
ALT_ESCAPE_RE = re.compile(
    r"alt:\s*(?P<expr>[^|,}\n]+(?:\.[^|,}\n]+)*)\s*\|\s*escape\b"
)


def fix_image_tag_alt(content: str) -> tuple[str, int]:
    """image_tag 内の `alt: X | escape` を assign 方式に置換"""
    fixes = 0
    counter = [0]  # 連番

    def replace_block(m: re.Match) -> str:
        nonlocal fixes
        body = m.group("body")
        if "image_tag" not in body:
            return m.group(0)
        if "| escape" not in body:
            return m.group(0)
        # alt: X | escape を検出して assign に
        assigns: list[str] = []

        def replace_alt(am: re.Match) -> str:
            nonlocal fixes
            expr = am.group("expr").strip()
            counter[0] += 1
            var_name = f"__alt_{counter[0]}"
            assigns.append(f"{{%- assign {var_name} = {expr} | escape -%}}")
            fixes += 1
            return f"alt: {var_name}"

        new_body = ALT_ESCAPE_RE.sub(replace_alt, body)
        if not assigns:
            return m.group(0)
        # ブロック直前に assign を挿入
        # 周囲のインデントを保つため、簡易的に改行で並べる
        prefix = "\n".join(assigns) + "\n"
        return prefix + "{{" + new_body + "}}"

    new_content = OUTPUT_BLOCK_RE.sub(replace_block, content)
    return new_content, fixes


# ============================================================
# CSS font-family を削除(var(--*) は維持、明示指定のみ削除)
# ============================================================
# パターン: font-family: <something>; (var(--*)、inherit を含まない場合のみ)

FONT_FAMILY_RE = re.compile(r"^(\s*)font-family\s*:\s*([^;\n]+);\s*$", re.M)


def fix_font_family(content: str) -> tuple[str, int]:
    fixes = 0

    def replace(m: re.Match) -> str:
        nonlocal fixes
        value = m.group(2)
        if "var(--" in value or "inherit" in value:
            return m.group(0)
        fixes += 1
        return ""  # 行ごと削除

    new_content = FONT_FAMILY_RE.sub(replace, content)
    return new_content, fixes


# ============================================================
# font-weight 800 / 900 を 700 に
# ============================================================
FONT_WEIGHT_RE = re.compile(
    r"font-weight\s*:\s*(?P<v>800|900)\b"
)


def fix_font_weight(content: str) -> tuple[str, int]:
    fixes = 0

    def replace(m: re.Match) -> str:
        nonlocal fixes
        fixes += 1
        return "font-weight: 700"

    new_content = FONT_WEIGHT_RE.sub(replace, content)
    return new_content, fixes


# ============================================================
# main
# ============================================================
def process_file(path: Path) -> dict:
    original = path.read_text(encoding="utf-8")

    # バックアップ(初回のみ)
    bak = path.with_suffix(path.suffix + ".pre_fix.bak")
    if not bak.exists():
        bak.write_text(original, encoding="utf-8")

    content = original
    content, alt_fixes = fix_image_tag_alt(content)
    content, ff_fixes = fix_font_family(content)
    content, fw_fixes = fix_font_weight(content)

    changed = content != original
    if changed:
        path.write_text(content, encoding="utf-8")

    return {
        "name": path.name,
        "alt_escape_fixes": alt_fixes,
        "font_family_fixes": ff_fixes,
        "font_weight_fixes": fw_fixes,
        "changed": changed,
        "before_lines": original.count("\n") + 1,
        "after_lines": content.count("\n") + 1,
    }


def main():
    sections = sorted(SECTIONS_DIR.glob("*.liquid"))
    # ranking-top-three は Opus 書き直し対象。機械修正の対象から除外。
    skip = {"ranking-top-three.liquid"}
    sections = [p for p in sections if p.name not in skip]

    print(f"# 機械修正実行({len(sections)} 件、ranking-top-three は除外)\n")
    print("| file | alt 修正 | font-family 削除 | fw800/900→700 | 行数 |")
    print("|---|---:|---:|---:|---|")
    totals = {"alt_escape_fixes": 0, "font_family_fixes": 0, "font_weight_fixes": 0}
    for p in sections:
        r = process_file(p)
        for k in totals:
            totals[k] += r[k]
        line_change = (
            f"{r['before_lines']}→{r['after_lines']}"
            if r["before_lines"] != r["after_lines"]
            else str(r["before_lines"])
        )
        print(
            f"| {r['name']} | {r['alt_escape_fixes']} | {r['font_family_fixes']} | {r['font_weight_fixes']} | {line_change} |"
        )

    print()
    print(f"## 合計修正箇所")
    print(f"- alt: X | escape → assign: **{totals['alt_escape_fixes']}** 箇所")
    print(f"- font-family 削除: **{totals['font_family_fixes']}** 箇所")
    print(f"- font-weight 800/900 → 700: **{totals['font_weight_fixes']}** 箇所")
    print(f"\nバックアップ: 各ファイルの隣に .pre_fix.bak で保存", file=sys.stderr)


if __name__ == "__main__":
    main()
