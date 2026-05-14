#!/usr/bin/env python
"""
Step 1-2: 採用リポから .liquid + theme-liquid-docs を 200件取得。
出力: data/raw_snippets.jsonl
"""
import os
import json
import sys
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

# (owner, repo, license, kind, per_repo_quota)
COMMUNITY_REPOS = [
    ("Shopify", "skeleton-theme", "MIT", "theme", 18),
    ("Shopify", "mcliquid-theme", "MIT", "theme", 8),
    ("kondasoft", "ks-bootshop", "MIT", "theme", 25),
    ("mirceapiturca", "Sections", "MIT", "sections", 15),
    ("vikrantnegi", "shopify-code-snippets", "MIT", "snippets", 18),
    ("pgrimaud", "shopify-snippets", "MIT", "snippets", 8),
    ("freakdesign", "shopify-code-snippets", "MIT", "snippets", 25),
    ("instantcommerce", "shopify-headless-theme", "MIT", "theme", 15),
    ("uicrooks", "shopify-theme-lab", "MIT", "theme", 22),
]

REFERENCE_REPO = ("Shopify", "theme-liquid-docs", "MIT")
REF_QUOTA = {"filters": 16, "tags": 16, "objects": 16}


def gh_get(url, **kwargs):
    return requests.get(url, headers=GH_HEADERS, timeout=60, **kwargs)


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
        if size > 100_000 or size < 200:
            continue
        files.append({"path": path, "sha": entry["sha"], "size": size})
    return branch, files


def fetch_raw(owner, repo, branch, path):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        return None
    return r.text


def fetch_community(fout):
    count = 0
    for owner, repo, lic, kind, quota in COMMUNITY_REPOS:
        print(f"[fetch] {owner}/{repo} (quota={quota})", file=sys.stderr)
        try:
            branch, files = list_liquid_files(owner, repo)
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            continue
        # snippets/ や sections/ 配下を優先
        def priority(f):
            p = f["path"].lower()
            if "/snippets/" in p or p.startswith("snippets/"):
                return 0
            if "/sections/" in p or p.startswith("sections/"):
                return 1
            return 2
        files.sort(key=lambda f: (priority(f), f["size"]))
        taken = 0
        for f in files:
            if taken >= quota:
                break
            code = fetch_raw(owner, repo, branch, f["path"])
            if not code:
                continue
            lines = code.count("\n") + 1
            if lines < 5 or lines > 500:
                continue
            record = {
                "id": f"comm-{owner}-{repo}-{f['sha'][:8]}",
                "source_kind": "community" if kind in ("snippets", "sections") else "theme",
                "repo_owner": owner,
                "repo_name": repo,
                "repo_url": f"https://github.com/{owner}/{repo}",
                "license": lic,
                "branch": branch,
                "file_path": f["path"],
                "file_name": Path(f["path"]).name,
                "size_bytes": f["size"],
                "line_count": lines,
                "code": code,
                "raw_url": f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{f['path']}",
            }
            fout.write(json.dumps(record, ensure_ascii=False) + "\n")
            taken += 1
            count += 1
        print(f"  -> took {taken}/{len(files)}", file=sys.stderr)
    return count


def fetch_reference(fout):
    owner, repo, lic = REFERENCE_REPO
    print(f"[fetch] {owner}/{repo} (reference)", file=sys.stderr)
    try:
        branch = get_default_branch(owner, repo)
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        return 0

    # tree API でファイル一覧を取得して filters/tags/objects 関連 JSON を探す
    r = gh_get(
        f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}",
        params={"recursive": "1"},
    )
    r.raise_for_status()
    tree = r.json()
    # filters.json / tags.json / objects.json を含む path を抽出
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
    print(f"  reference candidates: { {k: v for k, v in candidates.items()} }", file=sys.stderr)

    count = 0
    for kind, paths in candidates.items():
        quota = REF_QUOTA.get(kind, 10)
        # 最も entry が多そうな 1 つを採用(複数あれば最初の優先)
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
        items.sort(key=lambda x: x.get("name", "") or "")
        # 均等サンプリング
        stride = max(1, len(items) // quota)
        taken = 0
        for i in range(0, len(items), stride):
            if taken >= quota:
                break
            item = items[i]
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
            taken += 1
            count += 1
        print(f"  -> reference {kind}: took {taken}/{len(items)} from {used_path}", file=sys.stderr)
    return count


def main():
    out_path = ROOT / "data" / "raw_snippets.jsonl"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fout:
        c1 = fetch_community(fout)
        c2 = fetch_reference(fout)
    print(f"\n[done] community={c1} reference={c2} total={c1 + c2} -> {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
