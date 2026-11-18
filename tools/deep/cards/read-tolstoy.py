# -*- coding: utf-8 -*-
"""깊은 카드: 사람은 무엇으로 사는가(read-tolstoy) · 중심 방식 = 만드는 차례
기준서 2판 · 틀 deep3-4 · 키트 3판 · 2026-11-18 창 3(묶음 16)이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 신사가 1년을 신어도 망가지지 않을 장화를 주문하는 순간 — 미하일이 신사 뒤쪽을 보다가 두 번째로 웃어요. 그리고 그날 오후, 장화 대신 지은 실내화 앞에서 세몬이 탄식할 때 문의 쇠고리가 울려요
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 미하일이 신사의 가죽으로 장화 대신 부드러운 실내화를 지은 차례(펴서 접기 → 둥글게 오리기 → 한 끝 실로 꿰매기 → 실내화 → 쇠고리가 울림), 7장
카드 크기: 한 장면 카드 — 자유롭게 쓸 그림은 앞면의 레핀 그림뿐이라, 장면 2개로 하고 실내화 단계 그림은 이 안내서가 그렸어요.
그림 원본: 앞면 그림(site/img/c). 단계 그림은 아래 SVG(이 안내서가 그림)."""
S = 'read-tolstoy/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

MX = 'https://www.marxists.org/archive/tolstoy/1885/what-men-live-by/part-1-chapter-'
CC = 'https://ccel.org/ccel/tolstoy/23_tales/23_tales.iv.i.html'
OL = 'https://openlibrary.org/books/OL18747536M/Twenty-three_tales'
WP = 'https://en.wikipedia.org/wiki/What_Men_Live_By'
RU = 'https://ru.wikisource.org/wiki/%D0%A7%D0%B5%D0%BC_%D0%BB%D1%8E%D0%B4%D0%B8_%D0%B6%D0%B8%D0%B2%D1%8B_(%D0%A2%D0%BE%D0%BB%D1%81%D1%82%D0%BE%D0%B9)'
NEED = '사람에게는 자기에게 무엇이 필요한지 아는 힘이 주어지지 않았어요.'
STEPS_SVG = r'''<svg viewBox="0 0 460 320" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="msW" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a2a1e"/><stop offset="1" stop-color="#2a1d14"/></linearGradient><linearGradient id="msT" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9a6b42"/><stop offset="1" stop-color="#7a5030"/></linearGradient><radialGradient id="msL" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#9a5a2c"/><stop offset="1" stop-color="#6e3e1c"/></radialGradient></defs><rect width="460" height="320" fill="url(#msW)"/><rect x="360" y="20" width="84" height="150" fill="#2a1c12" stroke="#5a3c24" stroke-width="3"/><path d="M372 32 H432 M372 76 H432 M372 120 H432" stroke="#4a3220" stroke-width="2"/><circle cx="378" cy="100" r="9" fill="none" stroke="#9a9690" stroke-width="3"/><path d="M0 150 L460 150 L460 320 L0 320 Z" fill="url(#msT)"/><path d="M0 178 C 120 174 300 183 460 176" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 192 C 120 188 300 197 460 190" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 206 C 120 202 300 211 460 204" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 220 C 120 216 300 225 460 218" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 234 C 120 230 300 239 460 232" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 248 C 120 244 300 253 460 246" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 262 C 120 258 300 267 460 260" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 276 C 120 272 300 281 460 274" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 290 C 120 286 300 295 460 288" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 304 C 120 300 300 309 460 302" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 318 C 120 314 300 323 460 316" stroke="#5a3a22" stroke-width="1" opacity=".35" fill="none"/><path d="M0 150 L460 150" stroke="#c49a6a" stroke-width="2"/><g data-s="1" data-off="5"><path d="M70 150 C 66 122 92 104 120 108 C 140 96 170 100 196 96 C 226 92 250 104 268 100 C 292 96 314 116 312 140 C 322 160 318 188 304 204 C 296 226 270 240 242 236 C 214 248 180 244 152 248 C 124 252 94 240 86 220 C 66 206 62 176 70 150 Z" fill="url(#msL)" stroke="#3e2210" stroke-width="2"/><path d="M188 104 C 186 150 190 200 186 246" fill="none" stroke="#3e2210" stroke-width="1.6" stroke-dasharray="6 5" opacity=".8"/><path d="M100 160 C 130 150 150 170 176 166" fill="none" stroke="#b97a46" stroke-width="1.4" opacity=".5"/></g><g data-s="2" data-off="5" fill="#2a1d14" stroke="#3e2210" stroke-width="1.4"><path transform="translate(132 176)" d="M0 -30 C 15 -30 22 -14 22 0 C 22 18 14 32 0 32 C -14 32 -22 18 -22 0 C -22 -14 -15 -30 0 -30 Z"/><path transform="translate(236 178)" d="M0 -30 C 15 -30 22 -14 22 0 C 22 18 14 32 0 32 C -14 32 -22 18 -22 0 C -22 -14 -15 -30 0 -30 Z"/><path transform="translate(140 222) scale(.8)" d="M-24 8 C -24 -18 -10 -30 0 -30 C 10 -30 24 -18 24 8 C 14 2 -14 2 -24 8 Z"/><path transform="translate(244 224) scale(.8)" d="M-24 8 C -24 -18 -10 -30 0 -30 C 10 -30 24 -18 24 8 C 14 2 -14 2 -24 8 Z"/></g><g data-s="2" data-off="4"><path d="M300 262 L356 240 L360 248 L306 270 Z" fill="#cfd3d6" stroke="#6a6e72" stroke-width="1.2"/><path d="M356 240 L392 226 C 398 224 402 232 396 236 L360 248 Z" fill="#5a3a22" stroke="#2a1a10" stroke-width="1.2"/></g><g data-s="2" data-off="4" fill="#a8743f" stroke="#4a2a14" stroke-width="1.6"><path transform="translate(60 268) rotate(-70) scale(.85)" d="M0 -30 C 15 -30 22 -14 22 0 C 22 18 14 32 0 32 C -14 32 -22 18 -22 0 C -22 -14 -15 -30 0 -30 Z"/><path transform="translate(128 282) rotate(-70) scale(.85)" d="M0 -30 C 15 -30 22 -14 22 0 C 22 18 14 32 0 32 C -14 32 -22 18 -22 0 C -22 -14 -15 -30 0 -30 Z"/><path transform="translate(204 282) scale(.9)" d="M-24 8 C -24 -18 -10 -30 0 -30 C 10 -30 24 -18 24 8 C 14 2 -14 2 -24 8 Z"/><path transform="translate(262 286) scale(.9)" d="M-24 8 C -24 -18 -10 -30 0 -30 C 10 -30 24 -18 24 8 C 14 2 -14 2 -24 8 Z"/></g><g data-s="3" data-off="4"><g fill="none" stroke="#efe6cf" stroke-width="1.4" stroke-dasharray="3 3"><path transform="translate(60 268) rotate(-70) scale(.85)" d="M0 -30 C 15 -30 22 -14 22 0 C 22 18 14 32 0 32 C -14 32 -22 18 -22 0 C -22 -14 -15 -30 0 -30 Z"/><path transform="translate(128 282) rotate(-70) scale(.85)" d="M0 -30 C 15 -30 22 -14 22 0 C 22 18 14 32 0 32 C -14 32 -22 18 -22 0 C -22 -14 -15 -30 0 -30 Z"/><path transform="translate(204 282) scale(.9)" d="M-20 6 C -20 -14 -8 -24 0 -24 C 8 -24 20 -14 20 6"/></g><path d="M222 258 L250 236" stroke="#d7dadc" stroke-width="2.2" stroke-linecap="round"/><circle cx="250" cy="236" r="2" fill="none" stroke="#d7dadc" stroke-width="1.2"/><path d="M250 236 C 268 222 286 232 280 246 C 274 260 296 266 312 254" fill="none" stroke="#efe6cf" stroke-width="1.6"/></g><g data-s="4" data-off="5"><g transform="translate(150 272) scale(1 1)"><path d="M-46 10 C -48 -6 -30 -16 -6 -16 C 22 -16 46 -10 50 4 C 52 16 40 24 18 24 C -6 24 -44 26 -46 10 Z" fill="#6e4424" stroke="#3a2210" stroke-width="1.6"/><path d="M-6 -14 C 10 -26 34 -22 46 -4 C 34 0 10 2 -6 -14 Z" fill="#8a5a34" stroke="#3a2210" stroke-width="1.4"/><path d="M-40 12 C -20 18 20 18 44 8" fill="none" stroke="#e8dcc0" stroke-width="1.2" stroke-dasharray="3 3"/><path d="M-4 -12 C 12 -22 32 -18 42 -4" fill="none" stroke="#e8dcc0" stroke-width="1.1" stroke-dasharray="3 3"/></g><g transform="translate(262 278) scale(-1 1)"><path d="M-46 10 C -48 -6 -30 -16 -6 -16 C 22 -16 46 -10 50 4 C 52 16 40 24 18 24 C -6 24 -44 26 -46 10 Z" fill="#6e4424" stroke="#3a2210" stroke-width="1.6"/><path d="M-6 -14 C 10 -26 34 -22 46 -4 C 34 0 10 2 -6 -14 Z" fill="#8a5a34" stroke="#3a2210" stroke-width="1.4"/><path d="M-40 12 C -20 18 20 18 44 8" fill="none" stroke="#e8dcc0" stroke-width="1.2" stroke-dasharray="3 3"/><path d="M-4 -12 C 12 -22 32 -18 42 -4" fill="none" stroke="#e8dcc0" stroke-width="1.1" stroke-dasharray="3 3"/></g></g><g data-s="5"><circle cx="378" cy="100" r="9" fill="none" stroke="#e8c27a" stroke-width="3.2"/><path d="M352 84 L340 76 M350 100 L336 100 M352 116 L340 124" stroke="#e8c27a" stroke-width="2.4" stroke-linecap="round"/><rect x="372" y="24" width="66" height="142" fill="rgba(236,240,246,.16)"/></g><g data-s="5"><g transform="translate(330 214) scale(.8)"><g transform="translate(0 0) scale(1 1)"><path d="M-46 10 C -48 -6 -30 -16 -6 -16 C 22 -16 46 -10 50 4 C 52 16 40 24 18 24 C -6 24 -44 26 -46 10 Z" fill="#6e4424" stroke="#3a2210" stroke-width="1.6"/><path d="M-6 -14 C 10 -26 34 -22 46 -4 C 34 0 10 2 -6 -14 Z" fill="#8a5a34" stroke="#3a2210" stroke-width="1.4"/><path d="M-40 12 C -20 18 20 18 44 8" fill="none" stroke="#e8dcc0" stroke-width="1.2" stroke-dasharray="3 3"/><path d="M-4 -12 C 12 -22 32 -18 42 -4" fill="none" stroke="#e8dcc0" stroke-width="1.1" stroke-dasharray="3 3"/></g></g><g transform="translate(400 222) scale(.8)"><g transform="translate(0 0) scale(-1 1)"><path d="M-46 10 C -48 -6 -30 -16 -6 -16 C 22 -16 46 -10 50 4 C 52 16 40 24 18 24 C -6 24 -44 26 -46 10 Z" fill="#6e4424" stroke="#3a2210" stroke-width="1.6"/><path d="M-6 -14 C 10 -26 34 -22 46 -4 C 34 0 10 2 -6 -14 Z" fill="#8a5a34" stroke="#3a2210" stroke-width="1.4"/><path d="M-40 12 C -20 18 20 18 44 8" fill="none" stroke="#e8dcc0" stroke-width="1.2" stroke-dasharray="3 3"/><path d="M-4 -12 C 12 -22 32 -18 42 -4" fill="none" stroke="#e8dcc0" stroke-width="1.1" stroke-dasharray="3 3"/></g></g><g transform="translate(372 270)"><ellipse cx="0" cy="0" rx="44" ry="16" fill="#9a5a2c" stroke="#3e2210" stroke-width="1.6"/><ellipse cx="40" cy="0" rx="8" ry="15" fill="#7a4420" stroke="#3e2210" stroke-width="1.4"/><path d="M34 -4 C 40 -8 44 -2 40 4" fill="none" stroke="#c4935e" stroke-width="1.4"/></g></g></svg>'''

