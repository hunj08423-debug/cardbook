# -*- coding: utf-8 -*-
"""깊은 카드: 성탄 피라미드(craft-pyramid) · 중심 방식 = 놓아 보기(+두 그림 나란히, 고르기)
기준서 1판 · 틀 deep3-2 · 키트 2판 · 2026-11-18 5번 묶음 창이 만듦.
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 성탄 전날 저녁, 마지막 근무를 일찍 마친 광부가 집에서 ‘촛대 상자’를 풀고
     피라미드(‘돌아가는 촛대’)에 불을 붙이는 때(지버 1959).
  2. 손으로 하는 한 가지: 남아 있는 가장 오래된 피라미드(렌츠의 피라미드, 안나베르크 에르츠산맥 박물관)의 네 층을
     박물관 기록 차례대로 놓고(광부 행렬 → 아기 예수 탄생·동방박사·목자 → 낙타와 동물 → 천사) 등잔불을 켜면 날개가 돌기.
카드 크기: 큰 카드(장면 4개).
무대 그림은 아래 stage_svg()가 그려요(이 안내서가 그림, 박물관 기록의 층 차례를 따름).
불을 켜면 날개와 층이 몇 바퀴 돌다가 멈춰요(늘 도는 움직임 없음, 움직임 줄이기 설정이면 돌지 않음).
그림 원본(src)은 deep_src/craft-pyramid/ (저장소 밖)."""
import random

S = 'craft-pyramid/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
SIEBER = 'https://www.bergbaumuseum.de/fileadmin/forschung/zeitschriften/der-anschnitt/1959/1959-06/anschnitt-6-1959-siegfried-sieber-bergmaennische-weihnachtsbraeuche-im-erzgebirge.pdf'
EVDE = 'https://www.evangelisch.de/inhalte/97447/11-12-2009'
XMUS = 'https://weihnachtsmuseum.de/en/pyramide'
LENZ = 'https://sachsen.museum-digital.de/object/206'


# ---------- 무대 그림(SVG): 광부의 집, 밤. 렌츠의 피라미드 네 층(박물관 기록 차례) ----------
CX = 400
TIERS = [  # (층, 판 가운데 y, 판 반지름 x, 그림 높이)
    ('parade', 356, 136, 40),
    ('nativity', 290, 112, 34),
    ('animals', 228, 88, 28),
    ('angels', 170, 64, 24),
]

def _miner(x, y, k):
    flag = (k % 4 == 1)
    s = (f'<rect x="{x-3.4:.1f}" y="{y-10}" width="2.4" height="10" fill="#141212"/><rect x="{x+1:.1f}" y="{y-10}" width="2.4" height="10" fill="#141212"/>'
         f'<path d="M{x-6:.1f} {y-10} L{x-5:.1f} {y-24} Q{x:.1f} {y-27} {x+5:.1f} {y-24} L{x+6:.1f} {y-10}Z" fill="#2b2a35"/>'
         f'<rect x="{x-6:.1f}" y="{y-14}" width="12" height="2.2" fill="#7a5532"/>'
         f'<circle cx="{x:.1f}" cy="{y-28}" r="3.6" fill="#e2c39a"/>'
         f'<rect x="{x-3.8:.1f}" y="{y-39}" width="7.6" height="8.4" rx="1" fill="#121010"/>'
         f'<path d="M{x+2:.1f} {y-39} q2 -5 5.5 -6" stroke="#ece5d6" stroke-width="1.5" fill="none" stroke-linecap="round"/>')
    if flag:
        s += (f'<line x1="{x+6.5:.1f}" y1="{y-6}" x2="{x+6.5:.1f}" y2="{y-46}" stroke="#7a5532" stroke-width="1.4"/>'
              f'<rect x="{x+6.5:.1f}" y="{y-46}" width="13" height="8" fill="#2f6b4a"/><rect x="{x+6.5:.1f}" y="{y-42}" width="13" height="2.6" fill="#ece5d6"/>')
    else:
        s += (f'<line x1="{x+5:.1f}" y1="{y-20}" x2="{x+7:.1f}" y2="{y-15}" stroke="#2b2a35" stroke-width="2"/>'
              f'<circle cx="{x+7.4:.1f}" cy="{y-14}" r="1.8" fill="#ffcf73"/>')
    return s

