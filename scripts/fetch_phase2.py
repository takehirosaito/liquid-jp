#!/usr/bin/env python
"""
Phase 2: 採用リポジトリから .liquid + theme-liquid-docs を全件取得。
quota 撤廃、SHA ベース重複除外、Shopify/liquid と Shopify/theme-tools を追加
(include 使用コード混入のため)、行数下限を 5 行 / サイズ下限を 50B に緩和。

出力: --out で指定する jsonl (default: data/raw_full.jsonl)
"""
import argparse
import hashlib
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path
import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

GH_TOKEN = os.environ["GITHUB_TOKEN"]
GH_HEADERS = {
    "Authorization": f"Bearer {GH_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

# (owner, repo, license, kind, max_per_repo)
# max_per_repo は 9999 で実質無制限。"include 検出用" で集めるリポは少なめにする。
COMMUNITY_REPOS = [
    ("Shopify", "skeleton-theme", "MIT", "theme", 9999),
    ("Shopify", "mcliquid-theme", "MIT", "theme", 9999),
    ("kondasoft", "ks-bootshop", "MIT", "theme", 9999),
    ("mirceapiturca", "Sections", "MIT", "sections", 9999),
    ("vikrantnegi", "shopify-code-snippets", "MIT", "snippets", 9999),
    ("pgrimaud", "shopify-snippets", "MIT", "snippets", 9999),
    ("freakdesign", "shopify-code-snippets", "MIT", "snippets", 9999),
    ("instantcommerce", "shopify-headless-theme", "MIT", "theme", 9999),
    ("uicrooks", "shopify-theme-lab", "MIT", "theme", 9999),
    # Phase 2 追加: 古い include 使用コードがあるはず & fixtures に Liquid サンプル
    ("Shopify", "liquid", "MIT", "engine_fixtures", 9999),
    ("Shopify", "theme-tools", "MIT", "engine_fixtures", 9999),
]

REFERENCE_REPO = ("Shopify", "theme-liquid-docs", "MIT")

# Phase 2 のフィルタ閾値(Phase 1 より緩和)
SIZE_MIN = 50           # Phase 1: 200 → vikrantnegi pagination 系を拾うため
SIZE_MAX = 100_000      # Phase 1 と同じ
LINE_MIN = 5
LINE_MAX = 1000         # Phase 1: 500 → theme ファイルなど大きめも拾う

# engine_fixtures カテゴリ用: テスト fixture / spec 由来は別扱い
ENGINE_FIXTURE_PATHS = ("spec/", "test/", "fixtures/", "fixture/", "lib/liquid/")


def gh_get(url, **kwargs):
    """GitHub API 呼び出し(レート制限考慮)"""
    for attempt in range(3):
        r = requests.get(url, headers=GH_HEADERS, timeout=60, **kwargs)
        if r.status_code == 403 and "rate limit" in r.text.lower():
            reset = int(r.headers.get("X-RateLimit-Reset", "0"))
            wait = max(0, reset - int(time.time())) + 5
            print(f"  [rate limit] wait {wait}s", file=sys.stderr)
            time.sleep(min(wait, 60))
            continue
        return r
    return r


def get_default_branch(owner, repo):
    r = gh_get(f"https://api.github.com/repos/{owner}/{repo}")
    r.raise_for_status()
    return r.json()["default_branch"]


def list_liquid_files(owner, repo):
    branch = get_default_branch(owner, repo)
    r = gh_get(
        f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}",
        params={"recursive": "1"},
    )
    r.raise_for_status()
    tree = r.json()
    if tree.get("truncated"):
        print(f"  WARN: tree truncated for {owner}/{repo}", file=sys.stderr)
    files = []
    for entry in tree.get("tree", []):
        if entry["type"] != "blob":
            continue
        path = entry["path"]
        if not path.endswith(".liquid"):
            continue
        size = entry.get("size", 0)
        if size > SIZE_MAX or size < SIZE_MIN:
            continue
        files.append({"path": path, "sha": entry["sha"], "size": size})
    return branch, files


def fetch_raw(owner, repo, branch, path):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        return None
    return r.text


def is_engine_fixture(path: str) -> bool:
    p = path.lower()
    return any(p.startswith(prefix) or f"/{prefix}" in p for prefix in ENGINE_FIXTURE_PATHS)


