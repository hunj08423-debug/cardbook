# -*- coding: utf-8 -*-
"""깊은 카드: 루세카트(tb-lussekatt) · 중심 방식 = 놓아 보기(+두 그림 나란히)
기준서 1판 · 틀 deep3-3 · 키트 2판(보탬) · 2026-11-18 만들기 시작
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 12월 13일 새벽, 옛 달력으로 한 해 가장 긴 밤이 끝나 갈 때,
     깜깜한 부엌에서 S자 빵이 노랗게 구워져 나오는 순간
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 앞면 이야기에 적힌 만드는 차례 그대로
     (사프란 → 긴 막대 반죽 → 양 끝을 서로 반대로 말아 S자 → 건포도) 빚기. 다 빚으면 어둠 속에 노란 빵
카드 크기: 한 장면 카드 — 재료(그림 3장)가 한 장면에 몰려 있어요. 루치아 행렬·촛불은 3번 묶음 lig-lucia가 맡아 넣지 않았어요.
무대 그림은 이 카드 안의 stage_svg()로 이 안내서가 그렸어요(남의 그림을 따라 그리지 않음).
그림 원본(src)은 deep_src/tb-lussekatt/ (저장소 밖). 받는 법: commons_get.py"""
import math, random
S = 'tb-lussekatt/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

LIU = 'https://liu.se/en/article/lucia-celebrations-a-unique-tradition-with-ancient-roots'
NM = 'https://www.nordiskamuseet.se/en/traditions-celebrations/lucia/'
RM = 'https://www.rijksmuseum.nl/en/collection/SK-A-390'
AO = 'https://www.atlasobscura.com/articles/st-lucia-day-buns'
LOCAL = 'https://www.thelocal.se/20181212/swedishchristmas-why-lussekatter-are-one-hell-of-a-bun-dec12'
WC = 'https://commons.wikimedia.org/wiki/File:'
STEEN = 'Bakker_Arent_Oostwaard_en_zijn_vrouw_Catharina_Keizerswaard_SK-A-390.jpg'


def _spiral(cx, cy, r0, th0, turns=1.12, shrink=.74, n=90):
    pts = []
    tot = 2 * math.pi * turns
    for i in range(n + 1):
        s = tot * i / n
        r = r0 * (1 - shrink * s / tot)
        th = th0 - s
        pts.append((cx + r * math.cos(th), cy + r * math.sin(th)))
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)


