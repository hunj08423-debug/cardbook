# -*- coding: utf-8 -*-
"""깊은 카드: 와타나베 사다오의 성경 판화(aa-watanabe) · 중심 방식 = 놓아 보기(+두 그림 나란히)
기준서 1판(보탬 8) · 틀 deep3-3 · 키트 2판(보탬 2026-11-18) · 2026-11-18 26번 묶음 창이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 도쿄 집 작업실에서, 먹으로 새까맣게 덮인 종이를 찬물에 헹구자
     쌀풀이 씻겨 나가며 칠해 둔 색이 떠오르는 순간(헬렌 메릿, Christian Century 1977).
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 메릿이 적어 둔 그의 색 판화 차례.
     불빛 → 종이 본 → 물감 → 쌀풀 → 먹 → 찬물을 차례대로 작업대에 놓아요.
카드 크기: 한 장면 카드(장면 2). 와타나베(1996년 별세)의 판화는 저작권이 있어 싣지 않고,
그가 쓴 기법의 자료(가타가미 · 빈가타, 퍼블릭 도메인)와 이 안내서가 그린 작업대 무대로 만들어요.
무대 끝에 드러나는 물고기·물결 무늬는 그의 판화가 아니라 차례를 보여 주려고 이 안내서가 그린 연습 그림이에요.
그림 원본(src)은 deep_src/aa-watanabe/."""
import random
S = 'aa-watanabe/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

MERRITT = 'https://www.religion-online.org/?p=7365'
FIOR = 'https://viewingjapaneseprints.net/texts/sosaku_hanga/watanabe_sadao.html'
HONO = 'https://honolulu.emuseum.com/people/241/watanabe-sadao'
HANGA = 'https://sites.google.com/view/sadaohanga/home/introduction/introduction-to-sadao-watanabe'
MINGEI = 'https://mingeikan.or.jp/about/'
JRE = 'https://www.jreast.co.jp/tohokurekishi/tohoku-pdf/tohoku_2019-06.pdf'

# ---------- 작업대 무대(이 안내서가 그림) ----------
# 종이: x 232~568, y 74~376. 무늬(물고기·해·물결)는 이 안내서가 지은 연습 그림이에요.
FISH = 'M300 196 C 326 150, 418 142, 468 188 C 420 236, 330 242, 300 196 Z'
TAIL = 'M462 188 L 516 150 C 506 172, 506 206, 516 228 Z'
FIN = 'M370 160 C 384 132, 414 132, 432 150 C 410 152, 392 156, 370 160 Z'
FIN2 = 'M384 226 C 396 244, 418 248, 432 240 C 414 236, 398 232, 384 226 Z'
WAVES = ['M250 292 C 280 268, 310 268, 340 292 S 400 316, 430 292 S 490 268, 520 292 S 548 302, 556 298',
         'M250 336 C 280 312, 310 312, 340 336 S 400 360, 430 336 S 490 312, 520 336 S 548 346, 556 342']
FOAM = [(296, 276), (476, 276), (386, 320), (296, 320), (476, 320), (386, 276)]
SCALES = ['M366 172 C 376 184, 376 204, 366 216', 'M392 168 C 402 182, 402 206, 392 220', 'M418 172 C 428 184, 428 204, 418 214']
SUN = (512, 112, 20)

def _design(body, tail, fin, sun, wave, sw=15, op=1.0, scales=None, eye=None, foam=None):
    sx, sy, sr = SUN
    g = (f'<g opacity="{op}"><path d="{FISH}" fill="{body}"/><path d="{TAIL}" fill="{tail}"/><path d="{FIN}" fill="{fin}"/><path d="{FIN2}" fill="{fin}"/>'
         f'<circle cx="{sx}" cy="{sy}" r="{sr}" fill="{sun}"/>'
         + ''.join(f'<path d="{w}" fill="none" stroke="{wave}" stroke-width="{sw}" stroke-linecap="round"/>' for w in WAVES))
    if foam: g += ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="{foam}"/>' for x, y in FOAM)
    if eye: g += f'<circle cx="328" cy="190" r="8" fill="{eye[0]}"/><circle cx="328" cy="190" r="3.4" fill="{eye[1]}"/>'
    if scales: g += ''.join(f'<path d="{d}" fill="none" stroke="{scales}" stroke-width="2.4" stroke-linecap="round"/>' for d in SCALES)
    return g + '</g>'

