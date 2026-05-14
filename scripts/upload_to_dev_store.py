#!/usr/bin/env python
"""
22 セクションを Shopify 開発ストアに Admin API で一括投入する。

前提:
  ~/liquid-jp/.env に以下が設定されていること:
    DEV_STORE_DOMAIN     例: alsel-liquid-jp-dev.myshopify.com
    DEV_STORE_ADMIN_TOKEN 例: shpat_xxxxxxxxxxxx(Custom App の Admin API access token)
    DEV_STORE_THEME_ID   例: 123456789012(投入先テーマ ID、未指定なら main theme)

使い方:
  python scripts/upload_to_dev_store.py                  # 全 22 件投入
  python scripts/upload_to_dev_store.py --slugs hero-fv-lp,hero-mobile
  python scripts/upload_to_dev_store.py --list-themes    # テーマ ID 一覧を表示
  python scripts/upload_to_dev_store.py --dry-run        # ファイル一覧のみ表示
"""
import argparse
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
import requests

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

SHOP = os.environ.get("DEV_STORE_DOMAIN", "")
TOKEN = os.environ.get("DEV_STORE_ADMIN_TOKEN", "")
THEME_ID = os.environ.get("DEV_STORE_THEME_ID", "")
API_VERSION = "2024-10"


def headers():
    return {
        "X-Shopify-Access-Token": TOKEN,
        "Content-Type": "application/json",
    }


def list_themes():
    """ストアの全テーマを一覧表示(main 確認用)"""
    url = f"https://{SHOP}/admin/api/{API_VERSION}/themes.json"
    r = requests.get(url, headers=headers(), timeout=30)
    r.raise_for_status()
    themes = r.json().get("themes", [])
    print(f"=== {SHOP} のテーマ一覧 ===")
    for t in themes:
        marker = "👑" if t.get("role") == "main" else "  "
        print(f"  {marker} id={t['id']} role={t['role']:11s} name={t['name']!r}")


def get_main_theme_id() -> int:
    url = f"https://{SHOP}/admin/api/{API_VERSION}/themes.json"
    r = requests.get(url, headers=headers(), timeout=30)
    r.raise_for_status()
    for t in r.json().get("themes", []):
        if t.get("role") == "main":
            return t["id"]
    raise RuntimeError("main theme が見つかりません")


def upload_section(theme_id: int, slug: str, content: str) -> tuple[int, dict]:
    """1セクションをテーマに投入"""
    url = f"https://{SHOP}/admin/api/{API_VERSION}/themes/{theme_id}/assets.json"
    payload = {"asset": {"key": f"sections/{slug}.liquid", "value": content}}
    r = requests.put(url, headers=headers(), json=payload, timeout=60)
    try:
        return r.status_code, r.json()
    except ValueError:
        return r.status_code, {"raw": r.text[:500]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slugs", help="csv で対象 slug を指定")
    parser.add_argument("--list-themes", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.list_themes:
        if not SHOP or not TOKEN:
            sys.exit("ERR: DEV_STORE_DOMAIN / DEV_STORE_ADMIN_TOKEN を .env に設定してください")
        list_themes()
        return

    # 対象ファイル一覧
    sections = sorted((ROOT / "sections").glob("*.liquid"))
    if args.slugs:
        targets = set(args.slugs.split(","))
        sections = [s for s in sections if s.stem in targets]
    print(f"[upload] {len(sections)} 件 対象")
    if args.dry_run:
        for s in sections:
            print(f"  → sections/{s.stem}.liquid ({s.stat().st_size:,} bytes)")
        return

    if not SHOP or not TOKEN:
        sys.exit(
            "ERR: DEV_STORE_DOMAIN / DEV_STORE_ADMIN_TOKEN を .env に設定してください。\n"
            "詳細は docs/phase6_dev_store_setup.md 参照。"
        )

    theme_id = int(THEME_ID) if THEME_ID else get_main_theme_id()
    print(f"[upload] theme_id={theme_id}", file=sys.stderr)

    ok = 0
    ng = 0
    for s in sections:
        content = s.read_text(encoding="utf-8")
        code, body = upload_section(theme_id, s.stem, content)
        if 200 <= code < 300:
            print(f"  OK  {s.stem}.liquid ({code})", file=sys.stderr)
            ok += 1
        else:
            err = body.get("errors") or body
            print(f"  ERR {s.stem}.liquid ({code}): {err}", file=sys.stderr)
            ng += 1
        time.sleep(0.4)  # Admin API rate limit 配慮(2 req/s)

    print(f"\n[upload] done: ok={ok} err={ng}", file=sys.stderr)
    if ng:
        sys.exit(1)


if __name__ == "__main__":
    main()
