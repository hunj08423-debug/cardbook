#!/usr/bin/env python3
"""보이는 글 뽑기(재벌 · 악마의 대변인에게 줄 것) — 2026-11-22 본부
(17:20 고침: 영화 자막의 인용 “ ”과 출처 ‘— 누구’가 빠졌던 것을 화면대로 넣어요)

깊은 카드에서 보는 사람에게 보이는 글(앞면 물음 · 첫머리 · 장면 · 손으로 하는 칸 · 상상 · 마무리 물음 ·
영화 자막)만 한 파일로 모으고, 카드에 나오는 그림을 작은 jpg로 옮겨요.
‘더 깊이’ 칸 · 근거 · 주석 · 아이 줄 · 그림 대체 글은 넣지 않아요(악마의 대변인이 처음 보는 사람처럼 읽게).

쓰는 법:
  python3 tools/deep/kit/reader_text.py <카드id 또는 cards/<카드id>.py> [--out 폴더] [--no-img]
  → <폴더>/reader.md 와 <폴더>/NN_<그림>.jpg (그림은 먼저 빌드한 site/deep/<카드id>/ 에서 가져와요)
폴더를 안 주면 임시 폴더(reader_<카드id>)에 써요. 재벌 창은 이 파일 하나만 읽어도 카드의 흐름을 알 수 있어요.
"""
import os, re, sys, json, glob, tempfile, importlib.util

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))

SKIP = {'id', 'img', 'imgs', 'src', 'u', 'svg', 'alt', 'vb', 'pos', 'fit', 'light', 'c', 'kid', 'kidq', 'leadKid',
        'askKid', 'linesKid', 'x', 'y0', 'w', 'h', 'p0', 'p1', 's0', 's1', 'o', 'sync', 'type', 'ch', 'mod'}
MODNAME = {'look': '그림 속 숫자를 하나씩 눌러 읽는 칸', 'choose': '고르기', 'gather': '모으기', 'place': '놓아 보기',
           'reveal': '비추기', 'route': '길 따라가기', 'slider': '그때와 지금 밀어 보기', 'steps': '만드는 차례',
           'timeline': '연표', 'trace': '따라 그리기', 'unroll': '펼쳐 읽기', 'voices': '소리 듣기', 'wreath': '화환'}


def clean(t):
    t = re.sub(r'<(script|style)\b.*?</\1>', ' ', str(t), flags=re.S | re.I)
    t = re.sub(r'<br\s*/?>', ' ', t, flags=re.I)
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def fline(x):
    """영화 자막 한 줄을 화면에 보이는 그대로: 인용(q)은 “ ”로 감싸고 출처(from)는 ‘— 출처’로 붙여요(2026-11-22 고침)."""
    if not isinstance(x, dict): return clean(x)
    t = clean(x.get('t', ''))
    if not t: return ''
    if x.get('q') and not re.search(r'[“”]', t): t = f'“{t}”'
    if x.get('from'): t += f' — {clean(x["from"])}'
    if x.get('ask'): t = f'(물어보기) {t}'
    return t