def _nativity(x, y, k):
    t = k % 6
    if t == 0:   # 마리아(무릎 꿇음)
        return (f'<path d="M{x-7:.1f} {y} Q{x-8:.1f} {y-14} {x-2:.1f} {y-20} Q{x+4:.1f} {y-16} {x+6:.1f} {y}Z" fill="#3c5f9e"/>'
                f'<circle cx="{x-1:.1f}" cy="{y-23}" r="3.4" fill="#e2c39a"/><path d="M{x-5:.1f} {y-22} Q{x-1:.1f} {y-30} {x+3:.1f} {y-22}" fill="#3c5f9e"/>')
    if t == 1:   # 구유와 아기
        return (f'<path d="M{x-8:.1f} {y-9} L{x+8:.1f} {y-9} L{x+6:.1f} {y-3} L{x-6:.1f} {y-3}Z" fill="#8a6238"/>'
                f'<line x1="{x-6:.1f}" y1="{y-3}" x2="{x-8:.1f}" y2="{y}" stroke="#8a6238" stroke-width="1.6"/><line x1="{x+6:.1f}" y1="{y-3}" x2="{x+8:.1f}" y2="{y}" stroke="#8a6238" stroke-width="1.6"/>'
                f'<ellipse cx="{x:.1f}" cy="{y-11}" rx="5.4" ry="2.8" fill="#f3ead6"/><circle cx="{x+4:.1f}" cy="{y-12}" r="1.9" fill="#e9c9a0"/>'
                f'<circle cx="{x:.1f}" cy="{y-11}" r="9" fill="#ffd98a" opacity=".18"/>')
    if t == 2:   # 요셉(지팡이)
        return (f'<path d="M{x-6:.1f} {y} L{x-4:.1f} {y-24} Q{x:.1f} {y-27} {x+4:.1f} {y-24} L{x+6:.1f} {y}Z" fill="#7a4a24"/>'
                f'<circle cx="{x:.1f}" cy="{y-28}" r="3.5" fill="#e2c39a"/><line x1="{x+8:.1f}" y1="{y}" x2="{x+8:.1f}" y2="{y-30}" stroke="#a07a4a" stroke-width="1.5"/>')
    if t in (3, 4):   # 동방박사(왕관과 선물)
        col = '#9b2f2f' if t == 3 else '#3d6b45'
        return (f'<path d="M{x-6:.1f} {y} L{x-4:.1f} {y-23} Q{x:.1f} {y-26} {x+4:.1f} {y-23} L{x+6:.1f} {y}Z" fill="{col}"/>'
                f'<circle cx="{x:.1f}" cy="{y-27}" r="3.4" fill="#e2c39a"/>'
                f'<path d="M{x-3.6:.1f} {y-30} l1.2 -4 1.2 2.6 1.2 -3.2 1.2 3.2 1.2 -2.6 1.2 4z" fill="#e3b53e"/>'
                f'<rect x="{x+3:.1f}" y="{y-16}" width="5" height="4.4" fill="#e3b53e"/>')
    # 목자(두건과 굽은 지팡이)
    return (f'<path d="M{x-6:.1f} {y} L{x-4:.1f} {y-22} Q{x:.1f} {y-25} {x+4:.1f} {y-22} L{x+6:.1f} {y}Z" fill="#7d6a4c"/>'
            f'<circle cx="{x:.1f}" cy="{y-25}" r="3.3" fill="#e2c39a"/><path d="M{x-4:.1f} {y-24} Q{x:.1f} {y-32} {x+4:.1f} {y-24}" fill="#5a4a34"/>'
            f'<path d="M{x-8:.1f} {y} L{x-8:.1f} {y-26} q0 -4 3.5 -4" stroke="#a07a4a" stroke-width="1.4" fill="none"/>')

def _animal(x, y, k):
    if k % 2 == 0:   # 낙타
        return (f'<path d="M{x-11:.1f} {y-12} Q{x-9:.1f} {y-17} {x-5:.1f} {y-15} Q{x-2:.1f} {y-23} {x+2:.1f} {y-15} Q{x+6:.1f} {y-16} {x+8:.1f} {y-12} Z" fill="#c69a5c"/>'
                f'<path d="M{x+7:.1f} {y-13} Q{x+11:.1f} {y-17} {x+11:.1f} {y-24} l3.2 0.6 -0.6 2.6 -2.2 0.2 Q{x+12:.1f} {y-16} {x+9:.1f} {y-12}Z" fill="#c69a5c"/>'
                + ''.join(f'<line x1="{x+dx:.1f}" y1="{y-12}" x2="{x+dx:.1f}" y2="{y}" stroke="#a87c44" stroke-width="1.6"/>' for dx in (-9, -5, 2, 6)))
    return (f'<ellipse cx="{x:.1f}" cy="{y-7}" rx="7" ry="4.6" fill="#ece5d6"/>'
            f'<circle cx="{x-3:.1f}" cy="{y-9}" r="3" fill="#ece5d6"/><circle cx="{x+3:.1f}" cy="{y-9}" r="3" fill="#ece5d6"/>'
            f'<ellipse cx="{x+8:.1f}" cy="{y-8}" rx="2.6" ry="2" fill="#3a332c"/>'
            + ''.join(f'<line x1="{x+dx:.1f}" y1="{y-4}" x2="{x+dx:.1f}" y2="{y}" stroke="#3a332c" stroke-width="1.3"/>' for dx in (-4, -1, 3, 5)))

def _angel(x, y, k):
    return (f'<ellipse cx="{x-5:.1f}" cy="{y-15}" rx="5" ry="7.5" fill="#d9b45a" transform="rotate(-24 {x-5:.1f} {y-15})"/>'
            f'<ellipse cx="{x+5:.1f}" cy="{y-15}" rx="5" ry="7.5" fill="#d9b45a" transform="rotate(24 {x+5:.1f} {y-15})"/>'
            f'<path d="M{x-5.5:.1f} {y} L{x-3:.1f} {y-17} Q{x:.1f} {y-20} {x+3:.1f} {y-17} L{x+5.5:.1f} {y}Z" fill="#f2ead8"/>'
            f'<circle cx="{x:.1f}" cy="{y-20}" r="3.2" fill="#e8caa2"/><circle cx="{x:.1f}" cy="{y-21}" r="5" fill="none" stroke="#e3b53e" stroke-width="1"/>')

DRAW = {'parade': (_miner, 30, 8), 'nativity': (_nativity, 26, 6), 'animals': (_animal, 30, 4), 'angels': (_angel, 28, 4)}

