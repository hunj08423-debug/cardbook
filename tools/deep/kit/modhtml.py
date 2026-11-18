# -*- coding: utf-8 -*-
"""자료만 적으면 되는 공통 방식의 HTML(키트 2판). build.py가 불러 써요. 제작 창은 고치지 않아요.
방식마다 함수 하나: look(찾아보기) · reveal(비추기) · slider(그때와 지금) · route(지도 위 길) · choose(고르기).
움직임은 틀(deep3_tpl.html)의 MODS.<이름>이 맡아요."""
import html

e = lambda s: html.escape(str(s), quote=True)

def _credit(IM, k):
    im = IM[k]; cr = e(im.get('cr', ''))
    return f'<a href="{e(im["u"])}" target="_blank" rel="noopener">{cr}</a>' if im.get('u') else cr

def _cap(IM, k, lead=''):
    im = IM[k]
    return (lead + (e(im['cap']) + ' · ' if im.get('cap') else '') + _credit(IM, k))

def _box(w, h, vh=72):
    r = w / h
    return f'aspect-ratio:{w}/{h};width:min(100%,calc({vh}vh * {r:.4f}))'

def _top(intro, ncls):
    return f'<div class="mod-top"><p class="mod-intro">{e(intro)}</p><span class="mod-n {ncls}" aria-live="polite"></span></div>'

def look(cfg, have, IM):
    k = cfg['img']; h = have[k]
    spots = ''.join(f'<button type="button" class="lk-spot" data-i="{i}" style="left:{s["x"]}%;top:{s["y"]}%" aria-label="{i + 1}번 찾아보기">{i + 1}</button>'
                    for i, s in enumerate(cfg['spots']))
    lis = ''.join(f'<li><button type="button" data-i="{i}">{i + 1}. ?</button></li>' for i in range(len(cfg['spots'])))
    return (f'<div class="mod lk" data-mod="look">{_top(cfg.get("intro", "그림 속 작은 것들을 하나씩 눌러 보세요."), "lk-n")}'
            f'<div class="lk-frame" style="{_box(h["w"], h["h"])}"><div class="lk-zoom"><img src="{h["u"]}" width="{h["w"]}" height="{h["h"]}" alt="{e(IM[k]["alt"])}" decoding="async">{spots}</div></div>'
            f'<p class="mod-cap">{_cap(IM, k)}</p>'
            f'<div class="lk-bar"><button type="button" class="mod-btn lk-zoombtn" aria-pressed="false" disabled>가까이 보기</button></div>'
            f'<ol class="lk-list" aria-label="찾을 곳">{lis}</ol>'
            f'<div class="mod-info lk-info" aria-live="polite"><p>그림 위의 숫자나 아래 번호를 눌러 보세요.</p></div>'
            f'<p class="mod-done lk-done" hidden>{e(cfg.get("done", ""))}</p></div>')

def reveal(cfg, have, IM):
    k = cfg['img']; h = have[k]; marks = cfg.get('marks') or []
    tags = ''.join(f'<button type="button" class="rv-tag" data-i="{i}" style="left:{m["x"]}%;top:{m["y"]}%">{e(m["t"])}</button>' for i, m in enumerate(marks))
    hint = '빛이 닿으면 숨은 표시가 나타나요.' if marks else '그림을 끝까지 비춰 보세요.'
    return (f'<div class="mod rv" data-mod="reveal">{_top(cfg.get("intro", "손가락이나 마우스로 문질러 비춰 보세요."), "rv-n")}'
            f'<div class="rv-box" style="{_box(h["w"], h["h"], 66)}" role="img" aria-label="{e(IM[k]["alt"])}">'
            f'<img class="rv-base" src="{h["u"]}" alt="" decoding="async"><canvas class="rv-lit"></canvas>{tags}<span class="rv-glow"></span></div>'
            f'<p class="mod-cap">{_cap(IM, k)}</p>'
            f'<div class="rv-bar"><button type="button" class="mod-btn rv-all">모두 밝히기</button></div>'
            f'<div class="mod-info rv-info" aria-live="polite"><p>{hint}</p></div>'
            f'<p class="mod-done rv-after" hidden>{e(cfg.get("after", ""))}</p></div>')

