# -*- coding: utf-8 -*-
"""깊은 카드: 세계 첫 성탄 카드(cus-card) · 중심 방식 = 만드는 차례(steps · 키트 3판 새 방식)
기준서 1판(보탬 10) · 틀 deep3-4 · 키트 3판 · 2026-11-18 4번 묶음 창이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 1843년 12월 런던. 17일 저녁 화가 호슬리가 카드 그림을 들고 헨리 콜을 찾아온 뒤
     (콜의 일기, V&A), 그 그림이 돌판에 찍히고 한 장씩 손으로 색칠되던 때
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 카드가 실제로 만들어진 차례(밑그림 → 석판 인쇄(잡스 인쇄소) →
     손 색칠(윌리엄 메이슨) → 가게(서머리의 홈 트레저리, 1실링) → 받는 사람·보내는 사람 손글씨 → 1페니 우편)를 한 단계씩
카드 크기: 큰 카드(장면 4개) — 1840년 첫 우표 편지, 서로 다른 두 장의 카드 사진, 콜의 일기와 박물관·경매 기록.
새 방식 견주기: 따라 쓰기는 따라 쓸 정해진 글씨가 없고, 흩어진 조각 모으기는 남은 카드가 한 물건의 조각이 아니며,
찾아보기는 앞면 이야기가 그림 속을 이미 설명해서 만드는 차례를 골랐어요.
만드는 차례 그림은 이 안내서가 1843년 카드(퍼블릭 도메인)의 짜임을 바탕으로 간단히 줄여 그린 SVG예요(아래 함수).
그림 원본(src)은 deep_src/cus-card/ (저장소 밖)."""
S = 'cus-card/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

VA = 'https://www.vam.ac.uk/articles/the-first-christmas-card'
CT = 'https://theculturetrip.com/europe/united-kingdom/england/london/articles/the-tale-of-the-first-ever-christmas-card-and-its-fascinating-design-evolution'
BOD = 'https://blogs.bodleian.ox.ac.uk/jjcoll/tag/christmas-cards/'
NPM = 'https://postalmuseum.si.edu/exhibition/the-queen%E2%80%99s-own-postal-reforms-that-transformed-the-mail/the-worlds-first-postage-stamps'
BRIT = 'https://www.britannica.com/technology/lithography'
HOI = 'https://historyofinformation.com/detail.php?entryid=3738'
ME = 'https://www.mediastorehouse.com/photo-prints/mary-evans-prints-online/may-1st-1843-english-academic-painter-27970032.html'
GWR = 'https://www.guinnessworldrecords.com/world-records/77401-first-printed-christmas-card'
RJ = 'https://www.london-walking-tours.co.uk/dickens-london/henry-cole-first-christmas-card.htm'
WPC = 'https://en.wikipedia.org/wiki/Christmas_card'

# ── 만드는 차례 그림(이 안내서가 그린 SVG) ───────────────────────────────
PENCIL = '#9a9184'
INK = '#3d2b1f'
HAND = '#2c3e6b'
SKIN = '#f1cdb0'

def leaf(x, y, s=1.0, rot=0):
    """담쟁이 잎 하나(작은 하트 모양)."""
    return (f'<path transform="translate({x} {y}) rotate({rot}) scale({s})" '
            'd="M0 9 C-2 6 -6 5 -8 2 C-9 -1 -7 -3 -5 -3 C-5 -6 -3 -9 0 -9 C3 -9 5 -6 5 -3 C7 -3 9 -1 8 2 C6 5 2 6 0 9 Z M0 8 L0 -5"/>')

# ── 선(연필 밑그림과 인쇄 먹선이 같은 모양을 써요) ──────────────────────────
def branch_paths():
    """나뭇가지 틀: 굵은 가지 선과 마디."""
    p = []
    # 왼쪽 칸 기둥 둘, 오른쪽 칸 기둥 둘
    for x in (50, 146, 314, 410):
        p.append(f'M{x} 58 Q{x - 2} 160 {x + 1} 262')
    # 위 가로 가지(길게)와 아래 가로 가지
    p.append('M42 62 Q230 54 418 62')
    p.append('M44 256 Q98 252 152 258')
    p.append('M308 258 Q362 252 416 256')
    # 양옆 칸 가운데 가로 가지(장면과 담쟁이 칸을 나눔)
    p.append('M50 176 Q98 172 146 177')
    p.append('M314 177 Q362 172 410 176')
    # 가운데 둥근 가지(아치)
    p.append('M146 108 Q160 70 230 64 Q300 70 314 108')
    p.append('M150 92 Q190 76 230 80 Q270 76 310 92')
    # 위에서 엇갈린 가지
    p.append('M206 58 L254 70 M206 70 L254 58')
    return p

def vine_paths():
    p = []
    for x0 in (56, 320):
        p.append(f'M{x0} 236 q14 -22 30 -8 t28 -4 q10 -18 26 -6')
        p.append(f'M{x0 + 4} 204 q16 -14 30 0 t26 2')
    return p

