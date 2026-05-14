#!/usr/bin/env python
"""
緊急ライセンス監査: 採用リポジトリの LICENSE 本文を取得し、
Shopify 系制限句や非標準ライセンスを検出する。
"""
import argparse
import base64
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

TOKEN = os.environ["GITHUB_TOKEN"]
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

# 採用12リポジトリ + 参考(Dawn / Horizon)+ 関連 Shopify 公式テーマ
REPOS = [
    # === 採用12リポジトリ(Phase 1〜2 で実際にデータ取得済み) ===
    "Shopify/skeleton-theme",
    "Shopify/mcliquid-theme",
    "Shopify/liquid",
    "Shopify/theme-tools",
    "Shopify/theme-liquid-docs",
    "kondasoft/ks-bootshop",
    "mirceapiturca/Sections",
    "vikrantnegi/shopify-code-snippets",
    "pgrimaud/shopify-snippets",
    "freakdesign/shopify-code-snippets",
    "instantcommerce/shopify-headless-theme",
    "uicrooks/shopify-theme-lab",
    # === 参考: 既に除外したが念のため再確認 ===
    "Shopify/dawn",
    "Shopify/horizon",
    # === 参考: Phase 4 候補として有名な Shopify 公式テーマ ===
    "Shopify/refresh",
    "Shopify/sense",
    "Shopify/craft",
    "Shopify/studio",
    "Shopify/origin",
]

# Shopify 独自制限の検出パターン(LICENSE 本文を小文字化して部分一致)
SHOPIFY_RESTRICTION_PATTERNS = [
    "integrate or interoperate with shopify",
    "develop themes that integrate",
    "all other uses of the software are strictly prohibited",
    "all other uses of the software are prohibited",
    "shopify software or services",
    "themes that integrate or interoperate",
    "for the development of shopify",
    "for use with shopify",
]

# 一般的に「翻訳して第三者サイトで再配布」可能なライセンス
PERMISSIVE_OK = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "0BSD", "CC0-1.0", "CC-BY-4.0", "ISC", "Unlicense"}


def fetch_license(repo: str) -> dict:
    """1リポジトリの LICENSE を取得し、判定する"""
    try:
        # repo metadata で archived 等も取得
        meta = requests.get(
            f"https://api.github.com/repos/{repo}", headers=HEADERS, timeout=30
        ).json()
        if "full_name" not in meta:
            return {"repo": repo, "error": meta.get("message", "repo not found")}

        # LICENSE 本文取得
        r = requests.get(
            f"https://api.github.com/repos/{repo}/license", headers=HEADERS, timeout=30
        )
        if r.status_code == 404:
            return {
                "repo": repo,
                "spdx_id": "NONE",
                "license_name": "(LICENSE ファイルなし)",
                "content": "",
                "restriction_hits": [],
                "verdict": "NO_LICENSE",
                "archived": meta.get("archived", False),
                "stars": meta.get("stargazers_count", 0),
                "html_url": meta.get("html_url", ""),
            }
        if r.status_code != 200:
            return {"repo": repo, "error": f"HTTP {r.status_code}: {r.text[:200]}"}

        data = r.json()
        spdx = (data.get("license") or {}).get("spdx_id", "unknown")
        name = (data.get("license") or {}).get("name", "unknown")
        path = data.get("path", "")
        content_b64 = data.get("content", "")
        try:
            content = base64.b64decode(content_b64).decode("utf-8", errors="replace")
        except Exception:
            content = ""

        # 制限句チェック(小文字一致)
        lower = content.lower()
        hits = [p for p in SHOPIFY_RESTRICTION_PATTERNS if p in lower]

        # 判定
        if hits:
            verdict = "RESTRICTED"
        elif spdx in PERMISSIVE_OK:
            verdict = "OK"
        elif spdx in ("Other", "NOASSERTION", "unknown") or not spdx:
            verdict = "REVIEW"
        else:
            verdict = "REVIEW"  # GPL/AGPL 等のコピーレフトも要レビュー

        return {
            "repo": repo,
            "spdx_id": spdx,
            "license_name": name,
            "license_path": path,
            "content": content,
            "restriction_hits": hits,
            "verdict": verdict,
            "archived": meta.get("archived", False),
            "stars": meta.get("stargazers_count", 0),
            "default_branch": meta.get("default_branch", ""),
            "html_url": meta.get("html_url", ""),
            "license_url": f"{meta.get('html_url', '')}/blob/{meta.get('default_branch', 'main')}/{path}",
        }
    except Exception as e:
        return {"repo": repo, "error": str(e)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/license_audit_raw.json")
    args = parser.parse_args()
    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)

    print(f"[audit] checking {len(REPOS)} repositories...", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch_license, REPOS))

    # サマリ
    print("\n=== 判定サマリ ===", file=sys.stderr)
    for r in results:
        if "error" in r:
            print(f"  ERROR  {r['repo']}: {r['error']}", file=sys.stderr)
            continue
        v = r["verdict"]
        spdx = r.get("spdx_id", "?")
        hits = ", ".join(r.get("restriction_hits", []))
        line = f"  {v:10s} {r['repo']:40s} spdx={spdx}"
        if hits:
            line += f" hits=[{hits}]"
        print(line, file=sys.stderr)

    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[audit] raw -> {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