def fetch_community(content_hashes: set, fout):
    """各リポから .liquid を全件取得。content_hashes は SHA256 で重複除外"""
    stats = Counter()
    for owner, repo, lic, kind, max_per in COMMUNITY_REPOS:
        print(f"[fetch] {owner}/{repo} (kind={kind})", file=sys.stderr)
        try:
            branch, files = list_liquid_files(owner, repo)
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            stats[f"err_{owner}_{repo}"] += 1
            continue
        # snippets/ や sections/ 配下を優先的に並べる(ファイル取得順)
        def priority(f):
            p = f["path"].lower()
            if "/snippets/" in p or p.startswith("snippets/"):
                return 0
            if "/sections/" in p or p.startswith("sections/"):
                return 1
            if "/layout/" in p or p.startswith("layout/"):
                return 2
            if "/templates/" in p or p.startswith("templates/"):
                return 3
            return 4
        files.sort(key=lambda f: (priority(f), f["size"]))
        taken = 0
        skipped_dup = 0
        skipped_lines = 0
        skipped_fetch = 0
        for f in files:
            if taken >= max_per:
                break
            code = fetch_raw(owner, repo, branch, f["path"])
            if not code:
                skipped_fetch += 1
                continue
            lines = code.count("\n") + 1
            if lines < LINE_MIN or lines > LINE_MAX:
                skipped_lines += 1
                continue
            # 内容ハッシュで重複除外
            h = hashlib.sha256(code.encode("utf-8")).hexdigest()
            if h in content_hashes:
                skipped_dup += 1
                continue
            content_hashes.add(h)

            source_kind = "community"
            if kind in ("snippets", "sections"):
                source_kind = "community"
            elif kind == "theme":
                source_kind = "theme"
            elif kind == "engine_fixtures":
                source_kind = "engine_fixture" if is_engine_fixture(f["path"]) else "engine_other"

            record = {
                "id": f"comm-{owner}-{repo}-{f['sha'][:10]}",
                "source_kind": source_kind,
                "repo_owner": owner,
                "repo_name": repo,
                "repo_url": f"https://github.com/{owner}/{repo}",
                "license": lic,
                "branch": branch,
                "file_path": f["path"],
                "file_name": Path(f["path"]).name,
                "size_bytes": f["size"],
                "line_count": lines,
                "content_hash": h,
                "code": code,
                "raw_url": f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{f['path']}",
            }
            fout.write(json.dumps(record, ensure_ascii=False) + "\n")
            fout.flush()
            taken += 1
            stats[f"ok_{owner}_{repo}"] += 1
        print(
            f"  -> took {taken}/{len(files)} (dup {skipped_dup}, "
            f"lines {skipped_lines}, fetch_err {skipped_fetch})",
            file=sys.stderr,
        )
        stats["total_ok"] += taken
        stats["total_dup"] += skipped_dup
    return stats


def fetch_reference(fout):
    """theme-liquid-docs から filters / tags / objects を全件取得(quota 撤廃)"""
    owner, repo, lic = REFERENCE_REPO
    print(f"[fetch] {owner}/{repo} (reference, 全件)", file=sys.stderr)
    try:
        branch = get_default_branch(owner, repo)
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        return 0

    r = gh_get(
        f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}",
        params={"recursive": "1"},
    )
    r.raise_for_status()
    tree = r.json()
    candidates = {"filters": [], "tags": [], "objects": []}
    for entry in tree.get("tree", []):
        if entry["type"] != "blob":
            continue
        path = entry["path"]
        if not path.endswith(".json"):
            continue
        low = path.lower()
        for kind in candidates:
            if low.endswith(f"/{kind}.json") or low == f"{kind}.json":
                candidates[kind].append(path)

    count = 0
    for kind, paths in candidates.items():
        if not paths:
            print(f"  WARN: no file for {kind}", file=sys.stderr)
            continue
        items = []
        used_path = None
        for path in paths:
            url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
            r2 = requests.get(url, timeout=30)
            if r2.status_code != 200:
                continue
            try:
                data = r2.json()
            except json.JSONDecodeError:
                continue
            parsed = []
            if isinstance(data, list):
                parsed = [x for x in data if isinstance(x, dict) and x.get("name")]
            elif isinstance(data, dict):
                for name, spec in data.items():
                    if isinstance(spec, dict):
                        parsed.append({"name": name, **spec})
            if len(parsed) > len(items):
                items = parsed
                used_path = path
        if not items:
            print(f"  WARN: no parsed items for {kind}", file=sys.stderr)
            continue
        # quota 撤廃: 全件
        items.sort(key=lambda x: x.get("name", "") or "")
        taken = 0
        for item in items:
            name = item.get("name", "")
            if not name:
                continue
            spec_text = json.dumps(item, ensure_ascii=False, indent=2)
            record = {
                "id": f"ref-{kind}-{name}",
                "source_kind": f"reference-{kind}",
                "repo_owner": owner,
                "repo_name": repo,
                "repo_url": f"https://github.com/{owner}/{repo}",
                "license": lic,
                "branch": branch,
                "file_path": used_path,
                "file_name": name,
                "size_bytes": len(spec_text.encode("utf-8")),
                "line_count": spec_text.count("\n") + 1,
                "code": spec_text,
                "raw_url": f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{used_path}",
                "reference_kind": kind,
                "reference_name": name,
            }
            fout.write(json.dumps(record, ensure_ascii=False) + "\n")
            fout.flush()
            taken += 1
            count += 1
        print(f"  -> reference {kind}: took {taken} from {used_path}", file=sys.stderr)
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/raw_full.jsonl")
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="(オプション) コミュニティ取得後にこの件数で打ち切り。デバッグ用",
    )
    args = parser.parse_args()
    out_path = ROOT / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    content_hashes: set = set()
    with out_path.open("w", encoding="utf-8") as fout:
        stats = fetch_community(content_hashes, fout)
        ref_count = fetch_reference(fout)
    elapsed = time.time() - t0
    total_comm = stats.get("total_ok", 0)
    print(
        f"\n[done] community={total_comm} reference={ref_count} "
        f"total={total_comm + ref_count} dup_removed={stats.get('total_dup', 0)} "
        f"elapsed={elapsed:.1f}s -> {out_path}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
