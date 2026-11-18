# -*- coding: utf-8 -*-
"""깊은 카드: 용서의 주일(sh-forgive) · 중심 방식 = 놓아 보기
기준서 1판(보탬 10) · 틀 deep3-4 · 키트 3판 · 2026-11-18 17번 묶음 창이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 사순절을 여는 저녁 예배 끝, 사제가 먼저 엎드려 용서를 구하고 신자들이 한 사람씩
     “용서해 주세요”를 주고받는 동안 성가대가 부활절 노래를 나직이 부르는 순간
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 예식에서 실제로 사제가 먼저, 그다음 한 사람씩 나와 절하고 줄을 이어 가는 데서 —
     사제 → 첫 사람 → 둘째 → 셋째를 차례로 놓고, 마지막에 부활의 노래를 더하기
카드 크기: 큰 카드 — 정교회 기관·교회 누리집의 예식 설명, 『이집트의 마리아 전기』, 한국 정교회 주보가 넉넉해요.
무대 그림: 이 안내서가 그린 저녁의 정교회 성당(SVG, 아래 stage_svg). 실제 성당을 그린 것이 아니에요.
5단계 마무리: 방식 마무리(놓아 보기 ‘home’ — 내가 먼저 용서를 구하고 싶은 자리) + 아이와 끝까지. 고르기(choose)는 쓰지 않아요.
그림 원본(src)은 deep_src/sh-forgive/ (저장소 밖). 받는 법: commons_get.py"""
S = 'sh-forgive/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

OCA = 'https://www.oca.org/saints/lives/2025/03/03/8-beginning-of-great-lent'
OCAPDF = 'https://oca.org/PDF/Music/Lent/prelent.4.sun.cheesefare.lic.kievan.pdf'
OT = 'https://orthodoxtimes.com/?p=86630'
AZB = 'https://azbyka.ru/days/2057-03-11'
OW = 'https://orthodoxwiki.org/Forgiveness_Sunday'
MP = 'https://www.mospatusa.com/news_180218_2'
NLM = 'https://www.newliturgicalmovement.org/2018/02/forgiveness-sunday-in-byzantine-rite.html'
BYZ = 'https://thebyzantinelife.com/forgivness-vespers'
MARY = 'https://origin-rh.web.fordham.edu/Halsall/basis/maryegypt.asp'
OCAMARY = 'https://www.oca.org/saints/all-lives/2029/03/25'
JUBO = 'https://orthodoxkorea.org/wp-content/uploads/2026/02/jubo-20260222_2565.pdf'
OKR = 'https://www.orthodoxkorea.org/'
SSN = 'https://m.seoul.co.kr/news/2007/05/30/20070530023003'
HW = 'https://www.mfa.gr/missionsabroad/images/stories/missions/south-korea/2026/Holy_Week_EN_KR.pdf'
WAM = 'https://commons.wikimedia.org/wiki/File:Hymnal,_Expulsion_of_Adam_and_Eve_from_Paradise,_Walters_Manuscript_W.547,_fol._54v.jpg'

# ── 무대 그림(이 안내서가 그림) ──
def person(x, base, h, coat, head='#d9b48f', hair='#2b1d14', scarf=None, lean=0, trim=None, beard=None):
    """서 있는 사람(옆에서 본 듯한 단순한 모양). lean: 머리를 왼쪽(-)으로 숙인 정도(px)."""
    sh = base - h * 0.80          # 어깨 높이
    hy = base - h * 0.90          # 머리 가운데
    r = h * 0.075                 # 머리 반지름
    ws, wb = h * 0.17, h * 0.27   # 어깨 반너비, 아래 반너비
    hx = x + lean
    body = (f'<path d="M{x - ws:.1f} {sh + r * .6:.1f} Q {x - ws - 2:.1f} {sh - r * .2:.1f} {x - ws * .45:.1f} {sh - r * .55:.1f} '
            f'L {x + ws * .45:.1f} {sh - r * .55:.1f} Q {x + ws + 2:.1f} {sh - r * .2:.1f} {x + ws:.1f} {sh + r * .6:.1f} '
            f'L {x + wb:.1f} {base:.1f} L {x - wb:.1f} {base:.1f} Z" fill="{coat}"/>')
    # 팔(앞으로 모은 손)
    arm = (f'<path d="M{x - ws * .9:.1f} {sh + h * .06:.1f} Q {x - ws * .2:.1f} {sh + h * .30:.1f} {x + ws * .15:.1f} {sh + h * .30:.1f}" '
           f'stroke="rgba(0,0,0,.28)" stroke-width="{h * .03:.1f}" fill="none" stroke-linecap="round"/>')
    neck = f'<rect x="{hx - r * .45:.1f}" y="{hy + r * .6:.1f}" width="{r * .9:.1f}" height="{r * .9:.1f}" fill="{head}"/>'
    face = f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{r:.1f}" fill="{head}"/>'
    if scarf:
        top = (f'<path d="M{hx - r * 1.35:.1f} {hy + r * 1.5:.1f} Q {hx - r * 1.45:.1f} {hy - r * 1.55:.1f} {hx:.1f} {hy - r * 1.35:.1f} '
               f'Q {hx + r * 1.45:.1f} {hy - r * 1.55:.1f} {hx + r * 1.35:.1f} {hy + r * 1.5:.1f} '
               f'Q {hx + r * .9:.1f} {hy + r * .2:.1f} {hx:.1f} {hy + r * .1:.1f} Q {hx - r * .9:.1f} {hy + r * .2:.1f} {hx - r * 1.35:.1f} {hy + r * 1.5:.1f} Z" fill="{scarf}"/>')
    else:
        top = f'<path d="M{hx - r:.1f} {hy - r * .05:.1f} Q {hx - r * 1.05:.1f} {hy - r * 1.25:.1f} {hx:.1f} {hy - r * 1.12:.1f} Q {hx + r * 1.05:.1f} {hy - r * 1.25:.1f} {hx + r:.1f} {hy - r * .05:.1f} Q {hx:.1f} {hy - r * .55:.1f} {hx - r:.1f} {hy - r * .05:.1f} Z" fill="{hair}"/>'
    bd = ''
    if beard:
        bd = f'<path d="M{hx - r * .85:.1f} {hy + r * .1:.1f} Q {hx - r * .7:.1f} {hy + r * 2.2:.1f} {hx:.1f} {hy + r * 2.5:.1f} Q {hx + r * .7:.1f} {hy + r * 2.2:.1f} {hx + r * .85:.1f} {hy + r * .1:.1f} Q {hx:.1f} {hy + r * .9:.1f} {hx - r * .85:.1f} {hy + r * .1:.1f} Z" fill="{beard}"/>'
    tr = ''
    if trim:   # 사제의 영대(목에서 아래로 늘어뜨린 띠)와 작은 십자
        tr = (f'<rect x="{x - h * .045:.1f}" y="{sh:.1f}" width="{h * .09:.1f}" height="{base - sh - 4:.1f}" fill="{trim}"/>'
              + ''.join(f'<path d="M{x:.1f} {y - 3:.1f} v6 M{x - 3:.1f} {y:.1f} h6" stroke="#cfc6d8" stroke-width="1.3"/>'
                        for y in (sh + h * .22, sh + h * .44, sh + h * .66)))
    return body + tr + arm + neck + face + top + bd


