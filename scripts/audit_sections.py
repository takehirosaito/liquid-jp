#!/usr/bin/env python
"""
sections/*.liquid 22件を解析し、修正分類を出力。
- image_tag の構文(1行詰め vs 複数行 vs assign 方式)
- alt 引数内の | escape 使用
- font-family 指定の有無
- font-weight 800/900 の使用
- 商品手動入力(product_name / product_image / product_link を schema settings に持つ)の検知
- product / collection ピッカーの使用
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS_DIR = ROOT / "sections"

# パターン定義
RE_IMAGETAG_INLINE = re.compile(
    r"\| image_tag:[^\n]*alt:[^,\n]*\| escape", re.S
)  # 1行詰めで alt: X | escape を含む(構文エラー)
RE_IMAGETAG_MULTILINE_ESCAPE = re.compile(
    r"\| image_tag:\s*\n[\s\S]+?alt:[^,]+\| escape", re.M
)  # 複数行で alt: X | escape(ベストプラクティス違反)
RE_ALT_ESCAPE_ANY = re.compile(r"alt:[^,\n}]+\|\s*escape")  # 任意の alt: X | escape
RE_FONT_FAMILY = re.compile(r"font-family\s*:\s*[^v;\n]+;")  # font-family 指定(var(--*) 除く)
RE_FONT_WEIGHT_HEAVY = re.compile(r"font-weight\s*:\s*(800|900)\b")
RE_MANUAL_PRODUCT_SETTING = re.compile(
    r'"id":\s*"product_(name|image|link|price|catchcopy)"'
)  # 手動商品入力フィールド
RE_PRODUCT_PICKER = re.compile(r'"type":\s*"product"')  # product picker
RE_COLLECTION_PICKER = re.compile(r'"type":\s*"collection"')


def analyze(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    info: dict = {
        "name": path.name,
        "lines": content.count("\n") + 1,
        # image_tag 構文
        "imagetag_inline_escape": len(RE_IMAGETAG_INLINE.findall(content)),
        "imagetag_multiline_escape": len(RE_IMAGETAG_MULTILINE_ESCAPE.findall(content)),
        "alt_escape_any": len(RE_ALT_ESCAPE_ANY.findall(content)),
        # font
        "font_family_count": len(
            [
                m
                for m in RE_FONT_FAMILY.findall(content)
                if "var(--" not in m and "inherit" not in m
            ]
        ),
        "font_weight_heavy": len(RE_FONT_WEIGHT_HEAVY.findall(content)),
        # 商品入力
        "manual_product_settings": len(set(RE_MANUAL_PRODUCT_SETTING.findall(content))),
        "uses_product_picker": bool(RE_PRODUCT_PICKER.search(content)),
        "uses_collection_picker": bool(RE_COLLECTION_PICKER.search(content)),
    }
    # 分類: 機械修正のみで足りるか、Opus 書き直しか
    needs_opus = (
        info["manual_product_settings"] >= 2  # 商品手動入力設計
        or path.name == "ranking-top-three.liquid"  # 既に問題5指摘あり、ピッカー化必須
    )
    info["category"] = "OPUS_REWRITE" if needs_opus else "MACHINE_FIX"
    return info


def main():
    sections = sorted(SECTIONS_DIR.glob("*.liquid"))
    results = [analyze(p) for p in sections]

    # サマリ
    machine = [r for r in results if r["category"] == "MACHINE_FIX"]
    opus = [r for r in results if r["category"] == "OPUS_REWRITE"]
    print(f"# 22件解析結果\n")
    print(f"- 機械修正のみ: **{len(machine)}件**")
    print(f"- Opus 書き直し対象: **{len(opus)}件**")
    print()
    print("## 全 22 件 詳細\n")
    print(
        "| ファイル | 行 | inline_esc | ml_esc | font-family | fw 800/900 | manual商品 | picker | 分類 |"
    )
    print(
        "|---|---:|---:|---:|---:|---:|---:|:---:|:---:|"
    )
    for r in results:
        picker = ""
        if r["uses_product_picker"]:
            picker += "P"
        if r["uses_collection_picker"]:
            picker += "C"
        if not picker:
            picker = "—"
        flag = "🔧" if r["category"] == "MACHINE_FIX" else "🤖"
        print(
            f"| {r['name']} | {r['lines']} | {r['imagetag_inline_escape']} | "
            f"{r['imagetag_multiline_escape']} | {r['font_family_count']} | "
            f"{r['font_weight_heavy']} | {r['manual_product_settings']} | "
            f"{picker} | {flag} {r['category'][:3]} |"
        )
    print()
    print("## Opus 書き直し対象\n")
    for r in opus:
        print(f"- `{r['name']}` (手動商品設定 {r['manual_product_settings']}件)")
    print()
    print("## 集計: 機械修正対象パターン\n")
    print(
        f"- image_tag 1行詰め + escape(構文エラー): "
        f"{sum(r['imagetag_inline_escape'] for r in results)} 箇所"
    )
    print(
        f"- image_tag 複数行 + escape(BP違反): "
        f"{sum(r['imagetag_multiline_escape'] for r in results)} 箇所"
    )
    print(f"- alt: X | escape(全パターン): {sum(r['alt_escape_any'] for r in results)} 箇所")
    print(f"- font-family 明示: {sum(r['font_family_count'] for r in results)} 箇所")
    print(f"- font-weight 800/900: {sum(r['font_weight_heavy'] for r in results)} 箇所")

    # JSON 出力
    out = ROOT / "data" / "section_audit.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[audit] -> {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
