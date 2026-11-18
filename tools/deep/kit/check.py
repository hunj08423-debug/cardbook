# -*- coding: utf-8 -*-
"""깊은 카드 기계 점검 (만들고 나서 꼭 돌려요)

쓰는 법(저장소 맨 위 폴더에서):
  python3 tools/deep/kit/check.py lig-wreath [sil-score ...]      → 카드 자료 점검 + 화면 점검(넘침·오류·1~3단계·영화 끝까지)
  python3 tools/deep/kit/check.py --all                            → site/deep 의 모든 깊은 카드(본부)
  python3 tools/deep/kit/check.py --fast lig-wreath                → 화면 점검 없이 자료 점검만
결과: 문제 목록을 화면에 보여 주고, 스크린샷을 check_out/<id>/ 에 저장해요(저장소 밖: cardbook 옆 폴더).
스크린샷은 직접 열어 보세요(휴대폰 390px 밝게, 컴퓨터 1280px 어둡게, 손으로 하는 장면, 영화 마지막).
"""
import sys; sys.dont_write_bytecode = True   # 사용자 폴더에 __pycache__를 만들지 않아요
import os, sys, re, json, glob, time, subprocess, importlib.util, socket

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))
OUT = os.environ.get('DEEP_CHECK') or os.path.abspath(os.path.join(REPO, '..', 'check_out'))
BAD_WORDS = ['확인 필요', 'TODO', 'XXX', '??', 'lorem', '(출처)', '__채우기__']
SELF_MADE = ('이 안내서가 그린', '이 안내서가 만든')   # 창이 코드로 직접 그린 그림(무대 SVG·계산한 달력 등). 남의 그림·사진을 따라 그린 것은 안 돼요
ALLOWED_LIC = ('퍼블릭 도메인', 'CC0', 'CC BY', 'CC BY-SA', '공공누리 제1유형', '공공누리 1유형') + SELF_MADE