def slider(cfg, have, IM):
    pairs = cfg['pairs']; out = []
    tabs = ''
    if len(pairs) > 1:
        tabs = '<div class="sl-tabs" role="group" aria-label="그때와 지금 고르기">' + ''.join(
            f'<button type="button" class="sl-tab" data-i="{i}" aria-pressed="{str(i == 0).lower()}">{e(p.get("thenT", ""))} → {e(p.get("nowT", ""))}</button>' for i, p in enumerate(pairs)) + '</div>'
    for i, p in enumerate(pairs):
        t, n = have[p['then']], have[p['now']]
        out.append(f'<div class="sl-pair" data-i="{i}"{" hidden" if i else ""}>'
                   f'<div class="sl-box" style="{_box(n["w"], n["h"])}">'
                   f'<img class="sl-now" src="{n["u"]}" alt="{e(IM[p["now"]]["alt"])}" decoding="async">'
                   f'<div class="sl-then"><img src="{t["u"]}" alt="{e(IM[p["then"]]["alt"])}" decoding="async"></div><div class="sl-handle"></div>'
                   f'<span class="sl-lab l">{e(p.get("thenT", "그때"))}</span><span class="sl-lab r">{e(p.get("nowT", "지금"))}</span>'
                   f'<input type="range" class="sl-range" min="0" max="100" value="50" aria-label="{e(p.get("thenT", "그때"))}와 {e(p.get("nowT", "지금"))} 사이를 밀기"><span class="sl-focus"></span></div>'
                   f'<p class="mod-cap">왼쪽 · {_cap(IM, p["then"])}<br>오른쪽 · {_cap(IM, p["now"])}</p>'
                   + (f'<div class="mod-info"><p>{p["p"]}</p></div>' if p.get('p') else '') + '</div>')
    return f'<div class="mod sl" data-mod="slider">{_top(cfg.get("intro", "가운데 손잡이를 밀어 그때와 지금을 겹쳐 보세요."), "sl-n")}{tabs}{"".join(out)}</div>'

def route(cfg, have, IM):
    k = cfg.get('img') or 'paper'; stops = cfg['stops']
    if k != 'paper' and k in have: W, H = have[k]['w'], have[k]['h']; bg = f'<img src="{have[k]["u"]}" alt="{e(IM[k]["alt"])}" decoding="async">'
    else: W, H = 1200, 900; bg = '<div class="rt-paper" aria-hidden="true"></div>'; k = 'paper'
    X = lambda s: s['x'] * W / 100; Y = lambda s: s['y'] * H / 100
    sw = max(W, H) / 220
    ghost = 'M' + ' L'.join(f'{X(s):.1f} {Y(s):.1f}' for s in stops)
    segs = ''.join(f'<path class="rt-seg" data-i="{i}" pathLength="100" stroke-width="{sw:.1f}" d="M{X(a):.1f} {Y(a):.1f} L{X(b):.1f} {Y(b):.1f}"/>' for i, (a, b) in enumerate(zip(stops, stops[1:])))
    dots = ''.join(f'<button type="button" class="rt-dot" data-i="{i}" style="left:{s["x"]}%;top:{s["y"]}%" aria-label="{i + 1}. {e(s["t"])}">{i + 1}</button>'
                   f'<span class="rt-name" style="left:{s["x"]}%;top:{s["y"]}%">{e(s["t"])}</span>' for i, s in enumerate(stops))
    cap = f'<p class="mod-cap">{_cap(IM, k)}</p>' if k != 'paper' else '<p class="mod-cap">지도는 이 안내서가 그린 길잡이 그림이에요(실제 거리와 다를 수 있어요).</p>'
    return (f'<div class="mod rt" data-mod="route">{_top(cfg.get("intro", "‘다음 곳으로’를 눌러 길을 따라가 보세요."), "rt-n")}'
            f'<div class="rt-box" data-w="{W}" data-h="{H}" style="{_box(W, H)}">{bg}'
            f'<svg class="rt-svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid meet" aria-hidden="true"><path class="rt-ghost" stroke-width="{sw * .6:.1f}" d="{ghost}"/>{segs}</svg>{dots}</div>'
            f'{cap}<div class="mod-info rt-info" aria-live="polite"></div>'
            f'<div class="rt-ctl"><button type="button" class="mod-btn main rt-next">다음 곳으로</button><button type="button" class="mod-btn rt-again" hidden>처음부터 다시</button></div>'
            f'<p class="mod-done rt-end" hidden>{e(cfg.get("end", ""))}</p></div>')

def choose(cfg, have, IM):
    opts = ''.join(f'<button type="button" data-t="{e(o["t"])}" aria-pressed="false">{e(o["t"])}</button>' for o in cfg['opts'])
    return (f'<div class="mod ch2" data-mod="choose"><p class="ch2-q">{e(cfg["q"])}</p>'
            f'<div class="ch2-opts" role="group" aria-label="{e(cfg["q"])}">{opts}</div><p class="ch2-r" aria-live="polite"></p></div>')
