# -*- coding: utf-8 -*-
"""깊은 카드: 민스파이(tb-mince) · 중심 방식 = 놓아 보기(+고르기)
기준서 1판 · 틀 deep3-3 · 키트 2판(보탬) · 2026-11-18 만들기 시작
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 1666년 성탄 전야, 큰불을 견딘 런던 피프스의 집 부엌.
     아내 엘리자베스가 새벽 네 시까지 하녀들이 민스파이 빚는 것을 지켜본 밤(피프스 일기 1666.12.24·25)
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 그 밤 부엌의 일, 곧 민스파이 빚기 → 같은 시대 로버트 메이의 요리책
     (1660) 차례대로 파이 껍질(코핀)에 다진 고기·기름·향신료·말린 과일을 채우고 뚜껑 덮기
카드 크기: 큰 카드 — 재료가 정해요(재료가 적은데 큰 카드로 늘리지 않아요).
무대 그림은 이 카드 안의 stage_svg()로 이 안내서가 그렸어요(남의 그림을 따라 그리지 않음).
그림 원본(src)은 deep_src/tb-mince/ (저장소 밖). 받는 법: commons_get.py"""
import random
S = 'tb-mince/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

PD = 'https://www.pepysdiary.com/diary/'
MAY = 'https://www.gutenberg.org/ebooks/22790'
OLAVE = 'https://saintolave.com/?p=724'
CL = 'https://www.countrylife.co.uk/articles/curious-questions-did-mince-pies-really-once-contain-meat-250600'
WC = 'https://commons.wikimedia.org/wiki/File:'


