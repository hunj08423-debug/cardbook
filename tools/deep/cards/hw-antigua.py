# -*- coding: utf-8 -*-
"""깊은 카드: 안티구아 과테말라 성주간과 꽃 카펫(hw-antigua) · 중심 방식 = 만드는 차례
기준서 2판 · 틀 deep3-4 · 키트 3판 · 2026-11-18 만들기 시작
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 행렬이 지나갈 돌길 위, 밤늦게까지 깐 카펫 앞으로 행렬이 다가오는 순간
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 주민들이 집 앞 돌길에 카펫을 까는 일
     (과테말라 문화체육부가 알린 과정 열한 가지를 일곱 단계로 묶고, 행렬이 지나가는 여덟째 단계를 더함)
카드 크기: 큰 카드 — 1981년 성금요일 사진 셋(만드는 모습 · 손 · 꽃 카펫) · 2023년 꽃 카펫 사진 · 기관 글이 있어요.
끝맺는 꼴: 궁금해하기 — 행렬이 밟고 지나가면 흩어지는 카펫. 만드는 사람은 ‘봉헌물’이라 하고, 사라지는 것은 상관없다고도 해요.
5단계 마무리: 아이와 함께 끝까지 보기(2장에 고르기가 많아 쓰지 않아요).
그림 원본(src)은 deep_src/hw-antigua/ (저장소 밖). 받는 법: commons_get.py"""
import random
S = 'hw-antigua/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

MCD26 = 'https://emisorasunidas.com/nacional/2026/03/30/asi-es-el-proceso-para-la-elaboracion-de-las-alfombras'
AFP23 = 'https://emisorasunidas.com/2023/04/07/guatemala-celebra-con-devocion-semana-santa-patrimonio-mundial/'
SI23 = 'https://festival.si.edu/blog/ubaldo-sanchez-alfombras-de-aserrin'
SI17 = 'https://festival.si.edu/blog/alfombras-de-aserrin-guatemalan-sawdust-carpets'
ICH = 'https://ich.unesco.org/en/RL/holy-week-in-guatemala-01854'
KIDM = 'https://kid-museum.org/?p=36479'

# ── 이 안내서가 그린 카펫 깔기 차례(SVG · 위에서 내려다본 돌길) ─────────────────────
# 바탕: 과테말라 문화체육부가 알린 과정(에미소라스 우니다스 2026-03-30)과 스미스소니언 민속 축제의 글 두 편.
# 무늬(보라·노랑 칸, 꽃, 덩굴)는 이 안내서가 꾸민 것이에요. 연한 빨간 화살표는 방금 한 손놀림이에요.
R = random.Random(18)
def n1(v):
    s = f'{v:.1f}'
    return s[:-2] if s.endswith('.0') else s
X0, Y0, X1, Y1 = 64, 34, 236, 306          # 카펫 자리
CX = 150
PUR, YEL, GRN, RED, ORA = '#6e3a8a', '#e2b12a', '#3f8f3a', '#b8432b', '#e47724'
BASE = '#d6bb87'
def arrow(d):
    return (f'<path d="{d}" fill="none" stroke="#c0503f" stroke-width="2.2" stroke-linecap="round" opacity=".75" '
            f'marker-end="url(#acA)"/>')
def cobbles():
    pal = ['#a39a8c', '#998f81', '#ada393', '#938a7c', '#a7a090', '#9e9688']
    out = ['<rect width="300" height="340" fill="#7f776b"/>']
    y, row = -4, 0
    while y < 340:
        x = -10 + (11 if row % 2 else 0)
        while x < 300:
            out.append(f'<rect x="{n1(x + R.uniform(-1, 1))}" y="{n1(y + R.uniform(-.8, .8))}" width="{n1(19 + R.uniform(-2.5, 2.5))}" '
                       f'height="{n1(12 + R.uniform(-1.5, 1.5))}" rx="4" fill="{R.choice(pal)}"/>')
            x += 22
        y += 15; row += 1
    return ''.join(out)
def chalk():   # 1: 줄자와 분필 선
    t = ''.join(f'<line x1="{n1(X0 + i * 8.6)}" y1="20" x2="{n1(X0 + i * 8.6)}" y2="{24 if i % 5 else 26}" stroke="#5b4a1c" stroke-width=".7"/>' for i in range(21))
    tape = (f'<g data-s="1" data-off="2"><rect x="{X0}" y="18" width="{X1 - X0}" height="8" fill="#ecc94b" stroke="#a7852b" stroke-width=".8"/>{t}'
            f'<rect x="234" y="13" width="19" height="17" rx="4" fill="#c0392b" stroke="#7d241b"/><circle cx="243.5" cy="21.5" r="3.4" fill="#7d241b"/>'
            f'{arrow("M74 9 L222 9")}</g>')
    lines = (f'<g data-s="1" data-off="8" fill="none" stroke="#f6f1e4" stroke-linecap="round">'
             f'<rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{Y1 - Y0}" stroke-width="1.8" stroke-dasharray="6 4"/>'
             f'<line x1="{CX}" y1="{Y0}" x2="{CX}" y2="{Y1}" stroke-width="1.1" stroke-dasharray="3 4" opacity=".85"/>'
             f'<line x1="{X0}" y1="170" x2="{X1}" y2="170" stroke-width="1.1" stroke-dasharray="3 4" opacity=".85"/></g>')
    return lines + tape
def petals(cx, cy, d, r, col, mid, n=5):
    import math
    s = ''.join(f'<circle cx="{n1(cx + d * math.cos(2 * math.pi * k / n - math.pi / 2))}" cy="{n1(cy + d * math.sin(2 * math.pi * k / n - math.pi / 2))}" r="{r}" fill="{col}"/>' for k in range(n))
    return s + f'<circle cx="{n1(cx)}" cy="{n1(cy)}" r="{n1(r * .68)}" fill="{mid}"/>'
