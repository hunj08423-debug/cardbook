# -*- coding: utf-8 -*-
"""깊은 카드: 빨간 달걀과 달걀 부딪치기(eg-redeggs) · 중심 방식 = 놓아 보기(+두 그림 나란히, 고르기)
기준서 1판 · 틀 deep3-3 · 키트 2판(보탬) · 2026-11-18 21번 묶음 창이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 성목요일(‘빨간 목요일’) 아침, 맨 처음 물든 달걀이 ‘성모의 달걀’로 집 안 이콘 앞에 놓이는 때.
     이 달걀은 깨뜨리지 않고 다음 부활절까지 그 자리에 둬요(in.gr 2024, 그리스 민속 달력).
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 성목요일에 달걀을 빨갛게 물들이는 일 —
     빨간 물 → 식초 → 달걀 → 올리브기름 → 첫 달걀은 이콘 앞(그리스 부활절 달걀 안내와 민속 자료의 차례).
카드 크기: 큰 카드(장면 4). 무대 그림은 이 파일의 stage_svg()로 이 안내서가 그림.
놓아 보기의 ‘우리 집 고르기’ 칸은 쓰지 않아요('home': None). 5단계는 ‘고르기(choose)’를 써요.
그림 원본(src)은 deep_src/eg-redeggs/ (저장소 밖)."""
import random
S = 'eg-redeggs/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

OCA = 'https://www.oca.org/liturgics/outlines/fasting-fast-free-seasons-of-the-church'
FOLK = 'https://pemptousia.gr/pdf.php?id=189121'          # 차코투-카르벨리 『민속 달력』 발췌(그리스어)
ONA = 'https://www.orthodoxianewsagency.gr/pdf.php?id=239310'
INGR = 'https://www.in.gr/2024/05/02/life/geysi/giati-vafoume-kokkina-ta-ayga-pasxa/'
CNNGR = 'https://www.cnn.gr/ellada/story/528007/ta-ethima-tis-megalis-pemptis-o-deipnos-ta-kokkina-avga-kai-oi-lamprokouloyres'
GH = 'https://greekherald.com.au/culture/red-eggs-for-orthodox-easter-symbolism-and-how-to-dye-them'
GF = 'https://thegreekfoodie.com/greek-red-easter-eggs/'
VIMA = 'https://www.tovima.com/culture/the-deeper-meaning-behind-greeces-red-easter-eggs/amp/'
LIFE = 'https://www.azbyka.ru/otechnik/Dmitrij_Rostovskij/zhitija-svjatykh/615'
OC = 'https://orthochristian.com/179333.html'


