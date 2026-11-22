# -*- coding: utf-8 -*-
"""깊은 카드: 키오스섬 부활절 ‘로켓 전쟁’(ev-rockets) · 중심 방식 = 놓아 보기
기준서 2판 · 틀 deep3-5 · 키트 3판(보탬 2) · 2026-11-22 20번 묶음 창(창 20)이 만듦 · 초벌(본부 소식 18)
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 2026년 4월 11일 성토요일, 자정이 가까운 브론타도스. 400미터 떨어진 두 언덕 사이 하늘이
     로켓 불빛 줄로 가득 차고, 철망을 두른 성당 안에서는 부활 예배가 이어지다 자정의 종이 울리는 순간.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 2026년 그날 밤의 차례(보도에 남은 시간표) — 미리 두르는 철판과 철망,
     저녁 6시 두 본당 팀의 함께 걷기(프로토테마·유로 위클리 뉴스), 늦은 밤 부활 예배(AP), 자정 가까이 수천 발(프로토테마),
     자정의 종(AP). 무대에 이 차례대로 하나씩 놓아요.
카드 크기: 큰 카드(장면 4) — 키오스 시 안내, 2016·2026년 보도, AP·로이터 기사가 넉넉하지만 쓸 수 있는 사진은 앞면 한 장이에요.
  로켓 만드는 법은 한 줄도 적지 않았어요(안전).
무대 그림: 이 카드 파일의 stage_svg()가 그려요(두 언덕·두 성당·마을은 이 안내서가 그린 그림 · 생김새는 단순하게 나타냄).
그림 원본(src)은 deep_src/ev-rockets/ (저장소 밖). 받는 법: commons_get.py"""
import math, random
S = 'ev-rockets/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

CHIOS = 'https://www.chios.gr/rouketopolemos/index-en.html'           # 키오스 시 관광 안내: 로켓 전쟁
WIKI = 'https://en.wikipedia.org/wiki/Rouketopolemos'
GV = 'https://globalvoices.org/2016/05/04/the-long-history-of-one-greek-islands-temporarily-canceled-easter-rocket-war/'
AP = 'https://globalnews.ca/news/1934170/mock-rocket-battle-marks-orthodox-easter-on-greek-island-of-chios/'   # AP 통신 2015.4.12
PT = 'https://en.protothema.gr/2026/04/12/magical-scenes-in-vrontados-chios-as-the-rocket-war-amazed-locals-and-tourists-video-photos/'
EWN = 'https://euroweeklynews.com/2026/04/14/chios-rocket-war-lights-up-vrontados-as-easter-tradition-continues-in-greece/'
RT = 'https://www.atlas-news.com/internacional/d004-grecia-quios-guerra-cohetes_4_02101657.html'           # 로이터 2026.4.12(아틀라스 뉴스 게재)
VG = 'https://visitgreece.gr/events/festival/easter-on-chios-island'
C_CARD = 'https://commons.wikimedia.org/wiki/File:%CE%92%CF%81%CE%BF%CE%BD%CF%84%CE%AC%CE%B4%CE%BF%CF%82_%CE%A7%CE%AF%CE%BF%CF%85_-_%CE%9F%CE%B9_%22%CF%81%CE%BF%CF%85%CE%BA%CE%B5%CF%84%CE%B1%CF%84%CE%B6%CE%AE%CE%B4%CE%B5%CF%82%22.jpg'
C_SCIO = 'https://commons.wikimedia.org/wiki/File:Isle_of_Scio_-_Wordsworth_Christopher_-_1882.jpg'


# ── 무대 그림: 두 언덕, 두 성당, 마을과 바닷가 길 (이 안내서가 그림) ─────────────────────────
CL, CR = (232, 238), (578, 232)          # 성 마르코 성당(왼쪽) · 성모 성당(오른쪽) 자리(땅 높이)

def _ground(x):
    """언덕 땅 높이(위에서 잰 y). 두 언덕 가운데 높은 쪽."""
    yl = CL[1] + (0.0032 if x > CL[0] else 0.0019) * (x - CL[0]) ** 2
    yr = CR[1] + (0.0033 if x < CR[0] else 0.0021) * (x - CR[0]) ** 2
    return min(yl, yr, 396)

def _bell(x, y, s):
    return (f'<path d="M{x - 6 * s:.1f} {y + 5 * s:.1f} C{x - 6 * s:.1f} {y - 2 * s:.1f} {x - 4 * s:.1f} {y - 7 * s:.1f} {x:.1f} {y - 7 * s:.1f} '
            f'C{x + 4 * s:.1f} {y - 7 * s:.1f} {x + 6 * s:.1f} {y - 2 * s:.1f} {x + 6 * s:.1f} {y + 5 * s:.1f}Z"/><circle cx="{x:.1f}" cy="{y + 6.6 * s:.1f}" r="{1.5 * s:.1f}"/>')

def _waves(x, y):
    out = ''
    for r in (12, 19, 26):
        for a0, a1 in ((150, 210), (-30, 30)):
            p0 = (x + r * math.cos(math.radians(a0)), y + r * math.sin(math.radians(a0)))
            p1 = (x + r * math.cos(math.radians(a1)), y + r * math.sin(math.radians(a1)))
            out += f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}"/>'
    return out

