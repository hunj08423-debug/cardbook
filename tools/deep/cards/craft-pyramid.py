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
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크(재벌 2026-11-22에 더함)
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'
SIEBER = 'https://www.bergbaumuseum.de/fileadmin/forschung/zeitschriften/der-anschnitt/1959/1959-06/anschnitt-6-1959-siegfried-sieber-bergmaennische-weihnachtsbraeuche-im-erzgebirge.pdf'
EVDE = 'https://www.evangelisch.de/inhalte/97447/11-12-2009'
XMUS = 'https://weihnachtsmuseum.de/en/pyramide'
LENZ = 'https://sachsen.museum-digital.de/object/206'
# 재벌(2026-11-22)에서 더한 근거
GOPELM = 'https://sachsen.museum-digital.de/object/34397'
TUC17 = 'https://www.tu-chemnitz.de/advent/1997/17/'
TUC05 = 'https://www.tu-chemnitz.de/advent/1997/5/bmweihnacht.html'
BRAUK = 'https://www.bergbaumuseum.de/fileadmin/forschung/zeitschriften/der-anschnitt/1999/1999-05-06/anschnitt-5-6-1999-heide-braukmueller-vom-bergmann-zum-spielzeugmacher.pdf'
FRITZ = 'https://www.bergbaumuseum.de/fileadmin/forschung/zeitschriften/der-anschnitt/1959/1959-06/anschnitt-6-1959-karl-ewald-fritzsch-bergmann-und-engel-als-weihnachtliche-lichtentraeger.pdf'
SIEB52 = 'https://www.bergbaumuseum.de/fileadmin/forschung/zeitschriften/der-anschnitt/1952/1952-06/anschnitt-1952-6-sieber-weihnachtsberge.pdf'
EPD25 = 'https://www.evangelisch.de/inhalte/250493/11-12-2025/warum-das-erzgebirgische-kunsthandwerk-so-bekannt-ist'
DPA26 = 'https://www.volksstimme.de/panorama/warum-in-sachsen-weihnachtspyramiden-angeschoben-werden-4358879'
GDCH = 'https://archiv.gdch.de/fileadmin/downloads/Netzwerk_und_Strukturen/Fachgruppen/Geschichte_der_Chemie/Mitteilungen_Band_09/1993-09-06.pdf'
REICH = 'https://opac.geologie.ac.at/ais312/dokumente/JB0032_036_A.pdf'
TREE21 = 'https://www.evangelisch.de/inhalte/193970/07-12-2021/den-weihnachtsbaum-gibt-es-seit-500-jahren'
TREE09 = 'https://www.evangelisch.de/inhalte/97564/18-12-2009'
ADVENT = 'https://www.britannica.com/topic/Advent'
FAU = 'https://bafid.fau.de/files/2024/12/02-02-Darstellung-des-Herrn-im-Tempel.pdf'
U1830 = 'https://commons.wikimedia.org/wiki/File:Christmas_pyramid_from_about_1830.jpg'
UGLOB = 'https://commons.wikimedia.org/wiki/File:Globensteiner_Pyramide.jpg'
UGLOBD = 'https://commons.wikimedia.org/wiki/File:Globensteiner_Pyramide_Detail.jpg'
UJG = 'https://commons.wikimedia.org/wiki/File:Johanngeorgenstadt._Am_Pferdeg%C3%B6pel_2H1A3971WI.jpg'


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
 # 재벌(2026-11-22): 뒷이야기·열쇠 영화에만 쓰는 그림(받아 둔 그림 · 앞의 사진 부분)
  'p30top': {'src': S + 'Christmas_pyramid_from_about_1830.jpg', 'crop': (0.30, 0.20, 0.72, 0.43), 'max': 1600, 'cap': '1830년 무렵 피라미드의 맨 위층', 'cr': '사진: Klaaschwotzer · CC0 · 위키미디어 공용 · 일부 잘라 씀', 'u': U1830,
             'alt': '노란 나무틀 안 둥근 판 위에, 잎이 달린 나무 한 그루와 사슴, 새들, 허리에 천을 두른 두 사람이 서 있다. 한 사람은 둥근 열매를 들고 있다.'},
  'p30mid': {'src': S + 'Christmas_pyramid_from_about_1830.jpg', 'crop': (0.25, 0.47, 0.80, 0.66), 'max': 1600, 'cap': '1830년 무렵 피라미드의 가운데층', 'cr': '사진: Klaaschwotzer · CC0 · 위키미디어 공용 · 일부 잘라 씀', 'u': U1830,
             'alt': '둥근 판 위에 높은 모자와 빨간 옷, 지팡이를 든 인형들이 둘러서 있다. 오른쪽에는 날개가 달린 듯한 인형과 하얀 치마를 입은 인형이 보인다. 판 옆으로 작은 초 접시가 달린 쇠막대가 튀어나와 있다.'},
  'p30bot': {'src': S + 'Christmas_pyramid_from_about_1830.jpg', 'crop': (0.25, 0.68, 0.75, 0.90), 'max': 1600, 'cap': '1830년 무렵 피라미드의 맨 아래층', 'cr': '사진: Klaaschwotzer · CC0 · 위키미디어 공용 · 일부 잘라 씀', 'u': U1830,
             'alt': '둥근 판 위에 검고 높은 모자를 쓰고 하얀 바지를 입은 인형들이 빽빽이 서 있다. 가운데 한 인형이 큰 깃발을 들었고, 오른쪽 뒤에는 나팔을 든 인형이 있다.'},
  'glob': {'src': S + 'Globensteiner_Pyramide.jpg', 'max': 1600, 'cap': '글로벤슈타인 피라미드의 한 층(2011년 사진)', 'cr': '사진: Klaaschwotzer · 퍼블릭 도메인(CC0) · 위키미디어 공용', 'u': UGLOB,
           'alt': '하얀 나무 기둥과 난간을 두른 피라미드의 한 층. 금빛 왕관을 쓴 인물들이 낙타와 말을 타거나 곁에 서 있고, 초록 옷을 입은 사람과 작은 나무들이 함께 놓여 있다.'},
  'globd': {'src': S + 'Globensteiner_Pyramide_Detail.jpg', 'max': 1600, 'cap': '같은 피라미드의 다른 층', 'cr': '사진: Klaaschwotzer · 퍼블릭 도메인(CC0) · 위키미디어 공용', 'u': UGLOBD,
            'alt': '하얀 기둥 사이에 눈이 내려앉은 듯한 전나무와 작은 나무들이 서 있고, 그 가운데 흰 수염에 챙 모자를 쓰고 파란 옷을 입은 사람이 지팡이를 들고 서 있다.'},
  'jg': {'src': S + 'Johanngeorgenstadt._Am_Pferdeg_pel_2H1A3971WI.jpg', 'max': 1600, 'cap': '요한게오르겐슈타트, 말 권양기 박물관 앞 겨울 길(2022년 사진)', 'cr': '사진: Kora27 · CC BY-SA 4.0 · 위키미디어 공용', 'u': UJG,
         'alt': '눈이 두껍게 쌓인 나무들 사이로 하얀 길이 뻗어 있고, 길 끝에 눈 덮인 지붕의 작은 하얀 집이 있다. 파란 하늘 아래 낮은 햇빛이 길에 긴 그림자를 드리운다.'},
 },
 'scenes': [
  {'id': 'gopel', 'label': '말이 돌리던 광산의 탑', 'kind': 'duo', 'imgs': ['gopel', 'p1830'],
   'caps': ['요한게오르겐슈타트의 말 권양기 집', '1830년 무렵 쇤하이데의 피라미드'],
   'text': ['독일과 체코 사이의 에르츠산맥은 ‘광석의 산’이라는 뜻이에요. 16세기부터 이렇게 불렸어요. 그때 이 산에는 광석을 캐는 광산이 곳곳에 있었어요.',
            '광산에는 ‘말 권양기’가 있었어요. 권양기는 무거운 것을 감아 올리는 기계예요. 말이 기계에 달린 긴 막대를 끌며 원을 그리고 돌면 가운데 굵은 축이 돌아가요. 축에 감기는 줄이 깊은 갱도에서 광석 통을 끌어 올렸어요.',
            '프라이베르크 근처 힘멜스퓌르스트 광산에도 말 권양기가 있었어요. 프라이베르크 광산 대학에 그 모형이 남아 있어요.',
            '이 카드의 주인공 성탄 피라미드는 층마다 인형을 세우고, 불을 켜면 빙글빙글 도는 나무 촛대예요. 지버는 이렇게 적었어요.'],
   'quote': {'t': '‘돌아가는 촛대’라고도 불렀는데, 옛 광산의 권양기를 본뜬 것이에요.',
             'from': '지크프리트 지버, 「에르츠산맥 광부들의 성탄 풍습」(1959) · 독일어를 이 안내서가 옮김', 'u': SIEBER},
   'text2': ['에르츠산맥 사람들은 성탄 피라미드를 사투리로 ‘페레메트’라고 불러요. 가운데 축에 층층이 판을 꿴 모양을 보고 말 권양기를 떠올린 사람들이 있었을 거라고 해요.'],
   'kid': '광산에서는 말이 빙빙 돌면서 무거운 광석을 끌어 올렸대.',
   'kidq': '말이 빙빙 돌리는 기계랑 피라미드, 어디가 닮았어?'},
  {'id': 'eve', 'label': '성탄 전날의 ‘촛대 상자’', 'kind': 'quote',
   'text': ['에르츠산맥의 역사를 연구한 향토사가 지크프리트 지버는 옛 광산의 성탄 전날을 이렇게 적었어요.',
            '프라이베르크 근처 힘멜스퓌르스트 광산의 광부들은 12월 24일에도 여느 날처럼 새벽 네 시에 모였어요. 성탄 전 마지막으로 일하는 날이었어요.',
            '일하는 중간에 쉬며 먹는 큰 새참 때까지만 일했어요. 작은 걸상에 둘러앉아 아침을 먹고, 이야기를 나누고 성탄 노래를 불렀어요. 바위에 뚫고 화약을 넣은 발파 구멍이 모두 터지기를 기다렸다가, 여느 날보다 일찍 땅 위로 올라왔어요.'],
   'quote': {'t': '집에 오면 광부는 촛대 상자를 풀고 성탄을 준비했어요.',
             'from': '지크프리트 지버, 「에르츠산맥 광부들의 성탄 풍습」(1959) · 독일어를 이 안내서가 옮김', 'u': SIEBER},
   'text2': ['광부들은 곳곳에서 초를 든 광부와 천사를 나무로 깎았어요. 피라미드도 광부들이 만든 불빛 가운데 하나였어요.'],
   'choose': True,
   'kid': '성탄 전날엔 광부 아저씨들이 여느 날보다 일찍 집에 왔대.',
   'kidq': '일찍 집에 온 아빠가 상자를 열면, 무엇이 나올까?'},
  {'id': 'light', 'label': '가장 오래된 피라미드에 불 켜기', 'kind': 'mod', 'mod': 'place', 'night': True,
   'text': ['안나베르크부흐홀츠의 에르츠산맥 박물관에는 따뜻한 공기로 도는 성탄 피라미드 가운데 지금 남은 가장 오래된 것이 있어요. 예전 주인의 이름을 따서 ‘렌츠의 피라미드’라고 불러요.',
            '층이 넷이고, 맨 위에 커다란 날개가 열 장 달렸어요. 박물관 기록은 층마다 선 인형을 아래층부터 적어 두었어요. 광부 행렬, 아기 예수 탄생과 동방박사·목자, 낙타와 여러 동물, 천사 차례예요. 그 차례대로 놓고, 끝으로 불을 켜 보세요.'],
   'text2': ['이 피라미드에는 지금도 유채 기름을 태우는 작은 등잔이 달려 있어요. 뒤에 나온 피라미드들은 등잔 대신 초로 돌렸어요.',
             '무대 그림은 박물관 기록의 차례를 따라 이 안내서가 그렸어요. 실제 피라미드의 모습과는 달라요.'],
   'kid': '피라미드를 한 층씩 꾸며 볼까? 맨 아래는 광부 아저씨들이야!',
   'kidq': '불을 켜면 어떻게 될까?'},
  {'id': 'square', 'label': '마을 광장의 큰 피라미드', 'kind': 'photo', 'img': 'krauss',
   'text': ['1930년대부터 에르츠산맥의 성탄 장터에 사람 키보다 훨씬 큰 피라미드가 몇 개씩 서기 시작했어요. 1950년대까지도 독일 전체에 열 개 남짓이었다고 해요. 오늘은 독일 곳곳의 성탄 장터에 큰 피라미드가 서요.',
            '사진은 슈바르첸베르크 광장의 크라우스 피라미드예요. 날개판에 별 모양 구멍이 촘촘히 뚫려 있어요.'],
   'text2': ['오늘 에르츠산맥의 성탄 철은 대림절(성탄을 준비하며 기다리는 때) 첫 일요일 무렵 ‘피라미드 밀기’로 시작해요. 마을 사람들이 모여 큰 피라미드를 처음 돌리는 날이에요. 빠른 곳은 그 앞 금요일 저녁부터 돌려요. 이 고장 사투리로는 ‘페레메트 아쉼’이라고 해요.',
             '성탄 철은 2월 2일 성촉절에 끝나요. 성촉절은 마리아와 요셉이 아기 예수를 데리고 처음 성전에 간 날을 기억하는 축일이에요.'],
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
 # ── 재벌(2026-11-22): 열쇠 물음 셋 ──
 'qs': [
  {'q': '아무도 밀지 않는데, 정말 어떻게 돌아요?', 'img': 'p1830', 'pos': '50% 8%',
   'a': ['판 가장자리에 꽂은 초나 등잔에 불을 켜면, 데워진 공기가 위로 올라가요. 맨 위의 비스듬한 날개가 이 공기에 밀려 돌고, 날개가 꽂힌 가운데 축과 축에 꿰인 판들이 함께 돌아요.',
         '바람개비를 아래에서 입김으로 불면 도는 것과 비슷해요. 진짜로는 입김 대신 불이 데운 공기가 밀어요. 축의 아래 끝은 뾰족하게 깎아 받침의 오목한 자리에 세워요.'],
   'see': '셋째 장면의 등잔불이, 날개를 밀어 올리는 보이지 않는 바람으로 보여요.', 'seeAt': 'light',
   'film': [
    {'type': 'img', 'img': 'p1830', 'fit': 'cover', 'p0': '77% 60%', 'p1': '75% 58%', 's0': 1.5, 's1': 1.7,
     'lines': [{'t': '판 옆의 작은 접시에 초나 등잔을 얹어요.'}, {'t': '불을 켜면 데워진 공기가 위로 올라가요.'}],
     'kid': [{'t': '초에 불을 켜면 따뜻한 바람이 위로 올라가!'}]},
    {'type': 'img', 'img': 'p1830', 'fit': 'cover', 'p0': '50% 0%', 'p1': '50% 4%', 's0': 1.25, 's1': 1.1,
     'lines': [{'t': '맨 위의 비스듬한 날개가 그 공기에 밀려 돌아요.'}, {'t': '바람개비를 아래에서 불면 도는 것과 비슷해요.'}],
     'kid': [{'t': '꼭대기 날개가 바람개비처럼 빙글!'}]},
    {'type': 'img', 'img': 'p1830', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 62%', 's0': 1.3, 's1': 1.15,
     'lines': [{'t': '날개가 꽂힌 가운데 축이 돌면, 축에 꿰인 층들이 함께 돌아요.'}],
     'kid': [{'t': '가운데 막대가 돌면 인형들도 같이 돌아.'}]},
    {'type': 'img', 'img': 'p1830', 'fit': 'cover', 'p0': '50% 50%', 'p1': '50% 45%', 's0': 1.0, 's1': 1.06,
     'lines': [{'t': '이제 셋째 장면을 다시 볼까요?'}, {'t': '불을 켜면, 보이지 않는 바람이 날개를 밀어요.'}],
     'kid': [{'t': '이제 다시 보면, 따뜻한 바람이 탑을 돌려!'}]}]},
  {'q': '광부들이 왜 성탄 장식을 깎았어요?', 'img': 'glob', 'pos': '45% 50%',
   'a': ['17세기부터 이 산의 좋은 광맥이 하나둘 바닥났어요. 사람들은 흔한 가문비나무로 눈을 돌렸고, 나무를 돌려 깎는 선반공이 1670년 무렵 23명에서 백 년 뒤 100명으로 늘었어요.',
         '광부들은 돈을 적게 벌었어요. 그래서 초를 든 광부와 천사를 깎아 가족이 쓰고, 남는 것은 팔아 살림에 보탰어요.'],
   'see': '둘째 장면의 ‘촛대 상자’가, 광부가 손수 깎아 가족과 나누고 팔기도 한 물건들로 보여요.', 'seeAt': 'eve',
   'film': [
    {'type': 'img', 'img': 'gopel', 'fit': 'cover', 'p0': '40% 50%', 'p1': '50% 45%', 's0': 1.2, 's1': 1.05,
     'lines': [{'t': '17세기부터 이 산의 좋은 광맥이 하나둘 바닥났어요.'}],
     'kid': [{'t': '광산에서 캘 돌이 점점 줄었대.'}]},
    {'type': 'img', 'img': 'glob', 'fit': 'cover', 'p0': '30% 45%', 'p1': '60% 50%', 's0': 1.15, 's1': 1.15,
     'lines': [{'t': '사람들은 흔한 나무를 깎기 시작했어요.'}, {'t': '나무를 돌려 깎는 사람이 백 년 사이 23명에서 100명이 되었어요.'}],
     'kid': [{'t': '그래서 나무로 인형을 깎기 시작했어!'}]},
    {'type': 'img', 'img': 'p30mid', 'fit': 'cover', 'p0': '30% 50%', 'p1': '70% 50%', 's0': 1.1, 's1': 1.1,
     'lines': [{'t': '돈을 적게 벌던 광부들도 초를 든 인형을 깎았어요.'}, {'t': '가족이 쓰고, 남는 것은 팔았어요.'}],
     'kid': [{'t': '가족 선물도 하고, 팔기도 했대.'}]},
    {'type': 'black',
     'lines': [{'t': '이제 둘째 장면을 다시 볼까요?'}, {'t': '일찍 올라온 광부가 푸는 상자에는, 손수 깎은 불빛이 들어 있어요.'}],
     'kid': [{'t': '이제 다시 보면, 아빠가 깎은 인형 상자야!'}]}]},
  {'q': '‘대림절’과 ‘성촉절’은 뭐예요? 성탄 철이 왜 2월까지예요?', 'img': 'krauss', 'pos': '50% 40%',
   'a': ['대림절은 ‘오심’이라는 뜻으로, 성탄을 준비하며 기다리는 때예요. 11월 30일에 가장 가까운 일요일에 시작해서, 2026년에는 11월 29일이 첫날이에요.',
         '성촉절은 성탄 40일째인 2월 2일, 아기 예수가 처음 성전에 간 날(' + bl('LUK.2', '누가복음 2장 22절') + ')을 기억해요. 초를 들고 걷던 행렬에서 ‘빛의 미사’라는 독일 이름이 왔대요. 오랫동안 성탄 절기는 이날 끝났어요.'],
   'see': '넷째 장면의 ‘피라미드 밀기’가, 성탄을 기다리는 때를 여는 첫 신호로 보여요.', 'seeAt': 'square',
   'film': [
    {'type': 'black',
     'lines': [{'t': '대림절은 ‘오심’이라는 뜻이에요.'}, {'t': '성탄을 준비하며 기다리는 때예요.'}],
     'kid': [{'t': '대림절은 아기 예수 오시는 날을 기다리는 때래.'}]},
    {'type': 'img', 'img': 'krauss', 'fit': 'cover', 'p0': '50% 62%', 'p1': '50% 50%', 's0': 1.2, 's1': 1.05,
     'lines': [{'t': '2026년에는 11월 29일 일요일에 시작해요.'}, {'t': '에르츠산맥에서는 그 무렵 큰 피라미드를 처음 돌려요.'}],
     'kid': [{'t': '그때 큰 피라미드가 처음 돌기 시작해!'}]},
    {'type': 'img', 'img': 'p1830', 'fit': 'cover', 'p0': '77% 60%', 'p1': '50% 40%', 's0': 1.5, 's1': 1.15,
     'lines': [{'t': '2월 2일 성촉절은 아기 예수가 처음 성전에 간 날이에요.'}, {'t': '초를 들고 걷던 날, 오랫동안 성탄 절기가 여기서 끝났어요.'}],
     'kid': [{'t': '2월 2일, 촛불의 날에 성탄 철이 끝나.'}]},
    {'type': 'img', 'img': 'krauss', 'fit': 'cover', 'p0': '50% 35%', 'p1': '50% 45%', 's0': 1.1, 's1': 1.0,
     'lines': [{'t': '이제 넷째 장면을 다시 볼까요?'}, {'t': '촛불의 날까지, 불로 도는 탑이 두 달 넘게 돌아요.'}],
     'kid': [{'t': '이제 다시 보면, 두 달 넘게 도는 탑이야!'}]}]},
 ],
 # ── 재벌(2026-11-22): 뒷이야기 꾸러미 ──
 'qx': [
  # 꾸러미 1(창이 고름: 대변인이 가장 먼저 물은 것 · 그림 속 ‘저건 뭐지?’ · 사람의 이야기)
  {'id': 'whim', 'pack': 1, 'q': '권양기 집 고깔 지붕 밑에서 말이 빙빙 돌았어요?', 'hook': '말과 소가 돌던 고깔 지붕', 'img': 'gopel', 'pos': '62% 35%',
   'a': ['네. 말 권양기는 16세기부터 19세기까지 중부 유럽 광산의 대표적인 기계였어요. 끈을 맨 말이나 소가 돌리는 막대를 끌며 원을 그리고 걸으면, 줄이 감기는 축이 돌았어요.',
         '에르츠산맥은 날씨가 거칠어서 권양기에 지붕을 덮어 주는 일이 많았어요. 프라이베르크 광산에서는 1902년까지도 이 권양기로 갱도에서 짐을 끌어 올렸어요.'],
   'see': '첫 장면의 고깔 지붕 집이, 말과 소가 빙빙 돌던 권양기의 겉옷으로 보여요.', 'seeAt': 'gopel',
   'src': [{'t': 'TU 베르크아카데미 프라이베르크 소장품: 힘멜스퓌르스트 광산의 말 권양기 모형', 'm': '독일어 · museum-digital · 16~19세기 광산의 기계, 말이나 소가 돌리는 막대를 끌며 원을 돎, 거친 날씨 때문에 지붕을 덮음, 프라이베르크에서 1902년까지 씀', 'u': GOPELM}]},
  {'id': 'name', 'pack': 1, 'q': '이집트 피라미드랑 하나도 안 닮았는데, 왜 ‘피라미드’예요?', 'hook': '이집트 소식이 산골까지', 'img': 'krauss', 'pos': '50% 30%',
   'a': ['이 탑은 위로 갈수록 작아지는 둥근 판을 층층이 쌓아 만들어요. 1790년 무렵 처음 나왔을 때는 정해진 이름이 없었대요.',
         '한 개신교 매체는 나폴레옹의 이집트 원정 소식과 그림이 이 산골까지 전해진 뒤, ‘피라미드’라는 말이 사투리 ‘페레메트’로 자리 잡았다고 소개해요.'],
   'see': '첫 장면의 사투리 ‘페레메트’가, 먼 이집트 소식이 산골 말로 바뀐 이름으로 보여요.', 'seeAt': 'gopel',
   'src': [{'t': 'TU 켐니츠 대학 대림절 달력(1997) 「에르츠산맥의 성탄 풍습」', 'm': '독일어 · 사투리 ‘페르메트’, 위로 갈수록 작아지는 판을 쌓은 모양', 'u': TUC17},
           {'t': '게오르크 클라인, 피라미드와 슈비보겐(evangelisch.de, 2009)', 'm': '독일어 · 1790년 무렵 첫 피라미드에는 정해진 이름이 없었음, 나폴레옹의 이집트 원정 소식과 그림, 사투리 ‘페레메트’', 'u': EVDE}]},
  {'id': 'tree', 'pack': 1, 'q': '이건 장식이에요, 크리스마스트리 같은 거예요?', 'hook': '트리와 한 뿌리래요', 'img': 'p1830', 'pos': '50% 50%',
   'a': ['옛날 브란덴부르크와 작센의 교회는 대림절에 ‘빛 틀’을 세웠어요. 푸른 가지를 감은 막대 넷을 꼭대기에서 묶고 초를 꽂은 틀이었어요.',
         '큰 도시에서는 이 틀이 나중에 성탄 트리가 되었고, 에르츠산맥 사람들은 틀 안을 꾸미기 시작했대요. 독일 성탄 박물관은 에르츠산맥에서는 피라미드가 흔히 성탄 트리를 대신한다고 소개해요.'],
   'see': '앞면 카드의 탑이, 성탄 트리와 한 뿌리에서 갈라져 나온 형제로 보여요.', 'seeAt': 'front',
   'go': {'t': '「윈저성의 성탄 트리」 카드로 가기', 'cid': 'cus-tree'},
   'src': [{'t': '게오르크 클라인, 피라미드와 슈비보겐(evangelisch.de, 2009)', 'm': '독일어 · 브란덴부르크·작센 교회의 대림절 빛 틀(푸른 가지를 감은 막대 넷, 꼭대기에서 묶고 초를 꽂음), 큰 도시에서는 성탄 트리로, 에르츠산맥에서는 틀 안을 꾸밈', 'u': EVDE},
           {'t': '독일 성탄 박물관: 피라미드', 'm': '영어 · 에르츠산맥에서는 피라미드가 흔히 성탄 트리를 대신함', 'u': XMUS}]},
  {'id': 'daylight', 'pack': 1, 'q': '광부들은 햇빛이 그리워서 그렇게 불을 켰을까요?', 'hook': '아름다운 이야기, 사실일까?', 'img': 'globd', 'pos': '50% 45%',
   'a': ['2009년 한 개신교 매체는 광부들이 겨울에 거의 보지 못한 햇빛을 그리워했다고 썼어요. 촛불 아치 ‘슈비보겐’의 옛 장식이 해와 달, 별이어서 하늘을 그린 것으로 보인대요.',
         '2025년 드레스덴의 미술사학자 이고르 옌첸은 이를 18세기 말쯤 퍼진 ‘경건한 전설’이라고 했어요. 불빛을 사랑한 까닭은 햇빛 그리움이 아니라, 잔치 때 불을 환히 밝히던 데 있다고 봐요.'],
   'see': '둘째 장면 ‘촛대 상자’ 속 불빛이, 햇빛을 그리던 마음일 수도 잔치의 불빛일 수도 있어 보여요.', 'seeAt': 'eve',
   'src': [{'t': '게오르크 클라인, 피라미드와 슈비보겐(evangelisch.de, 2009)', 'm': '독일어 · 슈비보겐의 옛 장식(해·달·별)은 하늘을, 겨울에 햇빛을 거의 못 본 광부들의 그리움을 나타낸다고 봄', 'u': EVDE},
           {'t': '「에르츠산맥 공예는 왜 이렇게 유명할까」(epd 인터뷰, evangelisch.de, 2025.12.11)', 'm': '독일어 · 미술사학자 이고르 옌첸: 햇빛 그리움은 18세기 말쯤 퍼진 경건한 전설, 불빛 사랑은 잔치의 조명에서', 'u': EPD25}]},
  {'id': 'push', 'pack': 1, 'q': '‘피라미드 밀기’ 날엔 진짜 손으로 밀어요?', 'hook': '“영차!” 세 번이면 돌아요', 'img': 'jg', 'pos': '50% 60%',
   'a': ['요즘 광장의 큰 피라미드는 전기로 돌아요. 그래서 미는 시늉만 해요. 안나베르크부흐홀츠에서는 1993년부터 다 함께 “하우 루크(영차)!”를 세 번 외치면 피라미드가 돌기 시작해요.',
         '드레스덴시는 “실제로 미는 사람은 없다”고 말해요. 2026년 요한게오르겐슈타트의 피라미드 밀기는 대림절 첫 일요일 앞 목요일, 11월 26일이에요.'],
   'see': '넷째 장면의 큰 피라미드가, 온 마을의 “영차!” 소리에 첫 바퀴를 도는 탑으로 보여요.', 'seeAt': 'square',
   'src': [{'t': '「작센에서는 왜 성탄 피라미드를 밀까」(dpa, 2026.11.19 · 폭스슈티메 실림)', 'm': '독일어 · 큰 피라미드는 전기로 돌고 미는 것은 상징, 안나베르크부흐홀츠는 1993년부터 ‘하우 루크’ 세 번, 드레스덴시 “직접 미는 사람은 없다”, 요한게오르겐슈타트 2026년 11월 26일', 'u': DPA26}]},
  {'id': 'angel', 'pack': 1, 'q': '초를 든 천사와 광부는 왜 늘 짝이에요?', 'hook': '천사가 광맥을 가리켰대요', 'img': 'p30mid', 'pos': '80% 45%',
   'a': ['에르츠산맥의 성탄 방에는 초를 든 천사와 광부가 빠지지 않았대요. 1520년의 한 에르츠산맥 그림에는 천사가 날아와 광석이 있는 곳을 가리키고, 광부가 일을 시작해요.',
         '옛날에는 장인의 집에 놓인 천사와 광부의 수로 일꾼이 몇 명인지 알 수 있었대요. 하녀마다 천사 하나, 젊은 일꾼마다 광부 하나였거든요.'],
   'see': '둘째 장면 고르기의 ‘촛불 천사’와 ‘촛불 광부’가, 하늘과 땅을 잇는 한 쌍으로 보여요.', 'seeAt': 'eve',
   'src': [{'t': 'TU 켐니츠 대학 대림절 달력(1997) 「에르츠산맥의 성탄 풍습」 · 천사와 광부', 'm': '독일어 · 천사와 광부는 하늘과 땅을 이음, 1520년 그림(천사가 광석 있는 곳을 가리킴), 19세기부터 깎은 인형, 하녀마다 천사·젊은 일꾼마다 광부', 'u': TUC17}]},
  # 꾸러미 2(꾸러미 1에서 이어져요)
  {'id': 'tallest', 'pack': 2, 'q': '세상에서 가장 큰 피라미드는 얼마나 커요?', 'hook': '25미터가 넘는 피라미드', 'img': 'krauss', 'pos': '50% 55%',
   'a': ['2026년 독일 dpa 통신은 세상에서 가장 큰 성탄 피라미드가 요한게오르겐슈타트에 있다고 전해요. 높이가 25.52미터예요.',
         '드레스덴의 슈트리첼마르크트에도 1997년부터 에르츠산맥식 피라미드가 서요. 2026년의 높이는 14.61미터예요.'],
   'see': '첫 장면의 말 권양기 집이 선 마을이, 세상에서 가장 큰 피라미드가 서는 마을로 보여요.', 'seeAt': 'gopel',
   'go': {'t': '「드레스덴 슈트리첼마르크트」 카드로 가기', 'cid': 'adv-striezel'},
   'src': [{'t': '「작센에서는 왜 성탄 피라미드를 밀까」(dpa, 2026.11.19 · 폭스슈티메 실림)', 'm': '독일어 · 요한게오르겐슈타트에 세계에서 가장 큰 피라미드(25.52m), 드레스덴 슈트리첼마르크트는 1997년부터·14.61m', 'u': DPA26}]},
  {'id': 'apron', 'pack': 2, 'q': '천사가 앞치마를 둘렀네요? 광부의 아내 아니에요?', 'hook': '천사일까, 광부의 아내일까', 'img': 'p30mid', 'pos': '85% 45%',
   'a': ['19세기부터 이 짝은 나무를 돌려 깎은 인형으로 퍼졌어요. 그려 넣은 앞치마 때문에 천사는 날개만 빼면 땅의 아가씨처럼 보였대요.',
         '그래서 광부의 아내로 보는 사람도 있었어요. 1959년 카를 에발트 프리치는 하얀 천사가 신앙의 세계에서 왔다고 보았어요. 뉘른베르크의 금박 천사를 본떴다고 보는 글도 있어요.'],
   'see': '둘째 장면 고르기의 ‘촛불 천사’가, 하늘의 천사와 땅의 아가씨 사이에 선 인형으로 보여요.', 'seeAt': 'eve',
   'go': {'t': '「바스락거리는 금빛 옷」 카드로 가기', 'cid': 'craft-angel'},
   'src': [{'t': 'TU 켐니츠 대학 대림절 달력(1997) · 천사와 광부', 'm': '독일어 · 19세기부터 깎은 인형으로 흔해짐, 날개로만 천사인 줄 앎, 그려 넣은 앞치마로 땅의 아가씨가 됨', 'u': TUC17},
           {'t': '카를 에발트 프리치, 「성탄의 불을 든 광부와 천사」, 『데어 안슈니트』 1959년 6호', 'm': '독일어 · 천사를 광부의 아내로 본 ‘합리주의’ 해석, 하얀 천사는 신앙의 세계에서 왔다고 봄', 'u': FRITZ},
           {'t': '하이데 브라우크뮐러, 「광부에서 장난감 장인으로」, 『데어 안슈니트』 1999년 5·6호', 'm': '독일어 · 초를 든 여인상은 뉘른베르크 금박 천사를 본뜬 것으로 여겨짐, 천사보다 광부의 아내에 가까워 보임', 'u': BRAUK}]},
  {'id': 'seyffert', 'pack': 2, 'q': '그럼 ‘광부의 공예’라는 이야기는 누가 키웠어요?', 'hook': '“도는 피라미드를 만들어 봐요”', 'img': 'glob', 'pos': '50% 45%',
   'a': ['2025년 미술사학자 옌첸에 따르면, 민속학자 오스카 자이페르트(1862~1940)가 이 고장 장난감 만드는 이들의 물건을 ‘민속 예술’로 내세웠어요.',
         '그는 만드는 이들에게 “도는 피라미드와 광부 감독 인형을 만들어 보라”고 권했대요. 옌첸은 그전까지 이들이 성탄 인형과 거의 상관이 없었다고 말해요.'],
   'see': '셋째 장면의 렌츠의 피라미드가, ‘민속 예술’이라는 이름이 붙기 훨씬 전부터 있던 물건으로 보여요.', 'seeAt': 'light',
   'src': [{'t': '「에르츠산맥 공예는 왜 이렇게 유명할까」(epd 인터뷰, evangelisch.de, 2025.12.11)', 'm': '독일어 · 오스카 자이페르트(1862~1940)가 장난감을 ‘민속 예술’로 내세움, “도는 피라미드와 광부 감독 인형을 만들어 보라”', 'u': EPD25}]},
  {'id': 'gerlach', 'pack': 2, 'q': '광산 일을 못 하게 된 광부는 어떻게 살았어요?', 'hook': '등에 광산을 지고 다닌 사람', 'img': 'jg', 'pos': '50% 78%',
   'a': ['1841년 프라이베르크 근처에서 태어난 에른스트 페르디난트 게를라흐는 할아버지와 아버지처럼 광부가 되었어요. 서른두 살 때 갱도의 발파 사고로 다쳐 더는 일할 수 없었어요.',
         '그는 자기가 다친 광산을 작은 모형으로 만들어 장터와 학교에서 보여 주고 돈을 받았어요. 일흔이 다 되어서도 등에 지는 광산 모형을 들고 드레스덴 장터에 섰어요.'],
   'see': '첫 장면의 광산이, 한 사람의 등에 실려 장터를 돌던 작은 세상으로 보여요.', 'seeAt': 'gopel',
   'src': [{'t': '하이데 브라우크뮐러, 「광부에서 장난감 장인으로」, 『데어 안슈니트』 1999년 5·6호', 'm': '독일어 · 1841년 브라운스도르프에서 난 게를라흐, 32살에 발파 사고, 다친 광산의 모형을 장터·광장·학교에서 보여 줌, 일흔 가까이 드레스덴 장터에서 ‘등짐 광산’', 'u': BRAUK}]},
  {'id': 'stollen', 'pack': 2, 'q': '가난한 광부들에게 성탄 잔치는 어땠어요?', 'hook': '광부들이 지켜 낸 슈톨렌', 'img': 'gopel', 'pos': '35% 45%',
   'a': ['슈네베르크 시의회는 이 고장 빵집을 지키려고 다른 곳 빵 장수를 막으려 했어요. 광부들이 따져서, 슈네베르크의 성탄 슈톨렌을 세 ‘거룩한 저녁’마다 싸고 좋게 팔게 만들었어요.',
         '1665년에는 부활절과 성령강림절에도 슈톨렌을 굽게 해 달라고 청했어요. “광부와 가난한 이들도 거룩한 때를 조금이나마 누리도록”이었지만, 그 청은 받아들여지지 않았어요.'],
   'see': '둘째 장면의 광부들이, 빵 한 조각의 축제도 스스로 지켜 낸 사람들로 보여요.', 'seeAt': 'eve',
   'go': {'t': '「드레스덴 슈톨렌」 카드로 가기', 'cid': 'adv-stollen'},
   'src': [{'t': '지크프리트 지버, 「에르츠산맥 광부들의 성탄 풍습」, 『데어 안슈니트』 1959년 6호', 'm': '독일어 · 슈네베르크 광부들의 청원, 세 ‘거룩한 저녁’(12월 24·31일, 1월 5일)의 싸고 좋은 슈톨렌, 1665년 부활절·성령강림절 청원은 실패', 'u': SIEBER}]},
  {'id': 'parade', 'pack': 2, 'q': '1830년 피라미드 맨 아래층 인형들은 군인이에요, 광부예요?', 'hook': '높은 모자와 깃발의 행렬', 'img': 'p30bot', 'pos': '50% 50%',
   'a': ['이 사진의 설명에는 인형들이 누구인지 적혀 있지 않아요. 다만 가장 오래된 렌츠의 피라미드는 맨 아래층에 광부 행렬을 세웠어요.',
         '에르츠산맥 광부들은 성탄에도 무리 지어 걸었어요. 1959년 지버는 광부 조합이 새벽 다섯 시 성탄 미사에 줄지어 들어가곤 했고, 외슈타트에서는 성탄 셋째 날이 광부 행렬의 날이었다고 적었어요.'],
   'see': '셋째 장면 맨 아래층의 광부 행렬이, 성탄 새벽 줄지어 교회로 가던 광부들로 보여요.', 'seeAt': 'light',
   'src': [{'t': '위키미디어 공용: 1830년 무렵의 피라미드(쇤하이데)', 'm': '영어 · 1830년 무렵 쇤하이데에서 만든 피라미드, 인형이 누구인지는 적지 않음', 'u': U1830},
           {'t': 'sachsen.museum-digital: 렌츠의 피라미드', 'm': '독일어 · 맨 아래층은 광부 행렬', 'u': LENZ},
           {'t': '지크프리트 지버, 「에르츠산맥 광부들의 성탄 풍습」, 『데어 안슈니트』 1959년 6호', 'm': '독일어 · 새벽 5시 성탄 미사에 광부 조합이 줄지어 참여, 외슈타트의 성탄 셋째 날 광부 행렬', 'u': SIEBER}]},
  {'id': 'adam', 'pack': 2, 'q': '1830년 피라미드 맨 위층의 나무와 두 사람은 무슨 장면이에요?', 'hook': '맨 위층의 둥근 열매', 'img': 'p30top', 'pos': '55% 50%',
   'a': ['사진의 설명에는 누구인지 적혀 있지 않아요. 다만 나무 아래 둥근 열매를 든 두 사람은 성경의 첫 사람 아담과 하와(' + bl('GEN.3', '창세기 3장') + ')를 떠올리게 해요.',
         '12월 24일은 이 첫 부부를 기억하는 날이기도 했어요. 중세에는 성탄 연극에 앞서 사과를 매단 ‘낙원 나무’ 곁에서 둘의 이야기를 보여 주었고, 북독일에서는 19세기 말까지 성탄 트리에 나무나 빵 반죽으로 만든 아담과 하와를 달았대요.'],
   'see': '앞면 카드 맨 위층의 작은 숲이, 성탄 전날의 낙원으로 보여요.', 'seeAt': 'front',
   'src': [{'t': '「성탄 트리는 500년 전부터」(evangelisch.de, 2021.12.7)', 'm': '독일어 · 중세 성탄 ‘낙원 연극’, 12월 24일은 첫 부부를 기억하는 날, 빨간 사과를 단 ‘낙원 나무’', 'u': TREE21},
           {'t': '게오르크 클라인, 「성탄 트리 — 뿌리가 여럿인 나무」(evangelisch.de, 2009.12.18)', 'm': '독일어 · 북독일에서는 19세기 말까지 나무나 빵 반죽으로 만든 아담·하와·뱀으로 트리를 꾸밈', 'u': TREE09}]},
  # 꾸러미 3(꾸러미 2에서 이어져요)
  {'id': 'berg', 'pack': 3, 'q': '피라미드 말고 또 움직이는 성탄 장식이 있었어요?', 'hook': '손잡이를 돌리면 광산이 움직여요', 'img': 'globd', 'pos': '50% 50%',
   'a': ['에르츠산맥 사람들은 방 한 구석을 가득 채우는 ‘성탄 산’도 꾸몄어요. 이끼와 수정, 촛불로 꾸민 무대에 베들레헴이나 광산 풍경을 세웠고, 대개 시계 장치로 움직였어요.',
         '1786년의 기록에는 요한게오르겐슈타트에서 만들어 외국에까지 판 ‘광산’ 모형이 나와요. 손잡이를 돌리면 움직였대요.'],
   'see': '셋째 장면의 층층 무대가, 방 한 구석을 채우던 움직이는 ‘성탄 산’과 닮아 보여요.', 'seeAt': 'light',
   'src': [{'t': '지크프리트 지버, 「성탄 산」, 『데어 안슈니트』 1952년 6호', 'm': '독일어 · 방 구석의 ‘성탄 산’(이끼·수정·촛불, 베들레헴이나 광산 풍경, 대개 시계 장치), 1786년 요한게오르겐슈타트에서 만들어 외국에 판 손잡이 광산 모형', 'u': SIEB52}]},
  {'id': 'paraffin', 'pack': 3, 'q': '등잔에서 초로 바뀐 건 언제쯤이에요?', 'hook': '나무 타르에서 나온 하얀 밀랍', 'img': 'p1830', 'pos': '77% 60%',
   'a': ['한 개신교 매체는 1830년 파라핀이 나와 누구나 초를 살 수 있게 되자, 피라미드가 독일 곳곳으로 퍼졌다고 소개해요.',
         '그 파라핀은 화학자 카를 폰 라이헨바흐가 1830년 무렵 너도밤나무 타르에서 처음 얻어 냈어요. 1852년 그의 아들은 파라핀을 공장에서 더 많이 만드는 법을 오스트리아 빈의 지질 연구 기관 모임에서 알렸어요.'],
   'see': '셋째 장면 렌츠의 피라미드에 달린 유채 기름 등잔이, 값싼 초가 나오기 전의 불빛으로 보여요.', 'seeAt': 'light',
   'src': [{'t': '게오르크 클라인, 피라미드와 슈비보겐(evangelisch.de, 2009)', 'm': '독일어 · 1830년 파라핀이 나와 초가 누구나 살 만해지면서 피라미드가 독일 곳곳으로 퍼짐', 'u': EVDE},
           {'t': '디터 바그너, 「에른스트 젤 — 독일 타르 증류의 창시자」(독일 화학회 화학사 소식지, 1993)', 'm': '독일어 · 1830년 무렵 라이헨바흐가 너도밤나무 타르에서 파라핀과 크레오소트를 얻음', 'u': GDCH},
           {'t': '라인홀트 폰 라이헨바흐, 「나무 식초에서 파라핀을 공장식으로 만드는 법」(1852)', 'm': '독일어 · 1852년 3월 9일 빈의 지질 연구 기관 모임에서 발표, 아버지가 1830년 나무 타르에서 찾은 밀랍 같은 물질', 'u': REICH}]},
  {'id': 'spider', 'pack': 3, 'q': '땅속 일터에도 성탄 장식을 했어요?', 'hook': '갱도 천장의 ‘촛대 거미’', 'img': 'gopel', 'pos': '45% 45%',
   'a': ['광산마다 저희끼리 ‘광산 성탄’을 지냈어요. 힘멜스퓌르스트 광산의 모임 방에서는 한 광부가 오르간을 치고, 감독이 성탄 기도를 했어요. 초는 광부들이 손수 내놓았어요.',
         '성탄 전날 땅속에서도 광부들은 가져간 초를 켜며 즐거워했어요. 갱도 천장에는 ‘촛대 거미’라 부르는 매다는 촛대가 걸렸대요.'],
   'see': '둘째 장면에서 둘러앉아 노래하던 광부들이, 갱도 천장의 촛불 아래 있는 사람들로 보여요.', 'seeAt': 'eve',
   'src': [{'t': '지크프리트 지버, 「에르츠산맥 광부들의 성탄 풍습」, 『데어 안슈니트』 1959년 6호', 'm': '독일어 · 광산마다 ‘광산 성탄’, 힘멜스퓌르스트 모임 방의 오르간과 성탄 기도, 광부들이 내놓은 초, 갱도 천장의 ‘촛대 거미’', 'u': SIEBER}]},
  {'id': 'funeral', 'pack': 3, 'q': '피라미드 모양 촛대는 처음부터 성탄 장식이었어요?', 'hook': '처음엔 장례식의 촛대', 'img': 'krauss', 'pos': '50% 50%',
   'a': ['독일 성탄 박물관에 따르면 16세기 보헤미아에서는 초를 꽂은 피라미드 모양의 ‘장례 틀’이 장례식에 쓰였어요.',
         '18세기에는 피라미드가 이미 교회의 성탄 장식이었대요. 베를린 둘레에서는 1800년부터 성탄 장대 피라미드가 기록에 나와요.'],
   'see': '앞면 카드의 촛대 탑이, 슬픔의 자리에서 기쁨의 자리로 옮겨 온 오래된 모양으로 보여요.', 'seeAt': 'front',
   'src': [{'t': '독일 성탄 박물관: 피라미드', 'm': '영어 · 16세기 보헤미아의 초를 꽂은 피라미드 모양 장례 틀, 18세기 교회의 성탄 장식, 베를린 둘레의 성탄 장대 피라미드(1800년부터)', 'u': XMUS}]},
 ],
 # ── 재벌 후보 모두(악마의 대변인 2026-11-22 + 창) ──
 'qcand': [
  {'q': '아무도 밀지 않는데 어떻게 돌아요? 날개는 왜 옆으로 돌아요?', 'at': '악마의 대변인 · 앞면 물음, B3·B4, C(비스듬한 날개·초록 막대), D(답이 영화 한 줄에만)', 'a': '판 바깥 초꽂이의 불 → 데운 공기 → 비스듬한 날개·축·판, 뾰족한 축 끝 — 독일 성탄 박물관·TU 켐니츠', 'pick': 1, 'see': '셋째 장면의 등잔불이 날개를 미는 바람으로 보여요.'},
  {'q': '광부가 왜 나무를 깎아? 부업이야?', 'at': '악마의 대변인 · B7, E(왜 만들었는지 끝까지 안 나옴), G', 'a': '17세기 광맥이 바닥남, 선반공 23→100명, 가족용이자 부업 — 브라우크뮐러 1999·지버 1959·evangelisch.de 2009', 'pick': 1, 'see': '둘째 장면의 ‘촛대 상자’가 손수 깎은 살림으로 보여요.'},
  {'q': '대림절·성촉절이 뭐야? 크리스마스가 왜 2월 2일까지야?', 'at': '악마의 대변인 · A17·A19, B14', 'a': '대림절 = 오심, 11월 30일에 가장 가까운 일요일(2026년 11월 29일) · 성촉절 = 성탄 40일째, 초 행렬, 성탄 절기의 끝 — 브리태니커·FAU', 'pick': 1, 'see': '넷째 장면의 피라미드 밀기가 기다림의 첫 신호로 보여요.'},
  {'x': 'whim', 'q': '권양기 집 고깔 지붕 밑에서 말이 돌았어?', 'at': '악마의 대변인 · C(말도 축도 안 보임), E(광산의 권양기에서 길 잃음) · 꾸러미 1', 'a': '말이나 소가 원을 돎, 거친 날씨에 지붕, 1902년까지 — museum-digital 34397', 'see': '고깔 지붕 집이 권양기의 겉옷으로 보여요.'},
  {'x': 'name', 'q': '이게 왜 피라미드야? 페레메트는?', 'at': '악마의 대변인 · B1, A6·A18 · 꾸러미 1(‘기록마다 다른 점’과 겹침 — 줄일 때 하나로)', 'a': '작아지는 판을 쌓은 모양, 1790년 무렵 이름 없음, 나폴레옹 원정 소식 — TU 켐니츠·evangelisch.de 2009', 'see': '페레메트가 이집트 소식의 산골 말로 보여요.'},
  {'x': 'tree', 'q': '장식이야, 트리 같은 거야?', 'at': '악마의 대변인 · B2 · ‘알고 보면’의 빛 틀을 옮김 · 꾸러미 1', 'a': '교회의 빛 틀 → 도시는 트리, 에르츠산맥은 틀 안을 꾸밈, 트리 대신 — evangelisch.de 2009·독일 성탄 박물관', 'see': '앞면의 탑이 트리의 형제로 보여요.'},
  {'x': 'daylight', 'q': '해를 거의 못 보는 광부들이 왜 불빛만 만들었어?', 'at': '악마의 대변인 · B8, G · 꾸러미 1', 'a': '햇빛 그리움(2009) ↔ 경건한 전설·잔치의 조명(2025, 옌첸) — 자료마다 다름', 'see': '촛대 상자의 불빛이 두 이야기 사이에 보여요.'},
  {'x': 'push', 'q': '피라미드 밀기 날엔 진짜 손으로 밀어? 크라우스 것도 촛불로 돌아? 바람 불면?', 'at': '악마의 대변인 · B5·B6, A17(‘밀기’와 앞면 물음이 부딪힘) · 꾸러미 1', 'a': '큰 피라미드는 전기, 상징으로 밈, ‘하우 루크’ 세 번, 2026년 11월 26일 — dpa 2026(바람은 답을 못 찾음)', 'see': '큰 피라미드가 마을의 “영차!”에 도는 탑으로 보여요.'},
  {'x': 'angel', 'q': '초 든 천사와 광부는 왜 짝이야?', 'at': '창 · 장면 2 고르기에서, D(천사·광부 인형 사진이 없어 고를 기준이 없음) · 꾸러미 1', 'a': '하늘과 땅, 1520년 그림, 하녀마다 천사·젊은 일꾼마다 광부 — TU 켐니츠 1997', 'see': '촛불 천사와 광부가 하늘과 땅의 한 쌍으로 보여요.'},
  {'x': 'tallest', 'q': '가장 큰 피라미드는?', 'at': '창 · 꾸러미 2', 'a': '요한게오르겐슈타트 25.52m, 드레스덴 1997년부터 14.61m — dpa 2026', 'see': '권양기 집 마을이 가장 큰 피라미드의 마을로 보여요.'},
  {'x': 'apron', 'q': '천사가 앞치마? 광부 아내?', 'at': '창 · 꾸러미 2(angel에서 이어짐)', 'a': '앞치마로 땅의 아가씨, 합리주의 해석 vs 신앙에서 온 천사, 뉘른베르크 금박 천사 — TU 켐니츠·프리치 1959·브라우크뮐러 1999', 'see': '촛불 천사가 하늘과 땅 사이의 인형으로 보여요.'},
  {'x': 'seyffert', 'q': '‘광부의 공예’ 이야기는 누가 키웠어?', 'at': '창 · 꾸러미 2(daylight에서 이어짐)', 'a': '자이페르트가 장난감을 ‘민속 예술’로, “도는 피라미드를 만들어 보라” — epd 2025', 'see': '렌츠의 피라미드가 이름보다 먼저 있던 물건으로 보여요(약해요).'},
  {'x': 'gerlach', 'q': '다친 광부는 어떻게 살았어?', 'at': '창 · 꾸러미 2(D에서 마음이 움직인 곳: 사람의 장면)', 'a': '게를라흐(1841~), 32살 사고, 다친 광산의 모형, 일흔에 드레스덴 장터 — 브라우크뮐러 1999', 'see': '첫 장면의 광산이 등에 실린 작은 세상으로 보여요.'},
  {'x': 'stollen', 'q': '가난한 광부들의 성탄 잔치는?', 'at': '창 · 꾸러미 2', 'a': '슈네베르크 광부들이 세 거룩한 저녁의 싼 슈톨렌을 얻어 냄, 1665년 부활절·성령강림절 청원 실패 — 지버 1959', 'see': '둘째 장면의 광부들이 빵 한 조각을 지켜 낸 사람들로 보여요.'},
  {'x': 'parade', 'q': '맨 아래층 인형들은 군인처럼 행진하던데, 진짜 광부들도 그랬어?', 'at': '악마의 대변인 · B12·B13, C(높은 모자·깃발·나팔) · 꾸러미 2', 'a': '사진 설명엔 누군지 없음, 렌츠 맨 아래층은 광부 행렬, 새벽 5시 성탄 미사·외슈타트 행렬 — 위키미디어·museum-digital 206·지버 1959', 'see': '맨 아래층 행렬이 성탄 새벽의 광부들로 보여요.'},
  {'x': 'adam', 'q': '맨 위층 나무·사슴·두 사람은 무슨 장면이야? 사과야?', 'at': '악마의 대변인 · C(맨 위층) · 꾸러미 2(누구인지는 사진 설명에 없어 ‘떠올리게 해요’로만)', 'a': '12월 24일 첫 부부를 기억, 낙원 연극과 사과 단 나무, 북독일 트리의 아담과 하와 — evangelisch.de 2021·2009', 'see': '맨 위층의 작은 숲이 성탄 전날의 낙원으로 보여요.'},
  {'x': 'berg', 'q': '피라미드 말고 움직이는 장식은?', 'at': '창 · 꾸러미 3', 'a': '‘성탄 산’, 1786년 요한게오르겐슈타트 손잡이 광산 — 지버 1952', 'see': '층층 무대가 성탄 산과 닮아 보여요.'},
  {'x': 'paraffin', 'q': '등잔에서 초로 바뀐 건 언제?', 'at': '창 · ‘알고 보면’의 ‘초가 싸지자’를 옮기며 고침(파라핀은 1830년엔 너도밤나무 타르에서 · 검수 4) · 꾸러미 3', 'a': '1830년 파라핀(라이헨바흐, 너도밤나무 타르), 1852년 아들의 공장 제조법 — evangelisch.de 2009·GDCh 1993·라이헨바흐 1852', 'see': '유채 기름 등잔이 값싼 초 이전의 불빛으로 보여요.'},
  {'x': 'spider', 'q': '땅속에서도 성탄 장식을 했어? 무슨 노래 불렀어?', 'at': '악마의 대변인 · B9(노래는 답을 못 찾음) · 꾸러미 3', 'a': '광산 성탄, 오르간과 기도, 광부들이 낸 초, 갱도 천장의 촛대 거미 — 지버 1959', 'see': '둘러앉은 광부들이 촛불 아래 있는 사람들로 보여요.'},
  {'x': 'funeral', 'q': '피라미드 모양 촛대는 처음부터 성탄용?', 'at': '창 · ‘알고 보면’의 ‘첫 피라미드’를 옮김 · 꾸러미 3', 'a': '16세기 보헤미아의 장례 틀, 18세기 교회 장식, 베를린 장대 피라미드 1800년 — 독일 성탄 박물관', 'see': '촛대 탑이 슬픔에서 기쁨의 자리로 옮겨 온 모양으로 보여요.'},
  {'q': '피라미드가 처음 기록된 해는?', 'at': '창 · ‘기록마다 다른 점’에 녹임(1716년 연대기 ↔ 1790년 무렵)', 'a': 'TU 켐니츠 1997 · evangelisch.de 2009', 'see': '(녹임)'},
  {'q': '렌츠는 누구야? 렌츠 피라미드의 진짜 사진은?', 'at': '악마의 대변인 · B10 · 답을 찾지 못한 물음(박물관 기록은 ‘한 주인의 이름’까지만, 사진은 쓸 수 있는 것을 못 찾음)', 'a': '', 'see': ''},
  {'q': '그 오래된 피라미드, 지금도 등잔을 켜면 돌아? 박물관에서 도는 걸 볼 수 있어?', 'at': '악마의 대변인 · B11 · 답을 찾지 못한 물음', 'a': '', 'see': ''},
  {'q': '날개 왼쪽에 하얗게 빛나는 동그란 불은 뭐야?', 'at': '악마의 대변인 · C(앞면 사진) · 답을 찾지 못한 물음(박물관 조명으로 보이지만 근거 없음)', 'a': '', 'see': ''},
  {'q': '크라우스 피라미드 층마다 종이 있던데 소리가 나? 울타리는 왜?', 'at': '악마의 대변인 · C(크라우스) · 답을 찾지 못한 물음', 'a': '', 'see': ''},
  {'q': '지금도 팔아? 한국에서도 살 수 있어?', 'at': '악마의 대변인 · B15 · 다루지 않음(물건 사기 안내는 카드의 일이 아님)', 'a': '', 'see': ''},
 ],
 'deep': [
  {'h': '기록마다 다른 점', 'p': [
    '<b>가장 오래된 피라미드의 나이</b> 독일 성탄 박물관은 렌츠의 피라미드를 1800년 무렵 것으로, 이 피라미드를 가진 안나베르크 박물관의 기록은 1810년 무렵으로 적었어요.',
    '<b>권양기를 본떴을까</b> 지버(1959)는 피라미드가 옛 광산의 권양기를 본뜬 것이라고 적었어요. 다른 글은 모양이 권양기를 떠올리게 했을 거라고만 말해요. 따뜻한 공기로 도는 장치까지 권양기에서 왔는지는 확실하지 않아요.',
    '<b>처음 기록된 피라미드</b> TU 켐니츠 대학의 대림절 글(1997)은 1716년 에르츠산맥의 한 연대기에 젊은이들이 불빛만으로 만든 피라미드를 세웠다는 기록이 처음 나온다고 적었어요. 한 개신교 매체(2009)는 성탄 인형을 올린 피라미드가 1790년 무렵부터 나타났다고 해요.',
    '<b>‘피라미드’라는 이름</b> 한 개신교 매체는 나폴레옹의 이집트 원정(1798~1801) 소식이 전해진 뒤 이 말이 이 고장 사투리 ‘페레메트’로 자리 잡았다고 소개해요.']},
  {'h': '직접 가 보기', 'img': ['wing'], 'checked': '2026년 11월 18일', 'p': [
    '렌츠의 피라미드는 안나베르크부흐홀츠의 에르츠산맥 박물관에 있어요. 박물관 마당에서 16세기 초의 옛 은광 ‘임 괴스너’로 내려갈 수 있어요. 여는 때는 미리 확인해 주세요.',
    '대림절 첫 주일 무렵 에르츠산맥 마을들이 ‘피라미드 밀기’를 해요. 마을마다 날이 조금씩 다르니 관광 협회 일정표를 보세요.'],
   'links': [{'t': '안나베르크부흐홀츠시: 에르츠산맥 박물관', 'u': 'https://www.annaberg-buchholz.de/de/kultur/erzgebirgsmuseum.php', 'm': '독일어'},
             {'t': '에르츠산맥 관광 협회: 성탄 철 안내', 'u': 'https://www.erzgebirge-tourismus.de/weihnachtszeit/', 'm': '독일어'}]},
 ],
 'src': [
  {'l': '(열쇠 물음) 독일 성탄 박물관: 피라미드 — 판 바깥의 초꽂이, 더운 공기가 날개와 판을 돌림, 축의 뾰족한 아래 끝과 오목한 자리 · TU 켐니츠(1997): 초에서 올라온 공기가 맨 위 날개바퀴를 돌림', 'u': XMUS},
  {'l': '(열쇠 물음) 하이데 브라우크뮐러, 「광부에서 장난감 장인으로」, 『데어 안슈니트』 1999년 5·6호 — 17세기에 좋은 광맥이 바닥남, 가문비나무, 선반공 1670년 무렵 23명·백 년 뒤 100명', 'u': BRAUK},
  {'l': '(열쇠 물음) 브리태니커: 대림절 — 라틴어 ‘오심’, 성탄을 준비하는 때, 11월 30일에 가장 가까운 일요일에 시작 · dpa(2026.11.19): 2026년 첫 대림절 앞 행사들', 'u': ADVENT},
  {'l': '(열쇠 물음) 에를랑겐뉘른베르크 대학(FAU) 누리집 자료: 주님 봉헌 축일(2월 2일) — 성탄 40일째, 대부분의 교회에서 성탄 절기가 끝남, 초를 들고 걷던 행렬과 ‘리히트메스’라는 이름', 'u': FAU},
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
             {'t': '이런 고깔 지붕 아래에서 말이 원을 그리며 걸었어요.'},
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
             {'t': '맨 아래 광부 행렬,', 'act': 'parade'}, {'t': '그 위에 아기 예수 탄생과 동방박사·목자들,', 'act': 'nativity'},
             {'t': '셋째 층에 낙타와 동물들,', 'act': 'animals'}, {'t': '맨 위에는 천사들.', 'act': 'angels'},
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
