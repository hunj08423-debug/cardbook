# -*- coding: utf-8 -*-
"""깊은 카드: 폴란드 유리 장식 ‘봄브키’(craft-bombki) · 중심 방식 = 놓아 보기(+두 그림 나란히, 고르기)
기준서 1판 · 틀 deep3-2 · 키트 2판 · 2026-11-18 5번 묶음 창이 만듦.
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 유리 공이 시골집까지 오기 전, 성탄 전날 저녁 폴란드 남쪽 산골집.
     천장 들보에 거꾸로 매단 전나무 꼭대기(포드와지니치카) 아래에서, 오플라테크로 ‘시비아티(세상)’를 지어 다는 때.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 오플라테크 동그라미 세 장(하나는 그대로, 하나는 반으로,
     하나는 넷으로)을 차례로 붙이고 실을 꿰어 포드와지니치카에 매달기(폴란드 민족지 단체의 만들기 안내 차례).
     도우미 고르기: 하얀 오플라테크로 지을지, 물들인 오플라테크로 지을지.
카드 크기: 한 장면 카드(장면 2개). 사용자 의견(2026-11-18): 작은 카드로 정하기 전 앞면 물음 쪽으로 다시 찾기 → 그림이 넉넉해 한 장면 카드.
무대 그림은 아래 stage_svg()가 그려요(이 안내서가 그림, 만들기 안내의 차례를 따름).
그림 원본(src)은 deep_src/craft-bombki/ (저장소 밖)."""
import random

S = 'craft-bombki/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

PRAC = 'https://czteryporyroku.etnograficzna.pl/wp-content/uploads/2026/01/Boze-Narodzenie-i-Nowy-Rok-Podlazniczka-i-swiaty.pdf'
PRAC_ZIMA = 'https://czteryporyroku.etnograficzna.pl/wp-content/uploads/2026/01/Material-uzupelniajacy_-Zima.pdf'
UDZ = 'https://radiokrakow.pl/aktualnosci/swiateczna-dekoratornia-kolebki-z-oplatkow-warsztaty-dla-doroslych-i-mlodziezy'
LACHY = 'https://dzieje.pl/node/25019'
SLASK = 'https://dzieje.pl/node/27400'
KIELCE = 'https://radiokielce.pl/1137602/swiaty-to-najbardziej-tradycyjna-polska-ozdoba-swiateczna'
WROC = 'https://www.radiokrakow.pl/aktualnosci/etnografka-choinka-to-nastepczyni-podlazniczki/'
CHRZ = 'https://www.radiokrakow.pl/aktualnosci/malopolskazachodnia/tradycyjne-ozdoby-na-choinke-mozna-wykonac-takze-z-oplatka'
NATGEO = 'https://www.national-geographic.pl/nauka/potega-oplatka/'
MALOP = 'https://visitmalopolska.pl/en_GB/-/krakow-muzeum-etnograficzne-boze-narodzenie'
MEK25 = 'https://www.radiokrakow.pl/promocja/muzeum-etnograficzne-w-grudniu/'
MILICZ = 'https://www.wroclaw.pl/kultura/ale-bombki-w-miliczu-dziala-muzeum-bombki-zobacz-jakie-cudenka-mozna-tam-zobaczyc-galeria'
NOWAD = 'https://podkarpackie.travel/en/product/museum-of-christmas-glass-baubles-in-nowa-deba'


# ---------- 무대 그림(SVG): 성탄 전날 저녁, 산골집 방. 들보에 거꾸로 매단 전나무 꼭대기와 저녁상 ----------
TX, TY = 560, 292          # 식탁 위에서 짓는 시비아트 가운데
HX, HY, HT = 262, 300, 236  # 매단 시비아트 가운데, 실 윗끝(전나무 끝)

def _swiat(cx, cy, r, parts=('whole', 'halves', 'quarters')):
    s = ''
    if 'whole' in parts:
        s += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f4ecda" stroke="#cdbb93" stroke-width="1.4"/>'
              f'<circle cx="{cx}" cy="{cy}" r="{r * .78:.1f}" fill="none" stroke="#e2d4b2" stroke-width="1"/>'
              + ''.join(f'<circle cx="{cx + r * .45 * __import__("math").cos(a / 6 * 6.283):.1f}" cy="{cy + r * .45 * __import__("math").sin(a / 6 * 6.283):.1f}" r="{r * .12:.1f}" fill="none" stroke="#e2d4b2" stroke-width=".9"/>' for a in range(6)))
    if 'quarters' in parts:
        s += (f'<ellipse cx="{cx}" cy="{cy}" rx="{r * .7:.1f}" ry="{r}" fill="#efe5cf" fill-opacity=".55" stroke="#cdbb93" stroke-width="1.2"/>'
              f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r * .7:.1f}" fill="#efe5cf" fill-opacity=".45" stroke="#cdbb93" stroke-width="1.2"/>')
    if 'halves' in parts:
        s += (f'<ellipse cx="{cx}" cy="{cy}" rx="{r * .32:.1f}" ry="{r}" fill="#f7f0e0" stroke="#c3ae82" stroke-width="1.3"/>'
              f'<line x1="{cx}" y1="{cy - r}" x2="{cx}" y2="{cy + r}" stroke="#c3ae82" stroke-width="1"/>')
    return s