def stencils():   # 2: 무늬를 오려 낸 틀
    hole = '#7f776b'
    a = (f'<rect x="250" y="50" width="42" height="54" rx="2" fill="#c9a46e" stroke="#8d6a3c" stroke-width="1.2"/>'
         + petals(271, 77, 8, 5.2, hole, hole))
    b = (f'<rect x="250" y="116" width="42" height="54" rx="2" fill="#c9a46e" stroke="#8d6a3c" stroke-width="1.2"/>'
         f'<polygon points="271,129 284,143 271,157 258,143" fill="{hole}"/>'
         + ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="{hole}"/>' for x, y in ((257, 123), (285, 123), (257, 163), (285, 163))))
    c = (f'<rect x="257" y="182" width="28" height="76" rx="2" fill="#c9a46e" stroke="#8d6a3c" stroke-width="1.2"/>'
         + ''.join(f'<polygon points="271,{y - 6} 276,{y} 271,{y + 6} 266,{y}" fill="{hole}"/>' for y in (196, 212, 228, 244)))
    return (f'<g data-s="2" data-off="8">{a}{b}{c}</g>'
            f'<g data-s="2" data-off="3">{arrow("M298 40 Q300 60 292 70")}</g>')
def bowls():   # 3: 체로 치고 물들인 톱밥
    out = []
    for y, col in zip((70, 114, 158, 202, 246), (PUR, YEL, GRN, RED, ORA)):
        out.append(f'<circle cx="32" cy="{y}" r="15" fill="#e9dfc9" stroke="#8f826a" stroke-width="1.2"/><circle cx="32" cy="{y}" r="11.5" fill="{col}"/>')
        out.append(''.join(f'<circle cx="{n1(32 + R.uniform(-8, 8))}" cy="{n1(y + R.uniform(-8, 8))}" r=".9" fill="#fff" opacity=".35"/>' for _ in range(7)))
    import math
    mesh = ''.join(f'<line x1="{n1(32 + d)}" y1="{n1(292 - math.sqrt(144 - d * d))}" x2="{n1(32 + d)}" y2="{n1(292 + math.sqrt(144 - d * d))}" stroke="#8d7a5c" stroke-width=".8"/>'
                   f'<line x1="{n1(32 - math.sqrt(144 - d * d))}" y1="{292 + d}" x2="{n1(32 + math.sqrt(144 - d * d))}" y2="{292 + d}" stroke="#8d7a5c" stroke-width=".8"/>' for d in (-8, -4, 0, 4, 8))
    sieve = f'<circle cx="32" cy="292" r="12" fill="#d9c69c"/>{mesh}<circle cx="32" cy="292" r="13.5" fill="none" stroke="#9b7a48" stroke-width="3"/>'
    return (f'<g data-s="3" data-off="8">{"".join(out)}</g>'
            f'<g data-s="3" data-off="4">{sieve}{arrow("M50 286 Q62 272 50 258")}</g>')
def planks():   # 4: 나무판
    def pl(x, y, w, h):
        g = (f'<line x1="{x + 2}" y1="{y + h / 2}" x2="{x + w - 2}" y2="{y + h / 2}"' if w > h else
             f'<line x1="{x + w / 2}" y1="{y + 2}" x2="{x + w / 2}" y2="{y + h - 2}"')
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#9a6a3a" stroke="#6b4422" stroke-width=".8"/>{g} stroke="#b98a55" stroke-width=".7"/>'
    return (f'<g data-s="4" data-off="8">{pl(57, 27, 7, 286)}{pl(236, 27, 7, 286)}{pl(57, 27, 186, 7)}{pl(57, 306, 186, 7)}</g>'
            f'<g data-s="4" data-off="5">{arrow("M150 336 L150 320")}</g>')
def drops(k):
    return ''.join(f'<circle cx="{n1(R.uniform(X0 + 6, X1 - 6))}" cy="{n1(R.uniform(Y0 + 6, Y1 - 6))}" r="1.7" fill="#5d9bd5" opacity=".8"/>' for _ in range(k))
def sprayer():
    return ('<rect x="254" y="282" width="17" height="25" rx="3.5" fill="#4f86c6" stroke="#2f5f96"/>'
            '<rect x="258" y="274" width="9" height="9" fill="#3b6aa3"/><rect x="247" y="272" width="14" height="4.5" rx="1.5" fill="#3b6aa3"/>'
            '<path d="M258 279 Q252 284 255 290" fill="none" stroke="#2f5f96" stroke-width="2"/>'
            '<path d="M244 270 q-4 3 0 7 M240 268 q-5 5 0 11" fill="none" stroke="#5d9bd5" stroke-width="1.3" stroke-linecap="round"/>')
def base():   # 5: 고른 바탕 + 물 뿌리기
    tex = ''.join(f'<circle cx="{n1(R.uniform(X0 + 1, X1 - 1))}" cy="{n1(R.uniform(Y0 + 1, Y1 - 1))}" r="{n1(R.uniform(.7, 1.2))}" fill="{R.choice(("#c2a26c", "#e6cfa0"))}"/>' for _ in range(150))
    return (f'<g data-s="5" data-off="8"><rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{Y1 - Y0}" fill="{BASE}"/>{tex}</g>'
            f'<g data-s="5" data-off="6">{drops(26)}{sprayer()}</g>')
def spiral(cx, cy, s=1.6):
    d = f'M{n1(cx)} {n1(cy)}'
    for i, dx in enumerate((2, -4, 6, -8, 10), 1):
        d += f' a{n1(i * s)} {n1(i * s)} 0 0 1 {n1(dx * s)} 0'
    return f'<path d="{d}" fill="none" stroke="{GRN}" stroke-width="2.6" stroke-linecap="round"/>'
def design():   # 6: 틀 대고 색 톱밥 채우기
    band = f'<rect x="68" y="38" width="164" height="264" fill="{RED}"/>'
    dia = ''
    for y in range(58, 290, 16):
        for x in (74, 226):
            dia += f'<polygon points="{x},{y - 3.4} {x + 3.4},{y} {x},{y + 3.4} {x - 3.4},{y}" fill="#efc541"/>'
    for x in range(88, 220, 16):
        for y in (44, 296):
            dia += f'<polygon points="{x},{y - 3.4} {x + 3.4},{y} {x},{y + 3.4} {x - 3.4},{y}" fill="#efc541"/>'
    panels = (f'<rect x="80" y="50" width="140" height="76" fill="{PUR}"/><rect x="80" y="130" width="140" height="80" fill="{YEL}"/>'
              f'<rect x="80" y="214" width="140" height="76" fill="{PUR}"/>'
              f'<rect x="80" y="126" width="140" height="4" fill="#f3e7cf"/><rect x="80" y="210" width="140" height="4" fill="#f3e7cf"/>')
    fl = ''.join(petals(x, y, 7, 5.5, '#e9c03a', '#d0502a') for y in (88, 252) for x in (104, 150, 196))
    sw = ''.join(spiral(x, 168) for x in (100, 146, 192))
    sw += ''.join(f'<ellipse cx="{x}" cy="{y}" rx="4.5" ry="2.2" fill="{GRN}" transform="rotate({a} {x} {y})"/>'
                  for x, y, a in ((122, 150, -30), (168, 150, -30), (122, 190, 30), (168, 190, 30)))
    sw += ''.join(petals(x, y, 3.6, 2.6, '#c0392b', '#f3d36b') for x, y in ((92, 140), (208, 140), (92, 200), (208, 200)))
    lifted = (f'<g data-s="6" data-off="7"><rect x="96" y="232" width="116" height="44" rx="2" fill="#5a4a35" opacity=".22"/>'
              f'<rect x="90" y="224" width="116" height="44" rx="2" fill="#c9a46e" opacity=".55" stroke="#8d6a3c" stroke-width="1.2"/>'
              + ''.join(f'<circle cx="{x - 4}" cy="244" r="12" fill="none" stroke="#6b4f2a" stroke-width="1" stroke-dasharray="2 2"/>' for x in (104, 150, 196))
              + arrow('M150 222 L150 202') + '</g>')
    return f'<g data-s="6" data-off="8">{band}{dia}{panels}{fl}{sw}</g>' + lifted
def flowers():   # 7: 꽃·솔잎·과일 + 다시 물
    import math
    nd = []
    per = [(x, Y0, 0, -1) for x in range(X0, X1 + 1, 6)] + [(x, Y1, 0, 1) for x in range(X0, X1 + 1, 6)] \
        + [(X0, y, -1, 0) for y in range(Y0 + 6, Y1, 6)] + [(X1, y, 1, 0) for y in range(Y0 + 6, Y1, 6)]
    for x, y, ox, oy in per:
        a = math.atan2(oy, ox) + R.uniform(-.7, .7); L = R.uniform(5, 8)
        nd.append(f'<line x1="{n1(x - math.cos(a) * 2)}" y1="{n1(y - math.sin(a) * 2)}" x2="{n1(x + math.cos(a) * L)}" y2="{n1(y + math.sin(a) * L)}" '
                  f'stroke="{R.choice(("#4f7f35", "#5f9140", "#3f6c2a"))}" stroke-width="1.2" stroke-linecap="round"/>')
    fl = ''.join(petals(x, y, 5, 4, '#f7f2e6', '#e9b52a') for x, y in ((74, 44), (226, 44), (74, 296), (226, 296), (74, 170), (226, 170), (150, 44), (150, 296)))
    fl += ''.join(petals(x, y, 3.4, 2.6, '#e86a9a', '#fff3c4') for x, y in ((104, 128), (150, 128), (196, 128), (104, 212), (150, 212), (196, 212)))
    fr = ''.join(f'<circle cx="{x}" cy="{y}" r="5.5" fill="#f08a24" stroke="#b5621a" stroke-width=".9"/>'
                 f'<ellipse cx="{x + 3}" cy="{y - 5.5}" rx="3" ry="1.5" fill="#3f7f2a" transform="rotate(-30 {x + 3} {y - 5.5})"/>'
                 for x, y in ((126, 168), (174, 168), (150, 146), (150, 192)))
    fr += petals(150, 168, 6, 4.6, '#f7f2e6', '#c0392b', 6)
    return (f'<g data-s="7" data-off="8">{"".join(nd)}{fl}{fr}</g>'
            f'<g data-s="7" data-off="8">{drops(22)}{sprayer()}</g>')
def trampled():   # 8: 행렬이 지나간 뒤
    import math
    pts = []
    for x in range(X0, X1 + 1, 12): pts.append((x + R.uniform(-3, 3), Y0 + R.uniform(-3, 4)))
    for y in range(Y0, Y1 + 1, 12): pts.append((X1 + R.uniform(-4, 3), y + R.uniform(-3, 3)))
    for x in range(X1, X0 - 1, -12): pts.append((x + R.uniform(-3, 3), Y1 + R.uniform(-4, 3)))
    for y in range(Y1, Y0 - 1, -12): pts.append((X0 + R.uniform(-3, 4), y + R.uniform(-3, 3)))
    smear = f'<polygon points="{" ".join(f"{n1(x)},{n1(y)}" for x, y in pts)}" fill="#b49c76" opacity=".95"/>'
    blot = ''
    for _ in range(34):
        x = R.uniform(X0 + 6, X1 - 6); y = R.uniform(Y0 + 6, Y1 - 6)
        blot += (f'<ellipse cx="{n1(x)}" cy="{n1(y)}" rx="{n1(R.uniform(5, 15))}" ry="{n1(R.uniform(2.5, 7))}" fill="{R.choice((PUR, YEL, GRN, RED, ORA))}" '
                 f'opacity="{n1(R.uniform(.25, .5))}" transform="rotate({int(R.uniform(-40, 40))} {n1(x)} {n1(y)})"/>')
    for y in range(52, 296, 22):   # 가장자리에 남은 띠 조각
        for x in (70, 224):
            if R.random() < .6:
                blot += f'<rect x="{n1(x + R.uniform(-2, 2))}" y="{y}" width="{n1(R.uniform(5, 8))}" height="{n1(R.uniform(6, 14))}" fill="{RED}" opacity=".6"/>'
    feet = ''
    for lane, x0 in enumerate((104, 128, 172, 196)):
        for i, y in enumerate(range(292 - lane * 6, 44, -26)):
            x = x0 + (4 if i % 2 else -4)
            feet += (f'<ellipse cx="{x}" cy="{y}" rx="4.2" ry="7.2" fill="#5e4b34" opacity=".5"/>'
                     f'<ellipse cx="{x}" cy="{y + 11}" rx="3.4" ry="3.2" fill="#5e4b34" opacity=".45"/>')
    pet = ''.join(f'<circle cx="{n1(R.uniform(X0 + 8, X1 - 8))}" cy="{n1(R.uniform(Y0 + 8, Y1 - 8))}" r="{n1(R.uniform(1.6, 2.6))}" fill="{R.choice(("#f7f2e6", "#e86a9a", "#efc541"))}"/>' for _ in range(16))
    way = arrow('M30 300 L30 70') + arrow('M270 300 L270 70')
    broom = ('<line x1="58" y1="262" x2="40" y2="314" stroke="#8a6a3f" stroke-width="3.2" stroke-linecap="round"/>'
             '<polygon points="30,312 48,316 50,334 22,330" fill="#c9a24f" stroke="#9a7a33"/>'
             '<path d="M58 326 q8 -6 16 0 M62 333 q8 -6 16 0" fill="none" stroke="#e8dcc0" stroke-width="1.4" stroke-linecap="round" opacity=".9"/>'
             '<ellipse cx="88" cy="330" rx="12" ry="4" fill="#b49c76"/>')
    return f'<g data-s="8">{smear}{blot}{feet}{pet}{broom}<g opacity=".55">{way}</g></g>'
def carpet_svg():
    return ('<svg viewBox="0 0 300 340" xmlns="http://www.w3.org/2000/svg">'
            '<defs><marker id="acA" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            '<path d="M0 0 L10 5 L0 10 z" fill="#c0503f" opacity=".85"/></marker></defs>'
            + cobbles() + chalk() + stencils() + bowls() + planks() + base() + design() + flowers() + trampled() + '</svg>')

CARD = {
 'id': 'hw-antigua', 'mode': '만드는 차례',
 'pagetitle': '안티구아 과테말라 성주간과 꽃 카펫',
 'brandsub': '깊은 카드 · 만드는 차례',
 'where': '<b>해마다 사순절과 성주간</b><span>과테말라 안티구아 · 행렬이 지나가는 돌길</span>',
 'lead': '과테말라 안티구아에서는 사순절과 성주간이면, 행렬이 지나갈 돌길 위에 가족과 이웃이 꽃과 물들인 톱밥으로 카펫을 깔아요. 공들여 깐 카펫은 행렬이 그 위를 지나가면 흩어져요. 카펫 한 장을 여덟 단계로 깔아 보세요.',
 'leadKid': '톱밥이랑 꽃으로 길바닥에 카펫을 깐대! 한 단계씩 같이 깔아 보자.',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분 · 여덟 단계로 깔아요',
 'draft': '검수 전 시안이에요(기준서 2판). 장면에는 과테말라 문화체육부와 스미스소니언 민속 축제, 유네스코, 신문 기사에 있는 것만 옮겼어요. 카펫 깔기 그림은 이 안내서가 그렸고, 그림 속 무늬는 이 안내서가 꾸민 것이에요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#9C4A1F;--accent-ink:#fffaf4;--soft:rgba(156,74,31,.09);--stamp:#6b3d8f}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#f0a56e;--accent-ink:#17100a;--soft:rgba(240,165,110,.10);--stamp:#c9a0e8}}
:root[data-theme="dark"]{--accent:#f0a56e;--accent-ink:#17100a;--soft:rgba(240,165,110,.10);--stamp:#c9a0e8}""",
 'stamp': {'t': '꽃 카펫', 'y': '성주간', 'sub': '과테말라 안티구아'},
 'doneNote': '돌길 위에 카펫을 여덟 단계로 깔고, 행렬이 지나가는 것까지 봤어요.',
 'images': {
  'making': {'src': S + 'Antigua_Guatemala_Alfombras_Viernes_Santo_1981_01.jpg', 'crop': [0, .25, 1, 1],
             'cap': '안티구아 6번가에서 만드는 카펫 · 1981년 성금요일',
             'cr': '사진: Infrogmation · CC BY-SA 4.0 · 위키미디어 공용',
             'u': 'https://commons.wikimedia.org/wiki/File:Antigua_Guatemala_Alfombras_Viernes_Santo_1981_01.jpg',
             'alt': '돌길 위에 긴 카펫이 비스듬히 뻗어 있다. 붉은 벽돌 무늬 테두리 안에 자주색 칸과 주황색 칸이 있고, 주황색 칸에는 검푸른 계단 모양 신전이, 그 아래 검은 칸에는 흰 무늬를 새긴 돌기둥 모양이 있다. 회색 둘레에는 흰 무늬가 줄지어 있고, 가장자리에는 긴 나무판이 놓였다. 오른쪽 위에는 무릎을 꿇은 두 사람이 붉은 그릇을 들고 일하고, 오른쪽 아래 구석에는 무늬를 오려 낸 흰 판이 놓여 있다.'},
  'hands': {'src': S + 'Antigua_Guatemala_Alfombras_Viernes_Santo_1981_11.jpg', 'crop': [.28, .55, .88, 1],
            'cap': '물들인 톱밥과 손 · 1981년 성금요일',
            'cr': '사진: Infrogmation · CC BY-SA 4.0 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Antigua_Guatemala_Alfombras_Viernes_Santo_1981_11.jpg',
            'alt': '돌길 위 카펫 가장자리에서 두 사람의 손이 붉은 칸 위에 닿아 있다. 곁에는 자줏빛 톱밥과 노란 톱밥을 담은 그릇이 놓였다. 앞쪽에는 보라 바탕에 노란 꽃무늬, 노란 바탕에 초록 덩굴무늬가 깔려 있고, 오른쪽 둘레는 초록이다.'},
  'christ': {'src': S + 'Antigua_Guatemala_Alfombras_Viernes_Santo_1981_04.jpg',
             'cap': '꽃잎으로 만든 카펫 · 1981년 성금요일',
             'cr': '사진: Infrogmation · CC BY-SA 4.0 · 위키미디어 공용',
             'u': 'https://commons.wikimedia.org/wiki/File:Antigua_Guatemala_Alfombras_Viernes_Santo_1981_04.jpg',
             'alt': '돌길 위의 네모난 꽃 카펫. 보랏빛 꽃잎을 마름모꼴로 깐 가운데에, 팔을 벌린 예수의 모습이 주황빛으로 놓였다. 둘레에는 흰 꽃으로 굽이치는 무늬를 둘렀고, 가장자리로 마른 솔잎이 삐져나와 있다.'},
  'path': {'src': S + 'Divine_Path_-_Antigua_s_Semana_Santa_Alfombra.jpg', 'crop': [0, .40, 1, 1], 'max': 1600,
           'cap': '행렬을 기다리는 꽃 카펫 · 2023년 4월 6일(성목요일)',
           'cr': '사진: Aandhu · CC BY 4.0 · 위키미디어 공용',
           'u': 'https://commons.wikimedia.org/wiki/File:Divine_Path_-_Antigua%27s_Semana_Santa_Alfombra.jpg',
           'alt': '돌길 위에 가늘고 긴 초록 잎을 깐 카펫. 노랑과 빨강 꽃으로 놓은 십자가와 둥근 무늬가 있고, 앞쪽에는 붉은 글라디올러스와 노란 꽃, 흰 장미에 둘러싸인 해바라기가 있다. 가장자리는 보랏빛 꽃으로 둘렀다. 왼쪽 위에 서 있는 두 사람의 다리가 보인다.'},
 },
 'scenes': [
  {'id': 'street', 'label': '행렬이 지나갈 길 위에', 'kind': 'photo', 'img': 'making',
   'text': ['과테말라 안티구아에서는 사순절(부활절을 앞둔 40일)과 성주간(부활절 바로 앞 한 주) 동안 행렬이 거리를 지나가요. 그 길을 따라, 가족과 이웃이 집 앞 돌길에 꽃과 톱밥으로 카펫을 깔아요. 이 카펫을 스페인어로 ‘알폼브라’라고 해요.',
            '사진은 1981년 성금요일, 안티구아 6번가예요. 카펫 가운데에 계단 모양 신전과, 옛 마야 글자를 닮은 무늬를 새긴 돌기둥이 있어요. 오른쪽 아래 구석에는 무늬를 오려 낸 틀이 놓여 있는데, 둘레의 흰 무늬가 그 틀과 같은 모양이에요.'],
   'quote': {'t': '우리는 우리를 과테말라 사람이게 해 주는 이 전통을 잃고 싶지 않아요.',
             'from': '2023년 성주간, 안티구아 거리에서 카펫을 마무리하던 한 식당 요리사가 AFP 기자에게 한 말(에미소라스 우니다스 2023년 4월 7일) · 이 안내서가 옮김', 'u': AFP23},
   'text2': ['스미스소니언 민속 축제의 글은 안티구아를 이 전통의 한가운데로 꼽아요. 길이가 45미터(150피트)나 되는 카펫이 성당에서부터 거리를 따라 이어지고, 만드는 사람들은 행렬 전날 밤늦게까지 일하기도 해요.'],
   'kid': '집 앞 돌길에 톱밥이랑 꽃으로 커다란 카펫을 깔아!',
   'kidq': '사진 오른쪽 아래, 무늬를 오려 낸 틀을 찾아볼래?'},
  {'id': 'lay', 'label': '카펫 한 장, 여덟 단계', 'kind': 'mod', 'mod': 'steps', 'night': False,
   'text': ['과테말라 문화체육부가 알린 카펫 만드는 과정을 여덟 단계로 묶어 그렸어요. 길이를 재어 선을 긋고, 틀과 물들인 톱밥을 준비한 뒤, 바탕을 깔고 무늬와 꽃을 올려요.',
            '단추를 누를 때마다 돌길 위에 한 가지씩 놓여요. 마지막 단추를 누르면, 행렬이 지나간 뒤의 길이 보여요.'],
   'kid': '돌길 위에 카펫을 깔아 보자. 단추를 하나씩 눌러 봐!',
   'kidq': '톱밥에 물을 자꾸 뿌리는 건 왜일까?'},
  {'id': 'hands', 'label': '손끝에서 떨어지는 색', 'kind': 'photo', 'img': 'hands',
   'text': ['무늬는 손으로 놓아요. 물들인 톱밥을 놓고 나무판으로 눌러 판판하게 하고, 모래는 꽉 쥔 주먹 사이로 흘리거나 틀 위로 뿌린 뒤 솔로 펴요. 솔잎과 채소도 손으로 하나하나 놓아요.',
            '물감이 물에 녹는 것이라, 빛깔이 선명하려면 카펫이 젖어 있어야 해요. 그래서 만드는 사람들은 손을 자주 적시고 무늬 위에 물을 뿌려요.'],
   'text2': ['사진은 1981년 성금요일에 찍은 손이에요. 자줏빛 톱밥과 노란 톱밥을 담은 그릇 곁에서, 두 사람이 붉은 칸 위에 손끝을 대고 있어요. 앞쪽에는 보라 바탕의 노란 꽃과, 노란 바탕의 초록 덩굴무늬가 다 깔려 있어요.'],
   'kid': '톱밥을 손으로 살살 뿌려서 그림을 그려.',
   'kidq': '그릇에 담긴 톱밥은 무슨 색이야?'},
  {'id': 'flowers', 'label': '톱밥 대신 꽃으로', 'kind': 'photo', 'img': 'christ',
   'text': ['톱밥만 쓰는 것은 아니에요. 꽃과 솔잎, 과일과 채소도 카펫이 돼요. 2023년 AFP 기사는 과테말라의 카펫을 꽃이나, 코로소로 향을 낸 톱밥으로 만든다고 전해요. 코로소는 향기가 나는 야자 열매예요.',
            '이 카펫도 1981년 성금요일에 찍었어요. 보랏빛 꽃잎 위에 십자가에 달린 예수의 모습을 주황빛으로 놓고, 둘레를 흰 꽃무늬로 둘렀어요. 가장자리에는 솔잎이 삐죽삐죽 나와 있어요.'],
   'kid': '이건 꽃잎으로 만든 카펫이야!',
   'kidq': '보라색 꽃잎 위에 누가 있을까?'},
  {'id': 'pass', 'label': '행렬이 지나가면', 'kind': 'photo', 'img': 'path',
   'text': ['행렬이 오면, 보라색 옷을 입은 사람들이 예수의 조각상을 얹은 가마를 어깨에 메고 음악에 맞춰 천천히 카펫 위로 걸어가요. 공들여 깐 무늬는 그 발걸음 아래에서 흩어져요.',
            '행렬이 끝나면, 청소하는 사람들이 금세 거리를 쓸어요.'],
   'text2': ['사진은 2023년 성목요일 오후, 행렬을 기다리는 꽃 카펫이에요. 가늘고 긴 초록 잎을 깐 바탕에 꽃으로 십자가와 둥근 무늬를 놓고, 앞쪽에는 흰 장미에 둘러싸인 해바라기를 놓았어요.'],
   'kid': '행렬이 카펫 위로 지나가면, 그림이 흩어져.',
   'kidq': '이 카펫에서 해바라기를 찾아볼래?'},
 ],
 'imagine': {'t': '돌길 위로 물 뿌리는 소리가 칙칙 나요. 젖은 톱밥에서 나무 냄새가, 솔잎에서 풋풋한 냄새가 올라와요. 멀리서 느린 행진곡과 함께 향 연기가 골목으로 밀려와요.',
             'kid': '눈을 감아 봐. 칙칙, 물 뿌리는 소리가 나. 솔잎 냄새도 나.'},
 'lines': ['공들여 깐 무늬가, 발걸음 아래에서 흩어져요.', '틀을 들어 올리면, 그림이 드러나요.', '젖어 있어야 빛나는 카펫이에요.'],
 'linesKid': ['톱밥으로 길에 그림을 그렸어!', '꽃이랑 과일도 올렸어.'],
 'close': {'form': '궁금해하기',
           'from': '행렬이 지나가며 흩어지는 카펫(AFP 2023 · 스미스소니언 2023). 과테말라시티에서 카펫을 깐 한 사람은 ‘봉헌물’이라 부르고(AFP 2023), 과테말라 출신 작가 우발도 산체스는 곧 사라진다는 것은 카펫이 하는 일에 상관없다고 말해요(스미스소니언 2023). 스미스소니언 2017년 글은 ‘그 순간을 즐기는 예술’이라 불러요. 만드는 차례 8단계(발자국만 남은 길)와 마지막 장면(행렬을 기다리는 카펫)에서 물음으로 열어 둬요.',
           'ask': '밟히는 순간, 카펫은 망가진 걸까요, 다 이루어진 걸까요?',
           'askKid': '행렬이 밟고 지나간 카펫, 망가진 걸까, 다 된 걸까?'},
 'goals': {
  's4': {'t': '여덟 단계 끝까지', 'p': '카펫을 여덟 단계 끝까지 깔아 보면 카드에 금박이 입혀져요.',
         'how': '‘카펫 한 장, 여덟 단계’ 장면에서 첫 단계부터 끝까지 눌러 보세요', 'done': '카펫을 끝까지 깔고 행렬까지 맞았어요',
         'ways': [{'id': 'steps', 't': '여덟 단계를 끝까지 해 보기'}]},
  's5': {'t': '아이와 함께', 'p': '아이와 함께 ‘영화처럼 보기’를 끝까지 보면 카드가 채색돼요.',
         'how': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'done': '아이와 함께 꽃 카펫 이야기를 끝까지 봤어요',
         'ways': [{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'steps': {
   'svg': carpet_svg(),
   'alt': '이 안내서가 그린, 위에서 내려다본 돌길. 단계마다 분필 선, 무늬를 오려 낸 틀, 물들인 톱밥 그릇, 나무판, 고른 바탕, 무늬, 꽃과 과일이 하나씩 놓이고, 마지막에는 발자국 사이로 흩어진 톱밥만 남는다.',
   'cap': '이 안내서가 그린 카펫 깔기 차례 · 바탕: 과테말라 문화체육부가 알린 과정(에미소라스 우니다스 2026년 3월 30일)과 스미스소니언 민속 축제의 글 · 그림 속 무늬는 이 안내서가 꾸민 것이에요',
   'intro': '단추를 누를 때마다 돌길 위에 한 가지씩 놓여요. 빨간 화살표는 방금 한 손놀림이에요.',
   'hint': '아래 ‘줄자로 재고 선 긋기’부터 눌러 보세요.',
   'marksLabel': '카펫에 들인 손길',
   'marks': [{'t': '길잡이 선', 'c': '#f6f1e4', 's': 1}, {'t': '물든 톱밥', 'c': PUR, 's': 3}, {'t': '고른 바탕', 'c': BASE, 's': 5},
             {'t': '무늬', 'c': RED, 's': 6}, {'t': '꽃과 과일', 'c': '#f08a24', 's': 7}],
   'steps': [
     {'do': '줄자로 재고 선 긋기', 't': '길잡이 선', 'p': '줄자로 길이를 재어 카펫이 한가운데 오게 하고, 분필이나 석고 가루로 땅에 길잡이 선을 그어요.'},
     {'do': '무늬 틀 오리기', 't': '틀 준비', 'p': '무늬를 손으로 오려 낸 틀을 준비해요. 모양 자를 대고 그리듯, 틀의 뚫린 자리에만 색 톱밥이 앉아요.'},
     {'do': '톱밥 체 치고 물들이기', 't': '물든 톱밥', 'p': '톱밥을 체로 쳐서 티끌을 골라내고, 물감과 뜨거운 물로 여러 색을 들여요. 소금을 넣으면 물든 색이 잘 빠지지 않아요.'},
     {'do': '나무판 두르기', 't': '나무판', 'p': '카펫 자리 둘레에 긴 나무판을 대고 분필로 표시해요. 무늬를 까는 동안 카펫의 모양을 지켜 줘요.'},
     {'do': '바탕 깔고 물 뿌리기', 't': '고른 바탕', 'p': '톱밥을 고르게 깔아 판판하게 하고, 물을 살짝 뿌려요. 젖은 모래가 단단히 뭉치듯 톱밥이 다져져요.'},
     {'do': '틀 대고 색 톱밥 채우기', 't': '무늬', 'p': '바탕 위에 틀을 놓고, 뚫린 자리를 다른 색 톱밥으로 채워요. 틀을 똑바로 들어 올리면 그림이 드러나요. 색이 섞이지 않게 둘레를 늘 깨끗이 해요.'},
     {'do': '꽃과 과일 올리기', 't': '꽃 · 솔잎 · 과일', 'p': '꽃과 솔잎, 과일을 손으로 올려요. 무늬가 흐트러지지 않고 빛깔이 살아 있게, 끝까지 물을 뿌려요.'},
     {'do': '행렬 맞이하기', 't': '행렬이 지나간 뒤', 'p': '가마를 멘 행렬이 카펫 위를 천천히 지나가요. 무늬는 발걸음에 흩어지고, 행렬이 끝나면 청소하는 사람들이 금세 거리를 쓸어요.'},
   ],
   'done': '여덟 단계를 끝까지 해 봤어요. 공들여 깐 카펫이, 행렬이 지나가는 사이에 흩어졌어요.',
 }},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>두 뿌리</b> 스미스소니언 민속 축제의 글은 이 카펫이 마야와 스페인 두 문화에 뿌리를 두었다고 소개해요. 스페인에서는 성체 성혈 대축일(코르푸스 크리스티) 행렬 길을 이렇게 꾸몄고, 마야 사람들은 귀한 이가 지나갈 길에 꽃과 풀, 초를 놓았대요.',
    '<b>가마를 메는 사람들</b> 스미스소니언의 2017년 글에 따르면, 보라색 뾰족 두건과 망토를 쓴 남자들과 검은 옷의 여자들이 17세기에 만든 예수와 마리아 조각상을 메고 가요. 조각상을 얹는 삼나무 가마는 무게가 3톤에 이르러요.',
    '<b>유네스코</b> 2022년, ‘과테말라의 성주간’이 유네스코 인류무형문화유산 대표 목록에 올랐어요. 행렬과 밤샘 기도, 장례 행진곡, 그 철의 음식, 그리고 카펫과 제단을 꾸미는 일이 함께 올랐어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>무엇으로 물들이나</b> 과테말라 문화체육부는 가게에서 산 물감이나 자연에서 얻은 물감을 뜨거운 물, 소금과 함께 쓴다고 해요. 스미스소니언의 2017년 글은 과테말라에서 나는 아닐린(화학 물감)을, 2023년 글은 산에서 나는 흰 분필과 관목에서 얻는 노랑·주황 물감 아치오테를 들어요.',
    '<b>사라지는 것을 두고</b> 스미스소니언의 2017년 글은 이 카펫을 ‘그 순간을 즐기도록 만든, 잠깐 있다 사라지는 예술’이라고 불러요. 그런데 과테말라 출신 작가 우발도 산체스는, 곧 사라진다는 것은 카펫이 하는 일에 상관없다고 말해요. 그 위를 걸을 때 생기는 마음이 하느님께 드리는 선물이 된대요. 2023년 과테말라시티에서 가족과 카펫을 깐 한 사람은, 어릴 때부터 깔아 온 카펫을 ‘봉헌물’이라고 불렀어요.']},
  {'h': '직접 해 보기', 'p': [
    '두꺼운 종이를 오려 틀을 만들고, 쟁반에 깐 바탕 위에 놓은 뒤 뚫린 자리를 색 모래나 꽃잎으로 채워 보세요. 틀을 똑바로 들어 올리면 무늬가 드러나요(미국 KID 박물관의 만들기 안내를 따랐어요). 안티구아의 카펫은 사순절과 성주간의 행렬 날에 거리에서 볼 수 있어요.'],
   'links': [{'t': '유네스코: ‘과테말라의 성주간’ 소개와 영상', 'u': ICH, 'm': '영어'},
             {'t': '스미스소니언 민속 축제: 과테말라 출신 작가 우발도 산체스의 톱밥 카펫', 'u': SI23, 'm': '영어'},
             {'t': '에미소라스 우니다스: 카펫을 만드는 과정(과테말라 문화체육부 설명)', 'u': MCD26, 'm': '스페인어'}]},
 ],
 'src': [
  {'l': '에미소라스 우니다스(2026년 3월 30일, 과테말라 문화체육부 자료): 카펫 만드는 과정 — 줄자로 재기, 분필·석고 선, 틀 준비, 톱밥 체 치기, 물감·뜨거운 물·소금으로 물들이기, 나무판, 고른 바탕, 물 뿌려 다지기, 깨끗이 하기, 틀·꽃·과일, 계속 물 뿌리기 · 가족과 이웃', 'u': MCD26},
  {'l': '스미스소니언 민속 축제(2023년 8월 11일): 우발도 산체스의 톱밥 카펫 — 제재소 톱밥, 흰 분필·아치오테, 나무판으로 누르기, 주먹 사이·틀 위로 모래 뿌리기, 솔잎·채소, 물에 녹는 물감이라 늘 적심, 마야·스페인(성체 성혈 대축일) 뿌리, 행렬 뒤 청소, 안티구아 최대 150피트, 전날 밤늦게까지, 사라지는 것에 대한 산체스의 생각, 2022년 유네스코', 'u': SI23},
  {'l': '스미스소니언 민속 축제(2017년 7월 9일, 욜란다 알코르타): 과테말라의 톱밥 카펫 — 사순절·성주간 행렬, 보라 두건·검은 옷, 17세기 조각상, 3톤 삼나무 가마, 가족과 이웃이 집 앞 거리에, 아닐린 물감, 손으로 오린 틀, 틀을 들어 올리면 그림이 드러남, 400년 된 전통, 순간의 예술', 'u': SI17},
  {'l': 'AFP(에미소라스 우니다스 2023년 4월 7일): 과테말라 성주간 — 보라 옷과 두건, 어깨에 멘 조각상, 음악에 맞춰 천천히 카펫 위로, 꽃이나 코로소(향기 나는 야자 열매)로 향을 낸 톱밥, 안티구아 식당 요리사의 말, 과테말라시티의 ‘봉헌물’, 행렬이 지나며 부서짐, 2022년 11월 30일 유네스코 등재', 'u': AFP23},
  {'l': '유네스코 인류무형문화유산: 과테말라의 성주간(2022년, 17차 위원회) — 행렬, 밤샘 기도, 장례 행진곡, 철 음식, 카펫·제단 꾸미기', 'u': ICH},
  {'l': 'KID 박물관(미국 메릴랜드) 「Making for the Moment」 — 두꺼운 종이로 틀 오리기, 채우고 똑바로 들어 올리기', 'u': KIDM},
  {'l': '위키미디어 공용: 1981년 성금요일(4월 17일) 안티구아의 톱밥·꽃·솔잎 카펫 사진들(Infrogmation, 6번가) · 2023년 성목요일의 꽃 카펫(Aandhu)', 'u': 'https://commons.wikimedia.org/wiki/Category:Holy_Week_in_Antigua_Guatemala,_1981'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 40%', 'p1': '55% 55%', 's0': 1.25, 's1': 1.05,
   'kicker': '해마다 사순절과 성주간 · 과테말라 안티구아', 'title': '안티구아 과테말라 성주간과 꽃 카펫',
   'lines': [{'t': '행렬이 지나갈 돌길 위에, 사람들은 카펫을 깔아요.'}, {'t': '꽃과 물들인 톱밥으로 만든 카펫이에요.'}],
   'kid': [{'t': '행렬이 지나갈 길에 카펫을 깔아!'}, {'t': '꽃이랑 톱밥으로 만든대.'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '행렬이 지나갈 길 위에'},
  {'type': 'img', 'ch': 1, 'img': 'making', 'fit': 'cover', 'p0': '50% 20%', 'p1': '75% 85%', 's0': 1.3, 's1': 1.3, 'cap': '안티구아 6번가 · 1981년 성금요일',
   'lines': [{'t': '1981년 성금요일, 안티구아 6번가예요.'}, {'t': '가족과 이웃이 집 앞 돌길에 카펫을 깔아요.'}, {'t': '구석에는 무늬를 오려 낸 틀이 놓여 있어요.'}],
   'kid': [{'t': '길바닥에 커다란 그림이 있어!'}, {'t': '무늬를 오려 낸 틀을 찾아볼래?', 'ask': True}]},
  {'type': 'quote', 'ch': 1, 'big': '이 전통을 잃고 싶지 않아요.',
   'lines': [{'t': '2023년, 안티구아에서 카펫을 마무리하던 한 요리사의 말이에요.'}, {'t': '우리를 과테말라 사람이게 해 주는 전통이래요.'}],
   'kid': [{'t': '이 전통을 잃고 싶지 않대.'}, {'t': '너는 지키고 싶은 전통이 있어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '카펫 한 장, 여덟 단계'},
  {'type': 'mod', 'mod': 'steps', 'ch': 2,
   'lines': [{'t': '줄자로 재고, 분필로 길잡이 선을 그어요.', 'act': 'step:1'},
             {'t': '틀을 오리고, 톱밥을 체로 쳐서 물들여요.', 'act': 'step:3'},
             {'t': '나무판을 두르고, 바탕을 깔아 물을 뿌려요.', 'act': 'step:5'},
             {'t': '틀을 대고 채운 뒤 들어 올리면, 무늬가 드러나요.', 'act': 'step:6'},
             {'t': '꽃과 솔잎, 과일을 올리고 또 물을 뿌려요.', 'act': 'step:7', 'wait': 1800},
             {'t': '그리고 행렬이 그 위를 천천히 지나가요.', 'act': 'step:8', 'wait': 2600}],
   'kid': [{'t': '선을 긋고, 톱밥에 물을 들여!', 'act': 'step:3'},
           {'t': '바탕을 깔고, 틀로 무늬를 찍어.', 'act': 'step:6'},
           {'t': '꽃이랑 과일까지 올리면 다 됐어!', 'act': 'step:7', 'wait': 1400},
           {'t': '톱밥에 물을 자꾸 뿌리는 건 왜일까?', 'ask': True},
           {'t': '행렬이 지나가면, 흩어져.', 'act': 'step:8', 'wait': 1600}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '손끝에서 떨어지는 색'},
  {'type': 'img', 'ch': 3, 'img': 'hands', 'fit': 'cover', 'p0': '35% 30%', 'p1': '60% 60%', 's0': 1.35, 's1': 1.1, 'cap': '물들인 톱밥과 손 · 1981년',
   'lines': [{'t': '무늬는 손으로 놓아요.'}, {'t': '모래는 꽉 쥔 주먹 사이로 흘려 뿌려요.'}, {'t': '빛깔이 선명하도록, 카펫을 늘 적셔 둬요.'}],
   'kid': [{'t': '손으로 톱밥을 살살 뿌려.'}, {'t': '그릇 속 톱밥은 무슨 색이야?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '톱밥 대신 꽃으로'},
  {'type': 'img', 'ch': 4, 'img': 'christ', 'fit': 'cover', 'p0': '50% 50%', 'p1': '52% 45%', 's0': 1.35, 's1': 1.05, 'cap': '꽃잎으로 만든 카펫 · 1981년',
   'lines': [{'t': '꽃과 솔잎, 과일과 채소도 카펫이 돼요.'}, {'t': '보랏빛 꽃잎 위에, 십자가에 달린 예수를 놓았어요.'}],
   'kid': [{'t': '이건 꽃잎으로 만들었어!'}, {'t': '보라색 꽃잎 위에 누가 있을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 5, 'no': 5, 't': '행렬이 지나가면'},
  {'type': 'img', 'ch': 5, 'img': 'path', 'fit': 'cover', 'p0': '45% 25%', 'p1': '55% 75%', 's0': 1.3, 's1': 1.15, 'cap': '행렬을 기다리는 꽃 카펫 · 2023년',
   'lines': [{'t': '2023년 성목요일, 행렬을 기다리는 카펫이에요.'}, {'t': '가마를 멘 행렬이 그 위를 천천히 지나가요.'}, {'t': '행렬이 끝나면, 청소하는 사람들이 금세 거리를 쓸어요.', 'wait': 1600}],
   'kid': [{'t': '행렬이 카펫 위로 지나가.'}, {'t': '그러면 그림이 흩어져.', 'wait': 1200}]},
  {'type': 'imagine', 'ch': 6,
   'lines': [{'t': '돌길 위로 물 뿌리는 소리가 칙칙 나요.'}, {'t': '젖은 톱밥에서 나무 냄새가 올라와요.'}, {'t': '멀리서 느린 행진곡이 다가와요.'}],
   'kid': [{'t': '눈을 감아 봐. 칙칙, 물 뿌리는 소리가 나.'}, {'t': '솔잎 냄새도 나.'}]},
  {'type': 'reward', 'ch': 6},
 ],
}
