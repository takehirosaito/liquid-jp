#!/usr/bin/env python
"""
Playwright で 22 セクションのスクショを自動撮影。

前提:
  ~/liquid-jp/.env に以下を設定:
    DEV_STORE_DOMAIN          例: alsel-liquid-jp-dev.myshopify.com
    DEV_STORE_PASSWORD        ストアフロントのパスワード(開発ストアの公開前パスワード)
    DEV_STORE_ADMIN_TOKEN     Admin API トークン(セクション挿入に使う、別途)
    DEV_STORE_THEME_ID        テーマ ID(必須)
  Playwright インストール:
    pip install playwright && playwright install chromium

実行:
  python scripts/screenshot_sections.py             # 全 22 件
  python scripts/screenshot_sections.py --slugs hero-fv-lp,hero-mobile
"""
import argparse
import json
import os
import re
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
PASSWORD = os.environ.get("DEV_STORE_PASSWORD", "")
API_VERSION = "2024-10"

OUTPUT_DIR = ROOT / "output" / "section_screenshots"
CHECKER_HTML = ROOT / "output" / "checker.html"


def get_main_theme_id() -> int:
    url = f"https://{SHOP}/admin/api/{API_VERSION}/themes.json"
    r = requests.get(
        url, headers={"X-Shopify-Access-Token": TOKEN}, timeout=30
    )
    r.raise_for_status()
    for t in r.json().get("themes", []):
        if t.get("role") == "main":
            return t["id"]
    raise RuntimeError("main theme not found")