def icon_panel(x, y, w, h, bg, robe, halo='#e2bd62'):
    cx = x + w / 2
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#__U__gold)"/>'
            f'<rect x="{x + 3}" y="{y + 3}" width="{w - 6}" height="{h - 6}" fill="{bg}"/>'
            f'<circle cx="{cx}" cy="{y + h * .3:.1f}" r="{w * .2:.1f}" fill="none" stroke="{halo}" stroke-width="2"/>'
            f'<circle cx="{cx}" cy="{y + h * .3:.1f}" r="{w * .12:.1f}" fill="#c99a6a" opacity=".7"/>'
            f'<path d="M{x + w * .2:.1f} {y + h - 3} C {x + w * .22:.1f} {y + h * .55:.1f} {cx - w * .1:.1f} {y + h * .45:.1f} {cx:.1f} {y + h * .45:.1f} '
            f'C {cx + w * .1:.1f} {y + h * .45:.1f} {x + w * .78:.1f} {y + h * .55:.1f} {x + w * .8:.1f} {y + h - 3} Z" fill="{robe}"/>')


def candle_stand(x, n=5, lit_id=''):
    base = (f'<path d="M{x - 14} 334 L {x + 14} 334 L {x + 6} 324 L {x - 6} 324 Z" fill="#8a6a34"/>'
            f'<rect x="{x - 2.5}" y="262" width="5" height="62" fill="#9c7a3c"/>'
            f'<ellipse cx="{x}" cy="262" rx="28" ry="6" fill="#b08a44"/><ellipse cx="{x}" cy="260" rx="24" ry="4" fill="#6e5528"/>')
    cs, fl = '', ''
    for k in range(n):
        cx = x - 18 + k * 36 / (n - 1)
        top = 236 + (k % 2) * 6
        cs += f'<rect x="{cx - 1.6:.1f}" y="{top}" width="3.2" height="{260 - top}" fill="#efe2bf"/>'
        fl += f'<ellipse cx="{cx:.1f}" cy="{top - 4}" rx="2.2" ry="4.2" fill="#ffd27a"/><ellipse cx="{cx:.1f}" cy="{top - 3}" rx="1" ry="2.2" fill="#fff6dc"/>'
    halo = f'<ellipse cx="{x}" cy="232" rx="34" ry="22" fill="url(#__U__flame)" opacity=".55"/>'
    return base + cs + halo + fl


def note(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><ellipse cx="0" cy="0" rx="6" ry="4.4" transform="rotate(-20)" fill="#ffdc8f"/>'
            f'<rect x="4.4" y="-22" width="2" height="22" fill="#ffdc8f"/><path d="M6.4 -22 q 8 4 9 13" stroke="#ffdc8f" stroke-width="2" fill="none"/></g>')