def load(path):
    spec = importlib.util.spec_from_file_location('card_' + os.path.basename(path)[:-3].replace('-', '_'), path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CARD


def front(cid):
    for f in sorted(glob.glob(os.path.join(REPO, 'site', 'data', 'ch-*.json'))):
        c = json.load(open(f, encoding='utf-8'))['cards'].get(cid)
        if c: return c
    return {}


def main(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__); return 0
    arg = argv[0]
    out = None; want_img = '--no-img' not in argv
    if '--out' in argv: out = argv[argv.index('--out') + 1]
    path = arg if arg.endswith('.py') else os.path.join(REPO, 'tools', 'deep', 'cards', arg + '.py')
    if not os.path.exists(path): sys.exit(f'카드 파일이 없어요: {path}')
    C = load(path); cid = C['id']; CC = front(cid)
    IM = C.get('images', {}); KEYS = set(IM) | {'card'}
    out = out or os.path.join(tempfile.gettempdir(), 'reader_' + cid)
    os.makedirs(out, exist_ok=True)
    order = []                                         # 그림이 처음 나오는 차례

    def see(k):
        if isinstance(k, str) and k in KEYS and k not in order: order.append(k)

    def strings(o, mod, acc):                          # 손으로 하는 칸: 보이는 글만, 나오는 차례대로
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ('img', 'imgs', 'then', 'now'):
                    for x in (v if isinstance(v, list) else [v]): see(x)
                if k in SKIP or (mod == 'trace' and k == 'd'): continue
                if isinstance(v, str):
                    if v in KEYS: see(v); continue
                    t = clean(v)
                    if t: acc.append(t)
                else: strings(v, mod, acc)
        elif isinstance(o, list):
            for v in o: strings(v, mod, acc)
        return acc

    L = [f'# 카드 「{CC.get("t") or C.get("pagetitle", cid)}」 — 보는 사람에게 보이는 글 전부', '']
    see('card')
    if CC.get('q'): L += [f'앞면 카드의 물음: {clean(CC["q"])}', '']
    if C.get('where'): L += [f'카드 머리: {clean(re.sub(r"</b>", " · ", C["where"]))}', '']
    L += ['## 첫머리', clean(C.get('lead', '')), '']
    for i, s in enumerate(C.get('scenes', []), 1):
        L.append(f'## 장면 {i} · {clean(s.get("label", ""))}')
        L += [clean(t) for t in (s.get('text') or [])]
        k = s.get('kind')
        caps = []
        if k == 'duo':
            for x, c in zip(s.get('imgs', []), s.get('caps') or [None] * len(s.get('imgs', []))):
                see(x); caps.append(c or IM.get(x, {}).get('cap'))
        elif k == 'thennow':
            for side in ('then', 'now'):
                x = s.get(side); see(x)
                caps.append(' · '.join(filter(None, [s.get(side + 'T'), IM.get(x, {}).get('cap')])))
        else:
            if s.get('img'): see(s['img']); caps.append(s.get('cap') or IM.get(s['img'], {}).get('cap'))
        for c in caps:
            if c: L.append(f'[그림 설명] {clean(c)}')
        if k == 'mod':
            mh = (C.get('modhtml') or {}).get(s.get('mod'))
            md = (C.get('mods') or {}).get(s.get('mod'))
            if isinstance(md, dict) and md.get('img'): see(md['img'])
            got = [clean(mh)] if mh else strings(md, s.get('mod'), [])
            if got:
                L.append(f'[{MODNAME.get(s.get("mod"), s.get("mod"))}]')
                L += [f'- {t}' for t in got if t]
        q = s.get('quote')
        if q: L.append(f'[인용] “{clean(q.get("t", ""))}” — {clean(q.get("from", ""))}')
        L += [clean(t) for t in (s.get('text2') or [])]
        if s.get('choose') and (C.get('mods') or {}).get('choose'):
            L.append('[고르기]'); L += [f'- {t}' for t in strings(C['mods']['choose'], 'choose', [])]
        L.append('')
    hs = [clean(d.get('h', '')) for d in (C.get('deep') or []) if d.get('h')]
    if hs: L += ['## 아래 ‘더 찾아보기’ 칸(이름만 · 글은 넣지 않았어요)'] + [f'- {h}' for h in hs] + ['']
    im = C.get('imagine') or {}
    if im.get('t'): L += ['## 눈 감고 상상해 보기', clean(im['t']), '']
    ask = (C.get('close') or {}).get('ask') or CC.get('ask')
    if ask: L += ['## 마무리 물음', clean(ask), '']
    if C.get('lines'): L += ['## ‘나의 한 줄’에서 고르는 말'] + [f'- {clean(t)}' for t in C['lines']] + ['']
    L.append('## 영화처럼 보기(자막 순서대로)')
    for fr in C.get('film', []):
        t = fr.get('type'); lines = ' / '.join(s for s in (fline(x) for x in (fr.get('lines') or [])) if s)
        if t == 'open':
            see(fr.get('img')); L.append(f'[시작] {clean(fr.get("kicker", ""))} · {clean(fr.get("title", ""))} — {lines}')
        elif t == 'chapter':
            L.append(f'[장면 제목] {clean(fr.get("t", ""))}')
        elif t in ('img', 'thennow'):
            for x in (fr.get('img'), fr.get('then'), fr.get('now')): see(x)
            L.append(f'[그림{": " + clean(fr["cap"]) if fr.get("cap") else ""}] {lines}')
        elif t == 'mod':
            L.append(f'[{MODNAME.get(fr.get("mod"), "손으로 하는 칸")}] {lines}')
        elif t == 'imagine':
            L.append(f'[눈 감고 상상] {lines}')
        elif t == 'quote':
            L.append(f'[인용] “{clean(fr.get("big", ""))}” {lines}')
        elif t == 'black':
            L.append(f'[검은 화면] {lines}')
    L.append('')
    if want_img:
        L.append('## 그림 파일(직접 보세요)')
        got = 0
        try:
            from PIL import Image
        except ImportError:
            Image = None
            print('  ⚠ PIL이 없어 그림을 옮기지 못했어요(글만 썼어요)')
        for n, k in enumerate(order, 1):
            if Image is None: break
            src = os.path.join(REPO, 'site', 'deep', cid, k + '.webp')
            if not os.path.exists(src): src = os.path.join(REPO, 'site', 'deep', cid, k + '.jpg')
            if not os.path.exists(src):
                print(f'  ⚠ 그림 {k}: site/deep/{cid}/에 없어요(먼저 빌드하세요)'); continue
            dst = os.path.join(out, f'{n:02d}_{k}.jpg')
            with Image.open(src) as g:
                g = g.convert('RGB'); g.thumbnail((1600, 1600)); g.save(dst, 'JPEG', quality=82)
            L.append(f'- {k}: {dst}'); got += 1
        if not got: L.append('- (그림을 옮기지 못했어요)')
    md = os.path.join(out, 'reader.md')
    open(md, 'w', encoding='utf-8').write('\n'.join(L).rstrip() + '\n')
    print(f'보이는 글: {md} · 글자 {len("".join(L))} · 그림 {len(order) if want_img else 0}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