def stage_svg():
    R = random.Random(1947)
    grain = ''.join(f'<path d="M0 {y:.0f} C 200 {y + R.uniform(-6, 6):.0f}, 600 {y + R.uniform(-6, 6):.0f}, 800 {y + R.uniform(-4, 4):.0f}" stroke="#4d3826" stroke-width="{R.uniform(.6, 1.6):.1f}" fill="none" opacity="{R.uniform(.25, .5):.2f}"/>' for y in range(18, 450, 26))
    def wrinkles(col, op, n=26):
        out = ''
        for _ in range(n):
            x, y = R.uniform(240, 560), R.uniform(82, 368)
            dx, dy = R.uniform(-34, 34), R.uniform(-18, 18)
            out += f'<path d="M{x:.0f} {y:.0f} q {dx / 2 + R.uniform(-8, 8):.0f} {dy / 2 + R.uniform(-8, 8):.0f} {dx:.0f} {dy:.0f}" stroke="{col}" stroke-width="1" fill="none" opacity="{op}"/>'
        return out
    paper = 'x="232" y="74" width="336" height="302"'
    frame = 'M216 58 h368 v334 h-368 Z M232 74 v302 h336 v-302 Z'
    outline = (f'<g fill="none" stroke="#6a5038" stroke-width="1.6" opacity=".75"><path d="{FISH}"/><path d="{TAIL}"/><path d="{FIN}"/><path d="{FIN2}"/>'
               f'<circle cx="{SUN[0]}" cy="{SUN[1]}" r="{SUN[2]}"/><circle cx="328" cy="190" r="8"/>'
               + ''.join(f'<path d="{w}" stroke-width="1.4" stroke-dasharray="0" />' for w in WAVES) + '</g>')
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="나무 작업대 위의 유리판과 종이. 놓은 것들이 차례로 나타나고, 마지막에 까만 바탕 위로 물고기와 해, 물결 그림이 드러난다. 이 안내서가 그린 연습 그림이다."><defs>
<linearGradient id="__U__wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f2218"/><stop offset="1" stop-color="#1b130d"/></linearGradient>
<radialGradient id="__U__lamp" cx=".5" cy=".18" r=".8"><stop offset="0" stop-color="#ffd99a" stop-opacity=".55"/><stop offset=".5" stop-color="#e6a35a" stop-opacity=".18"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__back" cx=".5" cy=".5" r=".62"><stop offset="0" stop-color="#fff7e2"/><stop offset=".75" stop-color="#f6ecd6"/><stop offset="1" stop-color="#e9dcc0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".5" r=".7"><stop offset="0" stop-color="#fff3d6" stop-opacity=".0"/><stop offset=".7" stop-color="#ffd9a0" stop-opacity=".18"/><stop offset="1" stop-color="#ffb866" stop-opacity=".32"/></radialGradient>
<pattern id="__U__silk" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 0 L6 6 M6 0 L0 6" stroke="#cfc3a6" stroke-width=".6" opacity=".55"/></pattern>
<pattern id="__U__wet" width="40" height="14" patternUnits="userSpaceOnUse"><path d="M0 7 C 10 3, 20 11, 40 7" stroke="#bcd6e6" stroke-width="1.2" fill="none" opacity=".35"/></pattern>
</defs>
<rect width="800" height="450" fill="url(#__U__wood)"/>{grain}
<rect class="glow" width="800" height="450" fill="url(#__U__lamp)" opacity=".14"/>
<rect x="196" y="42" width="408" height="366" rx="8" fill="#161b21" stroke="#4f5964" stroke-width="2"/>
<path d="M210 60 L300 60 L230 380 L210 380 Z" fill="#ffffff" opacity=".035"/>
<rect {paper} fill="#7c7567"/>{wrinkles('#958d7c', .55)}{wrinkles('#5f594e', .45, 18)}
<g class="lt" style="transition-delay:0s"><rect {paper} fill="url(#__U__back)" opacity=".94"/>{wrinkles('#cfc4ad', .55, 22)}</g>
<g class="lt" style="transition-delay:.2s"><rect x="200" y="46" width="400" height="358" rx="6" fill="none" stroke="#ffe7b0" stroke-width="5" opacity=".35"/></g>
<g class="lt" style="transition-delay:.4s"><rect x="226" y="68" width="348" height="314" fill="none" stroke="#fff3cf" stroke-width="9" opacity=".22"/></g>
<g class="obj" data-o="stencil"><path d="{frame}" fill="#5c3a20" fill-rule="evenodd" stroke="#7b5232" stroke-width="1"/>{outline}
<g fill="#7b5232"><circle cx="224" cy="66" r="2.4"/><circle cx="576" cy="66" r="2.4"/><circle cx="224" cy="384" r="2.4"/><circle cx="576" cy="384" r="2.4"/></g></g>
<g class="obj" data-o="color">{_design('#c4553f', '#d89a36', '#d89a36', '#e5c04f', '#3f6f99', sw=13, op=.8)}
<g><circle cx="120" cy="130" r="20" fill="#2a2018" stroke="#6b5440"/><circle cx="120" cy="130" r="13" fill="#c4553f"/>
<circle cx="120" cy="186" r="20" fill="#2a2018" stroke="#6b5440"/><circle cx="120" cy="186" r="13" fill="#d89a36"/>
<circle cx="120" cy="242" r="20" fill="#2a2018" stroke="#6b5440"/><circle cx="120" cy="242" r="13" fill="#3f6f99"/>
<path d="M88 300 L150 270" stroke="#a07a4c" stroke-width="5" stroke-linecap="round"/><path d="M150 270 L164 263" stroke="#2a221c" stroke-width="7" stroke-linecap="round"/></g></g>
<g class="obj" data-o="paste"><rect {paper} fill="url(#__U__silk)"/><path d="{frame}" fill="#5c3a20" fill-rule="evenodd" opacity=".9"/>
{_design('#eee4c9', '#eee4c9', '#eee4c9', '#eee4c9', '#eee4c9', sw=17, op=.93, eye=('#eee4c9', '#eee4c9'), foam='#f4ecd6')}
<g><ellipse cx="672" cy="150" rx="40" ry="16" fill="#3a2b1f" stroke="#6b5440"/><ellipse cx="672" cy="146" rx="32" ry="10" fill="#efe6cc"/>
<rect x="640" y="214" width="78" height="14" rx="4" fill="#b98d57" stroke="#7a5a36" transform="rotate(-18 679 221)"/></g></g>
<g class="obj" data-o="ink"><rect {paper} fill="#141213" opacity=".95"/>
{_design('#2a2725', '#2a2725', '#2a2725', '#2a2725', '#2a2725', sw=17, op=.85, eye=('#2a2725', '#2a2725'), foam='#2d2a28')}
<g><rect x="78" y="330" width="86" height="54" rx="10" fill="#1c1a19" stroke="#4a4440"/><ellipse cx="121" cy="352" rx="28" ry="12" fill="#0d0c0c"/>
<rect x="172" y="300" width="16" height="70" rx="3" fill="#1f1c1a" stroke="#4a4440" transform="rotate(28 180 335)"/></g></g>
<g class="obj" data-o="wash"><path d="{frame}" fill="#161b21" fill-rule="evenodd"/><rect {paper} fill="#151314"/>{wrinkles('#ffffff', .05, 30)}
{_design('#c8563f', '#dc9c38', '#dc9c38', '#e7c252', '#4677a3', sw=15, op=1, scales='#151314', eye=('#efe8d6', '#151314'), foam='#efe8d6')}
<rect {paper} fill="url(#__U__wet)" opacity=".4"/>
<g><path d="M640 300 C 660 286, 700 286, 720 300 L712 352 C 700 362, 660 362, 648 352 Z" fill="#26343d" stroke="#5d7584"/><ellipse cx="680" cy="300" rx="40" ry="10" fill="#9cc3d8" opacity=".55"/>
<rect x="612" y="372" width="70" height="16" rx="5" fill="#8a6a44" stroke="#5c452c"/><g stroke="#d8c39a" stroke-width="2">{''.join(f'<line x1="{x}" y1="388" x2="{x}" y2="398"/>' for x in range(616, 680, 6))}</g></g></g>
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''

