# -*- coding: utf-8 -*-
"""깊은 카드: 존 바턴 『성서의 역사』·『성서의 형성』(bb-barton) · 중심 방식 = 놓아 보기
기준서 1판(보탬 10) · 틀 deep3-4 · 키트 3판 · 2026-11-18 만들기 시작
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 700년 무렵 잉글랜드 웨어머스-재로 수도원, 여러 권으로 나누어 베끼던 성경이
     천 장이 넘는 한 권(판덱트)에 담겨 책상 위에 놓이는 순간.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 그 책(아미아티누스 사본)의 에스라 그림 속 책장에 놓인
     아홉 권 — 카시오도루스가 『인스티투티오네스』에 적은 ‘아홉 권 성경’의 차례대로 꽂고, 마지막에 한 권을 놓기.
카드 크기: 큰 카드(장면 4개) — 아타나시우스 이콘 · 에스라 그림 · 놓아 보기 무대 · 아미아티누스 사진 두 장.
무대 그림은 이 안내서가 그렸어요(에스라 그림을 베끼지 않고, 카시오도루스가 매긴 차례를 따라 그림).
그림 원본(src)은 deep_src/bb-barton/ (저장소 밖). 받는 법: commons_get.py"""
import random
S = 'bb-barton/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

BARTON = 'https://www.thebritishacademy.ac.uk/blog/how-new-testament-was-created/'
ATHAN = 'https://www.newadvent.org/fathers/2806039.htm'
CASS = 'https://faculty.georgetown.edu/jod/inst-trans.html'
JOD = 'https://faculty.georgetown.edu/jod/cassiodorus.html'
JODN = 'https://faculty.georgetown.edu/jod/texts/cassbook/chap6not.html'
WATSON = 'https://www.mdpi.com/2077-1444/13/6/530'
BEDE = 'https://sourcebooks.web.fordham.edu/basis/bede-jarrow.asp'
BLOG = 'https://blogs.bl.uk/digitisedmanuscripts/2018/06/the-first-voyage-of-codex-amiatinus.html'
CTIMES = 'https://www.churchtimes.co.uk/articles/2017/8-december/news/uk/oldest-latin-bible-to-return-to-britain'
HOI = 'https://historyofinformation.com/detail.php?id=188'
SUND = 'https://www.sunderland.gov.uk/article/12882/23-Codex-Amiatinus'
CATH = 'https://www.newadvent.org/cathen/04081a.htm'
MARSDEN = 'https://www.cambridge.org/core/journals/anglo-saxon-england/article/abs/manus-bedae-bedes-contribution-to-ceolfriths-bibles/D96284C67F8973118A0BAD92DAF6F14E'
SMART = 'https://smarthistory.org/codex-amiatinus/'

# 카시오도루스가 매긴 아홉 권의 차례(『인스티투티오네스』 1권: 첫째 부분 팔경 … 아홉째 부분 사도행전과 계시록)
ITEMS = [
 {'id': 'oct', 't': '팔경', 'la': 'Octateuchus', 'say': '첫째 권은 ‘팔경’이에요. 창세기부터 룻기까지 여덟 권의 책을 한데 묶었어요.'},
 {'id': 'reg', 't': '왕들의 책', 'la': 'Regum', 'say': '둘째 권은 ‘왕들의 책’. 사무엘기·열왕기와 역대기, 왕들의 이야기예요.'},
 {'id': 'psal', 't': '시편', 'la': 'Psalterium', 'say': '셋째 권은 시편. 카시오도루스가 가장 먼저 풀이를 쓴 책이에요.'},
 {'id': 'sal', 't': '솔로몬의 책', 'la': 'Salomon', 'say': '넷째 권은 ‘솔로몬의 책’. 잠언·전도서·아가와 지혜서·집회서가 들었어요.'},
 {'id': 'proph', 't': '예언서', 'la': 'Prophetae', 'say': '다섯째 권은 예언서. 이사야·예레미야·에스겔·다니엘과 열두 예언자의 글이에요.'},
 {'id': 'hag', 't': '거룩한 글들', 'la': 'Hagiographa', 'say': '여섯째 권은 ‘거룩한 글들’. 욥기·토빗기·에스더·유딧기, 에스라 두 권, 마카베오기 두 권이에요.'},
 {'id': 'evang', 't': '복음서', 'la': 'Evangelia', 'say': '일곱째 권부터 신약이에요. 마태·마가·누가·요한, 네 복음서예요.'},
 {'id': 'epist', 't': '사도들의 편지', 'la': 'Epistulae', 'say': '여덟째 권은 사도들의 편지. 바울의 편지들과 베드로·야고보·요한 등의 편지가 들었어요.'},
 {'id': 'act', 't': '사도행전·계시록', 'la': 'Actus · Apocalypsis', 'say': '아홉째 권은 사도행전과 요한계시록. 이렇게 성경 전체가 아홉 권이 되었어요.'},
 {'id': 'pandect', 't': '한 권 성경', 'la': 'pandectes', 'say': '그리고 이 모두를 한 권에 담은 큰 책. 웨어머스-재로 수도원에서 만든 ‘판덱트’예요.'},
]
SPINE = {'oct': '팔경', 'reg': '왕들', 'psal': '시편', 'sal': '솔로몬', 'proph': '예언서', 'hag': '거룩한 글', 'evang': '복음서', 'epist': '편지', 'act': '행전·계시'}