def stage_svg():
    R = random.Random(1810)
    stars = ''.join(f'<circle cx="{R.uniform(126, 224):.0f}" cy="{R.uniform(78, 160):.0f}" r="{R.choice([.6, .8, 1.0, 1.3]):.1f}" fill="#fff" opacity="{R.uniform(.4, .95):.2f}"/>' for _ in range(22))
    boards = ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="392" stroke="#fff" stroke-opacity=".035" stroke-width="2"/>' for x in range(36, 800, 52))
    defs, rows, anims = [], [], []
    for n, (tid, cy, rx, hh) in enumerate(TIERS, 1):
        fn, gap, kinds = DRAW[tid]
        per = gap * kinds
        x0, x1 = CX - rx + 6, CX + rx - 6
        defs.append(f'<clipPath id="__U__c{n}"><rect x="{x0}" y="{cy - hh - 8}" width="{x1 - x0}" height="{hh + 9}"/></clipPath>')
        figs, k, x = '', 0, x0 - gap
        while x < x1 + per + gap:
            figs += fn(x, cy - 1, k); k += 1; x += gap
        shade = (f'<rect x="{x0}" y="{cy - hh - 8}" width="{rx * .55:.0f}" height="{hh + 9}" fill="url(#__U__shL)"/>'
                 f'<rect x="{x1 - rx * .55:.0f}" y="{cy - hh - 8}" width="{rx * .55:.0f}" height="{hh + 9}" fill="url(#__U__shR)"/>')
        rows.append(f'<g class="obj" data-o="{tid}"><g clip-path="url(#__U__c{n})"><g class="pyr-run pyr-r{n}">{figs}</g></g>{shade}</g>')
        anims.append(f'.pl.lit .pyr-r{n}{{animation:pyrR{n} 8s linear 3}}@keyframes pyrR{n}{{to{{transform:translateX(-{per}px)}}}}')
    plates = ''.join(f'<ellipse cx="{CX}" cy="{cy}" rx="{rx}" ry="{6 if n < 3 else 5}" fill="#4a3220" stroke="#9a7344" stroke-width="1.4"/>'
                     for n, (tid, cy, rx, hh) in enumerate(TIERS, 1))
    lamps = [(CX - rx + 9, cy - 2) for _, cy, rx, _ in TIERS] + [(CX + rx - 9, cy - 2) for _, cy, rx, _ in TIERS] + [(248, 372), (552, 372)]
    lt = ''.join(f'<g class="lt" style="transition-delay:{k * .07:.2f}s"><circle cx="{x}" cy="{y - 7}" r="17" fill="url(#__U__lg)"/>'
                 f'<ellipse cx="{x}" cy="{y}" rx="4.2" ry="1.7" fill="#9a7344"/><circle class="c" cx="{x}" cy="{y - 5}" r="2.4" fill="#ffd27a"/></g>'
                 for k, (x, y) in enumerate(lamps))
    style = ('.pl .pyr-run{will-change:transform}' + ''.join(anims) +
             '.pl.lit .pyr-wing{animation:pyrW 4s linear 6}@keyframes pyrW{to{stroke-dashoffset:-100}}'
             '@media (prefers-reduced-motion:reduce){.pl.lit .pyr-run,.pl.lit .pyr-wing{animation:none}}')
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="밤, 광부의 집 창가. 네 층으로 된 나무 피라미드에 층마다 인형이 하나씩 놓이고, 불을 켜면 맨 위 날개와 층이 천천히 돈다."><style>{style}</style><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c0f19"/><stop offset="1" stop-color="#1d1610"/></linearGradient>
<linearGradient id="__U__win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#081128"/><stop offset="1" stop-color="#1c2c4c"/></linearGradient>
<linearGradient id="__U__sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a3a1c" stop-opacity=".0"/><stop offset="1" stop-color="#f0b979" stop-opacity=".35"/></linearGradient>
<radialGradient id="__U__warm" cx=".5" cy=".55" r=".55"><stop offset="0" stop-color="#ffcf86"/><stop offset=".5" stop-color="#d9893c" stop-opacity=".55"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__lg"><stop offset="0" stop-color="#ffe2a0" stop-opacity=".95"/><stop offset=".4" stop-color="#ffb35c" stop-opacity=".4"/><stop offset="1" stop-color="#ff9a3c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".55" r=".75"><stop offset="0" stop-color="#fff0c8" stop-opacity=".55"/><stop offset=".55" stop-color="#ffc77a" stop-opacity=".25"/><stop offset="1" stop-color="#ff9f4a" stop-opacity="0"/></radialGradient>
<linearGradient id="__U__shL" x1="0" x2="1"><stop offset="0" stop-color="#0c0a08" stop-opacity=".85"/><stop offset="1" stop-color="#0c0a08" stop-opacity="0"/></linearGradient>
<linearGradient id="__U__shR" x1="1" x2="0"><stop offset="0" stop-color="#0c0a08" stop-opacity=".85"/><stop offset="1" stop-color="#0c0a08" stop-opacity="0"/></linearGradient>
{''.join(defs)}</defs>
<rect width="800" height="450" fill="url(#__U__wall)"/>{boards}
<rect class="sky2" width="800" height="392" fill="url(#__U__sky2)"/>
<g><rect x="114" y="64" width="118" height="168" rx="3" fill="#2a1d12"/><rect x="122" y="72" width="102" height="152" fill="url(#__U__win)"/>{stars}
<path d="M122 206 C 146 192 170 200 190 190 C 206 184 216 192 224 188 L224 224 L122 224Z" fill="#cdd6e3" opacity=".55"/>
<rect x="171" y="72" width="4" height="152" fill="#2a1d12"/><rect x="122" y="146" width="102" height="4" fill="#2a1d12"/><rect x="108" y="230" width="130" height="7" fill="#3a2818"/></g>
<ellipse class="glow" cx="{CX}" cy="250" rx="270" ry="215" fill="url(#__U__warm)" opacity=".14"/>
<rect x="0" y="392" width="800" height="58" fill="#24180f"/><line x1="0" y1="392.5" x2="800" y2="392.5" stroke="#7a5532" stroke-width="1.5"/>
<path d="M236 374 L564 374 L576 392 L224 392Z" fill="#3a2614" stroke="#8a6238" stroke-width="1.4"/>
<line x1="{CX}" y1="392" x2="{CX}" y2="94" stroke="#7b5634" stroke-width="4" stroke-linecap="round"/>
{plates}
{''.join(rows)}
<path d="M252 374 L364 122 M548 374 L436 122" stroke="#6b4a2b" stroke-width="5" stroke-linecap="round" fill="none"/>
<rect x="350" y="112" width="100" height="11" rx="2" fill="#4a3220" stroke="#8a6238" stroke-width="1.2"/>
<ellipse cx="{CX}" cy="94" rx="152" ry="20" fill="none" stroke="#6f7a7c" stroke-width="1.2" opacity=".7"/>
<ellipse class="pyr-wing" cx="{CX}" cy="94" rx="148" ry="18" fill="none" stroke="#b9c2c4" stroke-width="13" pathLength="100" stroke-dasharray="6.4 3.6"/>
<circle cx="{CX}" cy="94" r="7" fill="#8a6238" stroke="#c49a62" stroke-width="1"/>
{lt}
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''