def figure_paths():
    """사람은 머리(동그라미)와 몸(사다리꼴)로만 줄였어요."""
    heads = [  # (x, y, r)
        (120, 92, 7), (78, 102, 6.5), (98, 140, 5),          # 왼쪽 칸: 먹을 것 나누기
        (344, 92, 7), (378, 128, 5.5),                        # 오른쪽 칸: 옷 입히기
        (172, 118, 8), (194, 112, 8.5), (212, 128, 6), (222, 106, 5.5),   # 가운데 가족(왼쪽 무리)
        (246, 110, 8), (266, 116, 7.5), (288, 118, 7.5), (234, 146, 6)]   # 가운데 가족(오른쪽 무리)
    bodies = [
        'M112 100 L106 160 L134 160 L128 100 Z',               # 나누어 주는 사람
        'M72 108 L64 164 L92 164 L86 108 Z',                   # 받는 사람
        'M94 145 L90 168 L106 168 L102 145 Z',                 # 아이
        'M336 100 L330 166 L360 166 L352 100 Z',               # 옷을 건네는 사람
        'M372 134 L368 168 L388 168 L384 134 Z',               # 아이
        'M160 128 Q172 124 186 128 L190 176 L156 176 Z',       # 할머니
        'M182 122 L178 176 L212 176 L206 122 Z',               # 할아버지
        'M206 134 L204 168 L220 168 L218 134 Z',
        'M236 120 L232 176 L262 176 L256 120 Z',
        'M256 126 L254 176 L282 176 L276 126 Z',
        'M278 128 L276 176 L304 176 L298 128 Z',
        'M228 152 L226 176 L242 176 L240 152 Z']
    extra = [
        'M114 112 L94 118', 'M80 119 Q88 124 96 119',         # 그릇을 내미는 팔과 그릇
        'M352 112 Q378 112 390 140 L386 168 L364 168 Q368 140 352 124',   # 아이에게 덮어 주는 옷
        'M164 112 Q172 102 181 112',                           # 할머니 모자
        'M150 178 L310 178',                                   # 식탁 끝
        'M217 111 Q222 124 228 111']                           # 들어 올린 아기의 포대기
    glasses = [(186, 136), (202, 132), (250, 130), (270, 136), (292, 138)]
    g = ''.join(f'<path d="M{x - 3} {y} L{x + 3} {y} L{x + 1} {y + 6} L{x - 1} {y + 6} Z M{x} {y + 6} L{x} {y + 9} M{x - 2} {y + 9} L{x + 2} {y + 9}"/>' for x, y in glasses)
    return heads, bodies, extra, glasses, g

BANNER = 'M156 180 L304 180 L304 236 Q230 258 156 236 Z'
LEAVES = [(50, 80, 1, -20), (52, 132, .9, 30), (146, 70, 1, 15), (148, 150, .9, -25), (314, 72, 1, -15), (312, 148, .9, 25),
          (410, 84, 1, 20), (408, 136, .9, -30), (120, 60, .9, 0), (340, 60, .9, 10), (70, 214, 1, 10), (102, 230, .9, -20),
          (128, 206, .8, 30), (334, 214, 1, -10), (366, 230, .9, 20), (392, 206, .8, -30), (230, 60, .8, 0)]

def lines(stroke, width, dash=''):
    heads, bodies, extra, glasses, gl = figure_paths()
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s = (f'<g fill="none" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{d}>'
         + ''.join(f'<path d="{p}" stroke-width="{width * 2.6:.1f}"/>' for p in branch_paths())
         + ''.join(f'<path d="{p}"/>' for p in vine_paths())
         + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in heads)
         + ''.join(f'<path d="{p}"/>' for p in bodies)
         + ''.join(f'<path d="{p}"/>' for p in extra)
         + gl
         + f'<path d="{BANNER}"/>'
         + ''.join(leaf(x, y, s, r) for x, y, s, r in LEAVES)
         + '</g>')
    return s

def printed_text():
    """석판으로 함께 찍힌 글자(인사말 · 가게 이름 · To/From 칸)."""
    f = "font-family=\"Georgia, 'Times New Roman', serif\""
    return (f'<g fill="{INK}" {f}>'
            '<text x="230" y="200" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="1">A MERRY CHRISTMAS</text>'
            '<text x="230" y="212" font-size="7.5" font-weight="700" text-anchor="middle" letter-spacing="1">AND</text>'
            '<text x="230" y="225" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="1">A HAPPY NEW YEAR</text>'
            '<text x="230" y="238" font-size="7.5" font-weight="700" text-anchor="middle" letter-spacing="1">TO YOU</text>'
            '<text x="44" y="47" font-size="10" font-style="italic">To</text>'
            '<text x="40" y="276" font-size="5.6">Published at Summerly’s Home Treasury Office,</text>'
            '<text x="64" y="284" font-size="5.6">12 Old Bond Street, London.</text>'
            '<text x="228" y="281" font-size="9" font-style="italic">From</text>'
            '</g>'
            f'<g stroke="{INK}" stroke-width=".9" stroke-dasharray="1 2.4" fill="none"><path d="M60 47 L300 47"/><path d="M254 281 L420 281"/></g>')

