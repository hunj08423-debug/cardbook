# -*- coding: utf-8 -*-
"""[본부 전용] site/data/index.json에서 묶음표(tools/deep/BATCHES.md)를 만들어요.
묶음 하나 = 사이트의 ‘묶음’(set) 하나. 장 차례, 묶음 차례, 카드 차례 그대로예요.
쓰는 법: python3 tools/deep/kit/make_batches.py
"""
import os, json, datetime

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))
DONE = {'keep-sinai': '기준 카드(시안 2, deep2 틀)', 'lig-wreath': '예시(날짜 따라가기)', 'sil-score': '예시(소리)', 'cus-greccio': '예시(놓아 보기)'}

def main():
    ix = json.load(open(os.path.join(REPO, 'site', 'data', 'index.json'), encoding='utf-8'))
    C = ix['cards']
    rows, n, total = [], 0, 0
    for ch in ix['chapters']:
        rows.append(f"\n## {ch['no']}장 {ch['t']}  ({ch['id']} · 카드 {ch.get('n', '')}장)\n\n| 번호 | 묶음 | 카드 | 장수 |\n|---|---|---|---|")
        for sid in ch['sets']:
            s = ix['sets'][sid]; n += 1; total += len(s['cards'])
            cards = ' · '.join(f"`{cid}` {C[cid]['t']}" + (f" (✓ {DONE[cid]})" if cid in DONE else '') for cid in s['cards'])
            rows.append(f"| {n} | {s['k']} — {s['t']} | {cards} | {len(s['cards'])} |")
    head = f"""# 깊은 카드 묶음표

만든 날: {datetime.date.today().isoformat()} · 묶음 {n}개 · 카드 {total}장 · 묶음 하나 = 사이트의 ‘묶음’ 하나(3~8장)

- 사용자가 창마다 “○번 묶음 맡아 주세요”라고 맡겨요. 한 창은 한 번에 한 묶음만 만들어요.
- ✓ 표시 카드는 이미 있어요(예시·기준). 그 카드는 만들지 않아요.
- 같은 장 안에서 바로 앞 카드와 같은 중심 방식을 쓰지 않아요. 앞 묶음의 status 파일이 있으면 마지막 카드의 방식을 확인해요.
- 진행 상황은 이 표가 아니라 `tools/deep/status/<카드id>.md`에 적어요(이 표는 본부만 고쳐요).
- 카드 정보 보기: `python3 tools/deep/kit/card_info.py --batch <번호>`
"""
    out = head + '\n'.join(rows) + '\n'
    open(os.path.join(KIT, '..', 'BATCHES.md'), 'w', encoding='utf-8').write(out)
    print(f'BATCHES.md: 묶음 {n}개, 카드 {total}장')

if __name__ == '__main__':
    main()
