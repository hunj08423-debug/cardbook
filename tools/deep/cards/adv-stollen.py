# -*- coding: utf-8 -*-
"""깊은 카드: 드레스덴 슈톨렌(adv-stollen) · 중심 방식 = 놓아 보기(+두 그림 나란히, 고르기)
기준서 1판 · 틀 deep3-3 · 키트 2판(보탬 2026-11-18, 품질 85로 다시 빌드) · 2026-11-18 1번 묶음 창이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 갓 구운 슈톨렌에 녹인 버터를 바르고 흰 설탕을 덮어 하얗게 감싸이는 순간.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 금식 때 못 쓰던 버터(‘버터 편지’)와, 구운 뒤 덮는 흰 설탕 —
     유럽연합 보호 지리적 표시 소개에 적힌 만드는 차례대로 재료를 하나씩 놓아요.
카드 크기: 한 장면 카드(장면 2) — 옛 그림은 1730년 동판화 한 장(작은 파일)뿐이에요.
사용자 의견(2026-11-18): ‘흰 포대기’ 풀이는 누가 하는지 밝힐 것 → epd·deutschland.de로 밝히고, 처음 푼 사람은 확인되지 않는다고 적음.
  1730년 판화는 작아서(500px) 두 그림 나란히(duo)에만 작게 쓰고, 영화에는 쓰지 않음.
놓아 보기의 ‘우리 집 고르기’ 칸은 쓰지 않아요('home': None, 키트 2판 보탬). 5단계는 ‘고르기(choose)’를 써요.
무대 그림은 이 파일의 stage_svg()로 이 안내서가 그림.
그림 원본(src)은 deep_src/adv-stollen/ (저장소 밖). messer_crop.jpg는 칼 사진에서 얼굴이 나오지 않게 가운데만 잘라 둔 것."""
import random
S = 'adv-stollen/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

EU = 'https://agriculture.ec.europa.eu/farming/geographical-indications-and-quality-schemes/geographical-indications-food-and-drink/dresdner-christsollen-pgi_en'
ATLAS = 'https://www.atlasobscura.com/articles/dresden-stollen'
EPD = 'https://www.evangelisch.de/inhalte/249878/23-11-2025/traditionshandwerk-christstollen'
DDE = 'https://www.deutschland.de/de/topic/leben/lifestyle-kulinarik/weihnachtsklassiker-christstollen'