def colours():
    """3단계: 손으로 칠한 색(가운데 가족 · 띠 · 잎). 양옆 나눔 장면은 칠하지 않아요(V&A 설명)."""
    heads, bodies, extra, glasses, gl = figure_paths()
    cols = ['#6d5a86', '#5c4434', '#9b3d3d', '#3f4f6b', '#8c4a5c', '#7f9cc4', '#c48f3f']   # 가운데 7명의 옷
    body_fill = ''.join(f'<path d="{bodies[5 + i]}" fill="{c}"/>' for i, c in enumerate(cols))
    face_fill = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SKIN}"/>' for x, y, r in heads[5:])
    hat = '<path d="M164 112 Q172 102 181 112 Z" fill="#f4efe6"/>'
    wine = ''.join(f'<path d="M{x - 3} {y} L{x + 3} {y} L{x + 1} {y + 6} L{x - 1} {y + 6} Z" fill="#a8263a"/>' for x, y in glasses)
    banner = f'<path d="{BANNER}" fill="#e8b4b8" opacity=".9"/>'
    leaves = '<g fill="#c9a548">' + ''.join(leaf(x, y, s, r) for x, y, s, r in LEAVES) + '</g>'
    return f'<g data-s="3">{banner}{body_fill}{face_fill}{hat}{wine}{leaves}</g>'

def tag():
    """4단계: 가게 꼬리표(1실링). 5단계에 사라져요(팔렸어요)."""
    return ('<g data-s="4" data-off="5">'
            '<path d="M402 34 Q410 22 418 14" fill="none" stroke="#7a6a4f" stroke-width="1.2"/>'
            '<path d="M416 8 L452 8 L452 44 L416 44 L406 26 Z" fill="#fbf6ea" stroke="#7a6a4f" stroke-width="1.2"/>'
            '<circle cx="414" cy="26" r="2" fill="none" stroke="#7a6a4f"/>'
            f'<text x="433" y="29" font-size="13" font-weight="700" text-anchor="middle" fill="{INK}" font-family="Georgia, serif">1s.</text>'
            '<text x="433" y="40" font-size="6.5" text-anchor="middle" fill="#6b5a40">1실링</text></g>')

def handwriting():
    """5단계: 받는 사람 · 보내는 사람. 2001년 경매에 나온 콜 부부의 카드(받는 사람 ‘할머니와 샤 이모’)를 바탕으로 옮겨 썼어요."""
    f = "font-family=\"'Segoe Script', 'Snell Roundhand', Georgia, serif\" font-style=\"italic\""
    return (f'<g data-s="5" fill="{HAND}" {f}>'
            '<text x="66" y="45" font-size="12">Granny &amp; Aunt Char</text>'
            '<text x="262" y="279" font-size="11">Henry &amp; Marian Cole</text></g>')

def post():
    """6단계: 봉투에 넣고 1페니 우표(1843년이면 빨간 1페니 우표)."""
    return ('<g data-s="6">'
            '<path d="M22 200 L438 200 L438 316 L22 316 Z" fill="#efe4cc" stroke="#b9a77f" stroke-width="1.2"/>'
            '<path d="M22 200 L230 262 L438 200" fill="none" stroke="#b9a77f" stroke-width="1.2"/>'
            '<rect x="392" y="208" width="32" height="38" fill="#b4262f"/>'
            '<rect x="395" y="211" width="26" height="32" fill="none" stroke="#f3d6d0" stroke-width=".8"/>'
            '<ellipse cx="408" cy="225" rx="7.5" ry="9" fill="#f3d6d0"/>'
            '<text x="408" y="243" font-size="4.6" text-anchor="middle" fill="#f3d6d0" font-family="Georgia, serif">ONE PENNY</text>'
            f'<text x="120" y="292" font-size="12" fill="{HAND}" font-family="\'Segoe Script\', \'Snell Roundhand\', Georgia, serif" font-style="italic">Granny &amp; Aunt Char</text>'
            '</g>')

def svg(uid='cc'):
    return ('<svg viewBox="0 0 460 320" xmlns="http://www.w3.org/2000/svg">'
            '<rect x="30" y="28" width="400" height="264" rx="4" fill="#f7f0e1" stroke="#d6c7a6"/>'
            + colours()
            + f'<g data-s="1" data-off="2">{lines(PENCIL, 0.8, "3 2")}</g>'
            + f'<g data-s="2">{lines(INK, 1.0)}{printed_text()}</g>'
            + tag() + handwriting() + post()
            + '</svg>')


