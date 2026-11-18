# -*- coding: utf-8 -*-
"""깊은 카드: 사악한 성경(pr-wicked) · 중심 방식 = 따라 쓰기
기준서 2판 · 틀 deep3-4 · 키트 3판 · 2026-11-18 만듦 · 32번 묶음
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 1631년 런던에서 찍은 성경의 출애굽기 20장 14절, ‘Thou shalt commit adultery’ 한 줄 앞.
     위아래 줄에는 다 있는 not이 이 줄에만 없어요.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 법원이 책을 거둬 고치게 했고, 빠진 not은 주로 손으로 고쳤어요
     (성경 박물관 · 크리스 존스). 그 not을 다섯 획으로 써 넣어요. 글씨본은 이 안내서가 그렸고, 쓰는 차례는 오늘 손글씨 차례
     (리딩 유니버스: n down, hump · o around, close · t down, cross / 오크 국립 아카데미: n은 down, up and over)를 따랐어요.
  5단계: 아이와 함께 끝까지 보기.
  끝맺는 꼴: 궁금해하기 ☆ — “세 글자가 빠졌을 뿐인데, 사람들은 왜 그토록 무겁게 여겼을까요?”(정답을 정하지 않은 물음)
카드 크기: 한 장면 카드(장면 2개) — 재료가 1631년 판 한 권(표제지 · 출애굽기 20장)에 몰려 있어요.
그림 원본(src)은 deep_src/pr-wicked/ (저장소 밖)."""
S = 'pr-wicked/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

PRIN = 'https://catalog.princeton.edu/catalog/9946280023506421'
PENN = 'https://find.library.upenn.edu/catalog/9932957033503681'
MOTB = 'https://museumofthebible.org/magazine/impact/from-the-podcast-dr.-chris-jones-and-the-wicked'
STA = 'https://www.stationers.org/news/features/ruth-frendo-writes-about-robert-baker-infamously-known-for-his-printing-of-the-wicked-bible'
FOLGER = 'https://catalog.folger.edu/record/169429'
RU = 'https://readinguniverse.org/skill-explainer/handwriting-spelling-typing/handwriting/how-to-teach-letter-formation'
OAK = 'https://www.thenational.academy/teachers/programmes/english-primary-ks1/units/writing-lower-case-letters-in-print/lessons/formation-of-m-n-and-r'
TP_U = 'https://commons.wikimedia.org/wiki/File:Wicked_Bible_-_title_page.jpg'
PASS_U = 'https://commons.wikimedia.org/wiki/File:Wicked_Bible_-_wicked_passage.jpg'
EX_U = 'https://commons.wikimedia.org/wiki/File:Wicked_Bible_Exodus_20.jpg'
WP = 'https://en.wikipedia.org/wiki/Wicked_Bible'