def stage_svg():
    R = random.Random(1889)
    stars = ''.join(f'<circle cx="{R.uniform(6, 794):.0f}" cy="{R.uniform(6, 150):.0f}" r="{R.choice([0.6, 0.8, 1.0, 1.2])}" fill="#fff" opacity="{R.uniform(.3, .85):.2f}"/>' for _ in range(44))
    pts = ' '.join(f'{x},{_ground(x):.1f}' for x in range(0, 801, 10))
    hills = f'<polygon points="0,450 {pts} 800,450" fill="#0b1222"/>'
    # 마을 집들: 언덕 비탈을 따라 두 줄(성당 둘레와 이름표 자리는 비워요)
    houses, near = [], []
    for row, off in ((0, 30), (1, 56), (2, 82)):
        x = 14 + row * 11
        while x < 790:
            w, h = R.choice([22, 24, 26, 28]), R.choice([13, 14, 16])
            y = _ground(x + w / 2) + off
            busy = (abs(x + w / 2 - CL[0]) < 86 or abs(x + w / 2 - CR[0]) < 92) and off < 60
            if y + h < 392 and not busy:
                houses.append((x, y, w, h))
                if (abs(x + w / 2 - CL[0]) < 125 or abs(x + w / 2 - CR[0]) < 125) and off < 60: near.append((x, y, w, h))
            x += w + R.choice([8, 10, 12, 14])
    hs = ''
    for x, y, w, h in houses:
        hs += f'<rect x="{x}" y="{y:.0f}" width="{w}" height="{h}" fill="#1b2335"/><path d="M{x - 1} {y:.0f} L{x + w / 2:.0f} {y - 5:.0f} L{x + w + 1} {y:.0f}Z" fill="#26202a"/>'
        if R.random() < .45: hs += f'<rect x="{x + 5}" y="{y + 4:.0f}" width="4" height="5" fill="#ffcf7a" opacity=".55"/>'
    # 바닷가 길의 가로등
    lamps = ''.join(f'<line x1="{x}" y1="398" x2="{x}" y2="380" stroke="#2b3550" stroke-width="1.6"/><circle cx="{x}" cy="379" r="7" fill="url(#__U__lg)" opacity=".55"/><circle cx="{x}" cy="379" r="1.6" fill="#ffe2a0"/>' for x in range(150, 700, 66))
    # 두 성당(생김새는 단순하게: 왼쪽은 둥근 지붕과 정문 위 이콘, 오른쪽은 시계 달린 종탑)
    lx, ly = CL
    left = (f'<g fill="#1f2638" stroke="#3a4560" stroke-width="1">'
            f'<rect x="{lx - 42}" y="{ly - 38}" width="84" height="42"/>'
            f'<rect x="{lx - 14}" y="{ly - 54}" width="28" height="16"/>'
            f'<path d="M{lx - 18} {ly - 54} A18 18 0 0 1 {lx + 18} {ly - 54}Z" fill="#273049"/>'
            f'<rect x="{lx - 56}" y="{ly - 74}" width="16" height="78"/><path d="M{lx - 58} {ly - 74} L{lx - 48} {ly - 88} L{lx - 38} {ly - 74}Z"/></g>'
            f'<path d="M{lx} {ly - 73} V{ly - 86} M{lx - 5} {ly - 81} H{lx + 5}" stroke="#8d97ad" stroke-width="1.6"/>'
            f'<rect x="{lx - 53}" y="{ly - 68}" width="10" height="13" rx="5" fill="#0a0f1c"/>'
            f'<path d="M{lx - 7} {ly + 4} V{ly - 9} A7 7 0 0 1 {lx + 7} {ly - 9} V{ly + 4}Z" fill="#0a0e18"/>'
            + ''.join(f'<rect x="{lx + dx}" y="{ly - 26}" width="5" height="9" rx="2.5" fill="#0a0f1c"/>' for dx in (-34, -24, 19, 29))
            + f'<rect x="{lx - 8}" y="{ly - 30}" width="16" height="13" rx="1.5" fill="#c9a34a"/>'
            f'<ellipse cx="{lx + 1}" cy="{ly - 21.5}" rx="4.6" ry="2.1" fill="#4a3416"/><circle cx="{lx - 4.4}" cy="{ly - 23.4}" r="2" fill="#4a3416"/>'
            f'<path d="M{lx - 1} {ly - 23} L{lx + 4} {ly - 27} L{lx + 3} {ly - 23}Z" fill="#4a3416"/>')
    rx_, ry_ = CR
    right = (f'<g fill="#1f2638" stroke="#3a4560" stroke-width="1">'
             f'<rect x="{rx_ - 46}" y="{ry_ - 34}" width="88" height="38"/>'
             f'<rect x="{rx_ + 14}" y="{ry_ - 120}" width="22" height="124"/><path d="M{rx_ + 12} {ry_ - 120} L{rx_ + 25} {ry_ - 136} L{rx_ + 38} {ry_ - 120}Z"/></g>'
             f'<path d="M{rx_ - 50} {ry_ - 34} L{rx_ - 2} {ry_ - 48} L{rx_ + 14} {ry_ - 43} L{rx_ + 14} {ry_ - 34}Z" fill="#3b2624"/>'
             f'<path d="M{rx_ + 25} {ry_ - 136} V{ry_ - 148} M{rx_ + 20} {ry_ - 143} H{rx_ + 30}" stroke="#8d97ad" stroke-width="1.6"/>'
             f'<circle cx="{rx_ + 25}" cy="{ry_ - 104}" r="7.5" fill="#e9dfc8" stroke="#7a6a4a" stroke-width="1.2"/>'
             f'<path d="M{rx_ + 25} {ry_ - 104} V{ry_ - 109} M{rx_ + 25} {ry_ - 104} L{rx_ + 29} {ry_ - 102}" stroke="#2a2418" stroke-width="1.2"/>'
             f'<rect x="{rx_ + 19}" y="{ry_ - 88}" width="12" height="16" rx="6" fill="#0a0f1c"/>'
             f'<path d="M{rx_ - 17} {ry_ + 4} V{ry_ - 8} A7 7 0 0 1 {rx_ - 3} {ry_ - 8} V{ry_ + 4}Z" fill="#0a0e18"/>'
             + ''.join(f'<rect x="{rx_ + dx}" y="{ry_ - 24}" width="5" height="9" rx="2.5" fill="#0a0f1c"/>' for dx in (-38, -28, 2)))
    # 과녁 표시와 이름표(늘 보여요)
    halo = 'paint-order:stroke;stroke:#060a14;stroke-width:3px;stroke-linejoin:round'
    marks = (f'<g fill="none" stroke="#ff9f5a" stroke-width="1.4" stroke-dasharray="3 4" opacity=".8">'
             f'<circle cx="{lx}" cy="{ly - 44}" r="38"/><circle cx="{rx_ + 25}" cy="{ry_ - 104}" r="16"/></g>'
             f'<path d="M{lx + 46} {ly + 6} L{rx_ - 50} {ry_ + 6}" stroke="#c9d3e6" stroke-width="1" stroke-dasharray="2 5" opacity=".7"/>'
             f'<text x="{(lx + rx_) / 2 + 2:.0f}" y="{ly - 2}" text-anchor="middle" fill="#dfe6f3" style="font:700 16px var(--sans,sans-serif);{halo}">약 400m</text>'
             f'<rect x="{lx - 118}" y="{ly + 12}" width="236" height="50" rx="9" fill="#060a14" opacity=".74"/>'
             f'<text x="{lx}" y="{ly + 33}" text-anchor="middle" fill="#f3ead8" style="font:700 18px var(--sans,sans-serif)">성 마르코 성당</text>'
             f'<text x="{lx}" y="{ly + 53}" text-anchor="middle" fill="#ffb98a" style="font:600 14px var(--sans,sans-serif)">과녁: 둥근 지붕 · 정문 위 이콘</text>'
             f'<rect x="{rx_ - 122}" y="{ry_ + 14}" width="244" height="50" rx="9" fill="#060a14" opacity=".74"/>'
             f'<text x="{rx_}" y="{ry_ + 35}" text-anchor="middle" fill="#f3ead8" style="font:700 18px var(--sans,sans-serif)">성모 성당(에리티아니)</text>'
             f'<text x="{rx_}" y="{ry_ + 55}" text-anchor="middle" fill="#ffb98a" style="font:600 14px var(--sans,sans-serif)">과녁: 종탑의 시계</text>')
    # ① 철판과 철망
    shield = (f'<g class="obj" data-o="shield"><g fill="url(#__U__mesh)" stroke="#a9b8cf" stroke-width=".8" stroke-opacity=".5">'
              f'<rect x="{lx - 62}" y="{ly - 94}" width="112" height="100" rx="3"/><rect x="{rx_ - 52}" y="{ry_ - 152}" width="94" height="158" rx="3"/>'
              + ''.join(f'<rect x="{x - 2}" y="{y - 7:.0f}" width="{w + 4}" height="{h + 9}"/>' for x, y, w, h in near) + '</g>'
              + ''.join(f'<rect x="{x + 4}" y="{y + 3:.0f}" width="7" height="7" fill="#6b4a2a"/>' for x, y, w, h in near) + '</g>')
    # ② 함께 걷기(바닷가 길)
    walk = ''.join(f'<circle cx="{x}" cy="{388 - (k % 2)}" r="3"/><path d="M{x - 4} 399 L{x - 3} 391 Q{x} 389 {x + 3} 391 L{x + 4} 399Z"/>' for k, x in enumerate(range(262, 546, 19)))
    march = (f'<g class="obj" data-o="march"><g fill="#d8c7a0">{walk}</g>'
             f'<g stroke="#8d97ad" stroke-width="1.4"><line x1="246" y1="399" x2="246" y2="364"/><line x1="558" y1="399" x2="558" y2="364"/></g>'
             f'<path d="M246 364 L264 369 L246 374Z" fill="#f2c46b"/><path d="M558 364 L576 369 L558 374Z" fill="#9fc0e8"/></g>')
    # ③ 부활 예배: 성당 문과 창의 불빛
    win = lambda x, y: f'<rect x="{x}" y="{y}" width="5" height="9" rx="2.5" fill="#ffcf7a"/>'
    service = (f'<g class="obj" data-o="service"><circle cx="{lx}" cy="{ly - 2}" r="30" fill="url(#__U__lg)"/><circle cx="{rx_ - 10}" cy="{ry_ - 2}" r="30" fill="url(#__U__lg)"/>'
               + ''.join(win(lx + dx, ly - 26) for dx in (-34, -24, 19, 29)) + ''.join(win(rx_ + dx, ry_ - 24) for dx in (-38, -28, 2))
               + f'<path d="M{lx - 7} {ly + 4} V{ly - 9} A7 7 0 0 1 {lx + 7} {ly - 9} V{ly + 4}Z" fill="#ffd27a" opacity=".85"/>'
               f'<path d="M{rx_ - 17} {ry_ + 4} V{ry_ - 8} A7 7 0 0 1 {rx_ - 3} {ry_ - 8} V{ry_ + 4}Z" fill="#ffd27a" opacity=".85"/></g>')
    # ④ 로켓: 두 언덕에서 서로의 성당 쪽으로(불빛 줄 24개가 차례로 켜져요)
    lt = ''
    for k in range(24):
        if k % 2 == 0:
            sx = R.uniform(272, 380); tx, ty = R.uniform(rx_ + 8, rx_ + 42), R.uniform(ry_ - 122, ry_ - 30)
        else:
            sx = R.uniform(432, 536); tx, ty = R.uniform(lx - 30, lx + 30), R.uniform(ly - 72, ly - 14)
        sy = _ground(sx) + 2
        cx, cy = (sx + tx) / 2 + R.uniform(-30, 30), min(sy, ty) - R.uniform(115, 185)
        d = f'M{sx:.0f} {sy:.0f} Q{cx:.0f} {cy:.0f} {tx:.0f} {ty:.0f}'
        sparks = ''.join(f'<circle cx="{tx + R.uniform(-11, 11):.0f}" cy="{ty + R.uniform(-9, 9):.0f}" r="1.1" fill="#ffd27a"/>' for _ in range(4))
        lt += (f'<g class="lt"><path d="{d}" fill="none" stroke="#ff9d42" stroke-width="1.3" opacity=".5"/>'
               f'<path d="{d}" fill="none" stroke="#ffd08a" stroke-width="2.3" stroke-linecap="round" stroke-dasharray="0.5 7" opacity=".9"/>'
               f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="10" fill="url(#__U__lg)"/>{sparks}<circle class="c" cx="{tx:.0f}" cy="{ty:.0f}" r="2.6" fill="#fff0c0"/></g>')
    # ⑤ 자정의 종
    bells = (f'<g class="obj" data-o="bells"><g fill="#f2c46b">{_bell(lx - 48, ly - 62, .72)}{_bell(rx_ + 25, ry_ - 80, .85)}</g>'
             f'<g fill="none" stroke="#ffe2a0" stroke-width="1.4" opacity=".85">{_waves(lx - 48, ly - 62)}{_waves(rx_ + 25, ry_ - 80)}</g></g>')
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="밤하늘 아래 마주 보는 두 언덕. 왼쪽 언덕에는 둥근 지붕의 성 마르코 성당, 오른쪽 언덕에는 시계 달린 종탑의 성모 성당이 서 있고, 비탈에는 마을 집들, 아래에는 바닷가 길이 있다. 놓은 것들이 하나씩 나타난다."><defs>
<linearGradient id="__U__sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#050914"/><stop offset="1" stop-color="#16223d"/></linearGradient>
<linearGradient id="__U__sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f3d63"/><stop offset=".55" stop-color="#a87668"/><stop offset="1" stop-color="#e9b886"/></linearGradient>
<radialGradient id="__U__lg"><stop offset="0" stop-color="#ffe2a0" stop-opacity=".95"/><stop offset=".4" stop-color="#ffb35c" stop-opacity=".4"/><stop offset="1" stop-color="#ff9a3c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__gl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffb35c" stop-opacity=".55"/><stop offset="1" stop-color="#ff7a2a" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".55" r=".8"><stop offset="0" stop-color="#ffe9c4" stop-opacity=".55"/><stop offset=".6" stop-color="#ffc98a" stop-opacity=".25"/><stop offset="1" stop-color="#ffb070" stop-opacity="0"/></radialGradient>
<pattern id="__U__mesh" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0V6M0 0H6" stroke="#a9b8cf" stroke-width=".7" opacity=".8"/></pattern></defs>
<rect width="800" height="450" fill="url(#__U__sky)"/><g>{stars}</g><rect class="sky2" width="800" height="450" fill="url(#__U__sky2)"/>
<path d="M0 272 C 110 250 210 262 320 252 C 430 242 520 256 640 244 C 720 238 770 248 800 246 L800 450 L0 450Z" fill="#0f1830"/>
<ellipse class="glow" cx="405" cy="190" rx="320" ry="160" fill="url(#__U__gl)" opacity=".14"/>
{hills}{hs}
<rect y="398" width="800" height="52" fill="#0a1530"/><rect y="396" width="800" height="5" fill="#151d2e"/>
<g stroke="#1d2c50" stroke-width="1.2">{''.join(f'<line x1="{x}" y1="{y}" x2="{x + 26}" y2="{y}"/>' for x, y in [(60, 416), (190, 430), (330, 420), (470, 436), (600, 418), (720, 432)])}</g>
{lamps}{left}{right}{marks}
{shield}{march}{service}{lt}{bells}
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''

ITEMS = [
 {'id': 'shield', 't': '철판과 철망', 'la': '미리', 'say': '성당과 가까운 집들을 철판과 철망으로 둘러싸요. 창문에는 판자를 대요.'},
 {'id': 'march', 't': '함께 걷기', 'la': '저녁 6시', 'say': '저녁 6시, 두 본당의 로켓 팀들이 바닷가 길을 함께 걸어요. 그날 밤 행사의 시작이에요.'},
 {'id': 'service', 't': '부활 예배', 'la': '늦은 밤', 'say': '밤이 깊으면 두 성당에서 부활 예배가 시작돼요. 사람들은 철망 안쪽 성당으로 들어가요.'},
 {'id': 'lights', 't': '로켓', 'la': '자정 가까이', 'say': '자정이 가까워지자, 수천 발의 로켓이 두 언덕 사이 하늘을 가로질러요.'},
 {'id': 'bells', 't': '자정의 종', 'la': '자정', 'say': '자정, 종이 울리며 부활을 알려요. 그 종소리 위로도 로켓이 쉬지 않고 날아요.'},
]

CARD = {
 'id': 'ev-rockets', 'mode': '놓아 보기',
 'pagetitle': "키오스섬 부활절 ‘로켓 전쟁’",
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>해마다 정교회 부활절 전날 밤</b><span>그리스 키오스섬 브론타도스</span>',
 'lead': '그리스 키오스섬의 마을 브론타도스, 정교회 부활절 전날 밤. 두 언덕 위 두 성당 사이로 손으로 만든 로켓 수천 발이 오가는 동안, 성당 안에서는 부활 예배가 이어져요. 2026년 그날 밤의 차례대로 무대에 하나씩 놓아 보세요.',
 'leadKid': '부활절 전날 밤, 그리스의 한 마을에서는 두 교회 사람들이 서로 불꽃 로켓을 쏜대. 진짜 싸움은 아니야! 그 밤을 하나씩 놓아 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 2판 · 초벌). 장면에는 키오스 시의 안내와 2015·2016·2026년 보도에 있는 것만 옮겼고, 시작에 관한 이야기는 ‘전해진다’고 밝혔어요. 로켓 만드는 법은 적지 않았어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 무대 그림은 이 안내서가 그렸어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 # 화면 색: 밤하늘 아래 불씨 빛(로켓 불꽃의 주황) · 끝(다음 날 아침)에는 로켓 불빛 줄이 연기처럼 옅어져요
 'theme': """:root{--accent:#9c3f17;--accent-ink:#fff8f3;--soft:rgba(156,63,23,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#f2a477;--accent-ink:#1a0f08;--soft:rgba(242,164,119,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#f2a477;--accent-ink:#1a0f08;--soft:rgba(242,164,119,.10);--stamp:#e86f5d}
.pl.lit .lt.on{opacity:.16;transition:opacity 2.6s ease}""",
 'stamp': {'t': '로켓', 'y': '2026', 'sub': '키오스 · 브론타도스'},
 'doneNote': '부활절 밤 불꽃 소리를 듣게 되면, 철망 안쪽에서 이어지던 부활 예배를 떠올려 보세요.',
 'images': {
  'card': {'src': S + '-.jpg', 'cap': '철망 뒤의 ‘로켓 전사들’, 2015년 4월 11일 밤',
           'cr': '사진: Dimitris Tachynakos · CC BY-SA 4.0 · 위키미디어 공용', 'u': C_CARD,
           'alt': '연기 낀 밤, 철망 울타리 뒤 비탈에 사람들이 서 있고, 그 위로 불꽃 줄기와 불티가 비스듬히 쏟아진다. 앞쪽에는 잎 없는 나뭇가지가 철망을 타고 뻗어 있다.'},
  'scio': {'src': S + 'Isle_of_Scio_-_Wordsworth_Christopher_-_1882.jpg', 'crop': (0.02, 0.02, 0.98, 0.76),
           'cap': '키오스섬, 크리스토퍼 워즈워스의 책 『그리스』(1882년 판)에 실린 판화',
           'cr': '판화: W. 하비 그림 · 에번스 새김 · 퍼블릭 도메인 · 위키미디어 공용', 'u': C_SCIO,
           'alt': '옛 판화. 바닷가 벼랑 사이로 잔잔한 바다와 돛단배, 멀리 산들이 보이고, 오른쪽 벼랑길을 사람들과 짐 실은 나귀가 걸어간다. 하늘에는 새들이 난다.'},
 },
 'scenes': [
  {'id': 'wire', 'label': '철망 뒤에서', 'kind': 'photo', 'img': 'card',
   'text': ['2015년 4월 11일 밤 11시쯤, 그리스 키오스섬의 브론타도스. 철망 너머로 불꽃이 쏟아지고, 사람들이 그 뒤에 서 있어요. 사진을 찍은 사람은 이들을 ‘로켓 전사들’이라고 불렀어요.',
            '브론타도스에는 큰 본당이 둘 있어요. 성 마르코 성당과 성모 성당(파나기아 에리티아니)이에요. 해마다 정교회 부활절 전날 밤, 두 본당 사람들은 손으로 만든 로켓을 서로의 성당 쪽으로 쏘아요. 이것을 ‘로켓 전쟁’(루케토폴레모스)이라고 불러요.'],
   'text2': ['로켓을 쏘는 팀은 로켓을 만드는 사람들이기도 해요. 적지 않은 재료값도 스스로 내요. 팀마다 역사나 전통, 또는 대장의 별명에서 따온 이름이 있어요.'],
   'kid': '부활절 전날 밤, 두 교회 사람들이 서로 불꽃 로켓을 쏜대. 부활절 밤을 아주아주 시끄럽게 맞는 거래.',
   'kidq': '사람들이 왜 철망 뒤에 서 있을까?'},
  {'id': 'night', 'label': '두 언덕의 밤', 'kind': 'mod', 'mod': 'place', 'night': True,
   'text': ['두 성당은 400미터쯤 떨어진 두 언덕 위에 서 있어요. 과녁도 정해져 있어요. 성모 성당 쪽은 성 마르코 성당의 둥근 지붕과, 정문 위에 걸린 사자와 함께 있는 마르코 이콘을 겨눠요. 성 마르코 쪽은 성모 성당의 시계를 겨눠요.',
            '2026년 4월 11일, 그날 밤의 차례대로 무대에 하나씩 놓아 보세요.'],
   'text2': ['2026년에는 주최 측이 말하기로 2만 발쯤 쏘았어요. 미리 정한 자리에서만 쏘았고, 사람들이 안전하게 오갈 수 있도록 중간중간 쉬기도 했어요.'],
   'kid': '두 교회가 마주 보는 언덕 위에 있어. 하나씩 놓아 보자. 마지막엔 종이 울려!',
   'kidq': '밖에서 로켓이 쉬익쉬익 날아다닐 때, 교회 안에서는 어떤 소리가 들릴까?'},
  {'id': 'cannon', 'label': '대포에서 로켓으로', 'kind': 'photo', 'img': 'scio',
   'text': ['위 판화는 1882년 영국 책에 실린 키오스섬이에요. 이 풍습이 언제 시작되었는지는 분명하지 않아요. 섬이 오스만 제국의 다스림을 받던 때로 거슬러 올라간다고 전해져요. 두 본당의 아이들이 돌을 던지며 ‘전쟁’ 놀이를 하던 데서 시작되었다고 말하는 사람들도 있어요.',
            '전해지는 이야기로는 처음에는 진짜 대포를 썼는데, 1889년 오스만 관리들이 대포를 막자 로켓으로 바뀌었다고 해요. 키오스 시의 안내는 그해 첫 로켓을 불꽃 기술자가 이탈리아 방식으로 만들었다고 적어요.'],
   'text2': ['1900년 무렵부터는 본당 사람들이 직접 로켓을 만들어 함께하기 시작했어요. 독일 점령기에는 거의 끊길 뻔했고, 군사 정권 때는 멈췄다가 1970년에 다시 열렸어요. 1950년대부터는 성당 가까운 들판에서 맞은편 성당을 겨눠 쏘게 되었어요.'],
   'kid': '옛날에는 진짜 대포를 쏘았대! 대포를 못 쓰게 되자 로켓으로 바뀌었대.',
   'kidq': '사람들은 왜 부활절 밤을 이렇게 시끄럽게 맞았을까?'},
  {'id': 'morning', 'label': '다음 날 아침', 'kind': 'quote',
   'text': ['다음 날, 종탑에 맞은 자국을 세어 이긴 쪽을 가린다고 해요. 그런데 두 본당은 늘 저마다 자기가 이겼다고 말해요. 깨진 유리창과 지붕 기와 같은 작은 피해도 남아요.'],
   'quote': {'t': '이 전쟁에는 이긴 쪽도 진 쪽도 없어요. 사람들은 악수하고, 내년에 다시 만나자고 약속해요.',
             'from': '키오스 시 관광 안내 ‘로켓 전쟁’ · 영어를 이 안내서가 우리말로 옮김', 'u': CHIOS},
   'text2': ['모두가 이 풍습을 반기는 것은 아니에요. 2016년에는 집이 망가진다며 소송을 하겠다는 주민들이 있어 열리지 않았고, 2017년부터 시간과 로켓 수에 규칙을 두고 다시 열렸어요. 2026년에는 부활절을 앞두고 로켓을 만들던 작업장에 불이 나 네 사람이 화상을 입었고 일곱 사람이 체포되었어요. 그해 로켓 전쟁은 성토요일 오후에야 열기로 정해졌어요.',
             '다음 정교회 부활절 전날 밤은 2027년 5월 1일이에요.'],
   'kid': '다음 날 아침, 두 교회는 서로 “우리가 이겼어!” 한대. 그리고 악수하고 내년에 또 만나자고 약속해.',
   'kidq': '둘 다 이겼다고 하면, 누가 이긴 걸까?'},
 ],
 'imagine': {'t': '깜깜한 언덕, 화약 냄새가 바람에 실려 와요. 쉬익, 쉬익, 머리 위로 불빛 줄이 수없이 지나가고, 철망에 무언가 탁탁 부딪혀요. 연기가 골짜기를 채워요. 철망 안쪽 성당에서는 부활의 노래가 이어지고, 자정의 종이 울리기 시작해요.',
             'kid': '눈을 감아 봐. 쉬익! 쉬익! 머리 위로 불빛이 날아가. 탁탁, 철망에 부딪히는 소리. 그런데 교회 안에서는 노래가 들려. 땡, 땡, 자정의 종이야!'},
 'lines': ['두 언덕, 두 성당, 하나의 밤.', '철망 안쪽에서 이어지는 부활의 노래.', '이긴 쪽도 진 쪽도 없는 전쟁.', '내년 부활절 밤에 다시.'],
 'linesKid': ['쉬익! 로켓이 날아가!', '교회 안에서는 노래해.', '내년에 또 만나!'],
 'close': {'form': '앞을 내다보기',
           'from': '다음 정교회 부활절 전날 밤(2027년 5월 1일) — 키오스 시 안내의 ‘악수하고 내년을 약속해요’ · 2026년에는 성토요일 오후에야 열기로 정해졌어요(프로토테마)',
           'ask': '로켓이 쏟아지는 동안에도 철망 안쪽에서는 부활 예배가 이어져요. 둘레가 아무리 시끄러워도, 내가 지키고 싶은 자리는 어디인가요?',
           'askKid': '밖이 아주 시끄러울 때, 너는 어디에 있으면 마음이 편해?'},
 'goals': {
  's4': {'t': '그날 밤의 차례', 'p': '2026년 그날 밤의 차례(철판과 철망, 함께 걷기, 부활 예배, 로켓, 자정의 종)대로 다 놓으면 카드에 금박이 입혀져요.',
         'how': '둘째 장면의 무대에 그날 밤의 차례대로 하나씩 놓아 보세요', 'done': '그날 밤의 차례대로 두 언덕의 밤을 열었어요',
         'ways': [{'id': 'plOrder', 't': '철판과 철망 → 함께 걷기 → 부활 예배 → 로켓 → 자정의 종 차례로 놓기'}]},
  's5': {'t': '아이와 함께', 'p': '아이와 함께 ‘영화처럼 보기’를 끝까지 보면 카드가 채색돼요.',
         'how': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'done': '아이와 함께 두 언덕의 밤을 끝까지 봤어요',
         'ways': [{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'place': {
   'items': ITEMS, 'order': '철판과 철망, 함께 걷기, 부활 예배, 로켓, 자정의 종',
   'intro': '아래에서 하나를 골라 무대에 놓아 보세요. 2026년 그날 밤의 차례는 철판과 철망, 함께 걷기, 부활 예배, 로켓, 자정의 종이에요.',
   'climax': '다음 날 아침, 두 본당은 저마다 자기가 이겼다고 말해요. 그리고 악수하며 내년을 약속해요.<span class="la">이 전쟁에는 이긴 쪽도 진 쪽도 없어요 · 키오스 시 관광 안내</span>',
   'home': None, 'daylight': False,
   'wrongOrder': '2026년 그날 밤의 차례는 이래요: {order}',
   'orderDone': '그날 밤의 차례대로 다 놓았어요',
   'svg': stage_svg()}},
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 놓아 보기</button></div>
</div></div>'''},
 'deep': [
  {'h': '기록마다 다른 점', 'p': [
    '<b>언제부터</b> 위키백과와 글로벌 보이스는 오스만 제국 때로 거슬러 올라간다고 적고, AP 통신은 19세기에 시작되었지만 더 오래되었을 수도 있다고 적어요. 키오스 시의 안내는 첫 로켓이 1889년에 나왔다고 적어요.',
    '<b>몇 시에</b> 2026년 보도는 자정 조금 전부터 수천 발이 날았다고 적고, 다른 기록들은 자정 부활 예배 때 시작된다고 적어요.',
    '<b>누가 이겼나</b> 다음 날 종탑에 맞은 자국을 센다는 기록도 있고, 로켓이 너무 많아 다음 날 셀 수 없다는 기록도 있어요. 키오스 시의 안내는 이 전쟁에 이긴 쪽도 진 쪽도 없다고 적어요.']},
  {'h': '함께 읽는 말씀', 'p': [
    '말씀은 뜻만 옮기고, 본문은 대한성서공회 개역개정으로 이어 드려요.',
    '<b>' + bl('1CO.15', '고린도전서 15장 54~57절') + '</b> 죽음이 생명에 삼켜졌다며 “죽음아, 너의 승리가 어디 있느냐” 하고 묻는 말씀이에요. 키오스 시의 안내는 부활절 밤의 로켓이 삶이 죽음을 이긴 것을 나타낸다고 적어요.']},
  {'h': '직접 가 보기', 'checked': '2026년 11월 22일', 'p': [
    '브론타도스는 키오스 시내 북쪽에 있어요. 다음 정교회 부활절 전날 밤은 2027년 5월 1일이에요.',
    '해마다 그 무렵에 열지 말지가 정해져요(2016년에는 열리지 않았고, 2026년에는 성토요일 오후에야 정해졌어요). 로켓이 떨어지는 곳 가까이는 위험하니, 그해의 안내를 꼭 따라 주세요.'],
   'links': [{'t': '키오스 시: 로켓 전쟁 안내', 'u': CHIOS, 'm': '영어'},
             {'t': '그리스 관광청(Visit Greece): 키오스섬의 부활절', 'u': VG, 'm': '영어'}]},
 ],
 'src': [
  {'l': '키오스 시 관광 안내: 로켓 전쟁 — 두 본당, 과녁(성 마르코의 둥근 지붕과 사자 이콘, 성모 성당의 시계), 아이들의 돌 던지기 이야기, 1889년 첫 로켓, 1900년부터 본당 사람들이, 독일 점령기와 군사 정권, 1970년, 1950년대 들판, 팀이 직접 만들고 재료값을 냄, 깨진 창과 기와, 이긴 쪽도 진 쪽도 없음, 삶이 죽음을 이김', 'u': CHIOS},
  {'l': '위키백과(영어): Rouketopolemos — 두 언덕, 약 400미터, 철판과 철망, 오스만 시대 전설, 1889년 대포 금지, 2016년 취소와 2017년 규칙, 다음 날 자국 세기, 저마다 이겼다고 함', 'u': WIKI},
  {'l': '글로벌 보이스(2016.5.4): 2016년 취소(주민들의 소송 경고), 자정 부활 예배 때, 다음 날 셀 수 없음', 'u': GV},
  {'l': 'AP 통신(글로벌 뉴스 게재, 2015.4.12): 종이 울릴 때, 늦은 밤 예배에 들어가는 사람들, 성당과 집을 두른 철망, 19세기', 'u': AP},
  {'l': '프로토테마(2026.4.12): 저녁 6시 두 본당 팀의 함께 행진, 자정 조금 전 수천 발, 일곱 명 체포, 중간 휴식, 성토요일 오후에 확정', 'u': PT},
  {'l': '유로 위클리 뉴스(2026.4.14): 미리 정한 발사 자리, 바닷가 행진, 맞은 자국을 셈', 'u': EWN},
  {'l': '로이터(아틀라스 뉴스 게재, 2026.4.12): 주최 측 추산 2만 발, 작업장 화재로 네 명 화상·일곱 명 체포, 규모를 줄임', 'u': RT},
  {'l': '그리스 관광청(Visit Greece): 키오스섬의 부활절 — 2026년 4월 11일 저녁, 두 큰 본당', 'u': VG},
  {'l': '위키미디어 공용: 앞면 사진 정보(2015년 4월 11일 22시 56분, ‘로켓 전사들’)', 'u': C_CARD},
  {'l': '대한성서공회 개역개정: 고린도전서 15장', 'u': NKRV + '1CO.15'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '40% 40%', 'p1': '55% 35%', 's0': 1.22, 's1': 1.04, 'kicker': '2015년 4월 11일 밤 · 그리스 키오스섬', 'title': "부활절 ‘로켓 전쟁’",
   'lines': [{'t': '부활절 전날 밤, 철망 너머로 불꽃이 쏟아져요.'}, {'t': '그리스 키오스섬의 마을, 브론타도스예요.'}],
   'kid': [{'t': '부활절 전날 밤이야. 와, 불꽃이 쏟아져!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '두 언덕의 밤'},
  {'type': 'mod', 'mod': 'place', 'ch': 1,
   'lines': [{'t': '두 성당이 400미터쯤 떨어진 두 언덕 위에 마주 서 있어요.'},
             {'t': '미리, 성당과 가까운 집들을 철판과 철망으로 둘러싸요.', 'act': 'shield'},
             {'t': '2026년 저녁 6시, 두 본당의 팀들이 함께 걸어요.', 'act': 'march'},
             {'t': '늦은 밤, 성당에서는 부활 예배가 시작돼요.', 'act': 'service'},
             {'t': '자정이 가까워지자, 수천 발의 로켓이 하늘을 가로질러요.', 'act': 'lights', 'wait': 3400},
             {'t': '자정, 종이 울리며 부활을 알려요.', 'act': 'bells', 'wait': 1500},
             {'t': '다음 날 아침, 두 본당은 저마다 자기가 이겼다고 말해요.', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '두 언덕에 교회가 하나씩!'},
           {'t': '철망을 둘러요.', 'act': 'shield'}, {'t': '다 같이 걸어요.', 'act': 'march'}, {'t': '교회 안에서는 예배!', 'act': 'service'},
           {'t': '쉬익! 로켓이 날아가!', 'act': 'lights', 'wait': 3400}, {'t': '땡, 땡! 자정의 종!', 'act': 'bells', 'wait': 1500},
           {'t': '다음 날 아침, 둘 다 “우리가 이겼어!”', 'act': 'day', 'wait': 1500}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '철망 안쪽'},
  {'type': 'img', 'ch': 2, 'img': 'card', 'fit': 'cover', 'p0': '70% 70%', 'p1': '58% 60%', 's0': 1.3, 's1': 1.12, 'cap': '철망 뒤의 사람들, 2015년',
   'lines': [{'t': '성당과 둘레의 집들은 철망을 둘러요.'}, {'t': '그 안쪽에서, 어떤 사람들은 늦은 밤 예배를 드려요.'}],
   'kid': [{'t': '철망이 로켓을 막아 줘.'}, {'t': '밖에서 로켓이 쉬익쉬익 날면, 교회 안에서는 어떤 소리가 들릴까?', 'ask': True}]},
  {'type': 'imagine', 'ch': 2,
   'lines': [{'t': '화약 냄새, 머리 위로 지나가는 불빛 줄.'}, {'t': '철망에 탁탁 부딪히는 소리, 골짜기를 채우는 연기.'}, {'t': '철망 안쪽에서는 부활의 노래가 이어져요.'}],
   'kid': [{'t': '눈을 감아 봐. 쉬익! 쉬익!'}, {'t': '탁탁, 철망에 부딪히는 소리.'}, {'t': '교회 안에서는 노래가 들려.'}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '대포에서 로켓으로'},
  {'type': 'img', 'ch': 3, 'img': 'scio', 'fit': 'cover', 'p0': '40% 55%', 'p1': '60% 45%', 's0': 1.15, 's1': 1.03, 'cap': '키오스섬 · 1882년 판화',
   'lines': [{'t': '처음에는 진짜 대포를 썼다고 전해져요.'}, {'t': '1889년 대포를 막자, 로켓으로 바뀌었대요.'}],
   'kid': [{'t': '옛날에는 진짜 대포를 쏘았대!'}, {'t': '대포를 못 쓰게 되자 로켓으로 바뀌었대.'}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '다음 날 아침'},
  {'type': 'quote', 'ch': 4, 'big': '이 전쟁에는 이긴 쪽도 진 쪽도 없어요.',
   'lines': [{'t': '사람들은 악수하고, 내년에 다시 만나자고 약속해요.', 'q': True, 'from': '키오스 시 관광 안내에서'},
             {'t': '다음 정교회 부활절 전날 밤은 2027년 5월 1일이에요.'}],
   'kid': [{'t': '둘 다 “우리가 이겼어!” 하고, 악수해.'}, {'t': '다음 부활절 밤은 2027년 5월 1일이야.'}]},
  {'type': 'reward', 'ch': 4},
 ],
}