ITEMS = [
 {'id': 'lights', 't': '불빛', 'la': '유리판 밑에 켜는 등', 'say': '유리판 밑에 불을 켜요. 그 위에 종이 본을 대고 종이를 올리면, 본의 선이 종이에 비쳐 보여요.'},
 {'id': 'stencil', 't': '종이 본', 'la': '型紙 · 감즙을 먹인 종이', 'say': '오려 둔 종이 본을 종이 밑에 대요. 불빛에 본의 선이 비쳐 보여요.'},
 {'id': 'color', 't': '물감', 'la': '광물처럼 자연에서 얻은 색', 'say': '선을 따라, 밝게 남길 곳에 물감을 칠해요. 다 칠하면 본을 빼고 종이를 말려요.'},
 {'id': 'paste', 't': '쌀풀', 'la': '糊 · 쌀로 쑨 풀과 비단 망', 'say': '이번엔 본과 고운 비단 망을 종이 위에 대고, 칠해 둔 색 위에 쌀풀을 발라 덮어요. 풀이 마를 때까지 기다려요.'},
 {'id': 'ink', 't': '먹', 'la': '墨 · 두부 물에 간 먹', 'say': '두부를 만들 때 나오는 물에 먹을 갈아 종이에 칠해요. 그러면 먹빛이 더 짙고 오래간다고 해요. 종이가 새까매져요.'},
 {'id': 'wash', 't': '찬물', 'la': '흐르는 물과 뻣뻣한 솔', 'say': '먹이 마르면 흐르는 찬물에 헹구며 뻣뻣한 솔로 힘껏 문질러요. 쌀풀이 씻겨 나가요.'},
]