CARD = {
 'id': 'read-tolstoy', 'mode': '만드는 차례',
 'pagetitle': '장화 대신 실내화',
 'brandsub': '깊은 카드 · 만드는 차례',
 'where': '<b>어느 겨울날</b><span>러시아 시골 · 구두장이 세몬의 오두막</span>',
 'lead': '어느 겨울날, 구두장이 세몬의 오두막에 커다란 신사가 비싼 가죽을 들고 와요. 1년을 신어도 망가지지 않을 장화를 지으라고요. 그 가죽으로 미하일이 무엇을 지었는지, 그날의 차례를 손으로 따라가 보세요.',
 'leadKid': '부자 신사 아저씨가 1년 동안 안 망가지는 장화를 만들어 달라고 했대. 그런데 미하일 아저씨는 다른 걸 만들었어! 하나씩 눌러서 따라가 보자.',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 2판). 장면은 톨스토이의 이야기를 모드 부부가 영어로 옮긴 글(1906)을 따랐고, 우리말은 이 안내서가 옮겼어요. 실내화 단계 그림은 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#6e4424;--accent-ink:#fff8f0;--soft:rgba(110,68,36,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#d9a878;--accent-ink:#1c1107;--soft:rgba(217,168,120,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#d9a878;--accent-ink:#1c1107;--soft:rgba(217,168,120,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '실내화', 'y': '1881', 'sub': '러시아 · 톨스토이'},
 'doneNote': '1년치를 마련하느라 바쁜 날, 신사의 장화와 미하일의 실내화를 떠올려 보세요.',
 'images': {},
 'scenes': [
  {'id': 'shop', 'label': '1년을 버틸 장화', 'kind': 'photo', 'img': 'card',
   'cap': '이 이야기를 위해 그린 연필 그림',
   'text': ['미하일의 솜씨가 소문나자, 세몬의 장화가 가장 꼼꼼하고 튼튼하다며 온 고장 사람들이 찾아왔어요. 그렇게 한 해가 지난 어느 겨울날, 방울을 단 세 필 말 마차가 오두막 앞에 섰어요.',
            '털외투를 입은 커다란 신사가 가죽 꾸러미를 내밀어요. 독일 가죽이고 20루블이나 했다고요. 1년을 신어도 모양이 망가지지 않고 실밥도 터지지 않을 장화를 지으라고 해요. 1년 안에 망가지면 감옥에 넣겠다고 으름장도 놓아요.'],
   'text2': ['세몬이 미하일을 쳐다보자 미하일이 고개를 끄덕여요. 맡으라고요. 세몬이 종잇조각을 이어 붙여 신사의 다리 치수를 재는 동안, 미하일은 신사 뒤쪽 구석을 바라보다가 갑자기 웃어요. 얼굴이 환해졌어요. 미하일이 이 집에 온 뒤 두 번째로 웃은 웃음이에요.',
             '신사는 나가다가 고개 숙이는 것을 잊고 문틀에 머리를 부딪혀요.'],
   'kid': '커다란 신사 아저씨가 와서 1년 동안 안 망가지는 장화를 만들라고 했대. 그런데 미하일 아저씨가 신사 뒤쪽을 보고 빙그레 웃었어!',
   'kidq': '미하일 아저씨는 신사 뒤에서 무엇을 보았을까?'},
  {'id': 'slippers', 'label': '그날 오후의 탁자', 'kind': 'mod', 'mod': 'steps',
   'text': ['신사가 떠나자 세몬은 미하일에게 일을 맡겨요. 가죽은 비싸고 신사는 성미가 급하니 실수하면 안 된다고요. 미하일은 차분히 일을 시작해요. 아래 단추를 눌러 그날 미하일의 손을 따라가 보세요.'],
   'quote': {'t': NEED, 'from': '미하일이 두 번째로 웃은 까닭을 들려주며 · 「사람은 무엇으로 사는가」 11장(모드 부부 영역) · 이 안내서가 옮김', 'u': MX + '11.html'},
   'text2': ['이야기 끝에 미하일은 그날 웃은 까닭을 들려줘요. 신사의 어깨 뒤에 죽음의 천사가 서 있었대요. 그 사람은 1년을 준비하면서, 저녁이 오기 전에 죽으리라는 것을 몰랐다고요. 그리고 하나님이 배우라고 하신 두 번째 말씀, 사람에게 무엇이 주어지지 않았는지를 깨달았다고요.'],
   'kid': '장화를 만들랬는데, 미하일 아저씨는 부드러운 실내화를 만들었어! 그런데 바로 그때 누가 문을 탕탕 두드렸대.',
   'kidq': '문을 두드린 사람은 무슨 말을 전했을까?'},
 ],
 'imagine': {'t': '좁은 오두막에 가죽 냄새가 배어 있어요. 썰매 방울 소리가 멀어지고, 칼이 가죽을 스치는 소리만 사각사각 들려요. 점심때가 되도록 미하일의 바늘은 쉬지 않아요. 그때 문에 달린 쇠고리가 탕탕 울려요.',
             'kid': '눈을 감아 봐. 사각사각 가죽 자르는 소리, 쓱쓱 바느질하는 소리. 그러다 탕탕! 누가 왔어.'},
 'lines': ['1년을 버틸 장화 대신, 부드러운 실내화 한 켤레.', '두 끝이 아니라 한 끝으로.', NEED],
 'linesKid': ['장화 대신 실내화!', '탕탕, 누가 문을 두드려.'],
 'close': {'form': '기록 한 마디',
           'from': '미하일이 두 번째로 웃은 까닭을 말하며 남긴 한 줄 “It is not given to man to know his own needs.”(11장, 모드 부부 영역) — 1년을 버틸 장화를 맞추던 신사와 그날 오후의 실내화',
           'ask': '세몬이 “나를 망쳤구나!” 하던 그때, 하인은 아직 문을 두드리기 전이었어요. 내가 그 오두막에 있었다면 미하일에게 무엇을 물었을까요?',
           'askKid': '장화 대신 실내화를 본 세몬 아저씨는 깜짝 놀랐어. 너라면 미하일 아저씨한테 뭐라고 물어봤을까?'},
 'goals': {
  's4': {'t': '실내화 끝까지', 'p': '그날 미하일의 다섯 단계를 끝까지 따라가면 카드에 금박이 입혀져요.', 'how': '‘가죽 펴기’부터 다섯 단계를 끝까지 해 보세요', 'done': '미하일의 실내화를 끝까지 지어 봤어요',
         'ways': [{'id': 'steps', 't': '다섯 단계를 끝까지 해 보기'}]},
  's5': {'t': '아이와 함께', 'p': '아이와 함께 ‘영화처럼 보기’를 끝까지 보면 카드가 채색돼요.', 'how': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'done': '아이와 함께 끝까지 봤어요',
         'ways': [{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'steps': {
   'svg': STEPS_SVG,
   'alt': '이 안내서가 그린 구두장이의 탁자. 단계마다 반으로 접은 가죽, 둥글게 오린 조각과 칼, 한 가닥 실과 바늘, 부드러운 실내화 한 켤레가 나타나고, 마지막에는 문의 쇠고리가 울리며 실내화와 말아 둔 자투리 가죽이 문 앞으로 가요.',
   'cap': '이 안내서가 그린 미하일의 탁자 · 「사람은 무엇으로 사는가」 7장(모드 부부 영역)의 차례를 바탕으로 · 가죽 조각의 모양은 이야기에 적힌 ‘둥글게’를 따라 짐작해 그렸어요',
   'intro': '단추를 누를 때마다 그날 오후 미하일의 탁자가 한 단계씩 바뀌어요.',
   'hint': '아래 ‘가죽 펴기’부터 눌러 보세요.',
   'marksLabel': '미하일의 탁자 위',
   'marks': [{'t': '20루블짜리 가죽', 'c': '#7a4a24', 's': 1}, {'t': '둥근 조각', 'c': '#a8743f', 's': 2},
             {'t': '한 가닥 실', 'c': '#efe6cf', 's': 3}, {'t': '부드러운 실내화', 'c': '#5a3418', 's': 4}, {'t': '말아 든 자투리', 'c': '#c4935e', 's': 5}],
   'steps': [{'do': '가죽 펴기', 't': '반으로 접은 가죽', 'p': '미하일은 신사가 두고 간 가죽을 탁자에 펴고, 반으로 접어요. 독일 가죽이고 20루블이나 했다던 바로 그 가죽이에요.'},
             {'do': '칼로 오리기', 't': '장화가 아니라 둥글게', 'p': '칼을 들고 오리기 시작해요. 그런데 장화 모양이 아니라 둥글게 오려요. 지켜보던 마트료나는 놀랐지만, 신사의 장화는 미하일이 더 잘 알겠거니 하고 끼어들지 않아요.'},
             {'do': '꿰매기', 't': '두 끝이 아니라 한 끝으로', 'p': '장화를 꿰맬 때처럼 실의 두 끝을 쓰지 않고, 부드러운 실내화를 지을 때처럼 한 끝으로만 꿰매요. 미하일은 점심때까지 쉬지 않고 꿰매요.'},
             {'do': '다 짓기', 't': '부드러운 실내화 한 켤레', 'p': '점심을 먹으려고 일어난 세몬이 보니, 신사의 가죽이 실내화가 되어 있어요. “나를 망쳤구나! 신사는 목 긴 장화를 주문했는데, 이게 뭔가!”'},
             {'do': '문 열기', 't': '문의 쇠고리가 울려요', 'p': '그 순간 문에 달린 쇠고리가 탕탕 울려요. 신사의 하인이에요. 주인이 마차 안에서 숨을 거두어 장화는 필요 없으니, 주검에 신길 부드러운 실내화를 서둘러 지어 달라는 마님의 말을 전해요. 미하일은 남은 가죽을 둘둘 말고, 실내화를 탁탁 털어 앞치마로 닦아 건네요.'}],
   'done': '탁자가 비었어요. 1년을 버틸 장화 대신, 그날 저녁에 필요한 실내화가 문을 나섰어요.',
 }},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>세 가지 배움</b> 이야기 속 하나님은 천사 미하일에게 세 가지를 배우라고 해요. 사람 안에 무엇이 있는지, 사람에게 무엇이 주어지지 않았는지, 사람은 무엇으로 사는지. 신사의 장화는 그 가운데 두 번째 물음의 답이 돼요.',
    '<b>세 번의 웃음</b> 첫 웃음은 처음에 화를 내던 마트료나가 남편의 말에 마음을 풀고 저녁을 내줄 때, 두 번째는 신사가 장화를 맞출 때, 세 번째는 미하일이 이 집에서 여섯 해째 살던 해에 찾아온 한 여인 때문이에요. 여인은 자기가 낳지도 않았고 친척도 아닌 쌍둥이 두 여자아이를 데려다 키우며, 그 아이들의 봄 신발을 맞추러 왔어요. 한 아이는 왼쪽 다리를 절었어요.',
    '<b>요한일서의 말씀</b> 톨스토이는 러시아어 원문 맨 앞에 요한일서의 구절 여럿을 적어 두었어요. 형제를 사랑하기에 죽음에서 생명으로 옮겨 간 줄 안다는 말씀(' + bl('1JN.3', '요한일서 3장 14절') + ')으로 시작하고, 하나님은 사랑이시니 사랑 안에 사는 사람은 하나님 안에 산다는 말씀(' + bl('1JN.4', '요한일서 4장 16절') + ')도 들어 있어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>쓴 해</b> 모드 부부가 엮은 영어 선집 『스물세 이야기』는 이 이야기를 1881년 작품으로 적어요. 몇몇 영어 자료는 1885년으로 적어요.',
    '<b>제목</b> 영어 제목은 흔히 “What Men Live By”이지만, “What People Live By”로 옮긴 책도 있어요.']},
  {'h': '원문 읽기', 'checked': '2026년 11월 18일', 'p': [
    '이 이야기는 러시아어 원문과 모드 부부의 영어 번역(1906) 모두 저작권이 끝나 누구나 읽을 수 있어요.'],
   'links': [{'t': '기독교 고전 전자 도서관(CCEL): 모드 부부의 영어 번역 「What Men Live By」(『스물세 이야기』 4번째 이야기)', 'u': CC, 'm': '영어'},
             {'t': '위키문헌: 러시아어 원문 「Чем люди живы」(요한일서 구절로 시작해요)', 'u': RU, 'm': '러시아어'}]},
 ],
 'src': [
  {'l': '톨스토이 아카이브(마르크스주의자 인터넷 아카이브, 프로젝트 구텐베르크의 모드 부부 번역) 6장 — 솜씨 소문, 한 해, 방울 단 세 필 말 마차, 털외투, 독일 가죽 20루블, 1년 장화, 감옥 으름장, 고개 끄덕임, 종잇조각 치수, 구석을 보다 웃음, 문틀', 'u': MX + '6.html'},
  {'l': '같은 아카이브 7장 — 실수하면 안 된다, 펴서 반으로 접어 오림, 둥글게, 마트료나, 한 끝 실, 점심때까지, “나를 망쳤구나”, 쇠고리, 하인의 말(마차 안에서 숨을 거둠, 주검에 신길 실내화), 자투리를 말아 건넴', 'u': MX + '7.html'},
  {'l': '같은 아카이브 8장 — 여섯 해째, 두 여자아이와 왼쪽 다리, 봄 신발, 데려다 키움', 'u': MX + '8.html'},
  {'l': '같은 아카이브 11장 — 첫 웃음(마트료나의 마음), 두 번째 웃음(죽음의 천사, 1년을 준비하며 저녁을 모름, 두 번째 말씀, “It is not given to man to know his own needs.”)', 'u': MX + '11.html'},
  {'l': '기독교 고전 전자 도서관(CCEL): 『스물세 이야기』(L. and A. Maude 옮김) 4. What Men Live By (1881)', 'u': CC},
  {'l': '오픈 라이브러리: 『Twenty-three tales』 — 옥스퍼드 대학 출판부 월즈 클래식스 72번, 1906년 12월, 머리말 1906년 2월 1일', 'u': OL},
  {'l': '위키백과(영어): What Men Live By — 1885년으로 적음, “What People Live By”로도 옮김', 'u': WP},
  {'l': '위키문헌(러시아어): 「Чем люди живы」 — 맨 앞의 요한일서 구절(3장 14절 · 17절 · 18절 · 4장 7절 · 8절 · 12절 · 16절 …)', 'u': RU},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 40%', 'p1': '55% 50%', 's0': 1.2, 's1': 1.05, 'kicker': '어느 겨울날 · 러시아 시골', 'title': '사람은 무엇으로 사는가',
   'lines': [{'t': '구두장이 세몬의 오두막에는 말수 적은 일꾼 미하일이 살아요.'}, {'t': '어느 겨울날, 커다란 신사가 비싼 가죽을 들고 찾아와요.'}],
   'kid': [{'t': '구두장이 아저씨네 집이야.'}, {'t': '부자 신사 아저씨가 찾아왔어!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '1년을 버틸 장화'},
  {'type': 'img', 'ch': 1, 'img': 'card', 'fit': 'contain', 'p0': '50% 50%', 'p1': '50% 40%', 's0': 1.0, 's1': 1.1, 'cap': '일리야 레핀의 연필 그림, 1881년',
   'lines': [{'t': '1년을 신어도 망가지지 않을 장화를 지으라. 못 하면 감옥이다.', 'q': True, 'from': '신사'},
             {'t': '치수를 재는 동안, 미하일은 신사 뒤쪽을 보다가 갑자기 웃어요.'},
             {'t': '이 집에 온 뒤 두 번째 웃음이에요.'}],
   'kid': [{'t': '1년 동안 안 망가지는 장화를 만들어라!'}, {'t': '미하일 아저씨가 빙그레 웃었어.'}, {'t': '왜 웃었을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '그날 오후의 탁자'},
  {'type': 'mod', 'mod': 'steps', 'ch': 2,
   'lines': [{'t': '미하일은 가죽을 펴고 반으로 접어요.', 'act': 'next'},
             {'t': '그런데 장화 모양이 아니라 둥글게 오려요.', 'act': 'next'},
             {'t': '실의 두 끝이 아니라 한 끝으로 꿰매요. 실내화를 지을 때처럼요.', 'act': 'next'},
             {'t': '“나를 망쳤구나! 신사는 장화를 주문했는데!”', 'act': 'next', 'q': True, 'from': '세몬'},
             {'t': '그때 문의 쇠고리가 울려요. 신사가 마차 안에서 숨을 거두었대요.', 'act': 'next', 'wait': 1500},
             {'t': '장화 대신, 부드러운 실내화가 필요하다고요.'}],
   'kid': [{'t': '가죽을 쫙 펴고,', 'act': 'next'}, {'t': '동글동글 오리고,', 'act': 'next'}, {'t': '쓱쓱 꿰매서,', 'act': 'next'},
           {'t': '실내화 완성! 세몬 아저씨는 깜짝 놀랐어.', 'act': 'next'}, {'t': '탕탕! 신사 아저씨가 마차 안에서 세상을 떠났대.', 'act': 'next', 'wait': 1500},
           {'t': '미하일 아저씨는 어떻게 미리 알았을까?', 'ask': True}]},
  {'type': 'imagine', 'ch': 3,
   'lines': [{'t': '가죽 냄새, 사각사각 칼 소리.'}, {'t': '점심때가 되도록 쉬지 않는 바늘.'}, {'t': '그때, 탕탕. 문의 쇠고리가 울려요.'}],
   'kid': [{'t': '사각사각, 쓱쓱.'}, {'t': '그러다 탕탕!'}]},
  {'type': 'quote', 'ch': 3, 'big': NEED,
   'lines': [{'t': '미하일이 두 번째로 웃은 까닭 · 11장', 'wait': 2600}],
   'kid': [{'t': '사람은 자기한테 정말 필요한 게 뭔지 다 알지는 못한대.', 'wait': 2600}]},
  {'type': 'reward', 'ch': 3},
 ],
}