def stage_svg():
    # 이콘 벽(이코노스타시스): 위 작은 줄 + 아래 큰 이콘 여섯과 가운데 문
    top_row = ''.join(icon_panel(146 + i * 43, 70, 36, 40, '#4a1c22' if i % 2 else '#1f2c4a', '#7a2a2a' if i % 2 else '#2a3f6b') for i in range(12))
    big = ''
    for i, x in enumerate([150, 222, 294]):
        big += icon_panel(x, 124, 64, 116, ['#1f2c4a', '#4a1c22', '#24331f'][i], ['#2a3f6b', '#8a2a24', '#5a3a1e'][i])
    for i, x in enumerate([442, 514, 586]):
        big += icon_panel(x, 124, 64, 116, ['#24331f', '#4a1c22', '#1f2c4a'][i], ['#5a3a1e', '#8a2a24', '#2a3f6b'][i])
    doors = ('<path d="M370 246 L 370 150 Q 370 124 400 120 Q 430 124 430 150 L 430 246 Z" fill="#4a3018" stroke="url(#__U__gold)" stroke-width="4"/>'
             '<line x1="400" y1="124" x2="400" y2="246" stroke="#c9a24c" stroke-width="2"/>'
             '<path d="M400 98 v18 M392 106 h16" stroke="#e2bd62" stroke-width="3"/>'
             '<rect x="380" y="160" width="14" height="22" fill="#6b4a24" stroke="#c9a24c" stroke-width="1"/><rect x="406" y="160" width="14" height="22" fill="#6b4a24" stroke="#c9a24c" stroke-width="1"/>')
    # 성가대(왼쪽 앞): 보면대와 세 사람
    choir = (person(160, 334, 92, '#2c2a3a', scarf='#3a3550') + person(188, 334, 98, '#33293a', hair='#3a2a1c')
             + person(214, 334, 90, '#2a3340', scarf='#4a4058')
             + '<path d="M176 300 L 210 296 L 212 304 L 178 308 Z" fill="#6e5528"/><rect x="192" y="304" width="4" height="30" fill="#5a4420"/>')
    # 성가대 노래(부활의 노래): 음표와 촛불 둘레 빛, 이콘 벽의 금빛
    lt = (f'<g class="lt">{note(170, 214, 1.0, -8)}</g><g class="lt">{note(200, 196, 1.15, 6)}</g><g class="lt">{note(228, 210, .95, -4)}</g>'
          '<g class="lt"><ellipse cx="268" cy="236" rx="70" ry="44" fill="url(#__U__flame)" opacity=".9"/><ellipse cx="664" cy="236" rx="60" ry="40" fill="url(#__U__flame)" opacity=".8"/></g>'
          '<g class="lt"><rect x="130" y="62" width="540" height="186" fill="#ffd68a" opacity=".14"/></g>')
    # 독서대(이콘을 놓은 받침)와 사순절의 어두운 덮개
    analogion = ('<path d="M338 332 L 346 276 M366 332 L 358 276" stroke="#5a4420" stroke-width="4"/>'
                 '<path d="M324 262 L 380 262 L 386 286 L 318 286 Z" fill="#3a1f3f"/>'
                 '<path d="M318 286 L 386 286 L 382 300 L 322 300 Z" fill="#2c1730"/>'
                 '<path d="M342 268 L 362 268" stroke="#b9a6c8" stroke-width="1.4"/>'
                 '<g transform="rotate(-10 352 252)"><rect x="340" y="236" width="24" height="30" fill="url(#__U__gold)"/><rect x="343" y="239" width="18" height="24" fill="#5b1418"/>'
                 '<circle cx="352" cy="247" r="4.5" fill="none" stroke="#e9c46a" stroke-width="1.2"/><path d="M346 263 C 347 254 350 252 352 252 C 354 252 357 254 358 263 Z" fill="#2a3f6b"/></g>')
    people = (f'<g class="obj" data-o="priest">{person(420, 334, 112, "#151318", head="#d8b28e", hair="#4a4a4a", beard="#6b6b6b", lean=-3, trim="#3b2142")}</g>'
              f'<g class="obj" data-o="p1">{person(478, 334, 98, "#5e2430", scarf="#7d93b0", lean=-4)}</g>'
              f'<g class="obj" data-o="p2">{person(536, 334, 106, "#2f4636", hair="#3b2a1c", lean=-3)}</g>'
              f'<g class="obj" data-o="p3">{person(592, 334, 84, "#8a6a2a", hair="#2b1d14", lean=-3)}</g>')
    floor_lines = ''.join(f'<line x1="{400 + (x - 400) * .35:.0f}" y1="300" x2="{x}" y2="450" stroke="#3a2c2a" stroke-width="1" opacity=".5"/>' for x in range(-200, 1001, 100))
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="저녁의 정교회 성당 안. 뒤쪽에 금빛 이콘 벽과 가운데 문이 있고, 앞쪽 가운데에 이콘을 얹은 독서대, 왼쪽에 성가대와 촛대가 있다. 놓은 사람들이 독서대 오른쪽으로 한 줄로 늘어서고, 부활의 노래를 더하면 음표와 촛불 빛이 퍼진다."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#120f1c"/><stop offset="1" stop-color="#271c2a"/></linearGradient>
<linearGradient id="__U__floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2024"/><stop offset="1" stop-color="#130e10"/></linearGradient>
<linearGradient id="__U__gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d4ae58"/><stop offset="1" stop-color="#7d5b22"/></linearGradient>
<radialGradient id="__U__flame" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd896" stop-opacity=".85"/><stop offset=".6" stop-color="#ff9d4a" stop-opacity=".22"/><stop offset="1" stop-color="#ff9d4a" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__glow" cx=".5" cy=".55" r=".55"><stop offset="0" stop-color="#ffcf8a" stop-opacity=".8"/><stop offset=".55" stop-color="#c06a2a" stop-opacity=".25"/><stop offset="1" stop-color="#2a140a" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".42" r=".8"><stop offset="0" stop-color="#fff0cc" stop-opacity=".5"/><stop offset=".55" stop-color="#ffcf8a" stop-opacity=".18"/><stop offset="1" stop-color="#ffb35c" stop-opacity="0"/></radialGradient></defs>
<rect width="800" height="450" fill="url(#__U__wall)"/>
<rect x="128" y="60" width="544" height="190" fill="#2e2016"/>{top_row}{big}{doors}
<rect x="128" y="246" width="544" height="8" fill="#5a4024"/>
<rect x="0" y="300" width="800" height="150" fill="url(#__U__floor)"/>{floor_lines}
<rect x="0" y="296" width="800" height="5" fill="#3a2a22"/>
<ellipse class="glow" cx="430" cy="290" rx="300" ry="170" fill="url(#__U__glow)" opacity=".14"/>
{candle_stand(268)}{candle_stand(664, 4)}
{choir}{analogion}{lt}{people}
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''


