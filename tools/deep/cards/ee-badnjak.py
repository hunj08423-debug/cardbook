# -*- coding: utf-8 -*-
"""깊은 카드: 세르비아 성탄 전야 ‘바드냐크’(ee-badnjak) · 중심 방식 = 놓아 보기 · 초벌
기준서 2판 · 틀 deep3-5 · 키트 3판 · 창 10 · 2026-11-22 만들기 시작
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 성탄 전야(1월 6일) 저녁, 체에서 곡식과 호두가 쏟아지는 가운데
     참나무 바드냐크가 화덕 불 위에 놓이고, 짚 위에서 아이들이 병아리처럼 호두를 줍는 순간.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 하나씩 놓아 보기 — 차차크 지방 기록(2006)의 흐름:
     체의 곡식 → 짚 → 꿀 → 바드냐크(불) → 포도주 → 호두.
카드 크기: 큰 카드(장면 넷) — 기록(차차크 국립 박물관 논문집 2006, 노보스티 2025·2026)과 그림(1909년 판화 · 2026년 사진)이 넉넉해요.
도우미: 고르기(넷째 장면 · 첫 손님에게 건넬 선물 — 이야기 속 집주인의 자리에서)
끝맺는 꼴: 기록 한 마디 — 폴로자이니크가 불씨를 뒤적이며 비는 말 “불꽃만큼 동전이, 양이, 소가…”
무대 그림은 이 안내서가 그렸어요(아래 stage_svg). 그림 원본(src)은 deep_src/ee-badnjak/ (저장소 밖)."""
import math, random
S = 'ee-badnjak/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

# 근거 주소
ZB = 'https://zbornik.cacakmuzej.org.rs/files/zbornik/36/ZRNMC_36_15.pdf'   # 샤포니치아샤닌 「성탄 절기」, 차차크 국립 박물관 논문집 36호(2006)
NOV25 = 'https://www.novosti.rs/c/drustvo/vesti/1447328/paljenjem-badnjaka-ispred-hrama-svetog-save-beogradjani-tradicionalno-obelezili-badnje-vece'
NOV26 = 'https://www.novosti.rs/c/drustvo/vesti/1562331/kako-pravilno-proslavlja-badnje-vece-pravoslavnoj-kuci-vernici-ove-obicaje-strogo-postuju'

# ── 이 안내서가 그린 무대: 밤의 시골집, 바닥 가운데 돌로 두른 화덕 ──
def leaf(cx, cy, s, rot, fill):
    # 참나무 잎(체르 참나무처럼 깊게 갈라진 잎)을 단순하게: 둥근 갈래가 있는 잎
    pts = []
    n = 9
    for i in range(n * 2 + 1):
        t = i / (n * 2)
        y = -1 + 2 * t                     # 잎자루 쪽(-1)에서 끝(1)으로
        w = math.sin(math.pi * t) * (0.55 if i % 2 == 0 else 0.33)
        pts.append((w, y))
    left = [(-w, y) for w, y in pts]
    right = [(w, y) for w, y in reversed(pts)]
    poly = left + right
    a = math.radians(rot)
    out = []
    for x, y in poly:
        X = cx + s * (x * math.cos(a) - y * math.sin(a)); Y = cy + s * (x * math.sin(a) + y * math.cos(a))
        out.append(f'{X:.1f},{Y:.1f}')
    vein = (cx - s * math.sin(a) * -1, cy + s * math.cos(a) * -1)
    tip = (cx - s * math.sin(a), cy + s * math.cos(a))
    return (f'<polygon points="{" ".join(out)}" fill="{fill}" stroke="#4a2a12" stroke-width="0.8" stroke-linejoin="round"/>'
            f'<line x1="{vein[0]:.1f}" y1="{vein[1]:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" stroke="#4a2a12" stroke-width="0.8"/>')
def flame(x, y, h, w):
    return (f'<path d="M{x} {y} C {x - w} {y - h * .35} {x - w * .4} {y - h * .7} {x} {y - h} C {x + w * .45} {y - h * .66} {x + w} {y - h * .32} {x} {y} Z" fill="url(#__U__fl)"/>'
            f'<path d="M{x} {y - 2} C {x - w * .45} {y - h * .3} {x - w * .15} {y - h * .55} {x} {y - h * .66} C {x + w * .2} {y - h * .5} {x + w * .45} {y - h * .28} {x} {y - 2} Z" fill="#fff1b8" opacity=".85"/>')
