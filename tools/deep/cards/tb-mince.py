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
그림 원본(src)은 deep_src/tb-mince/ (저장소 밖). 받는 법: commons_get.py
2026-11-22 재벌(재벌.md): 악마의 대변인 → 열쇠 물음 셋(qs) · 뒷이야기 열여덟(qx, 꾸러미 6 · 6 · 6) · 후보(qcand).
  본 카드는 길잡이 한 줄과 쉬운 말만 고치고, ‘알고 보면’ 칸은 뒷이야기로 옮겨 덜어 냈어요."""
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
# 더 깊이(재벌, 2026-11-22)의 근거 — 모두 창이 직접 열어 확인한 페이지
MAGD_DIARY = 'https://www.magd.cam.ac.uk/pepys/virtual-exhibitions/diary'
MAGD_LIB = 'https://www.magd.cam.ac.uk/pepys'
MAGD_EP = 'https://magdalene.maxarchiveservices.co.uk/index.php/pepys-elizabeth-1640-1669-wife-of-samuel-pepys'
MAGD_JOHN = 'https://www.magd.cam.ac.uk/library-news/john-pepys-goes-cambridge'
HT_DIARY = 'https://www.historytoday.com/archive/feature/hidden-diary-samuel-pepys'
HJ_LOVEMAN = 'https://doi.org/10.1017/S0018246X21000716'
NPG211 = 'https://www.npg.org.uk/collections/search/portrait/mw04948'
NPG_EP = 'https://npgshop.org.uk/products/elizabeth-pepys-npg-d5507-print'
MON = 'https://londonmuseum.org.uk/collections/london-stories/monument-great-fire-london'
LM_FIRE = 'https://www.londonmuseum.org.uk/collections/v/object-102171/the-great-fire-of-london/'
MOLP = 'https://www.museumoflondonprints.com/products/pod447308'
CHT = 'https://www.churchtimes.co.uk/articles/2016/2-september/features/features/alight-by-the-hand-of-god'
RMG_PENN = 'https://www.rmg.co.uk/collections/objects/rmgc-object-14419'
IHR = 'https://blog.history.ac.uk/2021/07/christmas-under-cromwell-the-hidden-religious-festivals-of-interregnum-britain/'
HOP13 = 'https://historyofparliament.com/2013/12/22/christmas-during-the-civil-war/'
HOP20 = 'https://historyofparliament.com/2020/12/23/did-the-puritans-ban-christmas-dinner/'
CKBK = 'https://app.ckbk.com/reference/food77337c13s001e116'
LEEDS = 'https://library.leeds.ac.uk/special-collections/view/805'
TRINH = 'https://trinhall.cam.ac.uk/posts/seventeenth-century-cookery-dont-try-this-at-home'
IDAY13 = 'https://foodhistorjottings.blogspot.com/2013/12/an-early-modern-christmas-party.html'
IDAY11 = 'https://foodhistorjottings.blogspot.com/2011/12/shaped-mincd-pies-again.html'
LUMIN = 'https://luminarium.org/sevenlit/herrick/xmaseve.htm'
POETF = 'https://www.poetryfoundation.org/poets/robert-herrick'
MW = 'https://www.merriam-webster.com/dictionary/'
UWLS = 'https://library.wisc.edu/specialcollections/2015/10/05/the-long-s-now-largely-extinct'
BCP = 'https://www.churchofengland.org/sites/default/files/2026-10/5-table-vigils-fasts.pdf'
DELI = 'https://deliciousmagazine.co.uk/recipes/pear-and-apple-mincemeat/amp'
U_MAY = WC + 'Frontispiece_(portrait)_of_Robert_May_and_title_page_from_his_book,_The_Accomplisht_Cook,_or_the_Art_and_Mystery_of_Cookery_LCCN2003674990.jpg'
CR_MAY = '판화: 1678년 판의 앞 그림 · 퍼블릭 도메인 · 위키미디어 공용(미국 의회도서관)'
CAP_MAY = '『솜씨 좋은 요리사』 1678년 넷째 판 부분'
U_FIRE = WC + 'Great_Fire_London.jpg'
CR_FIRE = '그림: 작가 모름 · 퍼블릭 도메인 · 위키미디어 공용'
CAP_FIRE = '「런던 대화재」 부분 · 1675년 무렵의 그림'
U_PEP = WC + 'Samuel_Pepys.jpg'
CR_PEP = '그림: 존 헤일스(John Hayls) · 퍼블릭 도메인 · 위키미디어 공용'
CAP_PEP = '존 헤일스가 그린 새뮤얼 피프스 부분, 1666년'
U_OLA = WC + 'StOlave_HartSt_London_315_20220422_1100.jpg'
CR_OLA = '사진: Karlunun · CC BY-SA 4.0 · 위키미디어 공용'
CAP_OLA = '세인트 올라프 교회 부분, 2022년'
U_PIES = WC + 'Mince_pies_on_a_plate.jpg'
CR_PIES = '사진: christmasstockimages.com · CC BY 3.0 · 위키미디어 공용'
CAP_PIES = '오늘의 민스파이 부분, 2013년'
def bit(name, alt, cap, cr, u):   # 더 깊이(열쇠 · 뒷이야기)에만 쓰는 부분 그림 — deep_src/tb-mince/parts/(2026-11-22, _orig 원본에서 잘라 긴 쪽 3000px 안쪽 · 메이 판화의 작은 조각은 1300px로 키움)
    return {'src': S + 'parts/' + name + '.jpg', 'max': 1600, 'cap': cap, 'cr': cr, 'u': u, 'alt': alt}   # 판 · 짧은 영화에만 써서 확대용 큰 그림은 안 만들어요
# parts/ 자른 비율(원본 기준): may_face (0.06,0.04,0.47,0.74) · may_kick (0.52,0.42,0.94,0.61) · may_figures (0.52,0.60,0.94,0.77) · may_55 (0.52,0.76,0.94,0.95)
#   fire_paul (0.30,0.36,0.68,0.72) · fire_flee (0.58,0.66,1,1) · fire_bridge (0,0.48,0.44,0.82) · fire_tower (0.70,0.36,1,0.76)
#   pepys_score (0,0.48,0.52,0.84 · 1300px로 키움) · pepys_face (0.22,0.04,0.80,0.46) · olave_nave (0.42,0.46,1,0.84) · olave_tower (0.12,0,0.72,0.34)
#   pies_candle (0,0,0.40,0.42) · pies_open (0.44,0.44,0.90,0.90)


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
  # 더 깊이(재벌, 2026-11-22)에만 쓰는 부분 그림 — 모두 카드에 이미 있는 그림의 부분(새로 받은 그림 없음)
  'may_face': bit('may_face', '긴 머리에 콧수염을 기른 남자가 넓은 흰 깃을 달고 이쪽을 본다. 오른쪽 어깨 옆에 작게 ‘71’과 ‘1660’이 새겨져 있고, 아래에 흘려 쓴 시가 조금 보인다.', CAP_MAY + ' · 메이의 초상', CR_MAY, U_MAY),
  'may_kick': bit('may_kick', '옛 활자로 찍은 영어 글줄. ‘FLESH, FOWL, and FISH’, ‘how to raise all manner of Pastes’, ‘CARVING and SEWING’, ‘A-la-mode Curiosities’ 같은 말이 보이고, s가 f처럼 생긴 글자가 섞여 있다.', CAP_MAY + ' · 제목 쪽 가운데', CR_MAY, U_MAY),
  'may_figures': bit('may_figures', '옛 활자로 찍은 영어 글줄. ‘The Fourth Edition’, ‘two hundred Figures’, ‘Pyes, Tarts, Custards, Cheesecakes, and Florentines’ 같은 말이 보인다.', CAP_MAY + ' · 제목 쪽 아래', CR_MAY, U_MAY),
  'may_55': bit('may_55', '옛 활자로 찍은 영어 글줄. ‘fifty five Years Experience’와 ‘ROBERT MAY’, 맨 아래에 ‘London’과 ‘1678’이 보인다.', CAP_MAY + ' · 제목 쪽 맨 아래', CR_MAY, U_MAY),
  'fire_paul': bit('fire_paul', '불길과 연기가 하늘로 치솟는 가운데, 한가운데에 네모난 탑을 단 길고 큰 교회가 검게 드러나 있다. 둘레로 지붕과 첨탑들이 불타고 있다.', CAP_FIRE + ' · 한가운데의 큰 교회', CR_FIRE, U_FIRE),
  'fire_flee': bit('fire_flee', '어둑한 강가에 사람들이 짐 보따리를 나르고, 오른쪽에 바퀴 큰 수레와 흰 말들이 서 있다. 짐을 덮은 천들이 여기저기 쌓여 있다.', CAP_FIRE + ' · 짐을 나르는 강가', CR_FIRE, U_FIRE),
  'fire_bridge': bit('fire_bridge', '왼쪽에 달이 뜬 밤, 아치가 길게 이어진 다리 위에 높은 건물들이 서 있다. 다리 건너 오른쪽 시내에서 불길이 치솟고, 앞쪽에 배의 돛대가 보인다.', CAP_FIRE + ' · 다리와 불길', CR_FIRE, U_FIRE),
  'fire_tower': bit('fire_tower', '어두운 하늘 아래 네 모서리에 작은 탑을 얹은 하얀 성채가 높이 솟아 있고, 둘레로 둥근 탑과 성벽이 이어진다. 성벽 아래 강가에 사람들이 모여 있다.', CAP_FIRE + ' · 오른쪽의 하얀 성채', CR_FIRE, U_FIRE),
  'pepys_score': bit('pepys_score', '갈색 비단 소매 밖으로 나온 손이 접힌 종이를 들고 있다. 종이에는 오선과 음표가 그려져 있다.', CAP_PEP + ' · 손에 든 악보', CR_PEP, U_PEP),
  'pepys_face': bit('pepys_face', '긴 곱슬머리의 남자가 고개를 돌려 이쪽을 본다. 흰 목도리를 두르고 갈색 비단 옷을 입었다.', CAP_PEP + ' · 얼굴', CR_PEP, U_PEP),
  'olave_nave': bit('olave_nave', '거친 돌로 쌓은 벽에 뾰족한 아치 창이 나란히 나 있고, 앞쪽에 나무와 풀이 자란다. 뒤로 유리 건물이 조금 보인다.', CAP_OLA + ' · 아치 창이 난 돌벽', CR_OLA, U_OLA),
  'olave_tower': bit('olave_tower', '흐린 하늘 아래 벽돌 탑 꼭대기에 초록 지붕의 작은 종탑과 풍향계가 있고, 둥근 창 옆에 검은 시계가 튀어나와 있다.', CAP_OLA + ' · 탑 꼭대기', CR_OLA, U_OLA),
  'pies_candle': bit('pies_candle', '어둠 속 붉은 장식 앞에 작은 나무 모양 불빛이 켜져 있고, 아래쪽에 설탕 가루를 뿌린 파이 하나가 보인다.', CAP_PIES + ' · 작은 불빛', CR_PIES, U_PIES),
  'pies_open': bit('pies_open', '설탕 가루를 뿌린 작은 파이가 쪼개져, 속에 검붉은 말린 과일 소가 가득 보인다.', CAP_PIES + ' · 쪼갠 파이', CR_PIES, U_PIES),
 },
 'extra_credits': [{'cr': '놓아 보기 무대: 이 안내서가 그린 1666년 성탄 전야의 부엌 · 피프스의 일기와 메이의 요리책을 바탕으로', 'u': PD + '1666/12/25/'}],
 'scenes': [
  {'id': 'cook', 'label': '1660년, 요리사의 책', 'kind': 'photo', 'img': 'may',
   'text': ['1660년, 두툼한 요리책 한 권이 나왔어요. 요리사 로버트 메이(Robert May, 1588년생)의 『솜씨 좋은 요리사』(The Accomplisht Cook)예요. 영국 최초의 본격적인 요리책으로 꼽혀요.',
            '메이는 프랑스에서 5년 동안 일하며 요리를 배웠고, 가톨릭과 왕당파(내전 때 왕의 편에 선 사람들) 귀족 집안의 부엌에서 일했어요. 그의 책에는 민스파이 만드는 법이 여러 가지 실려 있어요.'],
   'quote': {'t': '소고기 엉덩잇살의 껍질을 걷어 내고 잘게 썰어요. 소기름을 넣어 함께 다지고, 후추·정향·메이스(육두구 씨를 감싼 껍질)·육두구와 소금으로 간해요. 고기의 절반만큼 건포도·커런트(작은 건포도)·말린 자두를 넣어요.',
             'from': '로버트 메이, 『솜씨 좋은 요리사』의 ‘소고기 민스파이 만들기’(1685년 판) · 이 안내서가 줄여 우리말로 옮김', 'u': MAY},
   'text2': ['책이 나온 1660년은 왕정이 돌아온 해예요. 옥스퍼드 음식 백과는 메이가 이때를 기다렸다가 책을 냈을 것이라고 봐요.',
             '피프스네 부엌이 이 책을 보았는지는 알 수 없지만, 그 시대 민스파이의 속은 이 책이 알려 줘요.'],   # 재벌 길잡이 한 줄(대변인 D · E1: 메이가 왜 나오는지)
   'kid': '옛날 요리사 아저씨가 쓴 요리책이야. 민스파이에 소고기랑 기름이랑 건포도를 넣으래!',
   'kidq': '고기랑 건포도를 같이 넣은 파이는 무슨 맛일까?'},
  {'id': 'fire', 'label': '불탄 도시의 가을', 'kind': 'photo', 'img': 'fire',
   'text': ['1666년 9월 2일 새벽 세 시쯤, 런던 해군 사무소에서 일하며 그 곁에 사는 새뮤얼 피프스(Samuel Pepys, 1633~1703)의 집. 하녀 제인이 시내에 큰불이 났다며 식구들을 깨웠어요. 불은 푸딩 레인의 왕실 빵집에서 시작됐어요.',
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
            '피프스는 세인트 올라프 교회에 가서 밀스 목사의 좋은 설교를 들었어요. 집에 와서는 아내와 남동생 존, 아내 곁에서 시중드는 새 하녀 바커와 함께 구운 소갈비와 민스파이로 잘 먹었어요.'],
   'quote': {'t': '내 마음은 참된 기쁨으로 가득했고, 오늘 내 처지가 이렇게 좋은 것을 전능하신 하나님께 감사했다.',
             'from': '새뮤얼 피프스의 일기, 1666년 12월 25일 · 이 안내서가 우리말로 옮김', 'u': PD + '1666/12/25/'},
   'text2': ['15세기에 지은 세인트 올라프 교회는 큰불을 견딘 몇 안 되는 중세 교회 가운데 하나예요. 피프스와 엘리자베스는 지금 이 교회 안에 나란히 잠들어 있어요.'],
   'kid': '성탄 아침! 피프스 아저씨는 교회에 다녀와서 소갈비랑 민스파이를 먹었어. 마음이 기쁨으로 가득했대.',
   'kidq': '성탄 아침에 우리 가족은 무엇을 먹으면 좋을까?',
   'choose': True},
  {'id': 'today', 'label': '고기가 빠진 파이', 'kind': 'photo', 'img': 'pies',
   'text': ['18세기 중반부터 민스파이는 짭짤한 고기 요리에서 달콤한 과자로 바뀌기 시작했어요. 설탕이 싸지면서 단 파이가 더 사랑받았어요.',
            '20세기에 들어서는 고기가 거의 빠졌어요. 다진 것이라는 뜻의 이름 ‘민스’만 옛 고기 파이를 기억해요.',
            '그리고 1666년 성탄 전야의 그 밤은, 피프스의 일기 한 줄이 기억해요.'],
   # 마무리 ‘기록 한 마디’: 크기가 달라진 이야기(새 사실)는 ‘더 깊이 › 알고 보면’으로 옮김
   'quote': {'t': '집안 사람들은 민스파이를 만드느라 바쁘다. 그리고 나는 잠자리에 들었다.',
             'from': '새뮤얼 피프스의 일기, 1666년 12월 24일 · 이 안내서가 우리말로 옮김', 'u': PD + '1666/12/24/'},
   'kid': '지금 민스파이에는 고기가 거의 없어. 말린 과일이 가득한 달콤한 파이야.',
   'kidq': '옛날 고기 민스파이와 지금 과일 민스파이, 너는 어떤 걸 먹어 보고 싶어?'},
 ],
 'imagine': {'t': '촛불 하나가 밝힌 겨울밤 부엌. 칼이 도마를 두드리는 소리, 정향과 육두구 냄새, 손등에 묻은 밀가루. 하품을 참는 하녀들 곁에서 엘리자베스가 긴 파이를 지켜봐요. 불탄 도시의 창밖이 희뿌옇게 밝아 오면, 성탄 아침이에요.',
             'kid': '눈을 감아 봐. 촛불 하나 켠 깜깜한 부엌이야. 탁탁탁 고기 다지는 소리, 달콤한 향신료 냄새. 하품이 나와도 꾹 참고 파이를 채워. 창밖이 밝아지면 성탄 아침이야!'},
 'lines': ['새벽 네 시까지 불이 꺼지지 않던 부엌.', '불탄 도시에도 성탄 아침은 왔어요.', '내 마음은 참된 기쁨으로 가득했다.', '고기는 빠져도 이름은 남았어요.'],
 'linesKid': ['탁탁탁, 새벽 부엌!', '성탄 아침엔 민스파이!', '고기 파이가 과일 파이로!'],
 # 마무리(키트 3판 보탬 · 기준서 1판 보탬 11): 한가운데는 1666년 성탄 전야, 새벽 네 시까지의 부엌
 'close': {'form': '기록 한 마디',
           'from': '새뮤얼 피프스의 일기 1666년 12월 24일의 한 줄 “My people busy making mince pies, and so to bed.” — 한가운데 장면인 그 밤의 기록(25일 일기의 ‘참된 기쁨’은 넷째 장면에 이미 있어서 이 줄을 골랐어요)',
           'ask': '피프스는 먼저 잠자리에 들었고, 엘리자베스와 하녀들은 새벽 네 시까지 깨어 있었어요. 그 밤 부엌에 있었다면, 나는 어디에 있었을까요?',
           'askKid': '그 밤 부엌에 있었다면, 너는 파이를 빚을래, 지켜볼래, 먼저 잘래?'},
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
  # ‘알고 보면’ 칸은 재벌(2026-11-22) 때 덜어 냈어요: 피프스 → 둘째 장면 ‘해군 사무소에서 일하며’ · 열쇠 3 / 헤일스의 초상 → portrait / 코핀 · 긴 파이에서 작은 파이로 → coffin / 커런트 → currant
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
 # 더 깊이 ‘열쇠 물음’(2026-11-22 재벌): 악마의 대변인이 막힌 곳 · 답을 알면 장면이 달라 보이는 것 · 셋이 겹치지 않고 카드의 큰 줄기를 이루는 것 · 앞면 물음에 답하는 것
 'qs': [
  {'q': '고기에 건포도라니, 원래 무슨 맛이었을까요?', 'img': 'card', 'pos': '50% 60%',
   'a': ['갈비찜에 배와 대추를 넣어 달고 짭짤하게 만드는 것과 비슷해요. 메이의 민스파이도 고기의 절반만큼 말린 과일을 넣은, 달고 짭짤한 고기 파이였어요.',
         '후추·정향·육두구는 바다 건너 들여와 아주 비쌌어요. 그래서 이런 파이는 주로 부잣집에서 큰 날에만 구웠고, ‘성탄 파이’라고도 불렸어요.'],
   'see': '셋째 장면에서 채운 재료들이, 한 해 가장 큰 날을 위한 값비싼 잔치 차림으로 보여요.', 'seeAt': 'kitchen',
   'film': [
    {'type': 'img', 'img': 'pies_open', 'fit': 'cover', 'p0': '45% 55%', 'p1': '50% 50%', 's0': 1.15, 's1': 1.02,
     'lines': [{'t': '고기에 건포도와 말린 자두라니, 이상하죠?'}, {'t': '갈비찜에 배와 대추를 넣는 것과 비슷해요.'}],
     'kid': [{'t': '고기에 건포도를 넣었대. 갈비찜처럼 달고 짭짤했겠지?'}]},
    {'type': 'black',
     'lines': [{'t': '메이의 민스파이는 고기 절반만큼 말린 과일을 넣은,'}, {'t': '달고 짭짤한 고기 파이였어요.'}],
     'kid': [{'t': '달콤하고 짭짤한 고기 파이였대!'}]},
    {'type': 'img', 'img': 'may_kick', 'fit': 'cover', 'p0': '25% 50%', 'p1': '60% 50%', 's0': 1.1, 's1': 1.0,
     'lines': [{'t': '바다 건너 온 후추·정향·육두구는 아주 비쌌어요.'}, {'t': '그래서 큰 날에만 굽는 ‘성탄 파이’였어요.'}],
     'kid': [{'t': '향신료가 아주 비싸서, 큰 잔칫날에만 구웠대.'}]},
    {'type': 'img', 'img': 'card', 'fit': 'cover', 'p0': '50% 55%', 'p1': '50% 50%', 's0': 1.1, 's1': 1.0,
     'lines': [{'t': '이제 셋째 장면을 다시 볼까요?'}, {'t': '파이에 채운 재료들이, 한 해 가장 큰 날의 값비싼 잔치 차림이에요.'}],
     'kid': [{'t': '이제 다시 보면, 아주 귀한 잔치 파이야!'}]}]},
  {'q': '‘왕정이 돌아온 해’라니, 왕이 어디 갔었어요?', 'img': 'may_face', 'pos': '50% 35%',
   'a': ['1640년대 영국은 왕의 편과 의회 편이 맞선 내전을 겪었고, 그 뒤 한동안 왕 없이 의회가 나라를 다스렸어요. 의회는 성탄이 성경이 정한 날이 아니라며 축일로 지키지 못하게 했어요.',
         '1657년 성탄에는 몰래 성찬 예배를 드리던 사람들을 군인들이 머스킷 총을 들고 둘러싸기도 했어요. 1660년 왕이 돌아오자 그 법들은 무효가 됐고, 메이의 잔치 요리책도 그해에 나왔어요.'],
   'see': '첫째 장면의 1660년 요리책이, 잔칫상이 돌아온 해에 나온 책으로 보여요.', 'seeAt': 'cook',
   'film': [
    {'type': 'black',
     'lines': [{'t': '1640년대 영국은 왕의 편과 의회 편이 맞선 내전을 겪었어요.'}, {'t': '그 뒤 의회는 성탄을 축일로 지키지 못하게 했어요.'}],
     'kid': [{'t': '옛날 영국에는 성탄 잔치를 못 하게 한 때가 있었대.'}]},
    {'type': 'img', 'img': 'pies_candle', 'fit': 'cover', 'p0': '35% 45%', 'p1': '30% 55%', 's0': 1.12, 's1': 1.02,
     'lines': [{'t': '1657년 성탄에는, 몰래 드리던 성찬 예배를'}, {'t': '군인들이 총을 들고 둘러싸기도 했어요.'}],
     'kid': [{'t': '몰래 성탄 예배를 드리던 사람들도 있었대.'}]},
    {'type': 'img', 'img': 'may_face', 'fit': 'cover', 'p0': '50% 30%', 'p1': '55% 40%', 's0': 1.15, 's1': 1.02,
     'lines': [{'t': '1660년, 왕이 돌아오고 그 법들은 무효가 됐어요.'}, {'t': '그해, 일흔한 살 요리사의 잔치 요리책이 나왔어요.'}],
     'kid': [{'t': '왕이 돌아오고, 다시 잔치를 할 수 있게 됐어!'}]},
    {'type': 'img', 'img': 'may', 'fit': 'contain', 'p0': '50% 45%', 'p1': '50% 50%', 's0': 1.06, 's1': 1.0,
     'lines': [{'t': '이제 첫째 장면을 다시 볼까요?'}, {'t': '이 요리책이, 잔칫상이 돌아온 해에 나온 책이에요.'}],
     'kid': [{'t': '이제 다시 보면, 잔치가 돌아온 해의 요리책이야!'}]}]},
  {'q': '피프스의 일기는 왜 그렇게 유명해요?', 'img': 'pepys_face', 'pos': '50% 40%',
   'a': ['피프스는 1660년부터 9년 동안 날마다 일기를 썼어요. 큰불이 난 해의 런던도 하루하루 적었지만, ‘속기’라는 기호 글자로 써서 남은 읽을 수 없었어요.',
         '일기는 그것을 읽는 법을 적은 속기 교본과 함께 모교 모들린 칼리지에 남겨졌어요. 그래도 1825년에야 처음 책이 됐어요. 열아홉 살 대학생 존 스미스가 3년 동안 풀어낸 덕분이에요.'],
   'see': '다섯째 장면 끝의 일기 한 줄이, 150년 넘게 잠들었다 깨어난 기호 글자로 보여요.', 'seeAt': 'today',
   'film': [
    {'type': 'img', 'img': 'pepys_face', 'fit': 'cover', 'p0': '50% 35%', 'p1': '50% 45%', 's0': 1.15, 's1': 1.02,
     'lines': [{'t': '피프스는 1660년부터 9년 동안 날마다 일기를 썼어요.'}, {'t': '큰불이 난 해의 런던도 하루하루 적었어요.'}],
     'kid': [{'t': '피프스 아저씨는 9년 동안 날마다 일기를 썼대.'}]},
    {'type': 'black',
     'lines': [{'t': '그런데 ‘속기’라는 기호 글자로 써서,'}, {'t': '남은 읽을 수 없었어요.'}],
     'kid': [{'t': '그런데 암호 같은 글자로 써서 아무도 못 읽었대!'}]},
    {'type': 'img', 'img': 'pepys', 'fit': 'contain', 'p0': '50% 40%', 'p1': '50% 45%', 's0': 1.0, 's1': 1.08,
     'lines': [{'t': '일기는 읽는 법을 적은 교본과 함께 모교 도서관에 남았고,'}, {'t': '1825년, 열아홉 살 대학생이 3년 동안 풀어 처음 책이 됐어요.'}],
     'kid': [{'t': '나중에 대학생 형이 3년 동안 풀어냈대!'}]},
    {'type': 'img', 'img': 'pies', 'fit': 'cover', 'p0': '50% 55%', 'p1': '50% 50%', 's0': 1.1, 's1': 1.0,
     'lines': [{'t': '이제 다섯째 장면을 다시 볼까요?'}, {'t': '마지막 일기 한 줄이, 150년 넘게 잠들었다 깨어난 글자예요.'}],
     'kid': [{'t': '이제 다시 보면, 암호 속에서 깨어난 일기야!'}]}]},
 ],
 # 더 깊이 ‘뒷이야기’(2026-11-22 재벌): 근거를 찾은 물음은 모두 카드로(열여덟). 꾸러미 1은 사람 하나의 이야기 · 놀라움 · 단단한 근거 · 그림이 몰리지 않게 창이 고름.
 # 꾸러미 2는 꾸러미 1에서 이어지게(gold→monument · frogs→may71 · frogs→titlewords · portrait→books · elizabeth→y1662 · elizabeth→olaf), 꾸러미 3은 2에서(monument→paul · gold→penn · titlewords→figures200 · 열쇠 1→currant · coffin→meatgone · herrick→christmaseve)
 'qx': [
  # 꾸러미 1
  {'id': 'elizabeth', 'pack': 1, 'q': '밤새 깨어 있던 엘리자베스는 어떤 사람이었을까요?', 'hook': '남편 초상 곁, 사라진 초상', 'img': 'olave_nave', 'pos': '55% 55%',
   'a': ['엘리자베스는 1640년 영국 데번에서 태어나, 열다섯 살에 스물두 살 피프스와 결혼했어요. 1666년 화가 헤일스는 남편의 초상과 짝으로 걸렸을 그녀의 초상도 그렸지만, 그 그림은 19세기에 없어졌어요.',
         '1669년, 프랑스와 네덜란드를 여행하다 얻은 열병으로 그녀는 스물아홉에 세상을 떠났어요. 피프스는 세인트 올라프 교회 제단 둘레 벽, 예배 때 늘 보이는 자리에 그녀의 대리석 흉상을 세웠어요.'],
   'see': '넷째 장면의 교회가, 엘리자베스가 남편보다 먼저 잠든 곳으로 보여요.', 'seeAt': 'morning', 'seeImg': 'olave',
   'src': [{'t': '모들린 칼리지 문서고 「엘리자베스 피프스(1640~1669)」', 'm': '영어 · 1640년 10월 23일 데번 비데퍼드에서 태어남, 1655년 12월 1일 결혼(열다섯 · 스물둘), 1669년 프랑스·네덜란드 여행에서 얻은 열병, 11월 10일 스물아홉에 세상을 떠남(옥스퍼드 인명사전을 따름)', 'u': MAGD_EP},
           {'t': '영국 국립초상화미술관 「엘리자베스 피프스」 판화(NPG D5507) 설명', 'm': '영어 · 1666년 2월 헤일스에게 맡긴 아내의 초상, 피프스 초상과 짝으로 걸렸을 것, 성녀 카타리나의 모습, 그림은 19세기에 없어짐', 'u': NPG_EP},
           {'t': '세인트 올라프 교회 「Our Story」', 'm': '영어 · 1669년 열병으로 세상을 떠나 교회에 묻힘, 제단 둘레 북쪽 벽의 대리석 흉상(예배 때 보이는 자리), 1703년 피프스도 아내 곁에 묻힘', 'u': OLAVE}]},
  {'id': 'herrick', 'pack': 1, 'q': '성탄 전야, 파이를 밤새 지키라는 시가 있었다고요?', 'hook': '오늘 밤 파이를 지켜라!', 'img': 'pies_candle', 'pos': '35% 70%',
   'a': ['시인 로버트 헤릭(1591~1674)은 1648년 시집에 「성탄 전야, 또 하나의 의식」을 실었어요. ‘오늘 밤 성탄 파이를 지켜라, 아무리 날랜 도둑도 고기 갈고리를 들고 다가오지 못하게.’',
         '헤릭은 데번의 시골 목사였어요. 왕의 편에 선 국교회 목사라는 까닭으로 1647년 교회에서 쫓겨났다가, 1660년 다시 그 교회로 돌아갔어요.'],
   'see': '셋째 장면의 깨어 있는 밤이, 시 속에서 성탄 파이를 지키던 밤과 겹쳐 보여요.', 'seeAt': 'kitchen',
   'src': [{'t': '로버트 헤릭 「Christmas-Eve, Another Ceremony」(『헤스페리데스』 1648)', 'm': '영어 · 루미나리움(폴러드 편 1891년 판) · 오늘 밤 성탄 파이를 지켜 고기 갈고리를 든 도둑이 다가오지 못하게 하라는 시', 'u': LUMIN},
           {'t': '포에트리 파운데이션 「로버트 헤릭」', 'm': '영어 · 1591년 세례, 1630년 데번 딘 프라이어 교회 목사, 1647년 왕당파·국교회 목사로 쫓겨남, 1648년 『헤스페리데스』, 1660년 돌아감, 1674년 세상을 떠남', 'u': POETF}]},
  {'id': 'gold', 'pack': 1, 'q': '불길이 다가올 때, 피프스는 무엇을 지켰을까요?', 'hook': '금을 지킨 방, 일기를 맡긴 집', 'img': 'fire_flee', 'pos': '60% 55%',
   'a': ['큰불 동안 피프스는 바로 이 일기장을 귀중품과 함께 시 밖 윌리엄 라이더 경의 집으로 보냈어요. 9월 5일에는 금 2,350파운드어치를 배에 싣고 울리치로 옮겼고, 엘리자베스에게 금을 둔 방을 절대 떠나지 말라고 했어요.',
         '돌아와 보니 집은 타지 않았어요. 집들을 폭파해 불길을 끊고, 왕실 조선소 일꾼들이 도운 덕분이었어요.'],
   'see': '둘째 장면 앞쪽 짐 실은 수레들이, 저마다 지키고 싶은 것을 싣고 가는 사람들로 보여요.', 'seeAt': 'fire', 'seeImg': 'fire',
   'src': [{'t': '새뮤얼 피프스의 일기, 1666년 9월 5일', 'm': '영어 · 금 약 2,350파운드를 배로 울리치에, 아내에게 금을 잠가 둔 방을 떠나지 말라고 함, 집이 타지 않음, 집 폭파와 왕실 조선소 일꾼들의 도움', 'u': PD + '1666/09/05/'},
           {'t': '케이트 러브먼 「Women and the History of Samuel Pepys’s Diary」(『히스토리컬 저널』 65, 2022)', 'm': '영어 · 큰불 때 일기장을 귀중품과 함께 시 밖 윌리엄 라이더 경의 집으로 보냄', 'u': HJ_LOVEMAN}]},
  {'id': 'portrait', 'pack': 1, 'q': '피프스는 왜 펜 대신 악보를 들고 있을까요?', 'hook': '목이 부러질 뻔한 초상', 'img': 'pepys_score', 'pos': '25% 45%',
   'a': ['악보는 피프스가 직접 곡을 붙인 노래 「아름다움이여, 물러가라」예요. 그는 그림을 위해 인도풍 가운을 빌려 입었어요.',
         '1666년 3월 17일부터 화가 헤일스 앞에 앉았는데, 어깨 너머로 돌아보는 자세를 버티느라 ‘목이 부러질 뻔했다’고 일기에 적었어요. 5월 16일 그림값 14파운드와 액자값 25실링을 치렀어요.'],
   'see': '넷째 장면의 초상이, 빌린 가운을 입고 고개를 돌린 채 버틴 노래꾼으로 보여요.', 'seeAt': 'morning', 'seeImg': 'pepys',
   'src': [{'t': '런던 국립초상화미술관 NPG 211 「새뮤얼 피프스」(존 헤일스, 1666)', 'm': '영어 · 1666년 3월 17일 첫 앉기, 어깨 너머로 돌아보느라 목이 부러질 뻔했다는 일기, 빌린 인도풍 가운, 데버넌트의 노랫말에 피프스가 곡을 붙인 「Beauty, retire」, 5월 16일 14파운드와 액자값 25실링', 'u': NPG211}]},
  {'id': 'frogs', 'pack': 1, 'q': '메이의 잔칫상 파이에서는 무엇이 튀어나왔을까요?', 'hook': '파이를 열자 개구리가!', 'img': 'may_face', 'pos': '50% 40%',
   'a': ['메이는 성탄 잔치의 마지막 날인 열두째 날을 위해, 판지로 만든 배와 성에서 화약이 터지고 화살 맞은 사슴 과자에서 포도주가 피처럼 흐르는 상을 적었어요. 끝으로 파이 뚜껑을 열면 산 개구리가 뛰어나오고, 산 새들이 날아올라 촛불을 꺼요.',
         '1970년대 음식사학자 아이번 데이가 친구 생일에 이를 재현했더니, 개구리는 꼼짝하지 않았고 카나리아는 방을 날았지만 촛불을 끄지 못했대요.'],
   'see': '첫째 장면의 요리사가, 파이 하나로 잔칫상을 무대로 만들던 연출가로 보여요.', 'seeAt': 'cook', 'seeImg': 'may',
   'src': [{'t': '트리니티 홀(케임브리지) 「Seventeenth-century cookery: don’t try this at home」(제인 파트너)', 'm': '영어 · 메이(1685년 판)의 ‘요리의 승리와 트로피’: 열두째 날 같은 잔치, 판지 배와 성, 화살 맞은 사슴에서 흐르는 포도주, 산 개구리와 새가 든 파이, 새들이 촛불을 끔', 'u': TRINH},
           {'t': '리즈 대학 도서관 특별 장서 「Triumphs and Trophies in Cookery」', 'm': '영어 · 화약으로 터지는 모형, 달콤한 물을 넣은 달걀 껍데기, 마지막에 파이에서 나오는 산 개구리와 새 · 메이는 왕정이 돌아온 해에 씀', 'u': LEEDS},
           {'t': '아이번 데이 블로그 「An Early Modern Christmas Party」(2013년 12월 14일)', 'm': '영어 · 열두째 날은 성탄 휴일 끝의 가장 큰 잔치, 1970년대 친구의 스물한 살 생일에 카나리아 세 마리와 개구리 다섯 마리로 재현, 개구리는 꼼짝 않고 카나리아는 촛불을 못 끔', 'u': IDAY13}]},
  {'id': 'coffin', 'pack': 1, 'q': '옛 민스파이의 단단한 껍질은 먹었을까요?', 'hook': '먹지 않는 파이 껍질', 'img': 'card', 'pos': '50% 75%',
   'a': ['옛 파이 껍질은 ‘코핀’이라고 불렀어요. 원래 파이를 담는 상자라는 뜻이에요. 밀가루와 물로만 빚어, 속이 익고 나면 너무 단단해 거의 먹을 수 없었어요. 그래서 남은 껍질은 가난한 이웃이나 짐승에게 주곤 했어요.',
         '파이는 온 식구와 손님이 한자리에서 나눠 먹을 만큼 크고 길쭉했어요. 나중에 반죽에 기름을 넣어 부드러워지면서 껍질도 먹게 됐어요.'],
   'see': '셋째 장면에서 세운 긴 껍질이, 먹는 과자가 아니라 속을 굽는 그릇으로 보여요.', 'seeAt': 'kitchen',
   'src': [{'t': '컨트리 라이프(2022년 12월 3일) 「민스파이에 정말 고기가 들었을까?」(마틴 폰)', 'm': '영어 · 밀가루와 물로 빚은 단단한 코핀, 버리거나 가난한 이와 짐승에게, 뒤에 기름을 넣어 먹게 됨, 온 식구와 손님이 한자리에서 먹을 만큼 크고 길쭉한 파이', 'u': CL},
           {'t': '아이번 데이 블로그 「Shaped Minc’d Pies Again」(2011년 12월 24일)', 'm': '영어 · ‘코핀’은 원래 모든 파이 껍질(파이 상자)을 뜻함', 'u': IDAY11}]},
  # 꾸러미 2
  {'id': 'monument', 'pack': 2, 'q': '불이 시작된 빵집 자리에는 지금 무엇이 있을까요?', 'hook': '눕히면 빵집에 닿는 기둥', 'img': 'fire_bridge', 'pos': '75% 45%',
   'a': ['큰불을 기억하는 돌기둥 ‘모뉴먼트’가 1670년대에 세워졌어요. 높이 61.6미터로, 옆으로 눕히면 꼭대기가 불이 시작된 푸딩 레인 빵집 자리에 닿는대요.',
         '세인트 폴 대성당을 다시 지은 크리스토퍼 렌과 로버트 훅이 설계했어요. 속이 빈 기둥은 아래 작은 실험실에서 별을 보는 망원경으로도 쓰려 했지만, 둘레 길의 떨림 때문에 잘 맞지 않았대요. 311계단을 오르면 런던이 내려다보여요.'],
   'see': '둘째 장면의 불길이 시작된 곳이, 지금은 61.6미터 돌기둥이 가리키는 자리로 보여요.', 'seeAt': 'fire',
   'src': [{'t': '런던 박물관 「The Monument to the Great Fire of London」', 'm': '영어 · 높이 61.6미터, 눕히면 꼭대기가 토머스 패리너의 푸딩 레인 빵집에 닿음, 렌과 그의 조수 훅이 설계, 1671~1677년, 아래 실험실과 천정 망원경(떨림으로 정확하지 않음), 311계단', 'u': MON}]},
  {'id': 'may71', 'pack': 2, 'q': '메이는 몇 살에 이 책을 냈을까요?', 'hook': '일흔한 살 요리사의 책', 'img': 'may_55', 'pos': '50% 30%',
   'a': ['초상 옆에는 작게 ‘(나이) 71, 1660’이라는 라틴어 글귀가 새겨져 있어요. 1660년에 일흔한 살이었다는 뜻이에요. 메이는 열서너 살부터 요리사로 일했고, 도머 부인이 그를 프랑스로 보내 5년 동안 일하며 배우게 했어요.',
         '제목 쪽 아래에는 ‘55년의 경험’이라고 적혀 있어요. 450쪽이 넘는 책에 요리법이 1,000가지가 넘어요.'],
   'see': '첫째 장면의 초상이, 일흔한 살에 평생의 부엌을 한 권에 담은 요리사로 보여요.', 'seeAt': 'cook', 'seeImg': 'may',
   'src': [{'t': '옥스퍼드 음식 백과 ‘로버트 메이’(ckbk)', 'm': '영어 · 1588년생, 열서너 살부터 요리사, 도머 부인이 프랑스로 보내 5년, 450쪽 넘는 책에 1,000가지 넘는 요리법', 'u': CKBK},
           {'t': '위키미디어 공용: 『솜씨 좋은 요리사』 1678년 판 앞 그림과 제목 쪽(미국 의회도서관)', 'm': '그림 속 글씨 · 초상 옆 ‘(나이) 71, 1660’, 제목 쪽 ‘fifty five Years Experience’', 'u': U_MAY}]},
  {'id': 'titlewords', 'pack': 2, 'q': '요리책 제목에 웬 ‘비밀(MYSTERY)’과 ‘바느질(SEWING)’이에요?', 'hook': '바느질하는 요리책?', 'img': 'may_kick', 'pos': '60% 70%',
   'a': ['옛 영어의 mystery에는 ‘비밀’ 말고 ‘손기술, 직업’이라는 뜻도 있었어요. 제목은 ‘요리의 기술과 솜씨’라는 말이에요.',
         'SEWING도 바느질이 아니에요. 옛 귀족 집에는 잔칫상에 음식을 차려 내는 ‘수어(sewer)’라는 지위 높은 시중꾼이 있었어요. ‘CARVING and SEWING’은 고기 썰기와 상 내기에 쓰는 말들이에요. s가 f처럼 생긴 글자는 1800년 무렵까지 인쇄에 쓰던 ‘긴 s’예요.'],
   'see': '첫째 장면의 제목 쪽이, 잔칫상을 차리는 사람들의 솜씨 책으로 읽혀요.', 'seeAt': 'cook', 'seeImg': 'may',
   'src': [{'t': '메리엄-웹스터 사전 ‘mystery’(명사 2)', 'm': '영어 · 옛말: 손기술, 직업, 동업 조합', 'u': MW + 'mystery'},
           {'t': '메리엄-웹스터 사전 ‘sewer’(명사 3)', 'm': '영어 · 중세 귀족 집에서 상에 음식을 차려 내던, 흔히 지위 높은 시중꾼', 'u': MW + 'sewer'},
           {'t': '위스콘신 대학 도서관 특별 장서 「The Long S, Now Largely Extinct」(2015년 10월 4일)', 'm': '영어 · s 자리에 f처럼 보이는 글자, 영국 인쇄에서는 1800년 무렵 사라짐', 'u': UWLS}]},
  {'id': 'books', 'pack': 2, 'q': '성탄 오후, 피프스는 무엇을 했을까요?', 'hook': '성탄 오후의 책 정리', 'img': 'pepys_face', 'pos': '50% 45%',
   'a': ['1666년 성탄 오후, 피프스는 아내와 바커에게 자기 노래 「정해졌노라(It is decreed)」를 가르쳤어요. 저녁까지는 동생과 함께 책 이름을 알파벳 차례로 정리했대요(일기).',
         '바로 그해 그는 책장도 직접 설계했어요. 그 참나무 책장들은 지금도 케임브리지 모들린 칼리지에서 그의 책과 일기를 담고 있어요.'],
   'see': '넷째 장면의 성탄 하루가, 식탁을 지나 책장 앞에서 저무는 하루로 보여요.', 'seeAt': 'morning', 'seeImg': 'pepys',
   'src': [{'t': '새뮤얼 피프스의 일기, 1666년 12월 25일', 'm': '영어 · 오후에 아내와 바커에게 자기 노래 「It is decreed」를 가르침, 저녁까지 동생과 책 이름을 알파벳 차례로 정리', 'u': PD + '1666/12/25/'},
           {'t': '모들린 칼리지 「피프스 도서관」', 'm': '영어 · 1666년 피프스가 설계한 참나무 책장에 지금도 그의 책과 일기 원본을 보관(건물을 고치느라 2027년까지 방문을 받지 않음)', 'u': MAGD_LIB}]},
  {'id': 'y1662', 'pack': 2, 'q': '앞면 카드의 1662년 성탄, 피프스는 왜 민스파이를 사 왔을까요?', 'hook': '아내가 앓던 성탄', 'img': 'pies', 'pos': '50% 50%',
   'a': ['그날 엘리자베스는 몸이 아파 누워 있었어요. 피프스는 일기에 ‘아내가 아직 아파 손수 만들 수 없어서’ 민스파이 하나를 밖에서 사 오게 했다고 적었어요.',
         '둘은 그녀의 침대 곁에서 ‘플럼 포리지’ 한 그릇과 구운 영계로 성탄 식사를 했어요. 4년 뒤 성탄 전야, 그녀는 새벽 네 시까지 하녀들의 파이 빚기를 지켜보았어요.'],
   'see': '셋째 장면의 밤샘이, 파이를 사 와야 했던 4년 전과는 다른 성탄으로 보여요.', 'seeAt': 'kitchen',
   'src': [{'t': '새뮤얼 피프스의 일기, 1662년 12월 25일', 'm': '영어 · 아내가 아파 손수 만들 수 없어 민스파이를 밖에서 사 오게 함, 플럼 포리지와 구운 영계, 아내의 침대 곁에서 식사', 'u': PD + '1662/12/25/'}]},
  {'id': 'olaf', 'pack': 2, 'q': '교회 이름 ‘올라프’는 누구예요?', 'hook': '런던 교회의 노르웨이 왕', 'img': 'olave_tower', 'pos': '50% 50%',
   'a': ['노르웨이의 왕 올라프 2세예요. 교회는 그가 1014년 런던 다리 싸움에서 잉글랜드 왕 애설레드 편에 서서 데인족 군대와 싸웠다고 소개해요. 그는 노르웨이에 기독교를 퍼뜨렸고, 1030년 세상을 떠난 뒤 성인으로 기려져 노르웨이의 수호성인이 됐어요.',
         '1941년 폭격으로 교회가 크게 부서지자, 노르웨이 왕 호콘 7세가 1951년 머릿돌을 놓고 1954년 다시 봉헌했어요.'],
   'see': '넷째 장면의 작은 교회가, 바다 건너 노르웨이 왕의 이름을 품은 곳으로 보여요.', 'seeAt': 'morning', 'seeImg': 'olave',
   'src': [{'t': '세인트 올라프 교회 「Our Story」', 'm': '영어 · 노르웨이 왕 올라프 2세, 1014년 런던 다리 싸움에서 애설레드 편, 루앙에서 세례, 1030년 뒤 성인·노르웨이의 수호성인, 1941년 폭격, 1951년 호콘 7세의 머릿돌, 1954년 봉헌', 'u': OLAVE}]},
  # 꾸러미 3
  {'id': 'paul', 'pack': 3, 'q': '그림 한가운데 가장 크게 타는 건물은 무엇일까요?', 'hook': '책 창고가 된 대성당', 'img': 'fire_paul', 'pos': '45% 55%',
   'a': ['옛 세인트 폴 대성당이에요. 이 그림은 1666년 9월 4일 화요일 밤 8~9시쯤, 런던탑 부두 가까운 배에서 본 모습을 그렸어요. 오른쪽 하얀 성이 런던탑, 왼쪽 아치 다리가 옛 런던 다리예요.',
         '대성당은 고치려고 막 둘러친 나무 비계에 불티가 옮겨붙었어요. 둘레 책방들이 대성당 지하에 맡겨 둔 책들도 함께 탔어요. 시내 교회 109곳 가운데 87곳이 불탔어요.'],
   'see': '둘째 장면 한가운데 불길이, 대성당과 책들이 함께 타던 9월 4일 밤으로 보여요.', 'seeAt': 'fire', 'seeImg': 'fire',
   'src': [{'t': '런던 박물관 「the great fire of london」(57.54)', 'm': '영어 · 1666년 9월 4일 화요일 저녁 8~9시쯤, 런던탑 부두 근처 배에서 본 모습 · 높이 흩날리는 불티 같은 세부가 목격자를 짐작하게 함 · 1666~1675년, 네덜란드 화파', 'u': LM_FIRE},
           {'t': '런던 박물관 그림 인화 「The Great Fire of London 1666」 설명', 'm': '영어 · 옛 런던 다리, 집들, 여러 교회와 옛 세인트 폴, 런던탑', 'u': MOLP},
           {'t': '처치 타임스(2016년 9월 2일) 「Alight by the hand of God」(피터 스트리트)', 'm': '영어 · 9월 4일 저녁 세인트 폴에 불, 수리용 나무 비계, 책방들이 성 페이스 지하에 옮긴 책들, 시내 교회 109곳 가운데 87곳', 'u': CHT}]},
  {'id': 'penn', 'pack': 3, 'q': '피프스와 포도주를 묻은 이웃 펜 경은 누구예요?', 'hook': '펜실베이니아의 ‘펜’', 'img': 'fire_tower', 'pos': '50% 40%',
   'a': ['해군 제독 윌리엄 펜(1621~1670)이에요. 1665년 로스토프트 해전에서 함대를 이끈 함장이었어요.',
         '그의 아들 이름도 윌리엄 펜이에요. 퀘이커교도가 된 아들은 1682년 아메리카에 영국 식민지를 세웠어요. 찰스 2세는 아버지를 기려 그 땅 이름 앞에 ‘펜’을 붙이라고 했어요. 오늘날 미국의 펜실베이니아주예요.'],
   'see': '둘째 장면의 ‘이웃 펜 경’이, 미국 한 주의 이름 속에 남은 아버지로 보여요.', 'seeAt': 'fire',
   'src': [{'t': '영국 국립해양박물관(그리니치) 「Flagmen of Lowestoft: Admiral Sir William Penn, 1621-70」', 'm': '영어 · 1665년 로스토프트 해전의 함대 함장, 퀘이커교도 아들이 1682년 펜실베이니아를 세움, 찰스 2세의 명으로 아버지를 기려 ‘펜’을 붙임', 'u': RMG_PENN}]},
  {'id': 'figures200', 'pack': 3, 'q': '제목 쪽의 ‘그림 200개’는 어떤 그림이었을까요?', 'hook': '파이 모양 도안 200개', 'img': 'may_figures', 'pos': '50% 50%',
   'a': ['넷째 판 제목 쪽에는 고기·생선 파이와 타르트, 커스터드, 치즈케이크, 플로렌틴 같은 구운 요리의 모양 그림 200개를 실었다고 적혀 있어요.',
         '음식사학자 아이번 데이에 따르면 17세기 민스파이는 놀랄 만큼 갖가지 모양으로 빚었어요. 메이 같은 요리책 저자들은 작은 파이 여럿을 정원 화단처럼 늘어놓는 도안을 냈대요.'],
   'see': '첫째 장면 제목 쪽의 작은 글씨가, 갖가지 모양 파이의 도안집 광고로 읽혀요.', 'seeAt': 'cook', 'seeImg': 'may',
   'src': [{'t': '위키미디어 공용: 『솜씨 좋은 요리사』 1678년 넷째 판 제목 쪽(미국 의회도서관)', 'm': '그림 속 글씨 · ‘two hundred Figures of several Forms … as Pyes, Tarts, Custards, Cheesecakes, and Florentines’', 'u': U_MAY},
           {'t': '아이번 데이 블로그 「Shaped Minc’d Pies Again」(2011년 12월 24일)', 'm': '영어 · 1654~1751년에 나온 갖가지 파이 모양 도안, 메이와 키더의 정원 화단 같은 파이 배치 도안', 'u': IDAY11}]},
  {'id': 'currant', 'pack': 3, 'q': '‘커런트’는 어디서 온 건포도예요?', 'hook': '코린트에서 온 건포도', 'img': 'pies_open', 'pos': '45% 55%',
   'a': ['커런트는 씨 없는 작은 건포도예요. 이름부터 그리스의 도시 코린트에서 왔어요. ‘코린트의 건포도’가 줄어든 말이래요.',
         '1640년 뒤 영국 의회는 한때 커런트 수입을 막았다가, 그리스에서 들여오는 커런트에 세금을 매겨 포위된 도시 글로스터를 도왔어요. 고기와 소금에도 세금이 붙어, 그 시절 성탄 상은 그만큼 비싸졌어요.'],
   'see': '첫째 장면 요리책의 ‘커런트’가, 바다 건너 그리스에서 온 값비싼 재료로 보여요.', 'seeAt': 'cook',
   'src': [{'t': '메리엄-웹스터 사전 ‘currant’', 'm': '영어 · 지중해 동쪽에서 나던 씨 없는 작은 건포도, ‘코린트의 건포도’에서 온 이름', 'u': MW + 'currant'},
           {'t': '영국 의회 역사 연구소(2020년 12월 23일) 「Did the Puritans ban Christmas dinner?」(스티븐 로버츠)', 'm': '영어 · 1640년 뒤 한때 커런트 수입 금지, 그리스산 커런트에 세금을 매겨 포위된 글로스터를 도움, 1643년부터 고기·소금 등에 붙은 세금, 성탄 식사가 비싸졌을 것', 'u': HOP20}]},
  {'id': 'meatgone', 'pack': 3, 'q': '고기는 언제, 어떻게 빠졌을까요?', 'hook': '아직 남은 소기름', 'img': 'card', 'pos': '50% 50%',
   'a': ['1747년 해나 글래스의 요리책에서 고기는 넣어도 빼도 되는 재료가 됐어요. 1861년 비턴 부인의 책에는 고기가 든 것과 없는 것이 함께 실렸고, 20세기에 들어 고기는 거의 빠졌어요.',
         '그래도 전통 조리법은 지금도 파이 속 재료인 민스미트에 소기름을 넣어요. 그래서 채식하는 사람을 위해 소기름을 뺀 민스미트를 따로 만들기도 해요.'],
   'see': '다섯째 장면의 과일 파이가, 소기름으로 옛 고기 파이와 이어진 과자로 보여요.', 'seeAt': 'today', 'seeImg': 'pies',
   'src': [{'t': '컨트리 라이프(2022년 12월 3일) 「민스파이에 정말 고기가 들었을까?」', 'm': '영어 · 18세기 중반부터 단 음식으로, 1747년 해나 글래스(고기는 넣어도 그만), 1861년 비턴 부인(고기 있는 것과 없는 것), 20세기에는 거의 고기 없음', 'u': CL},
           {'t': '딜리셔스 매거진 「Pear and apple mincemeat」(애나 하이엄, 2019)', 'm': '영어 · 민스파이는 전통적으로 소기름을 넣음, 채식에 맞게 뺀 조리법', 'u': DELI}]},
  {'id': 'christmaseve', 'pack': 3, 'q': '성탄 전날 밤에 고기 파이를 빚어도 됐어요?', 'hook': '금식하는 밤의 고기 파이', 'img': 'olave_nave', 'pos': '30% 50%',
   'a': ['1662년 영국 국교회 기도서는 성탄 전날을 ‘전야(비질)’로, 금식하거나 절제하는 날의 목록에 올렸어요. 한 해 모든 금요일도 그런 날이었는데, 성탄절이 금요일이면 그날만은 뺐어요.',
         '피프스네가 그 밤 무엇을 먹었는지는 일기에 없어요. 밤새 빚은 파이는 이튿날 성탄 상에 올릴 것이었어요.'],
   'see': '셋째 장면의 밤 부엌이, 금식하는 밤에 이튿날 잔치를 준비하는 손으로 보여요.', 'seeAt': 'kitchen',
   'go': {'t': '「일곱 가지 생선 만찬」 카드로 가기', 'cid': 'tb-fishes'},
   'src': [{'t': '영국 국교회 『공동 기도서』(1662) 「A Table of the Vigils, Fasts, and Days of Abstinence」', 'm': '영어 · 성탄 전야를 비롯한 전야들, 사순절 40일 같은 금식·절제의 날, 한 해 모든 금요일(성탄절은 뺌)', 'u': BCP},
           {'t': '새뮤얼 피프스의 일기, 1666년 12월 24·25일', 'm': '영어 · 24일 밤 집안 사람들이 민스파이를 만듦, 25일 성탄 식사에 소갈비와 민스파이', 'u': PD + '1666/12/25/'}]},
 ],
 # 후보 모두(2026-11-22 재벌): 악마의 대변인의 A·B·C·G · 창 · 본 카드 ‘알고 보면’ 칸에서. 열쇠는 pick, 뒷이야기는 x, 녹이거나 남긴 것은 at에 자리를 적어요.
 'qcand': [
  {'q': '고기에 건포도랑 자두라니, 무슨 맛이었어요? 단짠 갈비찜 같은 거?', 'at': '악마의 대변인 · B9 · G(맛이 제일 궁금) · C(앞면 사진은 오늘 파이) · 앞면 물음', 'a': '고기 절반만큼의 말린 과일, 값비싼 향신료, 큰 날의 ‘성탄 파이’ — 메이 요리책·컨트리 라이프', 'pick': 1, 'see': '셋째 장면의 재료들이 값비싼 잔치 차림으로 보여요.'},
  {'q': '왕정이 돌아온 해? 왕이 어디 갔었어요? 왜 그때를 기다려 책을 냈어요?', 'at': '악마의 대변인 · A(왕정·왕당파·옥스퍼드 음식 백과) · B11 · D(첫째 장면이 지루함) · E1', 'a': '내전, 의회의 성탄 축일 금지(성경에 정한 날이 아님), 1657년 성찬 예배와 군인, 1660년 무효 — 영국 의회 역사 연구소·역사 연구소 블로그', 'pick': 1, 'see': '첫째 장면의 요리책이 잔칫상이 돌아온 해의 책으로 보여요.'},
  {'q': '피프스 일기가 왜 그렇게 유명해요? 그냥 아저씨 일기 아니에요?', 'at': '악마의 대변인 · A(일기 작가) · B1 · D · E6 · G', 'a': '1660~1669년 속기 일기, 읽는 법 교본과 함께 모교에, 1825년 존 스미스가 3년 동안 풀어 첫 책 — 모들린 칼리지·히스토리 투데이', 'pick': 1, 'see': '마지막 일기 한 줄이 150년 넘게 잠들었다 깨어난 글자로 보여요.'},
  {'x': 'elizabeth', 'q': '밤새운 아내 얼굴은 왜 없어요? 엘리자베스는 어떤 사람?', 'at': '악마의 대변인 · C(없는 그림: 엘리자베스) · F · B15(교회 안에 묻혔다고?) · 꾸러미 1', 'a': '1640년생, 열다섯에 결혼, 헤일스의 짝 초상은 19세기에 없어짐, 1669년 열병, 대리석 흉상 — 모들린 문서고·국립초상화미술관·세인트 올라프', 'see': '넷째 장면의 교회가 엘리자베스가 먼저 잠든 곳으로 보여요.'},
  {'x': 'herrick', 'q': '성탄 전야에 파이를 지키는 풍습이 있었어요?', 'at': '창(B3 ‘왜 지켜만 봤어?’에서 — 일기에는 까닭이 없어 그 시대의 시를 찾음) · 꾸러미 1', 'a': '헤릭 「성탄 전야, 또 하나의 의식」(1648), 1647년 쫓겨난 시골 목사 — 루미나리움·포에트리 파운데이션', 'see': '깨어 있는 밤이 파이를 지키는 밤과 겹쳐 보여요.'},
  {'x': 'gold', 'q': '불이 다가올 때 피프스는 치즈 말고 무엇을 지켰어요? 피프스 집은 어떻게 됐어요?', 'at': '악마의 대변인 · B6 · B5(치즈) · 꾸러미 1', 'a': '일기장과 귀중품을 라이더 경 집으로, 금을 울리치로, 집은 타지 않음 — 일기 9월 5일·러브먼', 'see': '앞쪽 수레들이 저마다 지키려는 것을 싣고 가는 사람들로 보여요.'},
  {'x': 'portrait', 'q': '일기 작가라면서 펜이 아니라 악보? 잠옷 같은 가운은?', 'at': '악마의 대변인 · C(피프스 초상) · 본 카드 ‘알고 보면’ 칸(헤일스의 초상) · 꾸러미 1', 'a': '자기가 곡을 붙인 「Beauty, retire」, 빌린 인도풍 가운, 목이 부러질 뻔한 자세 — 국립초상화미술관', 'see': '초상이 고개를 돌린 채 버틴 노래꾼으로 보여요.'},
  {'x': 'frogs', 'q': '메이의 잔칫상은 얼마나 화려했어요?', 'at': '창(대변인 D ‘첫째 장면은 정보만’에서 — 메이를 사람으로) · 꾸러미 1', 'a': '열두째 날의 판지 배·성·사슴, 산 개구리와 새 파이, 1970년대 아이번 데이의 재현 — 트리니티 홀·리즈 대학 도서관·아이번 데이', 'see': '요리사가 잔칫상을 무대로 만든 연출가로 보여요.'},
  {'x': 'coffin', 'q': '긴 파이 껍질을 ‘세운다’는 게 뭐예요? 그 껍질도 먹었어요?', 'at': '악마의 대변인 · A(영화 ‘껍질을 세우고’) · B10 · 본 카드 ‘알고 보면’ 칸(코핀 · 긴 파이에서 작은 파이로) · 꾸러미 1', 'a': '밀가루와 물로 빚은 단단한 코핀, 가난한 이와 짐승에게, 크고 길쭉한 파이 — 컨트리 라이프·아이번 데이', 'see': '세운 껍질이 속을 굽는 그릇으로 보여요.'},
  {'x': 'monument', 'q': '불을 낸 왕실 빵집은 어떻게 됐어요?', 'at': '악마의 대변인 · B7(빵집 사람은 벌 받았어? — 사람 이야기 대신 그 자리 이야기로) · 꾸러미 2', 'a': '61.6미터 모뉴먼트, 눕히면 빵집에 닿음, 렌과 훅, 망원경 — 런던 박물관', 'see': '불이 시작된 곳이 돌기둥이 가리키는 자리로 보여요.'},
  {'x': 'may71', 'q': '1588년생이면 일흔 넘어서 책을 낸 거죠? 55년 경력은 진짜예요?', 'at': '악마의 대변인 · B12 · C(초상 옆 ‘71’, ‘1660’) · 꾸러미 2', 'a': '초상 옆 ‘(나이) 71, 1660’, 열서너 살부터 요리사, 프랑스 5년, ‘55년의 경험’ — 옥스퍼드 음식 백과·그림 속 글씨', 'see': '초상이 평생의 부엌을 한 권에 담은 요리사로 보여요.'},
  {'x': 'titlewords', 'q': '제목의 Mystery, 요리책에 웬 SEWING(바느질)? s가 f처럼 생긴 건 오타?', 'at': '악마의 대변인 · C(메이 그림 셋) · 꾸러미 2', 'a': 'mystery = 손기술·직업, sewer = 상을 차려 내는 시중꾼, 긴 s — 메리엄-웹스터·위스콘신 대학 도서관', 'see': '제목 쪽이 잔칫상 솜씨 책으로 읽혀요.'},
  {'x': 'books', 'q': '성탄 점심 뒤에 피프스는 뭘 했어요?', 'at': '창(12월 25일 일기를 다시 열어 읽다가) · 꾸러미 2', 'a': '아내와 바커에게 노래를 가르치고 동생과 책 목록 정리, 1666년에 설계한 책장이 지금도 모들린에 — 일기·모들린 칼리지', 'see': '성탄 하루가 책장 앞에서 저무는 하루로 보여요.'},
  {'x': 'y1662', 'q': '앞면 카드에서 1662년엔 민스파이를 ‘사 왔다’던데 왜요?', 'at': '창(앞면 카드 글 ‘1662년 성탄절, 피프스는 민스파이를 사 오게 했다’에서) · 꾸러미 2', 'a': '아내가 아파 손수 만들 수 없어서, 침대 곁 성탄 식사 — 일기 1662년 12월 25일', 'see': '셋째 장면의 밤샘이 4년 전과 다른 성탄으로 보여요.'},
  {'x': 'olaf', 'q': '세인트 올라프? 올라프 하면 겨울왕국 눈사람만 떠올라요.', 'at': '악마의 대변인 · A(세인트 올라프) · C(십자가가 안 보여 교회 맞나 싶음 — 그 물음은 답을 찾지 못함) · 꾸러미 2', 'a': '노르웨이 왕 올라프 2세, 1014년 런던 다리 싸움, 수호성인, 1941년 폭격과 호콘 7세 — 세인트 올라프 교회', 'see': '작은 교회가 노르웨이 왕의 이름을 품은 곳으로 보여요.'},
  {'x': 'paul', 'q': '그림 가운데 제일 크게 타는 건물은 교회예요? 오른쪽 하얀 성이 타워? 직접 보고 그렸어요?', 'at': '악마의 대변인 · C(대화재 그림 넷) · 꾸러미 3', 'a': '옛 세인트 폴, 9월 4일 밤 8~9시 런던탑 부두 근처 배, 목격자 같은 세부, 비계와 지하의 책들, 교회 87곳 — 런던 박물관·처치 타임스', 'see': '한가운데 불길이 대성당과 책들이 타던 밤으로 보여요.'},
  {'x': 'penn', 'q': '이웃 윌리엄 펜 경은 누구예요? 이름만 나와요.', 'at': '악마의 대변인 · A · D(이름만 나오고 사라지는 사람) · 꾸러미 3', 'a': '해군 제독, 아들이 펜실베이니아를 세움, 찰스 2세가 ‘펜’을 붙임 — 영국 국립해양박물관', 'see': '이웃 펜 경이 한 주의 이름 속 아버지로 보여요.'},
  {'x': 'figures200', 'q': '제목에 ‘그림 200개’라던데, 긴 파이 모양도 있어요? 치즈케이크가 그때도 있었어요?', 'at': '악마의 대변인 · C(two hundred Figures · Cheesecakes) · 꾸러미 3', 'a': '파이·타르트·커스터드·치즈케이크 모양 그림 200개, 17세기 민스파이의 갖가지 모양과 배치 도안 — 그림 속 글씨·아이번 데이', 'see': '제목 쪽 글씨가 파이 도안집 광고로 읽혀요.'},
  {'x': 'currant', 'q': '커런트는 건포도랑 뭐가 달라요?', 'at': '악마의 대변인 · A · 본 카드 ‘알고 보면’ 칸(커런트) · 꾸러미 3', 'a': '씨 없는 작은 건포도, 코린트에서 온 이름, 수입 금지와 세금 — 메리엄-웹스터·영국 의회 역사 연구소', 'see': '커런트가 바다 건너온 값비싼 재료로 보여요.'},
  {'x': 'meatgone', 'q': '설탕이 싸진 거랑 고기를 뺀 게 무슨 상관이에요? 지금도 고기 넣는 데가 있어요?', 'at': '악마의 대변인 · A · B14 · 꾸러미 3', 'a': '1747년 글래스(고기는 넣어도 그만), 1861년 비턴, 20세기 고기 없음, 지금도 전통 조리법의 소기름 — 컨트리 라이프·딜리셔스 매거진', 'see': '과일 파이가 소기름으로 옛 고기 파이와 이어져 보여요.'},
  {'x': 'christmaseve', 'q': '성탄 전날 밤에 고기 파이를 빚어도 됐어요?', 'at': '창(이웃 카드 「일곱 가지 생선 만찬」의 고기 없는 성탄 전야에서) · 꾸러미 3 · 「일곱 가지 생선 만찬」으로 길을 놓음', 'a': '1662년 기도서의 성탄 전야(금식·절제의 날), 금요일 가운데 성탄절만 뺌 — 영국 국교회', 'see': '밤 부엌이 금식하는 밤에 잔치를 준비하는 손으로 보여요.'},
  # 본 카드에 녹인 것(쉬운 말 · 길잡이)
  {'q': '바커가 누구예요? 개 이름인 줄 알았어요. 동생은 남동생이에요?', 'at': '악마의 대변인 · A · B13 → 넷째 장면에 ‘남동생 존 · 아내 곁에서 시중드는 새 하녀 바커’로 녹임', 'a': '1666년 10월 21일 일기 ‘아내의 새 하녀 바커’ · 모들린 칼리지 ‘피프스의 남동생 존’ · 휘틀리 판 머리말(스탠더드 이북스: 1666년에 살아 있던 형제는 존(1641~1677)뿐)', 'see': '성탄 상에 둘러앉은 사람들이 누구인지 보여요.'},
  {'q': '피프스는 해군 사무소 옆집에 산 거예요, 해군에서 일한 거예요?', 'at': '악마의 대변인 · A · E2(영화에서 소개 없이 나옴) → 둘째 장면 ‘해군 사무소에서 일하며 그 곁에 사는’ · 영화 ‘해군 사무소에서 일하던 피프스는’', 'a': '본 카드 ‘알고 보면’ 칸(해군 사무소에서 일하며 그 곁에 삶) · 세인트 올라프(해군 사무소와 이어진 회랑)', 'see': '(약해요)'},
  {'q': '왕당파가 뭐예요? 메이스는 처음 들어 봐요.', 'at': '악마의 대변인 · A → 첫째 장면 ‘왕당파(내전 때 왕의 편에 선 사람들)’ · 인용 ‘메이스(육두구 씨를 감싼 껍질)’ · ‘커런트(작은 건포도)’', 'a': '옥스퍼드 음식 백과(왕당파 집안) · 메리엄-웹스터 mace·currant', 'see': '(약해요)'},
  {'q': '메이가 왜 나와요? 피프스네가 이 책을 보고 만든 거예요?', 'at': '악마의 대변인 · D · E1 → 첫째 장면 끝에 길잡이 한 줄(‘피프스네 부엌이 이 책을 보았는지는 알 수 없지만, 그 시대 민스파이의 속은 이 책이 알려 줘요’)', 'a': '셋째 장면 ‘무대의 차례는 같은 시대 메이의 요리책을 따랐어요’와 이어짐', 'see': '(약해요)'},
  {'q': '한겨울 새벽 네 시인데 창밖이 밝아 와요?', 'at': '악마의 대변인 · A · E3 → 영화 ‘뚜껑을 덮으니 어느새 새벽 네 시예요. / 창밖이 밝아 오면, 성탄 아침이에요.’로 고침(놓아 보기 끝맺음 · 상상 글과 같은 말)', 'a': '피프스 일기 12월 25일(새벽 네 시까지 깨어 앉음) · 런던의 12월 말 해 뜨는 시각은 이 카드에서 다루지 않음', 'see': '(약해요)'},
  {'q': '영화에서는 ‘민스’가 무슨 뜻인지 안 나와요.', 'at': '악마의 대변인 · E5 → 영화 다섯째 장 ‘‘다진 것’이라는 뜻의 이름 ‘민스’만…’', 'a': '본 카드 다섯째 장면 글(다진 것이라는 뜻의 이름)', 'see': '(약해요)'},
  {'q': '중세가 언제예요? 1666년도 중세? 교회 ‘안에’ 묻혔다는 거예요?', 'at': '악마의 대변인 · A · B15 → 넷째 장면 ‘15세기에 지은 … 중세 교회’ · ‘이 교회 안에 나란히’', 'a': '세인트 올라프 교회(1450년 다시 지음 · 피프스는 아내 곁 신도석 쪽에 묻힘)', 'see': '(약해요)'},
  # 남긴 것(근거가 약하거나 다른 데서 할 일)
  {'q': '빵집 사람은 벌 받았어요?', 'at': '악마의 대변인 · B7 → 넣지 않음(빵집 사람 이야기를 하려면 억울하게 처형된 사람 이야기로 이어져, 이 카드의 결과 맞지 않아요) · 자리 이야기는 monument로', 'a': '—', 'see': '(약해요)'},
  {'q': '런던 빵집 조합이 1986년에야 사과했다는데요?', 'at': '창(모뉴먼트를 찾다가) → 넣지 않음(직접 연 기관 자료를 찾지 못함 · 히스토리 닷컴 같은 2차 글만 있음)', 'a': '—', 'see': '(약해요)'},
  {'q': '초상 아래 꼬부랑 영어 시는 뭐라고 써 있어요?', 'at': '악마의 대변인 · C → 넣지 않음(읽을 수 있어요: ‘한 얼굴에서 온갖 대접을 보려거든 메이의 책을 보라’는 자랑 시 · may71에 넣을 만하지만 답이 길어져 검수 때 정해요)', 'a': '그림 속 글씨', 'see': '첫째 장면 초상 아래 시가 요리사를 자랑하는 광고 문구로 읽혀요.'},
  # 답을 찾지 못한 물음(근거 없음)
  {'q': '대체 몇 개를 만들었길래 새벽 네 시까지예요? 누구 먹이려고?', 'at': '악마의 대변인 · B2 · G → 답을 찾지 못함(일기에 수가 없음)', 'a': '—', 'see': '(약해요)'},
  {'q': '엘리자베스는 왜 같이 안 빚고 지켜보기만 했어요?', 'at': '악마의 대변인 · B3 → 답을 찾지 못함(일기에 까닭이 없음 · 그 시대 시는 herrick으로)', 'a': '—', 'see': '(약해요)'},
  {'q': '하녀들은 누구였고, 몇 명이었고, 그 파이를 먹었어요? 성탄에 쉬었어요?', 'at': '악마의 대변인 · B4 · F → 답을 찾지 못함(그 밤 하녀들의 이름과 수가 일기에 없음)', 'a': '—', 'see': '(약해요)'},
  {'q': '파르메산 치즈는 나중에 파냈어요?', 'at': '악마의 대변인 · B5 → 답을 찾지 못함', 'a': '—', 'see': '(약해요)'},
  {'q': '집 다 탄 사람들은 그해 성탄을 어떻게 보냈어요?', 'at': '악마의 대변인 · B8 → 답을 찾지 못함', 'a': '—', 'see': '(약해요)'},
  {'q': '언제부터 지금처럼 작고 동그래졌어요?', 'at': '악마의 대변인 · B10 → 답을 찾지 못함(크고 길쭉한 옛 파이까지는 coffin에)', 'a': '—', 'see': '(약해요)'},
  {'q': '옛날 고기 민스파이를 레시피대로 만들어 본 사람의 맛 후기가 있어요?', 'at': '악마의 대변인 · G → 답을 찾지 못함(아이번 데이의 모양 재현은 있으나 맛 이야기는 찾지 못함)', 'a': '—', 'see': '(약해요)'},
  {'q': '교회 탑이 아래는 돌, 위는 벽돌이에요. 시계는 왜 옆으로 튀어나왔어요? 왼쪽 잔디의 돌은 묘비예요? 십자가는 왜 안 보여요?', 'at': '악마의 대변인 · C(올라프 교회 사진) → 답을 찾지 못함', 'a': '—', 'see': '(약해요)'},
  {'q': '피프스 머리는 가발이에요? 표정이 왜 피곤해 보여요?', 'at': '악마의 대변인 · C(피프스 초상) → 답을 찾지 못함(자세가 힘들었다는 일기는 portrait에)', 'a': '—', 'see': '(약해요)'},
  {'q': '피프스 집과 올라프 교회는 대화재 그림 어디쯤이에요?', 'at': '악마의 대변인 · C → 답을 찾지 못함', 'a': '—', 'see': '(약해요)'},
  {'q': '오늘 민스파이 뚜껑의 무늬는 무슨 뜻이에요? 제목 쪽 오른쪽 위 손글씨는?', 'at': '악마의 대변인 · C → 답을 찾지 못함', 'a': '—', 'see': '(약해요)'},
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
  {'l': '새뮤얼 피프스의 일기, 1666년 10월 21일 — 아내의 새 하녀 바커가 처음으로 함께 교회에 감(넷째 장면의 바커)', 'u': PD + '1666/10/21/'},
  {'l': '모들린 칼리지 도서관 소식 「John Pepys goes to Cambridge」 — 피프스의 남동생 존(1677년 서른여섯에 세상을 떠남)', 'u': MAGD_JOHN},
  {'l': '스탠더드 이북스 『피프스의 일기』 머리말(휘틀리 판) — 형제들의 나고 죽은 해(1666년에 살아 있던 형제는 존뿐)', 'u': 'https://standardebooks.org/ebooks/samuel-pepys/the-diary/text/introduction'},
  {'l': '메리엄-웹스터 사전 ‘mace’ · ‘currant’ — 육두구 씨를 감싼 껍질로 만든 향신료, 씨 없는 작은 건포도(첫째 장면 인용의 쉬운 말)', 'u': MW + 'mace'},
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
   'lines': [{'t': '1666년 9월, 런던에 큰불이 났어요.'}, {'t': '해군 사무소에서 일하던 피프스는 포도주와 치즈를 땅에 묻었어요.'}, {'t': '불길은 그가 다니던 교회 앞에서 멈췄어요.'}],
   'kid': [{'t': '아주 큰불이 났어. 피프스 아저씨는 치즈를 땅에 묻었대!'}, {'t': '너라면 무엇을 지키고 싶어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '새벽 네 시까지'},
  {'type': 'mod', 'mod': 'place', 'ch': 3,
   'lines': [{'t': '1666년 성탄 전야, 피프스네 부엌.'},
             {'t': '긴 파이 껍질을 세우고,', 'act': 'coffin'}, {'t': '다진 고기와', 'act': 'meat'}, {'t': '소기름,', 'act': 'suet'},
             {'t': '향신료와', 'act': 'spice'}, {'t': '말린 과일을 채워요.', 'act': 'fruit'},
             {'t': '뚜껑을 덮으니 어느새 새벽 네 시예요.', 'act': 'lid', 'wait': 1500},
             {'t': '창밖이 밝아 오면, 성탄 아침이에요.', 'act': 'day', 'wait': 1500},
             {'t': '아내는 새벽 네 시까지 하녀들의 민스파이 빚기를 지켜보았다.', 'q': True, 'from': '피프스의 일기, 1666년 12월 25일'}],
   'kid': [{'t': '깜깜한 밤 부엌이야.'},
           {'t': '파이 껍질!', 'act': 'coffin'}, {'t': '고기!', 'act': 'meat'}, {'t': '기름!', 'act': 'suet'},
           {'t': '향신료!', 'act': 'spice'}, {'t': '말린 과일!', 'act': 'fruit'}, {'t': '뚜껑 덮고 끝!', 'act': 'lid', 'wait': 1200},
           {'t': '창밖이 밝아지면 성탄 아침! 어떤 냄새가 날까?', 'act': 'day', 'ask': True}]},
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
   'lines': [{'t': '18세기부터 민스파이는 점점 달콤해졌어요.'}, {'t': '이제는 고기 대신 말린 과일이 가득해요.'}, {'t': '‘다진 것’이라는 뜻의 이름 ‘민스’만 옛 고기 파이를 기억해요.'}],
   'kid': [{'t': '지금은 고기 대신 말린 과일이 가득해.'}, {'t': '옛날 고기 파이는 이름 ‘민스’ 속에 남았어.'}]},
  {'type': 'imagine', 'ch': 6,
   'lines': [{'t': '촛불 하나가 밝힌 겨울밤 부엌.'}, {'t': '도마 소리, 정향과 육두구 냄새, 손등의 밀가루.'}, {'t': '창밖이 밝아 오면, 성탄 아침이에요.'}],
   'kid': [{'t': '눈을 감아 봐. 촛불 하나 켠 부엌이야.'}, {'t': '탁탁탁! 달콤한 냄새! 창밖이 밝아지면 성탄 아침!'}]},
  # 마무리 ‘기록 한 마디’: 영화 끝은 그 밤의 일기 한 줄(나의 자리 물음은 틀이 이 뒤에 붙여요)
  {'type': 'quote', 'ch': 6, 'big': '집안 사람들은 민스파이를 만드느라 바쁘다. 그리고 나는 잠자리에 들었다.',
   'lines': [{'t': '새뮤얼 피프스의 일기, 1666년 12월 24일'}],
   'kid': [{'t': '피프스 아저씨는 성탄 전날 밤 일기에 이렇게 썼어.'}, {'t': '식구들은 민스파이를 만드느라 바쁘고, 나는 자러 간다고.'}]},
  {'type': 'reward', 'ch': 6},
 ],
}