CARD = {
 'id': 'cus-card', 'mode': '만드는 차례',
 'pagetitle': '세계 첫 성탄 카드',
 'brandsub': '깊은 카드 · 만드는 차례',
 'where': '<b>1843년 12월</b><span>영국 · 런던</span>',
 'lead': '1843년 12월 런던, 바쁜 헨리 콜의 책상에는 답장하지 못한 편지가 쌓여 있었어요. 친구인 화가가 그린 그림을 돌판으로 찍고 한 장씩 붓으로 칠해, 세계 첫 성탄 카드가 만들어졌어요. 단추를 눌러 그 차례를 한 단계씩 따라가 보세요.',
 'leadKid': '편지가 산더미처럼 쌓인 콜 아저씨가 그림 카드를 만들었대. 돌판으로 찍고, 붓으로 칠하고, 이름을 써서 보냈어. 같이 만들어 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 1판 보탬 10). 장면에는 박물관·도서관·경매 기록에 있는 것만 옮겼고, 기록마다 다른 점은 따로 적었어요. 만드는 차례 그림은 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#2e5a46;--accent-ink:#f7fbf8;--soft:rgba(46,90,70,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#93c2ab;--accent-ink:#0f1a15;--soft:rgba(147,194,171,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#93c2ab;--accent-ink:#0f1a15;--soft:rgba(147,194,171,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '첫 카드', 'y': '1843', 'sub': '런던 · 영국'},
 'doneNote': '올해 ‘받는 사람’ 칸에 가장 먼저 쓰고 싶은 이름은 누구인가요?',
 'images': {
  'card': {'src': S + 'Firstchristmascard.jpg', 'cap': '첫 상업용 성탄 카드, 1843년 · 남아 있는 카드 가운데 한 장', 'cr': '그림 존 콜콧 호슬리 · 퍼블릭 도메인 · 위키미디어 공용',
           'u': 'https://commons.wikimedia.org/wiki/File:Firstchristmascard.jpg',
           'alt': '나뭇가지를 엮은 틀 안에 세 칸 그림이 있다. 가운데에서는 할머니·할아버지부터 아이까지 한 가족이 붉은 포도주 잔을 들고 웃는다. 왼쪽 칸에서는 한 사람이 그릇에 담은 음식을 건네고, 오른쪽 칸에서는 한 여인이 아이에게 옷을 덮어 준다. 아래 분홍 띠에 ‘A MERRY CHRISTMAS AND A HAPPY NEW YEAR TO YOU’라고 적혀 있다. 틀의 잎은 금빛으로 칠해져 있고, 맨 위와 아래 빈칸, 오른쪽 가장자리에 펜으로 쓴 손글씨가 있다.'},
  'copy2': {'src': S + 'FirstX-MasPostcard1843.jpg', 'max': 1600, 'cap': '같은 카드의 또 다른 한 장(앨런 허긴스 소장) · 맨 위와 아래 칸에 다른 손글씨가 있어요', 'cr': '그림 존 콜콧 호슬리 · 퍼블릭 도메인 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:FirstX-MasPostcard1843.jpg',
            'alt': '같은 그림의 카드 한 장. 전체가 누렇고 갈색을 띠며, 가운데 띠도 갈색빛 분홍이다. 가운데 가족의 옷은 보라와 파랑, 갈색으로 칠해져 있다. 맨 위 ‘To’ 뒤와 아래 ‘From’ 뒤에 펜으로 쓴 이름이 있다. 인쇄된 사진을 다시 찍은 듯 잔 점무늬가 보인다.'},
  'post': {'src': S + 'Stamp_GB-Penny_Black_first_day_cover.jpg', 'cap': '첫 우표 ‘페니 블랙’을 붙여 1840년 5월 6일에 보낸 편지 · 우표를 쓸 수 있게 된 첫날이에요', 'cr': '영국 우정청(GPO) 우표 · 퍼블릭 도메인 · 위키미디어 공용',
           'u': 'https://commons.wikimedia.org/wiki/File:Stamp_GB-Penny_Black_first_day_cover.jpg',
           'alt': '종이를 접어 봉한 누런 편지 한 통. 오른쪽에 검은 우표가 붙어 있는데, 왼쪽을 바라보는 젊은 여왕의 옆얼굴 위에 ‘POSTAGE’, 아래에 ‘ONE PENNY’라고 찍혀 있다. 우표 위에 붉은 소인이 희미하게 겹쳐 있고, 아래에 펜으로 받는 곳이 세 줄 적혀 있다. 왼쪽 위에 둥근 도장이 찍혀 있다.'},
 },
 'scenes': [
  {'id': 'letters', 'label': '답장이 밀린 12월', 'kind': 'photo', 'img': 'post',
   'text': ['1840년 1월 10일, 영국은 반 온스(약 14그램)까지의 편지를 어디로 보내든 1페니만 받기로 했어요. 그해 5월 6일부터는 값을 미리 치렀다는 표시로 우표를 붙였어요. 헨리 콜은 이 ‘1페니 우편’을 이끈 로랜드 힐(Rowland Hill)과 함께 일한 사람이에요.',
            '런던의 빅토리아 앨버트 박물관(V&A)에 따르면, 1843년 성탄이 다가오자 바쁜 콜의 책상에는 답장하지 못한 편지가 쌓여 있었어요. 콜은 시간을 아낄 꾀를 내어, 친구인 화가 존 콜콧 호슬리(John Callcott Horsley)에게 그림을 부탁했어요.'],
   'kid': '편지 보내는 값이 1페니로 싸지자 편지가 많이 오갔어. 콜 아저씨 책상에도 답장 못 한 편지가 잔뜩 쌓였대.',
   'kidq': '답장할 편지가 산더미처럼 쌓이면, 너라면 어떻게 할래?'},
  {'id': 'evening', 'label': '12월 17일 저녁', 'kind': 'photo', 'img': 'card',
   'text': ['콜의 일기에는 그날 저녁이 한 줄로 남아 있어요.'],
   'quote': {'t': '저녁에 호슬리가 와서, 성탄 카드 그림을 가져왔다.', 'from': '헨리 콜의 일기, 1843년 12월 17일 · 이 안내서가 옮김', 'u': VA},
   'text2': ['그림은 세 칸이에요. 가운데에서는 한 가족이 잔을 들고, 양옆에서는 가난한 이웃에게 먹을 것과 옷을 건네요. V&A는 가운데 그림을 손으로 칠하고, 양옆 나눔 장면은 흑백으로 두었다고 설명해요.'],
   'kid': '콜 아저씨 친구인 화가가 저녁에 카드 그림을 가져왔대. 가운데는 가족이 잔을 들고 ‘메리 크리스마스!’ 하는 그림이야.',
   'kidq': '카드 그림을 부탁받는다면, 너는 가운데에 무엇을 그릴래?'},
  {'id': 'make', 'label': '한 장씩, 손으로', 'kind': 'mod', 'mod': 'steps', 'night': False,   # ← 그 자리에 있고 싶은 한 순간(한가운데 장면)
   'text': ['그림은 돌판에 옮겨 찍었어요. 이렇게 돌판으로 찍는 방법을 석판 인쇄라고 해요. 물에 떨어뜨린 기름이 물과 섞이지 않는 것처럼, 기름 크레용으로 그린 곳에만 잉크가 묻고 물에 젖은 곳은 잉크를 밀어내요.',
            '런던 홀번의 워릭 코트에 있던 인쇄소 잡스(Jobbins)가 1,000장을 찍었고, 색칠을 일로 하는 ‘색칠장이’ 윌리엄 메이슨(William Mason)이 붓으로 색을 칠했어요. 아래 단추를 눌러 그 차례를 따라가 보세요.'],
   'kid': '돌판을 커다란 도장처럼 써서 똑같은 그림을 여러 장 찍었어. 그다음엔 붓으로 한 장씩 색칠했대.',
   'kidq': '붓으로 칠한다면, 너는 무슨 색부터 칠할래?'},
  {'id': 'left', 'label': '남은 카드들', 'kind': 'photo', 'img': 'copy2',
   'text': ['카드는 한 장에 1실링이었어요. V&A의 큐레이터는 일하는 사람의 하루 품삯쯤이었다고 말해요. 콜이 쓰고 남은 카드는 함께 일하던 출판업자 조지프 컨들(Joseph Cundall)이 ‘서머리의 홈 트레저리’ 가게에서 팔았어요. ‘서머리’는 콜이 컨들과 일할 때 쓰던 다른 이름이에요.',
            '이 사진은 같은 카드의 또 다른 한 장이에요. 앞 장면의 카드와 견주어 보면 띠와 옷의 색이 다르고, 맨 위와 아래 칸의 손글씨도 달라요.'],
   'text2': ['콜이 가진 카드에는 호슬리가 서명 대신 오른쪽 아래에 아주 작은 자기 얼굴을 그리고 ‘Xmasse, 1843’이라고 적었어요. 헨리와 메리언 콜이 ‘할머니와 샤 이모(Granny and Aunt Char)’에게 보낸 카드는 2001년 11월 24일 영국 디바이지스의 경매에 나왔어요. 두 사람의 서명이 그대로 남아 있었어요.'],
   'kid': '남은 카드마다 이름이 다르게 쓰여 있어. 화가 아저씨는 콜 아저씨 카드에 자기 얼굴을 쪼그맣게 그려 넣었대!',
   'kidq': '앞의 카드와 이 카드, 무슨 색이 달라 보여?'},
 ],
 'imagine': {'t': '1843년 12월 런던의 저녁. 창밖으로 마차 바퀴가 덜컹거리며 지나가요. 책상 위에는 아직 답장하지 못한 편지 더미, 막 마른 카드에서 나는 물감 냄새. 펜촉이 ‘To’ 뒤의 빈칸을 사각사각 채워요.',
             'kid': '눈을 감아 봐. 마차 소리가 덜컹덜컹. 펜으로 할머니 이름을 사각사각 써.'},
 'lines': ['그린 손, 찍은 손, 칠한 손, 쓴 손.', '받는 사람 칸은 비워 두고 찍었어요.', '1페니면 어디든 가는 인사.'],
 'linesKid': ['돌판으로 꾹, 붓으로 슥슥.', '할머니께, 콜 부부가.'],
 'goals': {
  's4': {'t': '여섯 단계 끝까지', 'p': '첫 성탄 카드를 여섯 단계 끝까지 만들어 보면 카드에 금박이 입혀져요.', 'how': '‘그림 그리기’부터 여섯 단계를 끝까지 해 보세요', 'done': '첫 성탄 카드를 끝까지 만들어 봤어요',
         'ways': [{'id': 'steps', 't': '여섯 단계를 끝까지 해 보기'}]},
  's5': {'t': '아이와 함께', 'p': '아이와 함께 ‘영화처럼 보기’를 끝까지 보면 카드가 채색돼요.', 'how': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'done': '아이와 함께 끝까지 봤어요',
         'ways': [{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'steps': {
   'svg': svg(),
   'alt': '이 안내서가 그린 첫 성탄 카드. 단계마다 연필 밑그림, 인쇄한 갈색 선과 글자, 붓으로 칠한 색, 1실링 꼬리표, 손글씨 이름, 봉투와 빨간 우표가 더해져요.',
   'cap': '이 안내서가 그린 첫 성탄 카드의 짜임 · 1843년 카드(퍼블릭 도메인)를 바탕으로 사람과 틀을 간단히 줄여 그렸어요 · 손글씨 이름은 2001년 경매에 나온 콜 부부의 카드(경매 회사 설명)를 바탕으로 썼어요',
   'intro': '단추를 누를 때마다 첫 성탄 카드가 한 단계씩 만들어져요.',
   'hint': '아래 ‘그림 그리기’부터 눌러 보세요.',
   'marksLabel': '카드 한 장에 닿은 손',
   'marks': [{'t': '그린 손 · 호슬리', 'c': PENCIL, 's': 1}, {'t': '찍은 손 · 잡스 인쇄소', 'c': INK, 's': 2},
             {'t': '칠한 손 · 메이슨', 'c': '#a8263a', 's': 3}, {'t': '쓴 손 · 보내는 사람', 'c': HAND, 's': 5}],
   'steps': [{'do': '그림 그리기', 't': '호슬리의 그림', 'p': '화가 호슬리가 나뭇가지 틀과 세 칸 그림, 인사말 띠를 그렸어요. 콜의 일기를 보면 12월 17일 저녁에 이 그림을 가져왔어요.'},
             {'do': '돌판에 찍기', 't': '석판 인쇄', 'p': '그림을 기름 크레용으로 돌판에 옮기고, 물을 적신 뒤 잉크를 바르면 그림에만 잉크가 묻어요. 잡스 인쇄소가 이렇게 1,000장을 찍었어요. 인사말과 가게 이름, ‘To’와 ‘From’ 글자도 카드에 인쇄되어 있어요.'},
             {'do': '붓으로 칠하기', 't': '한 장씩 손으로', 'p': '색칠장이 윌리엄 메이슨이 붓으로 칠했어요. 이 그림에서는 V&A의 설명대로 양옆 나눔 장면은 흑백으로 두고, 남은 카드 사진을 보며 가운데 가족과 띠, 틀의 잎을 칠했어요.'},
             {'do': '가게에 내놓기', 't': '한 장에 1실링', 'p': '카드 아래에 ‘서머리의 홈 트레저리 가게, 올드 본드 거리 12번지’라고 찍혀 있어요. 콜이 쓰고 남은 카드를 이 가게에서 팔았어요.'},
             {'do': '이름 쓰기', 't': '받는 사람 · 보내는 사람', 'p': '맨 위와 아래 빈칸에 손으로 이름을 적어요. 헨리와 메리언 콜은 ‘할머니와 샤 이모’에게 보내는 카드에 두 사람의 이름을 적었어요.'},
             {'do': '우편으로 보내기', 't': '1페니면 어디든', 'p': '1840년부터는 반 온스(약 14그램)까지의 편지를 영국 어디로든 1페니에 보낼 수 있었어요. 콜이 함께 일한 ‘1페니 우편’이에요.'}],
   'done': '다 만들었어요. 한 사람이 그리고, 한 곳에서 찍고, 한 사람이 칠하고, 보내는 사람이 이름을 써서, 첫 성탄 카드 한 장이 길을 떠났어요.',
 }},
 'deep': [
  {'h': '알고 보면', 'p': [
   '<b>석판 인쇄</b> 1798년 독일 뮌헨의 알로이스 제네펠더가 찾아낸 인쇄법이에요. 기름과 물이 섞이지 않는 성질을 써서, 평평한 판에 그린 그림을 여러 장 찍어 내요.',
   '<b>둘째 성탄 카드</b> 다음 성탄 카드는 1848년에 화가 윌리엄 모 에글리(William Maw Egley)가 그렸어요. 날짜 ‘1848’을 ‘1842’로 잘못 읽어 한때 이 카드가 첫 카드로 여겨졌어요. 에글리의 카드도 즐거운 잔치와 이웃 돕기를 함께 그렸어요.',
   '<b>반 페니 우편</b> 1894년 반 페니 우편이 생기자 성탄 카드가 더 많이 팔렸어요.']},
  {'h': '기록마다 다른 점', 'p': [
   '<b>몇 장을 찍었나</b> V&A와 큐레이터 인터뷰는 약 1,000장이라고 해요. 두 번에 걸쳐 모두 2,050장(첫 인쇄 1,000장)을 찍었다는 기록도 있어요. 색을 칠하지 않은 흑백 카드는 6펜스에 팔았다는 이야기도 전해져요(런던 역사 해설가 리처드 존스).',
   '<b>잘 팔렸나</b> V&A는 장사로는 실패였다고 하고, 큐레이터 인터뷰도 값이 비싸다는 말을 들었다고 해요. 옥스퍼드 보들리언 도서관의 글은 ‘잘 팔렸지만’이라고 적었어요.',
   '<b>그림을 그린 때</b> 콜의 일기에는 1843년 12월 17일 저녁에 그림이 왔다고 적혀 있어요. 같은 해 5월 1일에 그렸다고 적은 자료도 있어요.',
   '<b>남은 카드</b> 1977년 케네스 로(Kenneth Rowe)가 찾아낸 카드는 21장이었어요. 기네스 세계 기록과 위키백과(영어)는 열두 장이 남았다고 적었어요.',
   '<b>2001년 경매</b> 값은 경매 회사의 사진 설명에 2만 2,500파운드, 기네스 세계 기록에 2만 파운드, 위키백과(영어)에 2만 2,250파운드로 적혀 있어요. 받는 사람도 경매 회사 설명은 ‘할머니와 샤 이모’, 기네스는 ‘어머니’라고 달리 적었어요.']},
  {'h': '더 보기', 'p': ['처음 만든 사람들의 기록을 직접 읽어 볼 수 있어요.'],
   'links': [{'t': 'V&A 박물관: 첫 성탄 카드 이야기와 콜의 일기, 둘째 카드', 'u': VA, 'm': '영어'},
             {'t': '옥스퍼드 보들리언 도서관 존 존슨 모음: 성탄 카드가 걸어온 길', 'u': BOD, 'm': '영어'},
             {'t': '스미스소니언 국립 우편 박물관: 세계 첫 우표와 1페니 우편', 'u': NPM, 'm': '영어'}]},
 ],
 'src': [
  {'l': 'V&A 박물관 「The first Christmas card」 — 콜의 일기(1843년 12월 17일), 바쁜 콜과 답장 못 한 편지, 친구 호슬리에게 부탁, 가운데만 손 색칠·양옆 흑백, 약 1,000장, 손글씨 인사, 1실링, 장사로는 실패, 호슬리의 작은 자기 얼굴과 ‘Xmasse, 1843’, 에글리의 1848년 카드(1842로 잘못 읽힘), 1페니 우편과 1894년 반 페니 우편', 'u': VA},
  {'l': '컬처 트립, V&A 큐레이터 팀 트래비스 인터뷰 — 잡스 인쇄소(홀번 워릭 코트)의 석판 인쇄 1,000장, 색칠장이 윌리엄 메이슨, 1실링은 하루 품삯쯤, 남은 카드는 컨들이 ‘서머리의 홈 트레저리’에서 팖, 값이 비싸다는 평', 'u': CT},
  {'l': '옥스퍼드 보들리언 도서관 존 존슨 모음 블로그 — 콜은 로랜드 힐과 1페니 우편(1840)에서 일함, ‘잘 팔렸지만’, 1,000장 석판·손 색칠, 다음 상업용 카드는 1848년', 'u': BOD},
  {'l': '스미스소니언 국립 우편 박물관 「The World’s First Postage Stamps」 — 1840년 1월 10일 반 온스 편지 1페니, 우표는 1840년 5월 6일부터 쓸 수 있음', 'u': NPM},
  {'l': '브리태니커 「lithography」 — 기름과 물이 섞이지 않는 성질, 1798년 알로이스 제네펠더', 'u': BRIT},
  {'l': 'History of Information — 1843년 5월 1일 그렸다는 기록, 두 번 2,050장(첫 인쇄 1,000장), 컨들의 가게 이름과 ‘서머리’라는 다른 이름, 1977년 케네스 로가 찾은 21장, 2001년 경매', 'u': HOI},
  {'l': '메리 에번스 사진 자료(헨리 올드리지 앤드 선 경매 사진) — 콜 부부가 ‘할머니와 샤 이모’에게 보낸 카드, 두 사람의 서명, 2001년 11월 24일 디바이지스, 2만 2,500파운드', 'u': ME},
  {'l': '기네스 세계 기록 「First printed Christmas card」 — 처음 찍은 1,000장 가운데 12장이 남음, 2001년 경매 2만 파운드, ‘어머니에게 보낸 카드’라는 설명', 'u': GWR},
  {'l': '리처드 존스(런던 역사 해설) — 두 번 2,050장, 흑백 6펜스·색칠 1실링, 잡스 인쇄소와 색칠장이 메이슨(전해지는 이야기로 밝힘)', 'u': RJ},
  {'l': '위키백과(영어) 「Christmas card」 — 길잡이로만(두 번 2,050장, 2001년 경매 값 2만 2,250파운드, 12장이 남았다는 말)', 'u': WPC},
  {'l': '위키미디어 공용: 1843년 카드 사진(두 장)과 1840년 5월 6일 편지 사진 정보', 'u': 'https://commons.wikimedia.org/wiki/File:Stamp_GB-Penny_Black_first_day_cover.jpg'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 45%', 'p1': '52% 40%', 's0': 1.25, 's1': 1.05, 'kicker': '1843년 12월 · 런던', 'title': '세계 첫 성탄 카드',
   'lines': [{'t': '답장하지 못한 편지가 쌓인 12월.'}, {'t': '한 사람이 꾀를 냈어요. 그림 카드 한 장.'}],
   'kid': [{'t': '편지가 산더미처럼 쌓였어.'}, {'t': '그래서 그림 카드를 만들었대!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '답장이 밀린 12월'},
  {'type': 'img', 'ch': 1, 'img': 'post', 'fit': 'cover', 'p0': '70% 50%', 'p1': '50% 55%', 's0': 1.3, 's1': 1.0, 'cap': '1840년 5월 6일, 첫 우표를 붙인 편지',
   'lines': [{'t': '1840년부터 편지는 어디로든 1페니.'}, {'t': '그 우편을 이끈 로랜드 힐 곁에 콜이 있었어요.'}],
   'kid': [{'t': '우표 한 장이면 어디든 편지가 갔어.'}, {'t': '편지가 많아지면 어떤 일이 생길까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '12월 17일 저녁'},
  {'type': 'img', 'ch': 2, 'img': 'card', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 50%', 's0': 1.5, 's1': 1.1, 'cap': '호슬리의 그림, 1843년',
   'lines': [{'t': '저녁에 호슬리가 와서, 성탄 카드 그림을 가져왔다.', 'q': True, 'from': '헨리 콜의 일기, 1843년 12월 17일'}, {'t': '가운데는 잔을 든 가족, 양옆은 이웃을 돕는 손.'}],
   'kid': [{'t': '화가 친구가 저녁에 카드 그림을 가져왔대.'}, {'t': '가운데 가족들은 손에 무엇을 들고 있어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '한 장씩, 손으로'},
  {'type': 'mod', 'mod': 'steps', 'ch': 3,
   'lines': [{'t': '화가가 그린 그림을', 'act': 'step:1'},
             {'t': '돌판에 옮겨 찍어요. 기름 묻은 곳에만 잉크가.', 'act': 'step:2', 'wait': 1200},
             {'t': '색칠장이가 한 장씩 붓으로.', 'act': 'step:3', 'wait': 1500},
             {'t': '가게에서 한 장에 1실링.', 'act': 'step:4'},
             {'t': '받는 사람과 보내는 사람을 손으로 써요.', 'act': 'step:5', 'wait': 1500},
             {'t': '우표를 붙여, 할머니께.', 'act': 'step:6', 'wait': 2200}],
   'kid': [{'t': '그림을 그리고, 돌판으로 꾹!', 'act': 'step:2'},
           {'t': '붓으로 슥슥 색칠.', 'act': 'step:3', 'wait': 1200},
           {'t': '이름을 쓰고 우표를 붙여!', 'act': 'step:6', 'wait': 1600},
           {'t': '너라면 누구 이름을 쓸래?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '남은 카드들'},
  {'type': 'img', 'ch': 4, 'img': 'copy2', 'fit': 'cover', 'p0': '30% 10%', 'p1': '70% 90%', 's0': 1.5, 's1': 1.5, 'cap': '같은 카드의 또 다른 한 장',
   'lines': [{'t': '찍은 카드 가운데 몇 장만 오늘까지 남았어요.'}, {'t': '카드마다 다른 이름, 다른 손글씨.'}],
   'kid': [{'t': '화가는 콜 아저씨 카드에 자기 얼굴을 쪼그맣게 그렸대.'}, {'t': '네 얼굴을 그려 넣는다면 어디에 그릴래?', 'ask': True}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '창밖에 마차 바퀴가 덜컹거려요.'}, {'t': '막 마른 카드에서 물감 냄새가 나요.'}, {'t': '펜촉이 빈칸을 사각사각 채워요.'}],
   'kid': [{'t': '마차 소리가 덜컹덜컹.'}, {'t': '펜으로 사각사각.'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