def _fir():
    """들보(y=34)에 거꾸로 매단 전나무 꼭대기: 위가 넓고 아래 끝(y=HT)이 뾰족해요."""
    R = random.Random(1924)
    out = [f'<line x1="{HX}" y1="34" x2="{HX}" y2="{HT}" stroke="#5a3e24" stroke-width="5" stroke-linecap="round"/>']
    for k in range(9):
        y = 46 + k * 20
        w = 128 - k * 13
        for side in (-1, 1):
            x2, y2 = HX + side * w, y + 26
            out.append(f'<path d="M{HX} {y} Q{HX + side * w * .55:.0f} {y + 4} {x2:.0f} {y2:.0f}" fill="none" stroke="#2f4a2c" stroke-width="3" stroke-linecap="round"/>')
            for j in range(7):
                t = (j + 1) / 8
                px, py = HX + side * w * t, y + 2 + 24 * t * t
                out.append(f'<path d="M{px:.0f} {py:.0f} l{side * R.uniform(6, 11):.0f} {R.uniform(9, 14):.0f} M{px:.0f} {py:.0f} l{-side * R.uniform(2, 5):.0f} {R.uniform(9, 13):.0f}" stroke="{R.choice(["#3e6337", "#355a30", "#47703f"])}" stroke-width="2.2" stroke-linecap="round"/>')
    deco = []
    for (x, y, kind) in [(HX - 92, 92, 'apple'), (HX + 70, 118, 'apple'), (HX - 40, 160, 'nut'), (HX + 34, 70, 'nut'), (HX - 60, 128, 'star'),
                         (HX + 96, 84, 'star'), (HX + 18, 186, 'apple'), (HX - 20, 104, 'star'), (HX + 52, 160, 'nut')]:
        if kind == 'apple':
            deco.append(f'<line x1="{x}" y1="{y - 12}" x2="{x}" y2="{y - 6}" stroke="#7a5532" stroke-width="1"/><circle cx="{x}" cy="{y}" r="7.5" fill="#b8352b"/><circle cx="{x - 2.5}" cy="{y - 2.5}" r="2" fill="#e9776b"/>')
        elif kind == 'nut':
            deco.append(f'<line x1="{x}" y1="{y - 10}" x2="{x}" y2="{y - 5}" stroke="#7a5532" stroke-width="1"/><ellipse cx="{x}" cy="{y}" rx="5" ry="5.8" fill="#8a6136"/><path d="M{x} {y - 5} V{y + 5}" stroke="#5c3d1f" stroke-width=".8"/>')
        else:
            pts = ' '.join(f'{x + (9 if i % 2 == 0 else 3.6) * __import__("math").cos(i * 3.1416 / 4):.1f},{y + (9 if i % 2 == 0 else 3.6) * __import__("math").sin(i * 3.1416 / 4):.1f}' for i in range(8))
            deco.append(f'<line x1="{x}" y1="{y - 14}" x2="{x}" y2="{y - 9}" stroke="#7a5532" stroke-width="1"/><polygon points="{pts}" fill="#e3c26a" stroke="#b8963e" stroke-width=".8"/>')
    chain = ''.join(f'<ellipse cx="{HX - 104 + k * 13}" cy="{130 + 22 * __import__("math").sin(k / 16 * 3.1416):.0f}" rx="6" ry="3.4" fill="none" stroke="{["#c9483b", "#e3c26a", "#4f7fb0", "#e8e0cc"][k % 4]}" stroke-width="2"/>' for k in range(17))
    return ''.join(out) + chain + ''.join(deco)

