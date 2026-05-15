#!/usr/bin/env python3
"""
liquid-jp-dev 開発ストアのホームページ(templates/index.json)に
ALSEL監修22セクションを一気に追加するスクリプト。

実行: cd ~/liquid-jp && .venv/bin/python scripts/seed_homepage_22_sections.py
"""
import os, json, sys, time
from pathlib import Path

# .env 読み込み(python-dotenv なくても動く簡易パーサ)
env_path = Path('.env')
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        os.environ.setdefault(k.strip(), v.strip())

import requests

SHOP = os.environ['DEV_STORE_DOMAIN']
TOKEN = os.environ['DEV_STORE_ADMIN_TOKEN']
API_VER = os.environ.get('SHOPIFY_API_VERSION', '2024-10')
BASE = f"https://{SHOP}/admin/api/{API_VER}"

def headers():
    return {
        'X-Shopify-Access-Token': TOKEN,
        'Content-Type': 'application/json',
    }

def get_main_theme_id():
    r = requests.get(f"{BASE}/themes.json", headers=headers(), timeout=30)
    r.raise_for_status()
    for t in r.json()['themes']:
        if t.get('role') == 'main':
            return t['id']
    raise RuntimeError('main テーマ未検出')

# ALSEL監修22セクションの section type と表示順
# 出現順: ヒーロー → 訴求 → ランキング/商品 → 信頼訴求 → 補足
ALSEL_SECTIONS = [
    'hero-fv-lp',
    'free-shipping-bar',
    'coupon-promotion',
    'limited-sale-banner',
    'countdown-timer',
    'first-time-offer',
    'three-reasons-why',
    'ranking-top-three',
    'best-seller-ranking',
    'new-products-list',
    'restock-products',
    'store-manager-pick',
    'bulk-buy-offer',
    'subscription-benefits',
    'gift-promotion',
    'seasonal-event',
    'brand-story',
    'producer-profile',
    'how-to-use-steps',
    'customer-review-card',
    'review-carousel',
    'hero-mobile',  # モバイル切替確認用に末尾
]

def main():
    theme_id = get_main_theme_id()
    print(f"[seed] theme_id={theme_id}")

    # 各セクションのプリセットdefault設定を使うため、最小JSON(typeのみ)で構成
    # blocksありセクションも、プリセット側のblocksが自動で展開される
    sections_obj = {}
    order = []
    for i, stype in enumerate(ALSEL_SECTIONS, 1):
        key = f"alsel_{stype.replace('-', '_')}_{i:02d}"
        sections_obj[key] = {
            'type': stype,
            'settings': {},
            # blocks は schema の preset から自動的に展開される(空指定でOK)
        }
        order.append(key)

    template = {
        'sections': sections_obj,
        'order': order,
    }

    payload = {
        'asset': {
            'key': 'templates/index.json',
            'value': json.dumps(template, ensure_ascii=False, indent=2),
        }
    }

    print(f"[seed] PUT templates/index.json ({len(order)} sections)")
    r = requests.put(
        f"{BASE}/themes/{theme_id}/assets.json",
        headers=headers(),
        json=payload,
        timeout=60,
    )
    if r.status_code >= 400:
        print(f"[seed] ERROR {r.status_code}: {r.text[:500]}")
        sys.exit(1)
    print(f"[seed] OK ({r.status_code})")
    print(f"[seed] -> Open: https://admin.shopify.com/store/liquid-jp-dev/themes/{theme_id}/editor")

if __name__ == '__main__':
    main()