def stage_svg():
    R = random.Random(107)
    stars = ''.join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff" opacity="{o:.2f}"/>' for x, y, r, o in
                    [(52, 150, 1.1, .8), (96, 176, 0.9, .6), (120, 140, 1.2, .9), (78, 214, 0.8, .5), (666, 128, 1.0, .8), (700, 150, 0.8, .6), (684, 172, 1.1, .7)])
    # 짚: 바닥에 흩어진 금빛 줄기
    straw = ''
    for _ in range(150):
        x = R.uniform(40, 770); y = R.uniform(362, 446); L = R.uniform(14, 34); a = R.uniform(-0.5, 0.5) + (math.pi if R.random() < .5 else 0)
        straw += f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x + L * math.cos(a):.0f}" y2="{y + L * math.sin(a) * .35:.0f}" stroke="{R.choice(["#d8b25a", "#e6c46e", "#c49a45", "#efd58a"])}"/>'
    # 호두: 짚 위
    nuts = ''
    for x, y in [(118, 404), (176, 432), (232, 398), (286, 438), (338, 414), (520, 430), (566, 404), (612, 440), (664, 410), (716, 436), (452, 442), (392, 446), (150, 382), (690, 384)]:
        nuts += (f'<g transform="translate({x} {y})"><ellipse rx="7.5" ry="6.4" fill="#8b5a2b" stroke="#4a2c12" stroke-width="1"/>'
                 f'<path d="M-6 0 Q0 -2 6 0" stroke="#5a3616" stroke-width="1" fill="none"/><path d="M-3 -4 Q-1 0 -3 4 M3 -4 Q1 0 3 4" stroke="#a87542" stroke-width=".8" fill="none"/></g>')
    # 체: 문 곁, 곡식과 호두가 문 쪽으로 쏟아져요
    grains = ''.join(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="2.2" ry="1.4" fill="{R.choice(["#e8c25a", "#d9a441", "#f0d98a"])}" transform="rotate({R.uniform(0, 180):.0f} {x:.0f} {y:.0f})"/>'
                     for x, y in [(R.uniform(150, 232), R.uniform(222, 330)) for _ in range(46)])
    fly_nuts = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="4.3" fill="#8b5a2b" stroke="#4a2c12" stroke-width=".8"/>' for x, y in [(186, 236), (168, 262), (204, 280), (176, 304), (150, 326), (214, 322)])
    mesh = ''.join(f'<line x1="{218 + d}" y1="226" x2="{218 + d}" y2="250" />' for d in range(-26, 27, 6))
    sieve = (f'<g class="obj" data-o="sieve">{grains}{fly_nuts}'
             f'<g transform="rotate(-24 250 236)"><ellipse cx="250" cy="236" rx="38" ry="15" fill="#3a2614" stroke="#a8743a" stroke-width="5"/>'
             f'<ellipse cx="250" cy="236" rx="31" ry="10" fill="none" stroke="#c8a46a" stroke-width="1" stroke-dasharray="2 3"/>'
             f'<ellipse cx="250" cy="232" rx="24" ry="6" fill="#e1b84e"/><circle cx="244" cy="230" r="4" fill="#8b5a2b"/><circle cx="256" cy="232" r="4" fill="#8b5a2b"/></g></g>')
    honey = ('<g class="obj" data-o="honey"><g transform="translate(262 328)">'
             '<path d="M-20 0 C -26 14 -24 32 -14 38 L14 38 C 24 32 26 14 20 0 Z" fill="#9a5a2e" stroke="#5a3016" stroke-width="1.5"/>'
             '<ellipse cx="0" cy="0" rx="21" ry="6" fill="#b8763e" stroke="#5a3016" stroke-width="1.5"/><ellipse cx="0" cy="0" rx="16" ry="4" fill="#f0b030"/>'
             '<path d="M10 2 C 12 10 9 14 11 20" stroke="#f0b030" stroke-width="3" fill="none" stroke-linecap="round"/>'
             '<line x1="-4" y1="2" x2="-16" y2="-26" stroke="#c89a62" stroke-width="4" stroke-linecap="round"/></g></g>')
    wine = ('<g class="obj" data-o="wine"><g transform="translate(640 318) rotate(-38)">'
            '<path d="M-14 -8 C -22 6 -22 30 -12 40 L12 40 C 22 30 22 6 14 -8 Z" fill="#7a3b22" stroke="#3e1c0e" stroke-width="1.5"/>'
            '<path d="M-8 -8 L-9 -22 L9 -22 L8 -8 Z" fill="#7a3b22" stroke="#3e1c0e" stroke-width="1.5"/><path d="M-9 -22 L-14 -26 L-6 -24 Z" fill="#7a3b22"/>'
            '<path d="M14 2 C 26 4 26 22 14 26" stroke="#3e1c0e" stroke-width="3" fill="none"/></g>'
            '<path d="M612 300 C 590 302 560 316 532 334" stroke="#7b1730" stroke-width="3.5" fill="none" stroke-linecap="round" opacity=".9"/>'
            '<g transform="translate(694 380)"><ellipse cx="0" cy="6" rx="30" ry="7" fill="#5a3a22"/><path d="M-24 4 C -24 -14 24 -14 24 4 Z" fill="#c98a45" stroke="#7a4a1e" stroke-width="1.2"/>'
            '<path d="M-14 -4 Q0 -10 14 -4" stroke="#a86a2e" stroke-width="1.2" fill="none"/><circle cx="-4" cy="-8" r="1.3" fill="#fff"/><circle cx="2" cy="-9" r="1.2" fill="#fff"/><circle cx="6" cy="-7" r="1.1" fill="#fff"/></g></g>')
    # 바드냐크(불빛 무리 .lt): 첫 무리는 참나무 줄기와 마른 잎, 다음은 불꽃들, 마지막은 불티
    leaves = ''.join(leaf(x, y, s, r, f) for x, y, s, r, f in
                     [(546, 316, 24, 60, '#8a5a2e'), (566, 334, 22, 112, '#9c6a38'), (552, 296, 21, 18, '#7a4c26'), (578, 308, 23, 82, '#a5713f'),
                      (530, 296, 19, -24, '#8f5f30'), (588, 330, 19, 140, '#7f5129'), (570, 286, 18, 44, '#9a6634'), (536, 334, 18, 168, '#86562b')])
    log = ('<g class="lt" style="transition-delay:0s">'
           '<path d="M322 356 L528 330" stroke="#3b2616" stroke-width="18" stroke-linecap="round"/>'
           '<path d="M322 356 L528 330" stroke="#5a3b22" stroke-width="12" stroke-linecap="round"/>'
           '<path d="M340 350 L380 346 M410 344 L452 338 M470 338 L500 334" stroke="#2c1a0e" stroke-width="2" stroke-linecap="round"/>'
           '<path d="M500 334 L536 316 M512 332 L548 334" stroke="#4a301a" stroke-width="4" stroke-linecap="round"/>'
           f'{leaves}<ellipse cx="320" cy="356" rx="6" ry="9" fill="#c8a06a" stroke="#5a3b22" stroke-width="2"/></g>')
    flames = ''
    for k, (x, y, h, w) in enumerate([(352, 348, 46, 16), (388, 344, 62, 20), (426, 340, 72, 22), (462, 336, 58, 19), (496, 332, 44, 15)]):
        flames += f'<g class="lt" style="transition-delay:{0.15 + k * 0.12:.2f}s">{flame(x, y, h, w)}</g>'
    sparks = '<g class="lt" style="transition-delay:.9s">' + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffd27a"/>' for x, y, r in
                                                                    [(410, 252, 1.8), (436, 236, 1.4), (452, 262, 1.6), (392, 270, 1.3), (470, 246, 1.2), (424, 214, 1.1)]) + '</g>'
    stones = ''.join(f'<ellipse cx="{420 + 132 * math.cos(t):.0f}" cy="{362 + 26 * math.sin(t):.0f}" rx="{R.uniform(12, 17):.0f}" ry="{R.uniform(7, 10):.0f}" fill="{R.choice(["#4a4440", "#55504a", "#3e3934"])}" stroke="#1e1a17" stroke-width="1"/>'
                     for t in [i * 2 * math.pi / 22 for i in range(22)])
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="밤의 시골집 안. 바닥 가운데에 돌로 두른 화덕이 있고, 놓은 것들이 하나씩 나타나요."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e0906"/><stop offset="1" stop-color="#2b1b10"/></linearGradient>
<linearGradient id="__U__floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a1c12"/><stop offset="1" stop-color="#1a110b"/></linearGradient>
<radialGradient id="__U__glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffcf86"/><stop offset=".45" stop-color="#e08a3c" stop-opacity=".7"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".53" cy=".74" r=".75"><stop offset="0" stop-color="#ffd59a" stop-opacity=".6"/><stop offset=".5" stop-color="#ff9f4a" stop-opacity=".28"/><stop offset="1" stop-color="#ff7a2a" stop-opacity="0"/></radialGradient>
<linearGradient id="__U__fl" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ff7a1a"/><stop offset=".55" stop-color="#ffb23a"/><stop offset="1" stop-color="#ffe28a" stop-opacity=".9"/></linearGradient></defs>
<rect width="800" height="450" fill="url(#__U__wall)"/>
<g fill="#0a0604"><rect x="0" y="0" width="800" height="16"/><rect x="0" y="52" width="800" height="10"/></g>
<path d="M24 336 L24 132 Q90 104 156 132 L156 336 Z" fill="#141d36"/>
<g>{stars}</g>
<path d="M24 336 L24 132 Q90 104 156 132 L156 336" fill="none" stroke="#4a3220" stroke-width="7"/>
<path d="M156 132 L190 150 L190 330 L156 336 Z" fill="#3e2a18" stroke="#24170d" stroke-width="2"/>
<rect x="648" y="110" width="72" height="80" fill="#141d36" stroke="#4a3220" stroke-width="6"/><path d="M684 110 V190 M648 150 H720" stroke="#4a3220" stroke-width="4"/>
<path d="M0 330 L800 330 L800 450 L0 450 Z" fill="url(#__U__floor)"/>
<g class="obj" data-o="straw"><g stroke-width="1.6" stroke-linecap="round">{straw}</g></g>
<ellipse cx="420" cy="364" rx="118" ry="22" fill="#120b07"/>
<ellipse class="glow" cx="420" cy="350" rx="190" ry="90" fill="url(#__U__glow)" opacity=".14"/>
{stones}
<g fill="#ff8a3a" opacity=".55">{''.join(f'<circle cx="{R.uniform(330, 510):.0f}" cy="{R.uniform(356, 372):.0f}" r="{R.uniform(1.5, 3):.1f}"/>' for _ in range(18))}</g>
{sieve}
{log}{flames}{sparks}
{honey}
{wine}
<g class="obj" data-o="walnuts">{nuts}</g>
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''