def stage_svg():
    R = random.Random(1900)
    logs = ''.join(f'<rect x="0" y="{y}" width="800" height="26" fill="{R.choice(["#4b3322", "#523826", "#47301f"])}"/><line x1="0" y1="{y + 25.5}" x2="800" y2="{y + 25.5}" stroke="#2c1d12" stroke-width="1.2"/>' for y in range(34, 340, 26))
    hay = ''.join(f'<path d="M{x:.0f} 352 q{R.uniform(-4, 4):.0f} {R.uniform(8, 14):.0f} {R.uniform(-6, 6):.0f} {R.uniform(14, 22):.0f}" stroke="#d6b45c" stroke-width="1.4" fill="none"/>' for x in [R.uniform(380, 780) for _ in range(28)])
    wafers = ''.join(f'<rect x="{430 + k * 3}" y="{338 - k * 2}" width="58" height="38" rx="2" fill="#f6efdf" stroke="#d8c8a4" stroke-width="1"/>' for k in range(3))
    build = (f'<g class="obj bld" data-o="whole">{_swiat(TX, TY, 44, ("whole",))}</g>'
             f'<g class="obj bld" data-o="quarters">{_swiat(TX, TY, 44, ("quarters",))}</g>'
             f'<g class="obj bld" data-o="halves">{_swiat(TX, TY, 44, ("halves",))}</g>'
             f'<g class="obj bld" data-o="thread"><path d="M{TX} {TY - 44} V{TY - 96} q0 -8 -6 -8" fill="none" stroke="#efe6d2" stroke-width="1.6"/>'
             f'<line x1="{TX - 26}" y1="{TY - 118}" x2="{TX + 8}" y2="{TY - 92}" stroke="#c9ccd1" stroke-width="2.2" stroke-linecap="round"/></g>')
    hang = (f'<g class="obj hangg" data-o="hang"><g class="sw-sway"><line x1="{HX}" y1="{HT}" x2="{HX}" y2="{HY - 38}" stroke="#efe6d2" stroke-width="1.6"/>'
            f'{_swiat(HX, HY, 38)}</g></g>')
    style = ('.pl .obj.on.hangg ~ .obj.bld{opacity:0;transform:translateY(-10px)}'
             '.pl .sw-sway{transform-box:view-box;transform-origin:' + f'{HX}px {HT}px' + '}'
             '.pl.lit .sw-sway{animation:swSway 3.2s ease-in-out 3}'
             '@keyframes swSway{0%,100%{transform:rotate(0)}25%{transform:rotate(4deg)}75%{transform:rotate(-4deg)}}'
             '@media (prefers-reduced-motion:reduce){.pl.lit .sw-sway{animation:none}}')
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="성탄 전날 저녁, 통나무 산골집. 천장 들보에 전나무 꼭대기가 거꾸로 매달려 있고 사과와 호두, 짚 별, 종이 사슬이 달려 있다. 아래 하얀 식탁보 위에서 웨하스 동그라미를 하나씩 붙여 둥근 세상 모양 장식을 짓고, 다 지으면 전나무 아래에 매단다."><style>{style}</style><defs>
<radialGradient id="__U__warm" cx=".5" cy=".6" r=".6"><stop offset="0" stop-color="#ffcf86"/><stop offset=".55" stop-color="#d9893c" stop-opacity=".5"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".35" cy=".55" r=".75"><stop offset="0" stop-color="#fff0c8" stop-opacity=".5"/><stop offset=".55" stop-color="#ffc77a" stop-opacity=".22"/><stop offset="1" stop-color="#ff9f4a" stop-opacity="0"/></radialGradient>
<linearGradient id="__U__win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1430"/><stop offset="1" stop-color="#22355a"/></linearGradient>
</defs>
<rect width="800" height="450" fill="#3a271a"/>{logs}
<g><rect x="636" y="96" width="104" height="120" rx="3" fill="#2a1a10"/><rect x="644" y="104" width="88" height="104" fill="url(#__U__win)"/>
<rect x="686" y="104" width="4" height="104" fill="#2a1a10"/><rect x="644" y="154" width="88" height="4" fill="#2a1a10"/>
<path d="M644 196 C 664 186 690 192 710 184 L732 182 L732 208 L644 208Z" fill="#cdd6e3" opacity=".5"/></g>
<rect x="0" y="0" width="800" height="34" fill="#2b1c11"/><rect x="0" y="26" width="800" height="12" fill="#6a4a2c"/><line x1="0" y1="38.5" x2="800" y2="38.5" stroke="#2b1c11" stroke-width="1.5"/>
<ellipse class="glow" cx="440" cy="300" rx="330" ry="220" fill="url(#__U__warm)" opacity=".14"/>
{_fir()}
<rect x="360" y="340" width="440" height="110" fill="#f2ede2"/><path d="M360 340 H800" stroke="#d9cfbd" stroke-width="2"/>{hay}
<rect x="360" y="420" width="440" height="30" fill="#e7e0d1"/>
{wafers}
{hang}{build}
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''


