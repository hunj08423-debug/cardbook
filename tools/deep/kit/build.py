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
import json, os, sys, html, shutil, importlib.util, glob, re
from PIL import Image

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))
# 받은 원본 그림·소리를 두는 곳: 저장소 밖(커밋되지 않게). 기본은 cardbook 옆의 deep_src 폴더.
SRCROOT = os.environ.get('DEEP_SRC') or os.path.abspath(os.path.join(REPO, '..', 'deep_src'))
e = lambda s: html.escape(str(s), quote=True)
TPLV = 'deep3-3'          # 틀 판(틀을 바꾸면 본부가 올려요) · 3: 놓아 보기·그때와 지금 문구 칸, 품질 85
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
    spec = importlib.util.spec_from_file_location('card_' + os.path.basename(path)[:-3].replace('-', '_'), path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CARD

def tpl():
    return open(os.path.join(KIT, 'deep3_tpl.html'), encoding='utf-8').read()

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
    for k, im in IM.items():
        out = os.path.join(od, k + ext)
        src = im.get('src')
        if src and not os.path.isabs(src): src = os.path.join(SRCROOT, src)
        if src and os.path.exists(src):
            I = Image.open(src); I.load()
            if I.mode not in ('RGB', 'L'): I = I.convert('RGB')
            if im.get('crop'):
                l, t, r, b = im['crop']; w, h = I.size
                I = I.crop((round(l * w), round(t * h), round(r * w), round(b * h)))
            mx = im.get('max', 1920 if fmt == 'webp' else 1280)
            if max(I.size) > mx:
                sc = mx / max(I.size); I = I.resize((round(I.width * sc), round(I.height * sc)), Image.LANCZOS)
            if I.mode == 'L': I = I.convert('RGB')
            if fmt == 'webp':                          # 품질 85(기준서 1판 보탬 7). 한 장 1MB(크게 볼 그림 1.5MB)를 넘을 때만 조금씩 낮춰요
                cap = (1536 if mx > 1920 else 1024) * 1024
                for q in ([im['q']] if im.get('q') else [85, 80, 76, 72]):
                    I.save(out, 'WEBP', quality=q, method=5)
                    if os.path.getsize(out) <= cap: break
            else: I.save(out, 'JPEG', quality=im.get('q', 80), optimize=True, progressive=True)
        elif not os.path.exists(out):
            raise SystemExit(f'그림이 없어요: {k} (src={src}) — commons_get.py로 받거나 경로를 고쳐 주세요')
        I = Image.open(out)
        have[k] = {'u': f'{cid}/{k}{ext}', 'w': I.width, 'h': I.height}
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
    film = []
    for sh in C['film']:
        sh = dict(sh)
        for key in ('img', 'then', 'now'):
            if sh.get(key):
                k = sh[key]; sh[key] = {'u': have[k]['u'], 'w': have[k]['w'], 'h': have[k]['h'], 'alt': IM[k]['alt']}
        film.append(sh)
    mods = json.loads(json.dumps(C.get('mods', {})))
    imgref = lambda k: {'u': have[k]['u'], 'w': have[k]['w'], 'h': have[k]['h'], 'alt': IM[k]['alt'], 'cr': IM[k].get('cr', ''), 'cap': IM[k].get('cap', '')}
    for m in mods.values():                                   # 소리 파일 주소를 카드 폴더 기준으로, 그림 키는 주소로
        for p in m.get('parts', []): p['u'] = f'{cid}/' + p['u'].split('/')[-1]
        if isinstance(m.get('img'), str) and m['img'] in have: m['img'] = imgref(m['img'])
        for pr in m.get('pairs', []) or []:
            for kk in ('then', 'now'):
                if isinstance(pr.get(kk), str) and pr[kk] in have: pr[kk] = imgref(pr[kk])
    data = {'id': cid, 'tplv': TPLV, 'stages': stages, 'front': front, 'card': have['card']['u'], 'film': film,
            'lines': C['lines'], 'linesKid': C['linesKid'], 'scenes': [s['id'] for s in C['scenes']], 'labels': {s['id']: s['label'] for s in C['scenes']},
            'stamp': C['stamp'], 'sound': None, 'goals': {g: {'ways': [{k2: w[k2] for k2 in ('id', 'hint', 'okt') if k2 in w} for w in G[g]['ways']]} for g in ('s4', 's5')},
            'mods': mods, 'nch': len(C['scenes']), 'doneNote': C.get('doneNote', ''), 'filmSound': bool(C.get('filmSound'))}
    card = have['card']
    rep = {
        '{{PAGETITLE}}': e(C['pagetitle']), '{{BRANDSUB}}': e(C['brandsub']), '{{SEAL}}': e(C['stamp']['t'][0]),
        '{{TITLE}}': e(CC['t']), '{{SETNAME}}': e(f"{SS['t']} · {CC['no']}"), '{{Q}}': e(CC['q']), '{{KQ}}': e(CC.get('kq', CC['q'])), '{{LINE}}': e(CC['line']),
        '{{TITLEREST}}': e(CC['t'][1:]), '{{TITLE1}}': e(CC['t'][0]),
        '{{CARDIMG}}': card['u'], '{{CARDW}}': str(card['w']), '{{CARDH}}': str(card['h']), '{{CARDALT}}': e(IM['card']['alt']),
        '{{WHERE}}': C['where'], '{{LEAD}}': C['lead'], '{{LEADKID}}': C['leadKid'], '{{META}}': e(C['meta']), '{{DRAFT}}': C['draft'],
        '{{SCENES}}': '\n'.join(sc_html), '{{IMAGINE}}': e(C['imagine']['t']), '{{IMAGINEKID}}': e(C['imagine']['kid']), '{{IMSND}}': C.get('imsnd', ''),
        '{{DEEP}}': '\n'.join(deep), '{{GOALS}}': gh, '{{LINES}}': lines,
        '{{ASK}}': e(CC['ask']), '{{ASKKID}}': e(CC.get('askKid', CC['ask'])),
        '{{SRC}}': src, '{{NSRC}}': str(len(C['src'])), '{{CREDITS}}': credits, '{{FOOT}}': C['foot'],
        '{{SNDTAG}}': '', '{{FILMLEN}}': e(C['filmlen']), '{{SNDNOTE}}': e(C.get('sndnote', '')),
    }
    out = tpl()
    for a, b in rep.items():
        assert a in out, a
        out = out.replace(a, b)
    # 카드마다 같은 스타일·스크립트는 공유 파일로(틀을 고치면 모든 카드에 바로 반영, 카드마다 130KB 아낌)
    s0, s1 = out.index('<style>'), out.index('</style>') + len('</style>')
    out = (out[:s0] + f'<link rel="stylesheet" href="{SHARED}/deep3.css">\n<style>:root{{--card-ar:{card["w"]}/{card["h"]}}}\n' + C.get('theme', '') + '\n</style>' + out[s1:])
    c0, c1 = out.index('<script>'), out.index('</script>') + len('</script>')
    out = out[:c0] + '<script>\n' + JS_HEAD + f'</script>\n<script src="{SHARED}/deep3.js"></script>' + out[c1:]
    old_brand = '<span class="brand"><span class="long"><b>처음 만나는 기독교 문화</b> · </span>' + e(C['brandsub']) + '</span>'
    assert old_brand in out
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
        for f in os.listdir(od): shutil.copy(os.path.join(od, f), os.path.join(pd, f))
        open(os.path.join(preview, cid + '.html'), 'w', encoding='utf-8').write(doc(body.replace(old_brand, prev_brand), ''))
        pdsh = os.path.join(preview, SHARED); os.makedirs(pdsh, exist_ok=True)
        for f in os.listdir(shared): shutil.copy(os.path.join(shared, f), os.path.join(pdsh, f))
    return {'id': cid, 't': CC['t'], 'tag': CC.get('tag', ''), 'mode': C.get('mode', ''), 'card': have['card']['u'], 'w': card['w'], 'h': card['h'], 'alt': IM['card']['alt'], 'lead': re.sub('<[^>]+>', '', C['lead'])}

def preview_index(preview, built, title='깊은 카드 시안'):
    cards = ''.join(f'''<article class="card"><img src="{b['card']}" alt="{e(b['alt'])}" width="{b['w']}" height="{b['h']}"><div class="in"><p class="mode">{e(b['mode'])}</p><h2>{e(b['t'])}</h2><p class="d">{e(b['lead'])}</p><a class="open" href="{b['id']}.html">시안 열기</a></div></article>''' for b in built)
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
        fm = {f'{SHARED}/{f}': os.path.join(preview, SHARED, f) for f in sorted(os.listdir(os.path.join(preview, SHARED)))}
        for b in built:
            fm[b['id'] + '.html'] = os.path.join(preview, b['id'] + '.html')
            for f in sorted(os.listdir(os.path.join(preview, b['id']))): fm[f"{b['id']}/{f}"] = os.path.join(preview, b['id'], f)
        json.dump(fm, open(os.path.join(preview, 'preview_files.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print('미리보기:', preview)
        print('아티팩트로 올리기: file_path =', os.path.join(preview, 'index_preview.html'), '· files =', os.path.join(preview, 'preview_files.json'), f'의 내용({len(fm)}개)')
