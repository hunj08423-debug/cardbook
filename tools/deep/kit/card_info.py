# -*- coding: utf-8 -*-
"""카드 한 장에 대해 사이트가 이미 가진 내용을 모두 보여 줘요(앞면, 이야기, 안내 항목, 긴 이야기, 출처).
깊은 카드를 만들기 전에 꼭 먼저 읽어요. 여기 적힌 사실도 출처를 다시 열어 확인한 뒤에만 써요.

쓰는 법(저장소 맨 위 폴더에서):
  python3 tools/deep/kit/card_info.py <카드id> [<카드id> ...]
  python3 tools/deep/kit/card_info.py --batch 7        → BATCHES.md의 7번 묶음 카드 다섯 장 모두
"""
import os, sys, json, glob, re

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))

def load():
    cards, items, stories = {}, {}, {}
    for f in sorted(glob.glob(os.path.join(REPO, 'site', 'data', 'ch-*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        cards.update(d.get('cards', {})); items.update(d.get('items', {})); stories.update(d.get('stories', {}))
    ix = json.load(open(os.path.join(REPO, 'site', 'data', 'index.json'), encoding='utf-8'))
    return cards, items, stories, ix

def batch_ids(n):
    p = os.path.join(KIT, '..', 'BATCHES.md')
    for ln in open(p, encoding='utf-8'):
        m = re.match(r'\|\s*(\d+)\s*\|', ln)
        if m and int(m.group(1)) == n:
            return re.findall(r'`([a-z0-9-]+)`', ln)
    raise SystemExit(f'BATCHES.md에 {n}번 묶음이 없어요')

def show(cid, C, I, S, ix):
    c = C.get(cid)
    if not c: print(f'■ {cid}: site/data에 없는 카드예요(이 창에 그 장의 ch-*.json을 가져왔는지 보세요)'); return
    st = ix['sets'][c['set']]; ch = next(x for x in ix['chapters'] if x['id'] == st['ch'])
    order = st['cards']; k = order.index(cid)
    print(f"■ {cid} · 「{c['t']}」 · {c['tag']}")
    print(f"  {ch['no']}장 {ch['t']} › {st['k']}({st['t']}) · 묶음 안 {k + 1}/{len(order)}번째 · 앞: {order[k - 1] if k else '-'} · 뒤: {order[k + 1] if k + 1 < len(order) else '-'}")
    print(f"  앞면 그림: {c['by']}\n    출처 줄: {c['cr']}\n    {c.get('cru', '')}\n    설명: {c['alt']}")
    print(f"  물음: {c['q']}\n  아이 물음: {c['kq']}\n  한 줄: {c['line']}")
    print('  앞면 이야기(이미 사이트에 있는 1단계 이야기):')
    for i, s in enumerate(c['scenes'], 1):
        print(f"    {i}. {'[' + s['label'] + '] ' if s.get('label') else ''}{s['t']}\n       아이: {s.get('kid', '')}")
    print(f"  알고 보면: {c.get('wow', '')}\n  아이: {c.get('wowKid', '')}")
    print(f"  나의 자리 물음: {c['ask']} / 아이: {c.get('askKid', '')}")
    print('  앞면 출처:'); [print(f"    - {x['l']}  {x['u']}") for x in c.get('src', [])]
    if c.get('see'): print('  더 보기:'); [print(f"    - {x['l']}  {x['u']}") for x in c['see']]
    it = I.get(c.get('item') or '')
    if it:
        print(f"  ▷ 안내 항목 「{it['t']}」({it.get('o', '')}) · {it.get('g', '')} · {it.get('y', '')} · {it.get('p', '')}")
        for key, lab in (('s', '이야기'), ('w', '왜 중요한가'), ('ac', '해 보기')):
            if it.get(key): print(f'    {lab}: {it[key]}')
        for x in it.get('src', []): print(f"    출처: {x['l']}  {x['u']}")
    for sid in [c.get('item')] + list(c.get('also', [])):
        s = S.get(sid or '')
        if not s: continue
        print(f"  ▷ 긴 이야기 「{s['t']}」 · {s.get('k', '')}\n    {s.get('lead', '')}")
        for p in s.get('body', []): print(f'    · {p}')
        if s.get('after'): print(f"    뒤 이야기: {s['after']}")
        if s.get('unc'): print(f"    기록마다 다른 점: {s['unc']}")
        for x in s.get('src', []): print(f"    출처: {x['l']}  {x['u']}")
    done = os.path.exists(os.path.join(REPO, 'site', 'deep', cid + '.html'))
    if done or cid in ix.get('deep', {}): print('  ※ 이미 깊은 카드가 있어요: site/deep/' + cid + '.html')
    print()

def neighbors(n, ix):
    """n번 묶음의 앞 묶음 마지막 카드와 뒤 묶음 첫 카드(같은 장 안에서만)"""
    order = [(ch['id'], sid) for ch in ix['chapters'] for sid in ch['sets']]
    chid, _ = order[n - 1]
    prev = ix['sets'][order[n - 2][1]]['cards'][-1] if n > 1 and order[n - 2][0] == chid else None
    nxt = ix['sets'][order[n][1]]['cards'][0] if n < len(order) and order[n][0] == chid else None
    return prev, nxt

def method_of(cid):
    p = os.path.join(KIT, '..', 'status', cid + '.md')
    if not os.path.exists(p): return '상태 파일 없음(아직 안 만들었거나 이 창에 안 가져옴)'
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('- 중심 방식'): return ln.strip()[2:]
    return '상태 파일에 중심 방식 줄이 없음'

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    C, I, S, ix = load()
    ids = batch_ids(int(a[1])) if a[0] == '--batch' else a
    if a[0] == '--batch':
        pv, nx = neighbors(int(a[1]), ix)
        print(f"■ 같은 장의 이웃 카드(중심 방식이 겹치지 않게): 앞 묶음 마지막 {pv or '-'} · 뒤 묶음 첫 {nx or '-'}")
        for x in (pv, nx):
            if x: print(f'  {x}: {method_of(x)}')
        print()
    for cid in ids: show(cid, C, I, S, ix)
