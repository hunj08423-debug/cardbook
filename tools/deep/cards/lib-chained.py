# -*- coding: utf-8 -*-
"""깊은 카드: 사슬에 묶인 책(lib-chained) · 중심 방식 = 놓아 보기(도우미: 그때와 지금 탭)
기준서 1판(보탬 10) · 틀 deep3-4 · 키트 3판 · 2026-11-18 37번 묶음 창이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 1611년, 헤리퍼드 대성당 성모 경당에 새 책장이 들어서고
     책마다 사슬이 걸리던 때.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 책 한 권을 책장에 거는 쇠붙이(책·사슬·쇠막대·자물쇠)와
     책상. 1901년 J. W. 클라크가 헤리퍼드 책장을 살펴 적은 그대로, 책 → 사슬 → 쇠막대 → 자물쇠 → 책상 차례로 놓아요.
재벌(더 깊이: 열쇠 셋 · 뒷이야기 15) 2026-11-22 37번 묶음 재벌 창.
카드 크기: 큰 카드(장면 4) — 대성당·재단 누리집, 1901년 클라크의 기록, 옛 엽서와 오늘 사진이 넉넉해요.
책장 무대는 이 안내서가 코드로 그렸어요(stage_svg). 그림 원본(src)은 deep_src/lib-chained/ (저장소 밖)."""
import random

S = 'lib-chained/'
MAPPA = 'https://themappamundi.co.uk/chained-library'
TRUST = 'https://themappamundi.co.uk/about-the-trust.php'
VISIT = 'https://themappamundi.co.uk/visit.php'
HCATH = 'https://www.herefordcathedral.org/chained-library'
CLARK = 'https://www.gutenberg.org/ebooks/26378'
CLARKT = 'https://www.gutenberg.org/files/26378/26378.txt'
SPECT = 'https://archive.spectator.co.uk/article/16th-july-1932/24/books-in-chains'
MAPW = 'https://themappamundi.co.uk/mappa-mundi/'
CABINET = 'https://www.cabinet.ox.ac.uk/node/7669'
GUIN = 'https://www.guinnessworldrecords.com/world-records/606607-largest-surviving-medieval-world-map'
HL88 = 'https://api.parliament.uk/historic-hansard/lords/1988/dec/06/the-mappa-mundi'
HC89 = 'https://api.parliament.uk/historic-hansard/written-answers/1989/mar/20/mappa-mundi'
NHMF = 'https://www.nhmf.org.uk/print/pdf/node/891'
CUPS = 'https://www.cambridge.org/core/books/the-chained-library/C67B27FFA8A13CD93F5A5C5B46742056'
FOURG = 'https://onlinebooks.library.upenn.edu/webbin/who/Streeter%2c%20Burnett%20Hillman%2c%201874%2d1937'
UVIC = 'https://mapoflondon.uvic.ca/CHUR8.htm'
NGETTY = 'https://nationalgallery.org.uk/about-us/history/collectors-and-benefactors/sir-paul-getty'
ITGETTY = 'https://www.irishtimes.com/news/benevolent-squire-tormented-by-oil-dynasty-s-vast-wealth-1.356298'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'


def bl(code, label):
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'


