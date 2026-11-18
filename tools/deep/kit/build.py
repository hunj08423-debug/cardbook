# -*- coding: utf-8 -*-
"""깊은 카드 만들기 (공통 틀 deep3, 저장소용)

쓰는 법(저장소 맨 위 폴더에서):
  python3 tools/deep/kit/build.py tools/deep/cards/<카드id>.py [...]          → site/deep/<id>.html + site/deep/<id>/
  python3 tools/deep/kit/build.py --all                                        → cards 폴더의 카드를 모두 다시 만들기(틀이 바뀌었을 때, 본부)
  python3 tools/deep/kit/build.py --preview <폴더> tools/deep/cards/<id>.py ...  → 검토용 미리보기(아티팩트로 게시할 폴더)

카드 내용은 tools/deep/cards/<id>.py 의 CARD 하나에만 적어요. 틀(deep3_tpl.html)은 고치지 않아요.
그림·소리의 'src'/'file'은 원본 폴더(DEEP_SRC, 기본 cardbook 옆 deep_src/) 기준 경로예요. 원본은 저장소에 넣지 않아요.
원본이 없으면(다른 컴퓨터, 다시 만들기) 이미 만들어 둔 site/deep/<id>/ 의 파일을 그대로 다시 써요.
"""
import sys; sys.dont_write_bytecode = True   # 사용자 폴더에 __pycache__를 만들지 않아요
import json, os, sys, html, shutil, importlib.util, glob, re, io
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None    # 원본(아주 큰 그림)도 열어요. 위키미디어에서 출처를 확인하고 받은 파일만 다뤄요

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))
# 받은 원본 그림·소리를 두는 곳: 저장소 밖(커밋되지 않게). 기본은 cardbook 옆의 deep_src 폴더.
SRCROOT = os.environ.get('DEEP_SRC') or os.path.abspath(os.path.join(REPO, '..', 'deep_src'))
e = lambda s: html.escape(str(s), quote=True)
TPLV = 'deep3-5'          # 틀 판(틀을 바꾸면 본부가 올려요) · 3: 놓아 보기·그때와 지금 문구 칸, 품질 85 · 4: 새 방식 여섯(키트 3판), 천천히 읽기 단추, 가로 앞면 그림 · 5: 그림 두 벌(큰 그림), 원본에서 만들기, 품질 90
# 그림 두 벌(기준서 2판 보탬 2 · 2026-11-18): 보통 그림은 긴 쪽 1920 이하, 큰 그림(<키>.big.webp)은 원본이 충분히 클 때 긴 쪽 3840까지.
# 큰 그림은 화면에 크게 보일 때만(큰 화면·확대·영화) 틀이 불러요. 원본이 같은 카드 폴더의 _orig/에 있으면 그것으로 만들어요.
BASE_MAX, BIG_MAX = 1920, 3840
BASE_Q, BIG_Q = (90, 88, 85, 82), (90, 88, 85)      # WebP 품질: 앞의 것부터, 한 장 크기를 넘을 때만 다음 것으로
BASE_CAP, BIG_CAP = 2 * 1024 * 1024, 6 * 1024 * 1024
BIG_GAIN = 1.15                  # 원본이 보통 그림보다 이만큼 이상 클 때만 큰 그림을 만들어요
PREVIEW_BIG_BUDGET = 36 * 1024 * 1024   # 미리 보기(아티팩트)에 넣는 큰 그림 합계(한 번 올리기 64MB 안쪽이 되게)
PREVIEW_USED = [0]
AVAIL = set()             # 틀에 들어 있는 손 방식(build 때 채움)

STAGE_BASE = [
    {'n': 1, 't': '양피지', 'done': '이야기를 끝까지 보고 카드를 받았어요', 'how': '카드의 ‘이야기 펼치기’나 ‘영화처럼 보기’를 끝까지 보면 받아요'},
    {'n': 2, 't': '먹 글씨', 'done': '그 자리에 서서 장면을 끝까지 걸었어요', 'how': '장면을 끝까지 걷거나, ‘영화처럼 보기’를 끝까지 보세요'},
    {'n': 3, 't': '붉은 머리글자', 'done': '나의 한 줄을 남기고 도장을 받았어요', 'how': '‘나의 자리’에 한 줄을 남겨 보세요'},
]

def site_data(repo):
    cards, sets = {}, {}
    for f in sorted(glob.glob(os.path.join(repo, 'site', 'data', 'ch-*.json'))):
        cards.update(json.load(open(f, encoding='utf-8'))['cards'])
    ix = json.load(open(os.path.join(repo, 'site', 'data', 'index.json'), encoding='utf-8'))
    return cards, ix['sets'], ix

