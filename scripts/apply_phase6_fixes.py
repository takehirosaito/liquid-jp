#!/usr/bin/env python3
"""
Phase 6β 動作確認で発見した8項目の修正を ~/liquid-jp/sections/*.liquid に一括適用。

実行: cd ~/liquid-jp && .venv/bin/python scripts/apply_phase6_fixes.py
"""
import os, re
from pathlib import Path

SECTIONS_DIR = Path('sections')
assert SECTIONS_DIR.exists(), f'sections/ ディレクトリが見つかりません(cwd={os.getcwd()})'

# ----- 修正ルール -----

# 1. 文体統一: ユーザー可視の default 値・本文中の「〜する。」を「〜します。」系に。
# default 値だけ狙う想定で、JSON文字列内のテキストのみ置換。コメント本文は触らない。
TEXT_REPLACEMENTS = [
    ('を紹介する。', 'をご紹介します。'),
    ('テーマエディタから紹介商品を選択する。', 'テーマエディタから紹介商品をご選択ください。'),
    ('一覧表示される。', '一覧表示されます。'),
    ('ぜひ一度試してみてほしい。', 'ぜひ一度お試しください。'),
    ('を運んでくれる。', 'を運んでくれます。'),
    ('自動で割引が適用される。', '自動で割引が適用されます。'),
    ('効果を実感できる。', '効果を実感できます。'),
    ('わかりやすく解説する。', 'わかりやすく解説します。'),
    ('状態を確認する。', '状態を確認します。'),
    ('定期購入をおすすめする。', '定期購入をおすすめします。'),
    ('わかりやすく説明する。', 'わかりやすく説明します。'),
    ('返品・交換に対応する。', '返品・交換に対応します。'),
    ('一つひとつ丁寧に収穫する。', '一つひとつ丁寧に収穫します。'),
    ('収穫翌日にお届けする。', '収穫翌日にお届けします。'),
    ('ご注文金額から10%を割引する。', 'ご注文金額から10%を割引します。'),
    ('全国どこでも送料を無料にする。', '全国どこでも送料を無料にします。'),
    ('人気商品のサンプルを同梱する。', '人気商品のサンプルを同梱します。'),
    ('PC ではゆったり長めの説明文を表示できる。', 'PC 表示時の説明文をここに入力します。'),
    ('PC で見るキャッチコピー', 'PC 表示時のメインメッセージ'),
]

# 2. countdown-timer: 終了年 2025 → 2099(マーチャントが上書きする想定の遠未来)
COUNTDOWN_FIX = {
    'file': 'countdown-timer.liquid',
    'patterns': [
        (r'("id":\s*"end_year",\s*"label":\s*"年",\s*"default":\s*)2025', r'\g<1>2099'),
    ],
}

# 3. seasonal-event: 「期間」バッジ部分が片側だけ赤背景になる問題
#    最小修正: バッジテキストを「期間」→「期間限定」に統一(視覚的に安定)
SEASONAL_FIX = {
    'file': 'seasonal-event.liquid',
    'patterns': [
        (r'>期間</span>', r'>期間限定</span>'),
    ],
}

# 4. customer-review-card / review-carousel: blocks ゼロ件フォールバック追加
#    {%- for block in section.blocks -%} の直前に「{%- if section.blocks.size == 0 -%}空メッセージ{%- endif -%}」を挿入
def add_review_fallback(content: str, section_class_root: str) -> str:
    fallback_html = (
        '\n  {%- if section.blocks.size == 0 -%}\n'
        f'    <p class="{section_class_root}__empty" style="text-align:center;color:#888;padding:2rem 0;">'
        '現在表示できるレビューはありません。テーマエディタからブロックを追加してください。'
        '</p>\n'
        '  {%- endif -%}\n'
    )
    # for ループ直前に挿入
    marker = '{%- for block in section.blocks -%}'
    if fallback_html.strip() in content:
        return content  # 適用済み
    return content.replace(marker, fallback_html + '    ' + marker, 1)


def main():
    files = sorted(SECTIONS_DIR.glob('*.liquid'))
    print(f'[fix] 対象 {len(files)} ファイル')
    changed = []

    for f in files:
        original = f.read_text(encoding='utf-8')
        new = original

        # 1. グローバル文字列置換
        for src, dst in TEXT_REPLACEMENTS:
            if src in new:
                new = new.replace(src, dst)

        # 2. countdown-timer
        if f.name == COUNTDOWN_FIX['file']:
            for pat, rep in COUNTDOWN_FIX['patterns']:
                new = re.sub(pat, rep, new)

        # 3. seasonal-event
        if f.name == SEASONAL_FIX['file']:
            for pat, rep in SEASONAL_FIX['patterns']:
                new = re.sub(pat, rep, new)

        # 4. customer-review-card
        if f.name == 'customer-review-card.liquid':
            new = add_review_fallback(new, 'alsel-customer-review-card')

        # 5. review-carousel
        if f.name == 'review-carousel.liquid':
            new = add_review_fallback(new, 'alsel-review-carousel')

        if new != original:
            f.write_text(new, encoding='utf-8')
            diff_count = sum(1 for a, b in zip(original.split('\n'), new.split('\n')) if a != b)
            extra = abs(len(new.split('\n')) - len(original.split('\n')))
            changed.append((f.name, diff_count + extra))
            print(f'  ✓ {f.name} ({diff_count + extra} lines diff)')

    print()
    print(f'[fix] {len(changed)} ファイル変更')
    if changed:
        print('[fix] 次のステップ: .venv/bin/python scripts/upload_to_dev_store.py')

if __name__ == '__main__':
    main()