CARD = {
 'id': 'aa-watanabe', 'mode': '놓아 보기 · 두 그림 나란히',
 'pagetitle': '먹 아래에서 떠오르는 그림',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>1940~1990년대</b><span>일본 도쿄 · 집 작업실</span>',
 'lead': '도쿄의 염색 가게에서 옷감 물들이는 일을 배운 소년이, 자라서 성경 이야기만 찍는 판화가가 되었어요. 그는 옷감에 쓰던 종이 본과 쌀풀로 종이에 판화를 찍었어요. 1977년 미국의 한 미술 교수가 적어 둔 그의 차례대로, 판화 한 장을 찍어 보세요.',
 'leadKid': '옛날 일본에 옷감을 물들이던 소년이 있었대. 어른이 되어서는 종이 본이랑 쌀풀로 성경 그림을 찍었어. 우리도 차례대로 찍어 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 1판). 와타나베의 판화는 저작권이 남아 있어 싣지 않았어요. 작업대 무대와 끝에 드러나는 물고기 무늬는 그의 판화가 아니라, 1977년 기록의 차례를 보여 주려고 이 안내서가 그린 그림이에요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 사람 얼굴이 나오는 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#2F4E6E;--accent-ink:#fffaf5;--soft:rgba(47,78,110,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#9db2c8;--accent-ink:#14100c;--soft:rgba(157,178,200,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#9db2c8;--accent-ink:#14100c;--soft:rgba(157,178,200,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '型染', 'y': '1947', 'sub': '도쿄 · 일본'},
 'doneNote': '판화 한 장을 걸 자리를, 사람들이 늘 모이는 곳에서 찾아보세요.',
 'images': {
  'card': {'src': S + 'MET_DP13870.jpg', 'cap': '잉어와 물결무늬 가타가미(옷감을 물들이는 종이 본), 19세기 일본 · 메트로폴리탄 미술관',
           'cr': '메트로폴리탄 미술관 · 퍼블릭 도메인(CC0) · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:MET_DP13870.jpg',
           'alt': '짙은 갈색 종이 본에 잉어 두 마리와 물결무늬를 오려 냈다. 오려 낸 흰 틈으로 비늘과 지느러미, 물결 선이 보인다.'},
  'katagami': {'src': S + 'Kata-gami-_Water_pattern_-_Google_Art_Project.jpg', 'cap': '물결무늬 가타가미(옷감을 물들이는 종이 본), 19세기 끝 무렵 일본 · 쿠퍼 휴잇 디자인 박물관',
               'cr': '만든 이 모름 · 퍼블릭 도메인 · 위키미디어 공용(구글 아트 프로젝트)', 'u': 'https://commons.wikimedia.org/wiki/File:Kata-gami-_Water_pattern_-_Google_Art_Project.jpg',
               'alt': '짙은 갈색 종이 한가운데에 소용돌이치는 물결무늬를 촘촘히 오려 낸 종이 본. 오려 낸 흰 틈 사이로 가는 실이 그물처럼 엇갈려 있다.'},
  'bingata': {'src': S + 'Garment_in_Bingata_Stencil_Dyeing_Okinawa_Main_Island_Second_Sho_Dynasty_Ryukyu_.jpg', 'max': 1920,
              'cap': '빈가타로 물들인 옷, 19세기 오키나와(류큐 왕국) · 도쿄국립박물관',
              'cr': '사진: Daderot · 퍼블릭 도메인(CC0) · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:Garment_in_Bingata_Stencil_Dyeing,_Okinawa_Main_Island,_Second_Sho_Dynasty,_Ryukyu_Kingdom,_19th_century,_peony_and_phoenix_design_on_light_blue_ramie_ground_-_Tokyo_National_Museum_-_DSC05385.JPG',
              'alt': '박물관 진열장에 펼쳐 건 옛 옷. 연한 푸른 바탕에 흰 모란꽃과 봉황, 대나무 잎, 구름 무늬가 물들어 있고, 깃은 분홍색, 소매 안쪽은 주황색이다.'},
  'mingeikan': {'src': S + 'Nihon_mingeikan_meguro_2009.jpg', 'cap': '도쿄 고마바의 일본민예관 정문, 2009년',
                'cr': '사진: Kamemaru2000 · CC BY-SA 3.0 · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:Nihon_mingeikan_meguro_2009.JPG',
                'alt': '돌기둥 두 개가 선 정문 너머로 기와지붕을 얹은 하얀 2층 건물이 보인다. 오른쪽 돌기둥에 세로로 쓴 나무 간판이 붙어 있고, 왼쪽에는 꽃이 핀 매화나무가 있다.'},
 },
 'extra_credits': [{'cr': '작업대 무대와 물고기 무늬: 이 안내서가 그린 그림 · 차례는 헬렌 메릿의 글(Christian Century, 1977)을 바탕으로', 'u': MERRITT}],
 'scenes': [
  {'id': 'shop', 'label': '염색 가게의 소년', 'kind': 'duo', 'imgs': ['katagami', 'bingata'],
   'caps': ['옷감을 물들이던 종이 본(가타가미), 19세기 끝 무렵', '종이 본으로 물들인 오키나와의 빈가타 옷, 19세기'],
   'text': ['와타나베 사다오(渡辺禎雄)는 1913년 도쿄에서 태어났어요. 열 살에 아버지를 여의고 학교를 일찍 그만둔 뒤, 염색 가게에 들어가 일을 배웠어요.',
            '열일곱 살이던 1930년, 이웃에 사는 한 그리스도인 여성이 그를 교회로 이끌었어요. 그해 성탄절에 그는 세례를 받았어요.'],
   'text2': ['1930년대 끝 무렵 그는 기모노와 오비(기모노 허리띠)의 무늬를 그리고 물들이는 일을 했어요. 1937년에는 염색가 세리자와 게이스케(芹沢銈介)의 전시를 보았어요. 세리자와는 오키나와의 빈가타(紅型)에서 종이 본을 대고 물들이는 법, 가타조메(型染)를 익힌 사람이에요.',
             '몇 해 뒤 와타나베는 세리자와가 가타조메를 가르치는 모임에 들어갔어요. 두 사람은 가까운 벗으로 지냈어요.'],
   'kid': '옷감 물들이는 가게에서 일하던 소년이 있었어. 이렇게 구멍 뚫린 종이 본을 대고 옷감에 색을 입혔대.',
   'kidq': '종이 본의 구멍으로 색이 들어가면, 옷감에 어떤 무늬가 생길까?'},
  {'id': 'bench', 'label': '먹 아래에서 떠오르는 그림', 'kind': 'mod', 'mod': 'place', 'night': False,
   'text': ['와타나베는 옷감을 물들이던 이 기법으로 종이에 판화를 찍었어요. 1977년, 미국의 미술 교수 헬렌 메릿(Helen H. Merritt)은 그가 판화 한 장을 찍는 차례를 자세히 적었어요.',
            '먼저 감즙을 먹인 두꺼운 종이에 붓과 먹으로 그림을 그리고, 작고 날카로운 칼로 오려 종이 본을 만들어요. 메릿은 오리는 동안에도 그림이 조금씩 바뀌어 간다고 적었어요. 색 판화는 그다음 아래 차례로 찍어요.'],
   'quote': {'t': '내 일은 아주 쉬워요. 누구라도 할 수 있어요.', 'from': '와타나베 사다오, 헬렌 메릿의 글(Christian Century, 1977)에서 · 이 안내서가 옮김', 'u': MERRITT},
   'text2': ['쌀풀이 덮인 곳에는 먹이 스미지 못해요. 그래서 풀을 씻어 내면 칠해 둔 색은 그대로 남고, 둘레만 까맣게 물들어요. 옷감을 물들이던 가타조메와 같은 이치예요.'],
   'kid': '불빛, 종이 본, 물감, 쌀풀, 먹, 찬물! 차례대로 놓아 볼까? 마지막에 그림이 짠 하고 나타나.',
   'kidq': '새까만 종이를 물에 헹구면 무슨 일이 생길까?'},
 ],
 'imagine': {'t': '종이 위로 찬물이 흘러요. 뻣뻣한 솔로 문지를수록 하얀 풀이 조금씩 풀려 나가요. 새까만 먹 아래에서 붉은빛, 노란빛이 하나씩 떠올라요. 작은 방 안에 먹 냄새와 물소리가 가득해요.',
             'kid': '눈을 감아 봐. 쏴아, 찬물이 흘러. 솔로 싹싹 문지르면, 새까만 종이에서 그림이 짠 나타나!'},
 'lines': ['먹 아래에서 떠오르는 그림.', '옷감을 물들이던 손으로 찍은 성경 이야기.', '내 일은 아주 쉬워요, 누구라도 할 수 있어요.', '사람들이 늘 모이는 곳에 걸린 한 장의 판화.'],
 'linesKid': ['불빛, 본, 물감, 풀, 먹, 물!', '짠! 그림이 나타났어.', '우리 집 어디에 걸까?'],
 'goals': {
  's4': {'t': '기록 차례대로', 'p': '메릿이 적은 차례(불빛, 종이 본, 물감, 쌀풀, 먹, 찬물)대로 다 놓으면 카드에 금박이 입혀져요.',
         'how': '1977년 기록의 차례대로 판화 한 장을 찍어 보세요', 'done': '기록 차례대로 판화 한 장을 찍었어요',
         'ways': [{'id': 'plOrder', 't': '불빛 → 종이 본 → 물감 → 쌀풀 → 먹 → 찬물 차례로 놓기'}]},
  's5': {'t': '판화를 걸 자리', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '사람들이 늘 모이는 곳 가운데 판화를 걸 자리를 고르거나, 아이와 함께 끝까지 보세요', 'done': '판화를 걸 자리를 정했어요',
         'ways': [{'id': 'home', 't': '사람들이 늘 모이는 곳 가운데, 판화 한 장을 걸 자리 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'place': {
   'items': ITEMS, 'order': '불빛, 종이 본, 물감, 쌀풀, 먹, 찬물',
   'intro': '아래에서 하나를 골라 작업대에 놓아 보세요. 1977년 기록에 남은 차례는 불빛, 종이 본, 물감, 쌀풀, 먹, 찬물이에요.',
   'climax': '쌀풀이 덮였던 곳에는 먹이 스미지 못했어요. 칠해 둔 색이 까만 바탕 위로 떠올라요.<span class="la">이 무늬는 와타나베의 판화가 아니라, 차례를 보여 주려고 이 안내서가 그린 연습 그림이에요 · 차례: 헬렌 메릿, 1977</span>',
   'home': ['거실', '부엌 식탁 곁', '현관', '교회 친교실', '교실'],
   'homeLabel': '판화를 걸 자리', 'homeWait': '판화를 다 찍은 뒤 고를 수 있어요',
   'wrongOrder': '메릿이 적어 둔 차례는 이래요: {order}', 'orderDone': '기록 차례대로 판화 한 장을 찍었어요',
   'daylight': False,
   'svg': stage_svg()}},
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 찍어 보기</button></div>
  <div class="pl-home" hidden><p>와타나베는 자기 판화가 ‘사람들이 늘 모이는 곳’에 걸리기를 바랐어요. 우리라면 어디에 걸까요?</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>민예</b> 사상가 야나기 무네요시(柳宗悦)가 1926년에 일으킨 운동이에요. 날마다 쓰는 소박한 물건의 아름다움을 귀히 여겼어요. 1936년에는 도쿄 고마바에 일본민예관을 열었어요.',
    '<b>첫 상</b> 1947년 일본민예관은 그의 큰 흑백 판화 「룻과 나오미」에 상을 주었어요. 메릿에 따르면 그는 다섯 해쯤 흑백 판화만 찍다가, 지금 알려진 색 판화를 시작했어요.',
    '<b>뉴욕에서</b> 1958년 뉴욕의 세인트제임스 교회가 연 일본 현대 판화전에서 「청동 뱀」이 1등을 했어요.',
    '<b>구긴 종이</b> 그는 닥나무 껍질로 뜬 고조가미(楮紙)와 모미가미(揉み紙)에 찍었어요. 모미가미는 곤약 가루로 쑨 풀을 바른 종이를, 젖은 채 손으로 주무르고 구겨 거친 결을 낸 종이예요.',
    '<b>그림 속 일본</b> 메릿은 「최후의 만찬」 상에 오른 도미와, 기모노의 가문(집안 문장)에서 온 둥근 무늬를 그의 판화 속 일본의 흔적으로 꼽아요.',
    '<b>어디에 걸까</b> 그는 판화가 사람들이 늘 모이는 곳에 걸려 있는 모습을 가장 보고 싶다고 적었어요(피오릴로가 옮겨 실은 글, 이 안내서가 옮김).']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>찍는 차례</b> 메릿(1977)은 색을 칠하고 쌀풀로 덮은 뒤 먹을 칠하고 씻어 내는 차례를 적었어요. 판화 해설가 존 피오릴로(2020)는 「기쿠(聞く)」(1960)를 예로 들어, 바탕을 붉게 칠하고 흰색·초록·노랑을 손으로 칠한 뒤 맨 마지막에 본을 대고 검은색을 붓으로 칠했다고 적어요.',
    '<b>세리자와에게 배운 때</b> 1937년 전시를 보고 몇 해 뒤(피오릴로), 1941년(호놀룰루 미술관), 1940년대(메릿)로 기록마다 달라요.',
    '<b>세리자와가 빈가타를 배운 때</b> 메릿은 1930년대 초 오키나와에서라고 적었어요. JR동일본이 펴낸 세리자와 연보는 1928년 박람회에서 빈가타 보자기를 보고 놀랐고, 1939년 첫 오키나와 여행 때 나하에서 배웠다고 적어요.']},
  {'h': '판화와 함께 읽는 말씀', 'p': [
    '말씀은 뜻만 옮기고, 본문은 대한성서공회 개역개정으로 이어 드려요.',
    '<b>' + bl('RUT.1', '룻기 1장 16절') + '</b> 남편을 잃은 룻이 시어머니 나오미에게, 어머니가 가는 곳에 나도 가겠다고 말해요. 1947년 상을 받은 판화가 룻과 나오미 이야기예요.',
    '<b>' + bl('NUM.21', '민수기 21장 9절') + '</b> 모세가 놋으로 뱀을 만들어 장대 위에 달자, 뱀에게 물린 사람이 그것을 쳐다보고 살았어요. 1958년 1등을 한 「청동 뱀」이 이 이야기예요.']},
  {'h': '판화 보러 가기', 'img': ['mingeikan'], 'checked': '2026년 11월 18일', 'p': [
    '그의 판화는 저작권이 남아 있어 이 카드에 싣지 않았어요. 아래 미술관과 해설 누리집에서 볼 수 있어요.',
    '도쿄 고마바의 일본민예관은 그에게 첫 상을 준 곳이에요. 여는 날과 시간은 누리집에서 확인해 주세요.'],
   'links': [{'t': '호놀룰루 미술관 온라인 소장품: 와타나베 사다오의 판화들', 'u': HONO, 'm': '영어'},
             {'t': 'Viewing Japanese Prints: 와타나베 사다오 해설과 판화 사진', 'u': FIOR, 'm': '영어'},
             {'t': '일본민예관: 박물관 소개와 관람 안내', 'u': MINGEI, 'm': '일본어'}]},
 ],
 'src': [
  {'l': '헬렌 H. 메릿, 「The Prints of Sadao Watanabe」, Christian Century 1977년 12월 21일(religion-online) — 감즙 먹인 종이에 그려 오린 본, 색 판화의 차례(불빛 위에 본, 색, 본과 비단 망·쌀풀, 두부 물에 간 먹, 찬물과 솔), 1940년대 세리자와, 1947년 「룻과 나오미」 상, 다섯 해쯤 흑백, 도미와 가문 무늬, 그의 말', 'u': MERRITT},
  {'l': '존 피오릴로, Viewing Japanese Prints(2020) — 열 살에 아버지를 여읨, 염색 가게, 1930년 열일곱 살 세례, 1937년 세리자와 전시, 가타조메 모임, 고조가미·모미가미, 「기쿠」(1960)의 차례, 1958년 「청동 뱀」, 성경 이야기만, 걸고 싶은 곳에 대한 그의 글', 'u': FIOR},
  {'l': '호놀룰루 미술관 소장품 작가 소개 — 1913년 도쿄, 1941년 세리자와에게 배우기 시작, 1947년 일본민예관 상, 1958년 뉴욕 1등', 'u': HONO},
  {'l': 'SadaoHanga Catalogue(작품 목록 누리집) — 1930년 성탄절 세례, 1930년대 끝 무렵 기모노·오비 무늬 일, 세리자와와의 만남', 'u': HANGA},
  {'l': '일본민예관: 박물관 소개 — 1926년 기획, 1936년 고마바에 문을 엶, 야나기 무네요시', 'u': MINGEI},
  {'l': 'JR동일본, 「芹沢銈介が残した東北の美」 연보(2019) — 1928년 빈가타 보자기, 1939년 첫 오키나와 여행과 나하에서 배움', 'u': JRE},
  {'l': '대한성서공회 개역개정: 룻기 1장 · 민수기 21장', 'u': NKRV + 'RUT.1'},
  {'l': '위키미디어 공용: 물결무늬 가타가미(쿠퍼 휴잇 디자인 박물관, 19세기 끝 무렵) 파일 정보', 'u': 'https://commons.wikimedia.org/wiki/File:Kata-gami-_Water_pattern_-_Google_Art_Project.jpg'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '60% 70%', 'p1': '45% 40%', 's0': 1.2, 's1': 1.05, 'kicker': '1913~1996 · 일본 도쿄', 'title': '먹 아래에서 떠오르는 그림',
   'lines': [{'t': '옷감을 물들이던 종이 본이에요.'}, {'t': '도쿄의 한 소년이 이런 본으로 옷감을 물들이는 일을 배웠어요.'}],
   'kid': [{'t': '구멍이 송송 뚫린 종이야. 물고기랑 물결 모양이 보여?'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '염색 가게의 소년'},
  {'type': 'img', 'ch': 1, 'img': 'katagami', 'fit': 'cover', 'p0': '35% 45%', 'p1': '60% 55%', 's0': 1.3, 's1': 1.1, 'cap': '물결무늬 가타가미, 19세기 끝 무렵',
   'lines': [{'t': '열 살에 아버지를 여의고, 염색 가게에서 일을 배웠어요.'}, {'t': '열일곱 살 성탄절에는 세례를 받았어요.'}],
   'kid': [{'t': '어려서 옷감 물들이는 가게에서 일을 배웠어.'}, {'t': '이 종이 본으로 물들이면 어떤 무늬가 나올까?', 'ask': True}]},
  {'type': 'img', 'ch': 1, 'img': 'bingata', 'fit': 'cover', 'p0': '50% 35%', 'p1': '50% 60%', 's0': 1.25, 's1': 1.05, 'cap': '오키나와 빈가타 옷, 19세기',
   'lines': [{'t': '1937년, 그는 염색가 세리자와의 전시를 보았어요.'}, {'t': '세리자와는 오키나와의 빈가타에서 종이 본으로 물들이는 법을 익힌 사람이에요.'}],
   'kid': [{'t': '종이 본으로 물들인 오키나와 옷이야. 꽃이랑 새가 보여?'}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '작업대'},
  {'type': 'mod', 'mod': 'place', 'ch': 2,
   'lines': [{'t': '1977년 한 미술 교수가 적어 둔 차례예요.'},
             {'t': '유리판 밑에 불을 켜고,', 'act': 'lights'},
             {'t': '종이 본을 종이 밑에 대요.', 'act': 'stencil'},
             {'t': '밝게 남길 곳에 물감을 칠하고,', 'act': 'color'},
             {'t': '칠한 색 위에 쌀풀을 발라 덮어요.', 'act': 'paste'},
             {'t': '두부 물에 간 먹을 칠하면 종이가 새까매져요.', 'act': 'ink', 'wait': 1200},
             {'t': '찬물에 헹구며 솔로 문지르면,', 'act': 'wash', 'wait': 1500},
             {'t': '풀이 씻겨 나간 자리에서 색이 떠올라요.', 'act': 'day', 'wait': 1500},
             {'t': '내 일은 아주 쉬워요. 누구라도 할 수 있어요.', 'q': True, 'from': '와타나베 사다오, 메릿의 글에서'}],
   'kid': [{'t': '불을 켜고!', 'act': 'lights'}, {'t': '종이 본을 대고!', 'act': 'stencil'}, {'t': '색칠하고!', 'act': 'color'},
           {'t': '쌀풀로 덮고!', 'act': 'paste'}, {'t': '먹을 칠하면 새까매져.', 'act': 'ink', 'wait': 1200},
           {'t': '물로 싹싹 헹구면?', 'act': 'wash', 'ask': True, 'wait': 1500}, {'t': '짠! 그림이 나타났어.', 'act': 'day', 'wait': 1500}]},
  {'type': 'imagine', 'ch': 3,
   'lines': [{'t': '종이 위로 찬물이 흘러요.'}, {'t': '솔로 문지를수록 하얀 풀이 조금씩 풀려 나가요.'}, {'t': '먹 아래에서 붉은빛, 노란빛이 떠올라요.'}],
   'kid': [{'t': '눈을 감아 봐. 쏴아, 찬물이 흘러.'}, {'t': '싹싹 문지르면, 그림이 짠!'}]},
  {'type': 'reward', 'ch': 3},
 ],
}
