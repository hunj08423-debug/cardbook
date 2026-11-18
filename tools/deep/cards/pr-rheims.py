# -*- coding: utf-8 -*-
"""깊은 카드: 두에-랭스 성경(pr-rheims) · 중심 방식 = 펼쳐 읽기 · 도우미 = 고르기
기준서 2판 · 틀 deep3-4 · 키트 3판 · 2026-11-18 만듦 · 32번 묶음
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 1589년 런던, 갓 나온 풀크의 큰 책을 펼치면 서로 맞선 두 번역이
     한 쪽에 두 단으로 나란히 놓여 있는 때.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 이 책의 첫 장(표제지) — 무엇을 싣고 무엇을 하려는지가
     책 이름에 길게 적혀 있어요. 표제지를 위에서부터 한 줄씩 펼쳐 읽어요.
     원문은 도서관 자료집의 옮겨 적기만 썼어요(그림 속 글씨를 직접 읽어 옮기지 않았어요).
  도우미: 고르기 — 1611년 번역자의 자리에서 야고보서 1장 5절의 ‘나무라지 않으신다’를 세 가지 옛 옮김 가운데 골라요
     (카를턴 1902, 58~59쪽과 표 I · 여러 옛 번역을 나란히 실은 자료).
  5단계: 고르기(묶음 안 두 번째 · 구텐베르크 카드와 붙어 있지 않음) 또는 아이와 함께 끝까지 보기.
  끝맺는 꼴: 생각이 바뀐 자리 — 앞면 물음(못하다는 걸 보이려고 나란히 찍었는데 결과는 뜻밖)으로 돌아가
     ‘처음엔 …, 이제는?’으로 물어요.
카드 크기: 한 장면 카드(장면 2개) — 재료가 이 책의 첫 장과 두 단에 몰려 있어요.
그림 원본(src)은 deep_src/pr-rheims/ (저장소 밖). 위키미디어 그림은 같은 책의 표제지와 마태복음 첫 쪽을
나란히 놓은 것이에요(두 쪽의 바탕색이 달라요). 두 장면 그림은 이 안내서가 그 그림을 왼쪽 반·오른쪽 반으로 잘랐어요."""
S = 'pr-rheims/'
F = 'Title_Page_of_the_Rheims_New_Testament_with_the_first_page_of_the_Gospel_Accordi.jpg'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

COM = 'https://commons.wikimedia.org/wiki/File:Title_Page_of_the_Rheims_New_Testament_with_the_first_page_of_the_Gospel_According_to_Matthew_Compared_with_the_Bishop%27s_Bible,_1589.jpg'
SFU = 'https://bep.dhil.lib.sfu.ca/books/17'
CLARK = 'https://clarklibrary.ucla.edu/?p=3749'
MOTB2 = 'https://collections.museumofthebible.org/artifacts/16134-rheims-bishops-parallel-new-testament-second-edition'
MOTBD = 'https://collections.museumofthebible.org/artifacts/57848-a-defense-of-the-sincere-and-true-translation-of-the-holy-scriptures'
MOTB4 = 'https://collections.museumofthebible.org/artifacts/57872-rheims-bishops-parallel-new-testament-fourth-edition'
KEN = 'https://www.bible-researcher.com/rheims2.html'
CARL = 'https://archive.org/details/partofrheimsinma00carlrich'
FG = 'https://faithofgod.net/NTcompare/James.htm'
DR = 'https://douayrheimsbible.pages.dev/compare/james/1'
THAY = 'https://www.blueletterbible.org/lexicon/G3679/tr'
WEB = 'https://websters1913.timcieplowski.com/word/upbraid/'
MWA = 'https://www.merriam-webster.com/dictionary/argument'
MWC = 'https://www.merriam-webster.com/dictionary/catholic'
MOR89 = 'https://www.themorgan.org/printed-books/53724'
MOR01 = 'https://www.themorgan.org/printed-books/220108'
TOL = 'https://emuseum.toledomuseum.org/objects/43078/english-bible-also-called-the-king-james-bible'
ECU = 'https://librarycatalog.ecu.edu/catalog/5387415'
WP = 'https://en.wikipedia.org/wiki/Douay%E2%80%93Rheims_Bible'
CR = '자료: 풀크의 대조판 신약(1589) · 퍼블릭 도메인 · 위키미디어 공용'

