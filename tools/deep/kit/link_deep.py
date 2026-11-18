# -*- coding: utf-8 -*-
"""[본부 전용] 만들어진 깊은 카드를 사이트 목록(site/data/index.json의 deep)에 이어요.

쓰는 법(저장소 맨 위에서):
  python3 tools/deep/kit/link_deep.py                    → 보기만(무엇이 더해질지)
  python3 tools/deep/kit/link_deep.py --write            → site/deep/*.html 중 통과한 카드를 모두 이어요
  python3 tools/deep/kit/link_deep.py --write id1 id2    → 이 카드만
이어 둔 카드는 지우지 않아요(keep-sinai 포함). tools/chapters.py의 DEEP 줄도 같이 맞춰요(build_site.py가 덮어쓰지 않게).
잇기 전에: 앱이 deep3 기록(‘deep3-<id>’)을 읽는지, 깊이 읽기 상자 문구가 카드 공통인지 확인해요(HQ.md).
"""
import os, sys, re, json, glob

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))

def main():
    a = sys.argv[1:]; write = '--write' in a; ids = [x for x in a if not x.startswith('--')]
    ixp = os.path.join(REPO, 'site', 'data', 'index.json')
    raw = open(ixp, encoding='utf-8').read(); ix = json.loads(raw)
    deep = dict(ix.get('deep', {}))
    found = []
    for f in sorted(glob.glob(os.path.join(REPO, 'site', 'deep', '*.html'))):
        cid = os.path.basename(f)[:-5]
        if cid == 'sinai' or (ids and cid not in ids): continue
        h = open(f, encoding='utf-8').read()
        if '"tplv":"deep3' not in h.replace(' ', ''): print(f'  건너뜀(deep3 아님): {cid}'); continue
        if cid not in ix['cards']: print(f'  건너뜀(없는 카드 id): {cid}'); continue
        if deep.get(cid) == f'deep/{cid}.html': continue
        found.append(cid)
    print(f"지금 이어진 카드 {len(deep)}장 · 새로 이을 카드 {len(found)}장: {', '.join(found) or '-'}")
    if not write or not found: return
    for cid in found: deep[cid] = f'deep/{cid}.html'
    ix['deep'] = deep
    out = json.dumps(ix, ensure_ascii=False, separators=(',', ':'))
    open(ixp, 'w', encoding='utf-8').write(out + ('\n' if raw.endswith('\n') else ''))
    cp = os.path.join(REPO, 'tools', 'chapters.py')
    if os.path.exists(cp):
        s = open(cp, encoding='utf-8').read()
        new = 'DEEP = ' + repr(deep)
        s2, n = re.subn(r'^DEEP = \{.*\}$', new, s, count=1, flags=re.M)
        if n: open(cp, 'w', encoding='utf-8').write(s2); print('tools/chapters.py의 DEEP도 맞췄어요')
        else: print('⚠ tools/chapters.py에서 DEEP 줄을 찾지 못했어요. 손으로 맞춰 주세요.')
    print(f'index.json에 이었어요: 모두 {len(deep)}장')

if __name__ == '__main__':
    main()