ITEMS = [
 {'id': 'parade', 't': '광부 행렬', 'la': 'Bergparade', 'say': '맨 아래층에 광부들의 행렬을 세웠어요. 박물관 기록이 맨 먼저 적은 층이에요.'},
 {'id': 'nativity', 't': '아기 예수 탄생', 'la': 'Christi Geburt', 'say': '둘째 층에는 아기 예수의 탄생과 동방박사, 목자들이 서요.'},
 {'id': 'animals', 't': '낙타와 동물', 'la': 'Tiere · Kamele', 'say': '셋째 층에는 낙타를 비롯한 여러 동물이 서요.'},
 {'id': 'angels', 't': '천사', 'la': 'Engel', 'say': '맨 위층에는 천사들이 서요.'},
 {'id': 'lights', 't': '등잔불', 'la': 'Rüböllampen', 'say': '끝으로 작은 기름 등잔에 불을 붙여요. 이 피라미드에는 지금도 유채 기름 등잔이 달려 있어요.'},
]

CARD = {
 'id': 'craft-pyramid',
 'mode': '놓아 보기 · 두 그림',
 'pagetitle': '돌아가는 촛대',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>1800년 무렵부터</b><span>독일 작센 · 에르츠산맥 광산 마을</span>',
 'lead': '독일 에르츠산맥의 광산 마을. 성탄 전날 일찍 일을 마친 광부는 집에 와서 ‘촛대 상자’를 풀었어요. 지금 남은 가장 오래된 피라미드의 층을 차례로 놓고, 불을 켜서 돌려 보세요.',
 'leadKid': '독일 산골 광산 마을에서는 성탄이 오면 불로 도는 탑을 세웠대. 우리도 한 층씩 꾸미고 불을 켜 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 1판). 성탄 전날 광부들의 하루는 지크프리트 지버의 연구(1959)를, 피라미드의 층은 에르츠산맥 박물관 기록을 따랐어요. 상상은 ‘눈 감고 상상해 보기’에서만 해요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#2f5d50;--accent-ink:#f6fbf8;--soft:rgba(47,93,80,.09);--stamp:#a8392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#8fc1b0;--accent-ink:#0f1a16;--soft:rgba(143,193,176,.10);--stamp:#e46e5c}}
:root[data-theme="dark"]{--accent:#8fc1b0;--accent-ink:#0f1a16;--soft:rgba(143,193,176,.10);--stamp:#e46e5c}
body.dim{--bg:#0a0d12;--paper:#131820;--ink:#f1ebdf;--muted:#b5ab98;--faint:#81796b;--line:#262c36;--soft:rgba(232,168,104,.10);--accent:#e8a868;--accent-ink:#1f1206}""",
 'stamp': {'t': '피라미드', 'y': '1810', 'sub': '안나베르크 · 에르츠산맥'},
 'doneNote': '성탄 장터에서 피라미드를 만나면, 날개 아래 불빛을 찾아보세요.',
 'images': {
  'p1830': {'src': S + 'Christmas_pyramid_from_about_1830.jpg', 'cap': '1830년 무렵 쇤하이데에서 만든 피라미드(쇤하이데 향토 박물관)', 'cr': '사진: Klaaschwotzer · CC0 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Christmas_pyramid_from_about_1830.jpg',
            'alt': '유리 진열장 안의 세 층짜리 연노랑 나무 피라미드. 맨 위에 넓은 날개가 펼쳐져 있고, 맨 위층에는 나무 아래 사슴과 사람, 가운데층과 아래층에는 검은 모자를 쓴 인형들이 빽빽하게 서 있다. 층 옆으로 작은 촛대가 나와 있다.'},
  'gopel': {'src': S + 'Pferdeg_pel_Johanngeorgenstadt_Au_enansicht_im_Winter_2H1A3968WI.jpg', 'crop': (0.0, 0.3, 0.6, 0.92),
            'cap': '요한게오르겐슈타트의 말 권양기 집(기술 문화재)', 'cr': '사진: Kora27 · CC BY-SA 4.0 · 위키미디어 공용 · 일부 잘라 씀',
            'u': 'https://commons.wikimedia.org/wiki/File:Pferdeg%C3%B6pel_Johanngeorgenstadt_(Au%C3%9Fenansicht)_im_Winter_2H1A3968WI.jpg',
            'alt': '눈 덮인 마을 길가에 원뿔 모양 지붕을 얹은 둥근 건물이 서 있고, 옆에 길쭉한 집이 붙어 있다. 뒤로 눈 쌓인 나무들과 파란 하늘.'},
  'krauss': {'src': S + 'Krau_-Pyramide_Schwarzenberg_im_Dunklen_2.jpg', 'cap': '슈바르첸베르크 광장의 크라우스 피라미드, 밤', 'cr': '사진: Aagnverglaser · CC BY 4.0 · 위키미디어 공용',
             'u': 'https://commons.wikimedia.org/wiki/File:Krau%C3%9F-Pyramide_Schwarzenberg_im_Dunklen_(2).jpg',
             'alt': '깜깜한 밤에 불이 켜진 키 큰 피라미드. 층층이 놓인 인형들이 불빛을 받고, 맨 위에는 별 모양 구멍이 뚫린 커다란 둥근 날개가 펼쳐져 있다.'},
  'wing': {'src': S + 'Krau_-Pyramide_Schwarzenberg_oberer_Teil.jpg', 'cap': '같은 피라미드의 날개를 아래에서 본 모습', 'cr': '사진: Aagnverglaser · CC BY-SA 4.0 · 위키미디어 공용',
           'u': 'https://commons.wikimedia.org/wiki/File:Krau%C3%9F-Pyramide_Schwarzenberg,_oberer_Teil.jpg',
           'alt': '흐린 하늘을 배경으로, 별 모양 구멍이 촘촘한 날개판들이 둥글게 펼쳐진 큰 날개. 그 아래로 촛대 모양 전등과 인형이 놓인 층이 보인다.'},
 },
 'scenes': [
  {'id': 'gopel', 'label': '말이 돌리던 광산의 탑', 'kind': 'duo', 'imgs': ['gopel', 'p1830'],
   'caps': ['요한게오르겐슈타트의 말 권양기 집', '1830년 무렵 쇤하이데의 피라미드'],
   'text': ['독일과 체코 사이의 에르츠산맥은 ‘광석의 산’이라는 뜻이에요. 16세기부터 이렇게 불렸어요. 그때 이 산에는 광석을 캐는 광산이 곳곳에 있었어요.',
            '광산에는 ‘말 권양기’가 있었어요. 권양기는 무거운 것을 감아 올리는 기계예요. 말이 긴 팔을 끌며 원을 그리고 돌면 가운데 굵은 축이 돌아가요. 축에 감기는 줄이 깊은 갱도에서 광석 통을 끌어 올렸어요.',
            '프라이베르크 근처 힘멜스퓌르스트 광산에도 말 권양기가 있었어요. 프라이베르크 광산 대학에 그 모형이 남아 있어요.'],
   'quote': {'t': '‘돌아가는 촛대’라고도 불렀는데, 옛 광산의 권양기를 본뜬 것이에요.',
             'from': '지크프리트 지버, 「에르츠산맥 광부들의 성탄 풍습」(1959) · 독일어를 이 안내서가 옮김', 'u': SIEBER},
   'text2': ['에르츠산맥 사람들은 이 탑을 사투리로 ‘페레메트’라고 불러요. 가운데 축에 층층이 판을 꿴 모양을 보고 말 권양기를 떠올린 사람들이 있었을 거라고 해요.'],
   'kid': '광산에서는 말이 빙빙 돌면서 무거운 광석을 끌어 올렸대.',
   'kidq': '말이 빙빙 돌리는 기계랑 피라미드, 어디가 닮았어?'},
  {'id': 'eve', 'label': '성탄 전날의 ‘촛대 상자’', 'kind': 'quote',
   'text': ['에르츠산맥의 향토사가 지크프리트 지버는 옛 광산의 성탄 전날을 이렇게 적었어요.',
            '프라이베르크 근처 힘멜스퓌르스트 광산의 광부들은 12월 24일에도 여느 날처럼 새벽 네 시에 모였어요. 성탄 전 마지막으로 일하는 날이었어요.',
            '큰 새참 때까지만 일했어요. 작은 걸상에 둘러앉아 아침을 먹고, 이야기를 나누고 성탄 노래를 불렀어요. 발파 구멍이 모두 터지기를 기다렸다가, 여느 날보다 일찍 땅 위로 올라왔어요.'],
   'quote': {'t': '집에 오면 광부는 촛대 상자를 풀고 성탄을 준비했어요.',
             'from': '지크프리트 지버, 「에르츠산맥 광부들의 성탄 풍습」(1959) · 독일어를 이 안내서가 옮김', 'u': SIEBER},
   'text2': ['광부들은 곳곳에서 초를 든 광부와 천사를 나무로 깎았어요. 피라미드도 광부들이 만든 불빛 가운데 하나였어요.'],
   'choose': True,
   'kid': '성탄 전날엔 광부 아저씨들이 여느 날보다 일찍 집에 왔대.',
   'kidq': '일찍 집에 온 아빠가 상자를 열면, 무엇이 나올까?'},
  {'id': 'light', 'label': '가장 오래된 피라미드에 불 켜기', 'kind': 'mod', 'mod': 'place', 'night': True,
   'text': ['안나베르크부흐홀츠의 에르츠산맥 박물관에는 따뜻한 공기로 도는 성탄 피라미드 가운데 지금 남은 가장 오래된 것이 있어요. 예전 주인의 이름을 따서 ‘렌츠의 피라미드’라고 불러요.',
            '층이 넷이고, 맨 위에 커다란 날개가 열 장 달렸어요. 박물관 기록은 층마다 선 인형을 아래층부터 적어 두었어요. 그 차례대로 놓고, 끝으로 불을 켜 보세요.'],
   'text2': ['이 피라미드에는 지금도 유채 기름을 태우는 작은 등잔이 달려 있어요. 뒤에 나온 피라미드들은 등잔 대신 초로 돌렸어요.',
             '무대 그림은 박물관 기록의 차례를 따라 이 안내서가 그렸어요. 실제 피라미드의 모습과는 달라요.'],
   'kid': '피라미드를 한 층씩 꾸며 볼까? 맨 아래는 광부 아저씨들이야!',
   'kidq': '불을 켜면 어떻게 될까?'},
  {'id': 'square', 'label': '마을 광장의 큰 피라미드', 'kind': 'photo', 'img': 'krauss',
   'text': ['1930년대부터 에르츠산맥의 성탄 장터에 사람 키보다 훨씬 큰 피라미드가 몇 개씩 서기 시작했어요. 1950년대까지도 독일 전체에 열 개 남짓이었다고 해요. 오늘은 독일 곳곳의 성탄 장터에 큰 피라미드가 서요.',
            '사진은 슈바르첸베르크 광장의 크라우스 피라미드예요. 날개판에 별 모양 구멍이 촘촘히 뚫려 있어요.'],
   'text2': ['오늘 에르츠산맥의 성탄 철은 대림절 첫 주일 무렵 ‘피라미드 밀기’로 시작해요. 마을 사람들이 모여 큰 피라미드를 처음 돌리는 날이에요. 빠른 곳은 그 앞 금요일 저녁부터 돌려요. 이 고장 사투리로는 ‘페레메트 아쉼’이라고 해요.',
             '성탄 철은 2월 2일 성촉절에 끝나요. 성촉절은 아기 예수를 성전에 바친 날을 기억하는 축일이에요.'],
   'kid': '마을 광장에는 집보다 큰 피라미드가 서. 다 같이 모여서 처음 돌리는 날도 있대!',
   'kidq': '이렇게 큰 피라미드를 처음 돌리는 날, 너라면 무슨 말을 외칠래?'},
 ],
 'imagine': {'t': '창밖은 오후 네 시인데도 벌써 깜깜해요. 땅속에서 일찍 올라온 아빠가 나무 상자를 열자, 마른 나무 냄새가 퍼져요. 작은 등잔에 불을 붙이면 잠시 뒤 머리 위 날개가 삐걱 움직여요. 광부 인형들이 천천히 한 바퀴 돌아 다시 내 앞으로 와요.',
             'kid': '눈을 감아 봐. 창밖은 깜깜해. 아빠가 상자를 열어. 불을 붙이면… 날개가 삐걱! 인형들이 빙글빙글 돌아 다시 와.'},
 'lines': ['불 하나로 도는 탑.', '땅속의 권양기가 집 안의 촛대가 되었어요.', '따뜻한 공기는 보이지 않게 날개를 밀어요.', '일찍 올라온 광부의 성탄 전날.'],
 'linesKid': ['불을 켜면 빙글빙글!', '따뜻한 바람이 날개를 밀어.', '광부 아저씨가 일찍 집에 왔어.'],
 'goals': {
  's4': {'t': '기록 차례대로 불 켜기', 'p': '박물관 기록의 차례(아래층부터 광부 행렬, 아기 예수 탄생, 동물, 천사)대로 놓고 끝으로 불을 켜면 카드에 금박이 입혀져요.',
         'how': '기록 차례대로 층을 놓고 불을 켜 보세요', 'done': '기록 차례대로 피라미드를 돌렸어요',
         'ways': [{'id': 'plOrder', 't': '광부 행렬 → 아기 예수 탄생 → 동물 → 천사 → 불 켜기'}]},
  's5': {'t': '우리 집 촛대 상자', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '우리 집 ‘촛대 상자’에서 먼저 꺼낼 것을 고르거나, 아이와 함께 끝까지 보세요', 'done': '우리 집 촛대 상자를 열었어요',
         'ways': [{'id': 'choose', 't': '광부처럼, 성탄 전날 ‘촛대 상자’에서 먼저 꺼낼 것 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'place': {
   'items': ITEMS, 'order': '아래층부터 광부 행렬 → 아기 예수 탄생 → 동물 → 천사, 그리고 끝으로 불 켜기',
   'intro': '아래에서 하나를 골라 피라미드에 놓아 보세요. 박물관 기록은 아래층부터 광부 행렬, 아기 예수 탄생, 동물, 천사 차례예요.',
   'climax': '등잔이 데운 공기가 위로 올라가 날개를 밀어요. 날개와 같은 축에 꿰인 층들이 천천히 돌기 시작해요.<span class="la">Laaflechter · 돌아가는 촛대</span>',
   'home': None,
   'wrongOrder': '박물관 기록에 남은 차례는 이래요: {order}',
   'orderDone': '기록 차례대로 피라미드를 쌓고 불을 켰어요',
   'daylight': False,
   'svg': stage_svg()},
  'choose': {
   'q': '성탄 전날, 우리 집 ‘촛대 상자’를 연다면 무엇부터 꺼낼까요?',
   'opts': [{'t': '피라미드', 'r': '불을 켜면 도는 촛대예요. 광부들은 ‘돌아가는 촛대’라고도 불렀어요.'},
            {'t': '촛불 천사', 'r': '광부들은 초를 든 천사를 나무로 깎았어요.'},
            {'t': '촛불 광부', 'r': '광부들은 초를 든 광부 인형도 깎았어요. 자기 모습을 닮은 인형이에요.'}]},
 },
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 놓아 보기</button></div>
  <div class="pl-home" hidden><p></p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>빛 틀</b> 옛날 브란덴부르크와 작센의 교회에서는 대림절에 ‘빛 틀’을 세웠어요. 푸른 가지를 감은 막대 네 개를 꼭대기에서 묶고 초를 꽂은 모양이었어요.',
    '<b>첫 피라미드</b> 성탄 인형을 올린 피라미드는 1790년 무렵부터 나타났다고 해요. 독일 성탄 박물관은 피라미드가 18세기에 이미 교회의 성탄 장식이었다고 소개해요.',
    '<b>돌아가는 원리</b> 가운데 축에 층층이 둥근 판이 꿰여 있고, 맨 위에 날개가 달려 있어요. 축의 뾰족한 아래 끝은 받침의 오목한 자리에 서 있어요. 판 가장자리의 불이 데운 공기가 날개를 돌리면, 같은 축의 판들도 함께 돌아요.',
    '<b>초가 싸지자</b> 1830년 무렵 파라핀이 나와 초가 누구나 살 만큼 싸지면서, 피라미드가 독일 곳곳으로 퍼졌다고 해요. 파라핀은 석유에서 얻는 하얀 밀랍 같은 재료예요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>가장 오래된 피라미드의 나이</b> 독일 성탄 박물관은 렌츠의 피라미드를 1800년 무렵 것으로, 이 피라미드를 가진 안나베르크 박물관의 기록은 1810년 무렵으로 적었어요.',
    '<b>권양기를 본떴을까</b> 지버(1959)는 피라미드가 옛 광산의 권양기를 본뜬 것이라고 적었어요. 다른 글은 모양이 권양기를 떠올리게 했을 거라고만 말해요. 따뜻한 공기로 도는 장치까지 권양기에서 왔는지는 확실하지 않아요.',
    '<b>‘피라미드’라는 이름</b> 한 개신교 매체는 나폴레옹의 이집트 원정(1798~1801) 소식이 전해진 뒤 이 말이 이 고장 사투리 ‘페레메트’로 자리 잡았다고 소개해요.']},
  {'h': '직접 가 보기', 'img': ['wing'], 'checked': '2026년 11월 18일', 'p': [
    '렌츠의 피라미드는 안나베르크부흐홀츠의 에르츠산맥 박물관에 있어요. 박물관 마당에서 16세기 초의 옛 은광 ‘임 괴스너’로 내려갈 수 있어요. 여는 때는 미리 확인해 주세요.',
    '대림절 첫 주일 무렵 에르츠산맥 마을들이 ‘피라미드 밀기’를 해요. 마을마다 날이 조금씩 다르니 관광 협회 일정표를 보세요.'],
   'links': [{'t': '안나베르크부흐홀츠시: 에르츠산맥 박물관', 'u': 'https://www.annaberg-buchholz.de/de/kultur/erzgebirgsmuseum.php', 'm': '독일어'},
             {'t': '에르츠산맥 관광 협회: 성탄 철 안내', 'u': 'https://www.erzgebirge-tourismus.de/weihnachtszeit/', 'm': '독일어'}]},
 ],
 'src': [
  {'l': '지크프리트 지버, 「에르츠산맥 광부들의 성탄 풍습」, 『데어 안슈니트』 1959년 6호(독일 광산 박물관) — 12월 24일 힘멜스퓌르스트 광산, 촛대 상자, ‘돌아가는 촛대’와 권양기, 촛불 광부·천사', 'u': SIEBER},
  {'l': 'sachsen.museum-digital: 에르츠산맥 박물관 ‘렌츠의 피라미드’ — 1810년, 네 층과 날개 열 장, 층마다 인형(아래층부터)', 'u': LENZ},
  {'l': '독일 성탄 박물관(로텐부르크): 피라미드 — 18세기 교회 장식, 렌츠의 피라미드 1800년 무렵·유채 기름 등잔, 돌아가는 원리', 'u': XMUS},
  {'l': 'evangelisch.de(2009): 피라미드와 슈비보겐 — 교회의 빛 틀, 권양기를 떠올린 모양, 1790년 무렵, ‘페레메트’, 1830년 파라핀', 'u': EVDE},
  {'l': 'TU 베르크아카데미 프라이베르크 소장품: 힘멜스퓌르스트 광산의 말 권양기 모형 — 16~19세기 광산의 권양기, 말이 돌리던 축과 줄', 'u': 'https://sachsen.museum-digital.de/object/34397'},
  {'l': 'TU 켐니츠 대림절 달력(1997): 광부의 성탄 — 16세기부터 ‘에르츠산맥’이라는 이름, 촛불 천사와 광부 한 쌍', 'u': 'https://www.tu-chemnitz.de/advent/1997/5/bmweihnacht.html'},
  {'l': 'TU 켐니츠 대림절 달력(2003): 에르츠산맥 박물관과 옛 은광 — 박물관 마당의 은광 입구, 1510년 무렵의 광구 주인', 'u': 'https://www.tu-chemnitz.de/advent/2003/17/'},
  {'l': 'TU 켐니츠 대림절 달력(2004): 피라미드 밀기 — 대림절 첫 주일 앞 금요일 저녁부터, 사투리 ‘페레메트 아쉼’', 'u': 'https://www.tu-chemnitz.de/advent/2004/1/'},
  {'l': '에르츠산맥 관광 협회 보도 자료(2019) — 성탄 철은 피라미드 밀기로 시작해 성촉절에 끝남', 'u': 'https://tourismusverband-erzgebirge-ev.mynewsdesk.com/pressreleases/weihnachtsland-erzgebirge-feiert-welterbe-2946678'},
  {'l': 'The German Way: 독일 성탄 피라미드 — 1930년대부터 장터의 큰 피라미드, 1950년대에도 열 개 남짓', 'u': 'https://german-way.com/history-and-culture/holidays-and-celebrations/christmas/german-christmas-pyramid-weihnachtspyramide'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'p1830', 'fit': 'cover', 'p0': '50% 22%', 'p1': '50% 52%', 's0': 1.3, 's1': 1.06, 'kicker': '1800년 무렵부터 · 독일 에르츠산맥', 'title': '돌아가는 촛대',
   'lines': [{'t': '독일 동쪽, 광산 마을이 많은 에르츠산맥.'}, {'t': '성탄이 오면 집집마다 불로 도는 탑이 섰어요.'}],
   'kid': [{'t': '독일 산골 광산 마을이야.'}, {'t': '성탄이 되면 불로 도는 탑을 세웠대!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '광산의 권양기'},
  {'type': 'img', 'ch': 1, 'img': 'gopel', 'fit': 'cover', 'p0': '40% 55%', 'p1': '48% 50%', 's0': 1.22, 's1': 1.05, 'cap': '요한게오르겐슈타트에 다시 지은 말 권양기 집',
   'lines': [{'t': '광산에는 말이 가운데 축을 돌려 광석을 끌어 올리는 권양기가 있었어요.'},
             {'t': '옛 광산의 권양기를 본뜬, 돌아가는 촛대.', 'q': True, 'from': '지버(1959)에서'}],
   'kid': [{'t': '말이 빙빙 돌면 가운데 기둥이 돌아갔대.'}, {'t': '피라미드랑 어디가 닮았을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '성탄 전날'},
  {'type': 'img', 'ch': 2, 'img': 'p1830', 'fit': 'cover', 'p0': '50% 84%', 'p1': '50% 66%', 's0': 1.55, 's1': 1.3, 'cap': '1830년 무렵 피라미드의 광부 인형들',
   'lines': [{'t': '12월 24일, 광부들은 새벽 네 시에 모여 성탄 전 마지막 일을 했어요.'},
             {'t': '발파가 끝나자, 여느 날보다 일찍 땅 위로 올라왔어요.'},
             {'t': '집에 오면 광부는 촛대 상자를 풀고 성탄을 준비했어요.', 'q': True, 'from': '지버(1959)에서'}],
   'kid': [{'t': '성탄 전날엔 광부 아저씨들이 일찍 집에 왔대.'}, {'t': '상자를 열면 뭐가 나올까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '불 켜기'},
  {'type': 'mod', 'mod': 'place', 'ch': 3,
   'lines': [{'t': '가장 오래 남은 피라미드는 네 층이에요.'},
             {'t': '맨 아래 광부 행렬,', 'act': 'parade'}, {'t': '아기 예수 탄생과 동방박사, 목자들,', 'act': 'nativity'},
             {'t': '낙타와 동물들,', 'act': 'animals'}, {'t': '맨 위에는 천사들.', 'act': 'angels'},
             {'t': '작은 기름 등잔에 불을 붙이면,', 'act': 'lights', 'wait': 1500},
             {'t': '데워진 공기가 날개를 밀어, 탑이 돌기 시작해요.', 'act': 'day', 'wait': 3000}],
   'kid': [{'t': '한 층씩 꾸며 보자.'},
           {'t': '광부 아저씨들!', 'act': 'parade'}, {'t': '아기 예수!', 'act': 'nativity'}, {'t': '낙타랑 양!', 'act': 'animals'}, {'t': '천사!', 'act': 'angels'},
           {'t': '불을 켜면 어떻게 될까?', 'ask': True},
           {'t': '불을 붙여!', 'act': 'lights', 'wait': 1500}, {'t': '빙글빙글 돌아!', 'act': 'day', 'wait': 3000}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '마을 광장'},
  {'type': 'img', 'ch': 4, 'img': 'krauss', 'fit': 'cover', 'p0': '50% 22%', 'p1': '50% 62%', 's0': 1.25, 's1': 1.05, 'cap': '슈바르첸베르크의 크라우스 피라미드',
   'lines': [{'t': '1930년대부터는 장터에 사람 키보다 훨씬 큰 피라미드가 섰어요.'},
             {'t': '대림절 첫 주일 무렵, 마을 사람들이 모여 피라미드를 처음 돌려요.'}],
   'kid': [{'t': '광장엔 집보다 큰 피라미드가 있어!'}, {'t': '처음 돌리는 날, 너라면 뭐라고 외칠래?', 'ask': True}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '창밖은 벌써 깜깜해요.'}, {'t': '상자를 열자 마른 나무 냄새가 퍼져요.'}, {'t': '불을 붙이면, 머리 위 날개가 삐걱 움직여요.'}],
   'kid': [{'t': '눈을 감아 봐. 창밖은 깜깜해.'}, {'t': '불을 붙이면… 날개가 삐걱!'}, {'t': '인형들이 빙글빙글 돌아.'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