def stage_svg():
    """성목요일 아침 부엌 무대(800×450, 4:3으로 보이므로 그림은 가운데 x 110~690 안에).
    놓을 것마다 data-o 무리: dye · vinegar · eggs · oil · first. 마지막에 창밖이 밝아져요(.sky2, .day)."""
    R = random.Random(1859)
    # 빨간 물 위에 뜬 양파 껍질 조각
    skins = ''
    for _ in range(9):
        x, y = R.uniform(352, 448), R.uniform(236, 246)
        a = R.uniform(-40, 40)
        skins += (f'<path d="M{x - 7:.0f} {y:.0f} q 7 -6 14 0" stroke="#c9732e" stroke-width="2.4" fill="none" stroke-linecap="round" '
                  f'transform="rotate({a:.0f} {x:.0f} {y:.0f})" opacity=".9"/>')
    # 냄비 속 달걀(물 위로 조금씩 보이는 모습)
    pot_eggs = ''.join(
        f'<ellipse cx="{x}" cy="{y}" rx="13" ry="9" fill="#b0221f" stroke="#7a1414" stroke-width="1"/>'
        f'<ellipse cx="{x - 4}" cy="{y - 3}" rx="4" ry="2" fill="#ff9b8a" opacity=".55"/>'
        for x, y in [(372, 239), (398, 236), (424, 240), (386, 244), (412, 245)])
    steam = ''.join(f'<path d="M{x} 222 c -8 -14 8 -22 0 -36 c -6 -10 4 -18 0 -26" stroke="#f3e6d4" stroke-width="2.2" fill="none" opacity=".22" stroke-linecap="round"/>'
                    for x in (378, 402, 426))
    # 그릇의 반짝이는 빨간 달걀
    bowl_eggs = ''.join(
        f'<ellipse cx="{x}" cy="{y}" rx="15" ry="11" fill="#b8231f" stroke="#7a1414" stroke-width="1" transform="rotate({r} {x} {y})"/>'
        f'<ellipse cx="{x - 5}" cy="{y - 4}" rx="5" ry="2.2" fill="#fff" opacity=".75" transform="rotate({r} {x} {y})"/>'
        for x, y, r in [(176, 342, -12), (204, 338, 8), (232, 342, -4), (190, 352, 14), (220, 353, -10), (248, 350, 6)])
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="성목요일 아침 부엌. 가운데 냄비, 왼쪽에 그릇, 오른쪽 위에 이콘을 모신 선반이 있다. 놓은 것들이 하나씩 나타난다."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#21150f"/><stop offset="1" stop-color="#3a2619"/></linearGradient>
<linearGradient id="__U__sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b2338"/><stop offset="1" stop-color="#3b3a50"/></linearGradient>
<linearGradient id="__U__sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfd6ee"/><stop offset=".7" stop-color="#f6dfb7"/><stop offset="1" stop-color="#ffd59a"/></linearGradient>
<linearGradient id="__U__table" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a4c2a"/><stop offset="1" stop-color="#4f2f19"/></linearGradient>
<linearGradient id="__U__pot" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2c3a46"/><stop offset=".45" stop-color="#4c6070"/><stop offset="1" stop-color="#25313b"/></linearGradient>
<linearGradient id="__U__gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e9c46a"/><stop offset="1" stop-color="#a87a2a"/></linearGradient>
<radialGradient id="__U__glow" cx=".5" cy=".6" r=".55"><stop offset="0" stop-color="#ffb37a" stop-opacity=".85"/><stop offset=".5" stop-color="#d0603a" stop-opacity=".3"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__halo" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd6a0" stop-opacity=".9"/><stop offset="1" stop-color="#ff9a5c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".2" cy=".2" r=".95"><stop offset="0" stop-color="#fff3d4" stop-opacity=".72"/><stop offset=".5" stop-color="#ffd59a" stop-opacity=".26"/><stop offset="1" stop-color="#ffb35c" stop-opacity="0"/></radialGradient></defs>
<rect width="800" height="450" fill="url(#__U__wall)"/>
<rect x="124" y="46" width="128" height="118" rx="4" fill="url(#__U__sky)"/><rect class="sky2" x="124" y="46" width="128" height="118" rx="4" fill="url(#__U__sky2)"/>
<g fill="none" stroke="#5b4030" stroke-width="7"><rect x="124" y="46" width="128" height="118" rx="4"/><line x1="188" y1="46" x2="188" y2="164"/><line x1="124" y1="104" x2="252" y2="104"/></g>
<rect x="116" y="162" width="144" height="9" rx="2" fill="#5b4030"/>
<g><line x1="604" y1="22" x2="596" y2="66" stroke="#b08a4a" stroke-width="1.4"/><line x1="604" y1="22" x2="612" y2="66" stroke="#b08a4a" stroke-width="1.4"/>
<path d="M592 66 L616 66 L611 84 Q604 90 597 84 Z" fill="#9c1c22" stroke="#d9b25c" stroke-width="1.2"/><circle cx="604" cy="63" r="2.6" fill="#ffd27a" opacity=".85"/></g>
<rect x="566" y="96" width="76" height="80" rx="3" fill="url(#__U__gold)"/><rect x="572" y="102" width="64" height="68" rx="2" fill="#5b1418"/>
<circle cx="604" cy="124" r="13" fill="none" stroke="#e9c46a" stroke-width="3"/><circle cx="604" cy="124" r="8" fill="#c99a6a" opacity=".55"/>
<path d="M588 168 C 590 146 596 138 604 138 C 612 138 618 146 620 168 Z" fill="#2a3f6b"/><path d="M596 168 C 598 150 601 144 604 144 C 607 144 610 150 612 168 Z" fill="#8a2a24" opacity=".85"/>
<rect x="648" y="114" width="40" height="56" rx="2" fill="url(#__U__gold)"/><rect x="652" y="118" width="32" height="48" rx="1.5" fill="#3d1c14"/>
<circle cx="668" cy="134" r="8" fill="none" stroke="#e9c46a" stroke-width="2"/><path d="M658 166 C 660 152 664 146 668 146 C 672 146 676 152 678 166 Z" fill="#6a4a2a"/>
<rect x="520" y="176" width="174" height="9" rx="2" fill="#6b4529"/><path d="M534 185 L 546 206 L 558 185 Z M660 185 L 672 206 L 684 185 Z" fill="#4a2f1c"/>
<ellipse class="glow" cx="400" cy="270" rx="260" ry="150" fill="url(#__U__glow)" opacity=".14"/>
<rect x="0" y="300" width="800" height="150" fill="url(#__U__table)"/><rect x="0" y="300" width="800" height="5" fill="#8a5a33"/>
<path d="M320 318 L 480 318 L 470 334 L 330 334 Z" fill="#1f1611" opacity=".8"/>
<path d="M330 236 C 330 300 340 318 400 318 C 460 318 470 300 470 236 Z" fill="url(#__U__pot)" stroke="#1a232b" stroke-width="2"/>
<path d="M326 236 C 312 236 306 244 316 250 M474 236 C 488 236 494 244 484 250" stroke="#25313b" stroke-width="6" fill="none" stroke-linecap="round"/>
<ellipse cx="400" cy="236" rx="72" ry="13" fill="#3e4f5d" stroke="#1a232b" stroke-width="2"/><ellipse cx="400" cy="238" rx="64" ry="10" fill="#120e0b"/>
<g class="obj" data-o="dye"><ellipse cx="400" cy="239" rx="63" ry="9.5" fill="#8a1716"/><ellipse cx="392" cy="236" rx="30" ry="3" fill="#d8504a" opacity=".35"/>{skins}</g>
<g class="obj" data-o="vinegar"><g transform="rotate(-28 520 250)"><rect x="508" y="238" width="24" height="46" rx="6" fill="#cfe3e6" opacity=".55" stroke="#e9f4f4" stroke-width="1.2"/>
<rect x="514" y="222" width="12" height="18" rx="3" fill="#cfe3e6" opacity=".6"/><rect x="508" y="262" width="24" height="22" rx="4" fill="#e9e3c0" opacity=".45"/></g>
<path d="M488 226 C 478 228 470 232 462 238" stroke="#e9f4f4" stroke-width="2" fill="none" opacity=".7"/><circle cx="466" cy="244" r="2" fill="#e9f4f4" opacity=".8"/></g>
<g class="obj" data-o="eggs">{pot_eggs}{steam}</g>
<g class="obj" data-o="oil"><path d="M150 340 C 152 368 172 378 212 378 C 252 378 272 368 274 340 Z" fill="#e8dcc4" stroke="#b7a684" stroke-width="1.5"/>
<ellipse cx="212" cy="340" rx="62" ry="9" fill="#cbbd9f"/>{bowl_eggs}
<g transform="translate(286 300)"><path d="M10 52 C 2 52 0 44 2 36 C 4 26 8 22 8 14 L 8 4 L 16 4 L 16 14 C 16 22 20 26 22 36 C 24 44 22 52 14 52 Z" fill="#9aa83a" opacity=".85" stroke="#d6dc8a" stroke-width="1"/>
<path d="M4 40 C 8 46 16 46 20 40" stroke="#e3e79c" stroke-width="1.4" fill="none" opacity=".7"/></g></g>
<g class="obj" data-o="first"><circle cx="543" cy="158" r="24" fill="url(#__U__halo)" opacity=".75"/>
<ellipse cx="543" cy="163" rx="10" ry="13" fill="#b8231f" stroke="#7a1414" stroke-width="1"/><ellipse cx="539" cy="157" rx="3.2" ry="4.6" fill="#fff" opacity=".6"/>
<path d="M531 176 C 535 171 551 171 555 176" stroke="#e9c46a" stroke-width="2" fill="none"/></g>
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''


