# -*- coding: utf-8 -*-
"""깊은 카드: 칠십인역(ob-lxx) · 중심 방식 = 놓아 보기(필론이 적은 파로스섬 잔치)
기준서 1판 · 틀 deep3-3 · 키트 2판(보탬) · 2026-11-18 만들기 시작 · 29번 묶음 둘째 카드
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 해마다 파로스섬 바닷가에서 번역을 기념하던 잔치 — 1세기 필론의 기록
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 필론이 적은 잔치의 차례(배로 건너옴 → 기도와 감사 → 천막 → 모래밭 자리 → 친척·친구와 잔치)
     → 그 차례대로 바닷가에 하나씩 놓아 보기
카드 크기: 큰 카드(장면 4개) — 아리스테아스의 편지·필론·탈무드 세 기록, 등대 복원도, 오늘의 요새까지 재료가 넉넉해요.
  가장 오래된 파피루스 조각(라일랜즈 458·푸아드 266)은 위키미디어 그림이 작고 화면 단추·설명 글자가 들어 있어 그림 없이 ‘더 깊이’ 글로만 썼어요.
무대 그림(SVG)은 이 안내서가 필론 『모세의 생애』 2권 41~42항을 바탕으로 그렸어요(남의 그림을 따라 그리지 않음).
그림 원본(src)은 deep_src/ob-lxx/ (저장소 밖). 받는 법: commons_get.py"""
S = 'ob-lxx/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

PHILO = 'https://www.earlychristianwritings.com/yonge/book25.html'
PHILO41 = 'https://cts.perseids.org/read/greekLit/tlg0018/tlg022/1st1K-eng1/2.41-2.60'
ARIS = 'https://greekdoc.github.io/apocrypha/aristeas10.html'
JE = 'https://www.jewishencyclopedia.com/articles/1765-aristeas-letter-of'
TAL = 'https://www.sefaria.org/Megillah.9a'
MAN = 'https://www.digitalcollections.manchester.ac.uk/view/MS-GREEK-P-00458/1'