def stage_svg():
    """12월 13일 새벽 전, 깜깜한 부엌의 빵 굽는 판. 이 안내서가 그림."""
    R = random.Random(1213)
    snow = ''.join(f'<circle cx="{R.uniform(60, 236):.0f}" cy="{R.uniform(66, 200):.0f}" r="{R.choice([1.2, 1.6, 2.0]):.1f}" fill="#fff" opacity="{R.uniform(.35, .8):.2f}"/>' for _ in range(26))
    L, Rr, R0 = (330, 402), (470, 402), 43
    left = _spiral(L[0], L[1] + R0, R0, -math.pi / 2)
    right = _spiral(Rr[0], Rr[1] - R0, R0, math.pi / 2)
    mid = f'M{L[0]} {L[1]} L{Rr[0]} {Rr[1]}'
    dough = 'stroke="#f2dfae" stroke-width="31" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    edge = 'stroke="#d8bf84" stroke-width="35" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    gold = 'stroke="#e9a623" stroke-width="31" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    goldedge = 'stroke="#b8741a" stroke-width="35" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    shine = 'stroke="#ffd36a" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" fill="none" opacity=".7"'
    cl = (L[0], L[1] + R0); cr = (Rr[0], Rr[1] - R0)
    return f'''<svg class="stage" viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice" role="img" aria-label="눈 내리는 창가의 깜깜한 부엌, 빵 굽는 판. 반죽을 하나씩 빚으면 S자 빵이 된다."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1119"/><stop offset="1" stop-color="#1a1714"/></linearGradient>
<linearGradient id="__U__night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#050812"/><stop offset="1" stop-color="#121b33"/></linearGradient>
<linearGradient id="__U__dawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#34446e"/><stop offset=".6" stop-color="#8a7aa0"/><stop offset="1" stop-color="#e9b48a"/></linearGradient>
<linearGradient id="__U__table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a3424"/><stop offset="1" stop-color="#2c1f15"/></linearGradient>
<radialGradient id="__U__oven" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffb35c" stop-opacity=".85"/><stop offset=".5" stop-color="#e0702a" stop-opacity=".3"/><stop offset="1" stop-color="#a03c10" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__warm" cx=".5" cy=".55" r=".6"><stop offset="0" stop-color="#ffd27a" stop-opacity=".85"/><stop offset=".5" stop-color="#f0a23a" stop-opacity=".35"/><stop offset="1" stop-color="#5a2f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".6" r=".8"><stop offset="0" stop-color="#ffe9a8" stop-opacity=".75"/><stop offset=".5" stop-color="#ffc861" stop-opacity=".35"/><stop offset="1" stop-color="#ffab3c" stop-opacity="0"/></radialGradient></defs>
<rect width="800" height="600" fill="url(#__U__wall)"/>
<g><rect x="56" y="62" width="188" height="142" rx="6" fill="url(#__U__night)"/><rect class="sky2" x="56" y="62" width="188" height="142" rx="6" fill="url(#__U__dawn)"/>{snow}
<path d="M56 182 C 100 170 150 186 244 174 L244 204 L56 204Z" fill="#dfe6f0" opacity=".85"/><path d="M150 62 V204 M56 133 H244" stroke="#241a14" stroke-width="7"/><rect x="56" y="62" width="188" height="142" rx="6" fill="none" stroke="#241a14" stroke-width="9"/></g>
<g><rect x="588" y="96" width="170" height="196" rx="10" fill="#1d1a1a" stroke="#352c27" stroke-width="4"/><rect x="616" y="196" width="114" height="62" rx="8" fill="#140c08" stroke="#3b2d24" stroke-width="3"/><ellipse cx="673" cy="230" rx="78" ry="44" fill="url(#__U__oven)"/><rect x="604" y="122" width="138" height="10" rx="4" fill="#2e2622"/></g>
<path d="M0 300 L800 300 L800 600 L0 600Z" fill="url(#__U__table)"/>
<path d="M0 300 L800 300" stroke="#6a4a30" stroke-width="3"/>
<path class="glow" d="M150 300 C 260 250 540 250 650 300 L740 600 L60 600Z" fill="url(#__U__warm)" opacity=".14"/>
<g><rect x="190" y="292" width="420" height="232" rx="16" fill="#2b2a2e" stroke="#4a4950" stroke-width="5"/><rect x="206" y="306" width="388" height="204" rx="8" fill="#ece0c4" opacity=".9"/></g>
<g class="obj" data-o="saffron"><ellipse cx="142" cy="452" rx="44" ry="12" fill="#6c5640"/><path d="M100 420 C 100 452 184 452 184 420Z" fill="#8a7458"/><ellipse cx="142" cy="420" rx="42" ry="11" fill="#f2b21e"/><g stroke="#b5230e" stroke-width="1.8" stroke-linecap="round" fill="none"><path d="M118 419 q5 -3 9 1"/><path d="M138 414 q4 4 9 2"/><path d="M156 421 q3 -4 8 -3"/><path d="M131 425 q2 -3 6 -2"/><path d="M148 427 q4 -2 6 1"/></g></g>
<g class="obj" data-o="dough"><path d="{mid}" {edge}/><path d="{mid}" {dough}/></g>
<g class="obj" data-o="left"><path d="{left}" {edge}/><path d="{left}" {dough}/></g>
<g class="obj" data-o="right"><path d="{right}" {edge}/><path d="{right}" {dough}/></g>
<g class="day"><path d="{left}" {goldedge}/><path d="{right}" {goldedge}/><path d="{mid}" {goldedge}/><path d="{left}" {gold}/><path d="{right}" {gold}/><path d="{mid}" {gold}/><path d="{left}" {shine}/><path d="{right}" {shine}/><path d="{mid}" {shine}/></g>
<g class="obj" data-o="raisins"><ellipse cx="{cl[0]}" cy="{cl[1]}" rx="9" ry="7.5" fill="#2a1022"/><ellipse cx="{cl[0] - 2}" cy="{cl[1] - 2}" rx="3" ry="2" fill="#6a3a54" opacity=".8"/><ellipse cx="{cr[0]}" cy="{cr[1]}" rx="9" ry="7.5" fill="#2a1022"/><ellipse cx="{cr[0] - 2}" cy="{cr[1] - 2}" rx="3" ry="2" fill="#6a3a54" opacity=".8"/></g>
<rect class="day" width="800" height="600" fill="url(#__U__day)"/>
</svg>'''


