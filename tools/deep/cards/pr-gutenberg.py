# -*- coding: utf-8 -*-
"""깊은 카드: 구텐베르크 성경(pr-gutenberg) · 중심 방식 = 만드는 차례
기준서 1판(보탬 11) · 틀 deep3-4 · 키트 3판(보탬) · 2026-11-18 만듦 · 32번 묶음
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 1450년대 마인츠 인쇄소 — 짜 놓은 활자에 먹을 바르고 압착기 손잡이를 당겨 첫 쪽이 찍혀 나오는 순간.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 인쇄소에서 실제로 한 일 — 강철 펀치 → 구리 틀 → 손 주형에 부어 활자 → 활자 상자 → 42줄 짜기
     → 먹 바르고 찍기 → 붉은 글씨는 손으로. 단추를 눌러 한 차례씩 해 봐요(그림은 이 안내서가 그렸어요).
  5단계: 고르기 — 1454년 프랑크푸르트에서 갓 찍은 낱장을 본 사람의 자리에서(고른 뒤 피콜로미니 편지에 남은 답).
  끝맺는 꼴: 기록 한 마디 — 피콜로미니의 1455년 3월 12일 편지 “안경 없이도 읽으실 수 있을 것입니다”(영화 끝 큰 인용).
카드 크기: 큰 카드 — 1455년 공증 문서, 피콜로미니 편지, 1568년 목판화, 남은 책 사진까지 재료가 넉넉해요.
그림 원본(src)은 deep_src/pr-gutenberg/ (저장소 밖). 받는 법: commons_get.py
인쇄 차례 그림은 /root/work/scripts/gut_steps.py로 그렸어요(카드에는 그림 글만 넣어요)."""
S = 'pr-gutenberg/'
RYL = 'https://rylandscollections.com/2025/07/31/introducing-the-early-european-print-collection/'
CAB = 'https://www.cabinet.ox.ac.uk/node/10570'
LOC = 'https://blogs.loc.gov/bibliomania/2024/12/17/just-my-type-making-letters-at-the-type-foundry/'
MOR = 'https://www.themorgan.org/collections/works/gutenberg/invention-of-printing'
WEL1 = 'https://wellcomecollection.org/works/j5mg28du'
WEL2 = 'https://wellcomecollection.org/works/rd7ce3yf'
HAL = 'https://hal.archives-ouvertes.fr/hal-01097147'
MZ = 'https://mainz.de/en/microsite/gutenberg-museum/Museum/ueber_das_Museum'
WP = 'https://en.wikipedia.org/wiki/Gutenberg_Bible'
FRESCO = 'https://commons.wikimedia.org/wiki/File:Pinturicchio._Enea_Silvio_Piccolomini_presents_emperor_Frederick_III_with_his_bride-to-be_Eleanora_of_Portugal._Siena_Cathedral,_Piccolomini_Library.jpg'