ITEMS = [
 {'id': 'sieve', 't': '곡식 체', 'la': 'сито · 체', 'say': '안주인이 체에 담은 곡식과 호두를, 바드냐크와 그것을 들고 온 사람에게 뿌려요.'},
 {'id': 'straw', 't': '짚', 'la': 'слама · 짚', 'say': '짚도 바드냐크와 함께 들어와 온 집에 펼쳐져요. 짚을 들이는 것을 “성탄을 들여온다”고 했어요.'},
 {'id': 'honey', 't': '꿀', 'la': 'мед · 꿀', 'say': '불에 올리기 전, 식구들이 하나씩 다가와 바드냐크에 입을 맞추고 꿀을 발라요.'},
 {'id': 'lights', 't': '바드냐크', 'la': 'бадњак · 참나무', 'say': '참나무를 화덕 불 위에 엄숙하게 올려요. 마른 잎에 불이 붙어요.'},
 {'id': 'wine', 't': '포도주', 'la': 'вино · 포도주', 'say': '타오르는 바드냐크에 빵과 소금을 건네고, 포도주를 부어요.'},
 {'id': 'walnuts', 't': '호두', 'la': 'ораси · 호두', 'say': '안주인이 짚 위에 호두를 뿌리며 암탉처럼 “꼬꼬” 소리를 내요. 아이들은 병아리처럼 “삐약삐약” 하며 따라다니며 호두를 주워요.'},
]