ITEMS = [
 {'id': 'priest', 't': '사제', 'la': 'простите ми, грешному',
  'say': '저녁 예배가 끝나면 사제가 먼저 사람들 앞에 서요. 땅에 엎드려 절하며 “죄인인 저를 용서해 주세요” 하고 모두에게 용서를 구해요.'},
 {'id': 'p1', 't': '첫 사람', 'la': 'Бог простит',
  'say': '첫 사람이 나와 이콘에 입을 맞추고, 사제 앞에 엎드려 “죄인인 저를 용서해 주세요” 해요. 사제도 엎드려 절하며 “하느님께서 용서하십니다. 저도 용서해 주세요” 하고 답해요.'},
 {'id': 'p2', 't': '둘째 사람', 'la': 'прости и нас, грешных',
  'say': '사제와 용서를 주고받은 첫 사람은 사제 옆에 서요. 둘째 사람은 사제와, 그다음 줄에 선 첫 사람과도 차례로 용서를 주고받아요.'},
 {'id': 'p3', 't': '셋째 사람', 'la': 'Бог простит, и я прощаю',
  'say': '셋째 사람은 줄에 선 세 사람과 차례로 용서를 주고받고 줄 끝에 서요. 이렇게 줄이 길어지면, 끝날 무렵에는 모두가 서로와 한 번씩 용서를 주고받아요.'},
 {'id': 'lights', 't': '부활의 노래', 'la': 'пасхальные песнопения',
  'say': '사람들이 용서를 주고받는 동안 성가대는 부활절 노래를 나직이 불러요. 사순절이 막 시작되는 저녁에, 부활의 기쁨을 미리 맛보게 하는 노래예요.'},
]