ITEMS = [
 {'id': 'whole', 't': '온 동그라미', 'la': 'całe kółko', 'say': '첫 장은 자르지 않고 그대로 둬요. 시비아트의 바탕이 돼요.'},
 {'id': 'halves', 't': '반쪽 둘', 'la': 'dwie połówki', 'say': '둘째 장은 반으로 잘라, 온 동그라미에 먼저 붙여요. 가장자리에 침이나 물을 살짝 묻히면 붙어요.'},
 {'id': 'quarters', 't': '사분의 일 넷', 'la': 'cztery ćwiartki', 'say': '셋째 장은 넷으로 잘라, 붙인 반쪽들 사이사이에 끼워 붙여요.'},
 {'id': 'thread', 't': '실 꿰기', 'la': 'nitka', 'say': '바늘에 실을 꿰어 시비아트 윗부분을 살짝 찔러 통과시키고, 고리로 묶어요.'},
 {'id': 'hang', 't': '매달기', 'la': 'na podłaźniczkę', 'say': '다 지은 시비아트를 포드와지니치카 아래에 매달아요.'},
]

CARD = {
 'id': 'craft-bombki',
 'mode': '놓아 보기 · 두 그림',
 'pagetitle': '천장에 매단 세상',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>유리 공이 오기 전, 1930년대까지</b><span>폴란드 남쪽 · 포드할레와 베스키디 산골</span>',
 'lead': '유리 공이 폴란드 시골집까지 오기 전, 산골집 천장에는 거꾸로 매단 전나무 꼭대기가 있었어요. 성탄 전날 저녁, 얇은 웨하스 세 장으로 둥근 ‘세상’을 지어 거기에 매달아 보세요.',
 'leadKid': '옛날 폴란드 산골집에서는 나무를 거꾸로 천장에 매달았대. 웨하스 세 장으로 동그란 장식을 만들어 달아 볼까?',
 'meta': '영화처럼 약 2분 · 천천히 읽으면 4분',
 'draft': '검수 전 시안이에요(기준서 1판). 포드와지니치카와 시비아티는 폴란드 민족지 단체의 안내와 1924년 크라쿠프 지방 기록, 여러 지역 박물관의 설명을 따랐어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 2분',
 'theme': """:root{--accent:#9a3b2c;--accent-ink:#fff8f2;--soft:rgba(154,59,44,.09);--stamp:#a8392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#e7a08a;--accent-ink:#1d0f0a;--soft:rgba(231,160,138,.10);--stamp:#e46e5c}}
:root[data-theme="dark"]{--accent:#e7a08a;--accent-ink:#1d0f0a;--soft:rgba(231,160,138,.10);--stamp:#e46e5c}""",
 'stamp': {'t': '세상', 'y': '1924', 'sub': '크라쿠프 지방 · 성탄 전날'},
 'doneNote': '유리 공을 나무에 걸 때, 산골집 천장에 매달던 하얀 ‘세상’도 떠올려 보세요.',
 'images': {
  'tetmajer': {'src': S + 'W_odzimierz_Tetmajer_-_Pod_a_niczka_1900.jpg',
               'cap': '브워지미에시 테트마예르, 「포드와지니치카」, 1900년',
               'cr': '그림: Włodzimierz Tetmajer · 퍼블릭 도메인 · 위키미디어 공용',
               'u': 'https://commons.wikimedia.org/wiki/File:W%C5%82odzimierz_Tetmajer_-_Pod%C5%82a%C5%BAniczka_1900.jpg',
               'alt': '어두운 시골집 방을 그린 유화. 천장에 거꾸로 매단 푸른 가지 묶음에 작은 불빛과 붉은 장식이 달려 있다. 그 아래 창가 의자에 머릿수건을 쓴 여인들과 어린 소녀, 검은 옷의 남자가 모여 있고, 오른쪽에 짚더미가 있다.'},
  'podlaznik': {'src': S + 'Podlaznik.jpg',
                'cap': '크라쿠프 지방의 포드와즈니크를 그린 그림(크라쿠프 민족지 박물관, 1932년 이전)',
                'cr': '그림: 작가 모름 · 퍼블릭 도메인 · 위키미디어 공용',
                'u': 'https://commons.wikimedia.org/wiki/File:Podlaznik.jpg',
                'alt': '흰 바탕에 색연필로 그린 거꾸로 매단 전나무 가지. 위쪽 끈에 매달려 아래로 가지가 퍼지고, 갈색 종이 사슬과 노란·파란 짚 장식, 작은 구슬과 붉은 열매가 달려 있다. 맨 아래에 분홍빛 둥근 장식이 매달려 있다.'},
  'swiaty': {'src': S + 'wiaty_-_traditional_Polish_Christmas_decoration_03.jpg',
             'cap': '크라쿠프 민족지 박물관에 전시된 시비아티, 2022년',
             'cr': '사진: Maire · CC BY-SA 4.0 · 위키미디어 공용',
             'u': 'https://commons.wikimedia.org/wiki/File:%C5%9Awiaty_-_traditional_Polish_Christmas_decoration_03.jpg',
             'alt': '검은 바탕에 실로 매단 웨하스 장식 둘. 왼쪽은 분홍·노랑·초록·파랑 웨하스 동그라미를 여러 장 겹쳐 공처럼 만든 것, 오른쪽은 노란 공 둘레에 뾰족한 초록 뿔이 여러 개 달린 별 모양이다.'},
  'swiaty1': {'src': S + 'wiaty_-_traditional_Polish_Christmas_decoration_01.jpg',
              'cap': '크라쿠프 민족지 박물관 천장에 매단 시비아티와 웨하스 장식, 2022년',
              'cr': '사진: Maire · CC BY-SA 4.0 · 위키미디어 공용',
              'u': 'https://commons.wikimedia.org/wiki/File:%C5%9Awiaty_-_traditional_Polish_Christmas_decoration_01.jpg',
              'alt': '어두운 천장 아래 실에 매단 여러 장식. 커다란 연노랑 공, 분홍·노랑 공, 뾰족한 노란 별, 레이스처럼 오려 낸 동그란 웨하스 장식들이 떠 있고 벽에 그림자가 진다.'},
  'gok': {'src': S + 'GOK_Podegrodzie_-_pod_a_niczka.jpg',
          'cap': '포데그로제 문화관의 전통 포드와지니치카(라흐 사람들의 방식)',
          'cr': '사진: 13piotrek · CC BY-SA 3.0 · 위키미디어 공용',
          'u': 'https://commons.wikimedia.org/wiki/File:GOK_Podegrodzie_-_pod%C5%82a%C5%BAniczka.jpg',
          'alt': '나무 천장에 거꾸로 매단 마른 전나무 꼭대기를 아래에서 올려다본 사진. 짚으로 엮은 별, 레이스 같은 하얀 웨하스 동그라미, 색종이 사슬, 분홍 종이 공 장식이 달려 있다.'},
 },
 'scenes': [
  {'id': 'beam', 'label': '유리 공이 오기 전, 산골집 천장', 'kind': 'duo', 'imgs': ['tetmajer', 'podlaznik'],
   'caps': ['테트마예르, 「포드와지니치카」(1900)', '크라쿠프 지방의 포드와즈니크(1932년 이전)'],
   'text': ['유리 공이 시골집 성탄 나무에 걸리기 전, 폴란드 남쪽 산골 포드할레와 베스키디의 집에서는 ‘포드와지니치카’를 걸었어요. 가문비나무나 전나무 꼭대기를 잘라 천장 들보에 거꾸로 매단 것이에요.',
            '흔히 성탄 전날 저녁상 바로 위나 방 한쪽 구석에 매달았어요. 종이 사슬과 짚으로 엮은 별, 사과와 호두, 과자를 달았어요. 집안에 복과 넉넉함을 가져온다고 여겼대요.'],
   'text2': ['왼쪽은 1900년 폴란드 화가 브워지미에시 테트마예르가 그린 「포드와지니치카」예요. 불빛이 달린 포드와지니치카 아래 식구들이 모여 있고, 오른쪽에 짚더미가 보여요.',
             '오른쪽은 크라쿠프 민족지 박물관이 1932년 이전에 남긴 포드와즈니크 그림이에요. 맨 아래에 둥근 장식이 매달려 있어요.',
             '산데츠 지방 라흐 사람들의 집에서는 서 있는 성탄 나무가 들어온 뒤에도, 1930년대까지 포드와지니치카가 흔했어요.'],
   'kid': '옛날 폴란드 산골집에서는 나무 꼭대기를 거꾸로 천장에 매달았대! 사과랑 호두도 달았대.',
   'kidq': '거꾸로 매단 나무 아래에서 식구들은 무엇을 했을까?'},
  {'id': 'swiat', 'label': '웨하스 세 장으로 지은 세상', 'kind': 'mod', 'mod': 'place', 'night': False,
   'text': ['성탄 전날 저녁상에서 나누어 먹는 얇은 웨하스를 ‘오플라테크’라고 해요(‘폴란드의 오플라테크’ 카드 참고). 이 오플라테크로 둥근 장식 ‘시비아티’를 지어 포드와지니치카에 달았어요.',
            '‘시비아트’는 폴란드 말로 ‘세상’이라는 뜻이에요. 1924년 크라쿠프 지방의 풍습을 적은 책에는 이렇게 나와요.'],
   'quote': {'t': '그때[저녁 식사 뒤]에는 오플라테크로 세상을 붙여 만들고, 그 아래 매다는 요람도 만들어요…',
             'from': '세베린 우지엘라, 『크라쿠프 사람들』(1924) 37쪽 · 폴란드어를 이 안내서가 옮김', 'u': UDZ},
   'text2': ['동그라미 세 장 가운데 하나는 그대로, 하나는 반으로, 하나는 넷으로 잘라요. 오플라테크는 잘 부서져서 입김을 불어 살짝 눅눅하게 한 뒤 잘라요.',
             '무대 그림은 폴란드 민족지 단체 ‘프라초브니아 에트노그라피치나’의 만들기 안내 차례를 따라 이 안내서가 그렸어요.'],
   'choose': True,
   'kid': '웨하스 세 장으로 동그란 세상을 만들어 보자! 하나는 그대로, 하나는 반으로, 하나는 넷으로!',
   'kidq': '웨하스를 반으로, 또 넷으로 자르면 모두 몇 조각이 될까?'},
 ],
 'imagine': {'t': '창밖은 캄캄하고, 방 안은 따뜻해요. 들보에 매단 전나무에서 송진 냄새가 나요. 식탁보 아래로 짚이 바스락거려요. 얇은 웨하스 가장자리에 입김을 불면, 하얀 동그라미가 살며시 휘어요.',
             'kid': '눈을 감아 봐. 방 안에 나무 냄새가 나. 후~ 입김을 불어 웨하스를 붙이자. 하얀 세상이 동그랗게 생겼어!'},
 'lines': ['천장에 매단 하얀 세상.', '웨하스 세 장, 일곱 조각.', '거꾸로 매단 나무 아래의 저녁.', '유리 공이 오기 전의 둥근 장식.'],
 'linesKid': ['웨하스로 동그란 세상!', '나무를 거꾸로 매달았어.', '후~ 입김을 불어 붙여요.'],
 'goals': {
  's4': {'t': '안내 차례대로 시비아트 짓기', 'p': '만들기 안내의 차례(온 동그라미, 반쪽 둘, 사분의 일 넷, 실 꿰기, 매달기)대로 놓으면 카드에 금박이 입혀져요.',
         'how': '안내 차례대로 오플라테크를 붙이고 매달아 보세요', 'done': '시비아트 하나를 지어 매달았어요',
         'ways': [{'id': 'plOrder', 't': '온 동그라미 → 반쪽 둘 → 사분의 일 넷 → 실 꿰기 → 매달기'}]},
  's5': {'t': '우리 집 시비아트', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '어떤 오플라테크로 시비아트를 지을지 고르거나, 아이와 함께 끝까지 보세요', 'done': '우리 집 시비아트를 지었어요',
         'ways': [{'id': 'choose', 't': '어떤 오플라테크로 시비아트를 지을지 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'place': {
   'items': ITEMS, 'order': '온 동그라미 → 반쪽 둘 → 사분의 일 넷 → 실 꿰기, 그리고 끝으로 매달기',
   'intro': '아래에서 하나를 골라 놓아 보세요. 만들기 안내의 차례는 온 동그라미, 반쪽 둘, 사분의 일 넷, 실 꿰기, 그리고 매달기예요.',
   'climax': '오플라테크로 지은 하얀 세상이 포드와지니치카 아래 매달렸어요.<span class="la">świat · 세상</span>',
   'home': None,
   'wrongOrder': '만들기 안내의 차례는 이래요: {order}',
   'orderDone': '안내 차례대로 시비아트를 지어 매달았어요',
   'daylight': False,
   'svg': stage_svg()},
  'choose': {
   'q': '우리라면 어떤 오플라테크로 시비아트를 지을까요?',
   'opts': [{'t': '하얀 오플라테크', 'r': '저녁상에서 나누고 남은 오플라테크로 시비아티를 짓기도 했대요.'},
            {'t': '물들인 오플라테크', 'r': '시비아티는 분홍·파랑·노랑·초록으로 물들인 오플라테크로도 자주 지었어요.'}]},
 },
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 지어 보기</button></div>
  <div class="pl-home" hidden><p></p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'img': ['swiaty'], 'p': [
    '<b>빌리이키</b> 시비아티는 성탄 전날(비길리아)에 만들어서 ‘빌리이키’라고도 불렀어요.',
    '<b>지구 모양</b> 키엘체 지방 농촌 박물관은 시비아티가 흔히 지구 모양이었다고 해요. 이 박물관은 그 모양이 세상을 다스리는 아기 예수를 나타냈다고 설명하고, 시비아티는 폴란드 땅에서만 볼 수 있는 장식이라고 소개해요.',
    '<b>말총과 아마실</b> 키엘체 지방에서는 시비아티를 말총이나 아마실로 천장 판자에 매달았어요. 시비아티가 모양을 얼마나 오래 지키는지 보고 집안의 앞날을 점치기도 했대요.',
    '<b>싱싱하면 좋은 해</b> 브로츠와프 민족지 박물관의 연구자는 포드와지니치카가 오래 싱싱하면 좋은 한 해가 온다고 여겼다고 해요. 시간이 지나며 그 자리를 성탄 나무가 차지했어요.',
    '<b>요람이 달린 세상</b> 1924년 기록처럼 시비아트 아래 작은 요람을 매달기도 했어요. 크라쿠프 민족지 박물관은 2024년에도 오플라테크로 요람을 짓는 모임을 열었어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>언제 지었나</b> 폴란드 민족지 단체는 시비아티를 성탄 전날 지었다고 해요. 1924년 크라쿠프 지방 기록과 한 지역 박물관은 저녁 식사 뒤, 남은 오플라테크로 지었다고 적었어요. 장식을 대림절부터 미리 만들기 시작했다는 글도 있어요.',
    '<b>몇 장으로 지었나</b> 이 카드의 차례는 동그라미 세 장이에요. 실레지아 박물관의 연구자는 가장 쉬운 시비아티를 동그라미 두 장을 반으로 잘라 짚 대롱에 붙여 공처럼 지었다고 해요.',
    '<b>어디에 걸었나</b> 한 단체는 저녁상 위나 방 구석을, 실레지아 박물관은 두 창문 사이 성화를 건 ‘거룩한 구석’의 들보를 들어요. 키엘체 지방에서는 나무 꼭대기 대신 철사 고리에 푸른 가지를 엮어 걸기도 했대요.']},
  {'h': '직접 가 보기', 'img': ['gok', 'swiaty1'], 'checked': '2026년 11월 18일', 'p': [
    '크라쿠프 민족지 박물관은 시비아티를 전시하고, 성탄 무렵 오플라테크로 시비아티를 짓는 모임을 열어 왔어요(2025년 12월에도 열었어요). 포데그로제 문화관은 해마다 성탄 전에 포드와지니치카 겨루기를 열어 왔어요(2014년에 37번째).',
    '유리 공의 이야기는 앞면에 이어져요. 밀리치의 옛 성탄 장식 공장 자리에는 ‘봄브키 박물관’이, 노바 덴바에는 2012년에 문을 연 성탄 유리 공 박물관이 있어요. 여는 때는 미리 확인해 주세요.'],
   'links': [{'t': '크라쿠프 민족지 박물관', 'u': 'https://etnomuzeum.eu/', 'm': '폴란드어'},
             {'t': '포드카르파치에 관광: 노바 덴바 성탄 유리 공 박물관', 'u': NOWAD, 'm': '영어'}]},
 ],
 'src': [
  {'l': '프라초브니아 에트노그라피치나(폴란드 민족지 단체, 2025): 「포드와지니치카와 시비아티」 — 포드할레·베스키디, 거꾸로 매단 꼭대기, 저녁상 위나 구석, 꾸미개, 성탄 전날 지은 ‘빌리이키’, 동그라미 세 장 만들기 차례', 'u': PRAC},
  {'l': '프라초브니아 에트노그라피치나: 겨울 보충 자료 — 하얀 식탁보 아래 짚, 천장에 매단 시비아티, 대림절부터 미리 만든 장식', 'u': PRAC_ZIMA},
  {'l': '세베린 우지엘라, 『크라쿠프 사람들』(1924) 37쪽 — 크라쿠프 민족지 박물관 모임 안내(2024)에 실린 인용', 'u': UDZ},
  {'l': 'PAP·dzieje.pl(2014): 포데그로제 포드와지니치카 겨루기 — 라흐 사람들 집에서 1930년대까지 흔했음', 'u': LACHY},
  {'l': 'PAP·dzieje.pl(2014): 실레지아 박물관 — 거룩한 구석의 들보, 가장 쉬운 시비아티(동그라미 두 장)', 'u': SLASK},
  {'l': '라디오 키엘체(2023): 키엘체 지방 농촌 박물관 — 지구 모양, 폴란드에만 있는 장식, 말총·아마실, 점치기, 철사 고리', 'u': KIELCE},
  {'l': '라디오 크라쿠프(2025): 브로츠와프 민족지 박물관 연구자 — 싱싱하면 좋은 해, 성탄 나무가 자리를 이음', 'u': WROC},
  {'l': '라디오 크라쿠프: 흐샤누프 박물관 — 비길리아 뒤 남은 오플라테크로 시비아티, 물이나 침으로 붙임', 'u': CHRZ},
  {'l': '내셔널 지오그래픽 폴란드: 「오플라테크의 힘」 — 남은 오플라테크로 지은 시비아티는 포드와즈니크의 으뜸 장식', 'u': NATGEO},
  {'l': '비짓 말로폴스카: 크라쿠프 민족지 박물관의 성탄 — 가문비나무·소나무·전나무 꼭대기', 'u': MALOP},
  {'l': '라디오 크라쿠프: 크라쿠프 민족지 박물관 2025년 12월 시비아티 만들기 모임', 'u': MEK25},
  {'l': 'wroclaw.pl: 밀리치의 옛 성탄 장식 공장 자리의 봄브키 박물관', 'u': MILICZ},
  {'l': '포드카르파치에 관광: 노바 덴바 성탄 유리 공 박물관(2012년 문을 엶)', 'u': NOWAD},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 55%', 's0': 1.25, 's1': 1.05, 'kicker': '1930년대까지 · 폴란드 남쪽 산골', 'title': '천장에 매단 세상',
   'lines': [{'t': '손으로 그린 폴란드의 유리 공.'}, {'t': '유리 공이 시골집에 오기 전, 산골집 천장에는 무엇이 걸렸을까요?'}],
   'kid': [{'t': '반짝반짝 폴란드 유리 공이야.'}, {'t': '유리 공이 오기 전엔 무엇을 달았을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '거꾸로 매단 나무'},
  {'type': 'img', 'ch': 1, 'img': 'tetmajer', 'fit': 'cover', 'p0': '55% 12%', 'p1': '45% 40%', 's0': 1.5, 's1': 1.15, 'cap': '테트마예르, 「포드와지니치카」(1900)',
   'lines': [{'t': '포드할레와 베스키디 산골집에서는'},
             {'t': '전나무 꼭대기를 천장 들보에 거꾸로 매달았어요.'},
             {'t': '사과와 호두, 짚으로 엮은 별을 달았어요.'}],
   'kid': [{'t': '나무 꼭대기를 거꾸로 매달았대!'}, {'t': '나무 아래에 누가 모여 있어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '웨하스로 지은 세상'},
  {'type': 'mod', 'mod': 'place', 'ch': 2,
   'lines': [{'t': '성탄 전날 저녁, 오플라테크 세 장으로 ‘세상’을 지어요.'},
             {'t': '한 장은 그대로,', 'act': 'whole'},
             {'t': '한 장은 반으로 잘라 붙이고,', 'act': 'halves'},
             {'t': '한 장은 넷으로 잘라 사이사이에 끼워요.', 'act': 'quarters'},
             {'t': '실을 꿰어,', 'act': 'thread'},
             {'t': '포드와지니치카 아래에 매달아요.', 'act': 'hang', 'wait': 1500},
             {'t': '‘시비아트’는 폴란드 말로 ‘세상’이라는 뜻이에요.', 'act': 'day', 'wait': 2500},
             {'t': '유리 공이 오기 전에도, 산골집 천장에는 둥근 ‘세상’이 걸려 있었어요.'}],
   'kid': [{'t': '웨하스 세 장을 준비해.'},
           {'t': '하나는 그대로!', 'act': 'whole'}, {'t': '하나는 반으로!', 'act': 'halves'}, {'t': '하나는 넷으로!', 'act': 'quarters'},
           {'t': '모두 몇 조각이지?', 'ask': True},
           {'t': '실을 꿰어서,', 'act': 'thread'}, {'t': '나무 아래에 매달아!', 'act': 'hang', 'wait': 1500}, {'t': '동그란 세상 완성!', 'act': 'day', 'wait': 2000}]},
  {'type': 'imagine', 'ch': 3,
   'lines': [{'t': '창밖은 캄캄하고, 방 안은 따뜻해요.'}, {'t': '전나무에서 송진 냄새가 나요.'}, {'t': '입김을 불면, 하얀 웨하스가 살며시 휘어요.'}],
   'kid': [{'t': '눈을 감아 봐. 나무 냄새가 나.'}, {'t': '후~ 입김을 불어 웨하스를 붙이자.'}, {'t': '하얀 세상이 동그랗게!'}]},
  {'type': 'reward', 'ch': 3},
 ],
}
