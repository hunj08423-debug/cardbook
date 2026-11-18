# -*- coding: utf-8 -*-
"""깊은 카드: 사슬에 묶인 책(lib-chained) · 중심 방식 = 놓아 보기(도우미: 그때와 지금 탭)
기준서 1판(보탬 10) · 틀 deep3-4 · 키트 3판 · 2026-11-18 37번 묶음 창이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 1611년, 헤리퍼드 대성당 성모 경당에 새 책장이 들어서고
     책마다 사슬이 걸리던 때.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 책 한 권을 책장에 거는 쇠붙이(책·사슬·쇠막대·자물쇠)와
     책상. 1901년 J. W. 클라크가 헤리퍼드 책장을 살펴 적은 그대로, 책 → 사슬 → 쇠막대 → 자물쇠 → 책상 차례로 놓아요.
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
 'lead': '1611년, 영국 헤리퍼드 대성당의 성모 경당에 새 책장이 들어섰어요. 책마다 사슬을 달아 책장에 걸었지요. 1901년의 기록대로, 책 한 권을 사슬에 거는 차례를 따라 책장을 꾸며 보세요.',
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
   'text2': ['1590년, 도서관은 종교개혁 뒤로 쓰지 않던 성모 경당으로 옮겨 갔어요. 1611년에는 도서관 책임자 토머스 손턴(Thomas Thornton)이 그곳에 사슬 도서관을 짓게 했어요.',
             '얼마 전 옥스퍼드 대학에 들어선 도서관들을 본떴어요. 나무 책장은 헤리퍼드에서 짰지만, 쇠붙이는 옥스퍼드에서 주문해야 했어요.'],
   'kid': '옛날 영국 헤리퍼드의 큰 교회에서는, 책을 잘 지키려고 쇠사슬로 묶기로 했대.',
   'kidq': '귀한 책을 지키려면, 너라면 어떻게 할래?'},
  {'id': 'press', 'label': '책장에 사슬 걸기', 'kind': 'mod', 'mod': 'place', 'night': False,
   'text': ['1901년, 영국 케임브리지 대학의 J. W. 클라크(John Willis Clark)가 헤리퍼드의 책장을 꼼꼼히 살펴 그림과 함께 적었어요. 그는 책을 사슬로 묶는 방식을 보여 줄 본보기로 헤리퍼드만 한 곳을 알지 못한다고 했어요.',
            '그 기록대로 책 한 권을 책장에 걸어 보세요. 아래에서 하나씩 골라 놓으면 돼요.'],
   'text2': ['책은 앞 책상까지 내려와 펼칠 수 있지만, 책장을 떠날 수는 없었어요. 클라크가 잰 사슬은 1m에서 1.3m쯤이었어요. 가운데에는 대개 빙글 도는 고리가 있었는데, 클라크는 사슬이 꼬이지 않게 하려는 것 같다고 보았어요.'],
   'kid': '책을 꽂고, 사슬을 달고, 쇠막대에 꿰고, 자물쇠를 채워 볼까? 마지막엔 책상에 펼쳐 읽어!',
   'kidq': '사슬에 묶인 책은 어디까지 데려갈 수 있을까?'},
  {'id': 'apart', 'label': '흩어졌다 다시 모인 책장', 'kind': 'thennow', 'then': 'postcard', 'now': 'lib2025',
   'thenT': '옛 그림엽서', 'nowT': '2025년',
   'text': ['1841년, 성모 경당을 고치는 공사 때문에 사슬 도서관을 뜯어냈어요. 책에서는 사슬을 떼어 냈고, 책상과 의자는 대성당 여기저기에서 다른 데 쓰였어요.',
            '1897년에는 대성당 회랑에 2층 건물을 새로 이어 짓고, 사슬 없는 도서관을 그 위층에 들였어요.'],
   'text2': ['위 엽서에는 찍은 해가 적혀 있지 않아요. 다만 책마다 사슬이 달려 있으니, 1930년 무렵 사슬을 다시 단 뒤의 모습일 거예요.',
             '그때 스트리터(B. H. Streeter) 참사회원이 성모 경당 때의 모습대로 책장을 되살리고 책에 사슬을 다시 달았어요. 하지만 책장은 문서 보관실과 위층 도서관, 두 곳에 나뉘어 있었어요.',
             '1996년 새 도서관 건물이 문을 열자, 사슬 도서관은 다시 한곳에 모였어요. 1611년부터 1841년까지 성모 경당에 있던 그대로 놓였어요.'],
   'kid': '사슬을 뗐다가, 다시 달았다가, 두 곳에 나뉘었다가… 이제는 한곳에 모였대!',
   'kidq': '옛 엽서랑 오늘 사진에서 똑같은 걸 하나 찾아볼까?'},
  {'id': 'keep', 'label': '팔지 않은 책들', 'kind': 'photo', 'img': 'mappa',
   'text': ['1980년대 끝 무렵, 대성당은 해마다 모자라는 살림으로 큰 어려움을 겪었어요. 적어도 600만 파운드의 기금이 있어야 한다는 조언을 듣고, 가진 것을 팔기로 했어요.',
            '대성당은 사슬 도서관의 귀한 책 여러 권을 골라 파는 대신, 1300년 무렵 송아지 가죽 한 장에 그린 세계 지도 「마파 문디(Mappa Mundi)」를 팔려고 했어요. 귀한 책을 골라 팔면 사슬 도서관이 온전하지 못하게 되기 때문이었어요.'],
   'text2': ['곧바로 대성당과 나라가 귀한 유산을 잃을까 걱정하는 목소리가 일었어요. 국가 유산 기념 기금(National Heritage Memorial Fund)과 존 폴 게티 2세(John Paul Getty Jr.), 그리고 세계 곳곳의 사람들이 힘을 보태 새 재단의 기금을 마련했어요.',
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
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>성모 경당</b> 성모 마리아에게 바친 예배당이에요. 종교개혁 뒤로 쓰이지 않다가, 1590년부터 1841년까지 대성당 도서관 자리가 되었어요.',
    '<b>옥스퍼드에서 온 쇠붙이</b> 앞 카드의 보들리안 도서관도 1600년 무렵 방에 쇠창살과 사슬 같은 쇠붙이를 달았어요. 헤리퍼드는 이런 옥스퍼드 도서관들을 본떠, 쇠붙이까지 옥스퍼드에서 들여왔어요.',
    '<b>하나의 자물쇠</b> 클라크가 본 헤리퍼드 책장은 책이 꽂힌 선반 세 칸의 쇠막대를 자물쇠 하나로 함께 잠갔어요.',
    '<b>가장 오래된 책</b> 사슬 도서관에는 책이 1,500권쯤 있어요. 그 가운데 중세 손글씨 책들이 책장 두 칸을 차지하고, 가장 오래된 것은 8세기에 쓴 「헤리퍼드 복음서」예요.',
    '<b>사슬이 사라진 때</b> 사슬 도서관은 생각보다 오래 이어졌어요. 1932년의 한 서평은 옥스퍼드의 모들린 칼리지가 1799년에야 책 사슬을 없앴다고 적었어요.']},
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
  {'l': '마파 문디·사슬 도서관 공식 누리집: 사슬 도서관 — 1583년 조사단과 새 규칙, 1590년 성모 경당, 1611년 손턴·옥스퍼드를 본뜸·쇠붙이 주문, 1841년 해체, 1897년 회랑 건물, 1930년 무렵 스트리터·두 곳, 1996년 5월 3일, 책 1,500권쯤·중세 손글씨 책 227권', 'u': MAPPA},
  {'l': '마파 문디 재단: 재단과 소장품의 역사 — 1980년대 말 적자와 600만 파운드, 사슬 도서관 대신 지도를 팔기로, 국가 유산 기념 기금·존 폴 게티 2세, 지도와 사본을 재단이 맡음, 새 돌 건물, 1996년 5월 5일 개관', 'u': TRUST},
  {'l': '마파 문디 재단 첫 화면 — 1988년 재단, 세계 곳곳 사람들의 도움', 'u': 'https://themappamundi.co.uk/'},
  {'l': '헤리퍼드 대성당: 사슬 도서관 — 앞표지에 단 사슬과 선반 아래 쇠막대, 책상에서 읽되 책장을 떠나지 못함, 종이 끝이 밖을 봄, 중세 손글씨 책 229권·두 칸, 1611~1841년의 모습', 'u': HCATH},
  {'l': 'J. W. Clark, 『The Care of Books』(Cambridge, 1901, Project Gutenberg) — 놋쇠 띠와 쇠고리, 조금 더 큰 고리와 쇠막대, 쇠판·걸쇠·자물쇠, 사슬 길이(3피트 4인치~4피트 3인치)와 돌림고리, 헤리퍼드보다 나은 본보기를 모름, 1394년 추정, 쥐트펀(1561~1563)과 독서대 방식', 'u': CLARKT},
  {'l': 'The Spectator, 1932년 7월 16일 「Books in Chains」(스트리터의 책 서평) — 클라크가 두 세기 이르게 잡음·1590년, 모들린 칼리지 1799년', 'u': SPECT},
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
   'lines': [{'t': '1583년, 여왕의 조사단은 대성당 도서관이 허물어져 간다고 보고했어요.'},
             {'t': '새 규칙은 말했어요. 책을 지키려면 사슬로 묶으라고.'},
             {'t': '1611년, 성모 경당에 사슬 책장이 들어섰어요.'}],
   'kid': [{'t': '책을 잘 지키려고 쇠사슬로 묶기로 했대.'}, {'t': '귀한 책을 지키려면 어떻게 할래?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '책장에 사슬 걸기'},
  {'type': 'mod', 'mod': 'place', 'ch': 2,
   'lines': [{'t': '1901년 클라크의 기록대로, 책 한 권을 걸어 볼게요.'},
             {'t': '책은 종이 끝이 밖을 보게 꽂고,', 'act': 'book'},
             {'t': '앞표지 고리에 사슬을 걸어요.', 'act': 'chain'},
             {'t': '사슬 끝 고리는 쇠막대에 꿰고,', 'act': 'rod'},
             {'t': '책장 끝에서 자물쇠를 채우면,', 'act': 'lock', 'wait': 1200},
             {'t': '책은 앞 책상까지만 내려와요.', 'act': 'read', 'wait': 1500},
             {'t': '읽을 수는 있어도, 가져갈 수는 없게.', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '빈 책장이야. 하나씩 놓아 보자.'}, {'t': '책!', 'act': 'book'}, {'t': '사슬!', 'act': 'chain'}, {'t': '쇠막대!', 'act': 'rod'},
           {'t': '자물쇠, 철컥!', 'act': 'lock', 'wait': 1200}, {'t': '책상에 펼쳐서 읽어!', 'act': 'read', 'wait': 1500},
           {'t': '이 책을 들고 밖에 나갈 수 있을까?', 'act': 'day', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '흩어졌다 다시 모인 책장'},
  {'type': 'img', 'ch': 3, 'img': 'postcard', 'fit': 'cover', 'p0': '35% 50%', 'p1': '60% 50%', 's0': 1.12, 's1': 1.02, 'cap': '옛 그림엽서 속 사슬 도서관',
   'lines': [{'t': '1841년, 공사 때문에 사슬을 떼고 책장을 뜯어냈어요.'},
             {'t': '1930년 무렵 사슬을 다시 달았지만, 책장은 두 곳에 나뉘었어요.'}],
   'kid': [{'t': '사슬을 뗐다가, 다시 달았대.'}]},
  {'type': 'img', 'ch': 3, 'img': 'lib2025', 'fit': 'cover', 'p0': '30% 50%', 'p1': '55% 50%', 's0': 1.15, 's1': 1.02, 'cap': '오늘의 사슬 도서관, 2025년',
   'lines': [{'t': '1996년, 책장은 다시 한곳에 모였어요.'}, {'t': '1611년 성모 경당에 있던 그대로예요.'}],
   'kid': [{'t': '이제는 다 같이 한곳에 모였어!'}, {'t': '옛 엽서랑 똑같은 게 보여?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '팔지 않은 책들'},
  {'type': 'img', 'ch': 4, 'img': 'mappa', 'fit': 'contain', 'p0': '50% 50%', 'p1': '50% 45%', 's0': 1.0, 's1': 1.12, 'o': '50% 50%', 'cap': '헤리퍼드 마파 문디, 1300년 무렵',
   'lines': [{'t': '1980년대 끝, 살림이 어려운 대성당은 무엇을 팔지 골라야 했어요.'},
             {'t': '사슬 도서관을 흩지 않으려고, 지도 한 장을 팔려고 했어요.'},
             {'t': '많은 사람이 힘을 보태, 지도도 책도 헤리퍼드에 남았어요.'}],
   'kid': [{'t': '책들을 지키려고 귀한 지도를 팔 뻔했대.'}, {'t': '많은 사람이 도와서 둘 다 지켰어!'}, {'t': '우리가 함께 지키는 건 뭐가 있을까?', 'ask': True}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '책을 당기면, 사슬이 차르륵 따라 내려와요.'}, {'t': '높은 창의 빛이 펼친 책 위로 떨어져요.'}, {'t': '이 책은 내일도 이 자리에 있을 거예요.'}],
   'kid': [{'t': '눈을 감아 봐. 책을 당기면 사슬이 차르륵!'}, {'t': '창으로 햇빛이 들어와.'}, {'t': '이 책은 내일도 여기 있을 거야.'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