CARD = {
 'id': 'pr-wicked', 'mode': '따라 쓰기',
 'pagetitle': '사악한 성경',
 'brandsub': '깊은 카드 · 따라 쓰기',
 'where': '<b>1631년</b><span>런던 · 왕의 인쇄인 로버트 바커와 마틴 루카스</span>',
 'lead': '1631년 런던에서 찍은 성경의 출애굽기 20장 14절에서 not 세 글자가 빠졌어요. 위아래 줄에는 다 있는 낱말이에요. 법원은 책을 거둬 고치게 했고, 빠진 낱말은 주로 손으로 써 넣었어요. 그 not을 한 획씩 써 넣어 봐요.',
 'leadKid': '성경에서 글자 세 개가 빠져서 큰일이 났대. 빠진 글자를 같이 써 넣어 볼까?',
 'meta': '영화처럼 약 2분 · 천천히 읽으면 4분',
 'draft': '검수 전 시안이에요(기준서 2판). 책과 벌금, 고친 방법은 대학 도서관 목록과 성경 박물관의 연구자 인터뷰, 문구상 조합의 글을 따랐고, 서로 다른 곳은 ‘기록마다 다른 점’에 적었어요. not 글씨본은 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 2분',
 # 화면 색: 오래된 종이의 짙은 황토빛(밝게·어둡게 두 벌)
 'theme': """:root{--accent:#7E6420;--accent-ink:#fffaf0;--soft:rgba(126,100,32,.10);--stamp:#8a6a1c}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#e0c574;--accent-ink:#17130a;--soft:rgba(224,197,116,.10);--stamp:#e8d088}}
:root[data-theme="dark"]{--accent:#e0c574;--accent-ink:#17130a;--soft:rgba(224,197,116,.10);--stamp:#e8d088}""",
 'stamp': {'t': 'not', 'y': '1631', 'sub': '출애굽기 20:14'},
 'doneNote': '빠졌던 not 세 글자를, 한 획씩 제자리에 써 넣었어요.',
 'images': {
  'tp': {'src': S + 'Wicked_Bible_-_title_page.jpg',
         'cap': '1631년 판의 표제지',
         'cr': '자료: 1631년 판 킹 제임스 성경 · 퍼블릭 도메인 · 위키미디어 공용',
         'u': TP_U,
         'alt': '누렇게 바랜 표제지. 가운데 하트 모양 칸에 THE HOLY BIBLE: CONTAINING THE OLD TESTAMENT AND THE NEVV라는 제목과 여러 줄의 글이 있다. 둘레의 테두리에는 왼쪽에 LEVI, DAN, GAD 같은 이름이 적힌 방패들이, 오른쪽에 둥근 틀 안의 사람 모습들이 줄지어 있고, 위와 아래에 큰 둥근 그림이 있다. 맨 아래에 Cum priuilegio라는 글이 보인다.'},
  'pass': {'src': S + 'Wicked_Bible_-_wicked_passage.jpg',
           'cap': '1631년 판 출애굽기 20장 12~16절',
           'cr': '자료: 1631년 판 킹 제임스 성경 · 퍼블릭 도메인 · 위키미디어 공용',
           'u': PASS_U,
           'alt': '누렇게 바랜 종이에 검은 활자가 찍힌 출애굽기 20장의 한 부분. 13절 Thou shalt not kill, 14절 Thou shalt commit adultery, 15절 Thou shalt not steale, 16절 Thou shalt not beare false witnesse가 차례로 보인다. 왼쪽 여백에 Deut., Matth. 같은 작은 장절 표시가 있다.'},
  'line': {'src': S + 'Wicked_Bible_-_wicked_passage.jpg', 'crop': (0.17, 0.385, 0.79, 0.748),
           'cap': '13~15절 — 이 안내서가 잘라 크게 보여요',
           'cr': '자료: 1631년 판 킹 제임스 성경 · 퍼블릭 도메인 · 위키미디어 공용',
           'u': PASS_U,
           'alt': '1631년 판 출애굽기 20장의 세 줄을 크게 자른 것. 위에서부터 13 Thou shalt not kill, 14 Thou shalt commit adultery, 15 Thou shalt not steale가 찍혀 있다. 가운데 줄에만 not이 없다.'},
  'ex20': {'src': S + 'Wicked_Bible_Exodus_20.jpg',
           'cap': '1631년 판의 출애굽기 20장 쪽(2020년 사진)',
           'cr': '사진: Narrington77 · CC BY-SA 4.0 · 위키미디어 공용',
           'u': EX_U,
           'alt': '비스듬히 찍은 옛 성경의 펼친 쪽. 따뜻한 불빛 아래 검은 활자 줄들이 기울어져 보이고, 가운데쯤 Thou shalt not kill, Thou shalt commit adultery, Thou shalt not steale 줄이 있다.'},
 },
 'scenes': [
  {'id': 'printer', 'label': '왕의 인쇄인이 찍은 책', 'kind': 'photo', 'img': 'tp',
   'text': ['1631년 런던에서 찍은 킹 제임스 성경의 표제지예요. 아래쪽에는 왕의 인쇄인 로버트 바커와 존 빌의 권리를 이어받은 이들이 찍었다고 적혀 있어요.',
            '가운데 글은 1611년 첫 판의 표제지와 거의 같아요. “원어에서 새로 옮기고, 앞선 번역들과 꼼꼼히 견주어 고쳤다.” 테두리 한쪽에는 이스라엘 지파의 이름을 적은 방패들이, 다른 쪽에는 사람 모습을 넣은 둥근 틀들이 줄지어 있어요.'],
   'text2': ['로버트 바커는 1611년 첫 판을 찍은 바로 그 인쇄인이에요. 그는 킹 제임스 성경을 찍는 독점권을 가졌고, 그 권리를 어긴 사람들을 고등 종교 법원(High Commission · 이 무렵 인쇄업자들의 일을 다루던 법원)에 여러 번 고발했어요.',
             '이번에는 동료 마틴 루카스와 함께 찍었어요. 크리스 존스는 이때 천 부쯤 찍었을 것으로 봐요.'],
   'kid': '400년 전에 찍은 성경이야. 이 성경에는 아주 유명한 실수가 있대.',
   'kidq': '테두리 왼쪽 방패에 짧은 이름들이 있어. DAN을 찾아볼까?'},
  {'id': 'not', 'label': '빠진 세 글자', 'kind': 'mod', 'mod': 'trace', 'img': 'line',
   'text': [bl('EXO.20', '출애굽기 20장') + '의 십계명이 적힌 쪽이에요. 13절은 사람을 죽이지 말라는 계명, 15절은 도둑질하지 말라는 계명이에요. 두 줄 모두 “Thou shalt not”으로 시작해요.',
            '그 사이 14절은 “Thou shalt commit adultery”라고 찍혔어요. 일곱째 계명 ‘간음하지 말라’(부부의 약속을 깨지 말라는 계명)에서 not 세 글자가 빠져, 뜻이 정반대가 되었어요.',
            '누군가 이 잘못을 알아챘고, 일은 고등 종교 법원으로 갔어요. 법원은 책을 거둬 바커에게 돌려보내, 고쳐서 팔게 했어요. 아래 글씨본은 이 안내서가 그렸어요. 쓰는 차례는 오늘 학교에서 배우는 손글씨 차례예요.'],
   'text2': ['같은 책 ' + bl('DEU.5', '신명기 5장 24절') + '에는 하나님의 ‘위대함(greatness)’이 ‘great ass(큰 나귀)’로 찍힌 곳도 있었어요.',
             '바커는 자기 잘못이 아니라 일꾼의 잘못이라며 맞섰고, 재판은 한 해 가까이 끌었어요. 벌금은 바커가 200파운드쯤, 루카스가 100파운드, 모두 300파운드였어요.'],
   'kid': '“하지 말라”에서 not이 빠져서 뜻이 거꾸로 됐대. 같이 써 넣어 볼까?',
   'kidq': '사진 속 다른 줄에서 not을 찾아볼까? 몇 번 나와?'},
 ],
 'imagine': {'t': '되돌아온 성경이 탁자 위에 쌓여 있어요. 한 사람이 책을 펼쳐 출애굽기 20장을 찾아요. 펜 끝에 먹을 찍어, 14절 Thou shalt와 commit 사이에 작게 not을 적어 넣어요. 먹이 마르기를 기다렸다가 책을 덮고, 다음 책을 펼쳐요.',
             'kid': '눈을 감아 봐. 책이 산처럼 쌓여 있어. 펜으로 작게 not, 다음 책도 not, 또 not.'},
 'lines': ['위아래 줄에는 있고, 이 줄에만 없는 세 글자.', '되돌아온 책마다, 손으로 써 넣은 not.', '한 낱말이 빠지자 계명이 거꾸로 섰어요.'],
 'linesKid': ['not 세 글자가 빠졌대!', '손으로 다시 써 넣었어.'],
 'close': {'form': '궁금해하기',
           'from': '출애굽기 20장 14절에서 빠진 not 세 글자 — 기록은 벌금과 재판, 손으로 고친 자국과 남은 책의 수를 남기지만, 사람들이 왜 그토록 무겁게 여겼는지는 말하지 않아요',
           'ask': '세 글자가 빠졌을 뿐인데, 사람들은 왜 그토록 무겁게 여겼을까요?',
           'askKid': '글자 세 개가 빠졌을 뿐인데, 왜 큰일이 났을까?'},
 'goals': {
  's4': {'t': '빠진 not 써 넣기', 'p': '빠진 not을 다섯 획 모두 써 넣으면 카드에 금박이 입혀져요.',
         'how': '두 번째 장면에서 빨간 점부터 다섯 획을 따라 써 보세요', 'done': '빠진 not을 써 넣었어요',
         'ways': [{'id': 'trace', 't': '빠진 not을 다섯 획으로 써 넣기'}]},
  's5': {'t': '아이와 함께', 'p': '아이와 함께 ‘영화처럼 보기’를 끝까지 보면 카드가 채색돼요.',
         'how': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'done': '아이와 함께 끝까지 봤어요',
         'ways': [{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'trace': {
   'glyph': {'vb': '0 0 240 240', 'name': 'not',
             'alt': '소문자 not 세 글자를 다섯 획으로 나눈 글씨본(이 안내서가 그림)',
             'strokes': [
              {'d': 'M22 108 L22 168', 't': 'n — 내리긋기',
               'p': '1631년, 왕의 인쇄인 로버트 바커와 마틴 루카스가 킹 제임스 성경을 다시 찍었어요.'},
              {'d': 'M22 126 C 28 112 40 106 50 106 C 63 106 70 116 70 130 L70 168', 't': 'n — 올라가 넘어 내리기',
               'p': '그 책의 출애굽기 20장 14절에서 이 낱말이 빠졌어요. 바로 위 13절과 아래 15절에는 그대로 있는 낱말이에요.'},
              {'d': 'M130 108 C 112 108 100 121 100 138 C 100 155 112 168 130 168 C 148 168 160 155 160 138 C 160 121 148 108 130 108', 't': 'o — 한 바퀴 돌아 닫기',
               'p': '누군가 이 잘못을 알아챘고, 일은 인쇄업자들의 일을 다루던 고등 종교 법원으로 갔어요.'},
              {'d': 'M200 76 L200 152 C 200 163 206 168 215 168 C 219 168 223 166 226 163', 't': 't — 내리긋기',
               'p': '법원은 책을 거둬 바커에게 돌려보내, 고쳐서 팔게 했어요.'},
              {'d': 'M184 108 L226 108', 't': 't — 가로 긋기: not',
               'p': '빠진 not은 주로 손으로 고쳤어요. 종이쪽을 붙여 고친 책도 있었지만, 고치지 않은 채 남은 책도 많았어요.'}]},
   'intro': '빨간 점에서 시작해, 흐린 선을 손가락이나 마우스로 따라 그어 보세요. 다섯 획이면 not이에요.',
   'hint': '빨간 점에서 시작해 흐린 선을 따라 그어 보세요. 다 그으면 먹색으로 바뀌어요.',
   'done': '“Thou shalt not commit adultery.” 빠졌던 세 글자가 제자리로 돌아왔어요.'}},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>풀 자국만 남은 책</b> 크리스 존스가 살핀 한 권은 not을 적은 종이쪽을 붙여 고쳤는데, 종이는 떨어져 나가고 풀 자국만 남았어요. 신명기의 ‘great ass’는 먹으로 덮어 지운 책들이 있었어요. 존스는 가장 값싼 방법으로 고쳤다고 말해요.',
    '<b>벌금의 끝</b> 바커는 300파운드 벌금을 끝내 내지 않았어요. 왕이 나서서, 바커가 그리스어 인쇄기를 갖추고 해마다 그리스어 책을 한 권 이상 찍으면 벌금을 없애 주겠다고 했어요. 바커는 그리스어 책을 한두 권 찍었지만, 세 해 뒤에도 독촉을 받았어요.',
    '<b>‘사악한 성경’이라는 이름</b> 이 별명은 런던에서 뉴욕 공공도서관을 위해 책을 모으던 미국인 헨리 스티븐스(Henry Stevens)가 붙였어요. 그가 찾은 한 권은 지금 뉴욕 공공도서관에 있어요.',
    '<b>두 권을 가진 박물관</b> 존스는 이 책을 영국 도서관, 옥스퍼드, 케임브리지, 더블린 트리니티 칼리지, 요크 민스터, 글래스고 등에서 살폈어요. 워싱턴의 성경 박물관은 드물게 두 권을 가지고 있어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>남은 책은 몇 권?</b> 앞면 카드는 25부쯤이라고 해요. 문구상 조합의 글은 14부라고 적었고, 크리스 존스는 기관에 17부, 개인에게 4~8부가 있다고 봐요.',
    '<b>모두 없앴을까?</b> 문구상 조합의 글은 거의 다 거둬 없앴다고 적어요. 존스는 법원이 책을 거둬 고쳐서 팔게 했고, 고치지 않은 채 남은 책도 많다고 말해요. 다 없어졌다고 한 스티븐스의 말도 맞지 않다고 봐요.',
    '<b>벌금은 바커를 무너뜨렸을까?</b> 문구상 조합의 글은 벌금이 바커를 무너뜨렸고, 그가 남은 삶을 빚진 사람을 가두는 감옥에서 보냈다고 적어요. 존스는 바커가 그 벌금을 끝내 내지 않았다고 말해요.']},
  {'h': '더 찾아보기', 'p': [
    '이 책을 연구한 사람의 이야기와 바커의 삶을 더 읽어 볼 수 있어요.'],
   'links': [{'t': '성경 박물관 매거진: 크리스 존스와 ‘사악한’ 성경 — 고친 자국, 남은 책의 수, 벌금의 끝', 'u': MOTB, 'm': '영어'},
             {'t': '문구상 조합: 로버트 바커와 ‘사악한 성경’ — 1611년 첫 판부터 1631년의 실수까지', 'u': STA, 'm': '영어'}]},
 ],
 'src': [
  {'l': '프린스턴 대학 도서관 목록(STC 2296) — 1631년 판 표제(newly translated out of the originall tongues, and with the former translations diligently compared and reuised, by His Maiesties speciall commandement ; appointed to be read in churches), 로버트 바커와 존 빌의 권리를 이은 이들, ‘Wicked Bible’ · 출애굽기 20장 14절 “Thou shalt commit adultery”, 외경 포함, 장식 테두리', 'u': PRIN},
  {'l': '펜실베이니아 대학 도서관 목록 — Printed at London : By Robert Barker ..., and by the assignes of Iohn Bill, 1631 · ‘Wicked Bible’', 'u': PENN},
  {'l': '성경 박물관 매거진 「From the Podcast: Dr. Chris Jones and the “Wicked” Bible」 — 바커의 독점권과 고등 종교 법원 고발, 누군가 알아챔, 벌금 바커 200파운드쯤·루카스 100파운드·모두 300파운드·끝내 내지 않음, 일꾼 탓, 한 해 가까이, 왕의 그리스어 인쇄 조건, 책을 거둬 고쳐 팔게 함·고치지 않은 책도 많음, 주로 손으로 고침·붙인 종이의 풀 자국·great ass는 먹으로 덮음, 천 부쯤, 기관 17부와 개인 4~8부, 헨리 스티븐스(뉴욕 공공도서관·이름 붙임), 살핀 기관들, 성경 박물관 두 권', 'u': MOTB},
  {'l': '문구상 조합(Stationers’ Company) 루스 프렌도의 글 — 로버트 바커: 1589년 조합에 들어옴, 1611년 킹 제임스 성경, 1631년 판에서 십계명의 not이 빠짐, 벌금이 그를 무너뜨림, 빚진 사람의 감옥, 대부분 거둬 없앰, 14부가 남음', 'u': STA},
  {'l': '폴저 셰익스피어 도서관 STC 2216 — 1611년 첫 판 표제(같은 구절)와 로버트 바커', 'u': FOLGER},
  {'l': '리딩 유니버스(WETA) 「How to Teach Letter Formation」 — n: down, hump · o: around, close · t: down, cross', 'u': RU},
  {'l': '오크 국립 아카데미 「Formation of m, n and r」 — m·n·r은 down, up and over', 'u': OAK},
  {'l': '위키미디어 공용: 1631년 판 표제지 사진(퍼블릭 도메인 · 소더비 2016) 정보', 'u': TP_U},
  {'l': '위키미디어 공용: 1631년 판 출애굽기 20장 12~16절 사진(퍼블릭 도메인 · 소더비 2016) 정보', 'u': PASS_U},
  {'l': '위키미디어 공용: 1631년 판 출애굽기 20장 쪽 사진(Narrington77, 2020 · CC BY-SA 4.0) 정보', 'u': EX_U},
  {'l': '위키백과 「Wicked Bible」(길잡이로만)', 'u': WP},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'ex20', 'fit': 'cover', 'p0': '45% 40%', 'p1': '50% 50%', 's0': 1.3, 's1': 1.1,
   'kicker': '1631 · 런던', 'title': '사악한 성경',
   'lines': [{'t': '1631년 런던에서 찍은 성경의 한 쪽.'}, {'t': '한 줄에서, 세 글자가 사라졌어요.'}],
   'kid': [{'t': '400년 전 성경의 한 쪽이야.'}, {'t': '어떤 글자가 사라졌을까?'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '왕의 인쇄인이 찍은 책'},
  {'type': 'img', 'ch': 1, 'img': 'tp', 'fit': 'cover', 'p0': '50% 35%', 'p1': '50% 50%', 's0': 1.15, 's1': 1.3, 'o': '50% 45%',
   'cap': '1631년 판의 표제지',
   'lines': [{'t': '왕의 인쇄인 로버트 바커가 찍은 성경.'},
             {'t': '가운데 글은 1611년 첫 판과 거의 같아요.'},
             {'t': '“앞선 번역들과 꼼꼼히 견주어 고쳤다.”'}],
   'kid': [{'t': '1611년에 처음 찍은 그 성경을 다시 찍었대.'},
           {'t': '테두리에서 DAN이라는 이름을 찾아볼까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '빠진 세 글자'},
  {'type': 'img', 'ch': 2, 'img': 'pass', 'fit': 'cover', 'p0': '20% 50%', 'p1': '74% 50%', 's0': 1.0, 's1': 1.0,
   'cap': '1631년 판 출애굽기 20장',
   'lines': [{'t': '13절, “Thou shalt not kill.”'},
             {'t': '14절, “Thou shalt commit adultery.”', 'wait': 1500},
             {'t': '15절, “Thou shalt not steale.”'}],
   'kid': [{'t': '위아래 줄에는 not이 있어.'},
           {'t': '가운데 줄에는? 없어!', 'ask': True}]},
  {'type': 'mod', 'mod': 'trace', 'ch': 2,
   'lines': [{'t': '빠진 not을 다시 써 넣어 봐요.'},
             {'t': '내리긋고, 올라가 넘어, n.', 'act': 'stroke:2'},
             {'t': '한 바퀴 돌아, o.', 'act': 'stroke:3'},
             {'t': '내리긋고 가로 그어, t.', 'act': 'stroke:5'},
             {'t': '법원은 책을 거둬 고치게 했어요. 주로 손으로.', 'act': 'all', 'wait': 1800}],
   'kid': [{'t': 'n, 쓱 쓱!', 'act': 'stroke:2'},
           {'t': 'o, 동그랗게!', 'act': 'stroke:3'},
           {'t': 't까지 쓰면 not!', 'act': 'all', 'wait': 1200},
           {'t': '빠진 글자를 다시 써 넣으니 어때?', 'ask': True}]},
  {'type': 'imagine', 'ch': 3,
   'lines': [{'t': '되돌아온 성경이 탁자 위에 쌓여 있어요.'},
             {'t': '펜 끝에 먹을 찍어, 14절에 작게 not.'},
             {'t': '먹이 마르면 책을 덮고, 다음 책을 펼쳐요.'}],
   'kid': [{'t': '눈을 감아 봐. 책이 산처럼 쌓여 있어.'},
           {'t': '펜으로 작게 not, 또 not.'}]},
  {'type': 'reward', 'ch': 3},
 ],
}