def shelf_svg():
    """수도원 책장 무대(800×450). 놓을 책마다 data-o 무리, 마지막 큰 책은 오른쪽 책상 위. 이 안내서가 그림."""
    R = random.Random(716)
    F = "font-family:var(--serif,serif)"
    rows = [170, 220, 270, 320, 370]          # 칸 바닥(선반 윗면)의 y. 위 네 칸은 두 권, 맨 아래 칸은 한 권(아홉 권)
    slots = [(309, rows[0]), (403, rows[0]), (309, rows[1]), (403, rows[1]), (309, rows[2]), (403, rows[2]),
             (309, rows[3]), (403, rows[3]), (309, rows[4])]
    books = ''
    for (x0, yb), it in zip(slots, ITEMS[:9]):
        k = R.uniform(-.6, .6)
        lines = ''.join(f'<line x1="{x0 + 3}" y1="{yb - 11 + i * 2.6:.1f}" x2="{x0 + 83}" y2="{yb - 11 + i * 2.6:.1f}"/>' for i in range(1, 4))
        books += (f'<g class="obj" data-o="{it["id"]}"><g transform="rotate({k:.2f} {x0 + 43} {yb - 20})">'
                  f'<rect x="{x0}" y="{yb - 12}" width="86" height="12" rx="1.5" fill="#e8dcc0" stroke="#7a5a3a" stroke-width="1"/>'
                  f'<g stroke="#b9a684" stroke-width=".8">{lines}</g>'
                  f'<path d="M{x0} {yb - 12} L{x0 + 86} {yb - 12} L{x0 + 80} {yb - 36} L{x0 + 6} {yb - 36}Z" fill="#9b2d22" stroke="#4e150e" stroke-width="1.4" stroke-linejoin="round"/>'
                  f'<path d="M{x0 + 10} {yb - 15} L{x0 + 76} {yb - 15} L{x0 + 72} {yb - 33} L{x0 + 14} {yb - 33}Z" fill="none" stroke="#d07a5c" stroke-width=".9" opacity=".75"/>'
                  f'<text x="{x0 + 43}" y="{yb - 19.5}" text-anchor="middle" font-size="13.5" font-weight="700" fill="#f7e6c2" style="{F}">{SPINE[it["id"]]}</text>'
                  f'</g></g>')
    shelves = ''.join(f'<rect x="304" y="{y}" width="192" height="5" fill="#7b6a2c"/><rect x="304" y="{y + 5}" width="192" height="2" fill="#2a1a0c" opacity=".6"/>' for y in rows)
    joints = ''                                # 돌벽 줄눈(희미하게)
    for j, y in enumerate([150, 214, 278, 342]):
        joints += f'<line x1="0" y1="{y}" x2="800" y2="{y}"/>'
        off = 0 if j % 2 else 60
        joints += ''.join(f'<line x1="{x}" y1="{y - 64}" x2="{x}" y2="{y}"/>' for x in range(off + 40, 800, 120))
    frieze = ''.join(f'<path d="M{x} 111 l5 -4 l5 4 l-5 4z" fill="#e7cfa5" opacity=".55"/>' for x in range(296, 506, 18))
    door_l = '<path d="M292 118 L248 132 L248 386 L292 377Z" fill="#84301f" stroke="#3c120b" stroke-width="2" stroke-linejoin="round"/>' + \
             ''.join(f'<path d="M286 {y} L256 {y + 9} L256 {y + 55} L286 {y + 47}Z" fill="none" stroke="#3c120b" stroke-width="1.6"/>' for y in (134, 196, 258, 318))
    door_r = '<path d="M508 118 L552 132 L552 386 L508 377Z" fill="#84301f" stroke="#3c120b" stroke-width="2" stroke-linejoin="round"/>' + \
             ''.join(f'<path d="M514 {y} L544 {y + 9} L544 {y + 55} L514 {y + 47}Z" fill="none" stroke="#3c120b" stroke-width="1.6"/>' for y in (134, 196, 258, 318))
    pages = ''.join(f'<line x1="576" y1="{y}" x2="672" y2="{y}"/>' for y in range(306, 334, 3))
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="돌벽 방 한가운데 문이 열린 붉은 책장. 놓은 책이 칸마다 하나씩 나타나고, 마지막에 오른쪽 책상 위에 아주 두꺼운 책 한 권이 놓인다."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#241911"/><stop offset="1" stop-color="#140d08"/></linearGradient>
<linearGradient id="__U__win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1428"/><stop offset="1" stop-color="#1b2540"/></linearGradient>
<linearGradient id="__U__sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f7e7bf"/><stop offset=".6" stop-color="#eec58a"/><stop offset="1" stop-color="#d99a5e"/></linearGradient>
<radialGradient id="__U__warm" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd89a" stop-opacity=".9"/><stop offset=".5" stop-color="#e7a35a" stop-opacity=".35"/><stop offset="1" stop-color="#b8692c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".55" r=".8"><stop offset="0" stop-color="#fff2d2" stop-opacity=".6"/><stop offset=".55" stop-color="#ffd08c" stop-opacity=".28"/><stop offset="1" stop-color="#e59a4e" stop-opacity="0"/></radialGradient></defs>
<rect width="800" height="450" fill="url(#__U__wall)"/>
<g stroke="#3a2a1d" stroke-width="1.2" opacity=".55">{joints}</g>
<g><path d="M136 262 V150 A29 29 0 0 1 194 150 V262Z" fill="#2c2017" stroke="#3b2b1f" stroke-width="10" stroke-linejoin="round"/>
<path d="M140 258 V150 A25 25 0 0 1 190 150 V258Z" fill="url(#__U__win)"/>
<path class="sky2" d="M140 258 V150 A25 25 0 0 1 190 150 V258Z" fill="url(#__U__sky2)"/>
<path d="M165 125 V258 M140 196 H190" stroke="#2c2017" stroke-width="3"/></g>
<path d="M0 396 L800 396 L800 450 L0 450Z" fill="#100a06"/><line x1="0" y1="396" x2="800" y2="396" stroke="#3a2a1d" stroke-width="2"/>
<ellipse class="glow" cx="420" cy="250" rx="230" ry="190" fill="url(#__U__warm)" opacity=".14"/>
{door_l}{door_r}
<path d="M282 104 L400 58 L518 104Z" fill="#7d2a1c" stroke="#3c120b" stroke-width="2" stroke-linejoin="round"/>
<rect x="389" y="80" width="22" height="13" fill="#2a0f08" stroke="#3c120b" stroke-width="1.2"/>
<rect x="284" y="103" width="232" height="15" fill="#7d2a1c" stroke="#3c120b" stroke-width="2"/>{frieze}
<rect x="292" y="117" width="216" height="262" fill="#6e2418" stroke="#3c120b" stroke-width="2"/>
<rect x="304" y="124" width="192" height="248" fill="#1d0e08"/>
{shelves}
<g fill="#ece2cc" stroke="#8d7a5a" stroke-width="1"><path d="M418 368 c6 -22 18 -30 24 -26 c-8 6 -14 16 -16 26z"/><path d="M440 368 c6 -22 18 -30 24 -26 c-8 6 -14 16 -16 26z"/></g>
<rect x="292" y="378" width="216" height="20" fill="#5c1e14" stroke="#3c120b" stroke-width="2"/>
<g fill="none" stroke="#e3cfa9" stroke-width="1.6" opacity=".8"><rect x="306" y="382" width="34" height="12"/><rect x="460" y="382" width="34" height="12"/><path d="M400 380 V396 M393 386 H407"/></g>
<rect x="298" y="398" width="14" height="8" fill="#3c120b"/><rect x="488" y="398" width="14" height="8" fill="#3c120b"/>
{books}
<g><rect x="560" y="336" width="122" height="10" rx="2" fill="#6a4524" stroke="#2f1d0e" stroke-width="1.5"/>
<rect x="568" y="346" width="8" height="50" fill="#5a3a1e"/><rect x="666" y="346" width="8" height="50" fill="#5a3a1e"/><rect x="568" y="372" width="106" height="5" fill="#4a2f18"/></g>
<g class="obj" data-o="pandect"><rect x="572" y="303" width="104" height="33" rx="2" fill="#eadcbc" stroke="#6e5434" stroke-width="1.4"/>
<g stroke="#bda98a" stroke-width=".8">{pages}</g>
<path d="M572 303 L676 303 L668 278 L580 278Z" fill="#5a2116" stroke="#2c0f09" stroke-width="1.6" stroke-linejoin="round"/>
<path d="M584 300 L664 300 L658 281 L590 281Z" fill="none" stroke="#c99a4a" stroke-width="1.2"/>
<text x="624" y="296" text-anchor="middle" font-size="13" font-weight="700" fill="#e9c77d" style="{F}">한 권</text></g>
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''