def load(cid):
    p = os.path.join(REPO, 'tools', 'deep', 'cards', cid + '.py')
    if not os.path.exists(p): return None
    spec = importlib.util.spec_from_file_location('c_' + cid.replace('-', '_'), p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CARD

def static(cid):
    """카드 자료 점검: 빈 칸, 출처, 라이선스, 자막 길이, 용량, 금지 말"""
    P, W = [], []
    C = load(cid)
    if C is None:
        return ['카드 자료 파일이 없어요: tools/deep/cards/%s.py' % cid], []
    need = ['id', 'mode', 'pagetitle', 'where', 'lead', 'leadKid', 'meta', 'draft', 'foot', 'filmlen', 'stamp', 'scenes', 'imagine', 'lines', 'linesKid', 'goals', 'deep', 'src', 'film']
    keys = set(C.get('images', {})) | {'card'}
    used = set()
    for s_ in C.get('scenes', []):
        used |= {s_.get('img'), s_.get('then'), s_.get('now')} | set(s_.get('imgs') or [])
    for f_ in C.get('film', []):
        used |= {f_.get('img'), f_.get('then'), f_.get('now')}
    for sec in C.get('deep', []): used |= set(sec.get('img') or [])
    for m_ in (C.get('mods') or {}).values():
        if isinstance(m_, dict):
            if isinstance(m_.get('img'), str) and m_['img'] != 'paper': used.add(m_['img'])
            for pr in m_.get('pairs') or []: used |= {pr.get('then'), pr.get('now')}
    used.discard(None)
    for k in sorted(used - keys): P.append(f'그림 키가 images에 없어요: {k}')
    for k in need:
        if not C.get(k): P.append(f'빈 칸: {k}')
    if C.get('id') != cid: P.append(f"id가 파일 이름과 달라요: {C.get('id')}")
    sc = C.get('scenes', [])
    if not 1 <= len(sc) <= 5: P.append(f'장면 수 {len(sc)}개: 1~5개여야 해요')
    for s in sc:
        for k in ('id', 'label', 'kind', 'kid', 'kidq'):
            if not s.get(k): P.append(f"장면 {s.get('id', '?')}: 빈 칸 {k}")
        if not (s.get('text') or s.get('quote')): P.append(f"장면 {s.get('id')}: 본문이 없어요")
        if s.get('quote') and not (s['quote'].get('from') and s['quote'].get('u')): P.append(f"장면 {s.get('id')}: 인용에 출처(from·u)가 없어요")
    for k, im in C.get('images', {}).items():
        for f in ('cr', 'u', 'alt'):
            if not im.get(f): P.append(f'그림 {k}: 빈 칸 {f}')
        if im.get('cr') and not any(l in im['cr'] for l in ALLOWED_LIC): P.append(f'그림 {k}: 라이선스가 출처 줄에 없어요(퍼블릭 도메인·CC0·CC BY·CC BY-SA·공공누리 제1유형, 직접 그린 그림은 ‘이 안내서가 그린 … · 바탕’): {im["cr"]}')
        if im.get('cr') and any(s in im['cr'] for s in SELF_MADE) and ' · ' not in im['cr']: W.append(f'그림 {k}: 직접 그린 그림은 무엇을 바탕으로 그렸는지 ‘ · ’ 뒤에 적어요(예: ‘이 안내서가 그린 달력 · 날짜는 계산으로 구함’)')
        if im.get('cr') and re.search(r'\b(NC|ND)\b|비영리|변경 금지', im['cr']): P.append(f'그림 {k}: 쓸 수 없는 라이선스(NC/ND): {im["cr"]}')
    if len(C.get('src', [])) < 3: P.append('근거(src)가 3개보다 적어요')
    for g in ('s4', 's5'):
        x = C.get('goals', {}).get(g)
        if not x or not x.get('ways'): P.append(f'{g} 목표가 없어요')
    types = [f.get('type') for f in C.get('film', [])]
    if types[:1] != ['open'] or types[-1:] != ['reward'] or 'imagine' not in types: P.append('영화: 처음은 open, 끝은 reward, 중간에 imagine이 있어야 해요')
    chs = [f for f in C.get('film', []) if f.get('type') == 'chapter']
    if len(chs) != len(sc): W.append(f'영화 장(chapter) {len(chs)}개 ≠ 장면 {len(sc)}개')
    for f in C.get('film', []):
        for ln in (f.get('lines') or []) + (f.get('kid') or []):
            t = ln.get('t', '')
            if len(t) > 64: W.append(f'영화 자막이 길어요({len(t)}자, 두 줄 넘을 수 있음): {t[:30]}…')
    blob = json.dumps(C, ensure_ascii=False)
    for w in BAD_WORDS:
        if w in blob: P.append(f'남은 메모·빈 말: “{w}”')
    if '개역개정' in blob and 'bible.bskorea.or.kr' not in blob: W.append('성경을 말하면 대한성서공회 개역개정 링크(bible.bskorea.or.kr/bible/NKRV/…)를 달아요')
    od = os.path.join(REPO, 'site', 'deep', cid)
    if os.path.isdir(od):
        tot = 0
        for f in os.listdir(od):
            sz = os.path.getsize(os.path.join(od, f)); tot += sz
            if f.endswith(('.jpg', '.webp')):
                try:
                    from PIL import Image
                    big = max(Image.open(os.path.join(od, f)).size) > 1920
                except Exception: big = False
                lim = 1536 if big else 1024
                if sz > (lim + 32) * 1024: W.append(f'그림이 커요: {f} {sz // 1024}KB(기준서: 한 장 {"1.5MB" if big else "1MB"} 안쪽. 빌드가 품질을 낮춰도 크면 \'max\'를 줄여요)')
            if f.endswith(('.mp3', '.ogg', '.m4a')) and sz > 1024 * 1024: W.append(f'소리가 커요: {f} {sz // 1024}KB(기준서: 한 개 1MB 안쪽)')
            if f.endswith(('.jpg', '.webp')):
                try:
                    from PIL import Image
                    w_, h_ = Image.open(os.path.join(od, f)).size
                    if max(w_, h_) > 2600: W.append(f'그림이 커요: {f} 긴 쪽 {max(w_, h_)}px(기준서: 1920px, 자세히 볼 그림만 2560px까지)')
                    if max(w_, h_) < 1000 and f.split('.')[0] != 'card': W.append(f'그림이 작아요: {f} 긴 쪽 {max(w_, h_)}px(크게 볼 때 흐려요. 더 큰 파일이 있으면 바꿔요)')
                except Exception: pass
        snd = sum(os.path.getsize(os.path.join(od, f)) for f in os.listdir(od) if f.endswith(('.mp3', '.ogg', '.m4a')))
        if tot - snd > 6.5 * 1024 * 1024: W.append(f'그림 합계가 커요: {(tot - snd) // 1024}KB(기준서: 카드 하나 6MB 안쪽)')
        hp = os.path.join(REPO, 'site', 'deep', cid + '.html')
        if os.path.exists(hp):
            h = open(hp, encoding='utf-8').read()
            miss = sorted({m for m in re.findall(re.escape(cid) + r'/[A-Za-z0-9_.\-]+\.(?:jpg|png|webp|svg|mp3|ogg|m4a)', h) if not os.path.exists(os.path.join(REPO, 'site', 'deep', m))})
            if miss: P.append(f'페이지가 부르는 파일이 없어요: {miss[:5]}')
            unused = sorted(set(os.listdir(od)) - {m.split('/', 1)[1] for m in re.findall(re.escape(cid) + r'/[A-Za-z0-9_.\-]+', h)})
            if unused: W.append(f'쓰지 않는 파일(지워도 돼요): {unused[:5]}')
        else:
            P.append('만든 결과가 없어요: build.py를 먼저 돌려 주세요')
    else:
        P.append('만든 결과가 없어요: build.py를 먼저 돌려 주세요')
    return P, W

def ending(cid):
    """5단계 마무리 종류: 고르기 · 방식 마무리 · 아이와 끝까지"""
    C = load(cid)
    if not C: return None
    ways = [w.get('id') for w in (C.get('goals', {}).get('s5', {}) or {}).get('ways', [])]
    if 'choose' in ways: return '고르기'
    if [w for w in ways if w != 'kid']: return '방식 마무리'
    return '아이와 끝까지'

MOD_NAMES = {'look': '찾아보기', 'reveal': '비추기', 'place': '놓아 보기', 'slider': '그때와 지금', 'route': '지도 위 길',
             'voices': '소리', 'wreath': '날짜 따라가기', 'choose': '고르기'}

def methods(cid):
    """(중심 방식, [도우미…]) — 장면에 쓴 방식과 도우미 장면 종류"""
    C = load(cid)
    if not C: return None
    mods = list((C.get('mods') or {}).keys())
    central = next((m for m in mods if m != 'choose'), None)
    if not central:
        central = next((s_.get('mod') for s_ in C.get('scenes', []) if s_.get('kind') == 'mod'), None)
    helpers = sorted({s_.get('kind') for s_ in C.get('scenes', []) if s_.get('kind') in ('duo', 'thennow')} | ({'choose'} if 'choose' in mods else set()))
    return central, helpers

def method_report(ids, batch=True):
    """여러 카드를 함께 점검할 때: 중심 방식·도우미가 한쪽으로 몰리지 않았나(기준서 1판 보탬 9)"""
    M = [(c, methods(c)) for c in ids]; M = [(c, m) for c, m in M if m and m[0]]
    if len(M) < 2: return
    from collections import Counter
    cc = Counter(m[0] for _, m in M); hc = Counter(h for _, m in M for h in m[1])
    print('중심 방식: ' + ' · '.join(f'{MOD_NAMES.get(k, k)} {v}' for k, v in cc.most_common()) + f' (카드 {len(M)}장)')
    if hc: print('도우미: ' + ' · '.join(f"{ {'duo': '두 그림 나란히', 'thennow': '그때와 지금 탭', 'choose': '고르기'}.get(k, k)} {v}" for k, v in hc.most_common()))
    if batch:
        for k, v in cc.items():
            if v > 2: print(f'  살펴볼 묶음 안에서 {MOD_NAMES.get(k, k)}이(가) {v}장이에요(두 장까지).')
        for k, v in hc.items():
            if v > 2 and k != 'choose': print(f'  살펴볼 묶음 안에서 도우미 {k}이(가) {v}장이에요(두 장까지).')
    elif cc.get('look', 0) * 4 > len(M) + 3:
        print('  살펴볼 찾아보기가 네 장에 한 장보다 많아요(장마다 네 장에 한 장쯤까지).')

def ending_report(ids, batch=True):
    """여러 카드를 함께 점검할 때: 5단계 마무리가 한 가지로 몰리지 않았나(기준서 1판 보탬 8)"""
    E = [(c, ending(c)) for c in ids]; E = [(c, e) for c, e in E if e]
    if len(E) < 2: return
    n = {k: sum(1 for _, e in E if e == k) for k in ('고르기', '방식 마무리', '아이와 끝까지')}
    print(f"5단계 마무리: 고르기 {n['고르기']} · 방식 마무리 {n['방식 마무리']} · 아이와 끝까지 {n['아이와 끝까지']} (카드 {len(E)}장)")
    if batch:
        if n['고르기'] > 2: print('  살펴볼 묶음 안 고르기가 두 장을 넘어요. 몇 장을 다른 마무리로 바꿔요(GUIDE.md 2장).')
        for (a, ea), (b, eb) in zip(E, E[1:]):
            if ea == eb == '고르기': print(f'  살펴볼 붙은 두 카드가 연달아 고르기로 끝나요: {a}, {b}')
    elif n['고르기'] * 3 > len(E) + 2:
        print('  살펴볼 고르기로 끝나는 카드가 세 장에 한 장보다 많아요(장을 마칠 때 본부가 고르게 해요).')

def free_port():
    s = socket.socket(); s.bind(('127.0.0.1', 0)); p = s.getsockname()[1]; s.close(); return p

def browser(ids):
    from playwright.sync_api import sync_playwright
    port = free_port()
    srv = subprocess.Popen([sys.executable, '-m', 'http.server', str(port), '-d', os.path.join(REPO, 'site')], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.0)
    res = {}
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for cid in ids:
                od = os.path.join(OUT, cid); os.makedirs(od, exist_ok=True)
                R = {'problems': [], 'notes': []}
                url = f'http://127.0.0.1:{port}/deep/{cid}.html'
                for vw, vh, sch in [(390, 844, 'light'), (1280, 900, 'dark'), (390, 844, 'dark'), (1280, 900, 'light')]:
                    ctx = b.new_context(viewport={'width': vw, 'height': vh}, color_scheme=sch)
                    pg = ctx.new_page(); errs = []
                    pg.on('pageerror', lambda e: errs.append(str(e)))
                    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' and 'Failed to load resource' not in m.text else None)
                    pg.goto(url); pg.wait_for_timeout(700)
                    sw = pg.evaluate('document.documentElement.scrollWidth'); cw = pg.evaluate('document.documentElement.clientWidth')
                    if sw > cw: R['problems'].append(f'{vw}px {sch}: 화면이 옆으로 넘쳐요({sw}>{cw})')
                    if errs: R['problems'].append(f'{vw}px {sch}: 오류 {errs[:3]}')
                    broken = pg.evaluate("[...document.images].filter(i => i.getAttribute('src') && i.complete && i.naturalWidth === 0 && !i.src.startsWith('data:')).map(i => i.getAttribute('src'))")
                    if broken: R['problems'].append(f'깨진 그림: {broken[:5]}')
                    if (vw, sch) in ((390, 'light'), (1280, 'dark')):
                        pg.screenshot(path=os.path.join(od, f'{vw}_{sch}_top.png'))
                        m = pg.query_selector('[data-mod]:not([data-mod="choose"])') or pg.query_selector('[data-mod]')
                        if m:
                            m.scroll_into_view_if_needed(); pg.wait_for_timeout(900)
                            m.screenshot(path=os.path.join(od, f'{vw}_{sch}_mod.png'))
                    ctx.close()
                # 흐름: 1단계(앞면 이야기) → 2단계(장면 다 지나가기) → 3단계(한 줄) → 영화 끝까지
                ctx = b.new_context(viewport={'width': 390, 'height': 844}); pg = ctx.new_page(); errs = []
                pg.on('pageerror', lambda e: errs.append(str(e)))
                pg.goto(url); pg.wait_for_timeout(500)
                st = lambda: pg.evaluate("() => JSON.parse(localStorage.getItem('deep3-' + DATA.id) || '{}')")
                pg.click('#openStory2')
                for _ in range(15):
                    if pg.is_hidden('#story'): break
                    pg.click('#stNext'); pg.wait_for_timeout(100)
                for sel in pg.evaluate("[...document.querySelectorAll('.sc')].map(s => '#' + s.id).concat(['#imagine'])"):
                    pg.eval_on_selector(sel, 'e => e.scrollIntoView({block: "center"})'); pg.wait_for_timeout(300)
                pg.click('.line.a'); pg.click('#stampBtn'); pg.wait_for_timeout(300)
                ach = st().get('ach', {})
                for k in ('s1', 's2', 's3'):
                    if k not in ach: R['problems'].append(f'{k} 단계가 오르지 않아요')
                pg.click('#filmBtn'); pg.wait_for_timeout(300); pg.click('#fGo'); pg.wait_for_timeout(400)
                seen, reached, shot = set(), False, False   # shot: 이번에 film_mod를 찍었나(돌릴 때마다 새로 찍어요)
                for _ in range(120):
                    info = pg.evaluate("() => ({fi, wait: fWait, type: DATA.film[fi] && DATA.film[fi].type})")
                    seen.add(info['fi'])
                    if info['type'] == 'mod' and not shot:
                        pg.wait_for_timeout(2500); pg.screenshot(path=os.path.join(od, 'film_mod.png')); shot = True
                    if info['type'] == 'reward': reached = True; break
                    pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(220)
                pg.wait_for_timeout(2200); pg.screenshot(path=os.path.join(od, 'film_end.png'))
                if not reached: R['problems'].append('영화처럼 보기가 마지막(reward)까지 가지 않아요')
                if errs: R['problems'].append(f'흐름 중 오류: {errs[:3]}')
                R['notes'].append(f'영화 장면 {len(seen)}개 지나감 · 스크린샷: {od}')
                ctx.close(); res[cid] = R
            b.close()
    finally:
        srv.terminate()
    return res

if __name__ == '__main__':
    args = sys.argv[1:]; fast = '--fast' in args
    args = [a for a in args if a != '--fast']
    all_mode = '--all' in args
    if all_mode:
        args = sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(REPO, 'site', 'deep', '*.html')) if os.path.basename(f) != 'sinai.html')
    total = 0
    st = {cid: static(cid) for cid in args}
    br = {} if fast else browser([c for c in args if os.path.exists(os.path.join(REPO, 'site', 'deep', c + '.html'))])
    for cid in args:
        P, W = st[cid]
        P = P + br.get(cid, {}).get('problems', [])
        total += len(P)
        print(f'■ {cid}: 문제 {len(P)} · 살펴볼 것 {len(W)}')
        for x in P: print('  문제  ', x)
        for x in W: print('  살펴볼', x)
        for x in br.get(cid, {}).get('notes', []): print('  ', x)
    method_report(args, batch=not all_mode)
    ending_report(args, batch=not all_mode)
    print('끝: 문제 %d개' % total + (' — 모두 고친 뒤 다시 돌려 주세요' if total else ' — 통과'))
    sys.exit(1 if total else 0)
