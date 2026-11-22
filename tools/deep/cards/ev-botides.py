# -*- coding: utf-8 -*-
"""깊은 카드: 코르푸섬 항아리 던지기(ev-botides) · 중심 방식 = 만드는 차례(+옛 소리)
기준서 2판 · 틀 deep3-5 · 키트 3판(보탬 2) · 2026-11-22 20번 묶음 창(창 20)이 만듦 · 초벌(본부 소식 18)
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 2026년 4월 11일 성토요일 오전 11시, 코르푸 구시가지. 대성당에서 대주교가
     “하나님, 일어나 땅을 심판하소서”를 노래하고 도시의 모든 종이 울리는 순간, 빨간 천을 드리운 발코니에서
     물을 채운 흙 항아리가 길로 떨어져 깨지는 순간(‘첫 부활’).
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 항아리 하나가 준비되어 깨지기까지의 차례 — 빨간 천(위키백과 ‘Botides’),
     빨간 리본·물(그리스 관광청 · 그릭 시티 타임스), 종소리와 시편 구절(코르푸 시 관광 안내), 던지기(15분쯤),
     조각 줍기(행운 · 위키백과 · 더 월드). 단추를 누를 때마다 그 차례대로 한 단계씩.
카드 크기: 큰 카드(장면 5) — 코르푸 시 안내, 2024~2026년 보도, 2025·2026년 사진, 1912년 행렬 사진(퍼블릭 도메인),
  2024·2025년 영상의 소리(CC BY 4.0)가 넉넉해요.
단계 그림: 이 카드 파일의 stage_svg()가 그려요(발코니와 항아리는 이 안내서가 그린 그림).
그림 원본(src)은 deep_src/ev-botides/ (저장소 밖). 이 묶음은 ‘그림 받기 부탁’으로 사용자 컴퓨터에서 받음."""
import math, random
S = 'ev-botides/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

VC = 'https://visit.corfu.gr/?p=4339'                                       # 코르푸 시 관광 안내: 2023 부활절 일정
WB = 'https://en.wikipedia.org/wiki/Botides'
WE = 'https://en.wikipedia.org/wiki/Easter_in_Corfu'
VG = 'https://visitgreece.gr/events/festival/easter-on-corfu-island'
GCT = 'https://greekcitytimes.com/2024/05/04/easter-in-corfu-a-unique-tradition-of-smashing-pots'
TW = 'https://theworld.org/stories/2018-04-07/greek-island-celebrates-easter-throwing-pots-water-out-windows'
OW = 'https://orthodoxwiki.org/Holy_Saturday'
PT = 'https://en.protothema.gr/2026/04/11/from-the-flying-priest-of-chios-to-the-gloria-of-zakynthos-the-first-resurrection-marked-by-deafening-noise-video/'
C_CARD = 'https://commons.wikimedia.org/wiki/File:Easter_Botides_Pentofanaro_Sq._Holy_Saturday_Corfu_2026-04-11_(1).jpg'
C_FLY = 'https://commons.wikimedia.org/wiki/File:Easter_Botides_Pentofanaro_Sq._Holy_Saturday_Corfu_2026-04-11_(2).jpg'
C_HOUSES = 'https://commons.wikimedia.org/wiki/File:Corfu_town_houses.jpg'
C_SHARDS = 'https://commons.wikimedia.org/wiki/File:Broken_vases_on_Holy_Saturday_in_Corfu.jpg'
C_LIT = 'https://commons.wikimedia.org/wiki/File:%CE%97_%CE%9B%CE%B9%CF%84%CE%B1%CE%BD%CE%B5%CE%AF%CE%B1_%CF%84%CE%BF%CF%85_%CE%91%CE%B3%CE%AF%CE%BF%CF%85.JPG'
C_CRASH = 'https://commons.wikimedia.org/wiki/File:Pot_Smashing_(Botides)_Pentofanaro_2024.webm'
C_MARCH = 'https://commons.wikimedia.org/wiki/File:Pedofanaro_(Mi_fovasthe_grekoi)_Kapodistrias_Holy_Saturday_2025.webm'


# ── 단계 그림: 코르푸 구시가지의 발코니와 흙 항아리 하나(이 안내서가 그림) ─────────────────────
JUG = ('M192 146 C 172 150 166 166 168 178 C 170 192 182 200 190 200 L210 200 C 218 200 230 192 232 178 '
       'C 234 166 228 150 208 146 Z')
INNER = ('M194 152 C 179 156 175 168 176 178 C 178 189 187 194 192 194 L208 194 C 213 194 222 189 224 178 '
         'C 225 168 221 156 206 152 Z')

def _jug(dx=0, dy=0, rot=0, op=1):
    t = f' transform="translate({dx} {dy}) rotate({rot} 200 172)"' if (dx or dy or rot) else ''
    return (f'<g{t} opacity="{op}"><path d="M190 140 C 175 138 168 152 173 164" fill="none" stroke="#9b3522" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M210 140 C 225 138 232 152 227 164" fill="none" stroke="#9b3522" stroke-width="5" stroke-linecap="round"/>'
            f'<rect x="192" y="134" width="16" height="16" fill="#c0462f" stroke="#8e2f1f" stroke-width="1.2"/>'
            f'<rect x="187" y="130" width="26" height="6" rx="2" fill="#c9533a" stroke="#8e2f1f" stroke-width="1.2"/>'
            f'<path d="{JUG}" fill="#c0462f" stroke="#8e2f1f" stroke-width="1.4"/>'
            f'<ellipse cx="184" cy="170" rx="5" ry="12" fill="#fff" opacity=".16"/></g>')