def stage_svg():
    """파로스섬 바닷가 무대(800×450, 화면에는 가운데 600폭이 보여요). 놓을 것: boat · prayer · tents · sand · feast. 이 안내서가 그림."""
    def person(x, y, robe, s=1.0):
        # 서서 두 팔을 든 사람(기도). 얼굴은 그리지 않아요.
        return (f'<circle cx="{x}" cy="{y}" r="{5*s:.1f}" fill="#7a5236"/>'
                f'<path d="M{x-6*s:.1f} {y+8*s:.1f} L{x+6*s:.1f} {y+8*s:.1f} L{x+9*s:.1f} {y+33*s:.1f} L{x-9*s:.1f} {y+33*s:.1f}Z" fill="{robe}" stroke="#5a4130" stroke-width=".8"/>'
                f'<path d="M{x-5*s:.1f} {y+10*s:.1f} L{x-12*s:.1f} {y-4*s:.1f} M{x+5*s:.1f} {y+10*s:.1f} L{x+12*s:.1f} {y-4*s:.1f}" '
                f'stroke="{robe}" stroke-width="{3.2*s:.1f}" stroke-linecap="round" fill="none"/>')

    def sitter(x, y, robe):
        return (f'<circle cx="{x}" cy="{y}" r="4.6" fill="#7a5236"/>'
                f'<path d="M{x-8} {y+20} C {x-8} {y+8}, {x+8} {y+8}, {x+8} {y+20}Z" fill="{robe}" stroke="#5a4130" stroke-width=".8"/>')

    waves = ''.join(f'<path d="M{x} {y} q 9 -4 18 0 t 18 0" fill="none" stroke="#e8f6f8" stroke-width="1.4" opacity="{o}"/>'
                    for x, y, o in [(110, 236, .55), (170, 262, .6), (300, 228, .5), (540, 240, .55), (590, 272, .6), (120, 280, .7), (360, 262, .6), (600, 226, .45)])
    city = ''.join(f'<rect x="{x}" y="{204 - h}" width="{w}" height="{h + 2}" fill="#9db1bd"/>' for x, w, h in
                   [(60, 26, 10), (84, 18, 16), (100, 30, 8), (128, 14, 20), (140, 34, 11), (172, 20, 15), (190, 40, 7), (228, 16, 13), (242, 30, 9), (270, 22, 5)])
    clouds = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#ffffff" opacity=".7"/>' for x, y, rx, ry in
                     [(190, 60, 48, 11), (230, 52, 30, 9), (420, 40, 56, 10), (470, 48, 34, 8)])
    tower = ('<g>'
             '<path d="M556 262 C 596 246 636 250 700 246 C 730 244 760 250 800 248 L800 266 L556 270Z" fill="#b9a27a"/>'
             '<rect x="616" y="168" width="48" height="84" fill="#f1eadb" stroke="#bfb29a" stroke-width="1"/>'
             '<rect x="640" y="168" width="24" height="84" fill="#ded3bf"/>'
             '<rect x="613" y="164" width="54" height="6" fill="#e6dccb" stroke="#bfb29a" stroke-width=".8"/>'
             '<path d="M626 164 L654 164 L652 126 L628 126Z" fill="#f1eadb" stroke="#bfb29a" stroke-width="1"/>'
             '<path d="M640 164 L654 164 L652 126 L640 126Z" fill="#ded3bf"/>'
             '<rect x="624" y="122" width="32" height="5" fill="#e6dccb" stroke="#bfb29a" stroke-width=".8"/>'
             '<rect x="633" y="100" width="14" height="22" fill="#f1eadb" stroke="#bfb29a" stroke-width="1"/>'
             '<path d="M631 100 L640 86 L649 100Z" fill="#d8ccb6" stroke="#bfb29a" stroke-width=".8"/>'
             '<circle cx="640" cy="108" r="3.2" fill="#ffcf6a"/>'
             + ''.join(f'<rect x="{x}" y="{y}" width="4" height="7" fill="#8d8170"/>' for x, y in [(624, 186), (634, 206), (624, 226), (630, 140), (646, 186), (646, 226)])
             + '</g>')
    boat = ('<g class="obj" data-o="boat">'
            '<path d="M206 236 L256 236 L247 245 L215 245Z" fill="#6b4a2e"/><line x1="231" y1="236" x2="231" y2="203" stroke="#5a3d25" stroke-width="2"/>'
            '<path d="M233 205 L233 233 L254 231Z" fill="#f4ead2" stroke="#c9b48a" stroke-width=".8"/>'
            '<path d="M424 270 L524 270 L510 285 L440 285Z" fill="#6b4a2e"/><line x1="472" y1="270" x2="472" y2="212" stroke="#5a3d25" stroke-width="2.4"/>'
            '<path d="M475 216 L475 266 L512 262 L507 220Z" fill="#efe0bf" stroke="#c9a46a" stroke-width="1"/>'
            '<path d="M476 232 L509 229 M476 248 L510 245" stroke="#c9a46a" stroke-width="2"/>'
            '<circle cx="450" cy="265" r="3.4" fill="#7a5236"/><circle cx="461" cy="264" r="3.4" fill="#7a5236"/><circle cx="495" cy="265" r="3.4" fill="#7a5236"/>'
            '</g>')
    prayer = ('<g class="obj" data-o="prayer">' + person(352, 302, '#f4f0e6') + person(374, 299, '#4f6c8f') + person(396, 303, '#b0663e')
              + person(418, 300, '#e6d3a6') + person(440, 304, '#8a6a4a') + '</g>')
    tents = ('<g class="obj" data-o="tents">'
             '<path d="M106 340 L134 304 L162 340Z" fill="#c8d6d9" stroke="#7d8f94" stroke-width="1.2"/>'
             '<path d="M150 356 L196 298 L242 356Z" fill="#ece0c4" stroke="#8b6a42" stroke-width="1.4"/>'
             '<path d="M186 356 L196 326 L206 356Z" fill="#6b4a2e"/>'
             '<path d="M173 327 L219 327 M164 340 L228 340" stroke="#c99a5c" stroke-width="2.4"/>'
             '<path d="M236 350 L272 304 L308 350Z" fill="#d9a46b" stroke="#8b6a42" stroke-width="1.4"/>'
             '<path d="M265 350 L272 330 L279 350Z" fill="#6b4a2e"/>'
             '<path d="M196 298 L140 360 M196 298 L254 362 M272 304 L318 354" stroke="#8b6a42" stroke-width=".9" opacity=".7"/>'
             '</g>')
    sand = ('<g class="obj" data-o="sand">'
            '<path d="M498 372 L578 366 L598 386 L514 393Z" fill="#b5523c"/><path d="M504 379 L585 373 M509 386 L591 380" stroke="#e6c27a" stroke-width="2"/>'
            '<ellipse cx="552" cy="376" rx="27" ry="6.5" fill="#f1ebdd" stroke="#8a7a62" stroke-width=".8"/><circle cx="522" cy="374" r="5" fill="#7a5236"/>'
            '<path d="M588 330 L660 326 L676 343 L602 347Z" fill="#3f6f7a"/><path d="M594 336 L666 332 M598 342 L671 338" stroke="#d9c79a" stroke-width="1.8"/>'
            '<ellipse cx="632" cy="336" rx="23" ry="5.5" fill="#e9dcc0" stroke="#8a7a62" stroke-width=".8"/><circle cx="658" cy="334" r="4.6" fill="#7a5236"/>'
            '</g>')
    feast = ('<g class="obj" data-o="feast">'
             '<path d="M292 386 L470 378 L488 410 L286 418Z" fill="#f6efe1" stroke="#c9b48a" stroke-width="1.2"/>'
             '<path d="M320 392 a 11 6 0 0 0 22 0Z" fill="#9b3f2f"/><path d="M372 390 a 12 6 0 0 0 24 0Z" fill="#9b3f2f"/><path d="M424 387 a 11 6 0 0 0 22 0Z" fill="#9b3f2f"/>'
             '<ellipse cx="350" cy="402" rx="10" ry="5" fill="#c88a43"/><ellipse cx="404" cy="401" rx="10" ry="5" fill="#c88a43"/>'
             + ''.join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#6d3a6b"/>' for x, y in [(436, 402), (441, 401), (446, 402), (438, 406), (443, 406), (440, 410)])
             + '<path d="M458 372 C 452 376 452 384 456 390 L 468 390 C 472 384 472 376 466 372 L 466 366 L 458 366Z" fill="#a8643a" stroke="#6b3f22" stroke-width=".8"/>'
             + sitter(282, 372, '#4f6c8f') + sitter(482, 362, '#b0663e') + sitter(318, 420, '#e6d3a6') + sitter(452, 420, '#8a6a4a')
             + '</g>')
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="파로스섬 바닷가. 바다 건너 왼쪽에 도시가 보이고, 오른쪽 곶에 높은 등대가 서 있다. 놓은 것들이 바다와 모래밭에 하나씩 나타난다."><defs>
<linearGradient id="__U__sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fb7dd"/><stop offset="1" stop-color="#e6f0f0"/></linearGradient>
<linearGradient id="__U__sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffcf8a" stop-opacity="0"/><stop offset=".55" stop-color="#ffc98a" stop-opacity=".22"/><stop offset="1" stop-color="#ffd9a0" stop-opacity=".42"/></linearGradient>
<linearGradient id="__U__sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2f7fa8"/><stop offset="1" stop-color="#6db8cc"/></linearGradient>
<linearGradient id="__U__sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ead6a6"/><stop offset="1" stop-color="#d9bb83"/></linearGradient>
<radialGradient id="__U__warm" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff1c8" stop-opacity=".8"/><stop offset="1" stop-color="#ffe0a0" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".62" r=".75"><stop offset="0" stop-color="#fff6dc" stop-opacity=".55"/><stop offset=".6" stop-color="#ffe2a8" stop-opacity=".2"/><stop offset="1" stop-color="#ffd38a" stop-opacity="0"/></radialGradient></defs>
<rect width="800" height="450" fill="url(#__U__sky)"/><rect class="sky2" width="800" height="450" fill="url(#__U__sky2)"/>
<circle cx="540" cy="64" r="34" fill="#fff6d8" opacity=".45"/><circle cx="540" cy="64" r="20" fill="#fffbe9"/>
<g>{clouds}</g>
<rect x="0" y="200" width="800" height="110" fill="url(#__U__sea)"/>
<g>{city}</g>
<g>{waves}</g>
{tower}
{boat}
<path d="M0 300 C 160 286 300 302 450 292 C 560 285 680 296 800 288 L800 450 L0 450Z" fill="url(#__U__sand)"/>
<path d="M0 300 C 160 286 300 302 450 292 C 560 285 680 296 800 288" fill="none" stroke="#ffffff" stroke-width="3" opacity=".8"/>
<path d="M0 306 C 160 293 300 309 450 299 C 560 292 680 303 800 295" fill="none" stroke="#c9ad78" stroke-width="5" opacity=".45"/>
<ellipse class="glow" cx="400" cy="380" rx="380" ry="110" fill="url(#__U__warm)" opacity=".14"/>
{prayer}
{tents}
{sand}
{feast}
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''