CARD = {
 'id': 'sh-forgive', 'mode': '놓아 보기',
 'pagetitle': '용서의 주일',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>사순절 바로 앞 일요일 저녁</b><span>정교회 세계 · 서울 성 니콜라스 대성당</span>',
 'lead': '정교회의 긴 사순절이 시작되기 전날 저녁, 신자들은 교회에 모여 한 사람씩 “용서해 주세요”를 주고받아요. 사제가 먼저 엎드려 용서를 구하고, 그동안 성가대는 부활절 노래를 불러요. 그 저녁의 예식을 한 사람씩 놓아 보세요.',
 'leadKid': '긴 금식을 시작하기 전날 저녁, 모두가 한 사람씩 “용서해 주세요” 하고 인사한대. 신부님이 맨 먼저 해!',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 6분 · 용서의 예식을 차례로 놓아 봐요',
 'draft': '검수 전 시안이에요(기준서 1판). 장면에는 정교회 기관과 교회 누리집, 『이집트의 마리아 전기』, 한국 정교회 주보에 있는 것만 옮겼어요. 예식의 모습은 교회마다 조금씩 달라서 그 점을 함께 적었어요. 무대 그림은 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#5B3A6E;--accent-ink:#fbf7ff;--soft:rgba(91,58,110,.09);--stamp:#7a3b8a}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#c9a9de;--accent-ink:#140f18;--soft:rgba(201,169,222,.10);--stamp:#d58be8}}
:root[data-theme="dark"]{--accent:#c9a9de;--accent-ink:#140f18;--soft:rgba(201,169,222,.10);--stamp:#d58be8}""",
 'stamp': {'t': '용서', 'y': '7세기', 'sub': '요르단'},
 'doneNote': '사제부터 셋째 사람까지 용서의 줄을 잇고, 부활의 노래로 사순절 첫 저녁을 채웠어요.',
 'images': {
  # 'card'는 사이트 앞면 그림(2023년 용서의 주일, 키로프의 마슬레니차 인형)을 써요.
  'hymnal': {'src': S + 'Hymnal_Expulsion_of_Adam_and_Eve_from_Paradise_Walters_Manuscript_W.547_fol._54v.jpg', 'crop': (0.30, 0.095, 0.975, 0.765),
             'cap': '‘낙원에서 쫓겨남’ · 아르메니아 찬송집, 1678년 콘스탄티노폴리스',
             'cr': '그림: 월터스 미술관의 아르메니아 찬송집(W.547) · 퍼블릭 도메인 · 위키미디어 공용', 'u': WAM,
             'alt': '금빛 바탕의 그림. 왼쪽 위 구름 속에서 후광을 두른 분이 손을 내밀고, 그 아래에 붉은 옷과 푸른 겉옷을 입은 날개 달린 천사가 칼을 세워 들고 서 있다. 오른쪽 성벽의 아치 문 아래로, 나뭇잎 치마를 두른 아담과 하와가 가슴에 손을 얹고 문을 나선다. 그림 아래에는 두 물고기 모양의 붉은 머리글자로 시작하는 아르메니아 글이 쓰여 있다.'},
  'jordan': {'src': S + 'Jordan_River_at_Qasr_al-Yahud_2019_01.jpg',
             'cap': '요르단강, 카스르 알야후드에서 상류 쪽 · 2019년 4월',
             'cr': '사진: Bahnfrend · CC BY-SA 4.0 · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:Jordan_River_at_Qasr_al-Yahud,_2019_(01).jpg',
             'alt': '키 큰 갈대와 풀이 우거진 사이로 흙빛 강물이 흐른다. 강가에 나무들이 서 있고, 파란 하늘에 흰 구름이 떠 있다.'},
  'mosaic': {'src': S + 'St._Nicholas_Cathedral_Seoul_4.jpg',
             'cap': '대성당 문 위의 성 니콜라스 모자이크 · 2023년',
             'cr': '사진: Gre regiment · CC BY-SA 4.0 · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:St._Nicholas_Cathedral_(Seoul)_4.jpg',
             'alt': '반달 모양 아치 안의 금빛 모자이크. 후광을 두른 흰 수염의 성 니콜라스가 십자 무늬 띠를 두른 옷을 입고, 한 손으로 복을 빌며 다른 손에 책을 들었다. 양옆에 그리스 글자로 ‘성 니콜라오스’, 오른쪽 아래에 한글로 ‘성 니콜라스’라고 쓰여 있다.'},
  'plaque': {'src': S + 'St._Nicholas_Cathedral_Seoul.jpg',
             'cap': '대성당 벽의 ‘서울미래유산’ 표지 · 2023년',
             'cr': '사진: Gre regiment · CC BY-SA 4.0 · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:St._Nicholas_Cathedral_(Seoul).jpg',
             'alt': '자줏빛 금속판에 ‘정교회 한국대교구 서울 성 니콜라스 대성당’과 영어 이름이 새겨져 있다. 가운데 네모 칸에 ‘서울 미래 유산’이라는 큰 글씨가 있고, 아래에 ‘Seoul Future Heritage’와 ‘서울특별시 2013_275’가 쓰여 있다.'},
 },
 'scenes': [
  {'id': 'adam', 'label': '낙원 문 앞의 아담', 'kind': 'photo', 'img': 'hymnal',
   'text': ['정교회는 사순절 바로 앞 일요일을 ‘용서의 주일’이라고 불러요. 같은 날 아담이 낙원에서 쫓겨난 일도 기억해서, 교회 달력에는 ‘치즈 주일’, ‘아담이 쫓겨난 날’로도 적혀 있어요.',
            '이날 예배의 노래들은 낙원에서 쫓겨나 그 앞에 앉아 우는 아담을 노래해요. 아침 성찬예배에서는 남의 잘못을 용서하라는 말씀과, 금식할 때 남에게 드러내지 말라는 말씀을 읽어요(' + bl('MAT.6', '마태복음 6장 14~21절') + ').'],
   'text2': ['이 그림은 1678년 콘스탄티노폴리스에서 완성한 아르메니아 찬송집에 실린 ‘낙원에서 쫓겨남’이에요. 칼을 든 천사 앞에서 아담과 하와가 낙원의 문을 나서요.'],
   'kid': '아담과 하와가 낙원 문 밖으로 나가고 있어. 날개 달린 천사가 문을 지켜.',
   'kidq': '천사는 손에 무엇을 들고 있을까?'},
  {'id': 'jordan', 'label': '강을 건너기 전에', 'kind': 'photo', 'img': 'jordan',
   'text': ['서로 용서를 구하고 사순절을 시작하는 모습은 옛 기록에도 나와요. 7세기 예루살렘 총대주교 소프로니오스가 쓴 『이집트의 마리아 전기』는 요르단강 가까운 한 수도원의 규칙을 전해요.',
            '사순절이 시작될 때 수도자들은 성찬을 받고 조금 먹은 뒤 다시 성당에 모였어요. 엎드려 기도하고, 서로 입 맞추며 용서를 구하고, 원장에게 앞으로의 싸움을 위해 축복을 청했어요.'],
   'text2': ['그다음 주님이 나의 빛이고 구원이시니 두려울 것이 없다고 노래하는 시편(' + bl('PSA.27', '시편 27편') + ')을 부르며 문을 나서, 요르단강을 건너 사막으로 흩어졌어요. 수도원에는 한두 사람만 남았어요.',
             '사막에서는 서로 말을 걸지 않고, 남이 어떻게 금식하는지 알려 하지 않았어요. 그리고 부활절 한 주 전, 종려 주일에 수도원으로 돌아왔어요.'],
   'kid': '수도자들은 강을 건너 사막으로 떠나기 전에, 서로 “용서해 줘” 하고 인사했대.',
   'kidq': '먼 길을 떠나기 전에, 너는 누구에게 인사하고 싶어?'},
  {'id': 'vespers', 'label': '용서의 저녁 예배', 'kind': 'mod', 'mod': 'place', 'night': True,   # ← 그 자리에 있고 싶은 한 순간(한가운데 장면)
   'text': ['용서의 주일 저녁, 교회는 저녁 예배(만과)로 사순절을 열어요. 예배 앞부분은 밝은 축일 제의로 드리다가, 사순절을 알리는 큰 노래가 끝나면 제단 문을 닫고 사순절의 어두운 제의로 갈아입어요. 노래 가락도 사순절 가락으로 바뀌어요.',
            '예배가 끝나면 용서의 예식이 시작돼요. 아래에서 하나씩 골라 무대에 놓아 보세요. 사제가 먼저, 그다음 한 사람씩 나와요.'],
   'text2': ['교회마다 모습은 조금씩 달라요. 사람들이 사제에게 차례로 나아간 뒤 서로 용서를 구하는 곳도 있고, 이 무대처럼 사제 옆에 줄을 이어 서서 모두가 모두와 주고받는 곳도 있어요.'],
   'kid': '한 사람씩 앞으로 나와서 “용서해 주세요” 하고 절해. 신부님도 똑같이 절해!',
   'kidq': '“용서해 주세요”라는 말을 들으면, 너는 뭐라고 대답할래?'},
  {'id': 'seoul', 'label': '서울의 용서 주일', 'kind': 'duo', 'imgs': ['mosaic', 'plaque'],
   'text': ['한국에서는 세계 총대주교청에 속한 한국 정교회가 이 예배를 드려요. 한국 정교회 주보는 이날을 ‘용서 주일’, 이날 오후의 예배를 ‘참회의 만과’라고 적어요.',
            '2026년 용서 주일 주보는 사랑과 용서로 사순절을 시작하자며 모두 참례하자고 알렸어요. 다음 날은 ‘정결 월요일’, 사순절의 첫날이에요.'],
   'text2': ['서울 마포구 아현동 언덕의 성 니콜라스 대성당은 1968년에 세운, 한국에서 처음 지은 비잔틴 양식 성당이에요. 벽에는 ‘서울미래유산’ 표지가 붙어 있어요.'],
   'kid': '서울에도 이 예배를 드리는 성당이 있어. 문 위에 금빛 모자이크가 반짝여.',
   'kidq': '내일부터 새로 시작한다면, 오늘 누구에게 먼저 인사하고 싶어?'},
 ],
 'imagine': {'t': '촛불 몇 개만 남은 어스름한 성당에 향 냄새가 아직 남아 있어요. 앞에서 누군가 무릎을 꿇는 옷자락 소리가 나고, 낮은 목소리로 “용서해 주세요”가 오가요. 그 사이로 성가대의 부활절 노래가 작게, 아주 작게 흘러요.',
             'kid': '눈을 감아 봐. 촛불이 깜빡, 노래가 조용조용. “용서해 줘.” “하느님도, 나도 용서해.”'},
 'lines': ['용서해 주세요, 내가 먼저.', '한 사람씩, 줄이 길어져요.', '금식의 문 앞에서 부활을 노래해요.', '용서는 사순절의 시작이에요.'],
 'linesKid': ['용서해 줘!', '나도 용서해.', '한 사람씩 차례차례.'],
 'goals': {
  's4': {'t': '용서의 줄', 'p': '예식의 차례대로 다 놓으면 카드에 금박이 입혀져요.',
         'how': '‘용서의 저녁 예배’ 장면에서 사제부터 차례로 놓아 보세요', 'done': '사제부터 차례로 용서의 줄을 다 이었어요',
         'ways': [{'id': 'plOrder', 't': '사제 → 첫 사람 → 둘째 → 셋째 → 부활의 노래 차례로 놓기'}]},
  's5': {'t': '내가 먼저', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '다 놓은 뒤 ‘내가 먼저 용서를 구하고 싶은 자리’를 고르거나, 아이와 함께 끝까지 보세요', 'done': '내가 먼저 용서를 구하고 싶은 자리를 골랐어요',
         'ways': [{'id': 'home', 't': '내가 먼저 용서를 구하고 싶은 자리 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'place': {
   'items': ITEMS, 'order': '사제, 첫 사람, 둘째 사람, 셋째 사람, 부활의 노래',
   'intro': '아래에서 하나씩 골라 무대에 놓아 보세요. 사제가 먼저, 그다음 한 사람씩 나와요. 마지막으로 성가대의 노래를 더해요.',
   'climax': '사순절 첫 저녁, 성당이 서로 용서를 주고받는 사람들과 부활의 노래로 가득해요. 내일은 ‘정결 월요일’, 사순절의 첫날이에요.<span class="la">용서는 사순절의 시작이자 바탕이에요 · 슈메만 신부(미국 정교회)</span>',
   'home': ['우리 집', '일터', '학교', '친구들 사이', '교회'],
   'homeLabel': '내가 먼저 용서를 구하고 싶은 자리',
   'homeWait': '용서의 예식을 다 놓아 본 뒤 고를 수 있어요',
   'wrongOrder': '사제가 먼저 용서를 구하고, 사람들이 한 사람씩 나와요. 성가대는 그동안 노래해요. 놓는 차례는 이래요: {order}',
   'orderDone': '사제부터 차례로 용서의 줄을 다 이었어요',
   'daylight': False,
   'svg': stage_svg()},
 },
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 놓아 보기</button></div>
  <div class="pl-home" hidden><p>내 삶에서, 먼저 “용서해 주세요”라고 말하고 싶은 자리는 어디인가요?</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div><p class="mod-note">무대 그림: 이 안내서가 그린 저녁의 정교회 성당(실제 성당이 아니에요) · 예식의 차례는 <a href="''' + AZB + '''" target="_blank" rel="noopener">아즈부카 베리</a>와 <a href="''' + OW + '''" target="_blank" rel="noopener">오소독스위키</a>를 바탕으로</p></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>먼저 엎드리는 사제</b> 러시아 정교회의 안내는 이렇게 적어요. 사제가 땅에 엎드려 “복을 빌어 주시고, 죄인인 저를 용서해 주세요” 하고 청하면, 사람들도 엎드려 “하느님께서 용서하십니다. 저희도 용서하시고 복을 빌어 주세요” 하고 답해요. 그다음 모두가 서로 용서를 구해요.',
    '<b>“하느님께서 용서하십니다”</b> 이 대답은 ‘하느님께서 용서하시고, 나도 용서한다’는 뜻이에요. 러시아 정교회 누리집 ‘아즈부카 베리’는 이렇게 말하면 내가 남을 심판하는 자리에 서지 않게 된다고 풀어요.',
    '<b>제단 문이 닫히면</b> 사순절을 알리는 큰 노래 ‘큰 프로키메논’(' + bl('PSA.69', '시편 69편 17~18절') + '에서 따온 노래)이 끝나면 제단 문을 닫고, 성직자들이 사순절 제의로 갈아입어요. 그 뒤로 예배는 사순절의 모습이 돼요.',
    '<b>사막에서 만난 사람</b> 『이집트의 마리아 전기』에서 수도자 조시마는 바로 그 사순절 사막에서 이집트의 마리아를 만나요. 정교회는 사순절 다섯째 주일에 마리아를 기억해요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>주고받는 말</b> 교회와 언어마다 말이 조금씩 달라요. “하느님께서 용서하십니다. 저도 용서해 주세요”라고 답하기도 하고, “하느님께서 우리 둘을 용서하시기를” 하고 답하기도 해요.',
    '<b>줄을 서는 법</b> 사람들이 사제에게 차례로 나아간 뒤 서로 용서를 구하는 곳도 있고, 사제 옆에 줄을 이어 서서 모두가 모두와 주고받는 곳도 있어요.',
    '<b>어두운 빛깔</b> 사순절 제의를 검정이라고 적은 곳도 있고, 보라나 짙은 빨강이라고 적은 곳도 있어요.',
    '<b>어느 일요일에</b> 『이집트의 마리아 전기』를 옮긴 글마다, 수도자들이 떠난 날을 ‘사순절이 시작될 때(용서의 주일)’라고도, ‘사순절 첫 주일’이라고도 적어요.']},
  {'h': '함께 읽는 말씀', 'p': [
    '말씀은 뜻만 옮기고, 본문은 대한성서공회 개역개정으로 이어 드려요.',
    '<b>' + bl('MAT.6', '마태복음 6장 14~21절') + '</b> 남의 잘못을 용서하면 하늘 아버지도 너희를 용서하신다는 말씀, 금식할 때 남에게 보이려 하지 말라는 말씀, 보물을 하늘에 쌓으라는 말씀이에요. 용서의 주일 아침에 읽어요.',
    '<b>' + bl('GEN.3', '창세기 3장 23~24절') + '</b> 하나님이 사람을 에덴동산에서 내보내시고, 그룹들과 두루 도는 불 칼로 생명나무의 길을 지키게 하셨어요.',
    '<b>' + bl('ROM.13', '로마서 13장 11~14절') + '</b> 밤이 깊고 낮이 가까웠으니 어둠의 일을 벗고 빛의 갑옷을 입자는 말씀이에요. 용서의 주일 아침에 함께 읽어요.',
    '<b>' + bl('PSA.27', '시편 27편 1절') + '</b> 주님이 나의 빛이고 구원이시니 누구를 두려워하겠느냐는 노래예요. 옛 수도자들이 사막으로 떠나며 불렀어요.']},
  {'h': '직접 가 보기', 'checked': '2026년 11월 18일', 'img': ['mosaic'], 'p': [
    '서울 성 니콜라스 대성당(마포구 마포대로 18길 43)에서 용서 주일 오후에 참회의 만과를 드려요. 2027년 용서 주일은 3월 14일이에요(정교회 부활절 5월 2일로 계산).',
    '예배 시간은 해마다 달라질 수 있어요. 가기 전에 한국 정교회 누리집에서 그 주의 주보를 확인해 주세요.'],
   'links': [{'t': '한국 정교회 누리집 — 주보와 예배 안내', 'u': OKR, 'm': '한국어'},
             {'t': '2026년 용서 주일 주보(PDF) — 참회의 만과, 정결 월요일', 'u': JUBO, 'm': '한국어'},
             {'t': '미국 정교회: 슈메만 신부, 사순절의 시작 — 용서의 예식이 뜻하는 것', 'u': OCA, 'm': '영어'}]},
 ],
 'src': [
  {'l': '정교회 타임스(Orthodox Times): 용서의 주일 — 아담이 낙원에서 쫓겨난 일과 용서, 두 가지 주제 · 이날 읽는 로마서 13장 11절~14장 4절, 마태복음 6장 14~21절', 'u': OT},
  {'l': '미국 정교회(OCA): 치즈 주일 ‘주님, 제가 부르짖사오니’ 찬송 악보(PDF) — 낙원에서 쫓겨난 아담이 그 앞에 앉아 우는 노래', 'u': OCAPDF},
  {'l': '미국 정교회(OCA): 슈메만 신부, 사순절의 시작 — 저녁 예배에서 사순절을 알림, 큰 프로키메논, 사순절 가락, 성 에프렘의 기도와 엎드림, 서로 용서를 구함, 그동안 성가대가 부활절 노래를 부름, 용서는 사순절의 시작이자 바탕', 'u': OCA},
  {'l': '아즈부카 베리(Азбука веры): 용서의 주일 — 치즈 주일·아담의 쫓겨남, 저녁 예배 앞부분은 밝은 제의, 큰 프로키메논 뒤 제단 문을 닫고 사순절 제의로 갈아입음, 사제가 땅에 엎드려 먼저 용서를 청하는 말과 사람들의 대답, 모두가 서로 용서를 구함, 옛 수도원에서 부활절 노래를 부름, “하느님께서 용서하십니다”의 뜻', 'u': AZB},
  {'l': '오소독스위키: Forgiveness Sunday — 저녁 예배를 마친 뒤 한 사람씩 이콘에 입 맞추고 사제 앞에 엎드려 “죄인인 저를 용서해 주세요”, 사제도 엎드려 “하느님께서 용서하십니다. 저도 용서해 주세요”, 성가대는 부활절 노래를 나직이, 사람들끼리도 용서를 구함', 'u': OW},
  {'l': '러시아 정교회 미국 교구(2018): 뉴욕 성 니콜라스 대성당 용서의 예식 — 큰 프로키메논 뒤 밝은 제의를 어두운 빛으로 바꿈', 'u': MP},
  {'l': '민스크 성 엘리사벳 수도원 블로그(2018): 용서의 주일 — 제대보를 사순절 보라로, 사제는 어두운 제의로', 'u': 'https://catalog.obitel-minsk.com/blog/2018/02/forgivenes-sunday-as-our-guide-into'},
  {'l': '뉴 리터지컬 무브먼트(2018): 비잔틴 전례의 용서의 주일 — 밝은 제의와 제대보를 중간에 어두운 것으로 바꿈, 사제부터 모두가 서로에게, “하느님께서 우리 둘을 용서하시기를”, 곳마다 다름', 'u': NLM},
  {'l': '더 비잔틴 라이프: 용서의 저녁 예배 — 사제와 용서를 주고받은 사람이 사제 옆에 서서 줄을 이어 가는 교회들', 'u': BYZ},
  {'l': '포덤 대학교 중세 자료집: 『이집트의 마리아 전기』(소프로니오스, 조던빌 성삼위 수도원 옮김) — 사순절이 시작될 때 성찬, 조금 먹고 다시 모임, 엎드려 기도하고 서로 입 맞추며 용서를 구함, 원장의 축복, 시편을 부르며 요르단강을 건너 흩어짐, 한두 사람만 남음, 서로 묻지 않음, 종려 주일에 돌아옴', 'u': MARY},
  {'l': '미국 정교회(OCA): 사순절 다섯째 주일, 이집트의 성 마리아 — 사순절 첫 주일에 수도자들이 서로 용서를 구하고 사막으로 떠남, 조시마와 마리아', 'u': OCAMARY},
  {'l': '한국 정교회 주보 제2565호(2026년 2월 22일, PDF) — 용서 주일, “오늘 오후에 참회의 만과”, 사랑과 용서로 사순절을 시작하자, 다음 날 정결 월요일부터 사순절', 'u': JUBO},
  {'l': '서울신문(2007): 종교건축 이야기 — 성 니콜라스 서울대성당, 1968년 아현동 언덕에 세움, 한국에서 처음 세운 비잔틴 양식', 'u': SSN},
  {'l': '세계 총대주교청 한국 정교회 대교구 성 니콜라스 대성당: 2026년 성주간 예배 안내(PDF) — 대교구 이름', 'u': HW},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 35%', 'p1': '50% 55%', 's0': 1.25, 's1': 1.05, 'kicker': '사순절 바로 앞 일요일 · 정교회', 'title': '용서의 주일',
   'lines': [{'t': '정교회의 긴 사순절이 시작되기 전날이에요.'}, {'t': '사람들은 한 사람씩 “용서해 주세요”를 주고받아요.'}],
   'kid': [{'t': '긴 금식을 시작하기 전날이야.'}, {'t': '모두가 “용서해 줘” 하고 인사한대!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '낙원 문 앞의 아담'},
  {'type': 'img', 'ch': 1, 'img': 'hymnal', 'fit': 'cover', 'p0': '70% 60%', 'p1': '35% 40%', 's0': 1.35, 's1': 1.08, 'cap': '아르메니아 찬송집의 ‘낙원에서 쫓겨남’',
   'lines': [{'t': '같은 날, 교회는 아담이 낙원에서 쫓겨난 일을 기억해요.'},
             {'t': '예배의 노래는 낙원 앞에 앉아 우는 아담을 노래해요.'},
             {'t': '아침에는 용서하라는 말씀을 읽어요.'}],
   'kid': [{'t': '아담과 하와가 낙원 문 밖으로 나가고 있어.'}, {'t': '천사는 손에 무엇을 들고 있을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '강을 건너기 전에'},
  {'type': 'img', 'ch': 2, 'img': 'jordan', 'fit': 'cover', 'p0': '35% 55%', 'p1': '70% 70%', 's0': 1.2, 's1': 1.05, 'cap': '요르단강',
   'lines': [{'t': '옛 수도자들은 사순절이 시작될 때 서로 용서를 구했어요.'},
             {'t': '그리고 요르단강을 건너 사막으로 흩어졌어요.'},
             {'t': '종려 주일에야 돌아왔어요.'}],
   'kid': [{'t': '강을 건너기 전에 서로 “용서해 줘” 했대.'}, {'t': '먼 길 떠나기 전에 누구에게 인사할래?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '용서의 저녁 예배'},
  {'type': 'mod', 'mod': 'place', 'ch': 3,
   'lines': [{'t': '사제가 먼저 엎드려 “용서해 주세요” 해요.', 'act': 'priest', 'wait': 1200},
             {'t': '첫 사람이 나와 엎드려 절하며 용서를 구해요.', 'act': 'p1'},
             {'t': '“하느님께서 용서하십니다. 저도 용서해 주세요.”', 'act': 'p2', 'q': True, 'from': '서로 주고받는 말'},
             {'t': '한 사람씩, 줄이 길어져요.', 'act': 'p3'},
             {'t': '그동안 성가대는 부활절 노래를 나직이 불러요.', 'act': 'lights', 'wait': 1500},
             {'t': '사순절 첫 저녁이, 부활의 기쁨으로 밝아져요.', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '신부님이 먼저 “용서해 주세요” 해!', 'act': 'priest'},
           {'t': '“용서해 주세요” 하면 너는 뭐라고 대답할래?', 'act': 'p3', 'ask': True},
           {'t': '노래가 조용조용 들려.', 'act': 'lights'}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '서울의 용서 주일'},
  {'type': 'img', 'ch': 4, 'img': 'mosaic', 'fit': 'cover', 'p0': '50% 60%', 'p1': '50% 40%', 's0': 1.3, 's1': 1.05, 'cap': '서울 성 니콜라스 대성당의 모자이크',
   'lines': [{'t': '서울에서도 이날 오후 ‘참회의 만과’를 드려요.'},
             {'t': '다음 날은 정결 월요일, 사순절의 첫날이에요.'}],
   'kid': [{'t': '서울에도 이 예배를 드리는 성당이 있어.'}, {'t': '내일 새로 시작한다면, 누구에게 먼저 인사할래?', 'ask': True}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '촛불 몇 개만 남은 어스름한 성당이에요.'}, {'t': '낮은 목소리로 “용서해 주세요”가 오가요.'}, {'t': '부활절 노래가 작게, 아주 작게 흘러요.'}],
   'kid': [{'t': '눈을 감아 봐. 촛불이 깜빡.'}, {'t': '“용서해 줘.” “하느님도, 나도 용서해.”'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