def stage_svg():
    """1666년 성탄 전야 밤 부엌: 창(밤 → 새벽), 촛불, 식탁, 긴 파이 껍질과 채울 것들. 이 안내서가 그림."""
    R = random.Random(1666)
    stars = ''.join(f'<circle cx="{R.uniform(64, 236):.0f}" cy="{R.uniform(70, 196):.0f}" r="{R.choice([0.8, 1.0, 1.3]):.1f}" fill="#fff" opacity="{R.uniform(.4, .9):.2f}"/>' for _ in range(16))
    meat = ''.join((lambda x, y: f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{R.uniform(5, 9):.1f}" ry="{R.uniform(3, 5.5):.1f}" fill="{R.choice(["#6b3a22", "#7a4429", "#5c3020", "#8a5233"])}" transform="rotate({R.uniform(-40, 40):.0f} {x:.0f} {y:.0f})"/>')(R.uniform(262, 538), R.uniform(370, 404)) for _ in range(70))
    suet = ''.join(f'<rect x="{R.uniform(262, 534):.0f}" y="{R.uniform(368, 402):.0f}" width="{R.uniform(4, 7):.1f}" height="{R.uniform(3, 5):.1f}" rx="1.5" fill="#f3ead8" opacity=".92"/>' for _ in range(42))
    spice = ''.join(f'<g transform="translate({R.uniform(266, 532):.0f} {R.uniform(370, 402):.0f}) rotate({R.uniform(0, 90):.0f})"><rect x="-4" y="-0.9" width="8" height="1.8" fill="#2b170c"/><rect x="-0.9" y="-4" width="1.8" height="8" fill="#2b170c"/></g>' for _ in range(16))
    spice += ''.join(f'<circle cx="{R.uniform(266, 532):.0f}" cy="{R.uniform(370, 402):.0f}" r="1.3" fill="#1b120c"/>' for _ in range(40))
    fruit = ''.join(f'<circle cx="{R.uniform(266, 532):.0f}" cy="{R.uniform(369, 403):.0f}" r="{R.uniform(2.6, 4):.1f}" fill="{R.choice(["#2a1426", "#3b1a30", "#241018"])}"/>' for _ in range(60))
    fruit += ''.join(f'<ellipse cx="{R.uniform(270, 528):.0f}" cy="{R.uniform(372, 400):.0f}" rx="7.5" ry="5" fill="#2c1322" stroke="#4a2236" stroke-width="1"/>' for _ in range(9))
    return f'''<svg class="stage" viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice" role="img" aria-label="촛불 하나가 켜진 밤의 부엌 식탁. 놓은 것들이 긴 파이 껍질 안에 하나씩 채워진다."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140f12"/><stop offset="1" stop-color="#231912"/></linearGradient>
<linearGradient id="__U__night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070b18"/><stop offset="1" stop-color="#16203a"/></linearGradient>
<linearGradient id="__U__dawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5b6f9a"/><stop offset=".55" stop-color="#d9a37a"/><stop offset="1" stop-color="#f6d6a0"/></linearGradient>
<linearGradient id="__U__table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a3a22"/><stop offset="1" stop-color="#3a2516"/></linearGradient>
<radialGradient id="__U__cl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd98f" stop-opacity=".9"/><stop offset=".45" stop-color="#ffb055" stop-opacity=".35"/><stop offset="1" stop-color="#ff9a3c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__warm" cx=".5" cy=".62" r=".6"><stop offset="0" stop-color="#ffcf86" stop-opacity=".8"/><stop offset=".5" stop-color="#d9893c" stop-opacity=".35"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".25" cy=".25" r=".95"><stop offset="0" stop-color="#fff0c8" stop-opacity=".7"/><stop offset=".55" stop-color="#ffd59a" stop-opacity=".3"/><stop offset="1" stop-color="#ffb46a" stop-opacity="0"/></radialGradient>
<linearGradient id="__U__crust" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2b46e"/><stop offset="1" stop-color="#b47a3c"/></linearGradient>
<linearGradient id="__U__lid" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ecc27c"/><stop offset="1" stop-color="#c28a48"/></linearGradient></defs>
<rect width="800" height="600" fill="url(#__U__wall)"/>
<g><rect x="56" y="62" width="188" height="142" rx="6" fill="url(#__U__night)"/><rect class="sky2" x="56" y="62" width="188" height="142" rx="6" fill="url(#__U__dawn)"/>{stars}
<circle cx="204" cy="96" r="11" fill="#f2ead2" opacity=".85"/><path d="M150 62 V204 M56 133 H244" stroke="#2a1d14" stroke-width="7"/><rect x="56" y="62" width="188" height="142" rx="6" fill="none" stroke="#2a1d14" stroke-width="9"/></g>
<g fill="#2a2019" opacity=".9"><rect x="560" y="70" width="190" height="10" rx="3"/><circle cx="600" cy="62" r="11"/><rect x="636" y="44" width="22" height="26" rx="4"/><path d="M684 70 C684 48 716 48 716 70Z"/></g>
<path d="M0 300 L800 300 L800 600 L0 600Z" fill="url(#__U__table)"/>
<path d="M0 300 L800 300" stroke="#7a5233" stroke-width="3"/>
<g stroke="#4a2f1c" stroke-width="1.4" opacity=".55"><path d="M0 352 C 200 346 420 360 800 350"/><path d="M0 418 C 260 410 520 426 800 414"/><path d="M0 492 C 240 486 520 500 800 488"/><path d="M0 560 C 300 552 520 566 800 556"/></g>
<path class="glow" d="M120 300 C 200 250 600 250 680 300 L760 600 L40 600Z" fill="url(#__U__warm)" opacity=".14"/>
<g><rect x="628" y="214" width="20" height="76" rx="3" fill="#efe1bf"/><path d="M638 214 C 632 204 634 196 638 188 C 642 196 644 204 638 214Z" fill="#ffd27a"/><ellipse cx="638" cy="292" rx="26" ry="7" fill="#7b6a55"/><circle cx="638" cy="200" r="64" fill="url(#__U__cl)"/></g>
<g opacity=".95"><ellipse cx="400" cy="452" rx="250" ry="34" fill="#20140c" opacity=".55"/></g>
<g class="obj" data-o="coffin"><path d="M236 360 C 236 340 252 334 270 334 L530 334 C 548 334 564 340 564 360 L556 424 C 554 440 542 446 526 446 L274 446 C 258 446 246 440 244 424Z" fill="url(#__U__crust)" stroke="#8a5a2a" stroke-width="2"/>
<path d="M256 366 C 256 354 266 350 278 350 L522 350 C 534 350 544 354 544 366 L540 410 C 539 420 532 424 522 424 L278 424 C 268 424 261 420 260 410Z" fill="#5a3418"/>
<g fill="#f0c98a" opacity=".9">{''.join(f'<circle cx="{x}" cy="338" r="4"/>' for x in range(264, 540, 14))}</g></g>
<g class="obj" data-o="meat">{meat}</g>
<g class="obj" data-o="suet">{suet}</g>
<g class="obj" data-o="spice">{spice}<g transform="translate(176 404)"><ellipse rx="34" ry="9" fill="#cdbb9a"/><ellipse cy="-3" rx="30" ry="7" fill="#e7dcc6"/><g fill="#3a2414"><circle cx="-10" cy="-4" r="2.2"/><circle cx="4" cy="-5" r="2.2"/><circle cx="14" cy="-2" r="2"/></g><path d="M-18 -6 l10 -3 l2 6z" fill="#c8662a"/></g></g>
<g class="obj" data-o="fruit">{fruit}</g>
<g class="obj" data-o="lid"><path d="M244 352 C 246 336 262 330 280 330 L520 330 C 538 330 554 336 556 352 L552 400 C 550 418 536 426 518 426 L282 426 C 264 426 250 418 248 400Z" fill="url(#__U__lid)" stroke="#9a6430" stroke-width="2"/>
<g stroke="#8a5424" stroke-width="3" stroke-linecap="round"><path d="M330 370 l26 0"/><path d="M386 362 l28 0"/><path d="M444 370 l26 0"/><path d="M356 394 l26 0"/><path d="M418 394 l26 0"/></g>
<g fill="#f6d99a" opacity=".95">{''.join(f'<circle cx="{x}" cy="332" r="4.2"/>' for x in range(262, 542, 14))}</g></g>
<rect class="day" width="800" height="600" fill="url(#__U__day)"/>
</svg>'''


ITEMS = [
 {'id': 'coffin', 't': '파이 껍질', 'la': 'coffin', 'say': '먼저 긴 파이 껍질을 세워요. 옛사람들은 밀가루와 물로 단단하게 빚은 이 껍질을 ‘코핀’이라고 불렀어요.'},
 {'id': 'meat', 't': '다진 고기', 'la': 'buttock of beef', 'say': '메이의 요리책은 소고기 엉덩잇살의 껍질을 걷어 내고 잘게 썰라고 해요.'},
 {'id': 'suet', 't': '소기름', 'la': 'beef-suet', 'say': '소기름(수에트)을 넣어 고기와 함께 잘게 다져요.'},
 {'id': 'spice', 't': '향신료', 'la': 'pepper, cloves, mace, nutmeg', 'say': '후추·정향·메이스·육두구에 소금으로 간해요. 바다 건너 들여온 값비싼 향신료예요.'},
 {'id': 'fruit', 't': '말린 과일', 'la': 'raisins, currans, prunes', 'say': '건포도와 커런트(작은 건포도), 말린 자두를 넣어요. 메이는 고기의 절반만큼 넣으라고 했어요.'},
 {'id': 'lid', 't': '뚜껑', 'la': 'close it up and bake it', 'say': '뚜껑을 덮어 닫아요. 이제 오븐에 들어갈 차례예요.'},
]

CARD = {
 'id': 'tb-mince', 'mode': '놓아 보기 · 고르기',
 'pagetitle': "민스파이",
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>1666년 성탄 전야</b><span>영국 런던 · 시싱 레인의 피프스 집 부엌</span>',
 'lead': '큰불이 휩쓸고 간 1666년 런던, 성탄 전날 밤. 일기 작가 피프스의 집 부엌에서는 새벽 네 시까지 민스파이를 빚었어요. 같은 시대 요리책의 차례대로 긴 파이 껍질을 하나씩 채워 보세요.',
 'leadKid': '옛날 런던의 성탄 전날 밤, 한 집 부엌에서 새벽까지 고기 파이를 만들었대. 우리도 하나씩 채워 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 6분',
 'draft': '검수 전 시안이에요(기준서 1판). 그 밤의 일은 새뮤얼 피프스의 일기(1666년 12월 24·25일)를, 파이에 넣는 차례는 로버트 메이의 요리책을 따랐어요. 일기에 없는 그 밤의 차례는 지어내지 않았어요. 무대 그림은 이 안내서가 그렸고, 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#7a2e2a;--accent-ink:#fffaf5;--soft:rgba(122,46,42,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#ba9290;--accent-ink:#1a0f0e;--soft:rgba(186,146,144,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#ba9290;--accent-ink:#1a0f0e;--soft:rgba(186,146,144,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '파이', 'y': '1666', 'sub': '런던 · 영국'},
 'doneNote': '성탄 아침, 함께 둘러앉은 식구들과 감사한 일 하나를 나눠 보세요.',
 'images': {
  'may': {'src': S + 'Frontispiece_portrait_of_Robert_May_and_title_page_from_his_book_The_Accomplisht.jpg',
          'cap': '로버트 메이의 초상과 『솜씨 좋은 요리사』 제목 쪽, 1678년 넷째 판(첫판은 1660년)',
          'cr': '판화: 1678년 판의 앞 그림 · 퍼블릭 도메인 · 위키미디어 공용(미국 의회도서관)',
          'u': WC + 'Frontispiece_(portrait)_of_Robert_May_and_title_page_from_his_book,_The_Accomplisht_Cook,_or_the_Art_and_Mystery_of_Cookery_LCCN2003674990.jpg',
          'alt': '펼친 옛 책. 왼쪽 쪽에는 긴 머리에 흰 깃을 단 남자의 판화 초상과 그 아래 시 몇 줄, 오른쪽 쪽에는 ‘The Accomplisht Cook’으로 시작하는 제목과 1678이라는 해가 인쇄되어 있다.'},
  'fire': {'src': S + 'Great_Fire_London.jpg',
           'cap': '런던 대화재, 타워 부두 가까운 배에서 본 모습, 1675년 무렵의 그림',
           'cr': '그림: 작가 모름 · 퍼블릭 도메인 · 위키미디어 공용',
           'u': WC + 'Great_Fire_London.jpg',
           'alt': '밤하늘 아래 강 건너 도시가 붉게 타오르고 검은 연기가 피어오른다. 왼쪽에 아치가 이어진 다리, 오른쪽에 성벽과 탑이 보이고, 앞쪽 강가에는 짐을 나르는 사람들과 배들이 있다.'},
  'pepys': {'src': S + 'Samuel_Pepys.jpg',
            'cap': '존 헤일스가 그린 새뮤얼 피프스, 1666년(런던 국립초상화미술관)',
            'cr': '그림: 존 헤일스(John Hayls) · 퍼블릭 도메인 · 위키미디어 공용',
            'u': WC + 'Samuel_Pepys.jpg',
            'alt': '긴 곱슬머리의 남자가 갈색 비단 가운에 흰 목도리를 두르고, 한 손에 악보를 든 채 이쪽을 본다.'},
  'olave': {'src': S + 'StOlave_HartSt_London_315_20220422_1100.jpg', 'crop': (0, 0.08, 1, 1),
            'cap': '세인트 올라프 교회, 시싱 레인 쪽에서 본 모습, 2022년(위쪽을 조금 잘라 씀)',
            'cr': '사진: Karlunun · CC BY-SA 4.0 · 위키미디어 공용',
            'u': WC + 'StOlave_HartSt_London_315_20220422_1100.jpg',
            'alt': '아래는 돌, 위는 벽돌로 쌓은 네모난 탑에 둥근 창과 시계, 풍향계가 달려 있다. 앞에 아치형 문이 난 작은 돌 교회가 있고, 뒤로 유리 건물이 솟아 있다.'},
  'pies': {'src': S + 'Mince_pies_on_a_plate.jpg',
           'cap': '오늘의 민스파이, 2013년',
           'cr': '사진: christmasstockimages.com · CC BY 3.0 · 위키미디어 공용',
           'u': WC + 'Mince_pies_on_a_plate.jpg',
           'alt': '붉은 접시 위에 설탕 가루를 뿌린 작고 둥근 파이 여섯 개. 하나는 쪼개져 검붉은 말린 과일 소가 보인다.'},
 },
 'extra_credits': [{'cr': '놓아 보기 무대: 이 안내서가 그린 1666년 성탄 전야의 부엌 · 피프스의 일기와 메이의 요리책을 바탕으로', 'u': PD + '1666/12/25/'}],
 'scenes': [
  {'id': 'cook', 'label': '1660년, 요리사의 책', 'kind': 'photo', 'img': 'may',
   'text': ['1660년, 두툼한 요리책 한 권이 나왔어요. 요리사 로버트 메이(Robert May, 1588년생)의 『솜씨 좋은 요리사』(The Accomplisht Cook)예요. 영국 최초의 본격적인 요리책으로 꼽혀요.',
            '메이는 프랑스에서 5년 동안 일하며 요리를 배웠고, 가톨릭과 왕당파 귀족 집안의 부엌에서 일했어요. 그의 책에는 민스파이 만드는 법이 여러 가지 실려 있어요.'],
   'quote': {'t': '소고기 엉덩잇살의 껍질을 걷어 내고 잘게 썰어요. 소기름을 넣어 함께 다지고, 후추·정향·메이스·육두구와 소금으로 간해요. 고기의 절반만큼 건포도·커런트·말린 자두를 넣어요.',
             'from': '로버트 메이, 『솜씨 좋은 요리사』의 ‘소고기 민스파이 만들기’(1685년 판) · 이 안내서가 줄여 우리말로 옮김', 'u': MAY},
   'text2': ['책이 나온 1660년은 왕정이 돌아온 해예요. 옥스퍼드 음식 백과는 메이가 이때를 기다렸다가 책을 냈을 것이라고 봐요.'],
   'kid': '옛날 요리사 아저씨가 쓴 요리책이야. 민스파이에 소고기랑 기름이랑 건포도를 넣으래!',
   'kidq': '고기랑 건포도를 같이 넣은 파이는 무슨 맛일까?'},
  {'id': 'fire', 'label': '불탄 도시의 가을', 'kind': 'photo', 'img': 'fire',
   'text': ['1666년 9월 2일 새벽 세 시쯤, 런던 해군 사무소 곁에 사는 새뮤얼 피프스(Samuel Pepys, 1633~1703)의 집. 하녀 제인이 시내에 큰불이 났다며 식구들을 깨웠어요. 불은 푸딩 레인의 왕실 빵집에서 시작됐어요.',
            '이틀 뒤 불길이 다가오자, 피프스는 이웃 윌리엄 펜 경과 구덩이를 파고 포도주를, 그리고 자기 파르메산 치즈를 묻었어요.'],
   'text2': ['불길은 피프스가 다니던 세인트 올라프 교회 90미터 남짓 앞까지 왔어요. 하지만 바람이 바뀌어 교회는 불을 견뎠어요.'],
   'kid': '아주 큰불이 나서 런던이 많이 탔어. 피프스 아저씨는 땅을 파서 치즈를 묻었대!',
   'kidq': '피프스는 치즈를 지키려고 했어. 너라면 무엇을 꼭 지키고 싶어?'},
  {'id': 'kitchen', 'label': '성탄 전야, 새벽 네 시까지', 'kind': 'mod', 'mod': 'place', 'night': True,
   'text': ['넉 달 뒤, 1666년 12월 24일 밤. 피프스는 일기에 집안 사람들이 민스파이를 만드느라 바쁘다고 적고 잠자리에 들었어요.',
            '아내 엘리자베스는 잠들지 않고 새벽 네 시까지 하녀들이 민스파이를 빚는 것을 지켜보았어요. 아래 식탁에서, 메이의 요리책 차례대로 긴 파이 껍질을 하나씩 채워 보세요.'],
   'quote': {'t': '아내는 오늘 새벽 네 시까지 깨어 앉아, 하녀들이 민스파이 만드는 것을 지켜보았다.',
             'from': '새뮤얼 피프스의 일기, 1666년 12월 25일 · 이 안내서가 우리말로 옮김', 'u': PD + '1666/12/25/'},
   'text2': ['그 밤 부엌에서 무엇을 어떤 차례로 넣었는지는 일기에 없어요. 무대의 차례는 같은 시대 메이의 요리책을 따랐어요.'],
   'kid': '성탄 전날 밤, 피프스네 부엌이야. 하녀 언니들이 새벽까지 민스파이를 만들었대. 우리도 하나씩 채워 볼까?',
   'kidq': '새벽 네 시까지 깨어 있는 부엌에서는 어떤 냄새가 날까?'},
  {'id': 'morning', 'label': '성탄 아침의 식탁', 'kind': 'duo', 'imgs': ['pepys', 'olave'],
   'caps': ['새뮤얼 피프스, 1666년 존 헤일스 그림', '세인트 올라프 교회, 2022년'],
   'text': ['성탄 아침, 피프스는 늦게까지 누워 있다가 일어났어요. 새벽까지 깨어 있던 아내는 더 자게 두었어요.',
            '피프스는 세인트 올라프 교회에 가서 밀스 목사의 좋은 설교를 들었어요. 집에 와서는 아내와 동생, 바커와 함께 구운 소갈비와 민스파이로 잘 먹었어요.'],
   'quote': {'t': '내 마음은 참된 기쁨으로 가득했고, 오늘 내 처지가 이렇게 좋은 것을 전능하신 하나님께 감사했다.',
             'from': '새뮤얼 피프스의 일기, 1666년 12월 25일 · 이 안내서가 우리말로 옮김', 'u': PD + '1666/12/25/'},
   'text2': ['세인트 올라프 교회는 큰불을 견딘 몇 안 되는 중세 교회 가운데 하나예요. 피프스와 엘리자베스는 지금 이 교회에 나란히 잠들어 있어요.'],
   'kid': '성탄 아침! 피프스 아저씨는 교회에 다녀와서 소갈비랑 민스파이를 먹었어. 마음이 기쁨으로 가득했대.',
   'kidq': '성탄 아침에 우리 가족은 무엇을 먹으면 좋을까?',
   'choose': True},
  {'id': 'today', 'label': '고기가 빠진 파이', 'kind': 'photo', 'img': 'pies',
   'text': ['18세기 중반부터 민스파이는 짭짤한 고기 요리에서 달콤한 과자로 바뀌기 시작했어요. 설탕이 싸지면서 단 파이가 더 사랑받았어요.',
            '20세기에 들어서는 고기가 거의 빠졌어요. 다진 것이라는 뜻의 이름 ‘민스’만 옛 고기 파이를 기억해요.'],
   'text2': ['크기도 달라졌어요. 옛 파이는 온 식구와 손님이 한자리에서 나눠 먹을 만큼 크고 길쭉했어요. 지금은 한 손에 쏙 들어오는 작은 파이예요.'],
   'kid': '지금 민스파이에는 고기가 거의 없어. 말린 과일이 가득한 달콤한 파이야.',
   'kidq': '옛날 고기 민스파이와 지금 과일 민스파이, 너는 어떤 걸 먹어 보고 싶어?'},
 ],
 'imagine': {'t': '촛불 하나가 밝힌 겨울밤 부엌. 칼이 도마를 두드리는 소리, 정향과 육두구 냄새, 손등에 묻은 밀가루. 하품을 참는 하녀들 곁에서 엘리자베스가 긴 파이를 지켜봐요. 불탄 도시의 창밖이 희뿌옇게 밝아 오면, 성탄 아침이에요.',
             'kid': '눈을 감아 봐. 촛불 하나 켠 깜깜한 부엌이야. 탁탁탁 고기 다지는 소리, 달콤한 향신료 냄새. 하품이 나와도 꾹 참고 파이를 채워. 창밖이 밝아지면 성탄 아침이야!'},
 'lines': ['새벽 네 시까지 불이 꺼지지 않던 부엌.', '불탄 도시에도 성탄 아침은 왔어요.', '내 마음은 참된 기쁨으로 가득했다.', '고기는 빠져도 이름은 남았어요.'],
 'linesKid': ['탁탁탁, 새벽 부엌!', '성탄 아침엔 민스파이!', '고기 파이가 과일 파이로!'],
 'goals': {
  's4': {'t': '요리책 차례대로', 'p': '메이의 요리책 차례(고기 → 기름 → 향신료 → 말린 과일)대로 채우고 뚜껑까지 덮으면 카드에 금박이 입혀져요.',
         'how': '메이의 요리책 차례대로 그 밤의 파이를 다 채워 보세요', 'done': '요리책 차례대로 그 밤의 파이를 채웠어요',
         'ways': [{'id': 'plOrder', 't': '껍질 → 고기 → 기름 → 향신료 → 말린 과일 → 뚜껑 차례로 채우기'}]},
  's5': {'t': '성탄 아침의 감사', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '피프스처럼 성탄 아침에 감사할 한 가지를 고르거나, 아이와 함께 끝까지 보세요', 'done': '성탄 아침의 감사를 골랐어요',
         'ways': [{'id': 'choose', 't': '피프스처럼, 성탄 아침에 감사할 한 가지 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'place': {
   'items': ITEMS, 'order': '파이 껍질, 다진 고기, 소기름, 향신료, 말린 과일, 뚜껑',
   'intro': '아래에서 하나를 골라 식탁 위에 놓아 보세요. 메이의 요리책 차례는 다진 고기, 소기름, 향신료, 말린 과일이에요. 먼저 파이 껍질을 세우고, 마지막에 뚜껑을 덮어요.',
   'climax': '새벽 네 시. 긴 파이가 다 채워졌어요. 창밖이 밝아 오면 성탄 아침이에요.<span class="la">having sat up till four this morning seeing her mayds make mince-pies<br>새뮤얼 피프스의 일기, 1666년 12월 25일</span>',
   'home': None,
   'wrongOrder': '메이의 요리책과 그 밤의 일을 따른 차례는 이래요: {order}',
   'orderDone': '요리책 차례대로 다 채웠어요',
   'svg': stage_svg()},
  'choose': {
   'q': '피프스는 성탄 아침, 마음이 기쁨으로 가득하다며 감사를 적었어요. 우리 집이라면 무엇에 가장 먼저 감사할까요?',
   'opts': [{'t': '함께 둘러앉은 식구', 'r': '피프스도 그날 아내와 동생, 바커와 함께 상에 둘러앉았어요.'},
            {'t': '무사히 지난 한 해', 'r': '큰불이 난 해, 피프스는 자기 처지가 좋은 것을 하나님께 감사했어요.'},
            {'t': '따뜻한 한 끼', 'r': '그날 상에는 구운 소갈비와 민스파이가 올랐어요.'},
            {'t': '밤새 애쓴 손', 'r': '그 파이는 새벽 네 시까지 깨어 있던 손들이 빚었어요.'}]},
 },
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 채워 보기</button></div>
  <div class="pl-home" hidden><p>우리 집이라면?</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>새뮤얼 피프스</b> 1633~1703. 런던 시싱 레인의 해군 사무소에서 일하며 그 곁에 살았어요. 그가 남긴 일기는 큰불이 난 해의 런던을 날마다 보여 줘요.',
    '<b>헤일스의 초상</b> 1666년 3월 17일부터 피프스는 화가 존 헤일스 앞에 앉았어요. 그림을 위해 인도풍 가운을 빌려 입었고, 손에 든 악보는 피프스가 직접 곡을 붙인 노래 「아름다움이여, 물러가라」(Beauty, retire)예요. 5월 16일 그림값 14파운드와 액자값 25실링을 치렀어요.',
    '<b>코핀</b> 옛 파이 껍질은 밀가루와 물로 빚어 아주 단단했어요. 구운 뒤에도 먹기 힘들어, 가난한 이들에게 나눠 주거나 짐승에게 주기도 했어요.',
    '<b>커런트</b> 씨 없는 작은 건포도예요. 1640년 이후 의회는 커런트 수입을 막고 고기·생선·소금 같은 먹을거리에 세금을 매겼어요. 청교도가 다스리던 시절 성탄 상은 그만큼 비싸졌어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>민스파이 금지법?</b> ‘성탄에 민스파이를 먹으면 불법’이라는 말을 영국 의회 역사 연구소는 ‘되풀이되는 신화’라고 불러요. 1647년 6월 8일 의회는 성탄·부활절·성령강림절을 축일로 지키지 못하게 했지만, 음식을 막는 조항은 없었어요.',
    '<b>1644년의 성탄</b> 그해 성탄은 법으로 정한 금식일인 수요일과 겹쳤어요. 그래서 그해에는 민스파이를 먹는 일도 막힌 셈이라고 소개하는 글도 있어요(영국 법률위원회 자료, 런던대 고등법학연구소 블로그). 같은 자료도 민스파이 자체를 금지한 법은 없었다고 적어요.',
    '<b>긴 파이는 구유 모양?</b> 17세기 영국 학자 존 셀던(1584~1654)은 『탁상 담화』(1689)에서 성탄 파이의 긴 코핀이 구유를 본뜬 것이라고 했어요. 음식사학자 아이번 데이는 파이가 그런 모양이었다고 분명히 말한 사람은 셀던 하나뿐이라고 해요.']},
  {'h': '직접 가 보기', 'img': ['olave'], 'checked': '2026년 11월 18일', 'p': [
    '세인트 올라프 교회는 런던 시티의 시싱 레인 가에 있어요. 피프스는 해군 사무소와 계단으로 이어지는 회랑을 교회 안에 지었어요. 회랑은 헐렸지만, 그 계단 문 자리에 기념판이 있어요.',
    '여는 날과 시간은 바뀔 수 있으니 교회 누리집에서 미리 확인해 주세요.'],
   'links': [{'t': '피프스의 일기 1666년 12월 25일(원문과 해설)', 'u': PD + '1666/12/25/', 'm': '영어'},
             {'t': '세인트 올라프 교회: 교회 이야기와 여는 시간', 'u': OLAVE, 'm': '영어'},
             {'t': '프로젝트 구텐베르크: 로버트 메이의 『솜씨 좋은 요리사』 전문', 'u': MAY, 'm': '영어'}]},
 ],
 'src': [
  {'l': '새뮤얼 피프스의 일기, 1666년 12월 24일 — 집안 사람들이 민스파이를 만드느라 바쁨', 'u': PD + '1666/12/24/'},
  {'l': '새뮤얼 피프스의 일기, 1666년 12월 25일 — 아내가 새벽 네 시까지 하녀들의 민스파이 빚기를 지켜봄, 교회와 밀스 목사, 소갈비와 민스파이, 참된 기쁨과 감사', 'u': PD + '1666/12/25/'},
  {'l': '새뮤얼 피프스의 일기, 1666년 9월 2일 — 새벽 세 시 제인이 깨움, 푸딩 레인의 왕실 빵집', 'u': PD + '1666/09/02/'},
  {'l': '새뮤얼 피프스의 일기, 1666년 9월 4일 — 윌리엄 펜 경과 구덩이를 파서 포도주와 파르메산 치즈를 묻음', 'u': PD + '1666/09/04/'},
  {'l': '세인트 올라프 교회, 「Our Story」 — 큰불을 견딘 중세 교회, 불길이 100야드 앞까지, 피프스 부부의 무덤, 회랑과 기념판, 여는 시간', 'u': OLAVE},
  {'l': '런던 국립초상화미술관 NPG 211 — 존 헤일스의 피프스 초상(1666), 인도풍 가운, 악보 「Beauty, retire」, 그림값', 'u': 'https://www.npg.org.uk/collections/search/portrait/mw04948'},
  {'l': '옥스퍼드 음식 백과 ‘로버트 메이’ 항목 — 1588년생, 1660년 첫 본격 영국 요리책, 프랑스 5년, 가톨릭·왕당파 집안, 왕정복고를 기다린 출간', 'u': 'https://app.ckbk.com/reference/food77337c13s001e116'},
  {'l': '로버트 메이, 『솜씨 좋은 요리사』(1685년 판, 프로젝트 구텐베르크) — ‘소고기 민스파이 만들기’, 다른 파이의 ‘close it up and bake it’', 'u': MAY},
  {'l': '컨트리 라이프(2022.12.3) 「민스파이에 정말 고기가 들었을까?」 — 코핀, 양고기, 값비싼 향신료, 크고 길쭉한 파이, 18세기 중반부터 달콤해짐, 20세기 고기 없는 파이', 'u': CL},
  {'l': '아이번 데이 블로그 「Shaped Minc’d Pies Again」(2011.12.24) — 셀던 『탁상 담화』(1689)의 구유 설명과 그 근거의 한계', 'u': 'https://foodhistorjottings.blogspot.com/2011/12/shaped-mincd-pies-again.html'},
  {'l': '영국 의회 역사 연구소(2013.12.22) 「내전기의 의회와 성탄」 — 1647년 6월 8일 축일 폐지, 민스파이 금지법은 신화', 'u': 'https://historyofparliament.com/2013/12/22/christmas-during-the-civil-war/'},
  {'l': '영국 의회 역사 연구소(2020.12.23) 「청교도가 성탄 만찬을 금지했을까?」 — 1640년 이후 커런트 수입 금지, 먹을거리 세금', 'u': 'https://historyofparliament.com/2020/12/23/did-the-puritans-ban-christmas-dinner/'},
  {'l': '런던대 고등법학연구소 블로그(2021.12.22) — 1644년 성탄과 금식일, 영국 법률위원회 「Legal Curiosities」', 'u': 'https://ials.blogs.sas.ac.uk/2021/12/22/on-this-day-25-december-1647-christmas-was-cancelled/'},
  {'l': '위키미디어 공용: 「런던 대화재」 그림 정보(1675년 무렵, 타워 부두 가까운 배에서 본 모습)', 'u': WC + 'Great_Fire_London.jpg'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 45%', 'p1': '55% 50%', 's0': 1.2, 's1': 1.05, 'kicker': '1666년 성탄 전야 · 영국 런던', 'title': "민스파이",
   'lines': [{'t': '작고 달콤한 영국의 성탄 과자, 민스파이.'}, {'t': '360년 전 런던에서는 고기를 넣은 긴 파이였어요.'}],
   'kid': [{'t': '영국 사람들이 성탄에 먹는 작은 파이야.'}, {'t': '옛날엔 이 안에 고기가 들어갔대!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '요리사의 책'},
  {'type': 'img', 'ch': 1, 'img': 'may', 'fit': 'contain', 'p0': '50% 40%', 'p1': '30% 35%', 's0': 1.0, 's1': 1.12, 'cap': '로버트 메이와 『솜씨 좋은 요리사』',
   'lines': [{'t': '1660년, 요리사 로버트 메이의 책이 나왔어요.'},
             {'t': '소고기를 썰어 기름과 다지고, 향신료와 말린 과일을…', 'q': True, 'from': '메이의 ‘소고기 민스파이’에서'}],
   'kid': [{'t': '옛날 요리책에 민스파이 만드는 법이 있어.'}, {'t': '고기랑 건포도를 같이 넣는대. 맛이 어떨까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '불탄 도시'},
  {'type': 'img', 'ch': 2, 'img': 'fire', 'fit': 'cover', 'p0': '40% 50%', 'p1': '60% 45%', 's0': 1.18, 's1': 1.03, 'cap': '런던 대화재, 1675년 무렵의 그림',
   'lines': [{'t': '1666년 9월, 런던에 큰불이 났어요.'}, {'t': '피프스는 마당에 포도주와 치즈를 묻었어요.'}, {'t': '불길은 그가 다니던 교회 앞에서 멈췄어요.'}],
   'kid': [{'t': '아주 큰불이 났어. 피프스 아저씨는 치즈를 땅에 묻었대!'}, {'t': '너라면 무엇을 지키고 싶어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '새벽 네 시까지'},
  {'type': 'mod', 'mod': 'place', 'ch': 3,
   'lines': [{'t': '1666년 성탄 전야, 피프스네 부엌.'},
             {'t': '긴 파이 껍질을 세우고,', 'act': 'coffin'}, {'t': '다진 고기와', 'act': 'meat'}, {'t': '소기름,', 'act': 'suet'},
             {'t': '향신료와', 'act': 'spice'}, {'t': '말린 과일을 채워요.', 'act': 'fruit'},
             {'t': '뚜껑을 덮으니 어느새 새벽이에요.', 'act': 'lid', 'wait': 1500},
             {'t': '창밖이 밝아 와요.', 'act': 'day', 'wait': 1500},
             {'t': '아내는 새벽 네 시까지 하녀들의 민스파이 빚기를 지켜보았다.', 'q': True, 'from': '피프스의 일기, 1666년 12월 25일'}],
   'kid': [{'t': '깜깜한 밤 부엌이야.'},
           {'t': '파이 껍질!', 'act': 'coffin'}, {'t': '고기!', 'act': 'meat'}, {'t': '기름!', 'act': 'suet'},
           {'t': '향신료!', 'act': 'spice'}, {'t': '말린 과일!', 'act': 'fruit'}, {'t': '뚜껑 덮고 끝!', 'act': 'lid', 'wait': 1200},
           {'t': '창밖이 밝아졌어. 어떤 냄새가 날까?', 'act': 'day', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '성탄 아침'},
  {'type': 'img', 'ch': 4, 'img': 'pepys', 'fit': 'contain', 'p0': '50% 30%', 'p1': '50% 40%', 's0': 1.0, 's1': 1.1, 'cap': '새뮤얼 피프스, 1666년',
   'lines': [{'t': '성탄 아침, 피프스는 교회에 다녀왔어요.'}, {'t': '구운 소갈비와 민스파이로 잘 먹었어요.'},
             {'t': '내 마음은 참된 기쁨으로 가득했다.', 'q': True, 'from': '피프스의 일기, 1666년 12월 25일'}],
   'kid': [{'t': '성탄 아침! 교회에 갔다가 소갈비랑 민스파이를 먹었대.'}, {'t': '피프스 아저씨는 무엇이 그렇게 기뻤을까?', 'ask': True}]},
  {'type': 'img', 'ch': 4, 'img': 'olave', 'fit': 'cover', 'p0': '50% 30%', 'p1': '50% 50%', 's0': 1.15, 's1': 1.0, 'cap': '세인트 올라프 교회, 2022년',
   'lines': [{'t': '피프스가 다니던 세인트 올라프 교회는 큰불을 견뎌 지금도 서 있어요.'}],
   'kid': [{'t': '피프스 아저씨가 다니던 교회가 지금도 있어.'}]},
  {'type': 'chapter', 'ch': 5, 'no': 5, 't': '오늘의 민스파이'},
  {'type': 'img', 'ch': 5, 'img': 'pies', 'fit': 'cover', 'p0': '50% 55%', 'p1': '55% 60%', 's0': 1.15, 's1': 1.0, 'cap': '오늘의 민스파이',
   'lines': [{'t': '18세기부터 민스파이는 점점 달콤해졌어요.'}, {'t': '이제는 고기 대신 말린 과일이 가득해요.'}],
   'kid': [{'t': '지금은 고기 대신 말린 과일이 가득해.'}, {'t': '너는 어떤 민스파이를 먹어 보고 싶어?', 'ask': True}]},
  {'type': 'imagine', 'ch': 6,
   'lines': [{'t': '촛불 하나가 밝힌 겨울밤 부엌.'}, {'t': '도마 소리, 정향과 육두구 냄새, 손등의 밀가루.'}, {'t': '창밖이 밝아 오면, 성탄 아침이에요.'}],
   'kid': [{'t': '눈을 감아 봐. 촛불 하나 켠 부엌이야.'}, {'t': '탁탁탁! 달콤한 냄새! 창밖이 밝아지면 성탄 아침!'}]},
  {'type': 'reward', 'ch': 6},
 ],
}