ITEMS = [
 {'id': 'saffron', 't': '사프란', 'la': 'saffran', 'say': '사프란을 빻아 녹인 버터에 넣고 우려요. 반죽이 노랗게 물들어요.'},
 {'id': 'dough', 't': '긴 막대 반죽', 'la': 'deg', 'say': '노래진 반죽을 손으로 굴려 양 끝이 가는 긴 막대로 밀어요.'},
 {'id': 'left', 't': '한쪽 끝 말기', 'la': '', 'say': '한쪽 끝을 안쪽으로 납작하게 둥글게 말아요.'},
 {'id': 'right', 't': '다른 쪽 끝 말기', 'la': '', 'say': '다른 쪽 끝은 반대 방향으로 말아요. S자가 되었어요.'},
 {'id': 'raisins', 't': '건포도', 'la': 'russin', 'say': '둥글게 말린 자리마다 건포도를 하나씩 콕 박아요.'},
]

CARD = {
 'id': 'tb-lussekatt', 'mode': '놓아 보기 · 두 그림 나란히',
 'pagetitle': "루세카트",
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>12월 13일 새벽</b><span>스웨덴 · 옛 달력으로 가장 긴 밤이 끝나 갈 때</span>',
 'lead': '스웨덴이 옛 달력을 쓰던 때, 12월 13일로 넘어가는 밤은 한 해에서 가장 긴 밤이었어요. 그 밤의 끝, 깜깜한 부엌에서 노란 S자 빵을 하나씩 빚어 보세요.',
 'leadKid': '옛날 스웨덴에서는 12월 13일 밤이 일 년 중 가장 긴 밤이었대. 깜깜한 부엌에서 노란 빵을 같이 빚어 볼까?',
 'meta': '영화처럼 약 2분 · 천천히 읽으면 4분',
 'draft': '검수 전 시안이에요(기준서 1판). 그 밤과 빵의 이름은 스웨덴 노르디스카 박물관과 린셰핑 대학 자료를, 1658년 그림은 레이크스 미술관 설명을 따랐어요. 만드는 차례는 앞면 이야기의 차례 그대로이고, 무대 그림은 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 2분',
 'theme': """:root{--accent:#8f6200;--accent-ink:#fffaf5;--soft:rgba(143,98,0,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#c5ad7a;--accent-ink:#17120a;--soft:rgba(197,173,122,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#c5ad7a;--accent-ink:#17120a;--soft:rgba(197,173,122,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '사프란', 'y': '12·13', 'sub': '스웨덴'},
 'doneNote': '12월 13일 아침, 노란 빵 하나를 이웃과 나눠 보세요.',
 'images': {
  'bun': {'src': S + 'Saffron_bun_20051213_001.jpg',
          'cap': '루세카트, 2005년 12월 13일 스웨덴에서 찍음',
          'cr': '사진: Jonas Bergsten · 퍼블릭 도메인 · 위키미디어 공용',
          'u': WC + 'Saffron_bun_20051213_001.jpg',
          'alt': '하얀 바탕 위의 노란 빵 하나. 양 끝을 반대로 말아 S자를 이루었고, 둥글게 말린 두 자리에 검은 건포도가 박혀 있다.'},
  'steen': {'src': S + STEEN,
            'cap': '얀 스테인, 「빵집 부부 아렌트 오스트바르트와 카타리나 케이저르스바르트」, 1658년(레이크스 미술관)',
            'cr': '그림: 얀 스테인(Jan Steen) · 퍼블릭 도메인 · 위키미디어 공용(레이크스 미술관)',
            'u': WC + 'Bakker_Arent_Oostwaard_en_zijn_vrouw_Catharina_Keizerswaard,_SK-A-390.jpg',
            'alt': '빵집 앞. 흰 모자를 쓴 빵집 주인이 웃으며 빵 판을 들고, 왼쪽 창가의 아내가 둥근 빵을 들어 보인다. 위에는 매듭 모양 빵이 줄줄이 매달려 있고, 탁자에는 여러 빵과 함께 길쭉한 빵 하나가 세워져 있다.'},
  'steen_d': {'src': S + STEEN, 'crop': (0.28, 0.33, 0.50, 0.66),
              'cap': '같은 그림의 부분: 세워 놓은 다위베카터, 1658년',
              'cr': '그림: 얀 스테인 · 퍼블릭 도메인 · 위키미디어 공용(레이크스 미술관)',
              'u': WC + 'Bakker_Arent_Oostwaard_en_zijn_vrouw_Catharina_Keizerswaard,_SK-A-390.jpg',
              'alt': '벽에 기대 세운 길쭉한 빵. 가장자리가 물결처럼 오돌토돌하고, 위쪽 끝이 둥글게 말려 있다. 옆에 둥근 빵이 하나 서 있다.'},
  'saffron': {'src': S + 'Crocus_sativus_saffron_4.jpg',
              'cap': '사프란: 크로커스꽃의 붉은 암술을 말린 것, 2007년 프랑스',
              'cr': '사진: Emilie40 · 퍼블릭 도메인 · 위키미디어 공용',
              'u': WC + 'Crocus_sativus,_saffron_(4).jpg',
              'alt': '노란 천 위에 가늘고 붉은 실 같은 사프란 암술 여러 가닥이 놓여 있다.'},
 },
 'extra_credits': [{'cr': '놓아 보기 무대: 이 안내서가 그린 12월 13일 새벽의 부엌 · 앞면 이야기의 만드는 차례와 노르디스카 박물관 자료를 바탕으로', 'u': NM}],
 'scenes': [
  {'id': 'night', 'label': '가장 긴 밤, 노란 빵', 'kind': 'mod', 'mod': 'place', 'night': True,
   'text': ['스웨덴이 옛 율리우스력을 쓰던 1753년까지, 한 해에서 가장 긴 밤은 12월 12일에서 13일로 넘어가는 밤이었어요. 13일은 ‘빛’을 뜻하는 라틴말 룩스(lux)에서 이름이 온 루치아 성인의 날이에요.',
            '옛 농가 사람들은 이 밤에 나쁜 힘이 날뛴다고 믿었어요. 그래서 밤새 깨어 집과 짐승을 지키기도 했어요.',
            '그 밤이 끝나 갈 무렵, 깜깜한 부엌에서 노란 빵을 빚어 보세요. 앞면 이야기에 적힌 차례 그대로예요.'],
   'text2': ['스웨덴 노르디스카 박물관에 따르면, 이 빵에 사프란을 넣기 시작한 것은 19세기 끝 무렵이에요. 지금은 S자 모양이 가장 흔해요.'],
   'kid': '옛날 스웨덴에서는 12월 13일 밤이 일 년 중 가장 긴 밤이었대. 깜깜한 부엌에서 노란 빵을 빚어 볼까?',
   'kidq': '가장 긴 밤에 노란 빵이 구워져 나오면 어떤 기분일까?'},
  {'id': 'name', 'label': '이름의 수수께끼', 'kind': 'duo', 'imgs': ['steen_d', 'bun'],
   'caps': ['얀 스테인 그림 속 다위베카터(부분), 1658년', '오늘의 루세카트, 2005년'],
   'text': ['루세카트는 ‘루치아의 고양이’라는 뜻이에요. 하지만 노르디스카 박물관은 이 빵이 네덜란드와 북독일의 단 밀빵 다위베카터(duivekater)에서 왔다고 설명해요. 17세기에 네덜란드 사람들이 예테보리로 가져왔을 거래요.',
            '스웨덴 사람들 귀에 그 이름은 ‘디벨스카테르’, 곧 ‘악마의 고양이’처럼 들렸어요. 빵이 12월 13일과 이어지면서 이름이 루세카테르로 바뀌었어요.'],
   'text2': ['1658년 네덜란드 화가 얀 스테인이 그린 레이던의 빵집 앞에도 다위베카터가 있어요. 레이크스 미술관은 여러 빵 가운데 세워 놓은 다위베카터가 눈에 띄는 자리를 차지한다고 설명해요.'],
   'kid': '루세카트는 ‘루치아의 고양이’라는 뜻이야. 그런데 고양이랑은 상관없고, 네덜란드 빵 이름에서 왔대!',
   'kidq': '두 빵을 견주어 봐. 어디가 닮았고 어디가 달라?'},
 ],
 'imagine': {'t': '창밖에는 눈이 쌓이고, 한 해에서 가장 긴 밤이 이제 끝나 가요. 화덕 불빛만 붉은 부엌, 녹인 버터에서 번지는 사프란 향, 손바닥 아래 말랑한 반죽. 판 위에 노란 S자가 하나둘 늘어 가면, 어둠 속에 작은 해가 여럿 뜬 것 같아요.',
             'kid': '눈을 감아 봐. 창밖엔 하얀 눈, 부엌은 깜깜해. 화덕만 빨갛게 빛나. 노란 반죽을 돌돌 말아 S자! 건포도 콕! 어둠 속에 작은 해가 떴어!'},
 'lines': ['가장 긴 밤 끝에 노란 빵.', '어둠 속에 작은 해 하나.', '이름은 바다를 건너 바뀌었어요.'],
 'linesKid': ['돌돌 말아 S자!', '건포도 콕!'],
 'goals': {
  's4': {'t': '차례대로 빚기', 'p': '사프란 → 긴 막대 → 양 끝을 서로 반대로 말기 → 건포도 차례로 다 빚으면 카드에 금박이 입혀져요.',
         'how': '앞면 이야기의 차례대로 S자 빵을 다 빚어 보세요', 'done': '차례대로 노란 빵을 빚었어요',
         'ways': [{'id': 'plOrder', 't': '사프란 → 긴 막대 → 한쪽 끝 → 다른 쪽 끝 → 건포도 차례로 빚기'}]},
  's5': {'t': '가장 긴 밤의 끝', 'p': '아이와 함께 끝까지 보면 카드가 채색돼요.',
         'how': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'done': '가장 긴 밤의 끝을 함께 봤어요',
         'ways': [{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'place': {
   'items': ITEMS, 'order': '사프란, 긴 막대 반죽, 한쪽 끝 말기, 다른 쪽 끝 말기, 건포도',
   'intro': '아래에서 하나씩 골라 빵 판 위에서 빚어 보세요. 차례는 사프란, 긴 막대 반죽, 한쪽 끝 말기, 다른 쪽 끝 말기, 건포도예요.',
   'climax': '가장 긴 밤의 끝, 깜깜한 부엌에서 노란 빵이 구워져 나왔어요.<span class="la">lussekatt · 12월 13일 루치아의 날</span>',
   'home': None,
   'wrongOrder': '앞면 이야기에 적힌 만드는 차례는 이래요: {order}',
   'orderDone': '차례대로 다 빚었어요',
   'daylight': False,
   'svg': stage_svg()}},
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="빚을 차례 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 빚어 보기</button></div>
  <div class="pl-home" hidden><p>우리 집이라면?</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'img': ['saffron'], 'p': [
    '<b>사프란</b> 크로커스꽃의 붉은 암술을 말린 향신료예요. 빵을 노랗게 물들여요.',
    '<b>루치아의 날</b> 스웨덴의 가톨릭 달력에서는 16세기까지 12월 13일을 루치아 성인의 날로 지켰어요.',
    '<b>다위베카터</b> 네덜란드와 북독일의 단 밀빵이에요. 네덜란드 말로 ‘악마의 수고양이’ 또는 ‘악마의 과자’로 풀이되지만, 이름이 어디서 왔는지는 학자들도 확실히 몰라요.']},
  {'h': '그림 속 빵집', 'img': ['steen'], 'p': [
    '레이던의 빵집 주인 아렌트 오스트바르트와 아내 카타리나예요. 가게 앞에 작은 빵, 매듭 빵 크라켈링, 카데트, 다위베카터가 놓여 있고, 간판 자리에는 크라켈링이 매달려 있어요.',
    '레이크스 미술관 설명에 따르면, 빵이 나왔다고 뿔피리를 불어 알리는 아이는 화가의 아들 타데우스로, 1658년에 일곱 살쯤이었어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>사프란은 언제부터?</b> 노르디스카 박물관은 이 빵에 사프란을 넣은 때를 19세기 끝 무렵으로 봐요. 이 박물관의 큐레이터였던 레나 케트스트룀 회크는, 스웨덴에서 사프란 빵이 1600년대에 이미 귀한 빵이 되어 이름난 사람의 장례 잔치에 오르곤 했고, 1800년대에 들어서야 여러 사람이 먹게 되었다고 썼어요.',
    '<b>악마의 고양이?</b> 옛 이름 때문에 무서운 이야기가 붙곤 해요. 하지만 케트스트룀 회크는 이 이름이 고양이와는 아무 상관이 없다고 말해요.']},
  {'h': '집에서 빚어 보기', 'p': [
    '사프란을 빻아 녹인 버터에 넣고 15분쯤 우려 반죽에 섞어요. 반죽을 양 끝이 가는 막대로 밀고, 한쪽 끝을 납작하게 말고 다른 쪽 끝은 반대로 말아 S자를 만들어요. 달걀물을 바르고, 말린 자리마다 건포도를 하나씩 박아 구워요.'],
   'links': [{'t': '노르디스카 박물관: 루치아 풍습과 루세카트 이름 이야기', 'u': NM, 'm': '영어'},
             {'t': '레이크스 미술관: 얀 스테인의 빵집 부부 그림 크게 보기', 'u': RM, 'm': '영어'},
             {'t': '아틀라스 옵스큐라: 루세카트 이름 이야기와 만드는 법', 'u': AO, 'm': '영어'}]},
 ],
 'src': [
  {'l': '린셰핑 대학, 「루치아 축하: 오래된 뿌리를 가진 특별한 전통」 — 율리우스력에서 12월 12~13일 밤이 가장 긴 밤, 1753년, 라틴말 lux, 나쁜 힘을 막으려 밤새 지킴', 'u': LIU},
  {'l': '노르디스카 박물관 「Lucia」 — 다위베카터가 17세기 예테보리로, 디벨스카테르, 루세카테르로 이름이 바뀜, S자, 19세기 끝 무렵 사프란, 16세기까지 가톨릭 달력의 루치아 날', 'u': NM},
  {'l': '레이크스 미술관 SK-A-390 — 얀 스테인(1658), 빵들(작은 빵·크라켈링·카데트·다위베카터), 세운 다위베카터, 뿔피리 부는 아들 타데우스', 'u': RM},
  {'l': '아틀라스 옵스큐라 「Detangling the Devilish Origins of Scandinavia’s St. Lucia Buns」 — 레나 케트스트룀 회크: 고양이와 상관없음, 다위베카터의 뜻, 만드는 법', 'u': AO},
  {'l': '더 로컬 스웨덴(2018.12.12) — 케트스트룀 회크의 책 『God Jul!』: 1600년대 귀한 사프란 빵, 장례 잔치, 1800년대에 널리', 'u': LOCAL},
  {'l': '위키미디어 공용: 사프란(크로커스 사티부스) 사진 정보', 'u': WC + 'Crocus_sativus,_saffron_(4).jpg'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'bun', 'fit': 'cover', 'p0': '45% 50%', 'p1': '55% 50%', 's0': 1.2, 's1': 1.05, 'kicker': '12월 13일 · 스웨덴', 'title': "루세카트",
   'lines': [{'t': '12월 13일, 스웨덴의 노란 빵 루세카트.'}, {'t': '옛 달력으로 한 해 가장 긴 밤이 끝나는 날이에요.'}],
   'kid': [{'t': '노랗게 구운 S자 빵이야.'}, {'t': '일 년 중 가장 긴 밤이 끝나는 날에 먹었대.'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '가장 긴 밤'},
  {'type': 'mod', 'mod': 'place', 'ch': 1,
   'lines': [{'t': '1753년까지 스웨덴에서 가장 긴 밤은 12월 13일로 넘어가는 밤이었어요.'},
             {'t': '사프란을 녹인 버터에 우리고,', 'act': 'saffron'}, {'t': '노란 반죽을 길게 밀어요.', 'act': 'dough'},
             {'t': '한쪽 끝을 말고,', 'act': 'left'}, {'t': '다른 쪽 끝은 반대로 말아요.', 'act': 'right'},
             {'t': '말린 자리에 건포도를 콕.', 'act': 'raisins', 'wait': 1200},
             {'t': '가장 긴 밤의 끝, 노란 빵이 구워져 나와요.', 'act': 'day', 'wait': 1800}],
   'kid': [{'t': '깜깜한 밤 부엌이야.'},
           {'t': '사프란!', 'act': 'saffron'}, {'t': '길게 쭉!', 'act': 'dough'},
           {'t': '돌돌!', 'act': 'left'}, {'t': '반대로 돌돌!', 'act': 'right'}, {'t': '건포도 콕!', 'act': 'raisins'},
           {'t': '노란 빵이 나왔어! 누구에게 주고 싶어?', 'act': 'day', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '이름의 수수께끼'},
  {'type': 'img', 'ch': 2, 'img': 'steen', 'fit': 'contain', 'p0': '50% 40%', 'p1': '38% 45%', 's0': 1.0, 's1': 1.35, 'cap': '얀 스테인의 빵집 부부, 1658년',
   'lines': [{'t': '1658년 네덜란드 레이던의 빵집.'}, {'t': '세워 놓은 길쭉한 빵, 다위베카터가 보여요.'}, {'t': '이 빵이 바다를 건너 스웨덴의 루세카트가 되었다고 해요.'}],
   'kid': [{'t': '옛날 네덜란드 빵집이야. 길쭉한 빵이 서 있지?'}, {'t': '루세카트랑 어디가 닮았을까?', 'ask': True}]},
  {'type': 'imagine', 'ch': 3,
   'lines': [{'t': '창밖에는 눈, 가장 긴 밤이 끝나 가요.'}, {'t': '화덕 불빛, 사프란 향, 말랑한 반죽.'}, {'t': '어둠 속에 작은 해가 여럿 뜬 것 같아요.'}],
   'kid': [{'t': '눈을 감아 봐. 창밖엔 하얀 눈이 와.'}, {'t': '노란 S자 빵이 작은 해처럼 반짝여!'}]},
  {'type': 'reward', 'ch': 3},
 ],
}