ITEMS = [
 {'id': 'boat', 't': '배', 'la': '필론 · 2권 41항', 'say': '배를 타고 섬으로 건너와요. 유대인도, 다른 민족 사람들도 함께예요.'},
 {'id': 'prayer', 't': '감사 기도', 'la': '필론 · 2권 41항', 'say': '번역의 빛이 처음 비친 자리를 기리며, 오래되었지만 늘 새로운 선물을 주신 하나님께 감사해요.'},
 {'id': 'tents', 't': '천막', 'la': '필론 · 2권 42항', 'say': '기도와 감사를 마친 사람들이 바닷가에 천막을 쳐요.'},
 {'id': 'sand', 't': '모래밭 자리', 'la': '필론 · 2권 42항', 'say': '천막 없이 모래 위, 하늘 아래 눕는 사람들도 있어요.'},
 {'id': 'feast', 't': '잔칫상', 'la': '필론 · 2권 42항', 'say': '친척, 친구와 함께 잔치를 벌여요.'},
]

CARD = {
 'id': 'ob-lxx', 'mode': '놓아 보기',
 'pagetitle': '파로스섬의 잔치',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>기원전 3세기 ~ 1세기</b><span>이집트 알렉산드리아 앞바다 · 파로스섬</span>',
 'lead': '알렉산드리아 앞바다의 파로스섬에서는 해마다 잔치가 열렸어요. 성경이 처음 그리스어로 옮겨진 곳이라고 전해진 바닷가였어요. 1세기 학자 필론이 적은 차례대로 그 잔치를 놓아 보세요.',
 'leadKid': '옛날에 성경을 다른 나라 말로 처음 옮긴 섬이 있었대. 사람들이 해마다 거기서 소풍 같은 잔치를 했어. 우리도 하나씩 놓아 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 1판). 일흔두 명의 번역 이야기는 「아리스테아스의 편지」가 전하는 이야기라고 밝혔고, 섬의 잔치는 1세기 필론의 기록을 따랐어요. 바닷가 무대는 이 안내서가 필론의 글을 바탕으로 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 # 화면 색: 지중해 바다빛(밝게) · 밤바다의 물빛(어둡게)
 'theme': """:root{--accent:#1f6f8b;--accent-ink:#f4fbfd;--soft:rgba(31,111,139,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#7cc3d8;--accent-ink:#0b1c22;--soft:rgba(124,195,216,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#7cc3d8;--accent-ink:#0b1c22;--soft:rgba(124,195,216,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '파로스', 'y': '1세기', 'sub': '알렉산드리아'},
 'doneNote': '그리스어 성경 한 구절을 우리말 성경과 나란히 펴 보세요. 옮긴 사람들의 고민이 보여요.',
 'images': {
  'pharos': {'src': S + 'Lighthouse_-_Thiersch.png',
             'cap': '헤르만 티르시가 그린 파로스 등대 복원도, 1909년', 'cr': '그림: 헤르만 티르시 · 퍼블릭 도메인 · 위키미디어 공용',
             'u': 'https://commons.wikimedia.org/wiki/File:Lighthouse_-_Thiersch.png',
             'alt': '흑백 선 그림. 바다 앞 낮은 성벽 안에 창이 많은 네모난 아랫단이 높이 서 있고, 그 위에 팔각형 가운뎃단, 맨 위에 둥근 탑과 사람 모양 조각상이 있다. 꼭대기 옆으로 연기가 비스듬히 흐르고, 왼쪽 바다에 돛단배 한 척이 있다.'},
  'philo': {'src': S + 'PhiloThevet.jpg',
            'cap': '앙드레 테베의 인물 판화집에 실린 필론, 1584년', 'cr': '그림: 앙드레 테베 · 퍼블릭 도메인 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:PhiloThevet.jpg',
            'alt': '흑백 판화. 둥근 모자를 쓰고 수염을 기른 노인이 망토를 두르고 한 손에 책을 들고 있다. 모자 띠와 망토 깃에 히브리 글자가 적혀 있다.'},
  'qaitbay': {'src': S + 'Citadel_of_Qaitbay_Alexandria_Egypt.jpg', 'crop': [0, 0, 1, 0.75],
              'cap': '옛 등대 자리에 선 카이트베이 요새, 2007년', 'cr': '사진: Argenberg · CC BY 2.0 · 위키미디어 공용',
              'u': 'https://commons.wikimedia.org/wiki/File:Citadel_of_Qaitbay,_Alexandria,_Egypt.jpg',
              'alt': '맑은 하늘 아래 누런 돌로 쌓은 네모난 요새. 양쪽 모서리에 둥근 탑이 있고, 가운데 높은 탑 위에 이집트 국기가 날린다. 아래쪽 가운데에 아치 모양 문이 있다.'},
 },
 'extra_credits': [{'cr': '놓아 보기 무대: 이 안내서가 그린 파로스섬 바닷가 잔치 · 필론 『모세의 생애』 2권 41~42항을 바탕으로', 'u': PHILO41}],
 'scenes': [
  {'id': 'legend', 'label': '일흔두 명의 이야기', 'kind': 'photo', 'img': 'card',
   'cap': '1587년 로마판 칠십인역의 첫 장 · 판화 양옆은 발밑에 이름이 적힌 모세와 에스라',
   'text': ['기원전 3세기, 이집트 알렉산드리아에는 그리스어를 쓰는 유대인이 많이 살았어요. 학자들은 그 무렵 그들을 위해 모세오경이 처음 그리스어로 옮겨졌다고 봐요.',
            '「아리스테아스의 편지」라는 옛 글은 이 번역에 긴 이야기를 붙였어요. 왕 프톨레마이오스 2세가 바라서 예루살렘에서 원로 일흔두 명이 왔다고요. 학자들은 이 편지를 왕의 시대가 지난 뒤 유대인이 쓴 이야기로 봐요.'],
   'kid': '아주 옛날 이집트에 그리스 말을 쓰는 유대 사람들이 많이 살았대. 그래서 성경을 그리스 말로 옮겼어.',
   'kidq': '왜 그리스 말로 옮겨야 했을까?'},
  {'id': 'island', 'label': '바닷가 집의 일흔두 날', 'kind': 'photo', 'img': 'pharos',
   'text': ['편지에 따르면 데메트리오스라는 사람이 일흔두 명을 데리고, 바다 위로 난 일곱 스타디온(1킬로미터 남짓) 둑길을 지나 다리를 건넜어요. 파로스섬 북쪽, 바닷가에 지은 아름다운 집이 일터였어요.',
            '그들은 바닷물에 손을 씻고 기도한 뒤 맡은 구절을 읽고 옮겼어요. 저마다 옮긴 것을 서로 견주어 하나로 맞추었고, 일흔두 날 만에 일을 마쳤다고 해요.'],
   'text2': ['다 마치자 데메트리오스가 유대인들을 그 집에 모아 번역을 읽어 주었어요. 사람들은 이 번역을 그대로 지키자며, 한 낱말이라도 더하거나 바꾸거나 빼는 사람에게 저주를 빌었다고 편지는 전해요. 섬 끝에는 프톨레마이오스 2세 때 완성된 큰 등대가 서 있었어요.'],
   'kid': '바닷물에 손을 씻고 기도한 다음, 다 같이 번역했대.',
   'kidq': '여럿이 함께 번역하면 어떤 점이 좋을까?'},
  {'id': 'feast', 'label': '해마다 열린 섬의 잔치', 'kind': 'mod', 'mod': 'place', 'night': False,
   'text': ['그 뒤 250년도 더 지나, 알렉산드리아의 유대인 학자 필론이 이렇게 적었어요. 지금도 해마다 파로스섬에서 모임과 잔치가 열린다고요.',
            '유대인뿐 아니라 다른 민족 사람들도 배를 타고 건너와, 번역의 빛이 처음 비친 자리를 기리고 하나님께 감사한다고 했어요. 아래 바닷가에 필론이 적은 차례대로 하나씩 놓아 보세요. 무대는 이 안내서가 필론의 글을 바탕으로 그렸어요.'],
   'quote': {'t': '기도와 감사를 드린 뒤, 어떤 이들은 바닷가에 천막을 쳤고, 어떤 이들은 천막도 없이 바닷가 모래 위 하늘 아래 누워 친척, 친구와 함께 잔치를 벌였다. 그때만은 바닷가가 왕궁의 살림살이보다 더 아름다운 집이라고 여겼다.',
             'from': '필론, 『모세의 생애』 2권 42항(1세기) · 욘지의 영어 번역(1855)을 이 안내서가 우리말로 옮김', 'u': PHILO41},
   'text2': ['필론은 번역하던 날의 이야기도 편지와 조금 다르게 전했어요. 보이지 않는 누군가 불러 주기라도 한 듯, 모두가 똑같은 낱말을 골라 썼다고요.'],
   'kid': '배를 타고 섬에 와서, 고맙다고 기도하고, 천막을 치고, 모래 위에서 잔치를 했대!',
   'kidq': '바닷가 잔치에 간다면 누구랑 같이 가고 싶어?'},
  {'id': 'today', 'label': '오늘의 파로스', 'kind': 'photo', 'img': 'qaitbay',
   'text': ['등대는 여러 번의 지진으로 무너졌고, 15세기 말 술탄 카이트베이가 그 자리에 요새를 세웠어요. 섬을 잇던 둑길에는 흙이 쌓여, 지금은 도시가 들어선 땅이 되었어요.',
            '바닷가의 잔치는 사라졌지만, 번역은 남았어요. 칠십인역의 낱말은 신약 성경 곳곳에 남아 있어요(아래 ‘함께 읽는 말씀’).'],
   'kid': '등대가 있던 자리에 지금은 성처럼 생긴 요새가 있어.',
   'kidq': '옛날 등대는 밤바다의 배들에게 어떤 일을 해 주었을까?'},
 ],
 'imagine': {'t': '바닷바람에 천막 자락이 펄럭여요. 멀리 등대가 하얗게 서 있고, 모래는 발바닥에 따뜻해요. 어디선가 빵 냄새와 웃음소리가 들려와요. 누군가 그리스어로, 누군가 히브리어로 감사의 노래를 불러요.',
             'kid': '눈을 감아 봐. 바닷바람이 솔솔 불어. 모래가 따뜻해. 맛있는 빵 냄새! 다 같이 고마워요 노래를 불러.'},
 'lines': ['오래되었지만 늘 새로운 선물.', '왕궁보다 아름다운 모래밭.', '번역의 빛이 처음 비친 자리.', '바닷물에 손을 씻고 옮긴 말씀.'],
 'linesKid': ['배 타고 섬으로 잔치 가자!', '모래 위에서 다 같이 고마워요.'],
 'goals': {
  's4': {'t': '필론이 적은 차례대로', 'p': '배, 감사 기도, 천막, 모래밭 자리, 잔칫상을 필론이 적은 차례대로 다 놓으면 카드에 금박이 입혀져요.',
         'how': '필론이 적은 차례대로 섬의 잔치를 다 놓아 보세요', 'done': '필론이 적은 차례대로 섬의 잔치를 열었어요',
         'ways': [{'id': 'plOrder', 't': '배 → 감사 기도 → 천막 → 모래밭 자리 → 잔칫상 차례로 놓기'}]},
  's5': {'t': '나의 바닷가 자리', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '잔치에 간 사람이 되어 바닷가 자리를 고르거나, 아이와 함께 끝까지 보세요', 'done': '바닷가에 내 자리를 펼쳤어요',
         'ways': [{'id': 'home', 't': '잔치에 간 사람이라면 천막 안과 하늘 아래 모래 위 가운데 어디에 자리를 펼지 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'place': {
   'items': ITEMS, 'order': '배, 감사 기도, 천막, 모래밭 자리, 잔칫상',
   'intro': '아래에서 하나를 골라 바닷가에 놓아 보세요. 필론이 적은 차례는 배, 감사 기도, 천막, 모래밭 자리, 잔칫상이에요.',
   'climax': '그날만은 바닷가가 왕궁보다 아름다운 집이었어요.<span class="la">오래되었지만 늘 새로운 선물을 기뻐한 날 · 필론, 『모세의 생애』 2권 41~42항</span>',
   'home': ['바닷가 천막 안', '하늘 아래 모래 위'],
   'homeLabel': '내가 고른 바닷가 자리',
   'homeWait': '섬의 잔치를 다 놓아 본 뒤 고를 수 있어요',
   'wrongOrder': '필론이 적은 차례는 이래요: {order}',
   'orderDone': '필론이 적은 차례대로 다 놓았어요',
   'daylight': False,
   'svg': stage_svg()}},
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 놓아 보기</button></div>
  <div class="pl-home" hidden><p>필론의 잔치에 간 사람이라면, 어디에 자리를 펼까요?</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>칠십인역</b> ‘일흔 사람의 번역’이라는 뜻의 이름이에요. 일흔두 명의 이야기에서 나왔고, 로마 숫자로 일흔을 뜻하는 LXX라고 줄여 써요.',
    '<b>필론</b> 기원전 20년 무렵에 태어나 기원후 50년 무렵 세상을 떠난 알렉산드리아의 유대인 철학자예요. 그리스어로 글을 썼고, 성경도 주로 칠십인역으로 읽었어요.',
    '<b>파로스섬</b> 필론은 섬의 목이 혀처럼 도시 쪽으로 뻗어 있고, 얕은 물과 모래톱이 파도 소리를 막아 조용하다고 적었어요. 그래서 번역하는 이들이 율법에만 마음을 쏟을 수 있는 곳으로 골랐다고요.',
    '<b>스타디온</b> 옛 그리스의 거리 단위예요. 일곱 스타디온 둑길은 1.2킬로미터쯤이었어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>함께 맞추었을까, 저절로 같았을까</b> 「아리스테아스의 편지」는 일흔두 명이 저마다 옮긴 것을 서로 견주어 맞추었다고 해요. 필론은 보이지 않는 누군가 불러 주듯 모두가 똑같은 낱말을 썼다고 하고, 탈무드는 왕이 일흔두 명을 저마다 다른 방에 두었는데, 하나님이 모두에게 지혜를 주셔서 같은 뜻으로 옮겼다고 전해요.',
    '<b>누구를 위해 옮겼을까</b> 편지는 데메트리오스의 권유로 왕이 자기 도서관에 유대인의 율법 책 번역을 갖추려 했다고 해요. 학자들은 그보다 그리스어를 쓰던 유대인들 스스로를 위한 번역으로 보는 편이에요.',
    '<b>언제 쓴 편지일까</b> 편지는 왕의 신하가 쓴 것처럼 꾸몄지만, 유대교를 줄곧 높이는 글이라 학자들은 유대인이 썼다고 봐요. 기원전 200년 무렵에 썼다는 학자도, 그보다 늦게 기원전 63년 전에 썼다는 학자도 있어요.']},
  {'h': '가장 오래된 조각', 'p': [
    '번역을 처음 적은 두루마리는 남아 있지 않아요. 지금 남은 가장 오래된 칠십인역 조각들은 이집트에서 나온 파피루스예요. 파피루스는 같은 이름의 물풀 줄기로 만든 종이예요.',
    '영국 맨체스터 존 라일랜즈 도서관의 신명기 조각(라일랜즈 458)은 기원전 2세기 중반의 것으로 봐요. 사해 사본이 나오기 전까지는 가장 오래된 그리스어 성경 사본이었어요.',
    '기원전 1세기 무렵의 다른 신명기 조각(푸아드 266)에는 그리스어 글 사이에 하나님의 이름만 네모난 히브리 글자로 적혀 있어요. 처음부터 그렇게 썼는지, 나중에 다른 손이 써넣었는지는 학자마다 의견이 달라요.']},
  {'h': '함께 읽는 말씀', 'p': [
    '말씀은 뜻만 옮기고, 본문은 대한성서공회 개역개정으로 이어 드려요.',
    '<b>' + bl('MAT.1', '마태복음 1장 23절') + '</b> 이사야의 말을 인용하며 ‘처녀가 아들을 낳을 것’이라고 해요. 히브리어 이사야 7장 14절의 ‘알마(젊은 여자)’를 칠십인역이 ‘파르테노스(처녀)’로 옮겼고, 마태복음은 이 그리스어 낱말을 따라 인용해요. 이 낱말의 뜻을 두고는 오늘도 학자마다 풀이가 달라요.',
    '<b>' + bl('ISA.7', '이사야 7장 14절') + '</b> 마태복음이 인용한 바로 그 구절이에요. 우리말 성경과 견주어 읽어 보세요.']},
  {'h': '그림 속 필론', 'img': ['philo'], 'p': [
    '1584년 프랑스의 앙드레 테베가 펴낸 인물 판화집에 실린 필론이에요. 필론보다 1,500년쯤 뒤에 그린 것이라, 실제 얼굴과 같은지는 알 수 없어요.']},
  {'h': '직접 가 보기 · 집에서 읽기', 'checked': '2026년 11월 18일', 'p': [
    '알렉산드리아 바닷가의 옛 등대 자리에는 카이트베이 요새가 있어 둘러볼 수 있어요. 여는 때와 여행경보는 가시기 전에 꼭 확인해 주세요.',
    '집에서는 칠십인역을 옮긴 영어 성경(NETS)을 개인 공부용으로 무료로 내려받아 읽을 수 있어요. 가장 오래된 파피루스 조각도 맨체스터 대학 누리집에서 크게 볼 수 있어요.'],
   'links': [{'t': 'NETS — 칠십인역 영어 번역(책별 PDF, 개인 공부용)', 'u': 'https://ccat.sas.upenn.edu/nets/edition/', 'm': '영어'},
             {'t': '필론, 『모세의 생애』 2권 — 섬의 잔치 이야기(25~44항)', 'u': PHILO, 'm': '영어'},
             {'t': '맨체스터 대학 디지털 컬렉션 — 라일랜즈 458 신명기 조각 크게 보기', 'u': MAN, 'm': '영어'}]},
 ],
 'src': [
  {'l': '필론, 『모세의 생애』 2권 25~44항(욘지 영어 번역, 1855) — 프톨레마이오스 필라델푸스, 혀처럼 뻗은 섬의 목과 얕은 물·모래톱, 율법에만 마음을 쏟음, 보이지 않는 이가 불러 주듯 같은 낱말, 해마다 섬의 모임과 잔치', 'u': PHILO},
  {'l': '필론, 『모세의 생애』 2권 41~42항(Perseids, 욘지 번역) — 배로 건너옴, 번역의 빛이 처음 비친 자리, 감사, 천막과 모래, 친척·친구와 잔치, 왕궁보다 아름다운 바닷가', 'u': PHILO41},
  {'l': '「아리스테아스의 편지」 301~311항(영어 번역) — 데메트리오스, 일곱 스타디온 둑길과 다리, 파로스 북쪽 바닷가의 아름다운 집, 서로 견주어 맞춤, 바닷물에 손 씻고 기도, 72일, 유대인들에게 읽어 줌, 고치는 이에게 저주', 'u': ARIS},
  {'l': 'Jewish Encyclopedia: Aristeas, Letter of — 데메트리오스의 권유로 왕의 도서관에, 진짜 편지가 아님, 유대인 저자, 연대(기원전 200년 무렵설 · 기원전 63년 이전설)', 'u': JE},
  {'l': '바빌로니아 탈무드 메길라 9a(Sefaria) — 일흔두 원로를 저마다 다른 방에 두었는데, 하나님이 저마다의 마음에 지혜를 주셔서 모두 같은 뜻으로 옮김', 'u': TAL},
  {'l': 'Wikipedia: Septuagint — 길잡이(이름의 뜻, LXX, 모세오경은 기원전 3세기, 그리스어를 쓰는 유대인을 위해)', 'u': 'https://en.wikipedia.org/wiki/Septuagint'},
  {'l': 'Wikipedia: Philo — 길잡이(기원전 20년 무렵~기원후 50년 무렵, 성경을 주로 칠십인역으로 읽음)', 'u': 'https://en.wikipedia.org/wiki/Philo'},
  {'l': '맨체스터 대학 디지털 컬렉션: Rylands Greek Papyrus 458 — 신명기 두루마리 조각, 그리스도 이전 구약 본문의 가장 이른 증거 가운데 하나', 'u': MAN},
  {'l': 'Wikipedia: Papyrus Rylands 458 — 길잡이(기원전 2세기 중반, 사해 사본 전까지 가장 오래된 그리스어 성경 사본)', 'u': 'https://en.wikipedia.org/wiki/Papyrus_Rylands_458'},
  {'l': 'Wikipedia: Papyrus Fouad 266 — 길잡이(기원전 1세기, 네모난 히브리 글자의 하나님 이름, 처음부터인지 나중에 써넣었는지 의견이 갈림)', 'u': 'https://en.wikipedia.org/wiki/Papyrus_Fouad_266'},
  {'l': 'Wikipedia: Lighthouse of Alexandria — 길잡이(프톨레마이오스 1세 시작·2세 완성, 지진으로 무너짐, 1480년 무렵 카이트베이의 요새)', 'u': 'https://en.wikipedia.org/wiki/Lighthouse_of_Alexandria'},
  {'l': 'Wikipedia: Heptastadion — 길잡이(일곱 스타디온 둑길 1.2킬로미터쯤, 흙이 쌓여 땅이 됨)', 'u': 'https://en.wikipedia.org/wiki/Heptastadion'},
  {'l': 'Wikipedia: Matthew 1:23 — 길잡이(마태복음이 칠십인역의 낱말로 이사야 7:14를 인용)', 'u': 'https://en.wikipedia.org/wiki/Matthew_1:23'},
  {'l': 'The Bible and Interpretation(애리조나 대학): ’Almah in Isaiah 7:14 — 칠십인역의 parthenos와 마태복음 1:23', 'u': 'https://bibleinterp.arizona.edu/node/3932'},
  {'l': 'NETS(펜실베이니아 대학) — 칠십인역 영어 번역 전자판, 개인 공부용 무료 내려받기', 'u': 'https://ccat.sas.upenn.edu/nets/edition/'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'pharos', 'fit': 'cover', 'p0': '50% 60%', 'p1': '50% 40%', 's0': 1.2, 's1': 1.05, 'kicker': '기원전 3세기~1세기 · 알렉산드리아 파로스섬', 'title': '파로스섬의 잔치',
   'lines': [{'t': '알렉산드리아 앞바다의 작은 섬, 파로스.'}, {'t': '성경이 처음 그리스어로 옮겨진 곳이라고 전해지는 바닷가예요.'}],
   'kid': [{'t': '바다 위에 섬이 있어. 커다란 등대도 있대!'}, {'t': '여기서 성경을 다른 나라 말로 옮겼대.'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '일흔두 명'},
  {'type': 'img', 'ch': 1, 'img': 'card', 'fit': 'contain', 'p0': '50% 30%', 'p1': '50% 60%', 's0': 1.15, 's1': 1.0, 'cap': '1587년 로마판 칠십인역의 첫 장',
   'lines': [{'t': '그리스어를 쓰는 유대인들을 위해, 모세오경이 처음 그리스어로 옮겨졌어요.'}, {'t': '옛 편지는 예루살렘에서 원로 일흔두 명이 왔다고 전해요.'}, {'t': '학자들은 이 편지를 훗날 쓴 이야기로 봐요.'}],
   'kid': [{'t': '그리스 말을 쓰는 사람들을 위해 성경을 옮겼대.'}, {'t': '일흔두 명이 왔다는 이야기가 있어.', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '바닷가 집'},
  {'type': 'img', 'ch': 2, 'img': 'pharos', 'fit': 'cover', 'p0': '20% 85%', 'p1': '55% 60%', 's0': 1.35, 's1': 1.1, 'cap': '파로스 등대 복원도, 1909년',
   'lines': [{'t': '둑길과 다리를 건너, 섬 북쪽 바닷가의 아름다운 집으로.'}, {'t': '바닷물에 손을 씻고 기도한 뒤, 맡은 구절을 읽고 옮겼대요.'}, {'t': '서로 견주어 맞추며 일흔두 날 만에 마쳤다고 전해요.'}],
   'kid': [{'t': '바닷물에 손을 씻고 기도했대.'}, {'t': '여럿이 함께 번역하면 뭐가 좋을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '섬의 잔치'},
  {'type': 'mod', 'mod': 'place', 'ch': 3,
   'lines': [{'t': '250년도 더 지나 필론이 적었어요. 지금도 해마다 섬에서 잔치가 열린다고.'},
             {'t': '사람들이 배를 타고 건너와요.', 'act': 'boat'},
             {'t': '번역의 빛이 처음 비친 자리에서 하나님께 감사해요.', 'act': 'prayer'},
             {'t': '바닷가에 천막을 치고,', 'act': 'tents'},
             {'t': '천막 없이 모래 위에 눕기도 해요.', 'act': 'sand'},
             {'t': '친척, 친구와 함께 잔치를 벌여요.', 'act': 'feast', 'wait': 1500},
             {'t': '그날만은 바닷가가 왕궁보다 아름다운 집이었대요.', 'act': 'day', 'q': True, 'from': '필론, 『모세의 생애』 2권 42항에서'}],
   'kid': [{'t': '배를 타고 섬으로!', 'act': 'boat'}, {'t': '고맙습니다, 기도해요.', 'act': 'prayer'}, {'t': '천막을 치고,', 'act': 'tents'},
           {'t': '모래 위에 누워요.', 'act': 'sand'}, {'t': '다 같이 냠냠 잔치!', 'act': 'feast', 'wait': 1500}, {'t': '왕궁보다 좋은 바닷가래!', 'act': 'day', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '오늘의 파로스'},
  {'type': 'img', 'ch': 4, 'img': 'qaitbay', 'fit': 'cover', 'p0': '50% 55%', 'p1': '50% 45%', 's0': 1.15, 's1': 1.0, 'cap': '옛 등대 자리의 카이트베이 요새',
   'lines': [{'t': '등대는 지진으로 무너지고, 그 자리에 요새가 섰어요.'}, {'t': '잔치는 사라졌지만, 번역은 신약 성경 곳곳에 남았어요.'}],
   'kid': [{'t': '등대 자리에 지금은 요새가 있어.'}, {'t': '그래도 그때 옮긴 성경은 지금도 읽어!', 'ask': True}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '바닷바람에 천막 자락이 펄럭여요. 모래는 발바닥에 따뜻해요.'}, {'t': '빵 냄새와 웃음소리가 들려와요.'}, {'t': '누군가 그리스어로, 누군가 히브리어로 감사의 노래를 불러요.'}],
   'kid': [{'t': '눈을 감아 봐. 바닷바람이 솔솔.'}, {'t': '맛있는 빵 냄새! 다 같이 고마워요 노래를 불러.'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