def stage_svg():
    """슈톨렌 만들기 무대(800×450). 놓을 것마다 data-o 무리. 마지막에 창밖이 밝아져요(.sky2, .day)."""
    R = random.Random(1474)
    def on_loaf():
        while True:
            x = R.uniform(286, 514); y = R.uniform(252, 306)
            t = (x - 400) / 132
            if abs(t) < 0.95 and y > 314 - 74 * (1 - t * t) + 7: return x, y
    raisins = ''.join(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="4.4" ry="3.1" fill="#3a1e12" transform="rotate({R.uniform(-40, 40):.0f} {x:.0f} {y:.0f})"/>' for x, y in [on_loaf() for _ in range(24)])
    peel = ''.join(f'<rect x="{x - 3:.0f}" y="{y - 3:.0f}" width="6.5" height="5" rx="1" fill="{R.choice(["#e98a2a", "#f0a23c", "#a9c255", "#c8d36a"])}"/>' for x, y in [on_loaf() for _ in range(16)])
    almonds = ''.join(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="6.4" ry="2.7" fill="#f4e4c6" stroke="#c49a63" stroke-width="0.9" transform="rotate({R.uniform(-60, 60):.0f} {x:.0f} {y:.0f})"/>' for x, y in [on_loaf() for _ in range(12)])
    dust = ''.join(f'<circle cx="{R.uniform(196, 604):.0f}" cy="{R.uniform(318, 372):.0f}" r="{R.uniform(0.8, 2.1):.1f}" fill="#fff" opacity="{R.uniform(.45, .95):.2f}"/>' for _ in range(80))
    flakes = ''.join(f'<circle cx="{R.uniform(270, 530):.0f}" cy="{R.uniform(200, 236):.0f}" r="{R.uniform(0.8, 1.8):.1f}" fill="#fff" opacity="{R.uniform(.4, .9):.2f}"/>' for _ in range(26))
    grain = ''.join(f'<path d="M{x0:.0f} {y:.0f} C {x0 + 120:.0f} {y + R.uniform(-3, 3):.0f} {x0 + 260:.0f} {y + R.uniform(-3, 3):.0f} {x0 + 420:.0f} {y + R.uniform(-2, 2):.0f}" stroke="#5a3820" stroke-width="1" fill="none" opacity=".35"/>' for x0, y in [(R.uniform(182, 200), R.uniform(326, 376)) for _ in range(9)])
    loaf = 'M266 316 C 268 270 330 242 400 242 C 470 242 532 270 534 316 C 500 325 300 325 266 316 Z'
    coat = 'M259 318 C 261 264 328 234 400 234 C 472 234 539 264 541 318 C 505 329 295 329 259 318 Z'
    fold = 'M298 302 C 332 268 414 255 502 272'
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="나무 판 위에 슈톨렌 재료가 하나씩 놓이고, 마지막에 흰 설탕이 빵을 덮는다."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c130d"/><stop offset="1" stop-color="#30211a"/></linearGradient>
<linearGradient id="__U__sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d2740"/><stop offset="1" stop-color="#3a3a52"/></linearGradient>
<linearGradient id="__U__sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bcd3ee"/><stop offset=".7" stop-color="#f3dcb2"/><stop offset="1" stop-color="#ffd9a0"/></linearGradient>
<linearGradient id="__U__board" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a06b3c"/><stop offset="1" stop-color="#7a4d2a"/></linearGradient>
<linearGradient id="__U__loaf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e6b874"/><stop offset=".55" stop-color="#cf9452"/><stop offset="1" stop-color="#a8692f"/></linearGradient>
<linearGradient id="__U__coat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".7" stop-color="#f4f2ee"/><stop offset="1" stop-color="#dcdde3"/></linearGradient>
<radialGradient id="__U__glow" cx=".5" cy=".62" r=".55"><stop offset="0" stop-color="#ffcf86" stop-opacity=".9"/><stop offset=".5" stop-color="#d9893c" stop-opacity=".35"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".25" cy=".25" r=".95"><stop offset="0" stop-color="#fff3d4" stop-opacity=".7"/><stop offset=".5" stop-color="#ffd59a" stop-opacity=".28"/><stop offset="1" stop-color="#ffb35c" stop-opacity="0"/></radialGradient></defs>
<rect width="800" height="450" fill="url(#__U__wall)"/>
<rect x="96" y="44" width="150" height="128" rx="4" fill="url(#__U__sky)"/><rect class="sky2" x="96" y="44" width="150" height="128" rx="4" fill="url(#__U__sky2)"/>
<g fill="none" stroke="#5b4030" stroke-width="7"><rect x="96" y="44" width="150" height="128" rx="4"/><line x1="171" y1="44" x2="171" y2="172"/><line x1="96" y1="108" x2="246" y2="108"/></g>
<rect x="88" y="170" width="166" height="9" rx="2" fill="#5b4030"/>
<ellipse class="glow" cx="400" cy="300" rx="300" ry="150" fill="url(#__U__glow)" opacity=".14"/>
<rect x="0" y="336" width="800" height="114" fill="#3b2618"/><rect x="0" y="336" width="800" height="5" fill="#4b3121"/>
<rect x="176" y="300" width="448" height="84" rx="12" fill="url(#__U__board)"/>{grain}
<rect x="176" y="376" width="448" height="8" rx="4" fill="#5d3a1f" opacity=".7"/>
<g class="obj" data-o="dough"><path d="{loaf}" fill="url(#__U__loaf)" stroke="#7a4a22" stroke-width="2"/><path d="{fold}" fill="none" stroke="#8a5428" stroke-width="3" stroke-linecap="round" opacity=".8"/></g>
<g class="obj" data-o="butter"><path d="M196 318 L 236 306 L 266 316 L 226 330 Z" fill="#fbe9a3"/><path d="M196 318 L 226 330 L 226 348 L 196 336 Z" fill="#efcf63"/><path d="M226 330 L 266 316 L 266 334 L 226 348 Z" fill="#e4bf4c"/><ellipse cx="392" cy="262" rx="88" ry="14" fill="#fff6c4" opacity=".28"/></g>
<g class="obj" data-o="fruit">{raisins}{peel}</g>
<g class="obj" data-o="almond">{almonds}</g>
<g class="obj" data-o="sugar"><path d="{coat}" fill="url(#__U__coat)" stroke="#c9ccd6" stroke-width="1.5"/><path d="{fold}" fill="none" stroke="#d7d9e1" stroke-width="3" stroke-linecap="round"/>{dust}{flakes}</g>
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''

ITEMS = [
 {'id': 'dough', 't': '반죽', 'la': 'Mehl · Hefe · Milch', 'say': '밀가루와 효모, 우유로 묵직한 반죽을 만들어요. 1474년 첫 기록의 슈톨렌은 밀가루와 효모에 물만 더한 금식 빵이었어요.'},
 {'id': 'butter', 't': '버터', 'la': 'Butter', 'say': '버터를 넣어요. 대림절 금식 때는 쓸 수 없던 재료예요. 교황의 ‘버터 편지’가 이 일을 허락했어요.'},
 {'id': 'fruit', 't': '건포도와 과일 껍질', 'la': 'Sultaninen · Zitronat · Orangeat', 'say': '건포도와, 설탕에 절인 레몬·오렌지 껍질을 반죽에 고루 넣어요.'},
 {'id': 'almond', 't': '아몬드', 'la': 'Mandeln', 'say': '단 아몬드와 쌉쌀한 아몬드를 넣고 손으로 길쭉하게 빚어 구워요. 드레스덴 슈톨렌은 틀에 넣지 않고 손으로 빚어요.'},
 {'id': 'sugar', 't': '버터와 흰 설탕', 'la': 'Butter · Puderzucker', 'say': '갓 구운 빵에 녹인 버터를 바르고, 흰 설탕을 듬뿍 덮어요.'},
]

CARD = {
 'id': 'adv-stollen', 'mode': '놓아 보기 · 고르기',
 'pagetitle': "드레스덴 슈톨렌",
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>1474년 · 1490년 · 1730년</b><span>독일 드레스덴</span>',
 'lead': '독일 드레스덴의 성탄 빵 슈톨렌은 원래 대림절 금식 때 먹던 소박한 빵이었어요. 버터를 넣을 수 있게 된 것은 교황이 보낸 ‘버터 편지’ 덕분이었어요. 재료를 하나씩 넣고, 마지막에 흰 설탕을 덮어 보세요.',
 'leadKid': '하얀 가루를 덮은 성탄 빵이야. 옛날엔 이 빵에 버터를 넣을 수 없었대! 재료를 하나씩 넣어서 같이 만들어 볼까?',
 'meta': '영화처럼 약 2분 · 천천히 읽으면 4분',
 'draft': '검수 전 시안이에요(기준서 1판). 장면에는 기록에 있는 것만 옮겼고, 빵 모양의 뜻풀이는 누가 그렇게 소개하는지 밝혔어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요. 재료를 놓는 부엌 무대 그림은 이 안내서가 그렸어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 얼굴이 나오는 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 2분',
 'theme': """:root{--accent:#7A5230;--accent-ink:#fffaf5;--soft:rgba(122,82,48,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#baa593;--accent-ink:#14100c;--soft:rgba(186,165,147,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#baa593;--accent-ink:#14100c;--soft:rgba(186,165,147,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '슈톨렌', 'y': '1474', 'sub': '드레스덴 · 독일'},
 'doneNote': '올 대림절, 슈톨렌 한 조각을 누군가와 나눠 보세요.',
 'images': {
  'card': {'src': S + 'Stollen-Dresdner_Christstollen.jpg', 'cap': '드레스덴의 크리스트슈톨렌', 'cr': '사진: Gürgi · 퍼블릭 도메인 · 위키미디어 공용',
           'u': 'https://commons.wikimedia.org/wiki/File:Stollen-Dresdner_Christstollen.jpg',
           'alt': '하얀 설탕 가루를 뿌린 슈톨렌과 자른 조각이 나무 도마에 놓여 있고, 뒤에 눈 덮인 드레스덴 거리가 그려진 ‘Christstollen’ 상자가 있다.'},
  'riesen': {'src': S + 'Zeithainer_Riesenstollen.jpg', 'cap': '1730년 거대한 슈톨렌을 기념한 채색 동판화(엘리아스 베크)',
             'cr': '판화: 엘리아스 베크 · 퍼블릭 도메인 · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:Zeithainer_Riesenstollen.jpg',
             'alt': '푸른빛으로 찍힌 옛 판화. 가운데 커다란 화덕 건물이 있고, 아래쪽에서 말 여덟 마리가 길쭉한 슈톨렌을 실은 수레를 끈다. 왼쪽 위에는 천사가 펼친 천에 화덕 설계도가 그려져 있고, 맨 아래에 긴 독일어 설명 글이 있다.'},
  'messer': {'src': S + 'messer_crop.jpg', 'cap': '1730년의 칼을 본떠 만든 ‘드레스덴 슈톨렌 칼’, 2011년 슈톨렌 축제',
             'cr': '사진: Paulae · CC BY 3.0 · 위키미디어 공용 · 얼굴이 나오지 않게 일부 잘라 씀', 'u': 'https://commons.wikimedia.org/wiki/File:Gro%C3%9Fes_Dresdner_Stollenmesser_Nachbildung_2011.JPG',
             'alt': '흰 손잡이에 넓은 칼날이 달린 아주 큰 칼이 가죽 칼집과 함께 쇠사슬로 나무 장대에 매달려 있다. 뒤로 행렬을 따라 걷는 사람들의 몸이 보인다.'},
 },
 'scenes': [
  {'id': 'make', 'label': '흰 포대기 입히기', 'kind': 'mod', 'mod': 'place', 'night': False,
   'text': ['드레스덴 슈톨렌은 1474년 한 병원의 계산서에 처음 나와요. 대림절에 먹던 금식 빵으로, 밀가루와 효모와 물로만 만들었어요.',
            '유럽연합의 소개에 따르면, 1450년 교회는 대림절에 버터로 굽는 것을 금했어요. 기름으로 구운 빵은 밋밋하고 맛이 없었어요. 1490년, 교황 인노첸시오 8세가 ‘버터 편지’를 보내 드레스덴 슈톨렌 제빵사들을 이 금지에서 풀어 주었어요.',
            '아래 나무 판 위에 재료를 하나씩 놓아 보세요. 마지막에는 구운 빵에 버터를 바르고 흰 설탕을 덮어요.'],
   'text2': ['하얗게 감싸인 길쭉한 모양을 두고, 독일 개신교 언론 epd는 ‘성경 이야기 속 아기 예수를 떠올리게 하고, 흰 설탕은 포대기를 뜻한다고 한다’고 소개해요. 독일 소개 누리집 deutschland.de도 이 모양이 포대기에 싸인 아기 예수를 상징한다고 적어요. 누가 처음 그렇게 풀었는지는 확인되지 않아요.'],
   'kid': '반죽, 버터, 건포도, 아몬드, 그리고 흰 설탕! 하나씩 넣어서 슈톨렌을 만들어 볼까?',
   'kidq': '흰 설탕을 덮은 길쭉한 빵, 무엇을 닮은 것 같아?'},
  {'id': 'giant', 'label': '1730년의 거대한 슈톨렌', 'kind': 'duo', 'imgs': ['riesen', 'messer'], 'choose': True,
   'caps': ['1730년 기념 동판화(엘리아스 베크)', '오늘 축제의 큰 칼(2011년)'],
   'text': ['1730년, 작센의 선제후이자 폴란드 왕인 ‘강건왕’ 아우구스트 2세는 차이트하인 들판에서 큰 군대 잔치를 열고, 손님 2만 4천 명이 나눠 먹을 슈톨렌을 주문했어요.',
            '제빵사 100명쯤이 밀가루 20첸트너(1톤쯤), 달걀 3,600개, 우유 326통으로 1.8톤짜리 슈톨렌을 구웠어요. 이 빵을 굽기 위해 커다란 화덕을 따로 지었어요. 이 일을 기념한 동판화에는 말 여덟 마리가 슈톨렌을 실은 수레를 끄는 모습이 남아 있어요.'],
   'text2': ['드레스덴 제빵사들은 1730년의 이 일을 본떠 1994년부터 슈톨렌 축제를 열어요. 해마다 대림절 둘째 주일 전날, 커다란 슈톨렌을 수레에 싣고 시내를 돌아요. 첫 조각은 1730년의 칼을 본떠 만든 길이 1.5미터쯤의 큰 칼로 잘라요.'],
   'kid': '옛날 임금님이 엄청 큰 슈톨렌을 굽게 했대. 말 여덟 마리가 수레를 끌었어!',
   'kidq': '그렇게 큰 빵을 2만 4천 명이 나눠 먹으면, 한 사람이 얼마나 먹었을까?'},
 ],
 'imagine': {'t': '부엌에 버터 녹는 냄새가 퍼져요. 갓 구운 빵에서 김이 오르고, 붓이 지나간 자리가 반짝여요. 체를 톡톡 치자 흰 가루가 눈처럼 내려앉아요. 빵이 조용히 하얀 옷을 입어요.',
             'kid': '눈을 감아 봐. 고소한 버터 냄새! 체를 톡톡 치면 흰 가루가 눈처럼 내려와. 빵이 하얀 옷을 입었어.'},
 'lines': ['금식의 빵이 성탄의 빵이 되기까지.', '버터 한 덩이를 위한 편지.', '하얀 포대기를 떠올리게 하는 빵.', '나눌수록 커지는 성탄의 빵.'],
 'linesKid': ['버터를 넣어도 돼요!', '흰 설탕 눈이 내려요.', '누구랑 나눠 먹을까?'],
 'goals': {
  's4': {'t': '만드는 차례대로', 'p': '만드는 차례(반죽 → 버터 → 건포도와 과일 껍질 → 아몬드 → 버터와 흰 설탕)대로 다 놓으면 카드에 금박이 입혀져요.',
         'how': '만드는 차례대로 슈톨렌을 다 만들어 보세요', 'done': '만드는 차례대로 슈톨렌을 완성했어요',
         'ways': [{'id': 'plOrder', 't': '반죽 → 버터 → 건포도와 과일 껍질 → 아몬드 → 버터와 흰 설탕 차례로 놓기'}]},
  's5': {'t': '첫 조각 나누기', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.', 'how': '슈톨렌 첫 조각을 누구와 나눌지 고르거나, 아이와 함께 끝까지 보세요', 'done': '첫 조각을 나눌 사람을 정했어요',
         'ways': [{'id': 'choose', 't': '슈톨렌 첫 조각을 누구와 나눌지 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'place': {
   'items': ITEMS, 'order': '반죽, 버터, 건포도와 과일 껍질, 아몬드, 버터와 흰 설탕',
   'intro': '아래에서 하나를 골라 나무 판 위에 놓아 보세요. 만드는 차례는 반죽, 버터, 건포도와 과일 껍질, 아몬드, 그리고 구운 뒤 버터와 흰 설탕이에요.',
   'climax': '흰 설탕을 덮으니 슈톨렌이 하얗게 감싸였어요. 금식의 빵이 성탄의 빵이 되었어요.<span class="la">독일 쪽 자료들은 이 모양에서 포대기에 싸인 아기 예수를 떠올린다고 소개해요</span>',
   'home': None, 'orderDone': '기록 차례대로 다 넣었어요', 'wrongOrder': '기록에 남은 만드는 차례는 이래요: {order}', 'daylight': False,
   'svg': stage_svg()},
  'choose': {
   'q': '대림절에 구운 슈톨렌, 첫 조각은 누구와 나눌까요?',
   'opts': [{'t': '가족과 함께', 'r': '1730년의 큰 슈톨렌도 여럿이 나누려고 구웠어요.'},
            {'t': '이웃과 함께', 'r': '오늘 축제의 큰 슈톨렌도 조각조각 잘라 많은 사람이 나눠요.'},
            {'t': '고마운 사람에게', 'r': '옛 드레스덴 제빵사들은 해마다 성탄에 군주에게 슈톨렌을 바쳤어요.'}],
  },
 },
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="넣을 재료 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 만들어 보기</button></div>
  <div class="pl-home" hidden><p>슈톨렌을 다 만들었어요.</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div><p class="mod-note">무대 그림: 이 안내서가 그린 슈톨렌 만드는 판 · 재료와 차례는 <a href="''' + EU + '''" target="_blank" rel="noopener">유럽연합 보호 지리적 표시 소개</a>를 바탕으로</p></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>크리스트슈톨렌</b> 1530년 무렵 기록에는 ‘크리스트슈톨렌’이라는 이름이 나와요. 그 뒤 드레스덴 제빵사들은 해마다 성탄에 작센의 군주에게 슈톨렌을 바쳤어요. 장인 여덟 명이 18킬로그램짜리 슈톨렌을 들고 시내를 행진한 뒤 궁전으로 가져간 일도 있어요.',
    '<b>손으로 빚는 빵</b> 드레스덴 슈톨렌은 틀에 넣어 굽지 않고 손으로 빚어요. 처음에는 중간 온도로 짧게, 다음에는 낮은 온도로 오래 구워요.',
    '<b>보호받는 이름</b> 2010년 유럽연합은 ‘드레스덴 슈톨렌’을 보호 지리적 표시로 등록했어요. 드레스덴 둘레에서 정해진 재료 비율로 만든 것만 이 이름을 쓸 수 있어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>버터 편지는 몇 년?</b> 1490년이라고 적은 자료(유럽연합 소개)도 있고, 1491년이라고 적은 자료(애틀러스 옵스큐라)도 있어요.',
    '<b>누구에게 허락했나</b> 유럽연합 소개는 버터 편지가 드레스덴의 슈톨렌 제빵사들을 금지에서 풀어 주었다고 적어요. 선제후 집안에만 허락하고, 다른 사람은 해마다 프라이베르크 대성당을 짓는 데 돈을 내야 했다고 소개하는 자료(영어 위키백과, 근거 표시 없음)도 있어요.',
    '<b>흰 포대기</b> 빵 모양을 포대기에 싸인 아기 예수로 푸는 말은 독일의 여러 자료에 나와요. epd는 ‘그렇다고 한다’로, deutschland.de는 ‘상징한다’로 적었어요. 누가 처음 그렇게 풀었는지는 확인되지 않아요.',
    '<b>1474년보다 앞선 이야기</b> 1329년 한 독일 주교가 연 빵 대회에서 시작되었다는 이야기도 전해져요(유럽연합 소개). 드레스덴 슈톨렌이 처음 문서에 나오는 해는 1474년이에요.',
    '<b>1730년의 무게</b> 유럽연합 소개는 1.8톤, 애틀러스 옵스큐라는 ‘거의 2톤’이라고 적었어요.']},
  {'h': '함께 읽는 말씀', 'p': [
    '말씀은 뜻만 옮기고, 본문은 대한성서공회 개역개정으로 이어 드려요.',
    '<b>' + bl('LUK.2', '누가복음 2장 7절') + '</b> 마리아가 맏아들을 낳아 강보, 곧 포대기로 싸서 구유에 뉘었다는 말씀이에요.']},
 ],
 'src': [
  {'l': '유럽연합 집행위원회: 드레스덴 크리스트슈톨렌(보호 지리적 표시) — 1474년 병원 계산서, 1450년 버터 금지, 1490년 버터 편지, 1530년 이름, 1730년 2만 4천 명·제빵사 100명·재료, 축제, 2010년 등록, 만드는 차례', 'u': EU},
  {'l': '애틀러스 옵스큐라: 드레스덴 슈톨렌 — 1491년 버터 편지, 1730년 특별 화덕·제빵사 100명·여덟 마리 말 동판화, 슈톨렌 칼(5피트·26파운드, 1730년 칼을 본뜸, 첫 조각만)', 'u': ATLAS},
  {'l': 'evangelisch.de(epd), 2025.11.23: 전통 수공예 크리스트슈톨렌 — 모양과 흰 설탕의 뜻(‘그렇다고 한다’), 구운 뒤 버터·설탕, 반죽 재료, 1474년, 1994년부터 축제', 'u': EPD},
  {'l': 'deutschland.de: 성탄 고전 크리스트슈톨렌 — 포대기에 싸인 아기 예수를 상징, 2010년 보호 표시, 반죽 재료', 'u': DDE},
  {'l': '위키미디어 공용: 엘리아스 베크의 채색 동판화 설명(27½×13¾cm)', 'u': 'https://commons.wikimedia.org/wiki/File:Zeithainer_Riesenstollen.jpg'},
  {'l': '위키미디어 공용: 2011년 슈톨렌 축제의 큰 칼(본뜬 것) 사진 설명', 'u': 'https://commons.wikimedia.org/wiki/File:Gro%C3%9Fes_Dresdner_Stollenmesser_Nachbildung_2011.JPG'},
  {'l': '영어 위키백과: Stollen — 길잡이로만(버터 편지를 받은 사람과 프라이베르크 대성당 이야기, 근거 표시 없음)', 'u': 'https://en.wikipedia.org/wiki/Stollen'},
  {'l': '대한성서공회 개역개정: 누가복음 2장', 'u': NKRV + 'LUK.2'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '65% 70%', 'p1': '55% 60%', 's0': 1.22, 's1': 1.05, 'kicker': '드레스덴 · 독일', 'title': "드레스덴 슈톨렌",
   'lines': [{'t': '하얀 가루를 뒤집어쓴 성탄 빵.'}, {'t': '옛날에는 이 빵에 버터를 넣을 수 없었어요.'}],
   'kid': [{'t': '하얀 가루를 덮은 빵이야.'}, {'t': '옛날엔 버터를 못 넣었대!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '버터 편지'},
  {'type': 'mod', 'mod': 'place', 'ch': 1,
   'lines': [{'t': '대림절은 금식하는 때였어요. 기름으로 구운 빵은 맛이 없었어요.'},
             {'t': '반죽을 빚고,', 'act': 'dough'},
             {'t': '1490년 ‘버터 편지’ 덕분에 버터를 넣어요.', 'act': 'butter'},
             {'t': '건포도와 과일 껍질,', 'act': 'fruit'}, {'t': '아몬드를 넣어 구워요.', 'act': 'almond'},
             {'t': '버터를 바르고 흰 설탕을 덮으면,', 'act': 'sugar', 'wait': 1500},
             {'t': '하얗게 감싸인 성탄 빵이 돼요.', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '같이 만들어 보자!'}, {'t': '반죽!', 'act': 'dough'}, {'t': '버터!', 'act': 'butter'}, {'t': '건포도!', 'act': 'fruit'},
           {'t': '아몬드!', 'act': 'almond'}, {'t': '흰 설탕 눈이 내려!', 'act': 'sugar', 'wait': 1500},
           {'t': '흰 옷을 입은 빵, 무엇을 닮았을까?', 'act': 'day', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '1730년'},
  {'type': 'img', 'ch': 2, 'img': 'messer', 'fit': 'cover', 'p0': '45% 50%', 'p1': '55% 50%', 's0': 1.12, 's1': 1.0, 'cap': '1730년의 칼을 본뜬 드레스덴 슈톨렌 칼',
   'lines': [{'t': '1730년, 강건왕 아우구스트는 1.8톤짜리 슈톨렌을 굽게 했어요.'},
             {'t': '말 여덟 마리가 그 빵을 실은 수레를 끌었어요.'},
             {'t': '지금도 축제 날이면, 그 칼을 본뜬 큰 칼로 첫 조각을 잘라요.'}],
   'kid': [{'t': '옛날 임금님이 엄청 큰 빵을 굽게 했대!'}, {'t': '이렇게 큰 칼로 잘랐어!'}]},
  {'type': 'imagine', 'ch': 3,
   'lines': [{'t': '부엌에 버터 녹는 냄새가 퍼져요.'}, {'t': '체를 톡톡, 흰 가루가 눈처럼 내려앉아요.'}, {'t': '빵이 조용히 하얀 옷을 입어요.'}],
   'kid': [{'t': '눈을 감아 봐. 고소한 버터 냄새!'}, {'t': '체를 톡톡, 흰 눈이 내려와.'}]},
  {'type': 'reward', 'ch': 3},
 ],
}