CARD = {
 'id': 'pr-gutenberg', 'mode': '만드는 차례',
 'pagetitle': '구텐베르크 성경',
 'brandsub': '깊은 카드 · 만드는 차례',
 'where': '<b>1450년대</b><span>독일 마인츠 · 프랑크푸르트</span>',
 'lead': '1450년대 독일 마인츠에서, 손으로 베끼지 않고 쇠 글자로 찍은 성경이 나왔어요. 강철에 새긴 글자 하나가 수백 개의 납 활자가 되고, 활자가 한 줄씩 모여 두 단 42줄의 한 쪽이 되었어요. 그 차례를 하나씩 따라가 봐요.',
 'leadKid': '도장처럼 쇠로 글자를 만들어 꾹 찍었대. 글자 하나가 책 한 쪽이 되기까지, 같이 만들어 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 6분',
 'draft': '검수 전 시안이에요(기준서 1판). 인쇄소의 차례는 도서관·박물관의 설명을 따랐고, 구텐베르크가 활자를 정확히 어떻게 부었는지는 아직 연구 중이라고 밝혔어요. 인쇄 차례 그림은 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 # 화면 색: 손으로 써넣은 붉은 제목(루브릭)의 색(밝게·어둡게 두 벌)
 'theme': """:root{--accent:#9C3527;--accent-ink:#fffaf5;--soft:rgba(156,53,39,.09);--stamp:#a63a2b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#e3a093;--accent-ink:#170f0c;--soft:rgba(227,160,147,.10);--stamp:#ec9a8a}}
:root[data-theme="dark"]{--accent:#e3a093;--accent-ink:#170f0c;--soft:rgba(227,160,147,.10);--stamp:#ec9a8a}""",
 'stamp': {'t': '활자', 'y': '1455', 'sub': '마인츠'},
 'doneNote': '강철에 거꾸로 새긴 글자 하나가 종이 위에 바로 설 때까지, 일곱 차례를 따라왔어요.',
 'images': {
  'card': {'src': S + 'Gutenberg_Bible_Lenox_Copy_New_York_Public_Library_2009._Pic_01.jpg',
           'cap': '뉴욕 공공도서관의 구텐베르크 성경(레녹스 본)',
           'cr': '사진: NYC Wanderer (Kevin Eng) · CC BY-SA 2.0 · 위키미디어 공용',
           'u': 'https://commons.wikimedia.org/wiki/File:Gutenberg_Bible,_Lenox_Copy,_New_York_Public_Library,_2009._Pic_01.jpg',
           'alt': '유리 진열장 안 투명한 받침대 위에 두꺼운 옛 책이 펼쳐져 있다. 누렇게 바랜 두 쪽에 검은 글씨가 두 단으로 빼곡하고, 오른쪽 쪽에는 붉은 글씨 몇 줄과 붉고 푸른 머리글자가 있다. 책 사이로 붉은 끈이 늘어져 있다.'},
  'founder': {'src': S + 'Schriftgiesser.jpg',
              'cap': '활자공 — 요스트 암만, 1568년 목판화',
              'cr': '그림: 요스트 암만(1568) · 퍼블릭 도메인 · 위키미디어 공용',
              'u': 'https://commons.wikimedia.org/wiki/File:Schriftgiesser.jpg',
              'alt': '흑백 목판화. 격자 창 앞 의자에 앉은 남자가 한 손에 작은 틀을 들고, 다른 손의 작은 국자를 그 위로 기울이고 있다. 곁에 네모난 화로가 있고, 바닥에는 바구니와 쇠막대들이 놓여 있다.'},
  'printer': {'src': S + 'Buchdrucker-1568.png',
              'cap': '인쇄소 — 요스트 암만, 1568년 목판화',
              'cr': '그림: 요스트 암만(1568) · 퍼블릭 도메인 · 위키미디어 공용',
              'u': 'https://commons.wikimedia.org/wiki/File:Buchdrucker-1568.png',
              'alt': '흑백 목판화. 앞쪽에서 한 남자는 종이를 끼운 틀을 들어 올리고, 곁의 남자는 두 손에 든 둥근 공으로 활자판에 먹을 바른다. 오른쪽에 나사가 달린 큰 나무 인쇄기가 있고, 뒤쪽 창가에서 두 사람이 활자를 짠다. 맨 앞에 종이 더미 두 개가 있다.'},
  'fresco': {'src': S + 'Pinturicchio._Enea_Silvio_Piccolomini_presents_emperor_Frederick_III_with_his_br.jpg',
             'crop': (0.12, 0.44, 0.90, 0.90),
             'cap': '가운데 주교관을 쓴 사람이 피콜로미니예요 — 핀투리키오, 1502~1508년 무렵, 시에나 대성당 피콜로미니 도서관',
             'cr': '그림: 핀투리키오 · 사진: Vvlasenko(Ввласенко) · CC BY 4.0 · 위키미디어 공용',
             'u': FRESCO,
             'alt': '벽화의 아랫부분. 많은 사람이 모여 있고, 가운데에 흰 주교관을 쓴 사람이 서 있다. 그 왼쪽에서 금빛 옷에 왕관을 쓴 남자가 붉은 옷을 입은 여인과 손을 맞잡고 있고, 뒤로 흰 말과 창을 든 사람들이 보인다.'},
 },
 'scenes': [
  {'id': 'trades', 'label': '쇠로 만든 글자', 'kind': 'duo', 'imgs': ['founder', 'printer'],
   'caps': ['활자공 — 요스트 암만, 1568년', '인쇄소 — 요스트 암만, 1568년'],
   'text': ['1450년대 마인츠에서 요하네스 구텐베르크(Johannes Gutenberg)는 책을 손으로 베끼는 대신 찍어 내는 일을 했어요. 1455년 11월 6일 마인츠에서 쓴 한 공증 문서(공증인이 증언을 받아 적은 문서)는 이 일을 ‘책 만드는 일’이라고 불러요.',
            '그 문서에는 돈을 댄 요한 푸스트(Johann Fust)가 구텐베르크에게 돈을 돌려 달라며 다툰 일이 적혀 있어요. 그 일에 든 것으로 종이와 양피지, 먹, 그리고 이름을 밝히지 않은 장치가 나와요.'],
   'text2': ['구텐베르크의 인쇄소를 그린 그림은 남아 있지 않아요. 위의 두 그림은 100여 년 뒤인 1568년, 요스트 암만(Jost Amman)이 새긴 목판화예요. 왼쪽은 화로 곁에서 녹인 쇠를 작은 틀에 붓는 활자공이에요. 오른쪽 인쇄소에서는 창가의 두 사람이 활자를 짜고, 앞의 두 사람이 먹을 바르고 종이를 얹어요.'],
   'kid': '쇠로 글자를 만들어 도장처럼 찍었대. 오른쪽 그림에서 먹을 바르는 사람을 찾아볼까?', 'kidq': '도장을 찍어 본 적 있어? 무엇을 찍었어?'},
  {'id': 'steps', 'label': '글자 하나가 한 쪽이 되기까지', 'kind': 'mod', 'mod': 'steps', 'night': False,
   'text': ['구텐베르크가 찾은 것은 같은 글자를 수백, 수천 개 똑같이 만들어 내는 길이었어요. 강철 도장(펀치), 구리 틀(모형), 손 주형이 그 길이에요. 아래 단추를 누를 때마다 한 차례씩 해 볼 수 있어요.',
            '구텐베르크가 남긴 설명서는 없어요. 이 차례는 뒷날 인쇄소의 기록과 남은 책을 바탕으로 도서관과 박물관이 설명하는 방법이에요. 활자를 정확히 어떻게 부었는지는 지금도 연구가 이어지고 있어요.'],
   'kid': '쇠 막대에 글자를 거꾸로 새기고, 구리에 꾹! 그 틀에 녹인 쇠를 부으면 글자가 하나 생겨.', 'kidq': '도장 글자는 왜 거꾸로 새겨야 할까?'},
  {'id': 'lines', 'label': '40줄에서 42줄로', 'kind': 'photo', 'img': 'card',
   'text': ['네 사람이 성경을 거의 같은 네 부분으로 나누어 한꺼번에 짰다고 봐요. 처음에는 한 단에 40줄을 넣다가, 글자 높이를 조금 줄여 42줄로 바꾸었어요.',
            '열한 묶음쯤 찍었을 때 찍을 부수를 늘리기로 하고, 이미 찍은 묶음은 다시 짜서 찍었어요. 그렇게 종이 책이 적어도 120부, 양피지 책이 40부쯤 나왔다고 봐요. 한 질은 큰 종이 643장으로, 두 권으로 묶게 만들었어요.'],
   'text2': ['붉은 제목도 처음에는 찍으려 했어요. 하지만 두 번 찍는 데 손이 너무 많이 가서 그만두었어요. 그래서 붉은 제목과 머리글자는 사람이 손으로 써넣었어요. 위 사진은 뉴욕 공공도서관의 레녹스 본이에요. 오른쪽 쪽의 붉은 글씨와 푸른 머리글자도 그렇게 들어갔어요.'],
   'kid': '처음엔 40줄, 나중엔 42줄! 빨간 글씨는 사람이 손으로 썼대.', 'kidq': '사진에서 빨간 글씨를 몇 군데 찾을 수 있어?'},
  {'id': 'letter', 'label': '안경 없이도', 'kind': 'photo', 'img': 'fresco', 'choose': True,
   'text': ['1454년 10월, 프랑크푸르트에서 제국 회의가 열렸어요. 오스만 제국에 맞설 일을 의논하는 자리였어요. 그 무렵 프랑크푸르트에서 한 ‘놀라운 사람’이 여러 권의 성경에서 갓 찍은 낱장 묶음을 사람들에게 보여 주었어요.',
            '회의에서 황제를 대신해 연설한 에네아 실비오 피콜로미니(Enea Silvio Piccolomini, 뒷날 교황 비오 2세)는 이듬해 3월 12일, 비너노이슈타트에서 로마의 후안 데 카르바할 추기경에게 편지를 썼어요.'],
   'quote': {'t': '저는 다 만든 성경은 보지 못했고, 여러 권에서 나온 낱장 묶음만 보았습니다. 글씨가 아주 깨끗하고 바르며 틀린 데가 없어서, 추기경님께서도 애쓰지 않고 안경 없이도 읽으실 수 있을 것입니다.',
             'from': '피콜로미니가 카르바할 추기경에게 보낸 편지(1455년 3월 12일) · 에릭 화이트의 영어 번역(2025)을 이 안내서가 옮김', 'u': RYL},
   'text2': ['위 벽화는 50여 년 뒤 핀투리키오(Pinturicchio)가 시에나 대성당 도서관에 그린 피콜로미니의 모습이에요. 가운데 주교관을 쓴 사람이 그예요. 황제 프리드리히 3세에게 신부가 될 포르투갈의 엘레오노르를 소개하는 장면이에요.'],
   'kid': '이탈리아에서 온 주교님이 갓 찍은 성경을 보고 편지를 썼대. 글씨가 아주 깨끗했대!', 'kidq': '안경 없이도 읽을 수 있는 글씨는 어떤 글씨일까?'},
 ],
 'imagine': {'t': '창 너머로 흐린 빛이 들어와요. 축축한 종이 냄새와 기름 먹 냄새가 섞여 있어요. 나무 나사가 삐걱 돌아가고, 손잡이를 당겼다 놓는 소리가 나요. 종이를 천천히 들어 올리자, 까만 글자 두 단이 반짝여요.',
             'kid': '눈을 감아 봐. 끼익, 나무 나사가 돌아가. 종이를 살짝 들어 올리면, 까만 글자가 반짝!'},
 'lines': ['거꾸로 새긴 글자가 바로 선 글자를 낳아요.', '한 번 새긴 글자가 수백 번 찍혀요.', '찍은 글자 곁에, 손으로 쓴 붉은 글씨.'],
 'linesKid': ['거꾸로 새기면 바로 찍혀!', '꾹 눌러 찍었어!'],
 'close': {'form': '기록 한 마디',
           'from': '피콜로미니가 카르바할 추기경에게 보낸 편지(1455년 3월 12일) — “안경 없이도 읽으실 수 있을 것입니다”. 마지막 장면의 인용이자 영화 끝 큰 인용',
           'ask': '압착기 손잡이를 당긴 뒤 첫 쪽을 들어 올리는 사람 곁에 서 있다면, 무엇을 묻고 싶나요?',
           'askKid': '도장을 꾹 찍고 들어 올릴 때처럼, 첫 쪽을 들어 올리면 어떤 기분일까?',
           'film': False},
 'goals': {
  's4': {'t': '일곱 차례 끝까지', 'p': '글자 하나가 책 한 쪽이 되기까지, 일곱 차례를 끝까지 해 보면 카드에 금박이 입혀져요.',
         'how': '두 번째 장면에서 ‘강철에 글자 새기기’부터 끝까지 눌러 보세요', 'done': '일곱 차례를 끝까지 해 봤어요',
         'ways': [{'id': 'steps', 't': '일곱 차례를 끝까지 해 보기'}]},
  's5': {'t': '그 자리의 물음', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '네 번째 장면 끝에서 하나를 골라 보거나, ‘아이와 함께’를 켜고 영화를 끝까지 보세요', 'done': '그 자리에서 물어봤어요',
         'ways': [{'id': 'choose', 't': '1454년 프랑크푸르트의 낱장 앞에서 하나 물어보기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'steps': {
   'svg': '<svg viewBox="0 0 360 280" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="gtSt" x1="0" x2="1"><stop offset="0" stop-color="#c3c9d0"/><stop offset=".55" stop-color="#8d949c"/><stop offset="1" stop-color="#666d75"/></linearGradient><linearGradient id="gtCu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#dc9a62"/><stop offset="1" stop-color="#a65f2e"/></linearGradient><linearGradient id="gtPb" x1="0" x2="1"><stop offset="0" stop-color="#b8bcc1"/><stop offset=".6" stop-color="#8f949a"/><stop offset="1" stop-color="#72777d"/></linearGradient><linearGradient id="gtWd" x1="0" x2="1"><stop offset="0" stop-color="#a07a4e"/><stop offset="1" stop-color="#7c5a35"/></linearGradient></defs><rect width="360" height="280" rx="12" fill="#f3ead6"/><path d="M14 128 H346" stroke="#d8cbb0" stroke-width="1.2" stroke-dasharray="3 4"/><rect data-off="2" x="144" y="68" width="72" height="46" rx="4" fill="none" stroke="#c4b48c" stroke-width="1.4" stroke-dasharray="5 4"/><rect data-off="3" x="252" y="30" width="58" height="82" rx="3" fill="none" stroke="#c4b48c" stroke-width="1.4" stroke-dasharray="5 4"/><rect data-off="4" x="14" y="142" width="110" height="118" rx="4" fill="none" stroke="#c4b48c" stroke-width="1.4" stroke-dasharray="5 4"/><rect data-off="5" x="156" y="140" width="184" height="128" rx="3" fill="none" stroke="#c4b48c" stroke-width="1.4" stroke-dasharray="5 4"/><rect x="42" y="12" width="26" height="62" rx="3" fill="url(#gtSt)" stroke="#59606a" stroke-width="1.2"/><rect x="32" y="72" width="46" height="40" rx="4" fill="#8f969f" stroke="#59606a" stroke-width="1.2"/><g data-s="1"><text transform="translate(54,102) scale(-1,1)" text-anchor="middle" font-family="Georgia,\'Times New Roman\',serif" font-weight="700" font-size="34" fill="#e6e9ec" opacity=".85">a</text><text transform="translate(55,103) scale(-1,1)" text-anchor="middle" font-family="Georgia,\'Times New Roman\',serif" font-weight="700" font-size="34" fill="#2c3137">a</text></g><g data-s="2"><path d="M84 92 H134" stroke="#9a7b55" stroke-width="2" stroke-linecap="round"/><path d="M128 86 L136 92 L128 98" fill="none" stroke="#9a7b55" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><rect x="144" y="68" width="72" height="46" rx="4" fill="url(#gtCu)" stroke="#7c4520" stroke-width="1.2"/><text transform="translate(181.3,103.3)" text-anchor="middle" font-family="Georgia,\'Times New Roman\',serif" font-weight="700" font-size="34" fill="#f0c194" opacity=".9">a</text><text transform="translate(180,102)" text-anchor="middle" font-family="Georgia,\'Times New Roman\',serif" font-weight="700" font-size="34" fill="#5a2e12">a</text></g><g data-s="3"><path d="M220 92 H244" stroke="#9a7b55" stroke-width="2" stroke-linecap="round"/><path d="M238 86 L246 92 L238 98" fill="none" stroke="#9a7b55" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M252 30 H286 V112 H270 V52 H252 Z" fill="url(#gtWd)" stroke="#5e4226" stroke-width="1.2"/><path d="M310 30 H294 V112 H310 Z" fill="url(#gtWd)" stroke="#5e4226" stroke-width="1.2"/><rect x="286" y="40" width="8" height="70" fill="#7d8288"/><path d="M290 10 C 290 18 290 26 290 36" stroke="#f2a33a" stroke-width="4" stroke-linecap="round"/><circle cx="290" cy="8" r="5" fill="#f6b24a"/><rect x="320" y="56" width="22" height="56" rx="2" fill="url(#gtPb)" stroke="#5f6469" stroke-width="1.1"/><rect x="318" y="44" width="26" height="16" rx="2" fill="#9ea3a9" stroke="#5f6469" stroke-width="1.1"/><text transform="translate(331,57) scale(-1,1)" text-anchor="middle" font-family="Georgia,\'Times New Roman\',serif" font-weight="700" font-size="15" fill="#2c3137">a</text></g><g data-s="4"><rect x="14" y="142" width="110" height="118" rx="4" fill="url(#gtWd)" stroke="#5e4226" stroke-width="1.2"/><rect x="18.0" y="146.0" width="24" height="25.6" fill="#6f5232"/><rect x="21.0" y="151.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="28.0" y="154.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="35.0" y="151.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="18.0" y="174.2" width="24" height="25.6" fill="#6f5232"/><rect x="21.0" y="179.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="28.0" y="182.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="35.0" y="179.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="18.0" y="202.4" width="24" height="25.6" fill="#6f5232"/><rect x="21.0" y="207.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="28.0" y="210.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="35.0" y="207.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="18.0" y="230.6" width="24" height="25.6" fill="#6f5232"/><rect x="21.0" y="235.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="28.0" y="238.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="35.0" y="235.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="44.5" y="146.0" width="24" height="25.6" fill="#6f5232"/><rect x="47.5" y="151.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="54.5" y="154.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="61.5" y="151.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="44.5" y="174.2" width="24" height="25.6" fill="#6f5232"/><rect x="47.5" y="179.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="54.5" y="182.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="61.5" y="179.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="44.5" y="202.4" width="24" height="25.6" fill="#6f5232"/><rect x="47.5" y="207.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="54.5" y="210.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="61.5" y="207.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="44.5" y="230.6" width="24" height="25.6" fill="#6f5232"/><rect x="47.5" y="235.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="54.5" y="238.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="61.5" y="235.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="71.0" y="146.0" width="24" height="25.6" fill="#6f5232"/><rect x="74.0" y="151.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="81.0" y="154.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="88.0" y="151.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="71.0" y="174.2" width="24" height="25.6" fill="#6f5232"/><rect x="74.0" y="179.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="81.0" y="182.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="88.0" y="179.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="71.0" y="202.4" width="24" height="25.6" fill="#6f5232"/><rect x="74.0" y="207.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="81.0" y="210.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="88.0" y="207.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="71.0" y="230.6" width="24" height="25.6" fill="#6f5232"/><rect x="74.0" y="235.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="81.0" y="238.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="88.0" y="235.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="97.5" y="146.0" width="24" height="25.6" fill="#6f5232"/><rect x="100.5" y="151.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="107.5" y="154.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="114.5" y="151.0" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="97.5" y="174.2" width="24" height="25.6" fill="#6f5232"/><rect x="100.5" y="179.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="107.5" y="182.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="114.5" y="179.2" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="97.5" y="202.4" width="24" height="25.6" fill="#6f5232"/><rect x="100.5" y="207.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="107.5" y="210.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="114.5" y="207.4" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="97.5" y="230.6" width="24" height="25.6" fill="#6f5232"/><rect x="100.5" y="235.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="107.5" y="238.6" width="5" height="15" rx="1" fill="#9ca1a7"/><rect x="114.5" y="235.6" width="5" height="15" rx="1" fill="#9ca1a7"/></g><g data-s="5" data-off="6"><rect x="156" y="140" width="184" height="128" rx="3" fill="#ddd6c6" stroke="#9a9284" stroke-width="1.2"/><rect x="192" y="152.0" width="52" height="4.6" rx="1" fill="#8e939a"/><rect x="192" y="160.6" width="52" height="4.6" rx="1" fill="#8e939a"/><rect x="192" y="169.2" width="52" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="177.8" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="186.4" width="68" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="195.0" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="203.6" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="212.2" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="220.8" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="229.4" width="68" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="238.0" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="246.6" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="168" y="255.2" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="152.0" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="160.6" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="169.2" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="177.8" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="186.4" width="68" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="195.0" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="212.2" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="220.8" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="229.4" width="68" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="238.0" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="246.6" width="76" height="4.6" rx="1" fill="#8e939a"/><rect x="254" y="255.2" width="76" height="4.6" rx="1" fill="#8e939a"/></g><g data-s="6"><rect x="156" y="140" width="184" height="128" rx="3" fill="#fbf7ec" stroke="#cfc4ad" stroke-width="1.2"/><rect x="192" y="152.0" width="52" height="4.6" rx="1" fill="#211d18"/><rect x="192" y="160.6" width="52" height="4.6" rx="1" fill="#211d18"/><rect x="192" y="169.2" width="52" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="177.8" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="186.4" width="68" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="195.0" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="203.6" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="212.2" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="220.8" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="229.4" width="68" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="238.0" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="246.6" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="168" y="255.2" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="152.0" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="160.6" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="169.2" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="177.8" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="186.4" width="68" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="195.0" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="212.2" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="220.8" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="229.4" width="68" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="238.0" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="246.6" width="76" height="4.6" rx="1" fill="#211d18"/><rect x="254" y="255.2" width="76" height="4.6" rx="1" fill="#211d18"/><circle cx="140" cy="226" r="8.5" fill="#3a2a1e"/><rect x="138" y="206" width="4" height="12" rx="1.5" fill="#8a6a45"/><circle cx="140" cy="252" r="8.5" fill="#3a2a1e"/><rect x="138" y="232" width="4" height="12" rx="1.5" fill="#8a6a45"/></g><g data-s="6" data-off="7"><rect x="244" y="114" width="8" height="14" fill="#8a6a45" stroke="#5e4226" stroke-width="1"/><path d="M244 118 H252 M244 122 H252 M244 126 H252" stroke="#5e4226" stroke-width="1"/><rect x="150" y="128" width="196" height="9" rx="2" fill="#6b4b2b"/><path d="M222 116 H274" stroke="#5e4226" stroke-width="3" stroke-linecap="round"/></g><g data-s="7"><rect x="168" y="150" width="20" height="24" rx="2" fill="#2f5d9b"/><text x="178" y="170" text-anchor="middle" font-family="Georgia,\'Times New Roman\',serif" font-weight="700" font-size="21" fill="#f3ead6">I</text><path d="M166 176 C 162 190 170 198 164 214" stroke="#b3342a" stroke-width="1.2" fill="none"/><rect x="254" y="203.6" width="52" height="4.6" rx="1" fill="#b3342a"/><rect x="190" y="146" width="40" height="3.2" rx="1" fill="#b3342a"/><path d="M356 140 L341 176" stroke="#5e4226" stroke-width="2" stroke-linecap="round"/><path d="M357 138 C 351 142 347 150 345 160 C 351 154 355 147 357 138 Z" fill="#efe7d6" stroke="#9a8f7b" stroke-width="1"/></g></svg>',
   'alt': '이 안내서가 그린 인쇄 차례 그림. 위에는 강철 막대, 구리 틀, 나무 손 주형과 활자 하나가, 아래에는 활자 상자와 두 단으로 짠 한 쪽이 차례로 나타나요.',
   'cap': '이 안내서가 그린 인쇄 차례 · 미국 의회도서관 블로그(2024)와 모건 도서관의 설명을 바탕으로 · 글자는 알아보기 쉽게 오늘 글꼴로 그렸어요',
   'intro': '단추를 누를 때마다 한 차례씩 만들어져요. 글자 하나가 거꾸로, 바로, 다시 거꾸로 되었다가 마지막에 종이 위에 바로 서는 것을 눈여겨보세요.',
   'hint': '아래 ‘강철에 글자 새기기’부터 눌러 보세요.',
   'marksLabel': '글자 하나의 모습',
   'marks': [{'t': '강철 끝: 거꾸로 볼록', 'c': '#7b838c', 's': 1},
             {'t': '구리 틀: 바로 오목', 'c': '#b8703f', 's': 2},
             {'t': '납 활자: 거꾸로 볼록', 'c': '#9ca1a7', 's': 3},
             {'t': '종이: 바로 선 글자', 'c': '#5a5047', 's': 6},
             {'t': '붉은 제목: 손글씨', 'c': '#b3342a', 's': 7}],
   'steps': [
     {'do': '강철에 글자 새기기', 't': '펀치', 'p': '단단한 강철 막대 끝에 글자를 거꾸로 새겨요. 줄로 둘레를 갈아 내서 글자만 도장처럼 볼록하게 남겨요.'},
     {'do': '구리에 두드려 박기', 't': '구리 틀(모형)', 'p': '펀치를 무른 구리에 대고 망치로 두드려요. 찰흙에 도장을 누른 것처럼 오목한 자국이 나는데, 이번에는 글자가 바로 읽혀요.'},
     {'do': '틀에 녹인 쇠 붓기', 't': '손 주형', 'p': '구리 틀을 손 주형 바닥에 끼우고, 주로 납으로 된 녹인 쇠를 부어요. 식으면 주형을 열어 길쭉한 활자 하나를 꺼내요. 얼음 틀에 물을 부어 얼음을 꺼내는 것과 비슷해요.'},
     {'do': '같은 글자 수백 개', 't': '활자 상자', 'p': '틀 하나로 같은 글자를 몇 번이고 다시 부어요. 다 부은 활자는 글자마다 칸을 나눈 상자에 담아요.'},
     {'do': '한 줄씩 짜기', 't': '짜기(조판)', 'p': '활자를 한 자씩 집어 줄을 만들고, 줄을 쌓아 두 단 42줄의 한 쪽을 짜요. 머리글자 자리와 붉은 제목 자리는 비워 둬요.'},
     {'do': '먹 바르고 찍기', 't': '나사 압착기', 'p': '둥근 먹 공 두 개로 기름 먹을 고루 바르고, 종이를 얹은 뒤 나사 손잡이를 당겨 꾹 눌러요. 포도즙을 짜던 나사 틀과 같은 원리예요.'},
     {'do': '붉은 글씨는 손으로', 't': '붉은 제목과 머리글자', 'p': '비워 둔 자리에 붉은 제목과 푸른 머리글자를 사람이 손으로 써넣어요. 그래서 같은 쪽이라도 책마다 조금씩 달라요.'},
   ],
   'done': '다 만들었어요. 강철에 거꾸로 새긴 글자 하나가, 구리 틀과 납 활자를 거쳐 종이 위에 바로 섰어요.',
  },
  'choose': {
   'q': '1454년 프랑크푸르트에서 갓 찍은 낱장 묶음을 본 사람이라면, 무엇부터 물어볼까요?',
   'opts': [{'t': '몇 권이나 찍나요?', 'r': '피콜로미니는 여러 사람에게서 158권이 다 되었다고 들었고, 180권이라는 사람도 있었다고 적었어요.'},
            {'t': '한 권 살 수 있나요?', 'r': '그는 한 권 사 보겠다고 하면서도, 다 만들기도 전에 살 사람이 다 정해졌다더라며 어려울 것 같다고 적었어요.'},
            {'t': '누가 만들었나요?', 'r': '편지는 그 사람의 이름을 적지 않고, ‘놀라운 사람’이라고만 불러요.'}],
  },
 },
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>펀치와 구리 틀</b> 펀치는 강철 막대 끝에 글자를 거꾸로 새긴 도장이에요. 이것을 무른 구리에 두드려 박은 것이 구리 틀(모형, 매트릭스)이에요. 펀치와 틀만 있으면 같은 활자를 얼마든지 다시 부을 수 있어서, 활자보다 더 귀하게 여겼어요.',
    '<b>270가지 글자</b> 손으로 쓴 책처럼 보이게, 붙여 쓰는 글자와 줄여 쓰는 글자까지 따로 만들었어요. 모건 도서관은 한 벌에 270가지쯤의 글자가 있었다고 해요. 글꼴은 가장 격식 있는 예배용 책의 글씨를 닮은 네모난 고딕 글자예요.',
    '<b>기름 먹</b> 손으로 쓸 때의 먹은 물로 개어서 쇠 활자에 잘 묻지 않았어요. 구텐베르크는 기름을 섞은 먹을 만들었고, 과학자들은 그 먹에서 남다른 금속 성분을 찾아냈어요.',
    '<b>나사 압착기</b> 구텐베르크의 인쇄기는 남아 있지 않아요. 포도주를 짜거나 종이를 누르던 나사 압착기를 고쳐 썼을 거라고 봐요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>몇 부를 찍었나</b> 피콜로미니는 158권이라는 말과 180권이라는 말을 함께 들었다고 적었어요. 니덤과 화이트는 종이 책이 적어도 120부, 양피지 책이 40부쯤이라고 보고, 다른 학자들은 160~185부쯤으로 셈해요.',
    '<b>어떻게 부었나</b> 펀치·구리 틀·손 주형으로 부었다는 설명이 오래 이어져 왔어요. 하지만 모건 도서관은 최근 연구가 구텐베르크의 활자를 정확히 어떻게 부었는지 다시 묻고 있다고 해요.',
    '<b>빌린 돈인가, 함께 넣은 돈인가</b> 1455년 공증 문서에서 푸스트는 빌려준 돈이라고 했고, 구텐베르크는 둘이 함께 벌인 일에 넣은 돈이 대부분이라고 맞섰어요.']},
  {'h': '직접 가 보기', 'checked': '2026년 11월 18일', 'p': [
    '독일 마인츠 구텐베르크 박물관은 새 건물을 짓는 동안, 2024년 11월 말부터 자연사 박물관 건물에서 임시 전시를 하고 있어요. 보물실에서는 구텐베르크 성경 두 권을 견주어 볼 수 있어요. 관람 시간은 가기 전에 누리집에서 확인하세요.',
    '사진의 레녹스 본은 뉴욕 공공도서관의 희귀본실이 가지고 있어요. 전시 여부는 가기 전에 확인하세요.'],
   'links': [{'t': '모건 도서관: 인쇄의 발명 — 활자·기름 먹·나사 압착기, 알려진 것과 아직 모르는 것', 'u': MOR, 'm': '영어'},
             {'t': '미국 의회도서관 블로그: 펀치에서 활자까지, 사진으로 보는 활자 만들기(2024)', 'u': LOC, 'm': '영어'},
             {'t': '마인츠 구텐베르크 박물관 — 임시 전시와 보물실', 'u': MZ, 'm': '영어·독일어'}]},
 ],
 'src': [
  {'l': '존 갠디(2025), 존 라일랜즈 도서관 블로그 — 피콜로미니의 1455년 3월 12일 편지(비너노이슈타트에서 카르바할 추기경에게): 프랑크푸르트의 ‘놀라운 사람’, 다 만든 성경은 못 보고 여러 권의 낱장 묶음만 봄, 아주 깨끗하고 바르며 틀린 데 없음, 안경 없이도, 158권·180권, 사 보겠다는 말과 먼 거리·다 정해진 살 사람(에릭 화이트 2025 번역)', 'u': RYL},
  {'l': '폴 니덤·에릭 화이트, 「Gutenberg & After」(프린스턴 대학 도서관 2019 전시 · 옥스퍼드 Cabinet) — 네모난 고딕 글꼴, 큰 종이 643장·두 권, 40줄에서 글자 높이를 줄여 42줄, 네 식자공, 열한 묶음 뒤 부수를 늘려 다시 찍음, 종이 120부 이상·양피지 40부쯤, 1455년 11월 6일 마인츠 공증 문서(푸스트의 소송, ‘책 만드는 일’, 종이·양피지·먹·이름 없는 장치, 구텐베르크의 반론), 지난가을 프랑크푸르트의 ‘놀라운 사람’', 'u': CAB},
  {'l': '패트릭 헤이스팅스(2024), 미국 의회도서관 블로그 「Just My Type」 — 강철 펀치에 거꾸로 새기고 둘레를 갈아 냄, 구리에 박은 틀은 바로 읽힘, 손 주형에 틀을 끼움, 주로 납인 쇠, 같은 활자를 여러 번, 펀치와 틀이 활자보다 귀함, 칸 나눈 상자', 'u': LOC},
  {'l': '모건 도서관 「The Invention of Printing」 — 활자를 붓고 한 자·한 줄씩 짜는 기술, 정확히 어떻게 부었는지 최근 연구가 물음, 270가지쯤의 글자, 기름 먹과 금속 성분, 나사 압착기(포도주·제지), 붉은 제목을 찍으려다 그만둠', 'u': MOR},
  {'l': '미하엘 폰 코타쇤베르크 엮음, 피콜로미니 연설 「Constantinopolitana clades」(1454년 10월 15일 프랑크푸르트) — 1454년의 세 제국 회의, 황제의 대변인 피콜로미니, 오스만에 맞설 십자군 의논', 'u': HAL},
  {'l': '웰컴 컬렉션: 요스트 암만 「Der Buchdrucker」(1568) — 창가에서 활자를 짜는 두 사람, 종이를 준비하며 먹을 바르는 두 인쇄공, 찍은 종이와 안 찍은 종이 더미', 'u': WEL1},
  {'l': '웰컴 컬렉션: 요스트 암만 「Der Schrifftgiesser」(1568) — 라틴·고딕·그리스 활자를 만든다는 글, 오른쪽의 쇠 녹이는 화로', 'u': WEL2},
  {'l': '마인츠시: 구텐베르크 박물관 — 2024년 10월 초 옛 건물을 닫고 11월 말 자연사 박물관 건물에서 임시 전시, 보물실의 구텐베르크 성경 두 권(2026년 11월 18일 확인)', 'u': MZ},
  {'l': '위키미디어 공용: 핀투리키오 벽화 사진 정보(피콜로미니가 프리드리히 3세에게 엘레오노르를 소개함, 시에나 대성당 피콜로미니 도서관), 레녹스 본 사진(뉴욕 공공도서관 희귀본실), 암만의 목판화', 'u': FRESCO},
  {'l': '위키백과 Gutenberg Bible — 길잡이로만(160~185부라는 셈)', 'u': WP},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '45% 45%', 'p1': '60% 50%', 's0': 1.2, 's1': 1.05, 'kicker': '1450년대 · 마인츠', 'title': '구텐베르크 성경',
   'lines': [{'t': '손으로 쓰지 않고, 쇠 글자로 찍은 성경.'}, {'t': '글자 하나가 책 한 쪽이 되기까지 따라가 봐요.'}],
   'kid': [{'t': '도장처럼 찍어서 만든 큰 책이야.'}, {'t': '어떻게 만들었는지 같이 볼까?'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '쇠로 만든 글자'},
  {'type': 'img', 'ch': 1, 'img': 'printer', 'fit': 'contain', 'p0': '50% 50%', 'p1': '50% 50%', 's0': 1.0, 's1': 1.06, 'cap': '인쇄소 — 요스트 암만, 1568년',
   'lines': [{'t': '구텐베르크의 인쇄소 그림은 남아 있지 않아요.'}, {'t': '100여 년 뒤의 목판화예요. 창가의 두 사람이 활자를 짜요.'}, {'t': '앞에서는 먹을 바르고, 종이를 얹어 찍어요.'}],
   'kid': [{'t': '옛날 인쇄소 그림이야.'}, {'t': '먹을 바르는 사람이 어디 있을까?', 'ask': True}]},
  {'type': 'img', 'ch': 1, 'img': 'founder', 'fit': 'contain', 'p0': '50% 50%', 'p1': '50% 50%', 's0': 1.0, 's1': 1.06, 'cap': '활자공 — 요스트 암만, 1568년',
   'lines': [{'t': '활자공은 녹인 쇠를 작은 틀에 부어 글자를 만들었어요.'}, {'t': '1455년의 한 문서는 이 일을 ‘책 만드는 일’이라고 불렀어요.'}],
   'kid': [{'t': '녹인 쇠를 작은 틀에 부어서 글자를 만들어.'}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '글자 하나가 한 쪽이 되기까지'},
  {'type': 'mod', 'mod': 'steps', 'ch': 2,
   'lines': [{'t': '강철 막대 끝에 글자를 거꾸로 새겨요.', 'act': 'step:1'},
             {'t': '구리에 꾹 박으면, 글자가 바로 읽히는 틀이 돼요.', 'act': 'step:2'},
             {'t': '틀에 녹인 쇠를 부으면, 다시 거꾸로 선 활자 하나.', 'act': 'step:3'},
             {'t': '같은 글자를 수백 개 부어 상자에 담아요.', 'act': 'step:4'},
             {'t': '한 자씩 집어 두 단 42줄을 짜요.', 'act': 'step:5'},
             {'t': '기름 먹을 바르고, 나사 손잡이를 당겨 꾹.', 'act': 'step:6', 'wait': 1800},
             {'t': '붉은 제목은 사람이 손으로 써넣었어요.', 'act': 'step:7', 'wait': 1500}],
   'kid': [{'t': '거꾸로 새기고, 꾹 박고, 쇠를 부어!', 'act': 'step:3'},
           {'t': '먹을 바르고 꾹 누르면 글자가 바로!', 'act': 'step:6'},
           {'t': '도장 글자는 왜 거꾸로 새길까?', 'act': 'step:7', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '40줄에서 42줄로'},
  {'type': 'img', 'ch': 3, 'img': 'card', 'fit': 'cover', 'p0': '62% 42%', 'p1': '66% 52%', 's0': 1.55, 's1': 1.3, 'cap': '뉴욕 공공도서관의 레녹스 본',
   'lines': [{'t': '처음엔 한 단에 40줄. 곧 글자를 조금 줄여 42줄로.'}, {'t': '네 사람이 성경을 넷으로 나눠 한꺼번에 짰다고 봐요.'}, {'t': '붉은 제목과 푸른 머리글자는 사람이 손으로.'}],
   'kid': [{'t': '빨간 글씨는 사람이 손으로 썼대.'}, {'t': '빨간 글씨를 찾아볼까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '안경 없이도'},
  {'type': 'img', 'ch': 4, 'img': 'fresco', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 58%', 's0': 1.15, 's1': 1.02, 'cap': '피콜로미니(가운데 주교관) — 핀투리키오, 1502~1508년 무렵',
   'lines': [{'t': '1454년 10월, 프랑크푸르트의 제국 회의.'}, {'t': '갓 찍은 성경 묶음을 본 피콜로미니가 이듬해 편지를 썼어요.'}],
   'kid': [{'t': '이 주교님이 찍은 성경을 보고 편지를 썼대.'}, {'t': '편지에 뭐라고 썼을까?', 'ask': True}]},
  {'type': 'quote', 'ch': 4, 'big': '추기경님께서도 애쓰지 않고, 안경 없이도 읽으실 수 있을 것입니다.',
   'lines': [{'t': '피콜로미니가 카르바할 추기경에게 쓴 편지 · 1455년 3월 12일', 'wait': 2600}],
   'kid': [{'t': '안경 없이도 읽을 만큼 깨끗한 글씨였대.', 'wait': 1800}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '축축한 종이 냄새, 기름 먹 냄새.'}, {'t': '나무 나사가 삐걱 돌아가요.'}, {'t': '종이를 들어 올리자, 까만 글자 두 단이 반짝여요.'}],
   'kid': [{'t': '끼익, 나무 나사가 돌아가.'}, {'t': '종이를 들어 올리면, 반짝!'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