CARD = {
 'id': 'bb-barton', 'mode': '놓아 보기',
 'pagetitle': '아홉 권, 그리고 한 권',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>367년 ~ 716년</b><span>알렉산드리아 · 이탈리아 남쪽 · 잉글랜드 웨어머스-재로</span>',
 'lead': '1,300여 년 전, 잉글랜드 북쪽의 웨어머스-재로 수도원. 수도사들은 여러 권으로 나누어 베끼던 성경을 통째로 한 권에 담은 큰 책을 만들었어요. 그 책에 그려진 책장에 아홉 권을 차례대로 꽂고, 마지막에 그 한 권을 놓아 보세요.',
 'leadKid': '옛날 성경은 여러 권으로 나뉜 책이었대. 그런데 잉글랜드의 한 수도원에서 성경을 통째로 한 권에 담은 아주 큰 책을 만들었어. 책장에 한 권씩 꽂아 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 6분',
 'draft': '검수 전 시안이에요(기준서 1판). 장면에는 기록에 있는 것만 옮겼고, 자료마다 다른 것은 ‘기록마다 다른 점’에 적었어요. 놓아 보기의 책장 무대는 이 안내서가 그렸어요(옛 그림을 베끼지 않고, 카시오도루스가 적은 아홉 권의 차례를 따라 그렸어요). 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 얼굴 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 # 화면 색: 아미아티누스 사본의 보랏빛 쪽에서 가져온 자줏빛(밝게·어둡게 두 벌)
 'theme': """:root{--accent:#6b3a6e;--accent-ink:#fff8fb;--soft:rgba(107,58,110,.09);--stamp:#8c2f3c}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#c9a0cf;--accent-ink:#1a0f1c;--soft:rgba(201,160,207,.10);--stamp:#e2727f}}
:root[data-theme="dark"]{--accent:#c9a0cf;--accent-ink:#1a0f1c;--soft:rgba(201,160,207,.10);--stamp:#e2727f}""",
 'stamp': {'t': '한 권', 'y': '716', 'sub': '웨어머스-재로 · 잉글랜드'},
 'doneNote': '집에 있는 성경의 차례를 펼쳐 보세요. 여러 권의 책이 한 권에 모여 있어요.',
 'images': {
  'ezra': {'src': S + 'CodxAmiatinusFolio5rEzra.jpg', 'cap': '아미아티누스 사본의 에스라 그림(5쪽 앞면), 700년 무렵 · 피렌체 라우렌치아나 도서관',
           'cr': '웨어머스-재로 수도원 · 퍼블릭 도메인 · 위키미디어 공용(스캔한 곳은 적혀 있지 않아요)',
           'u': 'https://commons.wikimedia.org/wiki/File:CodxAmiatinusFolio5rEzra.jpg',
           'alt': '위쪽에 라틴어 글귀 두 줄. 붉은 테두리 안에서 후광을 두른 노인이 의자에 앉아 무릎 위 책에 글을 쓴다. 뒤에는 문이 열린 붉은 책장이 있고, 다섯 칸에 붉은 표지의 책 아홉 권이 누워 있다. 오른쪽에 작은 탁자, 바닥에 필기도구가 있다.'},
  'athan': {'src': S + 'Saint-Athanasius-of-Alexandria-icon-Sozopol-Bulgaria-17century.jpg',
            'cap': '아타나시우스를 그린 이콘 — 그때의 모습이 아니라 17세기 말 불가리아 소조폴에서 그린 것이에요(지금 소피아 국립미술관)',
            'cr': '작가 모름 · 퍼블릭 도메인 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Saint-Athanasius-of-Alexandria-icon-Sozopol-Bulgaria-17century.jpg',
            'alt': '군데군데 벗겨진 금빛 바탕 앞에서, 흰 수염이 가슴까지 내려온 노인이 십자 무늬 옷을 입고 오른손을 들어 축복하며 왼팔에 붉은 표지의 책을 안고 있다. 왼쪽 위에 그리스 글자가 적혀 있다.'},
  'amia3': {'src': S + 'Codex_Amiatinus_03.jpg', 'cap': '아미아티누스 사본의 책등과 두께, 2014년',
            'cr': '사진: Remi Mathis · CC BY-SA 4.0 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Codex_Amiatinus_03.jpg',
            'alt': '밝은 갈색 가죽으로 싼 아주 두꺼운 책이 탁자 위에 옆으로 누워 있고, 한 사람의 손이 책 위에 얹혀 있다. 책등에 가로 띠 여러 줄이 도드라져 있다.'},
  'amia1': {'src': S + 'Codex_Amiatinus_01.jpg', 'cap': '아미아티누스 사본의 보랏빛 쪽을 넘기는 모습, 2014년',
            'cr': '사진: Remi Mathis · CC BY-SA 4.0 · 위키미디어 공용',
            'u': 'https://commons.wikimedia.org/wiki/File:Codex_Amiatinus_01.jpg',
            'alt': '흰 장갑을 낀 두 손이 아주 두꺼운 책을 펼치고 한 장을 들어 넘긴다. 아래 쪽은 보랏빛 바탕에 아치 모양 테두리가 있고, 그 안에 두 단으로 글씨가 적혀 있다.'},
 },
 'extra_credits': [{'cr': '이 안내서가 그린 책장 무대 · 카시오도루스가 적은 아홉 권의 차례와 아미아티누스 사본의 에스라 그림을 바탕으로', 'u': CASS}],
 'scenes': [
  {'id': 'list', 'label': '367년, 책 이름을 적은 편지', 'kind': 'photo', 'img': 'athan',
   'text': ['처음 그리스도인들에게는 아직 신약성경이 없었어요. 예수의 이야기는 처음에 입에서 입으로 전해졌고, 편지와 복음서들은 저마다 따로 쓰였어요.',
            '367년, 이집트 알렉산드리아의 주교 아타나시우스가 부활절 편지를 썼어요. 그 편지에는 오늘 신약성경에 든 스물일곱 권의 이름이 하나하나 적혀 있었어요.'],
   'quote': {'t': '누구도 여기에 더하지 말고, 여기서 아무것도 빼지 마세요.', 'from': '아타나시우스, 39번째 부활절 편지(367) · 영어 번역(NPNF)을 이 안내서가 우리말로 옮김', 'u': ATHAN},
   'text2': ['존 바턴은 이 편지가 새 목록을 정한 것이 아니라, 교회들이 이미 함께 읽던 책들을 적어 둔 것이라고 봐요. 요한이서·요한삼서처럼 몇 권만 조금 망설였을 뿐이래요.'],
   'kid': '아주 옛날 주교님이 편지에 성경 책 이름을 하나하나 적었대.',
   'kidq': '책 이름을 적어서 나눠 주면 무엇이 좋을까?'},
  {'id': 'nine', 'label': '아홉 권으로 된 성경', 'kind': 'photo', 'img': 'ezra',
   'text': ['6세기 중반, 이탈리아 남쪽 이오니아 바닷가의 비바리움 수도원. 카시오도루스는 수도사들이 읽을 책을 모으면서 성경을 아홉 권으로 나누어 두었어요.',
            '150년쯤 뒤 잉글랜드에서 그린 이 그림 속 책장에도 붉은 책 아홉 권이 들어 있어요. 학자들은 카시오도루스의 아홉 권 성경을 본뜬 것으로 봐요.'],
   'quote': {'t': '거룩한 책들이 적의 손에 불타 버렸을 때, 하나님을 향한 열심으로 에스라가 이 일을 다시 이루었다.', 'from': '그림 위에 적힌 라틴어 글귀 · 이 안내서가 우리말로 옮김', 'u': WATSON},
   'text2': ['그림 속 사람은 에스라예요. 성경은 그를 모세의 율법에 익숙한 학자이자 제사장으로 소개해요(' + bl('EZR.7', '에스라 7장') + '). 옛 전승은 불타 버린 성경을 에스라가 다시 써서 되살렸다고 전해요.'],
   'kid': '그림 속 할아버지 뒤 책장에 빨간 책이 가득해. 몇 권인지 세어 볼까?',
   'kidq': '하나, 둘, 셋… 모두 몇 권이야?'},
  {'id': 'shelf', 'label': '아홉 권, 그리고 한 권', 'kind': 'mod', 'mod': 'place', 'night': False,
   'text': ['카시오도루스는 아홉 권에 차례를 매겼어요. 첫째 권은 창세기부터 룻기까지 여덟 권을 묶은 ‘팔경’이고, 일곱째 권부터는 신약이에요.',
            '아래 책장에 아홉 권을 하나씩 꽂아 보세요. 마지막에는 700년 무렵 잉글랜드 웨어머스-재로 수도원에서 만든 책이 기다려요.'],
   'text2': ['이 수도원의 수도원장 체올프리드는 성경 전체를 한 권에 담은 책을 세 권 만들게 했어요. 그 무렵 성경은 시편 한 권, 네 복음서 한 권처럼 몇 권씩 나누어 베끼는 것이 보통이었어요.',
             '그 수도원의 수도사 비드는 이렇게 적었어요. 체올프리드는 두 권을 두 수도원에 남기고, 한 권은 늙은 몸으로 로마로 떠나면서 선물로 가져갔다고요.'],
   'kid': '책을 칸마다 하나씩 꽂아 보자. 마지막엔 아주아주 큰 책이 나와!',
   'kidq': '아홉 권을 한 권으로 묶으면 얼마나 무거울까?'},
  {'id': 'road', 'label': '716년, 로마로 가는 큰 책', 'kind': 'duo', 'imgs': ['amia3', 'amia1'],
   'text': ['716년 6월 4일, 일흔이 넘은 체올프리드가 웨어머스를 떠났어요. 짐 속에는 교황께 드릴 큰 성경이 있었어요. 높이 50cm쯤, 천 장이 넘는 양피지에 무게가 30kg이 넘는 책이에요.',
            '체올프리드는 배로 바다를 건넌 뒤, 말을 타기도 하고 들것에 실리기도 하며 나아갔어요. 그리고 그해 9월, 프랑스 랑그르에서 세상을 떠났어요.'],
   'text2': ['함께 가던 수도사들이 길을 이어 가 선물을 교황께 전했다고 해요. 그 뒤 이 책은 이탈리아 아미아타산의 수도원에서 900년 넘게 머물렀고, 그래서 ‘아미아티누스 사본’이라 불려요. 지금은 피렌체의 라우렌치아나 도서관에 있어요.',
             '잉글랜드에 남은 두 권 가운데 한 권은 사라졌고, 다른 한 권은 몇 장만 남아 대영도서관에 있어요. 2018년, 이 큰 책은 1,300여 년 만에 잉글랜드로 돌아와 런던에서 전시되었어요.'],
   'kid': '수도원장 할아버지가 아주 큰 성경을 들고 로마로 먼 길을 떠났어.',
   'kidq': '이렇게 무거운 책을 들고 먼 길을 간다면, 어떻게 옮기면 좋을까?'},
 ],
 'imagine': {'t': '돌로 지은 수도원의 서늘한 방. 양피지를 넘길 때마다 바스락 소리가 나고, 가죽과 잉크 냄새가 나요. 두 팔로 안아도 버거운 책 한 권에 아홉 칸 책장이 통째로 들어 있어요. 이 책을 실은 배가 바다 위에서 출렁여요.',
             'kid': '눈을 감아 봐. 커다란 책장을 넘기면 바스락! 두 팔로 안아도 무거운 책이야. 이 책을 싣고 배가 출렁출렁 먼 바다로 가.'},
 'lines': ['책들이 모여 한 권이 되기까지.', '아홉 칸 책장이 한 권의 책으로.', '누구도 더하지 말고, 빼지 말라.', '먼 길을 떠난 한 권의 성경.'],
 'linesKid': ['아홉 권이 한 권으로!', '아주 크고 무거운 성경.', '책 이름을 하나하나 적었어.'],
 'goals': {
  's4': {'t': '카시오도루스의 차례대로', 'p': '카시오도루스가 적은 차례(팔경부터 사도행전·계시록까지)대로 아홉 권을 꽂고, 마지막에 한 권 성경까지 놓으면 카드에 금박이 입혀져요.',
         'how': '카시오도루스가 적은 차례대로 아홉 권을 꽂고 한 권 성경을 놓아 보세요', 'done': '아홉 권과 한 권을 차례대로 놓았어요',
         'ways': [{'id': 'plOrder', 't': '팔경 → … → 사도행전·계시록 → 한 권 성경 차례로 놓기'}]},
  's5': {'t': '큰 성경을 둘 자리', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '체올프리드의 자리에서 큰 성경을 둘 곳을 고르거나, 아이와 함께 끝까지 보세요', 'done': '큰 성경을 둘 자리를 골랐어요',
         'ways': [{'id': 'home', 't': '체올프리드라면 큰 성경을 어디에 둘지 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'place': {
   'items': ITEMS,
   'order': '팔경, 왕들의 책, 시편, 솔로몬의 책, 예언서, 거룩한 글들, 복음서, 사도들의 편지, 사도행전·계시록, 그리고 한 권 성경',
   'intro': '아래에서 책을 하나씩 골라 책장에 꽂아 보세요. 테두리가 빛나는 책이 카시오도루스가 적은 다음 차례예요.',
   'climax': '아홉 권이 다 꽂혔어요. 그리고 책상 위에는 성경 전체를 한 권에 담은 책이 놓였어요. 천 장이 넘는 양피지, 30kg이 넘는 무게. 700년 무렵 웨어머스-재로 수도원에서 만든 책이에요.<span class="la">pandectes · 성경 전체를 한 권에 담은 책</span>',
   'wrongOrder': '이 카드의 차례는 카시오도루스가 적은 대로예요: {order}',
   'orderDone': '카시오도루스의 차례대로 다 놓았어요',
   'home': ['수도원 교회', '도서관 책장', '로마의 교황께', '필사실 책상'],
   'homeLabel': '체올프리드라면 둘 곳',
   'homeWait': '책장과 책상을 다 채운 뒤 고를 수 있어요',
   'daylight': False,
   'svg': shelf_svg()}},
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="꽂을 책 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 꽂아 보기</button></div>
  <div class="pl-home" hidden><p>체올프리드라면, 이 큰 성경을 어디에 둘까요?</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>카시오도루스</b> 490년 무렵 태어나 585년 무렵 세상을 떠났어요. 나라의 높은 관리로 일하다가 수도사가 되어, 이탈리아 남쪽 이오니아 바닷가에 비바리움 수도원을 세웠어요.',
    '<b>『인스티투티오네스』</b> 라틴어로 ‘가르침’이라는 뜻이에요. 카시오도루스가 수도사들에게 무엇을 어떻게 읽을지 안내한 책으로, 첫째 책에서 성경 아홉 권과 그 풀이책들을 차례로 소개해요.',
    '<b>판덱트</b> 구약과 신약, 성경 전체를 한 권에 담은 책을 이렇게 불러요. 아미아티누스 사본은 지금 남아 있는 가장 오래된 한 권짜리 라틴어 성경이에요.',
    '<b>체올프리드</b> 642년 무렵 태어나 716년에 세상을 떠났어요. 잉글랜드 북쪽 웨어머스와 재로, 두 곳에 걸친 한 수도원의 수도원장이었어요.',
    '<b>비드</b> 일곱 살에 이 수도원에 들어와 평생 성경 공부에 몸을 바친 수도사예요. 『잉글랜드 교회사』를 쓴 학자로 이름났어요.']},
  {'h': '세 권의 그 뒤', 'p': [
    '<b>지워진 이름</b> 아미아티누스 사본 첫머리에는 이 책을 바치는 짧은 시가 있어요. 그런데 바친 사람과 받는 곳의 이름이 긁혀 지워지고, 다른 손으로 ‘랑고바르드족의 베드로’가 아미아타산의 구세주 수도원에 바친다고 고쳐 적혀 있었어요.',
    '그래서 이 책은 오랫동안 이탈리아에서 만든 책으로 여겨졌어요. 뒷날 학자들이 지워진 자리를 살피고 체올프리드의 옛 전기와 맞춰 본 끝에, 원래는 ‘잉글랜드 땅끝에서 온 수도원장 체올프리드’가 로마의 성 베드로에게 바친 책이었음이 밝혀졌어요.',
    '<b>땅문서를 싼 낱장</b> 잉글랜드에 남았던 큰 성경은 열 장 남짓만 남았어요. 그 가운데 몇 장은 뒷날 한 집안의 땅문서를 싸는 표지로 쓰였대요. 남은 낱장들은 지금 대영도서관에 있어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>세상을 떠난 날</b> 비드의 기록(자일스의 영어 번역)은 9월 25일에 세상을 떠났다고 적었어요(이 번역은 해를 715년으로 적었어요). 대영도서관 블로그는 25일 아침 랑그르에 닿아 29일에 세상을 떠났다고 적었어요. 이 카드는 ‘716년 9월’까지만 적었어요.',
    '<b>무게와 장 수</b> 무게는 75파운드(약 34kg)라는 자료와 35kg이라는 자료가 있어요. 양피지도 1,030장, 1,029장으로 달리 적혀요.',
    '<b>그림 속 사람</b> 그림 위 글귀는 에스라라고 밝혀요. 오도널은 많은 학자가 이 그림을 카시오도루스를 에스라처럼 그린 것으로 본다고 소개했고, 왓슨(2022)은 그림 속 사람을 글귀대로 에스라로 읽어요.',
    '<b>책등의 글씨</b> 그림 속 책등의 금 글씨는 많이 바랬어요. 왓슨은 맨 윗칸의 OCT(팔경)와 넷째 칸의 복음서·편지 글씨를 읽었고, 오도널은 아홉 권의 이름을 모두 읽어 카시오도루스의 배치와 꼭 맞는다고 했어요. 이 카드의 책장 무대는 카시오도루스가 매긴 차례를 따랐어요.']},
  {'h': '바턴의 책과 함께', 'p': [
    '바턴은 신약성경이 어느 날 한자리에서 정해진 것이 아니라고 말해요. 2세기에 이미 여러 교회가 이 책들을 성경으로 읽었고, 4세기의 목록과 회의는 그것을 적어 둔 것에 가깝다고 봐요. 몰래 짜 맞춘 일은 없었다고요.',
    '그는 또 처음 그리스도인들이 자기들의 글을 두루마리가 아니라 책 모양(코덱스, 낱장을 묶은 책)에 적었다는 점에 주목해요. 아홉 칸 책장과 한 권 성경은 그 ‘책’의 긴 이야기 속 한 장면이에요.',
    '『성서의 역사』는 성경이 쓰이고, 모이고, 읽혀 온 긴 역사를 한 권에 담았어요. 얇은 『성서의 형성』은 책들이 경전으로 받아들여진 과정만 따로 짧게 다뤄요.'],
   'links': [{'t': '대영도서관 블로그: 아미아티누스 사본의 첫 여행(716년의 길)', 'u': BLOG, 'm': '영어'},
             {'t': '스마트히스토리 영상: 대영도서관 전시실에서 본 아미아티누스 사본(약 6분)', 'u': SMART, 'm': '영어 영상'},
             {'t': '왓슨(2022): 에스라 그림 읽기 — 책장 속 아홉 권과 글귀', 'u': WATSON, 'm': '영어 · 무료 논문'}]},
 ],
 'src': [
  {'l': '존 바턴, 「신약성경은 어떻게 만들어졌나」(영국학술원 블로그, 2020.2.3) — 처음 그리스도인들, 2세기, 코덱스, 아타나시우스의 편지(367)와 ‘몇 권의 망설임’', 'u': BARTON},
  {'l': '아타나시우스, 39번째 부활절 편지(367) — 신약 27권 목록, ‘더하지도 빼지도 말라’(NPNF 영어 번역, New Advent)', 'u': ATHAN},
  {'l': '카시오도루스, 『인스티투티오네스』 1권(할펀 영어 번역) — 아홉 부분의 차례와 각 부분에 든 책, ‘아홉 권’', 'u': CASS},
  {'l': '제임스 오도널, 카시오도루스 안내 — 생몰년, 이오니아 바닷가 비바리움, 에스라 그림 해석', 'u': JOD},
  {'l': '제임스 오도널, 『카시오도루스』(1979) 6장 주 — 그림 속 책등 글씨와 카시오도루스의 배치', 'u': JODN},
  {'l': '프랜시스 왓슨, 「성경의 자화상: 아미아티누스 사본의 에스라 그림」(Religions 13, 2022) — 글귀 번역, 아홉 권, 책등 글씨, 에스라 전승', 'u': WATSON},
  {'l': '비드, 『웨어머스·재로 수도원장들의 생애』(자일스 영어 번역, 포덤 대학 자료집) — 세 권의 판덱트, 두 권은 두 수도원에, 한 권은 로마로, 74세', 'u': BEDE},
  {'l': '대영도서관 중세 사본 블로그, 「아미아티누스 사본의 첫 여행」(2018.6.4) — 6월 4일 출발, 배·말·들것, 랑그르, 선물 전달', 'u': BLOG},
  {'l': 'Church Times(2017.12.8) — 35kg, 1,030장, 세 권 가운데 하나는 사라지고 하나는 조각만, 2018년 대영도서관 전시', 'u': CTIMES},
  {'l': 'History of Information: 아미아티누스 사본 — 505×340mm, 1,030장, 75파운드, 에스라 그림 속 아홉 권', 'u': HOI},
  {'l': '선덜랜드 시립도서관 지역 연구 자료 23 — 그 무렵 성경을 몇 권씩 나누어 베끼던 방식, 남아 있는 가장 오래된 한 권 라틴어 성경', 'u': SUND},
  {'l': '가톨릭 백과사전(1908), 「아미아티누스 사본」 — 지워진 헌정 이름과 원래 글귀(성 베드로에게), 아미아타산 수도원, 1,029장', 'u': CATH},
  {'l': '대영도서관 중세 사본 블로그, 「체올프리드 성경」(2013) — 다른 한 권의 낱장 열 장 남짓, 땅문서 표지, 대영도서관 소장', 'u': 'https://britishlibrary.typepad.co.uk/digitisedmanuscripts/2013/05/the-ceolfrith-bible.html'},
  {'l': '리처드 마스든, 「비드의 손」(Anglo-Saxon England 27, 1998) 초록 — 일곱 살에 들어온 비드, 900년 넘게 아미아타산에', 'u': MARSDEN},
  {'l': '스마트히스토리: 클레어 브레이·베스 해리스, 「아미아티누스 사본」(2019) — 50.5×34.0cm, 세 권, 75파운드', 'u': SMART},
  {'l': '알라딘: 성서의 역사(비아토르, 2023, 박규태 옮김, 988쪽)', 'u': 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329541108'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'ezra', 'fit': 'cover', 'p0': '60% 32%', 'p1': '45% 50%', 's0': 1.3, 's1': 1.05, 'kicker': '367년 ~ 716년 · 책들이 한 권이 되기까지', 'title': '아홉 권, 그리고 한 권',
   'lines': [{'t': '성경은 처음부터 한 권이었을까요?'}, {'t': '이 그림 속 책장에는 붉은 책 아홉 권이 꽂혀 있어요.'}],
   'kid': [{'t': '성경은 처음부터 한 권이었을까?'}, {'t': '그림 속 책장을 봐. 빨간 책이 잔뜩 있어!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '책 이름을 적은 편지'},
  {'type': 'img', 'ch': 1, 'img': 'athan', 'fit': 'cover', 'p0': '50% 28%', 'p1': '50% 45%', 's0': 1.25, 's1': 1.05, 'cap': '아타나시우스 이콘, 17세기 말',
   'lines': [{'t': '처음 그리스도인들에게는 아직 신약성경이 없었어요.'},
             {'t': '367년, 알렉산드리아의 주교 아타나시우스가 부활절 편지에 스물일곱 권의 이름을 적었어요.'},
             {'t': '누구도 여기에 더하지 말고, 여기서 아무것도 빼지 마세요.', 'q': True, 'from': '아타나시우스의 부활절 편지(367)에서'}],
   'kid': [{'t': '주교님이 편지에 성경 책 이름을 하나하나 적었대.'}, {'t': '책 이름을 적어 두면 뭐가 좋을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '아홉 권의 책장'},
  {'type': 'img', 'ch': 2, 'img': 'ezra', 'fit': 'cover', 'p0': '62% 36%', 'p1': '42% 52%', 's0': 1.7, 's1': 1.15, 'cap': '아미아티누스 사본의 에스라 그림, 700년 무렵',
   'lines': [{'t': '6세기 중반, 이탈리아 남쪽의 수도원에서 카시오도루스는 성경을 아홉 권으로 나누어 두었어요.'},
             {'t': '150년쯤 뒤 잉글랜드에서 그린 이 그림 속 책장에도 아홉 권이 들어 있어요.'},
             {'t': '거룩한 책들이 불타 버렸을 때, 에스라가 이 일을 다시 이루었다.', 'q': True, 'from': '그림 위 라틴어 글귀에서'}],
   'kid': [{'t': '그림 속 책장에 빨간 책이 몇 권 있는지 세어 볼까?'}, {'t': '하나, 둘, 셋… 모두 몇 권이야?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '아홉 권, 그리고 한 권'},
  {'type': 'mod', 'mod': 'place', 'ch': 3,
   'lines': [{'t': '카시오도루스가 매긴 차례대로 꽂아 볼게요.'},
             {'t': '첫째 권, 팔경.', 'act': 'oct'}, {'t': '왕들의 책,', 'act': 'reg'}, {'t': '시편,', 'act': 'psal'}, {'t': '솔로몬의 책,', 'act': 'sal'},
             {'t': '예언서,', 'act': 'proph'}, {'t': '거룩한 글들.', 'act': 'hag'},
             {'t': '일곱째 권부터 신약이에요. 복음서,', 'act': 'evang'}, {'t': '사도들의 편지,', 'act': 'epist'}, {'t': '사도행전과 요한계시록.', 'act': 'act'},
             {'t': '그리고 이 모두를 한 권에 담은 큰 책.', 'act': 'pandect', 'wait': 1500},
             {'t': '700년 무렵 웨어머스-재로 수도원에서 만든, 천 장이 넘는 책이에요.', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '책장에 책을 하나씩 꽂아 보자.'},
           {'t': '하나!', 'act': 'oct'}, {'t': '둘!', 'act': 'reg'}, {'t': '셋!', 'act': 'psal'}, {'t': '넷!', 'act': 'sal'}, {'t': '다섯!', 'act': 'proph'},
           {'t': '여섯!', 'act': 'hag'}, {'t': '일곱!', 'act': 'evang'}, {'t': '여덟!', 'act': 'epist'}, {'t': '아홉!', 'act': 'act'},
           {'t': '그리고 아주 큰 책 한 권!', 'act': 'pandect', 'wait': 1500},
           {'t': '아홉 권이 한 권에 다 들어갔대. 얼마나 무거울까?', 'act': 'day', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '로마로 가는 길'},
  {'type': 'img', 'ch': 4, 'img': 'amia3', 'fit': 'cover', 'p0': '40% 60%', 'p1': '55% 55%', 's0': 1.2, 's1': 1.05, 'cap': '아미아티누스 사본의 책등, 2014년',
   'lines': [{'t': '716년 6월, 일흔이 넘은 수도원장 체올프리드가 이 큰 성경을 싣고 로마로 떠났어요.'},
             {'t': '배로 바다를 건너고, 말을 타고, 들것에 실려 가다가 9월에 프랑스 랑그르에서 세상을 떠났어요.'}],
   'kid': [{'t': '수도원장 할아버지가 아주 큰 성경을 들고 먼 길을 떠났어.'}, {'t': '이렇게 무거운 책을 어떻게 옮겼을까?', 'ask': True}]},
  {'type': 'img', 'ch': 4, 'img': 'amia1', 'fit': 'cover', 'p0': '45% 60%', 'p1': '55% 50%', 's0': 1.15, 's1': 1.0, 'cap': '보랏빛 쪽을 넘기는 손, 2014년',
   'lines': [{'t': '함께 가던 사람들이 길을 이어 갔고, 책은 이탈리아에 남았어요.'},
             {'t': '1,300년이 지난 지금, 이 책은 피렌체의 라우렌치아나 도서관에 있어요.'}],
   'kid': [{'t': '그 책은 지금 이탈리아의 큰 도서관에 있대.'}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '양피지를 넘길 때마다 바스락 소리가 나요.'}, {'t': '두 팔로 안아도 버거운 책 한 권에, 아홉 칸 책장이 통째로 들어 있어요.'}, {'t': '이 책을 실은 배가 바다 위에서 출렁여요.'}],
   'kid': [{'t': '눈을 감아 봐. 커다란 책장을 넘기면 바스락!'}, {'t': '이 책을 싣고 배가 출렁출렁 먼 바다로 가.'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