def stage_svg():
    """헤리퍼드 사슬 책장 무대. 클라크(1901)의 기록과 대성당 누리집 설명을 바탕으로 이 안내서가 그림.
    선반 셋 · 책은 종이 끝(책 배)이 밖을 보게 · 앞표지 놋쇠 띠와 고리 · 늘어진 사슬 · 선반 아래 쇠막대 ·
    책장 끝 쇠판과 걸쇠·자물쇠 · 앞 책상에 펼친 책(사슬이 책장까지 이어짐)."""
    R = random.Random(1611)
    f = lambda v: ('%.1f' % v).rstrip('0').rstrip('.')
    shelves = [(50, 118), (128, 206), (216, 294)]      # (책 윗면 한계, 선반 판 윗면)
    x0, x1, slot = 200, 600, (384, 406)                  # slot: 아래 칸에서 책상으로 내려온 책 자리(비워 둠)
    PAL = ['#bfae86', '#b3a07a', '#c8b68f', '#a99671', '#bba984', '#c4b18a']
    pages, lb, rb, ln, st, brass, ring1, chain, ring2 = ([] for _ in range(9))
    for si, (yt, yb) in enumerate(shelves):
        rod, x = yb - 6, x0
        while x < x1 - 10:
            w = R.choice([13, 14, 15, 16, 17, 18, 19, 20, 22, 24])
            if x + w > x1: w = x1 - x
            if si == 2 and x + w > slot[0] and x < slot[1]:
                x = slot[1] + 1
                continue
            h = R.uniform(.68, .96) * (yb - yt)
            y = yb - h
            pages.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{R.choice(PAL)}"/>')
            lb.append(f'<rect x="{f(x)}" y="{f(y)}" width="2.6" height="{f(h)}"/>')
            rb.append(f'<rect x="{f(x + w - 2.4)}" y="{f(y)}" width="2.4" height="{f(h)}"/>')
            ly = R.uniform(y + 6, yb - 6)
            ln.append(f'<line x1="{f(x + 3)}" y1="{f(ly)}" x2="{f(x + w - 3)}" y2="{f(ly)}"/>')
            if R.random() < .3:
                st.append(f'<rect x="{f(x + 1)}" y="{f(y + h * R.uniform(.22, .45))}" width="{f(w - 2)}" height="3.2"/>')
            ay, ax = y + h * R.uniform(.55, .8), x + 1.3
            bx = x + R.uniform(3, w - 3)
            sag = R.uniform(16, 44) if si < 2 else R.uniform(10, 26)
            brass.append(f'<rect x="{f(x - .6)}" y="{f(ay - 3)}" width="3.8" height="6.5"/>')
            ring1.append(f'<circle cx="{f(ax)}" cy="{f(ay + 4.5)}" r="1.9"/>')
            chain.append(f'<path d="M{f(ax)} {f(ay + 6.4)}C{f(ax - 1.5)} {f(rod + sag)} {f(bx + 1.5)} {f(rod + sag)} {f(bx)} {f(rod + 2.4)}"/>')
            ring2.append(f'<circle cx="{f(bx)}" cy="{rod}" r="2.6"/>')
            x += w + R.choice([.6, .8, 1, 1.2])
    shade = ''.join(f'<rect x="196" y="{yt - 2}" width="408" height="{yb - yt + 2}" fill="url(#__U__shade)"/>' for yt, yb in shelves)
    books = (f'<g>{"".join(pages)}</g><g fill="#5a3a22">{"".join(lb)}</g><g fill="#4a2f1b">{"".join(rb)}</g>'
             f'<g stroke="#8f7d58" stroke-width=".5" opacity=".55">{"".join(ln)}</g><g fill="#6b5130">{"".join(st)}</g>{shade}')
    chains = (f'<g fill="#b8913f">{"".join(brass)}</g><g fill="none" stroke="#aab0b6" stroke-width="1">{"".join(ring1)}</g>'
              f'<g fill="none" stroke="#7f878d" stroke-width="1.35" stroke-dasharray="1.9 1.1" stroke-linecap="round">{"".join(chain)}</g>'
              f'<g fill="none" stroke="#b3b9be" stroke-width="1.2">{"".join(ring2)}</g>')
    rods = ''.join(f'<rect x="187" y="{yb - 10}" width="10" height="8" rx="1.5" fill="#3a3e42" stroke="#6a7177" stroke-width=".8"/>'
                   f'<line x1="192" y1="{yb - 6}" x2="620" y2="{yb - 6}" stroke="#5b6167" stroke-width="3.4" stroke-linecap="round"/>'
                   f'<line x1="192" y1="{yb - 7}" x2="620" y2="{yb - 7}" stroke="#a3aab0" stroke-width=".8" opacity=".8"/>' for _, yb in shelves)
    lock = ('<rect x="609" y="64" width="30" height="236" rx="2" fill="#2d3135" stroke="#6c7379" stroke-width="1.2"/>'
            '<g fill="#8d949a">' + ''.join(f'<circle cx="{cx}" cy="{cy}" r="1.7"/>' for cx, cy in [(614, 70), (634, 70), (614, 294), (634, 294), (614, 160), (634, 160)]) + '</g>'
            + ''.join(f'<circle cx="624" cy="{yb - 6}" r="4" fill="#4b5157" stroke="#8d949a" stroke-width=".8"/>' for _, yb in shelves)
            + '<circle cx="624" cy="78" r="4.2" fill="#3a3f44" stroke="#9aa1a7" stroke-width="1"/>'
            '<rect x="618.5" y="78" width="11" height="140" rx="2" fill="#3c4146" stroke="#8a9197" stroke-width="1"/>'
            '<rect x="611" y="214" width="26" height="32" rx="3" fill="#24272a" stroke="#9aa1a7" stroke-width="1.2"/>'
            '<circle cx="624" cy="226" r="2.8" fill="#0b0b0b"/><rect x="623" y="226" width="2" height="9" fill="#0b0b0b"/>')
    sc = (slot[0] + slot[1]) / 2
    read = ('<path d="M336 335 L396 330 L396 352 L330 357Z" fill="#5a3a22"/><path d="M398 330 L458 335 L464 357 L398 352Z" fill="#4a2f1b"/>'
            '<path d="M340 333 L395 328.5 L395 349.5 L335 354Z" fill="#ecdfc2" stroke="#b9a77f" stroke-width=".6"/>'
            '<path d="M399 328.5 L454 333 L459 354 L399 349.5Z" fill="#e6d8b8" stroke="#b9a77f" stroke-width=".6"/>'
            '<g stroke="#6e5c3e" stroke-width=".7" opacity=".55">'
            + ''.join(f'<line x1="{f(344 + k * .45)}" y1="{f(335 + k * 3.1)}" x2="390" y2="{f(331.5 + k * 3.1)}"/>' for k in range(6))
            + ''.join(f'<line x1="404" y1="{f(331.5 + k * 3.1)}" x2="{f(449 + k * .45)}" y2="{f(335 + k * 3.1)}"/>' for k in range(6)) + '</g>'
            + f'<path d="M334 349 C318 318 372 300 {f(sc)} 290.4" fill="none" stroke="#7f878d" stroke-width="1.35" stroke-dasharray="1.9 1.1" stroke-linecap="round"/>'
            '<rect x="331.5" y="344" width="5" height="9" fill="#b8913f"/>'
            f'<circle cx="{f(sc)}" cy="288" r="2.6" fill="none" stroke="#b3b9be" stroke-width="1.2"/>')
    joints = ''
    for k, y in enumerate(range(18, 430, 34)):
        joints += f'<line x1="0" y1="{y}" x2="800" y2="{y}"/>' + ''.join(f'<line x1="{xx}" y1="{y}" x2="{xx}" y2="{y + 34}"/>' for xx in range(0 if k % 2 else 40, 800, 80))
    win = ''
    for a, b in [(36, 96), (704, 764)]:
        p, m = f'M{a} 330 V112 Q{a} 56 {(a + b) // 2} 40 Q{b} 56 {b} 112 V330Z', (a + b) // 2
        win += (f'<path d="{p}" fill="url(#__U__glass)" stroke="#2a221b" stroke-width="5"/><path class="sky2" d="{p}" fill="url(#__U__glass2)"/>'
                f'<g stroke="#2a221b" stroke-width="1.6">' + ''.join(f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y}"/>' for y in range(120, 330, 42))
                + f'<line x1="{m}" y1="44" x2="{m}" y2="330" stroke-width="2"/></g>')
    shelfboards = ''.join(f'<rect x="196" y="{yb}" width="408" height="8" fill="#4a311c"/><line x1="196" y1="{yb + 8}" x2="604" y2="{yb + 8}" stroke="#2a1b0f" stroke-width="1.2"/>' for _, yb in shelves)
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="돌벽과 높은 창 사이에 선 빈 나무 책장과 그 앞 책상. 놓은 것들이 책장에 하나씩 나타난다."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1511"/><stop offset="1" stop-color="#0d0a08"/></linearGradient>
<linearGradient id="__U__glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a3a52"/><stop offset="1" stop-color="#151d2b"/></linearGradient>
<linearGradient id="__U__glass2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1dfb4"/><stop offset="1" stop-color="#c9a970"/></linearGradient>
<linearGradient id="__U__wood" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3a2616"/><stop offset=".5" stop-color="#4d331e"/><stop offset="1" stop-color="#352213"/></linearGradient>
<linearGradient id="__U__shade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".5"/><stop offset=".35" stop-color="#000" stop-opacity=".12"/><stop offset=".8" stop-color="#000" stop-opacity=".08"/><stop offset="1" stop-color="#000" stop-opacity=".35"/></linearGradient>
<radialGradient id="__U__pool" cx=".5" cy=".6" r=".6"><stop offset="0" stop-color="#ffe2a8" stop-opacity=".26"/><stop offset=".6" stop-color="#f0b766" stop-opacity=".08"/><stop offset="1" stop-color="#f0b766" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".42" r=".8"><stop offset="0" stop-color="#fff3d6" stop-opacity=".2"/><stop offset=".6" stop-color="#ffd99a" stop-opacity=".08"/><stop offset="1" stop-color="#ffd99a" stop-opacity="0"/></radialGradient></defs>
<rect width="800" height="450" fill="url(#__U__wall)"/><g stroke="#241d17" stroke-width="1" opacity=".75">{joints}</g>{win}
<rect x="0" y="420" width="800" height="30" fill="#0a0807"/>
<rect x="196" y="46" width="408" height="262" fill="#1b130c"/>
<rect x="160" y="20" width="494" height="12" fill="#56391f"/><rect x="166" y="32" width="482" height="16" fill="#3d2817"/><line x1="166" y1="47" x2="648" y2="47" stroke="#6b4a2b" stroke-width="1"/>
<rect x="170" y="32" width="26" height="290" fill="url(#__U__wood)"/><rect x="604" y="32" width="40" height="290" fill="url(#__U__wood)"/>{shelfboards}
<rect x="166" y="302" width="482" height="20" fill="#2e1e11"/>
<path d="M186 326 L614 326 L634 354 L166 354Z" fill="#4b321d"/><rect x="166" y="354" width="468" height="6" fill="#2b1c10"/>
<rect x="196" y="360" width="10" height="56" fill="#24170d"/><rect x="594" y="360" width="10" height="56" fill="#24170d"/>
<rect x="146" y="398" width="508" height="10" rx="2" fill="#3b2717"/><rect x="156" y="408" width="8" height="14" fill="#24170d"/><rect x="636" y="408" width="8" height="14" fill="#24170d"/>
<ellipse class="glow" cx="400" cy="300" rx="300" ry="170" fill="url(#__U__pool)" opacity=".14"/>
<g class="obj" data-o="book">{books}</g>
<g class="obj" data-o="chain">{chains}</g>
<g class="obj" data-o="rod">{rods}</g>
<g class="obj" data-o="lock">{lock}</g>
<g class="obj" data-o="read">{read}</g>
<g class="day"><path d="M96 120 L96 330 L420 450 L300 450Z" fill="#ffe9bd" opacity=".05"/><path d="M704 120 L704 330 L470 450 L560 450Z" fill="#ffe9bd" opacity=".04"/><rect width="800" height="450" fill="url(#__U__day)"/></g>
</svg>'''


ITEMS = [
 {'id': 'book', 't': '책', 'la': 'fore-edge outwards',
  'say': '책을 꽂아요. 책등이 아니라 종이 끝(책 배)이 밖을 보게요. 그래야 앞표지에 단 사슬이 앞으로 나와요.'},
 {'id': 'chain', 't': '사슬', 'la': 'chain',
  'say': '앞표지에 얇은 놋쇠 띠를 감아 박고, 거기 달린 쇠고리에 사슬 한쪽 끝을 걸어요. 사슬은 두드려 만든 쇠고리를 길게 이은 거예요.'},
 {'id': 'rod', 't': '쇠막대', 'la': 'iron bar',
  'say': '사슬 다른 끝의 조금 더 큰 고리를 선반 아래쪽 쇠막대에 꿰어요. 고리는 막대를 따라 미끄러져요.'},
 {'id': 'lock', 't': '자물쇠', 'la': 'hasp and lock',
  'say': '책장 끝 쇠판에 달린 걸쇠를 내려 막대 끝을 덮고, 자물쇠를 채워요. 열쇠가 없으면 막대를 빼낼 수 없으니, 책도 빠지지 않아요.'},
 {'id': 'read', 't': '책상', 'la': 'desk',
  'say': '이제 책을 꺼내 앞 책상에 펼쳐요. 사슬이 닿는 데까지, 책은 책장 앞을 떠나지 않아요.'},
]

CARD = {
 'id': 'lib-chained', 'mode': '놓아 보기 · 그때와 지금',
 'pagetitle': '헤리퍼드의 사슬 책장',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>1611년</b><span>영국 헤리퍼드 대성당 · 성모 경당</span>',
 'lead': '1611년, 영국 헤리퍼드 대성당의 성모 경당에 새 책장이 들어섰어요. 책마다 사슬을 달아 책장에 걸었지요. 1901년 한 학자가 적어 둔 그대로, 책 한 권을 사슬로 책장에 걸어 보세요.',
 'leadKid': '옛날 영국의 큰 교회에서는 책을 쇠사슬로 책장에 묶어 두었대. 우리도 책 한 권을 사슬로 걸어 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 1판). 장면에는 헤리퍼드 대성당과 마파 문디 재단의 누리집, 그리고 1901년 J. W. 클라크가 헤리퍼드 책장을 살펴 적은 책에 있는 것만 옮겼어요. 책장 무대는 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 # 화면 색: 4장 색을 바탕으로, 오래된 참나무 책장의 갈색으로 맞췄어요.
 'theme': """:root{--accent:#7a5230;--accent-ink:#fffaf3;--soft:rgba(122,82,48,.09);--stamp:#a8392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#d4a878;--accent-ink:#1a120a;--soft:rgba(212,168,120,.10);--stamp:#e46e5c}}
:root[data-theme="dark"]{--accent:#d4a878;--accent-ink:#1a120a;--soft:rgba(212,168,120,.10);--stamp:#e46e5c}""",
 'stamp': {'t': '사슬', 'y': '1611', 'sub': '헤리퍼드 · 영국'},
 'doneNote': '헤리퍼드에 가면, 선반 아래 쇠막대와 책장 끝 쇠판의 자물쇠를 찾아보세요.',
 'images': {
  'chains': {'src': S + '2017-10-04_Chained_Library_Hereford.jpg',
             'cap': '헤리퍼드 대성당 사슬 도서관, 2017년',
             'cr': '사진: John Lord · CC BY 2.0 · 위키미디어 공용',
             'u': 'https://commons.wikimedia.org/wiki/File:2017-10-04_Chained_Library,_Hereford.jpg',
             'alt': '나무 선반에 옛 책들이 종이 끝을 앞으로 하고 빽빽이 꽂혀 있다. 책 표지 가장자리의 쇠고리마다 쇠사슬이 길게 늘어지고, 선반 앞을 가로지르는 쇠막대에 사슬 끝 고리가 줄지어 걸려 있다. 아래 칸 몇몇 책에는 흰 끈이 매여 있다.'},
  'clasp': {'src': S + 'Hereford_Cathedral_s_Chained_Library_-_geograph.org.uk_-_8179957.jpg',
            'cap': '사슬 달린 책들, 2025년',
            'cr': '사진: Philip Halling · CC BY-SA 2.0 · 위키미디어 공용(geograph.org.uk)',
            'u': 'https://commons.wikimedia.org/wiki/File:Hereford_Cathedral%27s_Chained_Library_-_geograph.org.uk_-_8179957.jpg',
            'alt': '종이 끝이 누렇게 바랜 두꺼운 옛 책들이 나란히 서 있다. 표지 가장자리에 쇠 장식이 박혀 있고, 그 앞으로 쇠사슬 여러 가닥이 커튼처럼 늘어져 선반 앞 쇠막대의 고리로 이어진다.'},
  'postcard': {'src': S + 'Postcard_of_The_Chained_Library._Hereford_Cathedral_undated.jpg', 'crop': [0.056, 0.038, 0.872, 0.959],
               'cap': '그림엽서 「헤리퍼드 대성당 사슬 도서관」, 찍은 해 모름',
               'cr': '엽서: Waterlow & Sons 인쇄 · 퍼블릭 도메인 · 위키미디어 공용',
               'u': 'https://commons.wikimedia.org/wiki/File:Postcard_of_The_Chained_Library._Hereford_Cathedral_(undated).jpg',
               'alt': '흑백 사진. 나무 들보 천장 아래 높은 책장들이 줄지어 서 있고, 선반마다 사슬이 늘어진 책이 빽빽하다. 책장 앞마다 책상과 나무 의자가 붙어 있고, 오른쪽 책장 끝에는 네모난 액자와 쇠판이 달려 있다.'},
  'lib2025': {'src': S + 'The_Chained_Library_Hereford_Cathedral_-_geograph.org.uk_-_8173040.jpg', 'crop': [0.045, 0.0, 0.955, 1.0],
              'cap': '1996년에 지은 새 도서관 건물 안의 사슬 도서관, 2025년',
              'cr': '사진: Stuart Wilding · CC BY-SA 2.0 · 위키미디어 공용(geograph.org.uk)',
              'u': 'https://commons.wikimedia.org/wiki/File:The_Chained_Library,_Hereford_Cathedral_-_geograph.org.uk_-_8173040.jpg',
              'alt': '아치 창으로 빛이 드는 방에 짙은 나무 책장들이 서 있다. 선반마다 옛 책이 종이 끝을 앞으로 하고 꽂혀 있고, 쇠사슬이 커튼처럼 드리워 있다. 앞 책상에는 설명 종이가 놓여 있고, 왼쪽 책장 끝에는 글씨 액자가 걸려 있다.'},
  'mappa': {'src': S + 'Hereford-Karte.jpg',
            'cap': '헤리퍼드 마파 문디, 1300년 무렵 · 팔릴 뻔했던 세계 지도',
            'cr': '지도: 만든 이 모름 · 퍼블릭 도메인 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Hereford-Karte.jpg',
            'alt': '꼭대기가 뾰족한 큰 양피지에 둥근 세계가 그려져 있다. 검푸른 물줄기와 바다가 땅을 가르고, 그 사이에 작은 성과 그림, 글씨가 빼곡하다. 오른쪽 위에 붉게 칠한 물줄기가 보이고, 맨 꼭대기 삼각형 안에는 앉은 인물이 그려져 있다.'},
  'pframe': {'src': S + 'Postcard_of_The_Chained_Library._Hereford_Cathedral_undated.jpg', 'crop': [0.49, 0.18, 0.80, 0.72],
             'cap': '옛 그림엽서의 부분 · 책장 끝의 목록 액자와 자물쇠 쇠판',
             'cr': '엽서: Waterlow & Sons 인쇄 · 퍼블릭 도메인 · 위키미디어 공용',
             'u': 'https://commons.wikimedia.org/wiki/File:Postcard_of_The_Chained_Library._Hereford_Cathedral_(undated).jpg',
             'alt': '흑백 엽서의 부분. 왼쪽 책장 꼭대기에 ‘Classis Secunda’라는 글씨 판이 있고, 오른쪽 책장 끝에는 세모 지붕을 얹은 액자 안에 글씨가 빼곡한 두 칸 판이 걸려 있다. 그 아래에 열쇠 구멍과 걸쇠가 달린 쇠판 두 개가 박혀 있다.'},
  'mtop': {'src': S + 'Hereford-Karte.jpg', 'crop': [0.30, 0.00, 0.70, 0.22], 'max': 1600,
           'cap': '마파 문디의 부분 · 꼭대기',
           'cr': '지도: 만든 이 모름 · 퍼블릭 도메인 · 위키미디어 공용',
           'u': 'https://commons.wikimedia.org/wiki/File:Hereford-Karte.jpg',
           'alt': '지도 꼭대기의 뾰족한 칸. 가운데에 두 팔을 든 인물이 앉아 있고, 양옆으로 천사들과 작은 사람들이 늘어서 있다. 그 아래 둥근 세상 테두리 바로 안쪽에 성벽으로 두른 동그란 섬이 있다.'},
  'mjeru': {'src': S + 'Hereford-Karte.jpg', 'crop': [0.38, 0.45, 0.64, 0.66], 'max': 1600,
            'cap': '마파 문디의 부분 · 한가운데',
            'cr': '지도: 만든 이 모름 · 퍼블릭 도메인 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Hereford-Karte.jpg',
            'alt': '지도 한가운데에 톱니 같은 성벽으로 두른 동그란 도시가 있고, 그 위에 십자가에 달린 사람이 작게 그려져 있다. 둘레에 작은 성과 글씨가 흩어져 있고, 아래쪽으로 검게 변한 물줄기가 가로지른다.'},
  'mred': {'src': S + 'Hereford-Karte.jpg', 'crop': [0.58, 0.22, 0.86, 0.46], 'max': 1600,
           'cap': '마파 문디의 부분 · 붉게 칠한 바다',
           'cr': '지도: 만든 이 모름 · 퍼블릭 도메인 · 위키미디어 공용',
           'u': 'https://commons.wikimedia.org/wiki/File:Hereford-Karte.jpg',
           'alt': '누런 양피지 위에 붉게 칠한 물줄기가 Y자 모양으로 갈라져 있다. 그 둘레로 검은 물줄기와 작은 성, 동물 그림, 빼곡한 글씨가 흩어져 있다.'},
  'mbrit': {'src': S + 'Hereford-Karte.jpg', 'crop': [0.02, 0.66, 0.30, 0.96], 'max': 1600,
            'cap': '마파 문디의 부분 · 왼쪽 아래 끝',
            'cr': '지도: 만든 이 모름 · 퍼블릭 도메인 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Hereford-Karte.jpg',
            'alt': '둥근 세상 테두리 안쪽 왼쪽 아래에, 강줄기가 여러 갈래로 지나는 길쭉한 섬이 있고 작은 성 그림들이 박혀 있다. 테두리 바깥 아래에는 말 탄 사람과 붉은 글씨가 보인다.'},
  'zutphen': {'src': S + 'Overzicht_lectrijnen_kettingbibliotheek_zutphen.jpg',
              'cap': '네덜란드 쥐트펀 성 발푸르가 교회의 사슬 도서관, 2023년',
              'cr': '사진: Mx Lucy · CC BY-SA 4.0 · 위키미디어 공용',
              'u': 'https://commons.wikimedia.org/wiki/File:Overzicht_lectrijnen_kettingbibliotheek_zutphen.jpg',
              'alt': '격자무늬 높은 창 아래, 비스듬한 나무 책상 위에 쇠 장식을 박은 두꺼운 책들이 나란히 눕혀 있다. 책마다 짧은 사슬이 책상 꼭대기를 가로지르는 쇠막대에 이어져 있고, 책상 앞에는 긴 나무 의자가 놓여 있다.'},
 },
 'extra_credits': [{'cr': '책장 무대: 이 안내서가 그린 그림 · J. W. 클라크 『The Care of Books』(1901)의 헤리퍼드 기록과 헤리퍼드 대성당 누리집 설명을 바탕으로', 'u': CLARK}],
 'scenes': [
  {'id': 'rule', 'label': '책을 묶으라는 규칙', 'kind': 'photo', 'img': 'chains',
   'text': ['1583년, 엘리자베스 1세 여왕이 보낸 조사단이 영국 헤리퍼드(Hereford) 대성당을 살폈어요. 조사단은 대성당 도서관이 돌보는 사람 없이 허물어져 가고 있다고 보고했어요.',
            '그러자 새 규칙이 생겼어요. 대성당 일을 맡은 성직자(참사회원) 한 사람을 ‘도서관 책임자’로 세우고, 책을 지키기 위해 사슬로 묶으라는 것이었어요.'],
   'text2': ['1590년, 도서관은 종교개혁 뒤로 쓰지 않던 성모 경당(성모 마리아에게 바친 작은 예배당)으로 옮겨 갔어요. 1611년에는 도서관 책임자 토머스 손턴(Thomas Thornton)이 그곳에 사슬 도서관을 짓게 했어요.',
             '그 무렵 옥스퍼드 대학에 새로 들어선 도서관들을 본떴어요. 나무 책장은 헤리퍼드에서 짰지만, 쇠붙이는 옥스퍼드에서 주문해야 했어요.'],
   'kid': '옛날 영국 헤리퍼드의 큰 교회에서는, 책을 잘 지키려고 쇠사슬로 묶기로 했대.',
   'kidq': '귀한 책을 지키려면, 너라면 어떻게 할래?'},
  {'id': 'press', 'label': '책장에 사슬 걸기', 'kind': 'mod', 'mod': 'place', 'night': False,
   'text': ['1901년, 옛 도서관을 연구하던 영국 케임브리지 대학의 J. W. 클라크(John Willis Clark)가 헤리퍼드의 책장을 꼼꼼히 살펴 그림과 함께 적었어요. 그는 책을 사슬로 묶는 방식을 보여 주는 데 헤리퍼드보다 나은 본보기는 없다고 했어요.',
            '그 기록대로 책 한 권을 책장에 걸어 보세요. 아래에서 하나씩 골라 놓으면 돼요.'],
   'text2': ['책은 책장 앞에 붙은 책상까지 내려와 펼칠 수 있지만, 책장을 떠날 수는 없었어요. 클라크가 잰 사슬은 1m에서 1.3m쯤이었어요. 가운데에는 대개 빙글 도는 고리가 있었는데, 클라크는 사슬이 꼬이지 않게 하려는 것 같다고 보았어요.'],
   'kid': '책을 꽂고, 사슬을 달고, 쇠막대에 꿰고, 자물쇠를 채워 볼까? 마지막엔 책상에 펼쳐 읽어!',
   'kidq': '사슬에 묶인 책은 어디까지 데려갈 수 있을까?'},
  {'id': 'apart', 'label': '흩어졌다 다시 모인 책장', 'kind': 'thennow', 'then': 'postcard', 'now': 'lib2025',
   'thenT': '옛 그림엽서', 'nowT': '2025년',
   'text': ['1841년, 성모 경당을 고치는 공사 때문에 사슬 도서관을 뜯어냈어요. 책에서는 사슬을 떼어 냈고, 책상과 의자는 대성당 여기저기에서 다른 데 쓰였어요.',
            '1897년에는 대성당 회랑(안뜰을 둘러싼 지붕 덮인 복도)에 2층 건물을 새로 이어 짓고, 사슬 없는 도서관을 그 위층에 들였어요.'],
   'text2': ['위 엽서에는 찍은 해가 적혀 있지 않아요. 다만 책마다 사슬이 달려 있으니, 1930년 무렵 사슬을 다시 단 뒤의 모습일 거예요.',
             '그때 스트리터(B. H. Streeter) 참사회원이 성모 경당 때의 모습대로 책장을 되살리고 책에 사슬을 다시 달았어요. 하지만 책장은 문서 보관실과 위층 도서관, 두 곳에 나뉘어 있었어요.',
             '1996년 새 도서관 건물이 문을 열자, 사슬 도서관은 다시 한곳에 모였어요. 새 건물 안에, 1611년부터 1841년까지 성모 경당에 있던 모습 그대로 놓였어요.'],
   'kid': '사슬을 뗐다가, 다시 달았다가, 두 곳에 나뉘었다가… 이제는 한곳에 모였대!',
   'kidq': '옛 엽서랑 오늘 사진에서 똑같은 걸 하나 찾아볼까?'},
  {'id': 'keep', 'label': '팔지 않은 책들', 'kind': 'photo', 'img': 'mappa',
   'text': ['그 새 건물이 서기까지는 큰 고비가 있었어요. 1980년대 끝 무렵, 대성당은 해마다 모자라는 살림으로 큰 어려움을 겪었어요. 적어도 600만 파운드의 기금이 있어야 한다는 조언을 듣고, 가진 것을 팔기로 했어요.',
            '대성당은 사슬 도서관의 귀한 책 여러 권을 골라 파는 대신, 1300년 무렵 송아지 가죽 한 장에 그린 세계 지도 「마파 문디(Mappa Mundi)」를 팔려고 했어요. 귀한 책을 골라 팔면 사슬 도서관이 온전하지 못하게 되기 때문이었어요.'],
   'text2': ['곧바로 걱정하는 목소리가 일었어요. 대성당도, 나라도 귀한 유산을 쉽게 잃을 수 있다는 것이었어요. 국가 유산 기념 기금(National Heritage Memorial Fund)과 존 폴 게티 2세(John Paul Getty Jr.), 그리고 세계 곳곳의 사람들이 힘을 보태 새 재단의 기금을 마련했어요.',
             '지도와 사슬 도서관의 옛 책들은 재단이 맡았어요. 둘을 함께 들일 돌 건물을 새로 지었고, 1996년 5월 엘리자베스 2세 여왕이 문을 열었어요. 지도도, 책도 헤리퍼드에 남았어요.'],
   'kid': '돈이 모자라서 귀한 지도를 팔 뻔했대. 책들을 흩어지지 않게 하려고! 그런데 많은 사람이 도와서 지도도 책도 지켰어.',
   'kidq': '많은 사람이 조금씩 도와서 지켰대. 우리가 함께 지키는 건 뭐가 있을까?'},
 ],
 'imagine': {'t': '돌벽에 기댄 나무 책장 앞, 긴 의자에 앉아요. 책을 당기자 사슬이 차르륵 따라 내려와요. 높은 창으로 든 빛이 펼친 책 위에 떨어지고, 몸을 움직일 때마다 사슬이 낮게 쩔렁여요. 이 책은 내일도 이 자리에 있을 거예요.',
             'kid': '눈을 감아 봐. 책을 당기면 사슬이 차르륵 따라와. 창으로 햇빛이 들어오고, 쩔렁쩔렁 소리가 나. 이 책은 내일도 여기 있을 거야.'},
 'lines': ['책 한 권, 사슬 하나.', '책상까지는 내려와도, 책장을 떠나지는 않아요.', '뜯기고 나뉘었다가, 다시 한곳에.', '흩어지지 않게, 여럿이 함께 지킨 책장.'],
 'linesKid': ['책 한 권, 사슬 하나!', '책상까지는 괜찮아, 밖으로는 안 돼!', '흩어졌던 책장이 다시 모였어.'],
 'goals': {
  's4': {'t': '사슬 거는 차례', 'p': '책, 사슬, 쇠막대, 자물쇠, 책상 차례로 놓아 책 한 권을 책장에 걸면 카드에 금박이 입혀져요.',
         'how': '책 한 권이 사슬에 걸리는 차례대로 책장을 꾸며 보세요', 'done': '사슬 거는 차례대로 책장을 꾸몄어요',
         'ways': [{'id': 'plOrder', 't': '책 → 사슬 → 쇠막대 → 자물쇠 → 책상 차례로 놓기'}]},
  's5': {'t': '우리 집 한자리 책', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '우리 집에 늘 한자리에 둘 책의 자리를 고르거나, 아이와 함께 끝까지 보세요', 'done': '우리 집 한자리 책의 자리를 정했어요',
         'ways': [{'id': 'home', 't': '누구나 펼쳐 볼 책을 우리 집 어디에 둘지 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'place': {
   'items': ITEMS, 'order': '책, 사슬, 쇠막대, 자물쇠, 책상',
   'intro': '아래에서 하나를 골라 책장에 놓아 보세요. 책 한 권이 사슬에 걸리는 차례는 책, 사슬, 쇠막대, 자물쇠, 그리고 책상이에요.',
   'climax': '책장 앞에서는 읽을 수 있게, 책장 밖으로는 가져가지 못하게. 1611년부터 1841년까지, 성모 경당의 책들은 이렇게 제자리를 지켰어요.<span class="la">taken from the shelf and read at the desk · 헤리퍼드 대성당 누리집</span>',
   'wrongOrder': '책 한 권을 사슬로 거는 차례는 이래요: {order}',
   'orderDone': '사슬 거는 차례대로 책장을 꾸몄어요',
   'home': ['식탁 옆', '거실 책장', '창가', '현관 옆', '잠자리 머리맡'],
   'homeLabel': '우리 집 한자리 책',
   'homeWait': '책장을 다 꾸민 뒤 고를 수 있어요',
   'daylight': False,
   'svg': stage_svg()}},
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 걸어 보기</button></div>
  <div class="pl-home" hidden><p>우리 집에도 늘 한자리에 두고 누구나 펼쳐 볼 책이 있다면, 어디에 둘까요?</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 # ── 재벌(2026-11-22): 열쇠 물음 셋 ──
 'qs': [
  {'q': '왜 책을 종이 끝이 밖을 보게 꽂았어요?', 'img': 'clasp', 'pos': '50% 30%',
   'a': ['사슬은 책 앞표지에 달려 있어요. 종이 끝이 밖을 보게 꽂으면, 책을 들어 내려 돌리지 않고 바로 펼칠 수 있어요.',
         '책을 돌리지 않으니 사슬도 엉키지 않았지요. 그래서 이 책장에서는 책등 대신 종이 끝이 우리를 봐요.'],
   'see': '둘째 장면에서 맨 먼저 놓는 책이, 사슬이 엉키지 않게 돌려 꽂은 책으로 보여요.', 'seeAt': 'press', 'seeImg': 'chains',
   'film': [
    {'type': 'img', 'img': 'clasp', 'fit': 'cover', 'p0': '50% 25%', 'p1': '50% 45%', 's0': 1.05, 's1': 1.2,
     'lines': [{'t': '헤리퍼드의 책은 책등이 아니라 종이 끝이 밖을 봐요.'}, {'t': '사슬이 책 앞표지에 달려 있기 때문이에요.'}],
     'kid': [{'t': '책을 거꾸로 꽂았네!'}]},
    {'type': 'img', 'img': 'chains', 'fit': 'cover', 'p0': '75% 45%', 'p1': '80% 52%', 's0': 1.1, 's1': 1.35,
     'lines': [{'t': '종이 끝이 밖을 보면, 책을 들어 내려 바로 펼칠 수 있어요.'}, {'t': '책을 돌릴 일이 없으니, 사슬도 엉키지 않아요.'}],
     'kid': [{'t': '꺼내서 바로 펼치면, 사슬이 안 꼬여!'}]},
    {'type': 'img', 'img': 'postcard', 'fit': 'cover', 'p0': '45% 60%', 'p1': '50% 70%', 's0': 1.1, 's1': 1.2,
     'lines': [{'t': '책장 앞에는 책상이 붙어 있었어요.'}, {'t': '책은 그 책상 위에서 펼쳐 읽었어요.'}],
     'kid': [{'t': '책상에 펼쳐서 읽어!'}]},
    {'type': 'img', 'img': 'chains', 'fit': 'contain', 'o': '50% 50%', 's0': 1.0, 's1': 1.06,
     'lines': [{'t': '이제 둘째 장면을 다시 볼까요?'}, {'t': '종이 끝이 밖을 보는 까닭은, 엉키지 않는 사슬이었어요.'}],
     'kid': [{'t': '이제 다시 보면, 사슬이 안 꼬이게 꽂은 거야!'}]}]},
  {'q': '그 책들은 무슨 책이었길래, 사슬까지 달았어요?', 'img': 'chains', 'pos': '50% 40%',
   'a': ['사슬 도서관에는 800년 무렵부터 19세기 초까지의 책이 1,500권쯤 있어요. 손으로 쓴 중세 책에는 초기 기독교 저술가들의 글과 교회법·일반 법의 책, 신학 책이 많아요.',
         '1583년 조사 뒤에 생긴 새 규칙은 책을 지키려고 사슬로 묶으라고 했어요. 사슬은 옛 유럽 도서관에서 가장 널리 쓰인, 가장 든든한 책 지키기였어요.'],
   'see': '첫째 장면 사진 속 낡은 책들이, 1,000년 동안 모인 신학과 법의 책으로 보여요.', 'seeAt': 'rule',
   'film': [
    {'type': 'img', 'img': 'chains', 'fit': 'cover', 'p0': '50% 30%', 'p1': '50% 55%', 's0': 1.15, 's1': 1.02,
     'lines': [{'t': '사슬 도서관에는 책이 1,500권쯤 있어요.'}, {'t': '800년 무렵부터 19세기 초까지 모인 책들이에요.'}],
     'kid': [{'t': '책이 1,500권이나 있대!'}]},
    {'type': 'img', 'img': 'clasp', 'fit': 'cover', 'p0': '50% 70%', 'p1': '50% 55%', 's0': 1.2, 's1': 1.05,
     'lines': [{'t': '손으로 쓴 중세 책에는 초기 기독교 저술가들의 글,'}, {'t': '교회법과 일반 법의 책, 신학 책이 많아요.'}],
     'kid': [{'t': '하나님 공부, 법 공부 책이 많대.'}]},
    {'type': 'black',
     'lines': [{'t': '사슬은 은행 창구의 줄 달린 볼펜과 비슷해요.'}, {'t': '그 자리에서는 쓰되, 들고 갈 수는 없지요.'}],
     'kid': [{'t': '은행 볼펜처럼 줄이 달렸어!'}]},
    {'type': 'img', 'img': 'chains', 'fit': 'contain', 'o': '50% 50%', 's0': 1.0, 's1': 1.06,
     'lines': [{'t': '사슬은 옛 유럽 도서관에서 가장 널리 쓰인 책 지키기였어요.'}, {'t': '이제 첫째 장면을 다시 볼까요?'}],
     'kid': [{'t': '이제 다시 보면, 소중한 책을 지키는 사슬이야!'}]}]},
  {'q': '마파 문디는 어떤 지도였길래, 팔 물건으로 골랐어요?', 'img': 'mappa', 'pos': '50% 50%',
   'a': ['1300년 무렵 송아지 가죽 한 장에 그린 세계 지도예요. 지금 남은 중세 세계 지도 가운데 가장 크고, 도시 420곳과 성경 속 사건 15가지를 그림 500개 넘게 담았어요.',
         '대성당은 사슬 도서관을 흩지 않고도, 이 지도 한 장이면 필요한 돈을 마련할 수 있다고 보았어요.'],
   'see': '넷째 장면의 지도가, 책들 대신 홀로 팔려 나갈 뻔한 세상 그림으로 보여요.', 'seeAt': 'keep',
   'film': [
    {'type': 'img', 'img': 'mappa', 'fit': 'contain', 'o': '50% 50%', 's0': 1.0, 's1': 1.06,
     'lines': [{'t': '1300년 무렵, 송아지 가죽 한 장에 그린 세계 지도예요.'}, {'t': '지금 남은 중세 세계 지도 가운데 가장 커요.'}],
     'kid': [{'t': '송아지 가죽 한 장에 세상을 그렸대!'}]},
    {'type': 'img', 'img': 'mjeru', 'fit': 'cover', 'p0': '50% 50%', 'p1': '50% 45%', 's0': 1.0, 's1': 1.25,
     'lines': [{'t': '한가운데 둥근 도시는 예루살렘이에요.'}, {'t': '도시 420곳과 성경 속 사건 15가지가 그림으로 들어 있어요.'}],
     'kid': [{'t': '가운데 동그라미가 예루살렘이야.'}]},
    {'type': 'img', 'img': 'mtop', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 25%', 's0': 1.05, 's1': 1.2,
     'lines': [{'t': '꼭대기에는 세상 위에 앉은 그리스도가 있어요.'}, {'t': '세상과 성경 이야기를 한 장에 담은 지도예요.'}],
     'kid': [{'t': '맨 위에는 예수님이 앉아 계셔.'}]},
    {'type': 'img', 'img': 'mappa', 'fit': 'contain', 'o': '50% 50%', 's0': 1.06, 's1': 1.0,
     'lines': [{'t': '대성당은 이 지도 한 장이면 필요한 돈이 된다고 보았어요.'}, {'t': '이제 넷째 장면을 다시 볼까요?'}],
     'kid': [{'t': '이제 다시 보면, 책들 대신 팔 뻔한 지도야!'}]}]},
 ],
 # ── 재벌: 뒷이야기 꾸러미(1 → 2 → 3) ──
 'qx': [
  # 꾸러미 1
  {'id': 'frames', 'pack': 1, 'q': '책 제목이 안 보이는데, 책은 어떻게 찾았어요?', 'hook': '책장 끝에 붙은 액자', 'img': 'pframe', 'pos': '62% 40%',
   'a': ['책장 끝마다 붙은 액자가 그 답이에요. 그 책장에 꽂힌 책들의 목록을 넣어 두는 틀이에요.',
         '1901년 클라크는 이 액자들을 17세기에 토머스 손턴이 더했다고 적었어요. 1611년 사슬 책장을 짓게 한 바로 그 도서관 책임자예요. 2025년 사진 속 책장 끝에도 이런 액자가 걸려 있어요.'],
   'see': '셋째 장면 엽서 속 책장 끝의 두 칸 액자가, 그 책장의 책 목록으로 읽혀요.', 'seeAt': 'apart', 'seeImg': 'postcard',
   'src': [{'t': 'J. W. Clark, 『The Care of Books』(1901)', 'm': '영어 · 프로젝트 구텐베르크 · 목록을 넣는 액자는 17세기에 참사회원 토머스 손턴이 더함', 'u': CLARKT},
           {'t': '마파 문디·사슬 도서관 누리집: 사슬 도서관', 'm': '영어 · 1611년 도서관 책임자 토머스 손턴이 성모 경당에 사슬 도서관을 짓게 함', 'u': MAPPA}]},
  {'id': 'streeter', 'pack': 1, 'q': '1930년에 사슬을 다시 단 스트리터는 누구예요?', 'hook': '복음서를 파고든 참사회원', 'img': 'postcard', 'pos': '50% 45%',
   'a': ['B. H. 스트리터는 옥스퍼드의 신학자이자 성경 학자로, 1915년부터 1934년까지 헤리퍼드 대성당의 참사회원이었어요. 그 사이 1924년에는 네 복음서가 어떻게 생겨났는지 파고든 책 『네 복음서』를 냈어요.',
         '사슬 도서관을 되살리는 동안 옛 도서관들을 두루 살폈고, 1931년 그 연구를 『사슬 도서관』이라는 책으로 냈어요. 1932년의 한 서평은 이 복원에 든 돈을 너그러운 기부자 한 사람이 댔다고 적었어요.'],
   'see': '셋째 장면의 ‘스트리터 참사회원’이, 복음서를 연구하다 책장의 사슬까지 되살린 학자로 보여요.', 'seeAt': 'apart', 'seeImg': 'lib2025',
   'src': [{'t': '케임브리지 대학 출판부: 『The Chained Library』 소개', 'm': '영어 · 옥스퍼드의 신학자·성경 학자(1874~1937), 1915~1934년 헤리퍼드 참사회원, 도서관을 되살리며 한 연구로 1931년에 펴냄', 'u': CUPS},
           {'t': '온라인 북스 페이지: B. H. Streeter', 'm': '영어 · 『The Four Gospels』(Macmillan, 1924)', 'u': FOURG},
           {'t': 'The Spectator, 1932년 7월 16일 「Books in Chains」', 'm': '영어 · 너그러운 기부자의 돈으로 한 헤리퍼드 도서관 복원을 지켜봄, 옥스퍼드·케임브리지의 옛 칼리지 도서관을 모두 살핌', 'u': SPECT},
           {'t': '마파 문디·사슬 도서관 누리집: 사슬 도서관', 'm': '영어 · 1930년 무렵 스트리터 참사회원이 성모 경당 때 모습대로 되살림', 'u': MAPPA}]},
  {'id': 'oath', 'pack': 1, 'q': '지금도 꺼내 쓰는 책이 있어요?', 'hook': '주교가 맹세하는 1,200년 된 책', 'img': 'chains', 'pos': '70% 40%',
   'a': ['사슬 도서관에서 가장 오래된 책 「헤리퍼드 복음서」는 800년 무렵 만들어졌어요. 지금 남은 책 가운데 웨일스에서 만든 가장 오래된 책일지도 몰라요.',
         '지금도 헤리퍼드의 주교와 주임 사제는 자리에 오를 때 이 책에 맹세해요. 주로 18~19세기에 만든 닳은 악보 책들은, 날마다 예배에서 노래하던 성가대 사제들이 썼고요.'],
   'see': '첫째 장면 사진 속 낡은 책들이, 지금도 맹세의 자리에 불려 나오는 책과 한 식구로 다가와요.', 'seeAt': 'rule',
   'src': [{'t': '마파 문디·사슬 도서관 누리집: 사슬 도서관', 'm': '영어 · 800년 무렵의 헤리퍼드 복음서, 웨일스에서 만든 가장 오래된 책일지 모름, 헤리퍼드의 주교와 주임 사제가 이 책에 맹세, 성가대 사제들이 날마다 예배에 쓴 18~19세기 악보 책', 'u': MAPPA}]},
  {'id': 'sale', 'pack': 1, 'q': '지도를 판다는 소식에, 사람들은 어떻게 했어요?', 'hook': '몇 주 전엔 아무도 몰랐던 지도', 'img': 'mappa', 'pos': '50% 40%',
   'a': ['1988년 12월 영국 상원에서 한 의원이 물었어요. 몇 주 전만 해도 마파 문디가 있는 줄 아는 사람은 아주 적지 않았느냐고요. 그는 지도를 내보이고 입장료를 받아 대성당을 돌보자고 했고, 정부 쪽도 그 뜻에 동의했어요.',
         '1989년 2월 말, 대성당은 지도를 경매에서 거두었어요. 지금은 입장료가 대성당의 큰 수입이 되어 소장품을 돌보는 데 쓰여요.'],
   'see': '넷째 장면의 지도가, 팔린다는 소식이 나고서야 온 나라가 알게 된 지도로 보여요.', 'seeAt': 'keep',
   'src': [{'t': '영국 상원 회의록 1988년 12월 6일 「The Mappa Mundi」', 'm': '영어 · 몬터규 경: 몇 주 전만 해도 이 나라에서 마파 문디를 아는 사람이 아주 적었다, 입장료를 받고 내보이자 · 정부 답변: 그 뜻에 전적으로 동의, 결정은 주임 사제의 몫', 'u': HL88},
           {'t': '영국 하원 서면 답변 1989년 3월 20일 「Mappa Mundi」', 'm': '영어 · 2월 말 지도를 경매에서 거둠', 'u': HC89},
           {'t': '마파 문디 재단: 재단과 소장품의 역사', 'm': '영어 · 입장료가 대성당의 큰 수입이 되어 소장품을 돌봄', 'u': TRUST}]},
  {'id': 'redsea', 'pack': 1, 'q': '지도 오른쪽 위의 빨간 Y자는 뭐예요?', 'hook': '바닷속으로 난 길', 'img': 'mred', 'pos': '45% 50%',
   'a': ['홍해예요. 지도는 홍해를 붉게 칠하고, 그 가운데로 길 하나를 또렷이 그었어요.',
         f'이스라엘 백성이 이집트의 종살이를 벗어나 ‘약속의 땅’으로 간 길이에요. 성경은 하나님이 바닷물을 가르셔서 백성이 마른 땅으로 건넜다고 전해요({bl("EXO.14", "출애굽기 14장")}).'],
   'see': '넷째 장면 지도 오른쪽 위의 붉은 물줄기가, 바다를 건넌 이야기를 품은 길로 보여요.', 'seeAt': 'keep',
   'src': [{'t': '마파 문디·사슬 도서관 누리집: 마파 문디', 'm': '영어 · 홍해를 지나는 또렷한 길, 이스라엘 백성이 이집트의 종살이에서 ‘약속의 땅’으로 간 길', 'u': MAPW},
           {'t': '대한성서공회 개역개정: 출애굽기 14장', 'm': '한국어 · 바다가 갈라져 이스라엘 자손이 마른 땅으로 건넘', 'u': NKRV + 'EXO.14'}]},
  {'id': 'britain', 'pack': 1, 'q': '이 지도에서 영국과 헤리퍼드는 어디예요?', 'hook': '세상 끝자락의 헤리퍼드', 'img': 'mbrit', 'pos': '60% 50%',
   'a': ['왼쪽 아래 가장자리, 둥근 세상의 끝에 붙은 길쭉한 섬들이 영국이 있는 브리튼 섬들이에요. 헤리퍼드도 와이강 가의 작은 건물로 그려져 있지만, 알아보기 어려워요.',
         '스코틀랜드 자리에는 이 지도를 그린 송아지 가죽의 핏줄 자국이 아직 남아 있어요.'],
   'see': '넷째 장면 지도의 왼쪽 아래 끝자락이, 지도가 걸린 헤리퍼드 사람들의 땅으로 보여요.', 'seeAt': 'keep',
   'src': [{'t': '옥스퍼드 캐비닛(Howard Hotson, 2021) 「Mappa Mundi」', 'm': '영어 · 브리튼 섬들은 왼쪽 아래', 'u': CABINET},
           {'t': '마파 문디·사슬 도서관 누리집: 마파 문디', 'm': '영어 · 와이강 가의 작고 흐릿한 건물로 그린 헤리퍼드, 스코틀랜드 자리에 남은 짐승의 핏줄 자국', 'u': MAPW}]},
  # 꾸러미 2
  {'id': 'addbook', 'pack': 2, 'q': '새 책 한 권을 넣으려면 어떻게 해요?', 'hook': '책 한 권 넣기가 큰일', 'img': 'clasp', 'pos': '50% 42%',
   'a': ['클라크가 본 헤리퍼드 책장에서는 쇠막대가 칸막이마다 끊겨 있어서, 선반 하나에 막대가 세 개씩 걸렸어요. 세 선반의 쇠붙이는 책장 끝 자물쇠 하나로 함께 잠갔고요.',
         '막대 끝이 자물쇠로 막혀 있으니, 클라크는 책 한 권을 빼거나 새로 넣는 일이 꽤 번거로웠을 거라고 적었어요.'],
   'see': '첫째 장면 사진의 가로 쇠막대들이, 책 한 권 들이기도 번거롭게 만든 자물쇠 달린 막대로 보여요.', 'seeAt': 'rule',
   'src': [{'t': 'J. W. Clark, 『The Care of Books』(1901)', 'm': '영어 · 프로젝트 구텐베르크 · 막대는 칸막이에서 칸막이까지라 선반마다 셋, 세 선반의 쇠붙이를 자물쇠 하나로, 책을 빼거나 더하는 일은 번거로웠을 것', 'u': CLARKT}]},
  {'id': 'getty', 'pack': 2, 'q': '돈을 보탠 존 폴 게티 2세는 누구예요?', 'hook': '직업 칸에 ‘자선가’라고 쓴 사람', 'img': 'lib2025', 'pos': '60% 50%',
   'a': ['석유 부자 J. 폴 게티의 아들로, 영국에 살며 큰돈을 내놓은 사람이에요. 인명사전 『후즈 후』의 직업 칸에는 ‘자선가’라고 적었고, 런던 국립 미술관에만 5,000만 파운드를 주었어요. 옛 책도 무척 아꼈다고 해요.',
         '1989년 그는 지도와 사슬 도서관을 함께 맡을 재단에 100만 파운드를 내겠다고 했어요. 1998년에는 영국 시민이 되었어요.'],
   'see': '셋째 장면의 2025년 사진 속 책장들이, 옛 책을 아낀 한 기부자도 함께 지킨 책장으로 보여요.', 'seeAt': 'apart',
   'src': [{'t': 'The Irish Times(2003) 부고 「Benevolent squire tormented by oil dynasty’s vast wealth」', 'm': '영어 · 전설적인 석유 부자 J. 폴 게티의 아들, 『후즈 후』에 직업을 ‘자선가’로, 국립 미술관에 5,000만 파운드, 옛 책을 사랑함', 'u': ITGETTY},
           {'t': '런던 국립 미술관: Sir Paul Getty', 'm': '영어 · 1932~2003, 미술관을 위한 넉넉한 기금, 1998년 영국 시민', 'u': NGETTY},
           {'t': '영국 하원 서면 답변 1989년 3월 20일 「Mappa Mundi」', 'm': '영어 · 지도와 사슬 도서관을 맡을 재단에 게티가 100만 파운드를 내겠다고 함', 'u': HC89},
           {'t': '마파 문디 재단: 재단과 소장품의 역사', 'm': '영어 · 존 폴 게티 2세가 크게 도움', 'u': TRUST}]},
  {'id': 'shares', 'pack': 2, 'q': '경매를 거둔 뒤에는 어떻게 돈을 모았어요?', 'hook': '1,000파운드짜리 지도 주식', 'img': 'mappa', 'pos': '50% 65%',
   'a': ['1989년 3월, 대성당은 한 주에 1,000파운드짜리 회사 주식을 팔아 돈을 모으겠다고 했어요. 주식을 산 사람은 지도 복제본을 받고, 회사 주식의 절반은 대성당이 갖는 계획이었어요.',
         '이때는 재단을 세우자는 제안이 받아들여지지 않았어요. 하지만 그해 10월, 국가 유산 기념 기금은 지도와 사슬 도서관을 맡을 새 재단에 200만 파운드를 주기로 했어요.'],
   'see': '넷째 장면의 ‘새 재단’이, 주식 계획까지 거친 끝에 세워진 재단으로 보여요.', 'seeAt': 'keep',
   'src': [{'t': '영국 하원 서면 답변 1989년 3월 20일 「Mappa Mundi」', 'm': '영어 · 1,000파운드 주식, 주주에게 지도 복제본, 주식 절반은 주임 사제와 참사회, 재단 제안은 이때 받아들여지지 않음', 'u': HC89},
           {'t': '국가 유산 기념 기금(NHMF): Mappa Mundi and Chained Library, Hereford Cathedral', 'm': '영어 · 새 재단의 기금 200만 파운드, 1989년 10월 26일', 'u': NHMF}]},
  {'id': 'elizabeth', 'pack': 2, 'q': '여왕이 왜 대성당 도서관까지 살폈어요?', 'hook': '교회를 다스린 두 엘리자베스', 'img': 'chains', 'pos': '25% 25%',
   'a': ['1534년 헨리 8세가 로마와 갈라서며 잉글랜드 교회가 생겼어요. 1559년 의회는 엘리자베스 1세 여왕을 잉글랜드 교회의 ‘최고 통치자’로 정했고, 1583년의 조사단도 이 여왕이 세운 것이었어요.',
         '이 자리는 지금도 영국 왕이 이어 가요. 1996년 사슬 도서관의 새 건물을 연 사람도 엘리자베스 2세 여왕이었어요.'],
   'see': '첫째 장면의 ‘여왕이 보낸 조사단’이, 교회의 최고 통치자가 보낸 조사단으로 읽혀요.', 'seeAt': 'rule',
   'src': [{'t': 'Map of Early Modern London(빅토리아 대학): Church of England', 'm': '영어 · 1534년 헨리 8세가 로마와 갈라섬, 1559년 의회가 엘리자베스 1세를 최고 통치자로, 지금도 영국 왕이 맡음', 'u': UVIC},
           {'t': '마파 문디·사슬 도서관 누리집: 사슬 도서관', 'm': '영어 · 1583년 엘리자베스 1세가 세운 조사단, 1996년 엘리자베스 2세가 새 건물을 엶', 'u': MAPPA}]},
  {'id': 'center', 'pack': 2, 'q': '지도 한가운데의 동그라미는 뭐예요?', 'hook': '세상의 한가운데, 예루살렘', 'img': 'mjeru', 'pos': '50% 50%',
   'a': ['둥근 성벽으로 그린 도시, 예루살렘이에요. 이 지도는 예수가 십자가에 달린 이곳을 세상의 한가운데에 두었어요. 그 바로 위에 십자가도 그려져 있어요.',
         '땅을 가르는 검은 줄들은 바다와 강이에요. 원래는 초록색이었는데, 구리로 만든 물감이 세월이 흐르며 검게 변했어요.'],
   'see': '넷째 장면 지도의 검은 T자 물줄기가, 처음엔 초록빛이던 바다로 보여요.', 'seeAt': 'keep',
   'src': [{'t': '마파 문디·사슬 도서관 누리집: 마파 문디', 'm': '영어 · 예루살렘은 십자가의 자리이자 지도의 한가운데, 바다는 원래 초록이었으나 구리 물감이 검게 변함', 'u': MAPW},
           {'t': '옥스퍼드 캐비닛(Howard Hotson, 2021) 「Mappa Mundi」', 'm': '영어 · 가운데 예루살렘', 'u': CABINET}]},
  # 꾸러미 3
  {'id': 'oxford', 'pack': 3, 'q': '헤리퍼드와 옥스퍼드, 누가 누구를 본떴어요?', 'hook': '서로 닮은 두 도서관', 'img': 'postcard', 'pos': '30% 40%',
   'a': ['마파 문디 누리집은 1611년의 사슬 책장이 그 무렵 옥스퍼드 대학에 새로 들어선 도서관들을 본떴다고 적어요. 쇠붙이도 옥스퍼드에서 주문했고, 클라크는 책장 끝 목록 액자가 옥스퍼드의 것과 아주 닮았다고 했어요.',
         '그런데 1932년의 한 서평은 거꾸로 적었어요. 1590년 헤리퍼드의 책장 방식을, 몇 해 뒤 옥스퍼드 보들리 도서관의 ‘험프리 공작 도서관’이 받아들였다는 거예요. 자료마다 달라요.'],
   'see': '첫째 장면의 ‘옥스퍼드를 본뜬 책장’이, 누가 먼저인지 자료마다 다른 이웃 책장으로 보여요.', 'seeAt': 'rule',
   'go': {'t': '「보들리의 빈방」 카드로 가기', 'cid': 'lib-bodleian'},
   'src': [{'t': '마파 문디·사슬 도서관 누리집: 사슬 도서관', 'm': '영어 · 그 무렵 옥스퍼드 대학에 새로 들어선 도서관들을 본뜸, 쇠붙이는 옥스퍼드에서 주문', 'u': MAPPA},
           {'t': 'J. W. Clark, 『The Care of Books』(1901)', 'm': '영어 · 목록 액자는 옥스퍼드의 것과 아주 닮음', 'u': CLARKT},
           {'t': 'The Spectator, 1932년 7월 16일 「Books in Chains」', 'm': '영어 · 헤리퍼드의 책장 방식을 몇 해 뒤 보들리의 ‘험프리 공작 도서관’이 받아들임, 헤리퍼드는 1590년', 'u': SPECT}]},
  {'id': 'last', 'pack': 3, 'q': '다른 도서관들은 사슬을 언제 풀었어요?', 'hook': '1799년에야 풀린 사슬', 'img': 'zutphen', 'pos': '50% 60%',
   'a': ['1932년의 한 서평은 사슬 도서관이 중세에만 있던 것이 아니라고 적었어요. 옥스퍼드의 모들린 칼리지는 1799년에야 책 사슬을 없앴대요.',
         '그 서평이 나올 무렵에도 헤리퍼드 대성당과 길퍼드의 한 문법 학교에는 사슬이 남아 있었어요. 헤리퍼드는 사슬과 쇠막대, 자물쇠가 모두 온전히 남은 사슬 도서관 가운데 가장 커요.'],
   'see': '앞면 카드의 사슬 달린 책이, 사슬을 끝내 풀지 않은 몇 안 되는 도서관의 책으로 보여요.', 'seeAt': 'front',
   'src': [{'t': 'The Spectator, 1932년 7월 16일 「Books in Chains」', 'm': '영어 · 사슬 도서관은 중세만의 것이 아님, 모들린 칼리지 1799년, 헤리퍼드 대성당과 길퍼드 문법 학교에는 아직 남음', 'u': SPECT},
           {'t': '헤리퍼드 대성당: 사슬 도서관', 'm': '영어 · 사슬·막대·자물쇠가 모두 남은 사슬 도서관 가운데 가장 큼', 'u': HCATH}]},
  {'id': 'vatican', 'pack': 3, 'q': '사슬에 묶인 책을 빌려주는 도서관도 있었어요?', 'hook': '사슬째 빌려 간 책', 'img': 'chains', 'pos': '80% 50%',
   'a': ['로마 바티칸의 교황 도서관은 1475년부터 책을 빌려주었고, 1547년까지의 대출 기록이 지금도 남아 있어요.',
         '그곳에서 책을 빌리는 사람은 책과 함께 사슬까지 가져가야 했어요. 미국 의회도서관 전시는 그 책이 자기 것이 아님을 잊지 말라는 뜻이었을 거라고 적어요.'],
   'see': '둘째 장면에서 책장을 떠나지 못하게 한 사슬이, 다른 곳에서는 책과 함께 길을 나선 사슬로도 보여요.', 'seeAt': 'press', 'seeImg': 'clasp',
   'go': {'t': '「라틴어 방의 벽화」 카드로 가기', 'cid': 'lib-vatican'},
   'src': [{'t': '바티칸 사도 도서관: 도서관의 역사', 'm': '영어 · 1475~1547년의 대출 기록이 남아 있음', 'u': 'https://www.vatlib.it/en/the-library/history-of-BAV.html'},
           {'t': '미국 의회도서관 「Rome Reborn」 전시: 도서관이 모양을 갖추다', 'm': '영어 · 빌리는 사람은 책과 함께 사슬도 가져가야 했고, 책이 자기 것이 아님을 일깨우려던 것으로 보임', 'u': 'https://www.ibiblio.org/expo/vatican.exhibit/exhibit/a-vatican_lib/Takes_shape.html'}]},
  {'id': 'top', 'pack': 3, 'q': '지도 꼭대기의 사람들은 누구예요?', 'hook': '세상 위에 앉은 그리스도', 'img': 'mtop', 'pos': '50% 30%',
   'a': ['꼭대기에는 그리스도가 세상 위 보좌에 앉아 온 세상을 내려다보고, 그 양옆으로 구원받는 사람들과 벌받는 사람들이 그려져 있어요. 그 아래 둥근 섬은 에덴동산이에요.',
         '이 지도는 해가 뜨는 동쪽을 위에 두었어요. 중세 그리스도인들은 그리스도가 다시 오실 곳을 동쪽에서 바라보았대요.'],
   'see': '넷째 장면 지도의 뾰족한 꼭대기가, 세상 위에 앉은 그리스도의 자리로 보여요.', 'seeAt': 'keep',
   'src': [{'t': '마파 문디·사슬 도서관 누리집: 마파 문디', 'm': '영어 · 그리스도가 세상 위 보좌에 앉아 온 창조 세계를 내려다봄, 구원받는 이들과 벌받는 이들, 동쪽 끝(위)의 둥근 섬 에덴', 'u': MAPW},
           {'t': '옥스퍼드 캐비닛(Howard Hotson, 2021) 「Mappa Mundi」', 'm': '영어 · 위에 에덴, 해 뜨는 동쪽에서 그리스도의 다시 오심을 바라봄', 'u': CABINET}]},
 ],
 # 검토용 · 더 깊이 후보(미리 보기에만): 악마의 대변인의 물음과 창의 후보, 어디에 썼는지
 'qcand': [
  {'q': '왜 종이 끝이 밖? 어떻게 꽂아?', 'at': '악마의 대변인 · 앞면 물음(“답이 자막 한 줄뿐, 왜 그렇게 꽂는지 없음”)', 'a': '사슬은 앞표지에, 돌리지 않고 펼침 → 사슬이 엉키지 않음 — 헤리퍼드 대성당 누리집', 'pick': 1, 'see': '둘째 장면의 책이 엉키지 않게 돌려 꽂은 책으로 보여요.'},
  {'q': '무슨 책? 성경? 허물어짐이 왜 사슬로?', 'at': '악마의 대변인 · 첫째 장면(“도둑 얘기 없음”)', 'a': '800년~19세기 초 1,500권쯤, 초기 기독교 저술가·교회법·일반 법·신학, 1583년 새 규칙 ‘안전하게 지키려고’, 유럽 도서관에서 가장 널리 쓰인 보안 — 마파 문디 누리집·대성당 누리집', 'pick': 1, 'see': '첫째 장면의 책들이 신학과 법의 책으로 보여요.'},
  {'q': '마파 문디는 무슨 지도? 왜 비싸? 왜 책 대신?', 'at': '악마의 대변인 · 넷째 장면·영화(E)', 'a': '1300년 무렵 송아지 가죽 한 장, 가장 큰 중세 세계 지도, 도시 420·성경 사건 15·그림 500 넘게, 한 점으로 필요한 돈 — 마파 문디 누리집·기네스·재단', 'pick': 1, 'see': '넷째 장면의 지도가 홀로 팔려 나갈 뻔한 지도로 보여요.'},
  {'x': 'frames', 'q': '종이 끝에 글씨가 없는데 어떻게 찾아? 엽서 책장 옆 두 칸 글씨판은?', 'at': '악마의 대변인 B8·C(그림) · 꾸러미 1', 'a': '목록 액자, 17세기 손턴 — 클라크', 'see': '엽서의 두 칸 액자가 책 목록으로 보여요.'},
  {'x': 'streeter', 'q': '1930년엔 왜 다시 달았어? 스트리터는 누구?', 'at': '악마의 대변인 B12·D(“이름만”) · 꾸러미 1', 'a': '옥스퍼드 신학자·성경 학자, 1915~1934 참사회원, 『네 복음서』(1924), 『사슬 도서관』(1931), 너그러운 기부자 — 케임브리지 대학 출판부·온라인 북스·스펙테이터', 'see': '스트리터가 사슬을 되살린 학자로 보여요.'},
  {'x': 'oath', 'q': '가장 오래된 책은 지금도 쓰여?', 'at': '창 · 꾸러미 1(‘알고 보면’의 ‘가장 오래된 책’을 옮김)', 'a': '헤리퍼드 복음서 800년 무렵, 웨일스에서 만든 가장 오래된 책일지 모름, 주교·주임 사제의 맹세, 성가대 사제의 악보 책 — 마파 문디 누리집', 'see': '낡은 책들이 맹세의 책과 한 식구로 보여요.'},
  {'x': 'sale', 'q': '누가 사려 했어? 사람들은 어떻게 했어?', 'at': '악마의 대변인 B14·G(“지도 사건 누가 얼마에”) · 꾸러미 1 · 누가 사려 했는지는 찾지 못함', 'a': '1988년 12월 상원 몬터규 경(몇 주 전엔 아는 사람이 적었다), 1989년 2월 말 경매에서 거둠, 입장료 수입 — 상원·하원 회의록·재단', 'see': '팔린다는 소식이 나고서야 알려진 지도로 보여요.'},
  {'x': 'redsea', 'q': '오른쪽 위 빨간 Y자는?', 'at': '악마의 대변인 C(그림) · 꾸러미 1', 'a': '홍해를 지나는 길, 출애굽 — 마파 문디 누리집, 출애굽기 14장', 'see': '붉은 물줄기가 바다를 건넌 길로 보여요.'},
  {'x': 'britain', 'q': '영국·헤리퍼드는 어디? 한국은?', 'at': '악마의 대변인 C(그림) · 꾸러미 1 · 한국은 지도에 없어 답하지 않음', 'a': '왼쪽 아래 브리튼 섬들, 와이강 가의 헤리퍼드, 스코틀랜드 자리의 핏줄 자국 — 옥스퍼드 캐비닛·마파 문디 누리집', 'see': '왼쪽 아래 끝자락이 헤리퍼드 사람들의 땅으로 보여요.'},
  {'x': 'addbook', 'q': '자물쇠는 뭘 잠가? 책 한 권 넣으려면?', 'at': '악마의 대변인 A(“자물쇠를 채우면 — 뭘?”) · 꾸러미 2(‘알고 보면’의 ‘하나의 자물쇠’를 옮김) · 영화 자막에 ‘쇠막대를’ 길잡이', 'a': '선반마다 막대 셋, 세 선반에 자물쇠 하나, 빼고 넣기 번거로움 — 클라크', 'see': '쇠막대가 자물쇠 달린 막대로 보여요.'},
  {'x': 'getty', 'q': '존 폴 게티 2세는 누구?', 'at': '악마의 대변인 B15 · 꾸러미 2(지도 이야기에서 이어짐)', 'a': '석유 부자의 아들, ‘자선가’, 국립 미술관 5,000만 파운드, 옛 책 사랑, 1989년 100만 파운드, 1998년 영국 시민 — 아이리시 타임스·국립 미술관·하원', 'see': '책장들이 한 기부자도 함께 지킨 책장으로 보여요.'},
  {'x': 'shares', 'q': '힘을 보태=돈? 어떻게 모았어?', 'at': '악마의 대변인 E · 꾸러미 2(지도 이야기에서 이어짐) · 영화 자막 ‘돈을 보태’로 고침', 'a': '1989년 3월 1,000파운드 주식·복제본 계획, 재단 제안은 이때 받아들여지지 않음, 10월 국가 유산 기념 기금 200만 파운드 — 하원·NHMF', 'see': '새 재단이 주식 계획을 거쳐 세워진 재단으로 보여요.'},
  {'x': 'elizabeth', 'q': '여왕이 왜 성당 조사? 천주교? 개신교?', 'at': '악마의 대변인 B4·B5·D(“엘리자베스 1세→2세 대칭”) · 꾸러미 2 · 영화 자막에 ‘엘리자베스 1세’ 길잡이', 'a': '1534년 헨리 8세, 1559년 최고 통치자, 지금도 영국 왕, 1996년 엘리자베스 2세 — 빅토리아 대학·마파 문디 누리집', 'see': '조사단이 교회의 최고 통치자가 보낸 조사단으로 보여요.'},
  {'x': 'center', 'q': '가운데 동그라미, T자 검은 줄은?', 'at': '악마의 대변인 C(그림) · 꾸러미 2(홍해 이야기에서 이어짐)', 'a': '예루살렘(십자가의 자리, 한가운데), 바다는 원래 초록·구리 물감이 검게 — 마파 문디 누리집·옥스퍼드 캐비닛', 'see': '검은 물줄기가 초록이던 바다로 보여요.'},
  {'x': 'oxford', 'q': '옥스퍼드 도서관=해리 포터? 쇠붙이 옥스퍼드 주문 “그래서?”', 'at': '악마의 대변인 B7·D · 꾸러미 3(‘알고 보면’의 ‘옥스퍼드에서 온 쇠붙이’를 옮김 · 「보들리의 빈방」으로 길)', 'a': '옥스퍼드를 본뜸·쇠붙이 주문, 목록 액자가 닮음, 1932년 서평은 거꾸로(1590년 헤리퍼드 → 험프리 공작 도서관) — 마파 문디 누리집·클라크·스펙테이터', 'see': '옥스퍼드를 본뜬 책장이 이웃 책장으로 보여요.'},
  {'x': 'last', 'q': '사슬은 언제 사라졌어?', 'at': '창 · 꾸러미 3(‘알고 보면’의 ‘사슬이 사라진 때’를 옮김)', 'a': '모들린 1799년, 1932년에도 헤리퍼드·길퍼드 문법 학교에 남음, 사슬·막대·자물쇠가 온전한 가장 큰 곳 — 스펙테이터·대성당 누리집', 'see': '앞면의 책이 사슬을 끝내 풀지 않은 곳의 책으로 보여요.'},
  {'x': 'vatican', 'q': '사슬 책을 빌려주기도 했어?', 'at': '창 · 꾸러미 3(같은 묶음 lib-vatican의 chainloan에서 거꾸로 오는 길 · 「라틴어 방의 벽화」로 길)', 'a': '바티칸 1475~1547 대출 기록, 사슬째 빌림 — 바티칸 도서관·미국 의회도서관 전시', 'see': '사슬이 책과 함께 길을 나선 사슬로도 보여요.'},
  {'x': 'top', 'q': '꼭대기 사람들은? 왜 집 모양?', 'at': '악마의 대변인 C(그림) · 꾸러미 3 · 뾰족한 모양의 까닭은 찾지 못함', 'a': '보좌의 그리스도, 구원받는 이들과 벌받는 이들, 에덴, 동쪽이 위 — 마파 문디 누리집·옥스퍼드 캐비닛', 'see': '뾰족한 꼭대기가 그리스도의 자리로 보여요.'},
  {'q': '‘경당’이 뭐야? 종교개혁과 안 쓴 게 무슨 상관?', 'at': '악마의 대변인 A · 본 이야기 첫째 장면에 쉬운 말 ‘(성모 마리아에게 바친 작은 예배당)’ · 안 쓰게 된 까닭은 누리집에 없어 덧붙이지 않음', 'a': '마파 문디 누리집(disused after the Reformation)', 'see': '(약해요)'},
  {'q': '1901년 기록 갑자기 누구? ‘꾸며 보세요’=장식?', 'at': '악마의 대변인 A · 첫머리 글을 ‘1901년 한 학자가 적어 둔 그대로 … 걸어 보세요’로, 둘째 장면에 ‘옛 도서관을 연구하던’ 길잡이', 'a': 'Clark 1901 속표지', 'see': '(약해요)'},
  {'q': '“헤리퍼드만 한 곳을 알지 못한다” 꼬임 · ‘얼마 전’ · ‘앞 책상’ · ‘회랑’', 'at': '악마의 대변인 A · 본 이야기에서 쉬운 말로 고침', 'a': 'Clark(no better example) · 마파 문디 누리집', 'see': '(약해요)'},
  {'q': '1996년 “성모 경당에 있던 그대로” = 돌아간 거야? 하얀 벽 새 건물인데?', 'at': '악마의 대변인 A·C · 셋째 장면과 영화에 ‘새 건물 안에’ 길잡이', 'a': '마파 문디 누리집·대성당 누리집(as it was from 1611 to 1841)', 'see': '(약해요)'},
  {'q': '장면 3(1996)→장면 4(1980년대) 시간이 거꾸로 · 팔자는 대성당이 걱정?', 'at': '악마의 대변인 A·E · 넷째 장면 첫 줄에 ‘그 새 건물이 서기까지는 큰 고비가 있었어요’, 걱정하는 목소리 문장을 풀어 씀', 'a': '재단 역사(local and national concern that the cathedral (and in fact the UK) could easily lose)', 'see': '(약해요)'},
  {'q': '1841 사슬 떼었다면서 자막 위 엽서엔 사슬?', 'at': '악마의 대변인 E · 영화 엽서 설명을 ‘1930년 무렵 사슬을 다시 단 뒤’로', 'a': '본 이야기 셋째 장면의 추정과 같음', 'see': '(약해요)'},
  {'q': '1583 규칙~1611 사이 28년은?', 'at': '악마의 대변인 B6 · 본 이야기에 이미 1590년 성모 경당으로 옮김이 있어 더하지 않음', 'a': '마파 문디 누리집', 'see': '(약해요)'},
  {'q': '사슬 엉키지 않아?', 'at': '악마의 대변인 B10 · 열쇠 1과 둘째 장면의 돌림고리로 답함', 'a': '대성당 누리집·클라크', 'see': '(약해요)'},
  {'q': '1841년 왜 떼었어?', 'at': '악마의 대변인 B11 · 본 이야기 셋째 장면(성모 경당 고치는 공사)으로 답함', 'a': '마파 문디 누리집', 'see': '(약해요)'},
  {'q': '책 한 권 값(지금 돈)? 600만 파운드=우리 돈?', 'at': '악마의 대변인 B2·B13 · 답을 찾지 못한 물음(그때 값을 적은 근거를 못 찾음, 환율로 바꾸는 셈은 해마다 달라 쓰지 않음)', 'a': '—', 'see': '(약해요)'},
  {'q': '진짜 책 도둑 사건?', 'at': '악마의 대변인 B3·G · 답을 찾지 못한 물음(헤리퍼드 책 도난 기록을 찾지 못함)', 'a': '—', 'see': '(약해요)'},
  {'q': '아무나 읽었어?', 'at': '악마의 대변인 B9 · 답을 찾지 못한 물음(그때 누가 썼는지 적은 근거를 못 찾음 · 지금은 세계 곳곳의 학자가 연구)', 'a': '마파 문디 누리집(scholars from all over the world)', 'see': '(약해요)'},
  {'q': '2017년 사진의 하얀 끈 묶인 책 · 2025년 사진 아래 칸의 갈색 덮개?', 'at': '악마의 대변인 C(그림) · 답을 찾지 못한 물음', 'a': '—', 'see': '(약해요)'},
  {'q': '책장 꼭대기 ‘Classis Secunda’ 글씨는?', 'at': '악마의 대변인 C(그림) · 라틴어 글자 뜻(‘둘째 칸’)만 알 수 있고 헤리퍼드 책장 이름에 대한 근거를 못 찾아 쓰지 않음', 'a': '—', 'see': '(약해요)'},
  {'q': '앞면 사진 책의 왼쪽 뾰족한 쇠 넷, 오른쪽 쇠 조각 둘, 꼭대기 창끝 쇠?', 'at': '악마의 대변인 C(앞면 그림, 쥐트펀) · 답을 찾지 못한 물음(쥐트펀 책의 장식을 설명한 근거를 못 찾음)', 'a': '—', 'see': '(약해요)'},
  {'q': '2025년 사진 책상 위 펼친 종이(파란 동그라미 그림)?', 'at': '악마의 대변인 C(그림) · 답을 찾지 못한 물음', 'a': '—', 'see': '(약해요)'},
  {'q': '1611년에 나온 킹 제임스 성경과 이어질까?', 'at': '창 · 헤리퍼드 사슬 도서관에 1611년 성경이 있다는 근거를 못 찾아 넣지 않음', 'a': '킹 제임스 성경 1611년(케임브리지 대학 출판부) — 헤리퍼드와 잇는 근거 없음', 'see': '(약해요)'},
 ],
 'deep': [
  {'h': '책을 눕혀 둔 사슬 도서관', 'img': ['zutphen'], 'p': [
    '네덜란드 쥐트펀의 성 발푸르가 교회 도서관은 1561년에 짓기 시작해 1563년에 마쳤어요. 이곳에서는 책을 선반에 세우지 않고, 교회 독서대 위의 성경처럼 비스듬한 책상에 눕혀 짧은 사슬로 매었어요.',
    '클라크는 쥐트펀 같은 모양을 ‘독서대 방식’이라고 불렀어요. 책이 쌓이자 독서대는 자리를 너무 차지했고, 그래서 책상 위에 선반을 올린 헤리퍼드 같은 책장이 생겼다고 설명했어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>책장을 만든 때</b> 1901년 클라크는 헤리퍼드 책장이 대부분 1394년에 들인 것이라고 보았어요. 1932년 『스펙테이터』의 서평은 클라크가 두 세기나 이르게 잡았다며 1590년의 것이라고 했어요. 지금 대성당과 마파 문디 재단은 1611년에 토머스 손턴이 짓게 했다고 적어요.',
    '<b>새 건물을 연 날</b> 마파 문디 누리집의 사슬 도서관 쪽 글은 1996년 5월 3일, 재단 쪽 글은 5월 5일이라고 적어요. 그래서 이 카드는 ‘1996년 5월’이라고만 썼어요.',
    '<b>중세 손글씨 책의 수</b> 마파 문디 누리집은 227권, 헤리퍼드 대성당 누리집은 229권이라고 적어요.']},
  {'h': '직접 가 보기', 'img': ['clasp'], 'checked': '2026년 11월 18일', 'p': [
    '헤리퍼드 대성당 곁 ‘마파 문디와 사슬 도서관’ 전시관에서 사슬 책장과 지도를 함께 볼 수 있어요. 전시관은 입장료가 있어요.',
    '2026년 9월 14일부터 월~토요일 오전 10시~오후 4시 30분에 열어요. 일요일, 성금요일, 12월 24~26일, 1월 1일에는 닫고, 해마다 1월에는 청소와 보존 작업으로 닫는 때가 있어요. 가기 전에 누리집에서 다시 확인하세요.'],
   'links': [{'t': '마파 문디와 사슬 도서관 — 방문 안내(여는 때·입장료)', 'u': VISIT, 'm': '영어'},
             {'t': 'J. W. 클라크 『The Care of Books』(1901) — 헤리퍼드의 사슬·쇠막대·자물쇠 그림이 실린 책', 'u': CLARK, 'm': '영어'},
             {'t': '헤리퍼드 대성당 — 사슬 도서관 소개', 'u': HCATH, 'm': '영어'}]},
 ],
 'src': [
  {'l': '마파 문디·사슬 도서관 공식 누리집: 마파 문디 — 송아지 가죽 한 장(높이 1.5m쯤), 한가운데 예루살렘, 꼭대기 에덴과 보좌의 그리스도, 그림 500개 넘게·도시 420곳·성경 사건 15가지, 홍해를 지나는 길, 와이강 가의 헤리퍼드, 스코틀랜드 자리의 핏줄 자국, 초록이던 바다(구리 물감) · 2026-11-22 확인', 'u': MAPW},
  {'l': '옥스퍼드 캐비닛(Howard Hotson, 2021) 「Mappa Mundi」 — 13세기 마지막 25년, 위 에덴·가운데 예루살렘·아래 헤라클레스 기둥, 동쪽과 그리스도의 다시 오심, 왼쪽 아래 브리튼 섬들', 'u': CABINET},
  {'l': '영국 상원 회의록 1988년 12월 6일 「The Mappa Mundi」 — 몇 주 전만 해도 아는 사람이 아주 적었다는 몬터규 경의 물음, 입장료를 받아 내보이자는 제안, 정부 답변', 'u': HL88},
  {'l': '영국 하원 서면 답변 1989년 3월 20일 「Mappa Mundi」 — 2월 말 경매에서 거둠, 1,000파운드 주식과 복제본 계획, 게티 100만 파운드·국가 유산 기념 기금 200만 파운드 제안(이때는 받아들여지지 않음)', 'u': HC89},
  {'l': '국가 유산 기념 기금(NHMF): 「Mappa Mundi and Chained Library, Hereford Cathedral」 — 새 재단의 기금 200만 파운드, 1989년 10월 26일', 'u': NHMF},
  {'l': '케임브리지 대학 출판부: B. H. Streeter, 『The Chained Library』(1931; 2011 다시 펴냄) 소개 — 옥스퍼드의 신학자·성경 학자, 1915~1934년 헤리퍼드 참사회원, 도서관을 되살리며 한 연구', 'u': CUPS},
  {'l': '온라인 북스 페이지: B. H. Streeter의 책 — 『The Four Gospels』(Macmillan, 1924)', 'u': FOURG},
  {'l': 'Map of Early Modern London(빅토리아 대학): 「Church of England」 — 1534년 헨리 8세, 1559년 엘리자베스 1세를 잉글랜드 교회의 최고 통치자로, 지금도 영국 왕이 이어 감', 'u': UVIC},
  {'l': 'The Irish Times(2003) 존 폴 게티 2세 부고 — 석유 부자 J. 폴 게티의 아들, 『후즈 후』에 직업을 ‘자선가’로, 국립 미술관 5,000만 파운드, 옛 책을 아낌', 'u': ITGETTY},
  {'l': '런던 국립 미술관(내셔널 갤러리): Sir Paul Getty — 1932~2003, 미술관을 위한 기금, 1998년 영국 시민', 'u': NGETTY},
  {'l': '마파 문디·사슬 도서관 공식 누리집: 사슬 도서관 — 1583년 조사단과 새 규칙, 1590년 성모 경당, 1611년 손턴·옥스퍼드를 본뜸·쇠붙이 주문, 1841년 해체, 1897년 회랑 건물, 1930년 무렵 스트리터·두 곳, 1996년 5월 3일, 책 1,500권쯤(800년 무렵~19세기 초)·중세 손글씨 책 227권·초기 기독교 저술가·교회법과 일반 법·신학, 헤리퍼드 복음서(웨일스에서 만든 가장 오래된 책일지 모름)와 주교·주임 사제의 맹세, 성가대 사제들의 악보 책 · 2026-11-22 다시 확인', 'u': MAPPA},
  {'l': '마파 문디 재단: 재단과 소장품의 역사 — 1980년대 말 적자와 600만 파운드, 지도 한 점이면 필요한 돈이 됨·사슬 도서관을 흩는 것보다 한 점을 파는 편이 나음, 대성당과 나라가 잃을 수 있다는 걱정, 국가 유산 기념 기금·존 폴 게티 2세, 지도와 사슬 도서관을 재단이 맡음, 새 돌 건물, 1996년 5월 5일 개관, 입장료 수입으로 소장품을 돌봄', 'u': TRUST},
  {'l': '마파 문디 재단 첫 화면 — 1988년 재단, 세계 곳곳 사람들의 도움', 'u': 'https://themappamundi.co.uk/'},
  {'l': '헤리퍼드 대성당: 사슬 도서관 — 앞표지에 단 사슬과 선반 아래 쇠막대, 책상에서 읽되 책장을 떠나지 못함, 종이 끝이 밖을 봄, 중세 손글씨 책 229권·두 칸, 1611~1841년의 모습, 돌리지 않고 펼쳐 사슬이 엉키지 않음, 유럽 도서관에서 가장 널리 쓰인 효과적인 보안, 사슬·막대·자물쇠가 온전한 가장 큰 사슬 도서관', 'u': HCATH},
  {'l': 'J. W. Clark, 『The Care of Books』(Cambridge, 1901, Project Gutenberg) — 놋쇠 띠와 쇠고리, 조금 더 큰 고리와 쇠막대, 쇠판·걸쇠·자물쇠, 사슬 길이(3피트 4인치~4피트 3인치)와 돌림고리, 헤리퍼드보다 나은 본보기를 모름, 1394년 추정, 쥐트펀(1561~1563)과 독서대 방식, 목록 액자(17세기 손턴·옥스퍼드와 닮음), 선반마다 막대 셋·세 선반에 자물쇠 하나, 책을 빼고 넣기 번거로움', 'u': CLARKT},
  {'l': 'The Spectator, 1932년 7월 16일 「Books in Chains」(스트리터의 책 서평) — 클라크가 두 세기 이르게 잡음·1590년, 헤리퍼드 방식을 몇 해 뒤 험프리 공작 도서관이 받아들임, 모들린 칼리지 1799년, 헤리퍼드와 길퍼드 문법 학교에 사슬이 남음, 너그러운 기부자의 돈으로 한 복원과 스트리터', 'u': SPECT},
  {'l': 'Guinness World Records: 가장 큰 중세 세계 지도 — 1300년 무렵, 송아지 가죽 한 장, 1.58×1.33m', 'u': 'https://www.guinnessworldrecords.com/world-records/606607-largest-surviving-medieval-world-map'},
  {'l': 'Victoria County History, Oxford 3권 「The Bodleian Library」 — 1600년 보들리 도서관의 쇠창살·사슬 같은 쇠붙이', 'u': 'https://www.british-history.ac.uk/vch/oxon/vol3/pp44-47'},
  {'l': '마파 문디와 사슬 도서관: 방문 안내 — 2026년 9월 14일부터 여는 때, 닫는 날, 입장료 · 2026-11-18 확인', 'u': VISIT},
  {'l': '위키미디어 공용: 옛 그림엽서(Waterlow & Sons 인쇄) 정보', 'u': 'https://commons.wikimedia.org/wiki/File:Postcard_of_The_Chained_Library._Hereford_Cathedral_(undated).jpg'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'chains', 'fit': 'cover', 'p0': '50% 35%', 'p1': '55% 60%', 's0': 1.2, 's1': 1.04, 'kicker': '1611년 · 영국 헤리퍼드 대성당', 'title': '헤리퍼드의 사슬 책장',
   'lines': [{'t': '책마다 쇠사슬이 달린 도서관이 있어요.'}, {'t': '400여 년 전, 책을 지키려고 사슬로 책장에 걸었어요.'}],
   'kid': [{'t': '와, 책마다 쇠사슬이 달려 있어!'}, {'t': '옛날 영국 큰 교회의 도서관이야.'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '책을 묶으라는 규칙'},
  {'type': 'img', 'ch': 1, 'img': 'clasp', 'fit': 'cover', 'p0': '50% 25%', 'p1': '50% 65%', 's0': 1.15, 's1': 1.0, 'cap': '사슬 달린 책들, 헤리퍼드',
   'lines': [{'t': '1583년, 엘리자베스 1세 여왕의 조사단은 대성당 도서관이 허물어져 간다고 보고했어요.'},
             {'t': '새 규칙은 말했어요. 책을 지키려면 사슬로 묶으라고.'},
             {'t': '1611년, 성모 경당에 사슬 책장이 들어섰어요.'}],
   'kid': [{'t': '책을 잘 지키려고 쇠사슬로 묶기로 했대.'}, {'t': '귀한 책을 지키려면 어떻게 할래?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '책장에 사슬 걸기'},
  {'type': 'mod', 'mod': 'place', 'ch': 2,
   'lines': [{'t': '1901년, 옛 도서관을 연구한 클라크의 기록대로 걸어 볼게요.'},
             {'t': '책은 종이 끝이 밖을 보게 꽂고,', 'act': 'book'},
             {'t': '앞표지 고리에 사슬을 걸어요.', 'act': 'chain'},
             {'t': '사슬 끝 고리는 쇠막대에 꿰고,', 'act': 'rod'},
             {'t': '책장 끝에서 쇠막대를 자물쇠로 잠그면,', 'act': 'lock', 'wait': 1200},
             {'t': '책은 앞 책상까지만 내려와요.', 'act': 'read', 'wait': 1500},
             {'t': '읽을 수는 있어도, 가져갈 수는 없게.', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '빈 책장이야. 하나씩 놓아 보자.'}, {'t': '책!', 'act': 'book'}, {'t': '사슬!', 'act': 'chain'}, {'t': '쇠막대!', 'act': 'rod'},
           {'t': '자물쇠, 철컥!', 'act': 'lock', 'wait': 1200}, {'t': '책상에 펼쳐서 읽어!', 'act': 'read', 'wait': 1500},
           {'t': '이 책을 들고 밖에 나갈 수 있을까?', 'act': 'day', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '흩어졌다 다시 모인 책장'},
  {'type': 'img', 'ch': 3, 'img': 'postcard', 'fit': 'cover', 'p0': '35% 50%', 'p1': '60% 50%', 's0': 1.12, 's1': 1.02, 'cap': '옛 그림엽서 · 1930년 무렵 사슬을 다시 단 뒤',
   'lines': [{'t': '1841년, 공사 때문에 사슬을 떼고 책장을 뜯어냈어요.'},
             {'t': '1930년 무렵 사슬을 다시 달았지만, 책장은 두 곳에 나뉘었어요.'}],
   'kid': [{'t': '사슬을 뗐다가, 다시 달았대.'}]},
  {'type': 'img', 'ch': 3, 'img': 'lib2025', 'fit': 'cover', 'p0': '30% 50%', 'p1': '55% 50%', 's0': 1.15, 's1': 1.02, 'cap': '오늘의 사슬 도서관, 2025년',
   'lines': [{'t': '1996년, 책장은 다시 한곳에 모였어요.'}, {'t': '새 건물 안에, 성모 경당 때 모습 그대로예요.'}],
   'kid': [{'t': '이제는 다 같이 한곳에 모였어!'}, {'t': '옛 엽서랑 똑같은 게 보여?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '팔지 않은 책들'},
  {'type': 'img', 'ch': 4, 'img': 'mappa', 'fit': 'contain', 'p0': '50% 50%', 'p1': '50% 45%', 's0': 1.0, 's1': 1.12, 'o': '50% 50%', 'cap': '헤리퍼드 마파 문디, 1300년 무렵',
   'lines': [{'t': '1980년대 끝, 살림이 어려운 대성당은 무엇을 팔지 골라야 했어요.'},
             {'t': '사슬 도서관을 흩지 않으려고, 지도 한 장을 팔려고 했어요.'},
             {'t': '많은 사람이 돈을 보태, 지도도 책도 헤리퍼드에 남았어요.'}],
   'kid': [{'t': '책들을 지키려고 귀한 지도를 팔 뻔했대.'}, {'t': '많은 사람이 도와서 둘 다 지켰어!'}, {'t': '우리가 함께 지키는 건 뭐가 있을까?', 'ask': True}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '책을 당기면, 사슬이 차르륵 따라 내려와요.'}, {'t': '높은 창의 빛이 펼친 책 위로 떨어져요.'}, {'t': '이 책은 내일도 이 자리에 있을 거예요.'}],
   'kid': [{'t': '눈을 감아 봐. 책을 당기면 사슬이 차르륵!'}, {'t': '창으로 햇빛이 들어와.'}, {'t': '이 책은 내일도 여기 있을 거야.'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