def stage_svg(uid='bt'):
    R = random.Random(1574)
    cob = ''.join(f'<path d="M{x:.0f} {y:.0f} q8 -5 16 0 q-8 5 -16 0Z"/>' for y in range(366, 460, 13) for x in [R.uniform(-8, 6) + k * 22 + (11 if (y // 13) % 2 else 0) for k in range(19)])
    shutters = lambda x, y, w, h: (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#3a2d26"/>'
                                   f'<rect x="{x - w / 2 - 2:.0f}" y="{y}" width="{w / 2:.0f}" height="{h}" fill="#4f7a5a" stroke="#355440" stroke-width="1"/>'
                                   f'<rect x="{x + w + 2}" y="{y}" width="{w / 2:.0f}" height="{h}" fill="#4f7a5a" stroke="#355440" stroke-width="1"/>'
                                   + ''.join(f'<line x1="{x - w / 2:.0f}" y1="{yy}" x2="{x - 2}" y2="{yy}" stroke="#355440" stroke-width=".8"/><line x1="{x + w + 4}" y1="{yy}" x2="{x + w + w / 2 + 2:.0f}" y2="{yy}" stroke="#355440" stroke-width=".8"/>' for yy in range(y + 6, y + h, 7)))
    bars = ''.join(f'<line x1="{x}" y1="206" x2="{x}" y2="244" />' for x in range(112, 292, 12))
    # 빨간 천: 발코니 앞에 드리워요(1단계)
    cloth = ('<path d="M104 204 L296 204 L296 250 C 286 262 274 246 262 258 C 250 268 238 250 226 262 C 214 272 200 252 188 264 '
             'C 176 272 164 252 152 262 C 140 270 128 250 116 260 C 110 264 106 258 104 254 Z" fill="#c3272b" stroke="#8e1a1d" stroke-width="1.2"/>'
             + ''.join(f'<path d="M{x} 208 C {x + 3} 228 {x - 2} 240 {x + 1} 256" fill="none" stroke="#8e1a1d" stroke-width="1" opacity=".55"/>' for x in range(124, 290, 22))
             + '<path d="M104 204 L296 204 L296 210 L104 210Z" fill="#e2c25a"/>')
    # 빨간 리본(2단계)
    ribbons = ('<g fill="#ff3a3f" stroke="#fff4e8" stroke-width="1.1" stroke-linejoin="round">'
               '<ellipse cx="161" cy="139" rx="7" ry="3.6" transform="rotate(-28 161 139)"/><ellipse cx="161" cy="149" rx="7" ry="3.6" transform="rotate(28 161 149)"/><circle cx="168" cy="144" r="3"/>'
               '<ellipse cx="239" cy="139" rx="7" ry="3.6" transform="rotate(28 239 139)"/><ellipse cx="239" cy="149" rx="7" ry="3.6" transform="rotate(-28 239 149)"/><circle cx="232" cy="144" r="3"/></g>'
               '<g fill="none" stroke-linecap="round"><path d="M166 147 C 158 160 166 174 156 190" stroke="#fff4e8" stroke-width="5"/><path d="M166 147 C 158 160 166 174 156 190" stroke="#ff3a3f" stroke-width="3"/>'
               '<path d="M234 147 C 242 160 234 174 244 190" stroke="#fff4e8" stroke-width="5"/><path d="M234 147 C 242 160 234 174 244 190" stroke="#ff3a3f" stroke-width="3"/></g>')
    # 4단계: 종소리(멀리 보이는 종탑)
    waves = ''
    for r in (12, 20, 28):
        for a0, a1 in ((145, 215), (-35, 35)):
            p0 = (336 + r * math.cos(math.radians(a0)), 34 + r * math.sin(math.radians(a0)))
            p1 = (336 + r * math.cos(math.radians(a1)), 34 + r * math.sin(math.radians(a1)))
            waves += f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{r} {r} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}"/>'
    bell = ('<path d="M329 39 C 329 31 332 26 336 26 C 340 26 343 31 343 39 Z" fill="#e7b443" stroke="#8a6414" stroke-width="1"/><circle cx="336" cy="40.5" r="1.8" fill="#8a6414"/>')
    # 5단계: 떨어져 깨짐 / 6단계: 행운의 조각
    shards = ''
    pieces = [(150, 416, 14, -20), (176, 430, 10, 30), (214, 432, 12, 75), (238, 414, 16, -50), (196, 410, 9, 10),
              (128, 432, 8, 60), (262, 430, 9, -15), (226, 446, 11, 40), (168, 446, 7, -70), (288, 420, 7, 20)]
    for x, y, s, a in pieces:
        shards += f'<path d="M{x - s} {y} L{x - s * .2:.1f} {y - s * .7:.1f} L{x + s} {y - s * .2:.1f} L{x + s * .4:.1f} {y + s * .5:.1f}Z" transform="rotate({a} {x} {y})"/>'
    splash = ''.join(f'<path d="M200 424 L{200 + 70 * math.cos(math.radians(a)):.0f} {424 - 52 * abs(math.sin(math.radians(a))):.0f}" />' for a in range(200, 341, 14))
    drops = ''.join(f'<circle cx="{200 + R.uniform(-95, 95):.0f}" cy="{R.uniform(372, 420):.0f}" r="{R.uniform(1.6, 3.4):.1f}"/>' for _ in range(22))
    return f'''<svg viewBox="0 0 400 460" xmlns="http://www.w3.org/2000/svg"><defs>
<clipPath id="{uid}In"><path d="{INNER}"/><rect x="195" y="134" width="10" height="20"/></clipPath>
<clipPath id="{uid}Half"><rect x="200" y="120" width="60" height="90"/></clipPath>
<radialGradient id="{uid}Gl"><stop offset="0" stop-color="#ffe7a8" stop-opacity=".95"/><stop offset="1" stop-color="#ffcf6a" stop-opacity="0"/></radialGradient></defs>
<rect width="400" height="74" fill="#cfe3f2"/>
<g fill="#e9dcc6" stroke="#b9a68a" stroke-width="1"><rect x="322" y="6" width="28" height="70"/><path d="M318 8 L336 -6 L354 8Z" fill="#c06a4a"/></g>
<rect x="328" y="24" width="16" height="20" rx="8" fill="#5a4a3a"/>
<rect y="70" width="400" height="290" fill="#edd2a4"/><rect y="70" width="400" height="9" fill="#dcbf8f"/>
<g stroke="#d8bb8c" stroke-width="1" opacity=".7">{''.join(f'<line x1="0" y1="{y}" x2="400" y2="{y}"/>' for y in range(112, 360, 34))}</g>
{shutters(48, 96, 40, 58)}{shutters(312, 96, 40, 58)}
<rect x="160" y="112" width="80" height="132" fill="#3a2d26"/><rect x="128" y="112" width="30" height="132" fill="#4f7a5a" stroke="#355440"/><rect x="242" y="112" width="30" height="132" fill="#4f7a5a" stroke="#355440"/>
<g stroke="#355440" stroke-width=".8">{''.join(f'<line x1="131" y1="{y}" x2="155" y2="{y}"/><line x1="245" y1="{y}" x2="269" y2="{y}"/>' for y in range(118, 240, 7))}</g>
{shutters(48, 282, 40, 56)}{shutters(312, 282, 40, 56)}
<rect x="100" y="244" width="200" height="12" fill="#d9c2a0" stroke="#b49a78"/>
<g fill="#cdb48e" stroke="#b49a78">{''.join(f'<path d="M{x - 9} 256 L{x + 9} 256 L{x + 4} 272 L{x - 4} 272Z"/>' for x in (122, 200, 278))}</g>
<g stroke="#4b4a46" stroke-width="2">{bars}</g><rect x="104" y="200" width="192" height="6" fill="#4b4a46"/>
<rect y="356" width="400" height="104" fill="#a89c8c"/><g fill="#bdb2a2" stroke="#8f8474" stroke-width=".8">{cob}</g>
<g data-s="1">{cloth}</g>
<g data-off="5">{_jug()}
<g data-s="3"><g clip-path="url(#{uid}Half)"><g clip-path="url(#{uid}In)"><rect x="160" y="128" width="80" height="80" fill="#6b2418"/>
<rect class="dye" data-s="3" x="160" y="160" width="80" height="48" fill="#5aa7d6"/><rect class="dye" data-s="3" x="160" y="158" width="80" height="4" fill="#bfe2f5"/></g></g>
<path d="M200 140 V198" stroke="#f3e3c8" stroke-width="1" stroke-dasharray="2 3"/></g>
<g data-s="2">{ribbons}</g></g>
<g data-s="4"><g>{bell}</g><g fill="none" stroke="#c98a14" stroke-width="1.6">{waves}</g>
<text x="18" y="44" fill="#5a4a3a" style="font:700 15px var(--sans,sans-serif)">오전 11시</text></g>
<g data-s="5" data-off="6"><g stroke="#c0462f" stroke-width="2" stroke-linecap="round" opacity=".5"><line x1="196" y1="214" x2="196" y2="270"/><line x1="214" y1="220" x2="214" y2="262"/></g>{_jug(6, 120, 24, .55)}</g>
<g data-s="5" data-off="6"><g stroke="#5aa7d6" stroke-width="3" stroke-linecap="round" opacity=".85">{splash}</g><g fill="#5aa7d6" opacity=".85">{drops}</g></g>
<g data-s="5"><g fill="#c0462f" stroke="#7a2416" stroke-width="1">{shards}</g></g>
<g data-s="6"><circle cx="238" cy="414" r="30" fill="url(#{uid}Gl)"/><path d="M222 414 L234.8 402.8 L254 410.8 L244.4 422Z" transform="rotate(-50 238 414)" fill="#d9573a" stroke="#7a2416" stroke-width="1.4"/>
<g fill="#ffd36a">{''.join(f'<path d="M{x} {y - 6} L{x + 1.6} {y - 1.6} L{x + 6} {y} L{x + 1.6} {y + 1.6} L{x} {y + 6} L{x - 1.6} {y + 1.6} L{x - 6} {y} L{x - 1.6} {y - 1.6}Z"/>' for x, y in ((266, 396), (214, 394), (270, 432)))}</g>
<text x="238" y="380" text-anchor="middle" fill="#7a2416" style="font:700 14px var(--sans,sans-serif);paint-order:stroke;stroke:#fff6e6;stroke-width:4px">행운의 조각</text></g>
</svg>'''

STEPS = [
 {'do': '발코니에 빨간 천 드리우기', 't': '빨간 천',
  'p': '그날 아침, 구시가지의 창과 발코니에는 빨간 천이 드리워요. 빨강은 코르푸를 나타내는 색이에요.'},
 {'do': '항아리 손잡이에 빨간 리본 묶기', 't': '보티스',
  'p': '던질 흙 항아리를 ‘보티스’, 여럿이면 ‘보티데스’라고 불러요. 입이 좁고 양옆에 손잡이가 둘 달렸어요. 손잡이에 빨간 리본을 묶어요.'},
 {'do': '항아리에 물 가득 채우기', 't': '물',
  'p': '항아리에 물을 가득 채워요. 떨어질 때 더 큰 소리가 나게 하려는 거예요.'},
 {'do': '11시 종소리 기다리기', 't': '첫 부활',
  'p': '오전 11시, 대성당에서 대주교가 “하나님, 일어나 땅을 심판하소서”를 노래하면 도시의 모든 종이 기쁘게 울려요. 이 아침을 ‘첫 부활’이라고 불러요.'},
 {'do': '발코니에서 던지기', 't': '쨍그랑!',
  'p': '종소리를 신호로 발코니와 창에서 항아리를 길로 던져요. 깨지는 소리가 천둥 같고, 물보라와 흙 조각이 튀어요. 15분쯤 이어져요.'},
 {'do': '깨진 조각 하나 줍기', 't': '행운의 조각',
  'p': '사람들은 깨진 조각을 주워 가요. 행운을 가져다준다고 여겨서예요. 그리고 악단들이 기쁜 행진곡을 연주하며 거리로 나서요.'},
]

CARD = {
 'id': 'ev-botides', 'mode': '만드는 차례 · 옛 소리',
 'pagetitle': '코르푸섬 항아리 던지기',
 'brandsub': '깊은 카드 · 만드는 차례',
 'where': '<b>2026년 4월 11일 · 성토요일 오전 11시</b><span>그리스 코르푸섬 구시가지</span>',
 'lead': '그리스 코르푸섬의 성토요일 오전 11시, 도시의 모든 종이 울리는 순간이에요. 빨간 천을 드리운 발코니마다 물을 채운 흙 항아리가 길로 떨어져 쨍그랑 깨져요. 항아리 하나를 준비해 던지기까지, 그날 아침의 차례대로 해 보세요.',
 'leadKid': '부활절 전 토요일 아침, 그리스의 한 섬에서는 종이 울리면 창밖으로 물 항아리를 던져서 쨍그랑 깨뜨린대! 우리도 항아리 하나를 준비해 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 6분',
 'draft': '검수 전 시안이에요(기준서 2판 · 초벌). 장면에는 코르푸 시 관광 안내, 그리스 관광청, 2024~2026년 보도에 있는 것만 옮겼고, 풍습이 어디서 왔는지는 여러 설이 있어 설이라고 밝혔어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 단계 그림은 이 안내서가 그렸어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 # 화면 색: 코르푸의 빨강(빨간 천·리본)
 'theme': """:root{--accent:#a3262a;--accent-ink:#fff8f5;--soft:rgba(163,38,42,.08);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#f08a80;--accent-ink:#1a0c0b;--soft:rgba(240,138,128,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#f08a80;--accent-ink:#1a0c0b;--soft:rgba(240,138,128,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '보티스', 'y': '2026', 'sub': '코르푸 · 첫 부활'},
 'doneNote': '어디선가 종이 한꺼번에 울리면, 코르푸의 발코니에서 떨어지던 빨간 항아리를 떠올려 보세요.',
 'images': {
  'card': {'src': S + 'Easter_Botides_Pentofanaro_Sq._Holy_Saturday_Corfu_2026-04-11_1.jpg',
           'cap': '펜도파나로 광장 쪽 발코니에서 떨어지는 보티스, 2026년 4월 11일 오전 11시 2분',
           'cr': '사진: Gkaridis0 · CC BY 4.0 · 위키미디어 공용', 'u': C_CARD,
           'alt': '파란 하늘 아래 연노랑·살구색 옛 건물들의 발코니마다 빨간 천이 드리워 있고, 사람들이 난간에 기대 내려다본다. 가운데에서 글씨가 쓰인 빨간 항아리가 빨간 리본을 날리며 거꾸로 떨어지고 있다.'},
  'houses': {'src': S + 'Corfu_town_houses.jpg', 'cap': '빨간 천을 드리운 구시가지의 집들, 2007년 4월 7일 성토요일',
             'cr': '사진: Cplakidas · CC BY-SA 3.0 · 위키미디어 공용', 'u': C_HOUSES,
             'alt': '파란 하늘 아래 연노랑·잿빛 옛 건물들. 초록 덧창이 달린 창과 쇠 난간 발코니마다 빨간 천이 드리워 있고, 몇몇 발코니에 사람들이 나와 있다. 아래에는 흰 차양이 길게 이어진다.'},
  'litany': {'src': S + 'file.jpg', 'cap': '게오르기오스 사마르치스 「성 스피리돈의 행렬」, 1912년 · 코르푸 스피아나다 광장',
             'cr': '그림: 게오르기오스 사마르치스 · 퍼블릭 도메인 · 위키미디어 공용', 'u': C_LIT,
             'alt': '옛 그림엽서 같은 채색 그림. 나무와 옛 건물 앞 광장을 긴 행렬이 지나간다. 화려한 제의를 입은 성직자들과 금빛 머리의 긴 초를 든 사람들, 총을 멘 군인들이 함께 걷고, 건물 발코니마다 사람들이 내려다본다.'},
  'fly': {'src': S + 'Easter_Botides_Pentofanaro_Sq._Holy_Saturday_Corfu_2026-04-11_2.jpg', 'crop': (0.2, 0.1, 1.0, 0.74),
          'cap': '하늘을 나는 보티스, 2026년 4월 11일 오전 11시 8분',
          'cr': '사진: Gkaridis0 · CC BY 4.0 · 위키미디어 공용', 'u': C_FLY,
          'alt': '파란 하늘을 배경으로 금빛 띠를 두른 커다란 빨간 항아리가 공중에서 떨어지고 있다. 왼쪽 건물에는 그리스 국기가 걸려 있고, 발코니마다 빨간 천과 사람들이 보인다.'},
  'shards': {'src': S + 'Broken_vases_on_Holy_Saturday_in_Corfu.jpg', 'cap': '길에 쌓인 항아리 조각, 2007년 4월 7일',
             'cr': '사진: Cplakidas · CC BY-SA 3.0 · 위키미디어 공용', 'u': C_SHARDS,
             'alt': '돌길 위에 주황빛 흙 항아리 조각이 수북이 흩어져 있고, 그 사이에 선 사람들의 다리가 보인다. 몇 사람은 손에 조각을 들고 있다.'},
 },
 'sounds': [
  {'file': S + 'crash.mp3', 'cr': '항아리 깨지는 소리 · 2024년 성토요일 코르푸 펜도파나로 광장(아르카디온 호텔에서 찍은 영상) · 찍은 사람: Gkaridis0 · CC BY 4.0 · 위키미디어 공용 · 영상의 소리만 씀', 'u': C_CRASH},
  {'file': S + 'march.mp3', 'cr': '「그리스인들이여, 두려워 마라」(미 포바스테 그레키) · 2025년 성토요일 카포디스트리아스 악단 · 찍은 사람: Gkaridis0 · CC BY 4.0 · 위키미디어 공용 · 영상의 소리 앞부분만 씀', 'u': C_MARCH},
 ],
 'scenes': [
  {'id': 'red', 'label': '빨간 천의 아침', 'kind': 'photo', 'img': 'houses',
   'text': ['성토요일 아침, 그리스 코르푸섬의 구시가지. 창과 발코니마다 빨간 천이 드리워 있어요. 빨강은 코르푸를 나타내는 색이에요.',
            '발코니에도, 길에도 사람들이 가득해요. 모두 오전 11시를 기다려요.'],
   'kid': '창문마다 빨간 천이 걸려 있어! 사람들이 무언가를 기다리고 있어.',
   'kidq': '발코니에 나온 사람들은 무엇을 기다리고 있을까?'},
  {'id': 'litany', 'label': '성 스피리돈의 행렬', 'kind': 'photo', 'img': 'litany',
   'text': ['아침 9시, 성 스피리돈 성당에서 행렬이 나서요. 코르푸의 수호성인 성 스피리돈의 유해와, 그리스도의 무덤을 나타내는 에피타피오스(꽃으로 덮은 관)를 함께 모시고 구시가지를 돌아요.',
            '그리스의 다른 곳에서는 에피타피오스 행렬을 성금요일에 하지만, 코르푸는 토요일 아침에도 해요. 베네치아가 섬을 다스리던 때 안전을 이유로 성금요일의 정교회 행렬을 막았기 때문이에요. 1574년부터 이어 온 풍습이에요.'],
   'text2': ['성 스피리돈의 성토요일 행렬은 1550년, 섬이 굶주림에서 벗어난 일을 기려 시작되었어요. 코르푸의 큰 악단 셋이 행렬을 따르며 장례 행진곡을 연주해요.',
             '이보다 이른 새벽 6시에는 ‘이방인의 성모 성당’에서 신자들이 의자를 두드려 ‘지진’을 일으켜요. 그리스도께서 부활하실 때 일어난 지진을 다시 보여 주는 풍습이에요.'],
   'kid': '아침에는 꽃으로 덮은 관과 성인의 유해를 모시고 동네를 한 바퀴 돌아. 악단이 슬픈 음악을 연주해.',
   'kidq': '새벽에 의자를 쿵쿵 두드리면, 어떤 소리가 날까?'},
  {'id': 'jug', 'label': '항아리 하나', 'kind': 'mod', 'mod': 'steps',
   'text': ['던질 흙 항아리를 ‘보티스’, 여럿이면 ‘보티데스’라고 불러요. 크고 작은 것이 있고, 입이 좁고 양옆에 손잡이가 둘 달렸어요.',
            '한 집의 발코니에서 항아리 하나가 준비되어 길에 떨어지기까지, 그날 아침의 차례대로 해 보세요.'],
   'kid': '빨간 천을 걸고, 리본을 묶고, 물을 채우고… 종이 울리면 던져!',
   'kidq': '항아리에 왜 물을 가득 채울까?'},
  {'id': 'crash', 'label': '쨍그랑!', 'kind': 'duo', 'imgs': ['card', 'shards'],
   'text': ['오전 11시, 대성당의 노래를 신호로 도시의 모든 종이 기쁘게 울리고, 수많은 항아리가 발코니에서 떨어져요.',
            '깨지는 소리가 천둥 같아요. 가까이 선 구경꾼들은 물보라와 흙 조각을 맞기도 해요. 그래도 크게 다친 사람은 아직 없었다고 주최 측은 말해요.'],
   'snds': [{'t': '항아리 깨지는 소리', 'd': '2024년 성토요일, 펜도파나로 광장 · 영상의 소리', 'u': S + 'crash.mp3', 'ev': 'crash'},
            {'t': '「그리스인들이여, 두려워 마라」', 'd': '2025년 성토요일, 카포디스트리아스 악단 · 영상의 소리', 'u': S + 'march.mp3', 'ev': 'march'}],
   'text2': ['15분쯤 지나 소리가 잦아들면, 사람들은 깨진 조각을 주워 가요. 행운을 가져다준다고 여겨서예요. 그리고 악단들이 「그리스인들이여, 두려워 마라」 같은 기쁜 행진곡을 연주하며 거리로 나서요.',
             '왜 항아리를 깨뜨리게 되었는지는 여러 설이 있어요. 베네치아 사람들이 새해에 묵은 그릇을 깨뜨리던 풍습에서 왔다는 설, 봄을 맞던 옛 그리스의 풍습에서 왔다는 설, 나쁜 기운을 쫓는다는 설이 함께 전해져요.'],
   'kid': '종이 울리자 쨍그랑! 쨍그랑! 항아리가 한꺼번에 떨어져. 조각을 주우면 행운이 온대.',
   'kidq': '깨지는 소리를 들어 볼래? 무슨 소리 같아?'},
  {'id': 'verse', 'label': '“하나님, 일어나소서”', 'kind': 'quote',
   'text': ['항아리가 떨어지기 바로 전, 대성당에서 울려 퍼지는 노래예요. 그리스 정교회의 성토요일 아침 예배에서 사제는 이 구절을 노래하며 성당 안에 월계수 잎과 꽃잎을 뿌려요. 부서진 지옥의 문과 끊어진 사슬, 죽음을 이긴 기쁨을 나타내요.'],
   'quote': {'t': '하나님, 일어나 땅을 심판하소서. 모든 민족을 주님께서 물려받으실 것입니다.',
             'from': '시편 82편 8절 · 성토요일 아침 예배에서 부르는 구절 · 이 안내서가 우리말로 옮김', 'u': NKRV + 'PSA.82'},
   'text2': ['코르푸 사람들은 깨지는 항아리에서 질그릇을 부순다는 예언자의 말을 읽어요. 코르푸 시의 안내는 그 요란한 소리가 삶이 죽음을 이긴 것을 나타내는지도 모른다고 적어요.',
             '부활의 큰 잔치는 그날 자정이에요. 그 밤 스피아나다 광장 위쪽 음악당에서 “크리스토스 아네스티”를 노래하고, 북소리와 불꽃이 이어져요. 아침의 항아리 소리는 그 밤을 미리 여는 ‘첫 부활’이에요.'],
   'kid': '항아리가 떨어지기 바로 전에 “하나님, 일어나세요!” 하고 노래한대. 교회 안에서는 월계수 잎을 뿌려.',
   'kidq': '“일어나세요!” 하고 부르면, 누가 일어날까?'},
 ],
 'imagine': {'t': '봄 햇살 아래 좁은 골목, 빨간 천이 바람에 흔들려요. 발코니마다 사람들이 무거운 항아리를 난간 위로 들어 올리고 숨을 죽여요. 멀리서 노래가 들리다, 갑자기 온 도시의 종이 한꺼번에 울려요. 쨍그랑, 쨍그랑! 물보라가 햇빛에 반짝이고, 발밑으로 빨간 조각이 굴러와요.',
             'kid': '눈을 감아 봐. 햇살이 따뜻해. 빨간 천이 펄럭펄럭. 다들 항아리를 들고 기다려. 땡그랑땡그랑, 종이 울린다! 쨍그랑! 물이 튀어서 시원해!'},
 'lines': ['빨간 천, 빨간 리본, 물 한가득.', '하나님, 일어나소서.', '온 도시의 종과 쨍그랑 소리.', '자정보다 먼저 오는 첫 부활.'],
 'linesKid': ['빨간 천, 빨간 리본!', '땡그랑, 종이 울려!', '쨍그랑! 행운의 조각!'],
 'close': {'form': '기록 한 마디',
           'from': '성토요일 아침 대성당에서 대주교가 노래하는 시편 82편 8절 “하나님, 일어나 땅을 심판하소서” — 이 노래가 항아리를 던지는 신호예요(코르푸 시 관광 안내)',
           'ask': '부활의 큰 잔치는 자정인데, 코르푸 사람들은 아침 11시 ‘첫 부활’의 종소리에 벌써 항아리를 깨뜨려요. 내게도 다 오기 전에 미리 터뜨리고 싶은 기쁨이 있나요?',
           'askKid': '기쁜 소식을 들으면, 너는 어떤 소리를 내고 싶어?'},
 'goals': {
  's4': {'t': '항아리 하나', 'p': '빨간 천부터 행운의 조각까지, 여섯 단계를 끝까지 해 보면 카드에 금박이 입혀져요.',
         'how': '셋째 장면에서 단추를 눌러 여섯 단계를 끝까지 해 보세요', 'done': '항아리 하나를 준비해 던지고, 행운의 조각까지 주웠어요',
         'ways': [{'id': 'steps', 't': '빨간 천 → 리본 → 물 → 종소리 → 던지기 → 조각 줍기, 끝 단계까지 해 보기'}]},
  's5': {'t': '그날의 소리', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.', 'how': '넷째 장면에서 항아리 깨지는 소리를 듣거나, 아이와 함께 끝까지 보세요', 'done': '그날 아침의 소리를 들었어요',
         'ways': [{'id': 'crash', 't': '넷째 장면에서 항아리 깨지는 소리 듣기', 'hint': '넷째 장면 ‘쨍그랑!’에서 소리 단추를 눌러 보세요', 'okt': '항아리 깨지는 소리를 들었어요'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'steps': {
   'svg': stage_svg(),
   'alt': '코르푸 구시가지의 옛 건물 발코니. 초록 덧창, 쇠 난간 위에 흙 항아리 하나가 놓여 있고, 아래는 돌을 깐 길이다. 단계마다 빨간 천, 리본, 물, 종소리, 떨어져 깨진 조각이 하나씩 나타난다.',
   'cap': '이 안내서가 그린 단계 그림 · 코르푸 시 관광 안내, 그리스 관광청, 위키백과 ‘Botides’를 바탕으로(항아리 오른쪽 절반은 속을 보여 주려고 잘라 그렸어요)',
   'intro': '단추를 누를 때마다 그날 아침이 한 단계씩 지나가요.',
   'hint': '아래 단추를 눌러, 발코니에 빨간 천을 드리우는 것부터 시작해 보세요.',
   'steps': STEPS,
   'done': '쨍그랑! 항아리 하나가 깨지고, 행운의 조각이 남았어요. 이제 악단들이 거리로 나서요.',
 }},
 'deep': [
  {'h': '기록마다 다른 점', 'p': [
    '<b>항아리 속</b> 코르푸 시의 안내와 위키백과, 그리스 관광청은 항아리에 물을 채운다고 적어요. 한 영어 기사는 빨간 리본을 채운다고 적었는데, 다른 기록들은 리본을 손잡이에 묶는다고 적어요.',
    '<b>몇 시에</b> 대부분의 기록은 오전 11시라고 적지만, 한 기사는 낮 12시라고 적었어요. 코르푸 시의 안내는 11시에 대성당 예배가 시작되고, 그 노래를 신호로 종이 울린다고 적어요.',
    '<b>어디서 왔나</b> 베네치아의 새해 풍습, 옛 그리스의 봄맞이, 성경의 질그릇 말씀, 부활 때의 지진, 나쁜 기운 쫓기까지 여러 설이 있어요. 어느 하나로 정해져 있지 않아요.']},
  {'h': '함께 읽는 말씀', 'p': [
    '말씀은 뜻만 옮기고, 본문은 대한성서공회 개역개정으로 이어 드려요.',
    '<b>' + bl('PSA.82', '시편 82편 8절') + '</b> 하나님께 일어나 세상을 심판해 달라고 부르짖는 구절이에요. 성토요일 아침, 항아리가 떨어지기 바로 전에 대성당에서 이 구절을 노래해요.',
    '<b>' + bl('PSA.2', '시편 2편 9절') + '</b> 질그릇같이 부순다는 말씀이에요. 성경에는 질그릇을 깨뜨리는 비유가 여러 번 나와요.',
    '<b>' + bl('MAT.28', '마태복음 28장 2절') + '</b> 큰 지진이 나고 주의 천사가 무덤의 돌을 굴려 냈다는 말씀이에요. 새벽 6시의 ‘지진’ 풍습은 이 장면을 다시 보여 줘요.']},
  {'h': '직접 가 보기', 'checked': '2026년 11월 22일', 'p': [
    '코르푸 구시가지의 리스톤 거리와 스피아나다 광장 둘레에서 볼 수 있어요. 2027년 정교회 성토요일은 5월 1일이에요.',
    '아침 9시 성 스피리돈 행렬 뒤, 오전 11시에 시작해 15분쯤 이어져요. 사람이 아주 많으니 일찍 자리를 잡고, 항아리가 떨어지는 곳에서는 조금 떨어져 서세요.'],
   'links': [{'t': '코르푸 시 관광 안내: 코르푸 시내의 부활절 일정', 'u': VC, 'm': '영어'},
             {'t': '그리스 관광청(Visit Greece): 코르푸섬의 부활절', 'u': VG, 'm': '영어'}]},
 ],
 'src': [
  {'l': '코르푸 시 관광 안내: 2023 부활절 일정 — 새벽 6시 지진 재현(이방인의 성모 성당), 9시 성 스피리돈 행렬과 에피타피오스, 11시 대성당 예배, “하나님, 일어나 땅을 심판하소서”에 종이 울리고 항아리를 던짐, 첫 부활, 예언자의 말, 삶이 죽음을 이김, 악단의 장례 행진곡', 'u': VC},
  {'l': '위키백과(영어): Botides — 11시, 15분쯤, 입이 좁고 손잡이 둘, 빨간 리본, 물, 빨간 천, 리스톤, 여러 설, 행운의 조각, 「오이 그레키」 행진곡', 'u': WB},
  {'l': '위키백과(영어): Easter in Corfu — 1550년 굶주림, 1574년부터, 베네치아의 성금요일 행렬 금지, 의자를 두드리는 지진, 자정 음악당과 불꽃', 'u': WE},
  {'l': '그리스 관광청(Visit Greece): 코르푸섬의 부활절 — 2026년 4월 11일 오전 11시, 모든 성당의 종, 첫 부활, 손잡이 둘 달린 흙 항아리, 빨간 리본, 물', 'u': VG},
  {'l': '그릭 시티 타임스(2024.5.4): 빨강은 코르푸의 색, 떨어질 때 소리가 나게 물을 채움, 「그리스인들이여, 두려워 마라」, 베네치아와 옛 그리스의 설', 'u': GCT},
  {'l': '더 월드(2018.4.7): 천둥 같은 소리, 물보라와 조각, 크게 다친 사람 없음, 조각을 행운의 부적으로', 'u': TW},
  {'l': '정교회 위키: 성토요일 — “하나님, 일어나소서”를 노래하며 월계수 잎과 꽃잎을 뿌림, 부서진 지옥의 문과 사슬, 죽음을 이긴 기쁨', 'u': OW},
  {'l': '프로토테마(2026.4.11): ‘첫 부활’은 부활 밤의 서곡, 코르푸 이방인의 성모 성당', 'u': PT},
  {'l': '위키미디어 공용: 2024년 항아리 깨지는 영상, 2025년 「미 포바스테 그레키」 영상(Gkaridis0 · CC BY 4.0)', 'u': C_CRASH},
  {'l': '대한성서공회 개역개정: 시편 82편 · 시편 2편 · 마태복음 28장', 'u': NKRV + 'PSA.82'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 45%', 'p1': '55% 50%', 's0': 1.2, 's1': 1.05, 'kicker': '2026년 4월 11일 오전 11시 · 그리스 코르푸섬', 'title': '항아리 던지기',
   'lines': [{'t': '부활절 전 토요일 오전 11시, 도시의 모든 종이 울려요.'}, {'t': '그 순간, 발코니에서 항아리가 떨어져요.'}],
   'kid': [{'t': '종이 울리면… 쨍그랑! 항아리가 떨어져!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '빨간 천의 아침'},
  {'type': 'img', 'ch': 1, 'img': 'houses', 'fit': 'cover', 'p0': '30% 50%', 'p1': '70% 45%', 's0': 1.18, 's1': 1.06, 'cap': '빨간 천을 드리운 구시가지, 2007년',
   'lines': [{'t': '구시가지의 창과 발코니마다 빨간 천이 드리워요.'}, {'t': '빨강은 코르푸를 나타내는 색이에요.'}],
   'kid': [{'t': '창문마다 빨간 천!'}, {'t': '사람들이 무엇을 기다리고 있을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '성 스피리돈의 행렬'},
  {'type': 'img', 'ch': 2, 'img': 'litany', 'fit': 'cover', 'p0': '30% 60%', 'p1': '65% 50%', 's0': 1.2, 's1': 1.05, 'cap': '사마르치스 「성 스피리돈의 행렬」, 1912년',
   'lines': [{'t': '아침 9시, 수호성인 성 스피리돈의 유해와 에피타피오스가 구시가지를 돌아요.'}, {'t': '베네치아 때부터, 코르푸는 이 행렬을 토요일 아침에 해 왔어요.'}],
   'kid': [{'t': '꽃으로 덮은 관을 모시고 동네를 한 바퀴!'}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '항아리 하나'},
  {'type': 'mod', 'mod': 'steps', 'ch': 3,
   'lines': [{'t': '발코니에 빨간 천을 드리우고,', 'act': 'step:1'}, {'t': '항아리 손잡이에 빨간 리본을 묶고,', 'act': 'step:2'},
             {'t': '물을 가득 채워요.', 'act': 'step:3', 'wait': 2200},
             {'t': '오전 11시, “하나님, 일어나 땅을 심판하소서.” 종이 울려요.', 'act': 'step:4', 'wait': 2200},
             {'t': '쨍그랑!', 'act': 'step:5', 'wait': 2000},
             {'t': '깨진 조각 하나는 행운의 조각이에요.', 'act': 'step:6', 'wait': 1800}],
   'kid': [{'t': '빨간 천!', 'act': 'step:1'}, {'t': '빨간 리본!', 'act': 'step:2'}, {'t': '물을 가득!', 'act': 'step:3', 'wait': 2200},
           {'t': '땡그랑땡그랑, 종이 울린다!', 'act': 'step:4', 'wait': 2200}, {'t': '쨍그랑!', 'act': 'step:5', 'wait': 2000},
           {'t': '조각을 주우면 행운이 온대.', 'act': 'step:6', 'wait': 1800}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '쨍그랑!'},
  {'type': 'img', 'ch': 4, 'img': 'fly', 'fit': 'cover', 'p0': '55% 40%', 'p1': '50% 52%', 's0': 1.25, 's1': 1.05, 'cap': '하늘을 나는 보티스 · 2026년 4월 11일',
   'lines': [{'t': '종소리를 신호로, 발코니마다 항아리가 떨어져요.'}, {'t': '깨지는 소리가 천둥 같아요. 물보라와 흙 조각이 튀어요.'}],
   'kid': [{'t': '항아리가 하늘을 날아!'}, {'t': '쨍그랑! 쨍그랑! 물이 튀어!'}]},
  {'type': 'img', 'ch': 4, 'img': 'shards', 'fit': 'cover', 'p0': '50% 60%', 'p1': '50% 40%', 's0': 1.2, 's1': 1.05, 'cap': '길에 쌓인 항아리 조각 · 2007년',
   'lines': [{'t': '소리가 잦아들면, 사람들은 조각을 주워 가요. 행운을 가져다준다고 여겨서예요.'}, {'t': '그리고 악단들이 기쁜 행진곡을 연주하며 거리로 나서요.'}],
   'kid': [{'t': '조각을 주우면 행운이 온대.'}, {'t': '너라면 어떤 조각을 고를래?', 'ask': True}]},
  {'type': 'imagine', 'ch': 4,
   'lines': [{'t': '빨간 천이 바람에 흔들려요. 다들 숨을 죽여요.'}, {'t': '갑자기 온 도시의 종이 한꺼번에.'}, {'t': '물보라가 햇빛에 반짝이고, 발밑으로 빨간 조각이 굴러와요.'}],
   'kid': [{'t': '눈을 감아 봐. 빨간 천이 펄럭펄럭.'}, {'t': '땡그랑땡그랑, 종이 울린다!'}, {'t': '쨍그랑! 물이 튀어서 시원해!'}]},
  {'type': 'chapter', 'ch': 5, 'no': 5, 't': '“하나님, 일어나소서”'},
  {'type': 'quote', 'ch': 5, 'big': '하나님, 일어나 땅을 심판하소서.',
   'lines': [{'t': '항아리가 떨어지기 바로 전, 대성당에서 울리는 노래예요.'}, {'t': '사제는 월계수 잎과 꽃잎을 뿌리며 이 구절을 노래해요.'},
             {'t': '모든 민족을 주님께서 물려받으실 것입니다.', 'q': True, 'from': '시편 82편 8절'}],
   'kid': [{'t': '“하나님, 일어나세요!”'}, {'t': '교회 안에서는 월계수 잎을 뿌려.'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