def load(path):
    if os.path.basename(os.path.dirname(os.path.abspath(path))) == 'examples':
        sys.exit('이 파일은 새 방식 예시 자료예요(kit/examples). 빌드하지 않아요: 같은 id의 진짜 카드를 덮어쓸 수 있어요. 자료 모양만 보고 cards/의 맡은 카드에 옮겨 적어요.')
    spec = importlib.util.spec_from_file_location('card_' + os.path.basename(path)[:-3].replace('-', '_'), path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CARD

def tpl():
    return open(os.path.join(KIT, 'deep3_tpl.html'), encoding='utf-8').read()

PSHARED = 'deep3'          # 미리보기(아티팩트)용 공유 폴더 이름: 아티팩트 서버는 ‘_’로 시작하는 경로를 받지 않아요
LIVE_DEEP = 'https://cardbook.hunji08423.workers.dev/deep/'   # 미리 보기에서 다른 카드로 가는 길(뒷이야기)
SHARED = '_deep3'            # 모든 깊은 카드가 같이 쓰는 틀 파일(site/deep/_deep3/deep3.css·deep3.js). 본부만 사용자 폴더에 넣어요.
JS_HEAD = "document.documentElement.classList.add('js');\nconst DATA = /*__DATA__*/null;\n"

def shared_parts():
    """틀에서 카드마다 같은 부분(스타일·스크립트)을 떼어 내요. 반환: (css, js)"""
    t = tpl()
    a0, a1 = t.index('<style>') + len('<style>'), t.index('</style>')
    css = t[a0:a1].replace('aspect-ratio:{{CARDW}}/{{CARDH}}', 'aspect-ratio:var(--card-ar)').replace('/*__THEME__*/', '')
    b0, b1 = t.index('<script>') + len('<script>'), t.index('</script>')
    js = t[b0:b1]
    assert js.startswith('\n' + JS_HEAD), '틀 스크립트 첫머리가 달라요'
    js = js[len('\n' + JS_HEAD):]
    assert '{{' not in css and '{{' not in js and '__DATA__' not in js
    return css, js

def write_shared(site_dir):
    css, js = shared_parts()
    d = os.path.join(site_dir, SHARED); os.makedirs(d, exist_ok=True)
    for name, txt in (('deep3.css', css), ('deep3.js', js)):
        f = os.path.join(d, name)
        if not os.path.exists(f) or open(f, encoding='utf-8').read() != txt:
            open(f, 'w', encoding='utf-8').write(txt)
    return d

def mods_in_tpl():
    return set(re.findall(r'MODS\.(\w+)\s*=', tpl()))

def gen_mod_html(name, cfg, have, IM):
    """자료만 적으면 되는 공통 방식(찾아보기·비추기·그때와 지금·지도 위 길·고르기)의 HTML. 없는 방식이면 None."""
    try:
        import modhtml
    except ImportError:
        return None
    f = getattr(modhtml, name, None)
    return f(cfg, have, IM) if f else None

ORIG_EXT = ('.jpg', '.jpeg', '.png', '.tif', '.tiff', '.gif', '.webp')
def orig_path(src):
    """받은 그림 src의 원본(같은 카드 폴더의 _orig/, 본부가 다시 받은 것)이 있으면 그 경로. 없으면 None"""
    d, fn = os.path.split(src); od = os.path.join(d, '_orig')
    if not os.path.isdir(od): return None
    cands = [fn]
    if fn.lower().endswith('.jpg'): cands.append(fn[:-4])                      # ‘이름.tif.jpg’ → ‘이름.tif’
    st = os.path.splitext(fn)[0]; cands += [st + x for x in ORIG_EXT]
    for c in cands:
        p = os.path.join(od, c)
        if os.path.isfile(p): return p
    return None

def _oriented(I):
    """EXIF 방향까지 셈한 (가로, 세로) — 열지 않고 머리만 읽어요"""
    w, h = I.size
    try: o = I.getexif().get(274, 1)
    except Exception: o = 1
    return (h, w) if o in (5, 6, 7, 8) else (w, h)

def open_src(path, need=None, crop=None):
    """그림 열기: 아주 큰 JPEG는 필요한 크기 가까이로 줄여 읽고(draft), EXIF 방향을 바로잡고, 색 공간을 sRGB로, 8비트 RGB로."""
    I = Image.open(path)
    if need and I.format == 'JPEG':
        W, H = _oriented(I)
        l, t, r, b = crop or (0, 0, 1, 1)
        cl = max((r - l) * W, (b - t) * H)
        if cl > need:
            k = need / cl
            I.draft('RGB', (max(1, int(I.size[0] * k) + 1), max(1, int(I.size[1] * k) + 1)))
    I.load()
    try: I = ImageOps.exif_transpose(I)
    except Exception: pass
    if I.mode in ('I;16', 'I;16B', 'I;16L', 'I', 'F'):
        import numpy as np
        a = np.asarray(I).astype('float64'); mx = a.max() or 1
        I = Image.fromarray((a * (255.0 / (65535 if mx > 255 else 255))).clip(0, 255).astype('uint8'), 'L')
    icc = I.info.get('icc_profile')
    if icc and I.mode in ('RGB', 'CMYK'):
        try:
            from PIL import ImageCms
            pr = ImageCms.ImageCmsProfile(io.BytesIO(icc))
            name = (ImageCms.getProfileDescription(pr) or '').lower().replace(' ', '')
            if I.mode == 'CMYK' or 'srgb' not in name:
                I = ImageCms.profileToProfile(I, pr, ImageCms.createProfile('sRGB'), outputMode='RGB')
        except Exception as ex:
            print(f'  (색 공간을 바꾸지 못했어요: {os.path.basename(path)} — {type(ex).__name__})')
    if I.mode not in ('RGB', 'L'): I = I.convert('RGB')
    return I

def srckey(im):
    """그림 자료(src·crop)를 알아보는 짧은 표(큰 그림을 지킬지 정할 때). 파일 경로처럼 보이지 않게 해시로"""
    import hashlib
    return hashlib.sha1(f"{im.get('src')}|{im.get('crop')}".encode('utf-8')).hexdigest()[:12]

def save_webp(I, out, qs, cap):
    """품질 qs의 앞의 것부터 저장하고, 한 장 크기(cap)를 넘을 때만 다음 품질로"""
    for q in qs:
        I.save(out, 'WEBP', quality=q, method=5)
        if os.path.getsize(out) <= cap: return q
    return qs[-1]

def build(C, repo=REPO, preview=None):
    global AVAIL
    AVAIL = mods_in_tpl()
    CARDS, SETS, _ = site_data(repo)
    cid = C['id']; assert cid in CARDS, f'site/data에 없는 카드 id: {cid}'
    CC = CARDS[cid]; SS = SETS[CC['set']]
    site_dir = os.path.join(repo, 'site', 'deep')
    od = os.path.join(site_dir, cid)                       # 사이트 자산 폴더
    os.makedirs(od, exist_ok=True)
    IM = dict(C['images'])
    # 앞면 그림: 따로 적지 않으면 사이트 카드 그림(site/img/c/<id>.webp)을 씀
    fmt = C.get('imgfmt', 'webp')                      # 그림 형식: 기본 WebP(같은 용량에 더 선명). 예시 세 장은 'jpg'
    ext = '.webp' if fmt == 'webp' else '.jpg'
    if 'card' not in IM:                               # 앞면 그림: 따로 적지 않으면 사이트 카드 그림(긴 쪽 1200 안팎)
        IM['card'] = {'src': os.path.join(repo, 'site', 'img', 'c', cid + '.webp'), 'max': 1200 if fmt == 'webp' else 900, 'q': 84, 'cr': CC['cr'], 'u': CC.get('cru', ''), 'alt': CC['alt']}
    have = {}
    big_note = []
    old_bigsrc, bigsrc = {}, {}                  # 큰 그림을 어느 원본·자르기로 만들었는지(다른 창이 _orig 없이 다시 빌드해도 큰 그림을 지키려고)
    try:
        h0 = open(os.path.join(site_dir, cid + '.html'), encoding='utf-8').read(); j0 = h0.index('const DATA = ') + len('const DATA = ')
        old_bigsrc = json.JSONDecoder().raw_decode(h0, j0)[0].get('bigsrc') or {}
    except Exception: pass
    for k, im in IM.items():
        out = os.path.join(od, k + ext)
        bout = os.path.join(od, k + '.big' + ext)
        src = im.get('src')
        if src and not os.path.isabs(src): src = os.path.join(SRCROOT, src)
        made_big = False
        if src and os.path.exists(src):
            mx = min(im.get('max', BASE_MAX if fmt == 'webp' else 1280), BASE_MAX)
            want = im.get('big', BIG_MAX if im.get('max', BASE_MAX) >= BASE_MAX else 0)
            if want is True: want = BIG_MAX
            want = int(want or 0) if fmt == 'webp' else 0
            use = src
            op = orig_path(src)
            if op:                                    # 원본이 있으면: 받아 둔 판과 비율이 같은지 보고(방향·다른 그림 막기) 원본으로
                try:
                    with Image.open(src) as a, Image.open(op) as b:
                        (aw, ah), (bw, bh) = _oriented(a), _oriented(b)
                    if abs(aw / ah - bw / bh) <= 0.02 * (aw / ah): use = op
                    else: print(f'  ⚠ {k}: _orig의 원본 비율이 받아 둔 판과 달라요({bw}×{bh} · {aw}×{ah}) — 받아 둔 판으로 만들어요')
                except Exception as ex:
                    print(f'  ⚠ {k}: 원본을 열지 못했어요({type(ex).__name__}) — 받아 둔 판으로 만들어요')
            try: I = open_src(use, max(mx, want), im.get('crop'))
            except Exception as ex:                 # 원본이 깨졌거나(받다 끊김) 열 수 없으면 받아 둔 판으로
                if use == src: raise
                print(f'  ⚠ {k}: 원본을 읽지 못했어요({type(ex).__name__}: {str(ex)[:60]}) — 받아 둔 판으로 만들어요'); use = src
                I = open_src(use, max(mx, want), im.get('crop'))
            if im.get('crop'):
                l, t, r, b = im['crop']; w, h = I.size
                I = I.crop((round(l * w), round(t * h), round(r * w), round(b * h)))
            if I.mode == 'L': I = I.convert('RGB')
            L0 = max(I.size)
            B = I
            if L0 > mx:
                sc = mx / L0; B = I.resize((round(I.width * sc), round(I.height * sc)), Image.LANCZOS)
            if fmt == 'webp':                          # 품질 90(기준서 2판 보탬 2). 한 장 2MB를 넘을 때만 조금씩 낮춰요
                save_webp(B, out, [im['q']] if im.get('q') else BASE_Q, BASE_CAP)
            else: B.save(out, 'JPEG', quality=im.get('q', 80), optimize=True, progressive=True)
            if want and L0 > max(B.size) * BIG_GAIN:  # 큰 그림: 원본이 보통 그림보다 충분히 클 때만
                G = I
                if L0 > want:
                    sc = want / L0; G = I.resize((round(I.width * sc), round(I.height * sc)), Image.LANCZOS)
                save_webp(G, bout, [im['bq']] if im.get('bq') else BIG_Q, BIG_CAP); made_big = True
                bigsrc[k] = srckey(im) + (':orig' if use != src else ':src')
            elif want and use == src and max(B.size) >= mx and '/_orig/' not in use.replace('\\', '/'):
                big_note.append(k)
            if not made_big and os.path.exists(bout):
                ob = old_bigsrc.get(k, '')
                if want and use == src and ob.startswith(srckey(im) + ':'):   # 같은 그림·같은 자르기로 본부가 원본에서 만든 큰 그림: 그대로 둬요
                    bigsrc[k] = ob; big_note.remove(k) if k in big_note else None
                else: os.remove(bout)               # 그림이 바뀌었거나 큰 그림이 필요 없어졌으면 치워요(이 카드가 만든 것)
        elif not os.path.exists(out):
            raise SystemExit(f'그림이 없어요: {k} (src={src}) — commons_get.py로 받거나 경로를 고쳐 주세요')
        I = Image.open(out)
        have[k] = {'u': f'{cid}/{k}{ext}', 'w': I.width, 'h': I.height}
        if os.path.exists(bout):
            with Image.open(bout) as G: have[k].update({'b': f'{cid}/{k}.big{ext}', 'bw': G.width, 'bh': G.height})
    if big_note: print(f'  · 큰 그림을 못 만든 그림 {len(big_note)}개(받아 둔 판이 작아요. 원본을 받으면 더 선명해져요): ' + ', '.join(big_note))
    for s in C.get('sounds', []):
        dst = os.path.join(od, os.path.basename(s['file']))
        src = s['file'] if os.path.isabs(s['file']) else os.path.join(SRCROOT, s['file'])
        if os.path.exists(src) and os.path.abspath(src) != os.path.abspath(dst): shutil.copy(src, dst)
        elif not os.path.exists(dst): raise SystemExit(f'소리 파일이 없어요: {s["file"]}')
    def credit(k):
        return f'<a href="{e(IM[k]["u"])}" target="_blank" rel="noopener">{e(IM[k]["cr"])}</a>' if IM[k].get('u') else e(IM[k]['cr'])
    def fig(k, cls='ph', cap=None):
        h = have[k]
        if h['h'] > h['w'] * 1.1 and 'side' not in cls and 'induo' not in cls: cls += ' tall'
        c = (e(cap) + ' · ' if cap else (e(IM[k]['cap']) + ' · ' if IM[k].get('cap') else '')) + credit(k)
        return (f'<figure class="{cls}"><div class="frame"><img src="{h["u"]}" width="{h["w"]}" height="{h["h"]}" alt="{e(IM[k]["alt"])}" loading="lazy" decoding="async"></div>'
                f'<figcaption>{c}</figcaption></figure>')
    paras = lambda lst: ''.join(f'<p class="tx">{t}</p>' for t in (lst or []))
    def quote(q, cls='jr'):
        if not q: return ''
        cite = f'<a href="{e(q["u"])}" target="_blank" rel="noopener">{e(q["from"])}</a>' if q.get('u') else e(q['from'])
        return f'<blockquote class="{cls}"><p>“{e(q["t"])}”</p><cite>{cite}</cite></blockquote>'
    sc_html = []
    for i, s in enumerate(C['scenes'], 1):
        pre, vis, k = paras(s.get('text')), '', s['kind']
        if k == 'photo':
            vis = fig(s['img'], cap=s.get('cap'))
        elif k == 'duo':
            vis = '<div class="duo">' + ''.join(fig(x, 'ph induo', c) for x, c in zip(s['imgs'], s.get('caps', [None] * len(s['imgs'])))) + '</div>'
        elif k == 'thennow':
            t, n = have[s['then']], have[s['now']]
            capt = lambda key: ((e(IM[key]['cap']) + ' · ') if IM[key].get('cap') else '') + credit(key)
            tid = '' if '<div class="tn" id="tn"' in ''.join(sc_html) else ' id="tn"'      # 틀의 탭 동작은 첫 ‘그때와 지금’ 하나에 붙어요
            vis = (f'<div class="tn"{tid} data-state="then"><div class="tn-tabs" role="tablist" aria-label="그때와 지금">'
                   f'<button type="button" role="tab" aria-selected="true" data-v="then">{e(s["thenT"])}</button><button type="button" role="tab" aria-selected="false" data-v="now">{e(s["nowT"])}</button></div>'
                   f'<figure class="ph tnfig"><div class="frame" style="aspect-ratio:{n["w"]}/{n["h"]}">'
                   f'<img class="tn-then" src="{t["u"]}" alt="{e(IM[s["then"]]["alt"])}" loading="lazy" decoding="async"><img class="tn-now" src="{n["u"]}" alt="{e(IM[s["now"]]["alt"])}" loading="lazy" decoding="async"></div>'
                   f'<figcaption><span class="cap-then">{capt(s["then"])}</span><span class="cap-now">{capt(s["now"])}</span></figcaption></figure></div>')
        elif k == 'mod':
            mh = (C.get('modhtml') or {}).get(s['mod'])
            if mh is None and s['mod'] in AVAIL: mh = gen_mod_html(s['mod'], C['mods'][s['mod']], have, IM)
            if mh is None or s['mod'] not in AVAIL:
                print(f"  ⚠ {cid}: ‘{s['mod']}’ 방식이 아직 틀에 없어요 → 이 장면은 그림만 보여 줘요(방식이 들어오면 다시 빌드)")
                fb = s.get('img') or (C.get('mods', {}).get(s['mod'], {}) or {}).get('img') or 'card'
                vis = fig(fb if fb in have else 'card', cap=s.get('cap'))
            else:
                vis = (fig(s['img'], cap=s.get('cap')) if s.get('img') else '') + mh
        elif k == 'quote':
            vis = fig(s['img'], cap=s.get('cap')) if s.get('img') else ''
        else:
            raise SystemExit(f'모르는 장면 종류: {k}')
        if s.get('snds'):
            vis += '<div class="snds">' + ''.join(
                f'<button type="button" class="snd1" data-u="{e(cid + "/" + x["u"].split("/")[-1])}" aria-pressed="false"' + (f' data-ev="{e(x["ev"])}"' if x.get('ev') else '') + '>'
                f'<span class="pb" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5l11 7-11 7z" fill="currentColor"/></svg></span><span><b>{e(x["t"])}</b><span>{e(x["d"])}</span></span></button>'
                for x in s['snds']) + '</div>'
        post = quote(s.get('quote'), 'jr big' if k == 'quote' else 'jr') + paras(s.get('text2'))
        if s.get('choose'):                                  # 도우미 ‘고르기’: 장면 끝에
            if 'choose' in AVAIL and (C.get('mods') or {}).get('choose'):
                post += gen_mod_html('choose', C['mods']['choose'], have, IM) or ''
            else:
                print(f"  ⚠ {cid}: ‘고르기’가 아직 틀에 없거나 mods['choose']가 없어요 → 빼고 만들어요")
        kid = f'<div class="k kidwrap"><p class="kidline">{e(s["kid"])}</p><p class="kidq"><b>물어보기</b>{e(s["kidq"])}</p></div>'
        cls = 'sc night' if s.get('night') else 'sc'
        sc_html.append(f'''<section class="{cls}" id="sc-{s["id"]}" data-sc="{s["id"]}"><div class="sc-head"><span class="no">{i}</span><h2>{e(s["label"])}</h2><button type="button" class="fromhere" data-ch="{i}">▶ 여기부터 크게</button></div>
{('<div class="a">' + pre + '</div>') if pre else ''}{vis}{('<div class="a">' + post + '</div>') if post else ''}{kid}</section>''')
    deep = []
    for sec in C['deep']:
        inner = ''
        imgs = [x for x in (sec.get('img') or []) if x in have]
        if imgs: inner += '<div class="sidepair">' + ''.join(fig(x, 'ph side') for x in imgs) + '</div>'
        if sec.get('checked'): inner += f'<p class="checked">확인한 날 · {e(sec["checked"])} · 바뀌기 쉬운 정보라 정기적으로 다시 확인해요</p>'
        inner += ''.join(f'<p>{t}</p>' for t in sec.get('p', []))
        if sec.get('links'):
            inner += '<ul class="links">' + ''.join(f'<li><a href="{e(l["u"])}" target="_blank" rel="noopener">{e(l["t"])}</a>{(" <span>" + e(l["m"]) + "</span>") if l.get("m") else ""}</li>' for l in sec['links']) + '</ul>'
        deep.append(f'<details class="dp"><summary><span>{e(sec["h"])}</span></summary><div class="dpb">{inner}</div></details>')
    # 더 깊이 ‘궁금증’(2026-11-19 본부): 물음 카드(그림 한 장 · 두세 문장 · 짧은 영화). 있으면 맨 위에, 참고 칸은 ‘더 찾아보기’ 아래로
    def filmref(sh):
        sh = dict(sh)
        for key in ('img', 'then', 'now'):
            if sh.get(key):
                k = sh[key]; sh[key] = {'u': have[k]['u'], 'w': have[k]['w'], 'h': have[k]['h'], 'alt': IM[k]['alt']}
                if have[k].get('bw'): sh[key].update(bw=have[k]['bw'], bh=have[k]['bh'])
        if sh.get('lines') and not sh.get('kid'): sh['kid'] = sh['lines']
        sh.setdefault('ch', 0)
        return sh
    qs_html, qs_data = '', []
    # ‘다시 보면’(2026-11-19 본부 · 사용자님 고름): 답을 알고 나서 그 장면이 ‘무엇으로’ 보이는지 한 줄 + 작은 그림 + 그 장면으로 가는 단추
    SCN = {s['id']: (i, s) for i, s in enumerate(C['scenes'], 1)}
    ORD = ['첫', '둘째', '셋째', '넷째', '다섯째', '여섯째', '일곱째', '여덟째', '아홉째', '열째']
    def see_go_t(sid):
        if sid == 'front': return '앞면 카드 다시 보기'
        i, s = SCN[sid]; return f'{ORD[i - 1]} 장면 다시 보기'   # 다시 보면 글에 이미 ‘○째 장면의 …’가 있어서 단추는 짧게(좁은 칸에서도 한 줄)
    def scene_img(sid):
        if sid == 'front': return 'card' if 'card' in have else None
        s = SCN[sid][1]
        k = s.get('img') or s.get('now') or s.get('then')
        if not k and s.get('mod'): k = (C.get('mods', {}).get(s['mod']) or {}).get('img')
        return k if k in have else None
    def see_data(it, main_k):   # 판이 그리는 다시 보면: 장면으로 가는 단추, 작은 그림(판 위 큰 그림과 다를 때만)
        sid = it.get('seeAt') if (it.get('seeAt') in SCN or it.get('seeAt') == 'front') else None
        sk = it.get('seeImg') or (scene_img(sid) if sid else None)
        return ({'sc': sid, 't': see_go_t(sid)} if sid else None), ({'u': have[sk]['u'], 'w': have[sk]['w'], 'h': have[sk]['h']} if sk and sk in have and sk != main_k else None)
    def see_html(q):
        if not q.get('see'): return ''
        sid = q.get('seeAt') if (q.get('seeAt') in SCN or q.get('seeAt') == 'front') else None
        k = q.get('seeImg') or (scene_img(sid) if sid else None)
        th = ''
        if k and k in have:
            hh = have[k]; th = f'<img class="see-img" src="{hh["u"]}" width="{hh["w"]}" height="{hh["h"]}" alt="" loading="lazy" decoding="async">'
        go = f'<a class="see-go" href="#{"lcard" if sid == "front" else "sc-" + e(sid)}" data-sc="{e(sid)}">{e(see_go_t(sid))}</a>' if sid else ''
        return f'<div class="see{" has-img" if th else ""}">{th}<div class="see-t"><b>다시 보면</b><p>{e(q["see"])}</p></div>{go}</div>'
    def film_secs(fr):   # 영화 장면 목록의 대략 길이(틀의 dur와 같은 셈 + 장면마다 1초)
        return sum(1.7 + 0.078 * len(ln.get('t', '')) + (1.4 if ln.get('q') else 0) + (ln.get('wait') or 0) / 1000 for f in fr for ln in (f.get('lines') or [])) + 1.0 * len(fr)
    def len_label(sec):
        return f'{max(10, round(sec / 10) * 10)}초' if sec < 90 else f'{round(sec / 60)}분'
    for n, q in enumerate(C.get('qs') or []):
        h = have[q['img']]
        flen = (' · ' + len_label(film_secs(q['film']))) if q.get('film') else ''
        mo = q.get('more') or {}
        mlen = len_label(film_secs(mo['film'])) if mo.get('film') else ''
        more_btn = (f'<button type="button" class="qmore" data-q="{n}">▶ 이어서 듣기 · {e(mo["t"])} · {mlen}</button>') if mo.get('film') else ''
        pos = f' style="object-position:{e(q["pos"])}"' if q.get('pos') else ''
        # 2026-11-19 사용자님: 답을 쪽 안에 펼치면 길어져서 싫음 → 세 칸 카드는 그대로, ‘답 보기’는 뒷이야기와 같은 판에서 열려요
        qs_html += (f'<article class="qcard" data-q="{n}"><div class="qimg"><img src="{h["u"]}" width="{h["w"]}" height="{h["h"]}" alt="{e(IM[q["img"]]["alt"])}" loading="lazy" decoding="async"{pos}></div>'
                    f'<div class="qin"><h3>{e(q["q"])}</h3><div class="qbtns"><button type="button" class="qopen" data-q="{n}" aria-haspopup="dialog">답 보기</button>'
                    + (f'<button type="button" class="qfilm" data-q="{n}">▶ 영화로 보기{flen}</button>' if q.get('film') else '') +
                    '</div></div></article>')
        sgo, simg = see_data(q, q['img'])
        qd = {'q': q['q'], 'film': [filmref(f) for f in q.get('film', [])], 'a': q['a'], 'see': q.get('see', ''), 'pos': q.get('pos', ''),
              'flen': flen.replace(' · ', '', 1), 'seeGo': sgo, 'seeImg': simg,
              'img': {'u': h['u'], 'w': h['w'], 'h': h['h'], 'alt': IM[q['img']]['alt'], 'cr': IM[q['img']].get('cr', '')}}
        if mo.get('film'): qd['more'] = {'t': mo['t'], 'next': mo.get('next', ''), 'len': mlen, 'film': [filmref(f) for f in mo['film']]}
        qs_data.append(qd)
    # 더 깊이 ‘뒷이야기’(2026-11-19 본부 · 사용자님 생각, 이름도 함께 정함): 열쇠 물음 말고 이어지는 이야기들은 흑백 카드로 남겨 둬요.
    # 누르면 색이 돌아오고(획득) 두세 문장 답 · 다시 보면 · 근거(새 탭) · 다른 카드로 가는 길이 열려요. 내용은 DATA.qx로 넘겨 틀이 판을 그려요.
    # 꾸러미(2026-11-19 사용자님과 정함): 'pack' 1·2·3… 화면에는 한 꾸러미(여섯 장 안팎)만 보이고, 다 펼치면 다음 꾸러미가 열려요.
    #   남은 이야기를 버리지 않으면서 화면은 복잡해지지 않게. pack이 없으면 모두 1(예전 카드 그대로).
    qx_html, qx_data = '', []
    QXL = sorted(C.get('qx') or [], key=lambda x: int(x.get('pack', 1)))   # 꾸러미 차례로(같은 꾸러미 안은 적은 차례 그대로)
    npk = max([int(x.get('pack', 1)) for x in QXL] or [1])
    for x in QXL:
        h = have[x['img']]
        pk = int(x.get('pack', 1))
        pos = f' style="object-position:{e(x["pos"])}"' if x.get('pos') else ''
        qx_html += (f'<button type="button" class="qxc" data-x="{e(x["id"])}" data-pk="{pk}" aria-haspopup="dialog"{" hidden" if pk > 1 else ""}>'
                    f'<span class="qx-img"><img src="{h["u"]}" width="{h["w"]}" height="{h["h"]}" alt="" loading="lazy" decoding="async"{pos}></span>'
                    f'<span class="qx-mark" aria-hidden="true">?</span><span class="qx-q">{e(x["q"])}</span>'
                    + (f'<span class="qx-hook">{e(x["hook"])}</span>' if x.get('hook') else '') + '</button>')
        go = x.get('go')
        sgo, simg = see_data(x, x['img'])
        qx_data.append({'id': x['id'], 'q': x['q'], 'a': x['a'], 'see': x.get('see', ''), 'pos': x.get('pos', ''), 'pk': pk,
                        'seeGo': sgo, 'seeImg': simg,
                        'img': {'u': h['u'], 'w': h['w'], 'h': h['h'], 'alt': IM[x['img']]['alt'], 'cr': IM[x['img']].get('cr', '')},
                        'src': [{'t': s2['t'], 'm': s2.get('m', ''), 'u': s2['u']} for s2 in x.get('src', [])],
                        'go': ({'t': go['t'], 'cid': go['cid'], 'u': f'{go["cid"]}.html'} if go else None)})
    if qx_html:
        nx = len([x for x in qx_data if x['pk'] == 1])
        more = (f'<p class="qx-more" id="qxMore">다 펼치면 다음 꾸러미가 열려요 · 꾸러미 1/{npk}</p>' if npk > 1 else '')
        qx_html = (f'<section class="qx" aria-label="뒷이야기"><div class="qx-head"><h3>뒷이야기</h3><span class="qx-n" id="qxN" aria-live="polite">0/{nx} 펼쳤어요</span>'
                   '<p>아직 펼치지 않은 이야기예요. 누르면 이야기가 펼쳐지고 색이 돌아와요. 더 알고 싶으면 근거를 따라가 보세요.</p>' + more + '</div>'
                   + ('<p class="qx-new" id="qxNew" role="status" hidden></p>' if npk > 1 else '') +
                   f'<div class="qx-grid">{qx_html}</div></section>')
    if qs_html or qx_html:   # 궁금증과 뒷이야기가 같이 쓰는 판 하나
        qs_html = ((f'<div class="qs">{qs_html}</div>' if qs_html else '') + qx_html + '<dialog class="qxs" id="qxSheet" aria-labelledby="qxsQ"><div class="qxs-in"></div></dialog>'
                   + ('<h3 class="dp-more">더 찾아보기</h3>' if deep else ''))
    G = C['goals']; gh = ''
    for g, tag in (('s4', '금박'), ('s5', '채색')):
        x = G[g]
        ways = ''.join(f'<div class="way" id="w-{w["id"]}"><span>{e(w["t"])}</span><em></em></div>' for w in x['ways'])
        gh += f'<div class="stepbox" id="box{g[1]}"><h3>{e(x["t"])} <span class="tag">{tag}</span></h3><p>{e(x["p"])}</p><div class="ways">{ways}</div></div>'
    stages = STAGE_BASE + [{'n': 4, 't': '금박', 'done': G['s4']['done'], 'how': G['s4']['how']}, {'n': 5, 't': '채색', 'done': G['s5']['done'], 'how': G['s5']['how']}]
    src = '<ol class="srcl">' + ''.join(f'<li><a href="{e(s["u"])}" target="_blank" rel="noopener">{e(s["l"])}</a></li>' for s in C['src']) + '</ol>'
    cred = [f'<li>{credit(k)}</li>' for k in [k for k in IM if k in have and k != 'card'] + ['card']]
    for s in C.get('sounds', []):
        if not s.get('cr'): continue
        cred.append(f'<li><a href="{e(s["u"])}" target="_blank" rel="noopener">{e(s["cr"])}</a></li>' if s.get('u') else f'<li>{e(s["cr"])}</li>')
    for s in C.get('extra_credits', []):
        cred.append(f'<li><a href="{e(s["u"])}" target="_blank" rel="noopener">{e(s["cr"])}</a></li>')
    credits = '<ul class="cred">' + ''.join(cred) + '</ul>'
    lines = ''.join(f'<button type="button" class="line a" data-l="{e(l)}">{e(l)}</button>' for l in C['lines']) + ''.join(f'<button type="button" class="line k" data-l="{e(l)}">{e(l)}</button>' for l in C['linesKid'])
    front = [{'t': sc['t'], 'kid': sc.get('kid') or sc['t'], 'f': sc.get('f')} for sc in CC['scenes'] if not sc.get('dark')]
    card_u = have['card']
    film = []
    for sh in C['film']:
        sh = dict(sh)
        for key in ('img', 'then', 'now'):
            if sh.get(key):
                k = sh[key]; sh[key] = {'u': have[k]['u'], 'w': have[k]['w'], 'h': have[k]['h'], 'alt': IM[k]['alt']}
                if have[k].get('bw'): sh[key].update(bw=have[k]['bw'], bh=have[k]['bh'])   # 영화가 큰 그림 크기로 선명함을 따져요(2026-11-19)
        film.append(sh)
    # 마무리(키트 3판 보탬 · 기준서 보탬 11): 나의 자리 물음, 다시 보기, 영화 끝 여운·물음
    CL = C.get('close') or {}
    ask_a = CL.get('ask') or CC['ask']
    ask_k = CL.get('askKid') or CC.get('askKid', CC['ask'])
    again_html = (f'<p class="again-t">{e(CL["again"])}</p>' + fig('card', 'ph again')) if CL.get('again') else ''
    if CL and CL.get('film', True):
        ri = next((j for j, f in enumerate(film) if f.get('type') == 'reward'), len(film))
        last = film[ri - 1] if ri > 0 else None
        ch = (last or {}).get('ch', len(C['scenes']))
        add_a, add_k = [], []
        if CL.get('hold'):
            ms = int(float(CL['hold']) * 1000); add_a.append({'t': '', 'wait': ms}); add_k.append({'t': '', 'wait': ms})
        if CL.get('ask'):
            add_a.append({'t': CL['ask'], 'ask': '생각해 보기', 'go': '생각해 본 뒤 이어 보기'})
            add_k.append({'t': CL.get('askKid') or CL['ask'], 'ask': True})
        if CL.get('again'):
            film.insert(ri, {'type': 'img', 'img': {'u': card_u['u'], 'w': card_u['w'], 'h': card_u['h'], 'alt': IM['card']['alt']}, 'ch': ch,
                             'lines': [{'t': CL['again']}] + add_a, 'kid': [{'t': CL['again']}] + add_k})
        elif add_a:
            if last and last.get('type') not in ('reward', 'chapter', 'candle') and not last.get('sync'):
                last['lines'] = list(last.get('lines') or []) + add_a
                last['kid'] = list(last.get('kid') or []) + add_k
            else:
                film.insert(ri, {'type': 'black', 'ch': ch, 'lines': add_a, 'kid': add_k})
    mods = json.loads(json.dumps(C.get('mods', {})))
    imgref = lambda k: {'u': have[k]['u'], 'w': have[k]['w'], 'h': have[k]['h'], 'alt': IM[k]['alt'], 'cr': IM[k].get('cr', ''), 'cap': IM[k].get('cap', '')}
    for m in mods.values():                                   # 소리 파일 주소를 카드 폴더 기준으로, 그림 키는 주소로
        for p in m.get('parts', []): p['u'] = f'{cid}/' + p['u'].split('/')[-1]
        if isinstance(m.get('img'), str) and m['img'] in have: m['img'] = imgref(m['img'])
        for pr in m.get('pairs', []) or []:
            for kk in ('then', 'now'):
                if isinstance(pr.get(kk), str) and pr[kk] in have: pr[kk] = imgref(pr[kk])
        for lk in ('stops', 'steps', 'doors', 'pieces'):          # 키트 3판 새 방식: 목록 안의 그림 키도 주소로
            for it in m.get(lk, []) or []:
                if isinstance(it, dict) and isinstance(it.get('img'), str) and it['img'] in have: it['img'] = imgref(it['img'])
    data = {'id': cid, 'tplv': TPLV, 'stages': stages, 'front': front, 'card': have['card']['u'], 'film': film,
            'lines': C['lines'], 'linesKid': C['linesKid'], 'scenes': [s['id'] for s in C['scenes']], 'labels': {s['id']: s['label'] for s in C['scenes']},
            'stamp': C['stamp'], 'sound': None, 'goals': {g: {'ways': [{k2: w[k2] for k2 in ('id', 'hint', 'okt') if k2 in w} for w in G[g]['ways']]} for g in ('s4', 's5')},
            'mods': mods, 'nch': len(C['scenes']), 'doneNote': C.get('doneNote', ''), 'filmSound': bool(C.get('filmSound')),
            'big': {h['u']: h['b'] for h in have.values() if h.get('b')}, 'bigsrc': {k: v for k, v in bigsrc.items() if have.get(k, {}).get('b')}}
    if qs_data: data['qs'] = qs_data
    if qx_data: data['qx'] = qx_data
    card = have['card']
    rep = {
        '{{PAGETITLE}}': e(C['pagetitle']), '{{BRANDSUB}}': e(C['brandsub']), '{{SEAL}}': e(C['stamp']['t'][0]),
        '{{TITLE}}': e(CC['t']), '{{SETNAME}}': e(f"{SS['t']} · {CC['no']}"), '{{Q}}': e(CC['q']), '{{KQ}}': e(CC.get('kq', CC['q'])), '{{LINE}}': e(CC['line']),
        '{{TITLEREST}}': e(CC['t'][1:]), '{{TITLE1}}': e(CC['t'][0]),
        '{{CARDIMG}}': card['u'], '{{CARDW}}': str(card['w']), '{{CARDH}}': str(card['h']), '{{CARDALT}}': e(IM['card']['alt']),
        '{{WHERE}}': C['where'], '{{LEAD}}': C['lead'], '{{LEADKID}}': C['leadKid'], '{{META}}': e(C['meta']), '{{DRAFT}}': C['draft'],
        '{{SCENES}}': '\n'.join(sc_html), '{{IMAGINE}}': e(C['imagine']['t']), '{{IMAGINEKID}}': e(C['imagine']['kid']), '{{IMSND}}': C.get('imsnd', ''),
        '{{DEEP}}': qs_html + '\n'.join(deep), '{{GOALS}}': gh, '{{LINES}}': lines,
        '{{ASK}}': e(ask_a), '{{ASKKID}}': e(ask_k), '{{AGAIN}}': again_html,
        '{{SRC}}': src, '{{NSRC}}': str(len(C['src'])), '{{CREDITS}}': credits, '{{FOOT}}': C['foot'],
        '{{SNDTAG}}': '', '{{FILMLEN}}': e(C['filmlen']), '{{SNDNOTE}}': e(C.get('sndnote', '')),
    }
    out = tpl()
    for a, b in rep.items():
        assert a in out, a
        out = out.replace(a, b)
    if qs_html:   # 궁금증이 있으면 더 깊이 안내 글도 그에 맞게
        out = out.replace('<p class="sub">궁금한 칸만 펼쳐 읽어도 괜찮아요.</p>', '<p class="sub">이야기를 보다 궁금해질 만한 것들이에요. 답을 읽거나 짧은 영화로 보세요.</p>')
    # 카드마다 같은 스타일·스크립트는 공유 파일로(틀을 고치면 모든 카드에 바로 반영, 카드마다 130KB 아낌)
    s0, s1 = out.index('<style>'), out.index('</style>') + len('</style>')
    out = (out[:s0] + f'<link rel="stylesheet" href="{SHARED}/deep3.css">\n<style>:root{{--card-ar:{card["w"]}/{card["h"]}}}\n' + C.get('theme', '') + '\n</style>' + out[s1:])
    c0, c1 = out.index('<script>'), out.index('</script>') + len('</script>')
    out = out[:c0] + '<script>\n' + JS_HEAD + f'</script>\n<script src="{SHARED}/deep3.js"></script>' + out[c1:]
    old_brand = '<span class="brand"><span class="long"><b>처음 만나는 기독교 문화</b> · </span>' + e(C['brandsub']) + '</span>'
    assert old_brand in out
    out = out.replace('href="#sc-road"', f'href="#sc-{C["scenes"][0]["id"]}"')   # ‘천천히 읽기 ↓’는 이 카드의 첫 장면으로
    site_brand = f'<a class="brand" href="../#c-{cid}" style="text-decoration:none">← <span class="long"><b>처음 만나는 기독교 문화</b> · </span>카드 책으로</a>'
    prev_brand = '<a class="brand" href="./" style="text-decoration:none">← <span class="long"><b>깊은 카드 시안</b> · </span>묶음 모아 보기</a>'
    body = out.replace('/*__DATA__*/null', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
    assert '{{' not in body, body[body.find('{{'):body.find('{{') + 60]
    def doc(b, icon):
        return ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
                f'<meta name="robots" content="noindex,nofollow">\n{icon}</head>\n<body>\n' + b + '\n</body>\n</html>\n')
    site_html = doc(body.replace(old_brand, site_brand), '<link rel="icon" href="../icon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="../apple-touch-icon.png">\n')
    open(os.path.join(site_dir, cid + '.html'), 'w', encoding='utf-8').write(site_html)
    shared = write_shared(site_dir)
    size = sum(os.path.getsize(os.path.join(od, f)) for f in os.listdir(od))
    print(f'{cid}: site/deep/{cid}.html {len(site_html)//1024}KB · 자산 {len(os.listdir(od))}개 {size//1024}KB')
    if preview:
        pd = os.path.join(preview, cid); os.makedirs(pd, exist_ok=True)
        pbig = {}
        for f in sorted(os.listdir(od)):
            fp = os.path.join(od, f)
            if '.big.' in f:                           # 큰 그림은 미리 보기 한도 안에서만(나머지는 보통 그림으로 보여요)
                if PREVIEW_USED[0] + os.path.getsize(fp) > PREVIEW_BIG_BUDGET: continue
                PREVIEW_USED[0] += os.path.getsize(fp); pbig[f'{cid}/{f}'] = 1
            shutil.copy(fp, os.path.join(pd, f))
        pdata = dict(data, big={u: b for u, b in data['big'].items() if b in pbig})
        if pdata.get('qx'):   # 미리 보기에는 다른 카드가 없어서, 뒷이야기의 ‘다른 카드로’ 길은 사이트의 그 카드로
            pdata['qx'] = [dict(x, go=dict(x['go'], u=LIVE_DEEP + x['go']['u'])) if x.get('go') else x for x in pdata['qx']]
        if len(pdata['big']) < len(data['big']): print(f'  · 미리 보기에는 큰 그림 {len(pdata["big"])}/{len(data["big"])}장만 넣었어요(올리기 한도). 사이트에는 모두 들어가요.')
        pbody = out.replace('/*__DATA__*/null', json.dumps(pdata, ensure_ascii=False).replace('</', '<\\/'))
        pbody = pbody.replace(old_brand, prev_brand).replace(f'"{SHARED}/', f'"{PSHARED}/')
        if C.get('qcand'):   # 검토용 · 더 깊이 예상 질문(2026-11-19): 미리 보기에만. 사용자님이 카드와 맞춰 보고 번호로 골라요
            items = ''.join(f'<li{" class=\"pk\"" if x.get("pick") else (" class=\"xk\"" if x.get("x") else "")}><b>{e(x["q"])}</b><span>{e(x.get("at", ""))}{" · " if x.get("at") and x.get("a") else ""}{e(x.get("a", ""))}</span>{('<span class="see">다시 보면 · ' + e(x["see"]) + '</span>') if x.get("see") else ""}</li>' for x in C['qcand'])
            rv = ('<section class="col rvw" aria-label="검토용 예상 질문"><style>.rvw{margin:10px auto 0;border:2px dashed var(--accent);border-radius:16px;padding:18px 18px 8px;background:var(--soft)}'
                  '.rvw h2{font:700 20px/1.35 var(--serif);margin:0 0 4px}.rvw .sub{color:var(--muted);font-size:14px;margin:0 0 12px}.rvw ol{margin:0;padding-left:26px}.rvw li{margin:0 0 12px}'
                  '.rvw li b{display:block;font:700 16.5px/1.5 var(--serif)}.rvw li span{display:block;color:var(--muted);font-size:14px;line-height:1.6}'
                  '.rvw li span.see{color:var(--ink);margin-top:2px}.rvw li.pk b::after{content:"  ✓ 열쇠 물음(궁금증)에 들어감";color:var(--accent);font:600 12.5px var(--sans)}.rvw li.xk b::after{content:"  ✓ 뒷이야기에 들어감";color:var(--accent);font:600 12.5px var(--sans)}</style>'
                  f'<h2>검토용 · 더 깊이 예상 질문 {len(C["qcand"])}개</h2><p class="sub">미리 보기에만 보이는 칸이에요. ‘다시 보면’은 답을 알고 나서 본 이야기의 그림이 어떻게 달라 보이는지예요. 마음에 드는 번호를 골라 알려 주세요.</p><ol>{items}</ol></section>\n')
            pbody = pbody.replace('  <section class="srcbox col">', rv + '  <section class="srcbox col">', 1)
        open(os.path.join(preview, cid + '.html'), 'w', encoding='utf-8').write(doc(pbody, ''))
        pdsh = os.path.join(preview, PSHARED); os.makedirs(pdsh, exist_ok=True)
        for f in os.listdir(shared): shutil.copy(os.path.join(shared, f), os.path.join(pdsh, f))
    return {'id': cid, 't': CC['t'], 'tag': CC.get('tag', ''), 'mode': C.get('mode', ''), 'card': have['card']['u'], 'w': card['w'], 'h': card['h'], 'alt': IM['card']['alt'], 'lead': re.sub('<[^>]+>', '', C['lead']), 'nq': len(C.get('qcand') or [])}

def preview_index(preview, built, title='깊은 카드 시안'):
    cards = ''.join(f'''<article class="card"><img src="{b['card']}" alt="{e(b['alt'])}" width="{b['w']}" height="{b['h']}"><div class="in"><p class="mode">{e(b['mode'])}</p><h2>{e(b['t'])}</h2><p class="d">{e(b['lead'])}</p>{('<p class="nq">검토용 예상 질문 ' + str(b['nq']) + '개 · 카드 맨 아래에</p>') if b.get('nq') else ''}<a class="open" href="{b['id']}.html">시안 열기</a></div></article>''' for b in built)
    page = f'''<title>{e(title)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
:root{{--bg:#f3eee4;--paper:#fbf8f1;--ink:#2b251d;--muted:#685e4f;--line:#e2d8c6;--accent:#8f5418;--accent-ink:#fffaf2;color-scheme:light}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#14110d;--paper:#1c1813;--ink:#ede5d6;--muted:#afa18b;--line:#342a20;--accent:#e3a75e;--accent-ink:#1d1307;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#14110d;--paper:#1c1813;--ink:#ede5d6;--muted:#afa18b;--line:#342a20;--accent:#e3a75e;--accent-ink:#1d1307;color-scheme:dark}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.7 "Apple SD Gothic Neo","Noto Sans KR","Malgun Gothic",sans-serif;word-break:keep-all;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.wrap{{max-width:1040px;margin:0 auto;padding-block:30px 40px}}h1{{font:700 clamp(26px,6vw,38px)/1.25 serif;margin:0 0 18px}}
.cards{{display:grid;gap:16px}}@media (min-width:760px){{.cards{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
.card{{background:var(--paper);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;min-width:0}}
.card img{{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;display:block}}.in{{padding:14px;display:flex;flex-direction:column;gap:6px;flex:1}}
.mode{{margin:0;font-size:12.5px;color:var(--accent);font-weight:600}}h2{{margin:0;font:700 19px/1.35 serif}}.d{{margin:0;font-size:15px;color:var(--muted)}}
.nq{{margin:0;font-size:13.5px;color:var(--accent);font-weight:600}}
.open{{margin-top:auto;align-self:flex-start;background:var(--accent);color:var(--accent-ink);text-decoration:none;border-radius:999px;padding:8px 16px;font-weight:600}}
</style>
<main class="wrap"><h1>{e(title)}</h1><section class="cards">{cards}</section></main>'''
    open(os.path.join(preview, 'index_preview.html'), 'w', encoding='utf-8').write(page)

if __name__ == '__main__':
    args = sys.argv[1:]
    preview = None
    if '--preview' in args:
        i = args.index('--preview'); preview = os.path.abspath(args[i + 1]); del args[i:i + 2]; os.makedirs(preview, exist_ok=True)
    if '--all' in args:
        args = sorted(glob.glob(os.path.join(REPO, 'tools', 'deep', 'cards', '*.py')))
    built = [build(load(p), REPO, preview) for p in args]
    if preview and built:
        preview_index(preview, built)
        fm = {f'{PSHARED}/{f}': os.path.join(preview, PSHARED, f) for f in sorted(os.listdir(os.path.join(preview, PSHARED)))}
        for b in built:
            fm[b['id'] + '.html'] = os.path.join(preview, b['id'] + '.html')
            for f in sorted(os.listdir(os.path.join(preview, b['id']))): fm[f"{b['id']}/{f}"] = os.path.join(preview, b['id'], f)
        json.dump(fm, open(os.path.join(preview, 'preview_files.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print('미리보기:', preview)
        print('아티팩트로 올리기: file_path =', os.path.join(preview, 'index_preview.html'), '· files =', os.path.join(preview, 'preview_files.json'), f'의 내용({len(fm)}개)')