CARD = {
 'id': 'ee-badnjak', 'mode': '놓아 보기',
 'pagetitle': '세르비아 성탄 전야 ‘바드냐크’',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>성탄 전날(1월 6일) 새벽부터 밤까지</b><span>세르비아 차차크 지방의 시골 집</span>',
 'lead': '세르비아의 성탄 전날, 해 뜨기 전에 베어 온 참나무가 저녁이면 화덕 불 위에 올라가요. 체에 담은 곡식부터 짚 위의 호두까지, 그 밤에 들어오는 것들이 차례로 있어요. 기록의 흐름대로 하나씩 놓아 화덕 앞의 밤을 열어 보세요.',
 'leadKid': '세르비아에서는 성탄 전날 밤, 참나무를 화덕에 올려 태운대. 곡식, 짚, 꿀, 호두… 하나씩 놓아 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 6분',
 'draft': '검수 전 시안이에요(기준서 2판 · 초벌). 장면에는 기록에 있는 것만 옮겼고, 곳마다 다른 것은 그렇다고 밝혔어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 # 화면 색: 화덕 불의 붉은 갈색
 'theme': """:root{--accent:#8A3A1C;--accent-ink:#fffaf5;--soft:rgba(138,58,28,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#e8a47c;--accent-ink:#14100c;--soft:rgba(232,164,124,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#e8a47c;--accent-ink:#14100c;--soft:rgba(232,164,124,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '불꽃', 'y': '성탄 전야', 'sub': '세르비아'},
 'doneNote': '참나무 한 그루가 숲에서 화덕까지 와서, 한 해의 복을 비는 불이 되었어요.',
 'images': {
  # 그림이 오면 채워요(그림을 Read로 본 뒤 alt·cap을 써요)
 },
 'scenes': [
  {'id': 'forest', 'label': '해 뜨기 전 숲으로', 'kind': 'photo', 'img': '__그림__',
   'text': ['성탄 전날 이른 아침, 해가 뜨기 전에 대개 집안의 가장 나이 많은 남자, 곧 집주인이 숲으로 가요. 차차크 지방에서는 곧고 잎이 무성한 체르 참나무를 골랐어요.',
            '베기 전에 그는 해 뜨는 동쪽을 보고 성호를 그어요. 그리고 나무에게 곡식 낟알을 선물해요. 나무를 사람처럼 부르며 이렇게 말했다고 해요.'],
   'quote': {'t': '너를 우리 집에 데려가려고 왔단다. 거기서 내 믿음직한 도우미가 되어 다오. 집에서도, 우리에서도, 들에서도, 어디서나 모든 일이 잘되고 나아지도록.',
             'from': 'M. 가브릴로비치가 1907년에 적은 말 · 샤포니치아샤닌 「성탄 절기」(차차크 국립 박물관 논문집 36호, 2006)에서 · 이 안내서가 옮김', 'u': ZB},
   'text2': ['도끼질은 홀수 번이어야 했어요. 집안의 복이 멈추지 않게 하려는 거예요. 나무는 다른 나무에 걸리지 않고 곧게 쓰러져야 했고, 집으로는 오른쪽 어깨에 메고 왔어요. 오른쪽이 복을 부른다고 여겼거든요.'],
   'kid': '해 뜨기 전에 할아버지가 숲에 가서, 참나무에게 곡식을 주며 인사해.', 'kidq': '나무에게 인사한다면, 무슨 말을 해 줄래?'},
  {'id': 'night', 'label': '화덕 앞의 밤', 'kind': 'mod', 'mod': 'place', 'night': True,   # ← 한가운데 장면
   'text': ['저녁이 되면 바드냐크를 집 안으로 들여요. 들고 온 사람이 문 앞에서 외쳐요. “주인장, 누구 있소?” 차차크 지방의 많은 마을에서는 안에서 이렇게 대답했어요. “있지요, 있어요. 당신이 오니 더 많아요.”',
            '그다음은 기록에 남은 흐름대로 이어져요. 아래에서 하나씩 골라 화덕 둘레에 놓아 보세요.'],
   'kid': '체에서 곡식이 쏟아지고, 참나무에 불이 붙어. 짚 위에 호두를 뿌리면 아이들이 병아리처럼 삐약삐약!', 'kidq': '너도 병아리처럼 호두를 주워 볼래? 어떤 소리를 낼 거야?'},
  {'id': 'today', 'label': '교회 앞마당의 불', 'kind': 'photo', 'img': '__그림__',
   'text': ['요즘 세르비아의 집은 대부분 화덕이 없어요. 그래서 바드냐크를 태우지 않고, 성탄날 먹을 고기 곁에 세워 두는 집이 많아요(노보스티, 2026년 1월).',
            '그 대신 성탄 전야 저녁에는 교회 앞마당에 모여 함께 바드냐크를 태워요. 2025년 1월 6일, 베오그라드 성 사바 성전 곁의 성 사바 교회 앞에도 아이 손을 잡은 부모와 노인들이 모였어요. 성가를 부르며 바드냐크를 축복하는 예배가 함께 드려졌어요.'],
   'text2': ['병아리 놀이도 이어지고 있어요. 요즘은 안주인이 식탁 밑에 과자와 선물, 장난감을 넣어 두면, 아이들이 병아리처럼 삐약거리며 찾아요(노보스티, 2026년 1월).'],
   'kid': '요즘은 교회 마당에 모여서 다 같이 불을 피워. 식탁 밑에서는 과자 찾기, 삐약삐약!', 'kidq': '식탁 밑에 무엇이 숨어 있으면 좋겠어?'},
  {'id': 'morning', 'label': '성탄 아침의 첫 손님', 'kind': 'photo', 'img': '__그림__', 'choose': True,
   'text': ['성탄 아침, 그 집에 처음 들어오는 손님을 폴로자이니크(положајник)라고 불러요. 그는 오는 길에 누구와도 성탄 인사를 나누지 않아요. 문을 두드리며 외쳐요. “그리스도께서 나셨어요, 즐거운 성탄이에요!” 주인이 답해요. “참으로 그리스도께서 나셨어요. 잘 오셨어요.”',
            '안주인은 그에게 갖가지 곡식을 뿌려요. 그는 화덕 곁 세 발 의자에 앉아 바드냐크의 불씨를 뒤적여 불꽃을 튀겨요. 그동안 안주인(대개 집안의 가장 나이 든 여자)이 그를 담요로 감싸 줘요. 불꽃이 튈 때 그는 이렇게 빌어요.'],
   'quote': {'t': '불꽃만큼 동전이, 양이, 소가, 새끼 돼지가, 밀이, 옥수수가…', 'from': '폴로자이니크가 불씨를 뒤적이며 비는 말 · 차차크 지방 기록(2006) · 이 안내서가 옮김', 'u': ZB},
   'text2': ['그가 떠날 때 집주인은 총을 한 번 쏘아, 이 집을 찾아온 첫 손님이 있었음을 마을에 알렸어요.'],
   'kid': '성탄 아침 첫 손님이 불씨를 탁탁! 불꽃만큼 복이 오래.', 'kidq': '불꽃이 하나 튈 때마다 무엇이 하나씩 생기면 좋겠어?'},
 ],
 'imagine': {'t': '문이 열리고 찬 공기와 함께 참나무 냄새가 들어와요. 체에서 쏟아진 낟알이 바닥에 사르르 흩어지고, 마른 잎이 탁탁 소리를 내며 타올라요. 짚 위로 굴러가는 호두 소리, 삐약삐약 웃음소리, 꿀과 연기가 섞인 냄새.',
             'kid': '눈을 감아 봐. 참나무가 탁탁 타는 소리. 호두가 데굴데굴. 삐약삐약 웃음소리!'},
 'lines': ['해 뜨기 전, 나무에게 곡식을 선물했어요.', '짚을 들이는 것은 성탄을 들여오는 일.', '불꽃만큼 동전이, 양이, 소가….'],
 'linesKid': ['참나무에게 인사해!', '호두를 줍자, 삐약삐약!'],
 'close': {'form': '기록 한 마디',
           'from': '성탄 아침 첫 손님 폴로자이니크가 바드냐크의 불씨를 뒤적이며 비는 말 “불꽃만큼 동전이, 양이, 소가, 새끼 돼지가, 밀이, 옥수수가…”(차차크 지방 기록 2006, 343쪽)',
           'ask': '화덕에 참나무를 올리는 저녁이라면, 새해 이 집에 무엇이 불꽃만큼 넉넉하기를 빌고 싶나요?',
           'askKid': '참나무에 불꽃이 튈 때, 우리 집에 무엇이 많아지면 좋겠어?'},
 'goals': {
  's4': {'t': '기록의 흐름대로', 'p': '기록의 흐름대로 여섯 가지를 다 놓으면 카드에 금박이 입혀져요.',
         'how': '곡식 체 → 짚 → 꿀 → 바드냐크 → 포도주 → 호두 차례로 놓아 보세요', 'done': '화덕 앞의 밤을 기록의 흐름대로 다 놓았어요',
         'ways': [{'id': 'plOrder', 't': '곡식 체 → 짚 → 꿀 → 바드냐크 → 포도주 → 호두 차례로 놓기'}]},
  's5': {'t': '첫 손님의 선물', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '넷째 장면 끝에서 첫 손님에게 건넬 선물을 고르거나, 아이와 함께 영화를 끝까지 보세요', 'done': '첫 손님에게 건넬 선물을 골랐어요',
         'ways': [{'id': 'choose', 't': '성탄 아침 첫 손님에게 건넬 선물 고르기', 'hint': '넷째 장면 ‘성탄 아침의 첫 손님’ 끝에서 골라 보세요', 'okt': '첫 손님에게 건넬 선물을 골랐어요'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'place': {
   'items': ITEMS, 'order': '곡식 체, 짚, 꿀, 바드냐크, 포도주, 호두',
   'intro': '아래에서 하나를 골라 화덕 둘레에 놓아 보세요. 차차크 지방의 기록은 체의 곡식으로 시작해 짚 위의 호두로 끝나요.',
   'climax': '화덕의 불빛이 온 방을 채워요. 참나무는 천천히 타오르고, 짚 위에서는 아이들이 호두를 주워요.<span class="la">Бадње вече · 바드냐크의 저녁 · 차차크 지방 기록(2006)의 흐름</span>',
   'home': None,
   'wrongOrder': '이 카드는 차차크 지방 기록의 흐름을 따라 놓아요: {order}',
   'orderDone': '기록의 흐름대로 다 놓았어요',
   'daylight': False,
   'svg': stage_svg()},
  'choose': {
   'q': '이 집 주인이라면, 성탄 아침 첫 손님에게 무엇을 건넬까요?',
   'opts': [{'t': '양말', 'r': '차차크 지방에서 흔히 건넨 선물이에요. 브르자니 마을에서는 양말과 실내화를 함께 줬어요.'},
            {'t': '수건', 'r': '수건도 흔히 건넨 선물이에요. 어떤 곳에서는 스카프를 줬어요.'},
            {'t': '셔츠', 'r': '셔츠도 흔히 건넨 선물이에요. 고리차니 마을에서는 삼이나 양털을 줬어요.'},
            {'t': '성탄 빵 한 조각', 'r': '어떤 집은 첫 손님과 함께 성탄 빵 ‘체스니차’를 쪼갰어요. 두 집이 하나 되어 서로 돕는다는 뜻이었어요.'}]},
 },
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 놓아 보기</button></div>
  <div class="pl-home" hidden><p></p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '기록마다 다른 점', 'p': [
    '<b>어떤 나무</b> 차차크 지방에서는 주로 체르 참나무를 골랐고, 곧고 잎이 무성한 나무를 찾았어요. 앞면 카드의 자료는 ‘곧게 자란 어린 참나무’라고 써요.',
    '<b>짚은 누가</b> 짚을 들이는 사람은 곳마다 달랐어요. 집주인이 들이는 곳도, 안주인이 들이는 곳도 있었어요. 19세기의 부크 카라지치는 안주인이나 가장 나이 든 여자가 들인다고 적었어요(차차크 지방 기록에서).',
    '<b>첫 손님의 이름</b> 앞면 카드는 ‘폴라즈니크’라고 썼어요. 차차크 지방 기록은 같은 성탄 아침의 첫 손님을 ‘폴로자이니크’라고 불러요.']},
  {'h': '함께 읽는 말씀', 'p': [
    '마리아는 아기를 포대기에 싸서 구유에 뉘었어요(' + bl('LUK.2', '누가복음 2장 7절') + '). 차차크 지방의 민속 기록은, 갓 태어난 그리스도가 처음 짚 위에 뉘었다는 이야기가 짚을 들이는 풍습과 이어졌다고 설명해요. 다만 풍습 자체는 그리스도교보다 훨씬 오래되었다고 해요.']},
  {'h': '직접 가 보기', 'checked': '2026년 11월 22일', 'p': [
    '세르비아 정교회의 성탄 전야는 옛 달력을 따라 1월 6일 저녁이에요. 베오그라드에서는 성 사바 성전 곁의 성 사바 교회 앞에서 해마다 바드냐크를 태워요(노보스티, 2025년 1월 6일 기사). 시간은 그해 교회 안내를 확인해요.'],
   'links': [{'t': '노보스티 — 2025년 베오그라드 성 사바 교회 앞 바드냐크 태우기', 'u': NOV25, 'm': '세르비아어'},
             {'t': '차차크 국립 박물관 논문집 — 「성탄 절기」(바드냐크와 첫 손님의 기록)', 'u': ZB, 'm': '세르비아어 · PDF'}]},
 ],
 'src': [
  {'l': '스네자나 샤포니치아샤닌 「성탄 절기」(차차크 국립 박물관 논문집 36호, 2006) 313~344쪽 — 해 뜨기 전 고르기, 체르 참나무·곧고 잎 무성, 동쪽·성호·곡식 선물, 나무에게 한 말(가브릴로비치 1907), 홀수 도끼질·곧게 쓰러짐·오른쪽 어깨, 문 앞 인사, 체의 곡식과 호두, 입맞춤·꿀, 빵·소금·밀·포도주, 짚(성탄을 들여옴)·호두와 병아리, 폴로자이니크(인사·곡식·세 발 의자·담요·불꽃의 말·선물·체스니차·총 한 방)', 'u': ZB},
  {'l': '노보스티 「성 사바 성전 앞 바드냐크 태우기」(2025년 1월 6일) — 성 사바 교회 앞, 부모와 아이·노인들, 바드냐크를 축복하는 예배와 성가', 'u': NOV25},
  {'l': '노보스티 「정교회 집에서 바드냐크의 저녁을 지내는 법」(2026년 1월 6일) — 화덕이 없는 집은 바드냐크를 성탄 고기 곁에, 짚은 온 집에, 식탁 밑의 과자와 장난감·병아리 소리', 'u': NOV26},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 50%', 'p1': '50% 45%', 's0': 1.2, 's1': 1.05, 'kicker': '성탄 전날 · 세르비아', 'title': '세르비아 성탄 전야 ‘바드냐크’',
   'lines': [{'t': '1월 6일, 세르비아의 성탄 전날.'}, {'t': '해가 뜨기 전에 숲으로 가요.'}],
   'kid': [{'t': '성탄 전날 아침이야.'}, {'t': '숲으로 나무를 베러 가!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '해 뜨기 전 숲으로'},
  {'type': 'img', 'ch': 1, 'img': '__그림__', 'fit': 'cover', 'p0': '50% 50%', 'p1': '50% 45%', 's0': 1.15, 's1': 1.0, 'cap': '__그림__',
   'lines': [{'t': '집안의 가장 나이 많은 남자가 숲에 가요.'}, {'t': '동쪽을 보고 성호를 긋고, 나무에게 곡식을 선물해요.'},
             {'t': '너를 우리 집에 데려가려고 왔단다.', 'q': True, 'from': '가브릴로비치가 적은 말(1907) · 이 안내서가 옮김'},
             {'t': '도끼질은 홀수 번. 집안의 복이 멈추지 않게.'}],
   'kid': [{'t': '할아버지가 참나무에게 인사해.'}, {'t': '곡식을 선물로 줘!'}, {'t': '나무에게 무슨 말을 해 줄래?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '화덕 앞의 밤'},
  {'type': 'mod', 'mod': 'place', 'ch': 2,
   'lines': [{'t': '저녁, 바드냐크가 집에 들어와요.'},
             {'t': '“주인장, 누구 있소?” “있지요, 당신이 오니 더 많아요.”'},
             {'t': '안주인이 체에 담은 곡식과 호두를 뿌려요.', 'act': 'sieve'},
             {'t': '짚도 함께 들어와 온 집에 펼쳐져요.', 'act': 'straw'},
             {'t': '입을 맞추고, 꿀을 발라요.', 'act': 'honey'},
             {'t': '참나무를 화덕 불 위에.', 'act': 'lights', 'wait': 1500},
             {'t': '빵과 소금을 건네고, 포도주를 부어요.', 'act': 'wine'},
             {'t': '짚 위에 호두가 쏟아지면, 아이들은 삐약삐약.', 'act': 'walnuts', 'wait': 1500},
             {'t': '화덕의 불빛이 온 방을 채워요.', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '체에서 곡식이 쏟아져!', 'act': 'sieve'}, {'t': '짚!', 'act': 'straw'}, {'t': '꿀!', 'act': 'honey'},
           {'t': '참나무에 불이 붙었어!', 'act': 'lights', 'wait': 1400}, {'t': '포도주!', 'act': 'wine'},
           {'t': '호두를 줍자, 삐약삐약!', 'act': 'walnuts', 'wait': 1400}, {'t': '방이 환해졌어!', 'act': 'day', 'wait': 1400}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '교회 앞마당의 불'},
  {'type': 'img', 'ch': 3, 'img': '__그림__', 'fit': 'cover', 'p0': '50% 50%', 'p1': '50% 45%', 's0': 1.15, 's1': 1.0, 'cap': '__그림__',
   'lines': [{'t': '요즘 집은 대부분 화덕이 없어요.'}, {'t': '성탄 전야에는 교회 앞마당에 모여 함께 태워요.'}, {'t': '식탁 밑에는 과자, 아이들은 여전히 삐약삐약.'}],
   'kid': [{'t': '교회 마당에서 다 같이 불을 피워.'}, {'t': '식탁 밑에 무엇이 숨어 있으면 좋겠어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '성탄 아침의 첫 손님'},
  {'type': 'img', 'ch': 4, 'img': '__그림__', 'fit': 'cover', 'p0': '50% 50%', 'p1': '50% 45%', 's0': 1.15, 's1': 1.0, 'cap': '__그림__',
   'lines': [{'t': '성탄 아침, 처음 들어오는 손님 폴로자이니크.'}, {'t': '“그리스도께서 나셨어요!” “참으로 나셨어요.”'}, {'t': '세 발 의자에 앉아 바드냐크의 불씨를 뒤적여요.'}],
   'kid': [{'t': '첫 손님이 불씨를 탁탁!'}, {'t': '불꽃이 튈 때마다 무엇이 생기면 좋겠어?', 'ask': True}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '참나무가 탁탁 소리를 내며 타올라요.'}, {'t': '짚 위로 호두가 데굴데굴 굴러가요.'}, {'t': '꿀과 연기가 섞인 냄새.'}],
   'kid': [{'t': '탁탁, 참나무가 타.'}, {'t': '호두가 데굴데굴!'}]},
  {'type': 'quote', 'ch': 5, 'big': '불꽃만큼 동전이, 양이, 소가, 새끼 돼지가, 밀이, 옥수수가…',
   'lines': [{'t': '성탄 아침 첫 손님이 불꽃을 튀기며 빈 말이에요.'}],
   'kid': [{'t': '불꽃만큼 복이 오래!'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
