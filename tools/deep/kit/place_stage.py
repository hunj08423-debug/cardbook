# -*- coding: utf-8 -*-
"""그레초의 밤 무대(SVG). 바위 동굴, 별, 구유·건초·소·나귀, 사람들의 촛불과 횃불.
소·나귀 실루엣: LadyofHats 그림(퍼블릭 도메인, 위키미디어 공용). 나머지는 이 안내서가 그림."""
import re, random

def _inner(path):
    s = open(path, encoding='utf-8').read()
    vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    body = s[s.index('>', s.index('<svg')) + 1:s.rindex('</svg>')]
    body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    body = re.sub(r'\s(fill|stroke|style|id|enable-background|xml:space)="[^"]*"', '', body)
    body = re.sub(r'\s+', ' ', body)
    return vb, body

def stage_svg(cow_svg, donkey_svg):
    R = random.Random(1223)
    cvb, cow = _inner(cow_svg)
    dvb, don = _inner(donkey_svg)
    stars = ''.join(f'<circle cx="{R.uniform(8, 792):.0f}" cy="{R.uniform(6, 150):.0f}" r="{R.choice([0.7, 0.9, 1.1, 1.4]):.1f}" fill="#fff" opacity="{R.uniform(.35, .95):.2f}"/>' for _ in range(46))
    hay = ''.join(f'<line x1="{x:.0f}" y1="{R.uniform(347, 353):.0f}" x2="{x + R.uniform(-9, 9):.0f}" y2="{R.uniform(330, 341):.0f}"/>' for x in [R.uniform(352, 448) for _ in range(34)])
    hay += ''.join(f'<line x1="{x:.0f}" y1="352" x2="{x + R.uniform(-14, 14):.0f}" y2="{R.uniform(362, 372):.0f}"/>' for x in [R.choice([R.uniform(342, 356), R.uniform(444, 458)]) for _ in range(8)])
    lights = [(52, 436), (88, 425), (124, 416), (160, 408), (198, 400), (604, 400), (640, 408), (676, 416), (712, 425), (748, 436),
              (262, 318), (538, 318), (318, 212), (482, 212), (234, 380), (566, 380)]
    lt = ''
    for k, (x, y) in enumerate(lights):
        torch = k % 3 == 0
        lt += (f'<g class="lt" style="transition-delay:{k * 0.06:.2f}s"><circle cx="{x}" cy="{y - 6}" r="{22 if torch else 15}" fill="url(#__U__lg)"/>'
               + (f'<line x1="{x}" y1="{y}" x2="{x - 2}" y2="{y + 16}" stroke="#2a1d12" stroke-width="2.4" stroke-linecap="round"/>' if torch else f'<rect x="{x - 2}" y="{y - 1}" width="4" height="9" rx="1" fill="#efe1bf"/>')
               + f'<circle class="c" cx="{x}" cy="{y - 5}" r="{3.6 if torch else 2.6}" fill="#ffd27a"/></g>')
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="밤하늘 아래 바위 동굴. 놓은 것들이 동굴 앞에 하나씩 나타난다."><defs>
<linearGradient id="__U__sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#060a15"/><stop offset="1" stop-color="#1a2440"/></linearGradient>
<linearGradient id="__U__sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a3150"/><stop offset=".6" stop-color="#b9785a"/><stop offset="1" stop-color="#f0b979"/></linearGradient>
<radialGradient id="__U__cave" cx=".5" cy=".72" r=".62"><stop offset="0" stop-color="#ffcf86"/><stop offset=".45" stop-color="#d9893c" stop-opacity=".7"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__lg"><stop offset="0" stop-color="#ffe2a0" stop-opacity=".95"/><stop offset=".4" stop-color="#ffb35c" stop-opacity=".4"/><stop offset="1" stop-color="#ff9a3c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".65" r=".75"><stop offset="0" stop-color="#fff0c8" stop-opacity=".75"/><stop offset=".55" stop-color="#ffc77a" stop-opacity=".35"/><stop offset="1" stop-color="#ff9f4a" stop-opacity="0"/></radialGradient>
<linearGradient id="__U__rock" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2a33"/><stop offset="1" stop-color="#17161b"/></linearGradient></defs>
<rect width="800" height="450" fill="url(#__U__sky)"/><rect class="sky2" width="800" height="450" fill="url(#__U__sky2)"/>
<g>{stars}</g>
<path d="M0 300 C 90 268 170 286 250 270 C 330 254 420 282 500 266 C 600 248 700 276 800 262 L800 450 L0 450Z" fill="#111a2e" opacity=".9"/>
<path fill="url(#__U__rock)" fill-rule="evenodd" d="M0 170 C 40 150 70 160 110 138 C 150 118 190 130 230 112 C 280 92 330 104 380 96 C 430 90 470 100 520 92 C 570 86 610 108 650 104 C 700 100 740 124 800 120 L800 450 L0 450Z
 M262 392 C 254 330 262 268 300 232 C 336 200 372 190 404 190 C 444 190 484 206 512 236 C 544 270 552 332 540 392Z"/>
<path d="M262 392 C 254 330 262 268 300 232 C 336 200 372 190 404 190 C 444 190 484 206 512 236 C 544 270 552 332 540 392Z" fill="#120d0a"/>
<path class="glow" d="M262 392 C 254 330 262 268 300 232 C 336 200 372 190 404 190 C 444 190 484 206 512 236 C 544 270 552 332 540 392Z" fill="url(#__U__cave)" opacity=".14"/>
<g fill="#151a1a">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(70, 150, 26), (102, 136, 22), (140, 124, 24), (600, 100, 22), (640, 98, 28), (686, 108, 24), (730, 118, 26), (764, 116, 20), (196, 118, 18), (560, 92, 16)])}</g>
<path d="M0 392 C 160 386 260 396 400 392 C 540 388 660 398 800 392 L800 450 L0 450Z" fill="#0d0b0a"/>
<g class="obj" data-o="donkey"><g transform="translate(330 214) scale(-1 1)"><svg x="0" y="0" width="98" height="178" viewBox="{dvb}" fill="#241a12" stroke="#7a5a36" stroke-width="3">{don}</svg></g></g>
<g class="obj" data-o="ox"><svg x="466" y="268" width="196" height="122" viewBox="{cvb}" fill="#241a12" stroke="#7a5a36" stroke-width="4">{cow}</svg></g>
<g class="obj" data-o="manger"><g fill="#2c2016" stroke="#7a5a36" stroke-width="1.6" stroke-linejoin="round"><path d="M336 348 L464 348 L450 376 L350 376Z"/><path d="M350 376 L340 402 M362 376 L372 402 M450 376 L460 402 M438 376 L428 402" stroke="#2c2016" stroke-width="6" stroke-linecap="round" fill="none"/><path d="M350 376 L340 402 M362 376 L372 402 M450 376 L460 402 M438 376 L428 402" stroke="#7a5a36" stroke-width="1.2" fill="none"/></g></g>
<g class="obj" data-o="hay"><g stroke="#d8b25a" stroke-width="1.6" stroke-linecap="round">{hay}</g><path d="M340 350 C 370 340 430 340 460 350" stroke="#e6c46e" stroke-width="3" fill="none" opacity=".8"/></g>
{lt}
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''
