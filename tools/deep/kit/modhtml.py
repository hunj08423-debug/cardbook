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

# ---------- 새 방식(키트 3판 후보 · 견본): 펼쳐 읽기 · 시간 따라 보기 · 만드는 차례 · 날짜 따라 여는 달력 · 흩어진 조각 모으기 · 따라 쓰기 ----------
def unroll(cfg, have, IM):
    k = cfg['img']; h = have[k]
    bands = ''.join(f'<span class="ur-band" data-i="{i}" style="top:{l["y0"]}%;height:{l["y1"] - l["y0"]:.2f}%;left:{l.get("x0", 0)}%;width:{l.get("x1", 100) - l.get("x0", 0)}%"></span>' for i, l in enumerate(cfg['lines']))
    return (f'<div class="mod ur" data-mod="unroll">{_top(cfg.get("intro", "종이 아래쪽 굴대를 끌거나 ‘한 줄 더 펼치기’를 눌러, 위에서부터 한 줄씩 읽어 보세요."), "ur-n")}'
            f'<div class="ur-box" style="{_box(h["w"], h["h"], 80)}" tabindex="0" role="group" aria-label="{e(IM[k]["alt"])} — 아래 화살표 키로 펼쳐요">'
            f'<img src="{h["u"]}" alt="" decoding="async">{bands}<div class="ur-cover"><span class="ur-roll" role="presentation"></span><span class="ur-tip" aria-hidden="true">↓ 굴대를 끌어 내려 펼쳐요</span></div></div>'
            f'<p class="mod-cap">{_cap(IM, k)}</p>'
            f'<div class="ur-ctl"><button type="button" class="mod-btn main ur-more">한 줄 더 펼치기</button><button type="button" class="mod-btn ur-allbtn">끝까지 펼치기</button></div>'
            f'<div class="mod-info ur-info" aria-live="polite"><p>{e(cfg.get("hint", "펼친 만큼 줄이 읽혀요. 읽은 줄은 아래에 차례로 모여요."))}</p></div>'
            f'<ol class="ur-list" aria-label="읽은 줄"></ol>'
            f'<p class="mod-done ur-done" hidden>{e(cfg.get("done", ""))}</p></div>')

def timeline(cfg, have, IM):
    stops = cfg['stops']; h0 = have[stops[0]['img']]
    r = max(4 / 3, min(16 / 9, h0['w'] / h0['h']))
    imgs = ''.join(f'<img class="tm-img" data-i="{i}" src="{have[s["img"]]["u"]}" alt="{e(IM[s["img"]]["alt"])}" decoding="async" style="opacity:{1 if i == 0 else 0}">' for i, s in enumerate(stops))
    caps = ''.join(f'<span class="tm-c" data-i="{i}"{"" if i == 0 else " hidden"}>{e(s["y"])} · {_cap(IM, s["img"])}</span>' for i, s in enumerate(stops))
    ticks = ''.join(f'<button type="button" class="tm-tick" data-i="{i}" aria-label="{e(s["y"])} · {e(s["t"])}"><i></i><span>{e(s["y"])}</span></button>' for i, s in enumerate(stops))
    return (f'<div class="mod tm" data-mod="timeline">{_top(cfg.get("intro", "시간 막대를 밀거나 해를 눌러, 같은 자리의 여러 때를 지나가 보세요."), "tm-n")}'
            f'<div class="tm-stage" style="{_box(round(1000 * r), 1000, 66)}">{imgs}<span class="tm-year" aria-hidden="true">{e(stops[0]["y"])}</span></div>'
            f'<p class="mod-cap tm-cap">{caps}</p>'
            f'<div class="tm-track"><span class="tm-line"></span><span class="tm-fill"></span>{ticks}'
            f'<input type="range" class="tm-range" min="0" max="1000" value="50" aria-label="시간 막대: 왼쪽은 옛날, 오른쪽은 오늘"><span class="tm-knob"></span></div>'
            f'<div class="mod-info tm-info" aria-live="polite"></div>'
            f'<p class="mod-done tm-done" hidden>{e(cfg.get("done", ""))}</p></div>')

def steps(cfg, have, IM):
    N = len(cfg['steps'])
    if cfg.get('svg'):
        stage = cfg['svg']
    else:
        base = cfg.get('img'); ims = []
        if base: ims.append(f'<img class="sp-img" data-i="0" src="{have[base]["u"]}" alt="{e(IM[base]["alt"])}">')
        for i, s in enumerate(cfg['steps'], 1):
            if s.get('img'): ims.append(f'<img class="sp-img" data-i="{i}" src="{have[s["img"]]["u"]}" alt="{e(IM[s["img"]]["alt"])}">')
        h = have[base or next(s['img'] for s in cfg['steps'] if s.get('img'))]
        stage = f'<div style="aspect-ratio:{h["w"]}/{h["h"]}"></div>' + ''.join(ims)
    cap = f'<p class="mod-cap">{e(cfg["cap"])}</p>' if cfg.get('cap') else ''
    marks = ''
    if cfg.get('marks'):   # 단계마다 쌓이는 것(예: 밀랍 밑에 지켜 둔 색). s단계부터 켜져요.
        li = ''.join(f'<li data-s="{m["s"]}"><i style="background:{e(m.get("c", "var(--accent)"))}"></i>{e(m["t"])}</li>' for m in cfg['marks'])
        marks = f'<div class="sp-marks"><span class="sp-ml">{e(cfg.get("marksLabel", "지금까지 쌓인 것"))}</span><ul>{li}</ul></div>'
    return (f'<div class="mod sp" data-mod="steps">{_top(cfg.get("intro", "단추를 누를 때마다 한 단계씩 만들어져요."), "sp-n")}'
            f'<div class="sp-stage" role="img" aria-label="{e(cfg.get("alt", "만드는 차례 그림"))}">{stage}</div>{cap}{marks}'
            f'<ol class="sp-dots" aria-hidden="true">{"".join("<li></li>" for _ in range(N))}</ol>'
            f'<div class="sp-ctl"><button type="button" class="mod-btn main sp-do"></button><button type="button" class="mod-btn sp-back" hidden>처음부터 다시</button></div>'
            f'<div class="mod-info sp-info" aria-live="polite"></div>'
            f'<p class="mod-done sp-done" hidden>{e(cfg.get("done", ""))}</p></div>')