CARD = {
 'id': 'pr-rheims', 'mode': '펼쳐 읽기',
 'pagetitle': '두에-랭스 성경',
 'brandsub': '깊은 카드 · 펼쳐 읽기',
 'where': '<b>1582년 · 1589년</b><span>랭스에서 옮기고, 런던에서 나란히 찍다</span>',
 'lead': '1589년 런던에서, 가톨릭의 랭스 신약과 개신교의 주교 성경을 한 쪽에 나란히 찍은 책이 나왔어요. 랭스 번역을 반박하려고 엮은 책이에요. 첫 장의 긴 제목을 한 줄씩 펼쳐 읽고, 야고보서의 한 구절을 1611년 번역자의 자리에서 옮겨 봐요.',
 'leadKid': '두 가지 성경을 나란히 찍은 책이 있대. 첫 장부터 한 줄씩 펼쳐 볼까?',
 'meta': '영화처럼 약 2분 · 천천히 읽으면 4분',
 'draft': '검수 전 시안이에요(기준서 2판). 표제지의 글은 대학 도서관 자료집에 옮겨 적힌 것을 따랐고, 그림 속 글씨를 직접 읽어 옮기지 않았어요. 옛 영어 성경들의 구절은 여러 번역을 나란히 실은 자료와 1902년 카를턴의 연구를 따랐어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 2분',
 # 화면 색: 옛 책 가죽 표지의 밤빛(밝게·어둡게 두 벌)
 'theme': """:root{--accent:#7A4A26;--accent-ink:#fff8f1;--soft:rgba(122,74,38,.09);--stamp:#8a4f24}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#dcb38d;--accent-ink:#17100a;--soft:rgba(220,179,141,.10);--stamp:#e6bf98}}
:root[data-theme="dark"]{--accent:#dcb38d;--accent-ink:#17100a;--soft:rgba(220,179,141,.10);--stamp:#e6bf98}""",
 'stamp': {'t': '대조판', 'y': '1589', 'sub': '런던'},
 'doneNote': '첫 장의 긴 제목부터 한 구절의 세 가지 옮김까지, 나란히 놓인 두 번역을 읽어 왔어요.',
 'images': {
  'card': {'src': S + F,
           'cap': '풀크의 대조판 신약(1589) — 표제지와 마태복음 첫 쪽',
           'cr': CR, 'u': COM,
           'alt': '옛 책의 두 쪽을 나란히 놓은 그림. 왼쪽은 무늬 테두리 안에 큰 글씨 제목이 여러 줄 찍힌 표제지로, 푸르스름하게 보인다. 오른쪽은 누렇게 바랜 쪽으로, THE HOLY GOSPEL OF IESVS CHRIST라는 큰 제목 아래 두 가지 번역이 두 단으로 나란히 찍혀 있다.'},
  'tp': {'src': S + F, 'crop': (0.0, 0.0, 0.5, 1.0), 'max': 2560,
         'cap': '표제지(첫 장) — 이 안내서가 그림의 왼쪽 반을 잘랐어요',
         'cr': CR, 'u': COM,
         'alt': '푸르스름하게 찍힌 옛 책의 첫 장. 꽃과 덩굴, 열매를 새긴 넓은 무늬 테두리가 둘레를 감싸고, 양옆에는 긴 옷을 입은 사람이 식물을 꽂은 긴 그릇을 들고 서 있다. 맨 아래 가운데에는 소머리가, 양쪽에는 가면 곁에 엎드린 사자가 있다. 가운데 흰 칸에 THE TEXT OF THE NEW TESTAMENT로 시작하는 제목이 여러 줄 찍혀 있고, 가운데쯤 WITH 양옆에 손으로 쓴 글씨가 있다.'},
  'mt': {'src': S + F, 'crop': (0.5, 0.0, 1.0, 1.0),
         'cap': '마태복음 1장 — 왼쪽 단은 랭스, 오른쪽 단은 잉글랜드 교회의 번역',
         'cr': CR, 'u': COM,
         'alt': '누렇게 바랜 쪽. 맨 위에 짐승과 덩굴을 새긴 띠 장식이 있고, 그 아래 THE ARGVMENT OF S. MATTHEWES GOSPEL이라는 제목과 기울인 글씨의 짧은 글이 있다. 가운데에 큰 글씨로 THE HOLY GOSPEL OF IESVS CHRIST ACcording to Matthew가 찍혀 있다. 그 아래는 두 단으로, 왼쪽 단은 바로 선 글꼴, 오른쪽 단은 기울인 글꼴이고, 두 단 모두 무늬를 새긴 큰 T자로 시작한다. 양쪽 여백에는 작은 글씨로 성경 장절이 적혀 있다.'},
 },
 'scenes': [
  {'id': 'title', 'label': '긴 제목을 한 줄씩', 'kind': 'mod', 'mod': 'unroll',
   'text': ['1589년 런던에서 큰 책 한 권이 나왔어요. 개신교 목사이자 신학자인 윌리엄 풀크(William Fulke)가 엮은 신약이에요. 첫 장(표제지)에는 책 이름이 아주 길게 찍혀 있어요.',
            '이 긴 이름이 책의 차림표예요. 무엇을 싣고, 무엇을 하려는 책인지가 다 들어 있어요.'],
   'text2': ['풀크가 처음부터 이 큰 책을 낸 것은 아니에요. 1582년 랭스 신약을 옮긴 그레고리 마틴(Gregory Martin)은 같은 해에 책을 하나 더 냈어요. 개신교 쪽 영어 성경들이 일부러 그릇된 가르침이 들어가게 옮겼다고 따지는 책이었어요.',
             '풀크는 이듬해 그 책에 답하는 책을 냈어요. 그다음에 상대의 번역을 통째로 싣고 한 줄 한 줄 반박하는 이 책을 엮었어요.'],
   'kid': '다른 사람이 만든 성경을 통째로 싣고, 하나하나 반박하려고 만든 책이래.',
   'kidq': '책 이름이 이렇게 길어! 맨 아래에는 무엇이 적혀 있을까?'},
  {'id': 'columns', 'label': '두 단, 한 구절', 'kind': 'photo', 'img': 'mt', 'choose': True,
   'text': ['같은 책의 마태복음 첫 쪽이에요. 왼쪽 단 위에는 ‘랭스의 번역’, 오른쪽 단 위에는 ‘잉글랜드 교회의 번역’이라고 찍혀 있어요. 랭스 쪽은 바로 선 글꼴, 잉글랜드 교회 쪽은 기울인 글꼴이에요.',
            '신약 전체가 이렇게 두 단으로 이어져요. 랭스 신약의 줄거리 풀이와 주석도 다 실었어요. 맨 위에 ‘Rhem.’ 표시가 붙은 마태복음 줄거리가 그 하나예요. 장마다 끝에는 풀크의 반박이 붙어요.',
            bl('JAS.1', '야고보서 1장 5절') + '은 지혜가 모자라면 하나님께 구하라는 구절이에요. 하나님은 모든 사람에게 아낌없이 주시고 나무라지 않으신다고 해요. 이 ‘나무라지 않으신다’를 옛 영어 성경들은 저마다 다르게 옮겼어요.'],
   'text2': ['반박하려던 책이 뜻밖의 길을 열었어요. 성경 박물관은 이 책 덕분에 잉글랜드의 가톨릭 신자들도 랭스 신약을 더 쉽게 구하게 되었다고 적어요.',
             '1902년 제임스 카를턴(James Carleton)은 1611년 킹 제임스 성경을 옮긴 사람들도 아마 이 책으로 랭스 신약을 알았을 거라고 짐작했어요.'],
   'kid': '왼쪽은 바로 선 글씨, 오른쪽은 기울어진 글씨야. 같은 구절을 두 가지로 옮겼어.',
   'kidq': '두 단 모두 커다란 글자로 시작해. 무슨 글자일까?'},
 ],
 'imagine': {'t': '촛불 곁에 커다란 책이 펼쳐져 있어요. 손가락 하나는 왼쪽 단을, 다른 하나는 오른쪽 단을 짚고 천천히 내려가요. 같은 구절인데 낱말이 달라요. 한 낱말 앞에서 손가락이 멈추고, 입속으로 두 말을 번갈아 읽어 봐요.',
             'kid': '눈을 감아 봐. 커다란 책 위에 두 손가락. 나란히 내려가다가, 어? 낱말이 달라. 손가락이 멈춰.'},
 'lines': ['맞서려고 놓은 두 단, 나란히 읽힌 두 번역.', '반박하려고 실은 번역의 말이, 1611년 성경에도.', '나무라지 않으신다 — 한 구절, 세 가지 옮김.'],
 'linesKid': ['흉보려고 나란히 놓았는데, 서로 배웠대.', '같은 말을 세 가지로 옮겼어!'],
 'close': {'form': '생각이 바뀐 자리',
           'from': '앞면 물음(“개신교 학자가 가톨릭 영어 성경이 못하다는 걸 보이려고 두 번역을 나란히 찍었어요. 그런데 결과는 뜻밖이었어요.”)으로 돌아가요 — 반박하려고 놓은 두 단이 서로 견주어 읽는 자리가 되었고, 랭스의 말(upbraideth not)이 1611년 킹 제임스 성경에도 있어요',
           'ask': '처음엔 어느 번역이 못한지 보이려고 나란히 놓은 두 단이었어요. 이제 이 쪽을 다시 보면, 두 단 사이에서 무엇이 보이나요?',
           'askKid': '흉보려고 나란히 놓았는데, 오히려 서로 배웠대. 이제 두 단을 보면 어떤 생각이 들어?'},
 'goals': {
  's4': {'t': '긴 제목 끝까지', 'p': '표제지를 끝까지 펼쳐 여덟 줄을 다 읽으면 카드에 금박이 입혀져요.',
         'how': '첫 장면에서 표제지를 끝까지 펼쳐 읽어 보세요', 'done': '표제지를 끝까지 펼쳐 읽었어요',
         'ways': [{'id': 'unroll', 't': '표제지를 끝까지 펼쳐 여덟 줄 읽기'}]},
  's5': {'t': '1611년 번역자의 자리', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '두 번째 장면 끝에서 하나를 골라 보거나, ‘아이와 함께’를 켜고 영화를 끝까지 보세요', 'done': '그 자리에서 골라 봤어요',
         'ways': [{'id': 'choose', 't': '1611년 번역자의 자리에서 야고보서 1장 5절 옮겨 보기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'unroll': {
   'img': 'tp',
   'textFrom': '표제지 원문: 사이먼 프레이저 대학 도서관 누리집의 ‘잉글랜드 교구의 책들’ 자료집에 실린 옮겨 적기(1589년 판) · 우리말과 풀이: 이 안내서(그림 속 글씨를 직접 읽어 옮기지 않았어요)',
   'intro': '종이 아래쪽 굴대를 끌어 내리거나 ‘한 줄 더 펼치기’를 눌러, 표제지를 위에서부터 한 줄씩 읽어 보세요.',
   'lines': [
    {'y0': 22.6, 'y1': 31.6, 'x0': 23, 'x1': 77,
     'o': 'The text of the Nevv Testament of Iesus Christ, translated out of',
     'k': '예수 그리스도의 신약 본문. 옮긴 바탕은 —',
     'n': '옛 철자예요. ‘Nevv’는 New, ‘Iesus’는 Jesus예요. 도서관 자료집은 W를 V 두 개로 찍은 곳을 그대로 옮겨 적었어요.'},
    {'y0': 31.6, 'y1': 34.95, 'x0': 23, 'x1': 77,
     'o': 'the vulgar Latine by the papists of the traiterous seminarie at Rhemes. With arguments of',
     'k': '널리 쓰던 라틴어. 옮긴 이는 랭스의 ‘반역’ 신학교에 있는 ‘교황파’. 함께 실은 것은 —',
     'n': '라틴어 성경 불가타를 가리켜요. ‘교황파’와 ‘반역’은 풀크가 고른 날카로운 말이에요. 신학교는 두에에 있었는데, 신약이 나올 무렵 잠시 랭스로 옮겨 가 있었어요.'},
    {'y0': 34.95, 'y1': 40.2, 'x0': 23, 'x1': 77,
     'o': 'bookes, chapters, and annotations, pretending to discouer the corruptions of diuers translations, and to cleare the controuersies of these dayes.',
     'k': '책과 장마다 붙인 줄거리 풀이와 주석. 여러 번역의 잘못을 밝히고 요즘의 논쟁을 풀겠다고 내세우는 것들.',
     'n': '여기서 ‘arguments’는 줄거리 풀이예요. 랭스 신약의 주석은 개신교의 가르침을 반박하려고 붙인 것이었어요.'},
    {'y0': 40.4, 'y1': 46.0, 'x0': 23, 'x1': 77,
     'o': 'VVhereunto is added the translation out of the original Greeke, commonly vsed in the Church of England,',
     'k': '여기에 그리스어 원문에서 옮겨, 잉글랜드 교회에서 흔히 쓰는 번역을 덧붙였다.',
     'n': '1572년에 고친 주교 성경의 신약이에요. 표제지는 라틴어에서 옮긴 번역과 그리스어에서 옮긴 번역을 이렇게 맞세워요.'},
    {'y0': 46.0, 'y1': 55.9, 'x0': 23, 'x1': 77,
     'o': 'with a confutation of all such arguments, glosses, and annotations, as conteine manifest impietie, of heresie, treason and slander,',
     'k': '그리고 뚜렷한 불경과 이단, 반역과 비방을 담은 줄거리 풀이·짧은 풀이·주석을 모두 반박한 글.',
     'n': '풀크의 반박은 장마다 끝에 붙어요. WITH 양옆의 글씨는 뒷날 누군가 손으로 적어 넣은 것이에요(이 카드는 읽어 옮기지 않았어요).'},
    {'y0': 55.9, 'y1': 58.4, 'x0': 23, 'x1': 77,
     'o': 'against the catholike Church of God, and the true teachers thereof, or the translations vsed in the Church of England ...',
     'k': '하나님의 보편 교회와 그 참된 교사들, 또는 잉글랜드 교회가 쓰는 번역들을 겨눈 것들을.',
     'n': '‘catholike’는 그리스어 ‘보편적인’에서 온 말이에요. 이 아래 몇 줄은 도서관 자료집이 ‘…’로 줄여, 이 카드도 옮기지 않았어요.'},
    {'y0': 62.8, 'y1': 65.9, 'x0': 23, 'x1': 77,
     'o': 'By William Fulke, Doctor in Diuinitie.',
     'k': '신학 박사 윌리엄 풀크.',
     'n': '풀크(1538~1589)는 케임브리지 펨브로크 홀의 학장이었어요. 이 책이 나온 1589년에 세상을 떠났어요.'},
    {'y0': 66.5, 'y1': 73.3, 'x0': 23, 'x1': 77,
     'o': 'Imprinted at London : by the deputies of Christopher Barker, printer to the Queenes most excellent Maiestie, anno 1589.',
     'k': '런던에서 찍음. 여왕 폐하의 인쇄인 크리스토퍼 바커의 대리인들. 1589년.',
     'n': '바커는 엘리자베스 1세 여왕의 성경 인쇄인이었어요. 1611년 킹 제임스 성경을 찍은 로버트 바커가 그의 아들이에요.'},
   ],
   'done': '끝까지 펼쳤어요. 맞서려고 만든 책이 상대의 번역을 통째로 싣는다는 것이, 첫 장에 다 적혀 있어요.'},
  'choose': {
   'q': '1611년 킹 제임스 성경을 옮기던 사람이라면, 야고보서 1장 5절의 ‘나무라지 않으신다’를 어떻게 옮겼을까요?',
   'opts': [
    {'t': 'casteth no man in the teeth · 아무에게도 허물을 들이밀지 않는다',
     'r': '틴데일 신약(1526)부터 커버데일 성경, 주교 성경까지 쓴 말이에요. ‘이빨에 던진다’는 옛 표현으로, 대놓고 나무란다는 뜻이에요. 1611년 번역자들은 이 구절에서 이 말을 쓰지 않았어요.'},
    {'t': 'reproacheth no man · 아무도 꾸짖지 않는다',
     'r': '1560년 제네바 성경의 말이에요(그때 철자는 reprocheth). 1611년 번역자들은 이 구절에서 이 말도 쓰지 않았어요.'},
    {'t': 'upbraideth not · 나무라지 않는다',
     'r': '1582년 랭스 신약의 말이에요. 1611년 킹 제임스 성경도 이 말을 골랐어요. 다만 200년쯤 앞선 위클리프 성경에도 ‘vpbreidith not’이 있어요.'},
   ]},
 },
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>주고 나서 나무라지 않음</b> 세이어의 그리스어 사전은 ' + bl('JAS.1', '야고보서 1장 5절') + '의 ‘나무라다’를 ‘받은 은혜를 들먹이며 나무라다’라는 뜻으로 풀어요. 아낌없이 주시고, 준 것을 두고 나무라지 않으신다는 말이에요.',
    '<b>네 번 찍힌 책</b> 풀크의 대조판은 1589년 뒤에도 1601년, 1617년, 1633년에 다시 나왔어요. 1601년 판은 크리스토퍼 바커의 아들 로버트 바커가 찍었어요.',
    '<b>300년 뒤에도 이 책으로</b> 카를턴은 1902년 책 「영어 성경을 만드는 데 랭스가 맡은 몫」에서 신약을 구절마다 견준 표를 만들었어요. 머리말에서 그는 이 일에 풀크의 1601년 판을 썼다고 밝혀요. 랭스와 주교 성경이 나란히 찍혀 있어서였어요.']},
  {'h': '한 구절, 여러 옛 번역', 'p': [
    bl('JAS.1', '야고보서 1장 5절') + '의 ‘나무라지 않으신다’를 옛 영어 성경들은 이렇게 옮겼어요. 위클리프 성경 말고는 오늘 철자로 적었어요.',
    '<b>위클리프 성경(14세기 말)</b> vpbreidith not',
    '<b>틴데일 신약(1526) · 커버데일 성경 · 주교 성경</b> casteth no man in the teeth',
    '<b>제네바 성경(1560)</b> reproacheth no man',
    '<b>랭스 신약(1582)</b> upbraideth not',
    '<b>킹 제임스 성경(1611)</b> upbraideth not']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>어느 단이 기울인 글꼴일까</b> 모건 도서관의 1589년 판 목록은 주교 성경이 바로 선 글꼴, 랭스가 기울인 글꼴이라고 적었어요. 같은 도서관의 1601년 판 목록은 왼쪽 랭스가 바로 선 글꼴이라고 적었어요. 이 그림(1589년 판)에서는 왼쪽 랭스 단이 바로 선 글꼴이에요.',
    '<b>‘upbraideth not’은 랭스에서 왔을까</b> 카를턴은 킹 제임스 성경이 이 구절에서 옛 번역들 대신 랭스의 말을 골랐다고 보았어요. 그런데 그는 위클리프 성경을 견주는 데서 뺐어요. 머리말에서 이 물음과 맞닿지 않는다고 했어요. 위클리프 성경에도 ‘vpbreidith not’이 있으니, 이 말이 랭스에서 처음 나온 것은 아니에요.']},
  {'h': '더 찾아보기', 'p': [
    '풀크의 책과 옛 번역들을 더 보고 싶다면 이런 곳이 있어요.'],
   'links': [{'t': 'UCLA 클라크 도서관: 풀크의 대조판 첫 판(1589) 소개 — 반박하려던 책이 오히려 랭스 신약을 널리 읽히게 한 이야기', 'u': CLARK, 'm': '영어'},
             {'t': '인터넷 아카이브: 카를턴의 책(1902) 원문 — 구절마다 견준 표를 직접 넘겨 보기', 'u': CARL, 'm': '영어'},
             {'t': 'Faith of God: 야고보서를 일곱 가지 옛 영어 번역으로 나란히 보기 — 1장 5절을 찾아 견주어 보세요', 'u': FG, 'm': '영어'}]},
 ],
 'src': [
  {'l': '‘잉글랜드 교구의 책들(Books in English Parishes)’ 자료집(사이먼 프레이저 대학 도서관 누리집) — 1589년 판 표제지 옮겨 적기, 크리스토퍼 바커의 대리인들이 찍음, 풀크 1538~1589, 랭스와 주교 성경을 두 단에 나란히 · 장마다 끝에 풀크의 풀이, 랭스는 주로 그레고리 마틴이 불가타에서 옮김', 'u': SFU},
  {'l': 'UCLA 클라크 도서관 「The Text of the New Testament of Iesus Christ」 — 풀크는 가톨릭에 맞선 사람, 주교 성경과 랭스를 나란히, 신학교가 잠시 랭스에 있다가 두에로 돌아감, 반박이 오히려 랭스 신약을 더 널리 퍼뜨림, 랭스의 낱말이 킹 제임스 성경에, 1589년은 풀크가 세상을 떠난 해', 'u': CLARK},
  {'l': '성경 박물관: 대조판 신약 둘째 판(1601) — 풀크는 청교도 목사이자 신학자, 랭스를 주교 성경과 나란히 실어 한 줄씩 반박, 뜻하지 않게 잉글랜드의 가톨릭 신자들이 랭스 신약을 더 쉽게 구함', 'u': MOTB2},
  {'l': '성경 박물관: 풀크 「A Defense of the Sincere and True Translation」(1583) — 마틴이 1582년에 개신교 영어 성경들이 일부러 이단의 잘못을 넣었다고 주장, 풀크가 이 책으로 반박, 뒤에 더 큰 반박인 대조판', 'u': MOTBD},
  {'l': '성경 박물관: 대조판 신약 넷째 판(1633) — 랭스 신약은 개신교 가르침을 반박하려는 주석을 붙인 불가타 영어 번역', 'u': MOTB4},
  {'l': '프레더릭 케니언 「English Versions」(헤이스팅스 성경 사전, 1909 · Bible Research 보관) — 풀크가 랭스 신약을 1572년 주교 성경과 나란히 찍고 주석과 반박을 실음, 꽤 널리 읽힘, 킹 제임스 번역자들이 쓴 판본의 하나, 그레고리 마틴', 'u': KEN},
  {'l': '제임스 카를턴 「The Part of Rheims in the Making of the English Bible」(옥스퍼드, 1902 · 인터넷 아카이브) — 풀크는 펨브로크 홀 학장, 마틴의 「발견」에 먼저 답함, 1589년 판과 1601·1617·1633년 판, 번역자들이 “아마도” 풀크의 책으로 랭스를 알았을 것(짐작), 58~59쪽 야고보서 1장 5절(upbraideth not을 reproacheth no man·casteth no man in the teeth보다 고름), 표 I 203쪽, 머리말(1601년 판을 씀 · 위클리프는 이 물음과 맞닿지 않음)', 'u': CARL},
  {'l': 'Faith of God 「The New Testament compared: James」 — 야고보서 1장 5절: 위클리프 vpbreidith not, 틴데일 1526·1534·커버데일·주교 성경 casteth no man in the teeth, 제네바 reprocheth no man, 킹 제임스 1611 vpbraideth not', 'u': FG},
  {'l': '두에-랭스 성경 대조 누리집 — 야고보서 1장 5절, 1582~1610년 원래 판 “upbraideth not”(오늘 철자)', 'u': DR},
  {'l': '세이어 그리스어 사전(Blue Letter Bible) ὀνειδίζω — 야고보서 1장 5절: ‘받은 은혜를 들먹이며 나무라다’', 'u': THAY},
  {'l': '웹스터 사전(1913) upbraid — ‘나무라다, 이빨에 던지다(cast something in the teeth of)’', 'u': WEB},
  {'l': '메리엄-웹스터 사전 argument 3 — 책의 요약·줄거리', 'u': MWA},
  {'l': '메리엄-웹스터 사전 catholic — 보편 교회, 그리스어 katholikos(보편적인)에서', 'u': MWC},
  {'l': '모건 도서관 PML 18409(1589년 판) — 런던, 크리스토퍼 바커의 대리인들, 1589 · 주교 성경 바로 선 글꼴·랭스 기울인 글꼴이라고 적음(기록마다 다른 점)', 'u': MOR89},
  {'l': '모건 도서관 PML 128916(1601년 판) — 로버트 바커가 찍음, 랭스가 왼쪽 바로 선 글꼴·주교 성경이 오른쪽 기울인 글꼴, 장마다 뒤에 주석', 'u': MOR01},
  {'l': '털리도 미술관: 킹 제임스 성경(1611) — 로버트 바커는 엘리자베스 1세의 성경 인쇄인 크리스토퍼 바커의 아들, 1599년 가업을 이음, 1611년 킹 제임스 성경을 찍음', 'u': TOL},
  {'l': '이스트캐롤라이나 대학 도서관: 1633년 판 목록 — 표제지의 “sometime Mr. of Pembroock Hall in Cambridge”, 풀크 1538~1589', 'u': ECU},
  {'l': '위키미디어 공용: 1589년 대조판의 표제지와 마태복음 첫 쪽(퍼블릭 도메인) 정보', 'u': COM},
  {'l': '위키백과 「Douay–Rheims Bible」(길잡이로만)', 'u': WP},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 55%', 's0': 1.12, 's1': 1.0,
   'kicker': '1589 · 런던', 'title': '풀크의 대조판 신약',
   'lines': [{'t': '서로 맞선 두 번역을, 한 책에 나란히.'}, {'t': '왜 이렇게 찍었을까요?'}],
   'kid': [{'t': '두 가지 성경을 나란히 찍은 책이야.'}, {'t': '왜 그랬을까?'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '긴 제목을 한 줄씩'},
  {'type': 'mod', 'mod': 'unroll', 'ch': 1,
   'lines': [{'t': '첫 장에 찍힌 책 이름이에요.', 'act': 'open'},
             {'t': '예수 그리스도의 신약 본문.', 'act': 'line:1'},
             {'t': '라틴어에서 옮긴 이들을, 풀크는 날카로운 말로 불렀어요.', 'act': 'line:2'},
             {'t': '여기에 잉글랜드 교회의 번역을 덧붙이고,', 'act': 'line:4'},
             {'t': '그 주석을 모두 반박하겠다고 해요.', 'act': 'line:5'},
             {'t': '맨 아래, 여왕의 인쇄인 바커. 1589년.', 'act': 'all', 'wait': 1800}],
   'kid': [{'t': '맨 위 큰 글씨는 ‘신약 성경’이래.', 'act': 'line:1'},
           {'t': '남의 번역을 통째로 실었대.', 'act': 'line:4'},
           {'t': '맨 아래엔 1589년!', 'act': 'all', 'wait': 1200},
           {'t': '반박하려고 실었는데, 어떻게 됐을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '두 단, 한 구절'},
  {'type': 'img', 'ch': 2, 'img': 'mt', 'fit': 'cover', 'p0': '38% 30%', 'p1': '38% 72%', 's0': 1.0, 's1': 1.08, 'o': '45% 60%',
   'cap': '마태복음 1장 · 왼쪽 단 랭스, 오른쪽 단 잉글랜드 교회',
   'lines': [{'t': '같은 책의 마태복음 첫 쪽.'},
             {'t': '왼쪽 단은 랭스, 오른쪽 단은 잉글랜드 교회의 번역.'},
             {'t': '같은 구절을 두 번역으로 견주어 읽어요.'}],
   'kid': [{'t': '왼쪽은 바로 선 글씨, 오른쪽은 기울어진 글씨!'},
           {'t': '두 단 모두 큰 글자로 시작해. 무슨 글자일까?', 'ask': True}]},
  {'type': 'black', 'ch': 2,
   'lines': [{'t': '야고보서 1장 5절, ‘나무라지 않으신다’.'},
             {'t': '틴데일과 주교 성경은 casteth no man in the teeth.'},
             {'t': '제네바 성경은 reproacheth no man.'},
             {'t': '1611년 킹 제임스 성경은, 랭스와 같은 upbraideth not.', 'wait': 1800}],
   'kid': [{'t': '‘나무라지 않으신다’를 세 가지로 옮겼대.'},
           {'t': '1611년 성경은 랭스와 같은 말을 골랐어.', 'wait': 1200}]},
  {'type': 'imagine', 'ch': 3,
   'lines': [{'t': '촛불 곁에 펼친 커다란 책.'},
             {'t': '두 손가락이 왼쪽 단과 오른쪽 단을 나란히 짚어 내려가요.'},
             {'t': '같은 구절, 다른 낱말. 손가락이 한 낱말 앞에서 멈춰요.'}],
   'kid': [{'t': '눈을 감아 봐. 커다란 책 위에 두 손가락.'},
           {'t': '나란히 내려가다가, 멈춰!'}]},
  {'type': 'reward', 'ch': 3},
 ],
}