ITEMS = [
 {'id': 'dye', 't': '빨간 물', 'la': 'βαφή · κρεμμυδόφυλλα',
  'say': '냄비에 빨간 물을 우려요. 가게에서 산 붉은 물감을 풀기도 하고, 양파 껍질을 오래 끓여 붉은 물을 내기도 해요.'},
 {'id': 'vinegar', 't': '식초', 'la': 'ξίδι',
  'say': '식초를 넣어요. 식초의 신맛이 물감을 껍데기에 단단히 붙여 줘요.'},
 {'id': 'eggs', 't': '달걀', 'la': 'αυγά',
  'say': '사순절 동안 모아 둔 흰 달걀을 살며시 넣어요. 따뜻한 빨간 물 속에서 달걀이 천천히 빨개져요.'},
 {'id': 'oil', 't': '올리브기름', 'la': 'λάδι',
  'say': '달걀이 다 마르면 올리브기름을 묻힌 천으로 닦아요. 빨간 달걀이 반짝반짝 빛나요.'},
 {'id': 'first', 't': '첫 달걀', 'la': 'το αυγό της Παναγίας',
  'say': '맨 처음 물든 달걀은 ‘성모의 달걀’이에요. 깨뜨리지 않고 집 안 이콘 앞에 모셔 둬요.'},
]