def doors(cfg, have, IM):
    k = cfg['img']; h = have[k]; mo = cfg.get('month', 12)
    btns = ''.join(f'<button type="button" class="dr-door" data-d="{x["d"]}" style="left:{x["r"][0]:.2f}%;top:{x["r"][1]:.2f}%;width:{x["r"][2]:.2f}%;height:{x["r"][3]:.2f}%" aria-label="{x["d"]}일 창"><span class="dr-flap"><b>{x["d"]}</b></span></button>' for x in cfg['doors'])
    sims = cfg.get('sim', [1, 13, 24])
    sim = ('<div class="sim dr-sim" role="group" aria-label="날짜 바꿔 미리 보기"><b>미리 보기</b>' + ''.join(f'<button type="button" data-sim="{d}">{mo}월 {d}일</button>' for d in sims)
           + '<button type="button" data-sim="" class="on">오늘</button></div>') if sims else ''
    return (f'<div class="mod dr" data-mod="doors">{_top(cfg.get("intro", "그날이 된 창만 열려요. 반짝이는 창을 눌러 보세요."), "dr-n")}'
            f'<div class="dr-box" style="{_box(h["w"], h["h"], 78)}"><img src="{h["u"]}" alt="{e(IM[k]["alt"])}" decoding="async">{btns}</div>'
            f'<p class="mod-cap">{_cap(IM, k)}</p><p class="dr-say" aria-live="polite"></p>{sim}'
            f'<div class="mod-info dr-info" aria-live="polite"><p>{e(cfg.get("hint", "반짝이는 창이 오늘 열 수 있는 창이에요."))}</p></div>'
            f'<p class="mod-done dr-done" hidden>{e(cfg.get("done", ""))}</p></div>')

def gather(cfg, have, IM):
    k = cfg['img']; h = have[k]
    def piece(i, p):
        x, y, w, hh = p['r']
        bx = 0 if w >= 100 else x / (100 - w) * 100
        by = 0 if hh >= 100 else y / (100 - hh) * 100
        return (f'<button type="button" class="ga-piece" data-i="{i}" aria-label="{e(p["t"])}" '
                f'style="background-image:url({h["u"]});background-size:{100 * 100 / w:.3f}% {100 * 100 / hh:.3f}%;background-position:{bx:.3f}% {by:.3f}%">'
                f'<span class="ga-lab">{e(p.get("lab", p["t"]))}</span></button>')
    return (f'<div class="mod ga" data-mod="gather">{_top(cfg.get("intro", "흩어진 조각을 하나씩 눌러 제자리로 모아 보세요."), "ga-n")}'
            f'<div class="ga-stage"><div class="ga-home" style="aspect-ratio:{h["w"]}/{h["h"]}"><img class="ga-ghost" src="{h["u"]}" alt="{e(IM[k]["alt"])}" decoding="async" style="width:100%;height:100%"></div>'
            + ''.join(piece(i, p) for i, p in enumerate(cfg['pieces'])) + '</div>'
            f'<p class="mod-cap">{_cap(IM, k)}</p>'
            f'<div class="mod-info ga-info" aria-live="polite"><p>{e(cfg.get("hint", "조각마다 지금 있는 곳이 적혀 있어요. 눌러서 한자리에 모아 보세요."))}</p></div>'
            f'<div class="ga-ctl"><button type="button" class="mod-btn ga-again">다시 흩어 놓기</button></div>'
            f'<p class="mod-done ga-done" hidden>{e(cfg.get("done", ""))}</p></div>')

def trace(cfg, have, IM):
    g = cfg['glyph']; vb = g['vb']; vw = float(vb.split()[2])
    gs = ''.join(f'<path class="tr-g" data-i="{i}" d="{s["d"]}"/>' for i, s in enumerate(g['strokes']))
    ks = ''.join(f'<path class="tr-k" data-i="{i}" d="{s["d"]}"/>' for i, s in enumerate(g['strokes']))
    return (f'<div class="mod tr" data-mod="trace">{_top(cfg.get("intro", "빨간 점에서 시작해, 흐린 선을 손가락이나 마우스로 따라 그어 보세요."), "tr-n")}'
            f'<div class="tr-pad"><svg class="tr-svg" viewBox="{vb}" role="img" aria-label="{e(g.get("alt", g.get("name", "따라 쓸 글자")))}"><g>{gs}</g><g>{ks}</g><circle class="tr-dot" r="{vw * .035:.1f}" cx="0" cy="0"/></svg><canvas class="tr-cv"></canvas></div>'
            f'<div class="tr-ctl"><button type="button" class="mod-btn tr-show">써 보여 주기</button><button type="button" class="mod-btn tr-clear">처음부터 다시</button></div>'
            f'<div class="mod-info tr-info" aria-live="polite"><p>{e(cfg.get("hint", "빨간 점에서 시작해 흐린 선을 따라 그어 보세요. 다 그으면 먹으로 바뀌어요."))}</p></div>'
            f'<p class="mod-done tr-done" hidden>{e(cfg.get("done", ""))}</p></div>')