def write_index_json(theme_id: int, slug: str, preset_name: str):
    """templates/index.json を上書きして指定セクション 1 個だけのページにする"""
    index_data = {
        "sections": {
            "_target": {
                "type": slug,
                # presets を持つセクションは初期 settings に preset の値が入る
                # ただし JSON テンプレートで presets を直接呼ぶ書き方は無いため、
                # type 指定のみで section が表示される(空 settings での描画)。
                # → preset を反映させたい場合は別途 settings を埋める必要あり
            }
        },
        "order": ["_target"],
    }
    url = f"https://{SHOP}/admin/api/{API_VERSION}/themes/{theme_id}/assets.json"
    payload = {
        "asset": {
            "key": "templates/index.json",
            "value": json.dumps(index_data, ensure_ascii=False),
        }
    }
    r = requests.put(
        url,
        headers={
            "X-Shopify-Access-Token": TOKEN,
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=30,
    )
    r.raise_for_status()


def extract_preset_name(liquid_content: str) -> str:
    """{% schema %} 内の最初のプリセット名を抽出"""
    m = re.search(r'"presets"\s*:\s*\[\s*\{[^}]*?"name"\s*:\s*"([^"]+)"', liquid_content, re.S)
    return m.group(1) if m else ""


def screenshot_section(page, slug: str, out_path: Path):
    """指定 slug がトップに表示されている状態のフルページをキャプチャ"""
    url = f"https://{SHOP}/"
    page.goto(url, wait_until="networkidle", timeout=60000)
    # 開発ストアパスワード入力
    if "/password" in page.url and PASSWORD:
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_load_state("networkidle", timeout=60000)
    # フルページスクショ
    page.screenshot(path=str(out_path), full_page=True)


def render_checker_html(items: list[dict]):
    """grid 表示 + OK/NG/要修正 ボタン付きのチェッカーUI"""
    html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>ALSEL監修セクション スクショチェッカー</title>
<style>
  body { font-family: -apple-system, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 1.5rem; }
  h1 { font-weight: 700; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(420px, 1fr)); gap: 1.5rem; }
  .card { background: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 6px 20px rgba(0,0,0,0.3); }
  .card img { width: 100%; height: 320px; object-fit: cover; object-position: top; background: #334155; cursor: pointer; }
  .meta { padding: 1rem; }
  .title { font-size: 0.95rem; font-weight: 700; margin: 0 0 0.5rem; color: #f8fafc; }
  .slug { font-size: 0.75rem; color: #94a3b8; font-family: ui-monospace, monospace; margin: 0 0 0.75rem; }
  .actions { display: flex; gap: 0.4rem; }
  .btn { flex: 1; padding: 0.4rem; font-size: 0.8rem; font-weight: 700; border: 0; border-radius: 6px; cursor: pointer; }
  .btn.ok { background: #22c55e; color: #0f172a; }
  .btn.ng { background: #ef4444; color: #fff; }
  .btn.fix { background: #f59e0b; color: #0f172a; }
  .modal { position: fixed; inset: 0; background: rgba(0,0,0,0.92); display: none; align-items: center; justify-content: center; padding: 2rem; z-index: 100; cursor: zoom-out; }
  .modal.show { display: flex; }
  .modal img { max-width: 100%; max-height: 100%; object-fit: contain; }
  .summary { background: #1e293b; padding: 1rem 1.25rem; border-radius: 12px; margin-bottom: 1.5rem; display: flex; gap: 2rem; align-items: center; }
  .summary > div { text-align: center; }
  .summary .num { font-size: 1.5rem; font-weight: 800; }
  .summary .lbl { font-size: 0.75rem; color: #94a3b8; }
  .summary .ok { color: #22c55e; }
  .summary .ng { color: #ef4444; }
  .summary .fix { color: #f59e0b; }
</style>
</head>
<body>
<h1>ALSEL監修セクション スクショチェッカー</h1>
<div class="summary">
  <div><div class="num ok" id="cnt-ok">0</div><div class="lbl">OK</div></div>
  <div><div class="num ng" id="cnt-ng">0</div><div class="lbl">NG</div></div>
  <div><div class="num fix" id="cnt-fix">0</div><div class="lbl">要修正</div></div>
  <div><div class="num" id="cnt-pending">22</div><div class="lbl">未判定</div></div>
  <button onclick="exportJSON()" style="padding:0.5rem 1rem;font-weight:700;border-radius:6px;border:0;cursor:pointer;background:#7c3aed;color:#fff;">結果を JSON でダウンロード</button>
</div>
<div class="grid" id="grid"></div>
<div class="modal" id="modal" onclick="this.classList.remove('show')"><img id="modal-img"></div>

<script>
const items = __ITEMS_JSON__;
const state = JSON.parse(localStorage.getItem('alsel_check') || '{}');
const grid = document.getElementById('grid');
const modal = document.getElementById('modal');
const modalImg = document.getElementById('modal-img');

function updateCounts() {
  const c = { ok: 0, ng: 0, fix: 0, pending: 0 };
  items.forEach(it => {
    const s = state[it.slug] || 'pending';
    c[s]++;
  });
  document.getElementById('cnt-ok').textContent = c.ok;
  document.getElementById('cnt-ng').textContent = c.ng;
  document.getElementById('cnt-fix').textContent = c.fix;
  document.getElementById('cnt-pending').textContent = c.pending;
}
function setStatus(slug, status) {
  state[slug] = status;
  localStorage.setItem('alsel_check', JSON.stringify(state));
  render();
}
function exportJSON() {
  const blob = new Blob([JSON.stringify(state, null, 2)], {type: 'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'alsel_check_result.json';
  a.click();
}
function render() {
  grid.innerHTML = '';
  items.forEach(it => {
    const card = document.createElement('div');
    card.className = 'card';
    const cur = state[it.slug] || 'pending';
    const borderColor = { ok: '#22c55e', ng: '#ef4444', fix: '#f59e0b', pending: 'transparent' }[cur];
    card.style.boxShadow = `0 0 0 3px ${borderColor}, 0 6px 20px rgba(0,0,0,0.3)`;
    card.innerHTML = `
      <img src="section_screenshots/${it.slug}.png" alt="${it.title}" onclick="document.getElementById('modal-img').src=this.src;document.getElementById('modal').classList.add('show');" />
      <div class="meta">
        <p class="title">${it.title}</p>
        <p class="slug">${it.slug}</p>
        <div class="actions">
          <button class="btn ok" onclick="setStatus('${it.slug}','ok')">OK</button>
          <button class="btn fix" onclick="setStatus('${it.slug}','fix')">要修正</button>
          <button class="btn ng" onclick="setStatus('${it.slug}','ng')">NG</button>
        </div>
      </div>`;
    grid.appendChild(card);
  });
  updateCounts();
}
render();
</script>
</body>
</html>
"""
    items_json = json.dumps(
        [{"slug": i["slug"], "title": i["title"]} for i in items], ensure_ascii=False
    )
    html = html.replace("__ITEMS_JSON__", items_json)
    CHECKER_HTML.write_text(html, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slugs", help="csv で対象 slug を指定")
    parser.add_argument(
        "--checker-only",
        action="store_true",
        help="スクショ撮影せず、既存 PNG から checker.html だけ再生成",
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 対象セクション
    sections = sorted((ROOT / "sections").glob("*.liquid"))
    if args.slugs:
        targets = set(args.slugs.split(","))
        sections = [s for s in sections if s.stem in targets]

    items = []
    for s in sections:
        content = s.read_text(encoding="utf-8")
        items.append(
            {
                "slug": s.stem,
                "title": extract_preset_name(content) or s.stem,
                "path": str(s),
            }
        )

    if args.checker_only:
        render_checker_html(items)
        print(f"[checker] -> {CHECKER_HTML}", file=sys.stderr)
        return

    # Playwright 撮影
    if not SHOP or not TOKEN or not THEME_ID:
        sys.exit(
            "ERR: DEV_STORE_DOMAIN / DEV_STORE_ADMIN_TOKEN / DEV_STORE_THEME_ID が未設定。\n"
            "docs/phase6_dev_store_setup.md 参照。"
        )
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit(
            "ERR: Playwright 未導入。\n"
            "  ~/liquid-jp/.venv/bin/pip install playwright\n"
            "  ~/liquid-jp/.venv/bin/playwright install chromium"
        )

    theme_id = int(THEME_ID)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, locale="ja-JP")
        page = ctx.new_page()
        ok = 0
        ng = 0
        for it in items:
            slug = it["slug"]
            print(f"[shot] {slug} ...", file=sys.stderr, end=" ")
            try:
                write_index_json(theme_id, slug, it["title"])
                time.sleep(2)  # CDN 反映待ち
                out = OUTPUT_DIR / f"{slug}.png"
                screenshot_section(page, slug, out)
                print(f"OK ({out.stat().st_size:,} bytes)", file=sys.stderr)
                ok += 1
            except Exception as e:
                print(f"ERR: {e}", file=sys.stderr)
                ng += 1
        browser.close()
        print(f"\n[shot] done: ok={ok} err={ng}", file=sys.stderr)

    # チェッカー HTML 生成
    render_checker_html(items)
    print(f"[checker] -> {CHECKER_HTML}", file=sys.stderr)


if __name__ == "__main__":
    main()