CARD = {
 'id': 'eg-redeggs', 'mode': '놓아 보기 · 고르기',
 'pagetitle': '빨간 목요일의 달걀',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>성목요일 · 부활의 밤</b><span>그리스와 정교회 세계</span>',
 'lead': '그리스 정교회에서는 부활절을 사흘 앞둔 목요일에 달걀을 빨갛게 물들여요. 맨 처음 물든 달걀은 ‘성모의 달걀’이 되어 한 해 동안 이콘 앞을 지켜요. 물들이는 차례대로 놓아 보고, 부활의 인사와 함께 ‘톡’ 해 보세요.',
 'leadKid': '부활절 사흘 전, 그리스 사람들은 달걀을 빨갛게 물들인대. 맨 처음 물든 달걀은 깨뜨리지 않고 일 년 동안 간직해! 같이 물들여 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 1판). 장면에는 기록에 있는 것만 옮겼고, 마리아 막달레나의 달걀 이야기는 전해지는 이야기라고 밝혔어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요. 물들이는 부엌 무대 그림은 이 안내서가 그렸어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 얼굴이 나오는 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#8E2B33;--accent-ink:#fffaf5;--soft:rgba(142,43,51,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#c49195;--accent-ink:#14100c;--soft:rgba(196,145,149,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#c49195;--accent-ink:#14100c;--soft:rgba(196,145,149,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '빨간 달걀', 'y': '성목요일', 'sub': '그리스 · 정교회'},
 'doneNote': '올 부활절, “부활하셨네!” 하고 누군가와 달걀을 톡 부딪쳐 보세요.',
 'images': {
  'card': {'src': S + 'Bg-easter-eggs.jpg', 'cap': '불가리아 정교회의 부활절 달걀(2007년)', 'cr': '사진: Ikonact · CC BY-SA 3.0 · 위키미디어 공용',
           'u': 'https://commons.wikimedia.org/wiki/File:Bg-easter-eggs.jpg',
           'alt': '검은 바탕 위 바구니에 빨강·분홍·초록·주황·파랑 달걀이 담겨 있고, 몇 개에는 꽃무늬가 그려져 있다.'},
  'tsoureki': {'src': S + 'tsoureki_2023.jpg', 'cap': '그리스 부활절 빵 ‘초레키’와 빨간 달걀(2023년 4월 16일 사진)', 'cr': '사진: José D. · CC BY-SA 2.0 · 위키미디어 공용',
               'u': 'https://commons.wikimedia.org/wiki/File:16april2023_%CE%A7%CF%81%CE%B9%CF%83%CF%84%CF%8C%CF%82_%CE%91%CE%BD%CE%AD%CF%83%CF%84%CE%B7_%CE%BA%CE%B1%CE%B9_%CE%BA%CE%B1%CE%BB%CF%8C_%CE%A0%CE%AC%CF%83%CF%87%CE%B1_-_Flickr_-_Jos%C3%A9_D....jpg',
               'alt': '나무 도마 위에 땋아 구운 빵이 있고, 빵 위에 두 개, 옆에 한 개, 분홍빛이 도는 빨간 달걀이 놓여 있다. 아래에 꽃무늬 천이 깔려 있다.'},
  'greek': {'src': S + 'Traditional_Greek_Orthodox_Paschal_Easter_foods.jpg', 'cap': '그리스 부활절 음식: 초레키, 마기리차 수프, 빨간 달걀(2010년)', 'cr': '사진: ΙΣΧΣΝΙΚΑ-888 · CC BY-SA 3.0 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Traditional_Greek_Orthodox_Paschal_(Easter)_foods.jpg',
            'alt': '레이스 식탁보 위에 비닐에 싼 둥근 땋은 빵, 빨간 달걀과 꽃무늬 달걀이 담긴 유리 바구니, 구슬로 꾸민 달걀 장식, 그리고 푸른빛 수프 한 그릇이 놓여 있다.'},
  'tap': {'src': S + 'Eierpecken.jpg', 'cap': '오스트리아의 달걀 부딪치기(2014년 부활절)', 'cr': '사진: Anna reg · CC BY-SA 3.0 at · 위키미디어 공용',
          'u': 'https://commons.wikimedia.org/wiki/File:Eierpecken.jpg',
          'alt': '두 사람의 손이 각각 짙은 빨간 달걀과 주황 달걀을 쥐고, 달걀 끝을 서로 맞대고 있다.'},
  'game1888': {'src': S + 'igra_v_yaitsa_1888.jpg', 'cap': '‘달걀 놀이’, 1888년 러시아 잡지 『세계 화보』에 실린 판화', 'cr': '판화: 작가 미상 · 퍼블릭 도메인 · 위키미디어 공용',
               'u': 'https://commons.wikimedia.org/wiki/File:%D0%98%D0%B3%D1%80%D0%B0_%D0%B2_%D1%8F%D0%B9%D1%86%D0%B0_%D0%B2_%D0%9C%D0%B0%D0%BB%D0%BE%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B8.jpg',
               'alt': '흑백 판화. 마을 길에서 아이들이 짝을 지어 손에 쥔 것을 맞대고 있고, 뒤로 사람들이 모여 있으며 멀리 교회의 둥근 지붕이 보인다. 아래에 러시아어 제목이 적혀 있다.'},
  'korea': {'src': S + 'Easter_eggs_in_Korea_03.jpg', 'cap': '한국의 부활절 달걀(2015년 4월 5일 부활절)', 'cr': '사진: Piotrus · CC BY-SA 3.0 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Easter_eggs_in_Korea_03.JPG',
            'alt': '하트 무늬 비닐봉지 안에 그림 비닐을 입힌 삶은 달걀 두 개가 들어 있다. 한 달걀에는 웃는 얼굴의 인물 그림과 성경 구절이 인쇄되어 있다.'},
 },
 'scenes': [
  {'id': 'lent', 'label': '사순절 동안 모은 달걀', 'kind': 'photo', 'img': 'tsoureki',
   'text': ['정교회의 사순절은 부활절 전날까지 이어지는 긴 금식이에요. 이 동안 고기는 물론 달걀과 우유, 치즈도 먹지 않아요.',
            '닭은 그동안에도 알을 낳아요. 그리스의 민속 기록은 그 달걀을 사순절 내내 모아 두었다고 전해요.'],
   'text2': ['부활절을 사흘 앞둔 성목요일, 집집마다 부활절 빵을 반죽하고 달걀을 빨갛게 물들여요. 그래서 그리스에서는 이날을 ‘빨간 목요일’이라고도 불러요.',
             '빵 한가운데에 빨간 달걀을 박아 굽기도 해요. 그리스 민속 달력은 이것을 비잔티움 시대부터 이어진 풍습이라고 적어요.'],
   'kid': '사순절에는 달걀을 안 먹고 모아 둬. 성목요일이 되면 한꺼번에 빨갛게 물들여!',
   'kidq': '빵 위에 빨간 달걀을 올리면 무엇처럼 보일까?'},
  {'id': 'thursday', 'label': '빨간 목요일 아침', 'kind': 'mod', 'mod': 'place', 'night': False,
   'text': ['성목요일 아침, 부엌에서 달걀 물들이기가 시작돼요. 그리스 민속 달력에 따르면 상을 당한 집 말고는 모든 집이 빨간 달걀을 물들였어요.',
            '아래 부엌에 하나씩 놓아 보세요. 마지막에는 맨 처음 물든 달걀을 이콘 앞으로 옮겨요. 이콘은 예수와 성인들을 그린 정교회의 성화예요.'],
   'text2': ['맨 처음 물든 달걀을 그리스에서는 ‘성모의 달걀’이라고 불러요. 신기한 힘이 있다고 여겨, 여인들은 이 달걀로 아픈 아이에게 성호를 그어 주기도 했어요.',
             '성모의 달걀은 깨뜨리지 않아요. 집 안 이콘 선반에 모셔 두고, 다음 부활절까지 그 자리에 둬요.'],
   'kid': '빨간 물, 식초, 달걀, 기름! 그리고 맨 처음 물든 달걀은 그림 앞에 살짝.',
   'kidq': '일 년 동안 깨뜨리지 않고 둔 달걀은 어떻게 될까?'},
  {'id': 'emperor', 'label': '황제 앞의 빨간 달걀', 'kind': 'quote',
   'text': ['왜 하필 빨간 달걀일까요? 정교회에는 마리아 막달레나의 이야기가 전해져요. 막달레나는 부활하신 예수를 처음 만난 사람으로 복음서에 나와요.',
            '14세기 비잔티움의 교회 역사가 니케포로스 크산토풀로스는 막달레나가 로마에 가서 티베리우스 황제 앞에서 전도했다고 적었어요. 러시아 정교회의 성인전은 그 장면을 이렇게 전해요.'],
   'quote': {'t': '이탈리아에 갔을 때, 막달레나는 그때 다스리던 티베리우스 황제 앞에 나설 기회를 얻었어요. 그리고 널리 퍼진 동방의 풍습대로 빨갛게 물들인 달걀을 바치며 말했어요. ‘그리스도께서 부활하셨습니다!’',
             'from': '러시아 정교회 성인전(로스토프의 디미트리 『성인전』 러시아어판), 마리아 막달레나 편 · 러시아어를 이 안내서가 우리말로 옮김', 'u': LIFE},
   'text2': ['이 성인전은 그 뒤 그리스도인들이 막달레나를 따라, 부활을 기억하며 빨간 달걀을 주고받게 되었다고 전해요.',
             '그리스에서는 조금 다르게 전해져요. 황제가 “달걀이 빨개지면 믿겠다”고 하자 달걀이 빨갛게 변했다는 이야기예요. 둘 다 성경에는 없는, 전해지는 이야기예요.'],
   'kid': '옛날이야기야. 마리아 막달레나가 황제에게 빨간 달걀을 건네며 “그리스도께서 부활하셨어요!” 했대.',
   'kidq': '기쁜 소식을 전할 때, 너는 무엇을 함께 건네고 싶어?'},
  {'id': 'tap', 'label': '톡, 그리스도 부활하셨네', 'kind': 'duo', 'imgs': ['greek', 'tap'], 'night': True, 'choose': True,
   'caps': ['부활 예배 뒤의 그리스 식탁(2010년)', '달걀 끝을 맞대고 톡(오스트리아, 2014년)'],
   'text': ['토요일 밤 자정을 넘겨 부활 예배가 끝나면, 가족이 모여 늦은 밤 식사를 해요. 그 식탁에서 빨간 달걀 부딪치기 ‘추그리스마’(τσούγκρισμα)가 시작돼요. ‘맞부딪치기’라는 뜻이에요.',
            '한 사람이 “그리스도 부활하셨네!”(Χριστός Ανέστη) 하며 달걀 끝으로 상대 달걀을 톡 치면, 상대는 “참으로 부활하셨네!”(Αληθώς Ανέστη) 하고 받아요.'],
   'text2': ['그리스 사람들은 단단한 껍데기를 봉인된 무덤으로, 깨지는 껍데기를 열린 무덤으로 읽어요. 끝까지 깨지지 않은 달걀의 주인은 한 해 운이 좋다고들 해요.'],
   'kid': '“그리스도 부활하셨네!” 톡! “참으로 부활하셨네!” 톡!',
   'kidq': '톡 하고 껍데기가 깨지면, 무엇이 열린 걸까?'},
 ],
 'imagine': {'t': '자정이 지난 식탁 위로 촛불이 흔들려요. 손바닥에 쥔 빨간 달걀이 매끈하고 단단해요. 맞은편 사람과 눈이 마주치고, 함께 숨을 고르는 순간 — 톡. 가는 금 사이로 하얀 속이 보이고, 웃음이 터져요.',
             'kid': '눈을 감아 봐. 빨간 달걀을 꼭 쥐었어. 하나, 둘, 셋 — 톡! 깨진 껍데기 사이로 하얀 속이 보여. 다 같이 웃어!'},
 'lines': ['사순절 내내 모아 둔 달걀.', '맨 처음 물든 달걀은 한 해 동안 이콘 앞에.', '그리스도 부활하셨네 — 참으로 부활하셨네.', '깨진 껍데기 사이로 열린 무덤.'],
 'linesKid': ['빨간 목요일!', '톡! 부활하셨네!', '성모의 달걀은 깨지 않아요.'],
 'goals': {
  's4': {'t': '물들이는 차례대로', 'p': '빨간 물 → 식초 → 달걀 → 올리브기름 → 첫 달걀 차례대로 다 놓으면 카드에 금박이 입혀져요.',
         'how': '물들이는 차례대로 빨간 목요일의 부엌을 다 놓아 보세요', 'done': '빨간 목요일의 달걀을 다 물들였어요',
         'ways': [{'id': 'plOrder', 't': '빨간 물 → 식초 → 달걀 → 올리브기름 → 첫 달걀 차례로 놓기'}]},
  's5': {'t': '부활의 인사', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '누구와 먼저 ‘톡’ 할지 고르거나, 아이와 함께 끝까지 보세요', 'done': '부활의 인사를 나눌 사람을 정했어요',
         'ways': [{'id': 'choose', 't': '부활의 인사와 함께 누구와 먼저 ‘톡’ 할지 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'place': {
   'items': ITEMS, 'order': '빨간 물, 식초, 달걀, 올리브기름, 첫 달걀',
   'intro': '아래에서 하나를 골라 부엌에 놓아 보세요. 물들이는 차례는 빨간 물, 식초, 달걀, 올리브기름, 그리고 첫 달걀이에요.',
   'climax': '빨간 목요일의 일이 끝났어요. 성모의 달걀은 다음 부활절까지 이콘 앞을 지켜요. 이제 부활의 밤을 기다려요.<span class="la">맨 처음 물든 달걀은 깨뜨리지 않고 이콘 선반에 둬요 · 그리스 민속 기록</span>',
   'home': None, 'orderDone': '물들이는 차례대로 다 놓았어요', 'wrongOrder': '물들이는 차례는 이래요: {order}', 'daylight': False,
   'svg': stage_svg()},
  'choose': {
   'q': '부활의 인사와 함께, 누구와 먼저 ‘톡’ 할까요?',
   'opts': [{'t': '예배를 마친 가족과', 'r': '그리스에서는 부활 예배가 끝나면 가족이 모여 늦은 밤 식사를 하며 달걀을 부딪쳐요.'},
            {'t': '식탁에 둘러앉은 모두와', 'r': '달걀 하나가 식탁을 한 바퀴 돌며 차례로 인사를 나누기도 해요. 한쪽 끝이 깨지면 둥근 쪽을 내밀어요.'},
            {'t': '이콘 앞의 성모의 달걀과', 'r': '성모의 달걀은 부딪치지 않아요. 다음 부활절까지 깨뜨리지 않고 이콘 앞에 둬요.'}],
  },
 },
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 물들여 보기</button></div>
  <div class="pl-home" hidden><p>빨간 달걀을 다 물들였어요.</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div><p class="mod-note">무대 그림: 이 안내서가 그린 성목요일 부엌과 집 안 이콘 선반 · 물들이는 차례는 <a href="''' + GF + '''" target="_blank" rel="noopener">그리스 부활절 달걀 안내</a>와 <a href="''' + INGR + '''" target="_blank" rel="noopener">in.gr</a>을 바탕으로</p></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>빨간 목요일</b> 그리스에서는 성목요일을 ‘빨간 목요일’(Κόκκινη Πέμπτη)이라고도 불러요. 이날 달걀을 빨갛게 물들이기 때문이에요. 빨강은 그리스도의 피를 떠올리게 한다고 여겨요.',
    '<b>식구 수만큼, 그리고 하나 더</b> 옛날 흑해 바닷가 시노프(오늘의 튀르키예)에 살던 그리스 사람들은 식구 수만큼 달걀을 물들이고, 성모의 몫으로 하나를 더했어요. 성목요일 밤에 교회로 가져가 부활 때까지 제단 아래 두었다고 해요.',
    '<b>자정에 물들인 첫 달걀</b> 그리스 서마케도니아에서는 성수요일 자정에 첫 달걀을 물들였어요. 그 달걀은 밭의 첫 고랑에 묻었어요. 씨앗이 달걀의 생명력으로 싹트기를 바란 거예요.',
    '<b>빨간 천</b> 흑해 바닷가 메심브리아(오늘의 불가리아 네세바르)의 그리스 사람들은 성목요일에 달걀과 함께 천도 빨갛게 물들여, 40일 동안 창밖에 걸었어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>막달레나의 달걀</b> 러시아 성인전은 막달레나가 빨갛게 물들인 달걀을 가져갔다고 적어요. 그리스에서는 황제의 말에 달걀이 빨개졌다는 이야기로, 또는 막달레나의 바구니 속 흰 달걀이 빨개졌다는 이야기로 전해져요.',
    '<b>막달레나가 로마에?</b> 막달레나가 로마에 가서 티베리우스 황제 앞에서 전도했다는 이야기는 14세기 크산토풀로스의 『교회사』에 나와요. 성경에는 없는 이야기예요.',
    '<b>어느 쪽부터 칠까</b> 그리스 음식 안내 누리집은 뾰족한 끝으로 먼저 치고, 깨지면 달걀을 돌려 둥근 쪽을 내민다고 적어요. 집집마다 규칙이 조금씩 달라요.',
    '<b>언제 물들일까</b> 대부분 성목요일에 물들이지만, 서마케도니아처럼 성수요일 자정에 시작하는 곳도 있어요. 물들이는 달걀 수와 방법도 고장마다 달라요.']},
  {'h': '세계의 달걀 부딪치기', 'img': ['game1888', 'korea'], 'p': [
    '1888년 러시아 잡지 『세계 화보』에는 ‘달걀 놀이’라는 판화가 실렸어요. 그림 아래에는 ‘소러시아의 부활 주간’이라고 적혀 있어요. 소러시아는 그때 러시아 제국이 우크라이나 땅을 부르던 말이에요. 오스트리아에도 비슷한 놀이 ‘에어페켄’(Eierpecken)이 있어요.',
    '오른쪽 사진은 2015년 4월 5일 부활절에 한국에서 찍은 달걀이에요. 그림과 성경 구절을 입힌 삶은 달걀을 비닐봉지에 담았어요.'],
   'links': [{'t': '그리스 헤럴드: 빨간 달걀의 뜻과 물들이는 법', 'u': GH, 'm': '영어'},
             {'t': 'in.gr: 왜 부활절 달걀을 빨갛게 물들일까', 'u': INGR, 'm': '그리스어'},
             {'t': '러시아 정교회 성인전: 마리아 막달레나', 'u': LIFE, 'm': '러시아어'}]},
  {'h': '함께 읽는 말씀', 'p': [
    '말씀은 뜻만 옮기고, 본문은 대한성서공회 개역개정으로 이어 드려요.',
    '<b>' + bl('MAT.27', '마태복음 27장 66절') + '</b> 사람들은 예수의 무덤을 막은 돌을 봉인하고 경비병을 세워 지켰어요.',
    '<b>' + bl('MRK.16', '마가복음 16장 1~6절') + '</b> 안식일이 지난 이른 아침, 여인들이 무덤에 가 보니 큰 돌이 이미 굴려져 있었어요.',
    '<b>' + bl('JHN.20', '요한복음 20장 1~18절') + '</b> 마리아 막달레나가 빈 무덤 곁에서 부활하신 예수를 처음 만나고, 제자들에게 알려요.']},
 ],
 'src': [
  {'l': '미국 정교회(OCA): 금식 기간 — 사순절과 성주간에는 고기·달걀·유제품을 먹지 않음', 'u': OCA},
  {'l': '아이카테리니 차코투-카르벨리, 『민속 달력』 발췌(pemptousia, 그리스어) — 상중인 집 말고 모든 집이 물들임, 사순절 내내 모음, 성모의 달걀·성호, 부활절 빵의 빨간 달걀(비잔티움 때부터)', 'u': FOLK},
  {'l': '정교회 통신(2020, 그리스어): 성목요일 풍습 — 성모의 달걀, 시노프·서마케도니아·메심브리아 풍습, 고장마다 다른 방법', 'u': ONA},
  {'l': 'in.gr(2024, 그리스어): 첫 달걀은 성모의 것, 깨뜨리지 않고 다음 부활절까지 이콘 선반에, 껍데기와 무덤', 'u': INGR},
  {'l': 'CNN 그리스(2026.4.9, 그리스어): 성목요일을 ‘빨간 목요일’이라 부르는 까닭, 첫 빨간 달걀을 이콘 선반에', 'u': CNNGR},
  {'l': '그리스 헤럴드(2024): 빨간 달걀의 뜻, 자정 예배 뒤 가족 식사와 ‘추그리스마’, 인사말, 식초와 기름', 'u': GH},
  {'l': '그리스 음식 안내(2026): 식초가 물감을 붙임, 마른 뒤 올리브기름, 양파 껍질 물들이기, 끝을 맞대고 깨지면 둥근 쪽', 'u': GF},
  {'l': '토 비마(2025): 황제의 말에 바구니의 달걀이 빨개졌다는 그리스의 막달레나 이야기', 'u': VIMA},
  {'l': '러시아 정교회 성인전(로스토프의 디미트리 『성인전』 러시아어판, azbyka): 마리아 막달레나와 티베리우스 황제, 빨간 달걀', 'u': LIFE},
  {'l': '오소크리스천(2026): 크산토풀로스(†1335)의 『교회사』와 디미트리 로스토프스키(†1709)의 막달레나 이야기', 'u': OC},
  {'l': '위키미디어 공용: ‘달걀 놀이’ 판화 설명(『세계 화보』 17호, 1888)', 'u': 'https://commons.wikimedia.org/wiki/File:%D0%98%D0%B3%D1%80%D0%B0_%D0%B2_%D1%8F%D0%B9%D1%86%D0%B0_%D0%B2_%D0%9C%D0%B0%D0%BB%D0%BE%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B8.jpg'},
  {'l': '대한성서공회 개역개정: 마태복음 27장 · 마가복음 16장 · 요한복음 20장', 'u': NKRV + 'JHN.20'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 45%', 'p1': '50% 55%', 's0': 1.2, 's1': 1.04, 'kicker': '성목요일 · 그리스와 정교회 세계', 'title': '빨간 달걀과 달걀 부딪치기',
   'lines': [{'t': '부활절을 사흘 앞둔 목요일.'}, {'t': '그리스의 부엌마다 달걀이 빨갛게 물들어요.'}],
   'kid': [{'t': '알록달록 부활절 달걀이야!'}, {'t': '오늘은 빨간 목요일!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '모아 둔 달걀'},
  {'type': 'img', 'ch': 1, 'img': 'tsoureki', 'fit': 'cover', 'p0': '45% 50%', 'p1': '55% 45%', 's0': 1.15, 's1': 1.0, 'cap': '그리스 부활절 빵 초레키와 빨간 달걀',
   'lines': [{'t': '사순절 동안, 달걀은 먹지 않고 모아 둬요.'}, {'t': '성목요일에는 부활절 빵을 굽고 달걀을 물들여요.'}],
   'kid': [{'t': '달걀을 안 먹고 모아 뒀대.'}, {'t': '빵 위에 빨간 달걀이 쏙! 무엇을 닮았을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '빨간 목요일'},
  {'type': 'mod', 'mod': 'place', 'ch': 2,
   'lines': [{'t': '성목요일 아침, 냄비에 빨간 물을 우려요.', 'act': 'dye'},
             {'t': '식초를 넣고,', 'act': 'vinegar'},
             {'t': '모아 둔 달걀을 넣어요.', 'act': 'eggs'},
             {'t': '마르면 올리브기름으로 반짝반짝 닦아요.', 'act': 'oil'},
             {'t': '맨 처음 물든 달걀은 이콘 앞으로.', 'act': 'first', 'wait': 1500},
             {'t': '성모의 달걀이에요. 다음 부활절까지 이 자리를 지켜요.', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '같이 물들여 보자!'}, {'t': '빨간 물!', 'act': 'dye'}, {'t': '식초!', 'act': 'vinegar'}, {'t': '달걀 퐁당!', 'act': 'eggs'},
           {'t': '기름으로 반짝반짝!', 'act': 'oil'}, {'t': '첫 달걀은 그림 앞에 살짝.', 'act': 'first', 'wait': 1500},
           {'t': '일 년 동안 깨뜨리지 않는대. 왜 그럴까?', 'act': 'day', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '황제 앞의 달걀'},
  {'type': 'quote', 'ch': 3, 'big': '그리스도께서 부활하셨습니다!',
   'lines': [{'t': '정교회에는 이런 이야기가 전해져요.'},
             {'t': '막달레나가 로마 황제에게 빨간 달걀을 바치며 인사했다고요.', 'q': True, 'from': '러시아 정교회 성인전에서'},
             {'t': '그 뒤 그리스도인들이 빨간 달걀을 주고받게 되었다고 해요.'}],
   'kid': [{'t': '옛날이야기야.'}, {'t': '빨간 달걀을 건네며 “그리스도께서 부활하셨어요!”'},
           {'t': '기쁜 소식에는 무엇을 함께 건네면 좋을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '톡'},
  {'type': 'img', 'ch': 4, 'img': 'greek', 'fit': 'cover', 'p0': '60% 40%', 'p1': '50% 50%', 's0': 1.18, 's1': 1.02, 'cap': '부활 예배 뒤의 그리스 식탁',
   'lines': [{'t': '토요일 밤, 부활 예배를 마치고 식탁에 둘러앉아요.'}, {'t': '“그리스도 부활하셨네!”'}],
   'kid': [{'t': '한밤중에 식탁에 모였어.'}, {'t': '“그리스도 부활하셨네!”'}]},
  {'type': 'img', 'ch': 4, 'img': 'tap', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 45%', 's0': 1.25, 's1': 1.05, 'cap': '달걀 끝을 맞대고 톡',
   'lines': [{'t': '톡. “참으로 부활하셨네!”'}, {'t': '깨진 껍데기는 열린 무덤이에요.'}],
   'kid': [{'t': '톡! “참으로 부활하셨네!”'}, {'t': '껍데기가 깨지면 무엇이 열린 걸까?', 'ask': True}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '자정이 지난 식탁 위로 촛불이 흔들려요.'}, {'t': '맞은편 사람과 함께 숨을 고르는 순간 — 톡.'}, {'t': '가는 금 사이로 하얀 속이 보이고, 웃음이 터져요.'}],
   'kid': [{'t': '눈을 감아 봐. 빨간 달걀을 꼭 쥐었어.'}, {'t': '하나, 둘, 셋 — 톡! 다 같이 웃어!'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
