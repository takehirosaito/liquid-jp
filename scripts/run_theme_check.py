#!/usr/bin/env python
"""
22件の sections/*.liquid に対し Shopify Theme Check を実行。
ダミーテーマ最小構成を作って、その sections/ にコピー → check → 結果集計。

出力:
  - docs/phase6_check_report.md(Markdown レポート)
  - data/theme_check_raw.json(生の Theme Check 出力)
"""
import json
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "theme-check-target"
SECTIONS_SRC = ROOT / "sections"
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"


def setup_dummy_theme():
    """テーマチェックに必要な最小構成のダミーテーマを作る"""
    # 既存があればクリア(sections/ のみ)
    sec_dir = TARGET / "sections"
    if sec_dir.exists():
        shutil.rmtree(sec_dir)
    for d in (
        "layout",
        "templates",
        "sections",
        "assets",
        "config",
        "snippets",
        "locales",
    ):
        (TARGET / d).mkdir(parents=True, exist_ok=True)

    # 必要最小ファイル(Shopify テーマの validate に必要)
    (TARGET / "layout" / "theme.liquid").write_text(
        "<!DOCTYPE html>\n<html>\n<head>{{ content_for_header }}</head>\n"
        "<body>{{ content_for_layout }}</body>\n</html>\n",
        encoding="utf-8",
    )
    (TARGET / "templates" / "index.json").write_text(
        '{"sections": {}, "order": []}', encoding="utf-8"
    )
    (TARGET / "config" / "settings_schema.json").write_text(
        '[{"name":"theme_info","theme_name":"liquid-jp-check",'
        '"theme_version":"1.0.0","theme_author":"ALSEL",'
        '"theme_documentation_url":"https://liquid-jp.jp",'
        '"theme_support_email":"info@alsel.co.jp"}]',
        encoding="utf-8",
    )
    (TARGET / "config" / "settings_data.json").write_text(
        '{"current":{}}', encoding="utf-8"
    )
    (TARGET / "locales" / "en.default.json").write_text("{}", encoding="utf-8")

    # sections コピー(.bak は除外)
    count = 0
    for f in sorted(SECTIONS_SRC.glob("*.liquid")):
        shutil.copy2(f, TARGET / "sections" / f.name)
        count += 1
    return count


def run_check() -> tuple[str, str, int]:
    cmd = [
        "shopify",
        "theme",
        "check",
        "--no-color",
        "--output",
        "json",
        "--path",
        str(TARGET),
    ]
    print(f"[check] running: {' '.join(cmd)}", file=sys.stderr)
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=300,
    )
    return result.stdout, result.stderr, result.returncode


def parse_results(raw_json: str) -> list[dict]:
    """Theme Check の JSON 出力をパース"""
    try:
        return json.loads(raw_json)
    except json.JSONDecodeError as e:
        print(f"[check] JSON parse failed: {e}", file=sys.stderr)
        print(raw_json[:2000], file=sys.stderr)
        return []


def severity_label(s):
    return {0: "error", 1: "suggestion", 2: "style", "error": "error",
            "warning": "warning", "info": "info"}.get(s, str(s))


def write_report(results: list[dict], total_files: int):
    """Markdown レポート生成"""
    # results は [{path, offenses: [...]}, ...] の形式想定(Theme Check v2)
    by_file: dict[str, list] = defaultdict(list)
    severity_counter: Counter = Counter()
    check_name_counter: Counter = Counter()

    for entry in results:
        path = entry.get("path", "<unknown>")
        for off in entry.get("offenses", []):
            sev = off.get("severity", "?")
            check = off.get("check", off.get("name", "?"))
            severity_counter[severity_label(sev)] += 1
            check_name_counter[check] += 1
            by_file[Path(path).name].append(
                {
                    "severity": severity_label(sev),
                    "check": check,
                    "message": off.get("message", ""),
                    "start_row": off.get("start_row", off.get("line", -1)),
                }
            )

    lines = ["# Phase 6β: Theme Check 結果レポート", ""]
    lines.append(f"対象ファイル: {total_files} 件")
    lines.append("")
    lines.append("## サマリ")
    lines.append("")
    if not severity_counter:
        lines.append("✅ **全件エラー・警告なし**")
    else:
        lines.append("| Severity | 件数 |")
        lines.append("|---|---:|")
        for sev, n in severity_counter.most_common():
            lines.append(f"| {sev} | {n} |")
    lines.append("")
    if check_name_counter:
        lines.append("## チェック種別")
        lines.append("")
        lines.append("| チェック | 件数 |")
        lines.append("|---|---:|")
        for ck, n in check_name_counter.most_common():
            lines.append(f"| {ck} | {n} |")
        lines.append("")

    if by_file:
        lines.append("## ファイル別 detail")
        lines.append("")
        for fname in sorted(by_file.keys()):
            offenses = by_file[fname]
            lines.append(f"### `{fname}` — {len(offenses)} 件")
            lines.append("")
            lines.append("| severity | check | line | message |")
            lines.append("|---|---|---:|---|")
            for o in offenses:
                msg = o["message"].replace("|", "\\|").replace("\n", " ")
                lines.append(
                    f"| {o['severity']} | {o['check']} | {o['start_row']} | {msg[:200]} |"
                )
            lines.append("")
    else:
        lines.append(f"\n## エラー・警告なし(全 {total_files} 件クリーン)")

    out = DOCS_DIR / "phase6_check_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    return out, severity_counter, by_file


def main():
    print("[check] setup dummy theme...", file=sys.stderr)
    file_count = setup_dummy_theme()
    print(f"  copied {file_count} sections", file=sys.stderr)

    stdout, stderr, rc = run_check()
    raw_path = DATA_DIR / "theme_check_raw.json"
    raw_path.write_text(stdout, encoding="utf-8")
    if stderr.strip():
        print(f"[check] stderr:\n{stderr[:2000]}", file=sys.stderr)

    results = parse_results(stdout)
    out_md, sev_counter, by_file = write_report(results, file_count)

    print(f"\n[check] report -> {out_md}", file=sys.stderr)
    print(f"[check] raw -> {raw_path}", file=sys.stderr)
    print(f"[check] severity summary: {dict(sev_counter)}", file=sys.stderr)
    print(
        f"[check] files with issues: {len(by_file)} / {file_count}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
