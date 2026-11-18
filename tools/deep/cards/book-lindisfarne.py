# -*- coding: utf-8 -*-
"""깊은 카드: 린디스판 복음서(book-lindisfarne) · 중심 방식 = 놓아 보기
기준서 1판 · 틀 deep3-3 · 키트 2판(보탬) · 2026-11-18 27번 묶음 창이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 970년 무렵 체스터르스트리트, 사제 앨드레드가 250년 된 복음서의
     맨 끝 쪽(259r) 빈자리에 ‘이 책을 만든 네 사람’과 그들이 한 일을 적어 넣는 순간.
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 앨드레드의 맺음말에 적힌 차례 그대로
     쓰기(에드프리스) → 묶고 덮기(에셀왈드) → 금·보석으로 꾸미기(빌프리스) → 줄 위에 영어 뜻 달기(앨드레드).
카드 크기: 큰 카드(장면 5개) — 책의 쪽 사진(퍼블릭 도메인)과 섬·교회 사진, 맺음말 기록이 넉넉해요.
무대 그림은 이 안내서가 그렸어요(아래 stage_svg). 양탄자 페이지를 베끼지 않고 십자가와 점무늬만 단순하게 그렸어요.
그림 원본(src)은 deep_src/book-lindisfarne/ (저장소 밖). 받는 법: commons_get.py"""
import random
S = 'book-lindisfarne/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

BLCAT = 'https://searcharchives.bl.uk/catalog/040-001102725'
COLO = 'https://artofthemiddleages.com/s/main/item/4425'
SMART = 'https://smarthistory.org/the-lindisfarne-gospels/'
SFU = 'https://journals.lib.sfu.ca/index.php/asmmf/article/download/5513/4594/19960'


def stage_svg():
    """이 안내서가 그린 무대: 어두운 방, 책상 위 펼친 양피지. 놓을 때마다 글·표지·보석·뜻풀이가 더해져요."""
    R = random.Random(970)
    blk = ''; gl = ''
    for c0, c1 in [(414, 468), (476, 530)]:
        y = 216
        for i in range(11):
            x0 = c0 + (12 if (c0 == 414 and i < 2) else 0)
            x1 = c1 - (R.uniform(6, 18) if i in (4, 10) else 0)
            blk += f'<line x1="{x0:.0f}" y1="{y}" x2="{x1:.0f}" y2="{y}"/>'
            gx = x0
            while gx < x1 - 4:
                w = R.uniform(4, 10); e = min(gx + w, x1)
                gl += f'<line x1="{gx:.1f}" y1="{y - 4.3:.1f}" x2="{e:.1f}" y2="{y - 4.3:.1f}"/>'
                gx = e + R.uniform(2.6, 4.8)
            y += 10
    dots = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r=".9"/>' for x, y in
                   [(R.uniform(274, 386), R.uniform(212, 322)) for _ in range(170)])
    gems = [(300, 192), (350, 192), (450, 192), (500, 192), (300, 338), (350, 338), (450, 338), (500, 338),
            (252, 236), (252, 294), (548, 236), (548, 294)]
    cols = ['#c0392b', '#2c5aa0', '#2e8b57']
    lt = '<g class="lt" style="transition-delay:0s"><rect x="251.5" y="191.5" width="297" height="147" rx="3" fill="none" stroke="#d9ad46" stroke-width="1.6"/></g>'
    for k, (x, y) in enumerate([(252, 192), (548, 192), (252, 338), (548, 338)]):
        lt += (f'<g class="lt" style="transition-delay:{0.06 + k * 0.06:.2f}s"><circle cx="{x}" cy="{y}" r="13" fill="url(#__U__gg)"/>'
               f'<rect x="{x - 6}" y="{y - 6}" width="12" height="12" transform="rotate(45 {x} {y})" fill="#d9ad46" stroke="#8a6420" stroke-width=".8"/>'
               f'<circle cx="{x}" cy="{y}" r="2.4" fill="#fff3c4"/></g>')
    for k, (x, y) in enumerate(gems):
        c = cols[k % len(cols)]
        lt += (f'<g class="lt" style="transition-delay:{0.3 + k * 0.06:.2f}s"><circle cx="{x}" cy="{y}" r="11" fill="url(#__U__gg)"/>'
               f'<circle cx="{x}" cy="{y}" r="4.6" fill="#d9ad46"/><circle cx="{x}" cy="{y}" r="3.4" fill="{c}"/>'
               f'<circle cx="{x - 1.1}" cy="{y - 1.2}" r="1" fill="#fff" opacity=".85"/></g>')
    win = lambda x: (f'<path d="M{x} 196 L{x} 104 Q{x} 66 {x + 35} 66 Q{x + 70} 66 {x + 70} 104 L{x + 70} 196Z" fill="#2a2420" stroke="#4a3e33" stroke-width="5"/>'
                     f'<path d="M{x + 8} 190 L{x + 8} 106 Q{x + 8} 76 {x + 35} 76 Q{x + 62} 76 {x + 62} 106 L{x + 62} 190Z" fill="url(#__U__sky)"/>'
                     f'<path class="sky2" d="M{x + 8} 190 L{x + 8} 106 Q{x + 8} 76 {x + 35} 76 Q{x + 62} 76 {x + 62} 106 L{x + 62} 190Z" fill="url(#__U__sky2)"/>'
                     f'<line x1="{x + 35}" y1="76" x2="{x + 35}" y2="190" stroke="#2a2420" stroke-width="3"/>')
    return f'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="어두운 방, 책상 위에 아직 글이 없는 양피지가 펼쳐져 있다. 놓을 때마다 글과 그림, 가죽 표지, 금과 보석, 줄 위의 작은 뜻풀이가 하나씩 더해진다. 이 안내서가 그린 무대."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#110e10"/><stop offset="1" stop-color="#231a14"/></linearGradient>
<linearGradient id="__U__sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#151c2c"/><stop offset="1" stop-color="#2b3550"/></linearGradient>
<linearGradient id="__U__sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8fa7c4"/><stop offset="1" stop-color="#e8cf9c"/></linearGradient>
<linearGradient id="__U__pg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d9c7a2"/><stop offset=".85" stop-color="#ead9b6"/><stop offset="1" stop-color="#c2ad86"/></linearGradient>
<linearGradient id="__U__pg2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c2ad86"/><stop offset=".15" stop-color="#ead9b6"/><stop offset="1" stop-color="#d9c7a2"/></linearGradient>
<linearGradient id="__U__wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a3a22"/><stop offset="1" stop-color="#3a2414"/></linearGradient>
<radialGradient id="__U__glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd896" stop-opacity=".85"/><stop offset=".55" stop-color="#e09a4a" stop-opacity=".35"/><stop offset="1" stop-color="#e09a4a" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__gg"><stop offset="0" stop-color="#fff0bf" stop-opacity=".9"/><stop offset=".5" stop-color="#f2c060" stop-opacity=".35"/><stop offset="1" stop-color="#f2c060" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".5" cy=".6" r=".75"><stop offset="0" stop-color="#fff2cf" stop-opacity=".62"/><stop offset=".6" stop-color="#f4c47c" stop-opacity=".24"/><stop offset="1" stop-color="#f4c47c" stop-opacity="0"/></radialGradient></defs>
<rect width="800" height="450" fill="url(#__U__wall)"/>
<g opacity=".35" stroke="#3a2e26" stroke-width="1">{''.join(f'<line x1="0" y1="{y}" x2="800" y2="{y}"/>' for y in range(40, 330, 36))}</g>
{win(122)}{win(608)}
<ellipse class="glow" cx="400" cy="268" rx="230" ry="130" fill="url(#__U__glow)" opacity=".14"/>
<path d="M176 342 L624 342 L660 376 L140 376Z" fill="url(#__U__wood)" stroke="#6e4a2c" stroke-width="1.2"/>
<ellipse cx="400" cy="346" rx="170" ry="7" fill="#1a0f08" opacity=".55"/>
<rect x="140" y="376" width="520" height="12" fill="#2c1b0f"/>
<path d="M172 388 L166 450 M628 388 L634 450" stroke="#2c1b0f" stroke-width="14"/>
<g class="obj" data-o="bind"><rect x="248" y="188" width="304" height="154" rx="5" fill="#5b3420" stroke="#8a5530" stroke-width="1.4"/>
<rect x="396" y="186" width="8" height="158" fill="#3a2010"/>{''.join(f'<line x1="397" y1="{y}" x2="403" y2="{y}" stroke="#c9a77a" stroke-width="1.6"/>' for y in (206, 232, 258, 284, 310, 330))}</g>
<path d="M262 200 Q330 194 398 202 L398 334 Q330 328 262 334Z" fill="url(#__U__pg)"/>
<path d="M402 202 Q470 194 538 200 L538 334 Q470 328 402 334Z" fill="url(#__U__pg2)"/>
<line x1="400" y1="202" x2="400" y2="334" stroke="#9c8661" stroke-width="1.2"/>
<g class="obj" data-o="write">
<g fill="#b8402d" opacity=".8">{dots}</g>
<rect x="272" y="210" width="116" height="114" fill="none" stroke="#b8402d" stroke-width="1.6"/>
<path d="M322 216 h16 v32 h32 v16 h-32 v52 h-16 v-52 h-32 v-16 h32Z" fill="#d9ad46" stroke="#5a3a1a" stroke-width="1.4"/>
<path d="M326 222 h8 v30 h30 v8 h-30 v50 h-8 v-50 h-30 v-8 h30Z" fill="#2f6b4f"/>
<g fill="none" stroke="#8a2a1d" stroke-width="1.3">{''.join(f'<circle cx="{x}" cy="{y}" r="5"/>' for x, y in [(282, 220), (378, 220), (282, 314), (378, 314)])}</g>
<g stroke="#2a1f17" stroke-width="1.7" stroke-linecap="round">{blk}</g>
<path d="M414 210 h9 v9 h-9Z" fill="#b8402d"/><path d="M416 212 q3 -2 5 0 q-1 4 -5 5Z" fill="#d9ad46"/>
</g>
{lt}
<g class="obj" data-o="gloss"><g stroke="#a3552e" stroke-width="1.05" stroke-linecap="round">{gl}</g></g>
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''


ITEMS = [
 {'id': 'write', 't': '쓰기', 'la': 'Eadfrith · 에드프리스',
  'say': '린디스판 교회의 주교 에드프리스가 처음에 이 책을 썼어요. 하나님과 성 쿠스버트, 그리고 섬의 모든 성인을 위해서요.'},
 {'id': 'bind', 't': '묶고 덮기', 'la': 'Æthelwald · 에셀왈드',
  'say': '린디스판 섬사람들의 주교 에셀왈드가 바깥을 묶고 덮었어요. 앨드레드는 ‘그가 잘 아는 솜씨대로’라고 적었어요.'},
 {'id': 'lights', 't': '꾸미기', 'la': 'Billfrith · 빌프리스',
  'say': '은둔 수도자 빌프리스가 바깥 장식을 두드려 만들고, 금과 보석, 금을 입힌 은으로 꾸몄어요.'},
 {'id': 'gloss', 't': '뜻 달기', 'la': 'Aldred · 앨드레드',
  'say': '그리고 앨드레드가 하나님과 성 쿠스버트의 도움으로, 라틴어 줄 위에 영어로 뜻을 적었어요.'},
]

CARD = {
 'id': 'book-lindisfarne', 'mode': '놓아 보기',
 'pagetitle': '린디스판 복음서 · 책 끝의 네 사람',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>715년 무렵 → 970년 무렵</b><span>잉글랜드 린디스판 섬 · 체스터르스트리트</span>',
 'lead': '1,300년 전 잉글랜드 북쪽의 섬 린디스판에서 네 복음서를 담은 책이 만들어졌어요. 250년쯤 뒤 사제 앨드레드는 이 책 맨 끝에 ‘이 책을 만든 네 사람’을 적어 두었어요. 앨드레드가 적은 차례대로 책 한 권을 완성해 보세요.',
 'leadKid': '아주 옛날 섬마을 수도원에서 그림이 가득한 성경책을 만들었대. 나중에 한 수도사가 책 끝에 “이 책은 네 사람이 만들었어요” 하고 적어 두었어. 우리도 그 차례대로 만들어 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 6분',
 'draft': '검수 전 시안이에요(기준서 1판). 책을 만든 사람들의 이야기는 앨드레드가 10세기에 책 끝에 적은 맺음말(영국도서관 목록의 영어 번역)을 따랐어요. 무대 그림은 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에서만 해요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#2f6b4f;--accent-ink:#f6fbf7;--soft:rgba(47,107,79,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#8fc9a8;--accent-ink:#0c1610;--soft:rgba(143,201,168,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#8fc9a8;--accent-ink:#0c1610;--soft:rgba(143,201,168,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '맺음말', 'y': '970', 'sub': '체스터르스트리트'},
 'doneNote': '다음에 책을 펼치면, 맨 끝에 적힌 이름들도 한 번 읽어 보세요.',
 'images': {
  'causeway': {'src': S + 'Holy_Island_Lindisfarne_Causeway_-_geograph.org.uk_-_6670221.jpg', 'cap': '린디스판 섬으로 이어지는 둑길. 밀물 때는 물에 잠겨요',
               'cr': '사진: Lewis Clarke · CC BY-SA 2.0 · 위키미디어 공용(geograph)', 'u': 'https://commons.wikimedia.org/wiki/File:Holy_Island_,_Lindisfarne_Causeway_-_geograph.org.uk_-_6670221.jpg',
               'alt': '구름 낀 하늘 아래 아스팔트 길이 곧게 뻗어 있다. 길 오른쪽으로 물이 고인 갯벌과 나무 기둥들, 풀 덮인 모래 언덕이 보인다.'},
  'matthew': {'src': S + 'St._Matthew_-_Lindisfarne_Gospels_710-721_f.25v_-_BL_Cotton_MS_Nero_D_IV.jpg', 'cap': '린디스판 복음서 25v쪽, 글을 쓰는 마태',
              'cr': '퍼블릭 도메인 · 위키미디어 공용(영국도서관 Cotton MS Nero D IV)', 'u': 'https://commons.wikimedia.org/wiki/File:St._Matthew_-_Lindisfarne_Gospels_(710-721),_f.25v_-_BL_Cotton_MS_Nero_D_IV.jpg',
              'alt': '둥근 금빛 후광을 두른 마태가 나무 의자에 앉아 무릎 위의 책에 글을 쓴다. 그 위에서 날개 달린 사람이 나팔을 불고, 오른쪽 붉은 휘장 뒤에서 한 사람이 책을 들고 내다본다.'},
  'church': {'src': S + 'St_Mary_and_St_Cuthbert_s_Church_Chester-le-Street_County_Durham.jpg', 'cap': '체스터르스트리트의 성 마리아·성 쿠스버트 교회. 공동체가 처음 세운 나무 교회 자리에 뒷날 돌로 지었어요',
             'cr': '사진: JohnBlackburne · CC BY-SA 3.0 · 위키미디어 공용', 'u': "https://commons.wikimedia.org/wiki/File:St_Mary_and_St_Cuthbert%27s_Church,_Chester-le-Street,_County_Durham.jpg",
             'alt': '눈 쌓인 날, 파란 하늘과 흰 구름 아래 누런 돌로 지은 교회가 서 있다. 시계가 달린 탑 위로 높고 뾰족한 첨탑이 솟아 있다.'},
  'chirho': {'src': S + 'LindisfarneChiRiho.jpg', 'cap': '린디스판 복음서 29r쪽, 마태복음 1장 18절이 시작되는 ‘키로’ 쪽',
             'cr': '퍼블릭 도메인 · 위키미디어 공용(영국도서관 Cotton MS Nero D IV)', 'u': 'https://commons.wikimedia.org/wiki/File:LindisfarneChiRiho.jpg',
             'alt': '커다란 X와 P 모양 글자가 매듭과 소용돌이 무늬로 쪽의 위쪽을 가득 채웠고, 아래에 굵은 라틴어 글줄 세 줄이 이어진다. 큰 글자들 위와 오른쪽 여백에 갈색의 작은 글씨가 적혀 있다.'},
  'luke': {'src': S + 'Lindisfarne_Gospels_folio_139r.jpg', 'cap': '139r쪽, 누가복음 첫 쪽',
           'cr': '퍼블릭 도메인 · 위키미디어 공용(영국도서관 Cotton MS Nero D IV)', 'u': 'https://commons.wikimedia.org/wiki/File:Lindisfarne_Gospels_folio_139r.jpg',
           'alt': '왼쪽에 매듭 무늬로 채운 커다란 Q 글자가 서 있고, 오른쪽에 붉은 점으로 테를 두른 라틴어 글자들이 줄지어 있다. 글줄 사이사이에 갈색의 작은 글씨가 적혀 있다.'},
  'priory': {'src': S + 'Lindisfarne_Priory_2016-05-29.jpg', 'cap': '린디스판 수도원 터. 지금 남은 붉은 돌 폐허는 뒷날(11~12세기) 다시 지은 수도원이에요',
             'cr': '사진: August Schwerdfeger · CC BY 4.0 · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:Lindisfarne_Priory_2016-05-29.jpg',
             'alt': '붉은 사암으로 지은 아치와 벽이 반쯤 무너진 채 서 있고, 가운데로 높은 반원 아치 하나가 흐린 하늘을 가로지른다. 바닥은 푸른 잔디다.'},
 },
 'scenes': [
  {'id': 'island', 'label': '물이 빠지면 열리는 섬', 'kind': 'photo', 'img': 'causeway',
   'text': ['잉글랜드 북동쪽 바닷가의 린디스판은 하루에 두 번 밀물에 길이 끊기는 섬이에요. 바닷물이 빠졌을 때만 둑길로 건널 수 있어요.',
            '635년, 스코틀랜드 아이오나 섬에서 온 수도사 에이단이 이곳에 수도원을 세웠어요. 이 수도원의 주교였던 쿠스버트가 687년에 세상을 떠나자, 사람들은 그를 성인으로 기렸어요.'],
   'kid': '물이 빠지면 길이 열리는 섬이래! 하루에 두 번 길이 물에 잠겨.',
   'kidq': '이 섬에 가려면 언제 출발해야 할까?'},
  {'id': 'scribe', 'label': '한 사람이 쓰고 그린 책', 'kind': 'photo', 'img': 'matthew',
   'text': ['715년 무렵, 이 섬에서 네 복음서를 담은 큰 책이 만들어졌어요. 학자들은 한 사람이 이 책을 다 쓰고 그렸다고 봐요. 아마 698년부터 721년까지 린디스판의 주교였던 에드프리스예요.',
            '양피지 259장, 한 장의 크기는 세로 36.5cm, 가로 27.5cm쯤이에요. 마태복음 앞의 그림에서도 마태가 무릎 위 책에 글을 쓰고 있어요.'],
   'text2': ['책 끝의 기록은 이 책이 ‘하나님과 성 쿠스버트를 위해’ 만들어졌다고 적었어요.'],
   'kid': '한 사람이 이 큰 책을 다 쓰고 그렸대. 그림 속 마태 아저씨도 글을 쓰고 있어.',
   'kidq': '마태 아저씨 머리 위에서 나팔을 부는 건 누구일까?'},
  {'id': 'leave', 'label': '섬을 떠난 책', 'kind': 'photo', 'img': 'church',
   'text': ['793년, 바이킹이 이 섬의 수도원을 덮쳤어요. 875년 바이킹이 다시 오자, 주교 에아르둘프와 수도사들은 섬을 떠났어요. 쿠스버트의 유해와 에드프리스·에셀왈드의 뼈, 그리고 이 복음서를 들고서요.',
            '일곱 해를 떠돈 끝에 883년, 그들은 옛 로마 요새 자리인 체스터르스트리트에 자리를 잡았어요. 이 책은 그 뒤 112년 동안 이곳에 있었어요.'],
   'text2': ['공동체가 처음 세운 교회는 나무 교회였어요. 사진 속 교회는 그 자리에 뒷날 돌로 다시 지은 건물이에요.'],
   'kid': '바이킹이 오자 수도사들이 성인의 관이랑 이 책을 들고 섬을 떠났대.',
   'kidq': '소중한 것을 들고 먼 길을 떠난다면, 무엇부터 챙길까?'},
  {'id': 'colophon', 'label': '책 끝의 네 사람', 'kind': 'mod', 'mod': 'place', 'night': False,   # ← 그 자리에 있고 싶은 한 순간(한가운데 장면)
   'text': ['970년 무렵 체스터르스트리트. 이 공동체의 사제 앨드레드가 250년 된 복음서의 맨 끝 쪽을 펼쳐요. 요한복음이 끝난 그 쪽 빈자리에, 그는 이 책을 누가 만들었는지 적어 넣었어요.',
            '앨드레드는 네 사람의 일을 차례대로 적었어요. 쓰고, 묶고 덮고, 꾸미고, 뜻을 달았다고요. 아래 책상 위의 책에 그 차례대로 하나씩 더해 보세요.'],
   'quote': {'t': '린디스판 교회의 주교 에드프리스가 처음에 이 책을 썼어요. 하나님과 성 쿠스버트, 그리고 섬에 있는 모든 성인을 위해서요.',
             'from': '앨드레드의 맺음말 첫 줄, 린디스판 복음서 259r쪽(10세기) · 영국도서관 목록의 영어 번역을 이 안내서가 우리말로 옮김', 'u': BLCAT},
   'text2': ['맺음말의 첫 줄이에요. 맨 끝에 자기 이름을 적을 때, 앨드레드는 스스로를 ‘부족하고 가장 비참한 사제’라고 불렀어요.'],
   'kid': '책 끝에 이 책을 만든 네 사람이 적혀 있어. 차례대로 하나씩 놓아 볼까?',
   'kidq': '네 사람 가운데 누구 일이 가장 오래 걸렸을까?'},
  {'id': 'gloss', 'label': '줄 위의 작은 영어', 'kind': 'photo', 'img': 'chirho',
   'text': ['큰 라틴어 글자 위를 보세요. 갈색의 작은 글씨가 낱말마다 얹혀 있어요. 앨드레드가 라틴어 낱말 하나하나 위에 그 뜻을 옛 영어로 적은 거예요.',
            '이 쪽 맨 위, ‘복음서를 시작해요’라는 라틴어 위에 godspell이라는 낱말이 보여요. ‘좋은 이야기’라는 뜻의 옛 영어예요. 오늘의 영어 gospel(복음)이 여기서 나왔어요.'],
   'text2': ['앨드레드는 네 복음서의 뜻풀이를 저마다 누군가에게 바쳤어요. 마태복음은 하나님과 성 쿠스버트께, 마가복음은 주교에게, 누가복음은 공동체 형제들에게, 요한복음은 자기 자신을 위해서요. 여백에는 자기를 이렇게 소개했어요. “앨프레드에게서 태어나 앨드레드라 불리는 나, 좋은 여인의 아들이 말해요.”'],
   'kid': '큰 글자 위에 작은 갈색 글씨가 보여? 앨드레드가 영어로 적은 뜻이야!',
   'kidq': '‘좋은 이야기’라는 말을 우리말 한 낱말로 하면 뭘까?'},
 ],
 'imagine': {'t': '970년 무렵, 강가 마을의 작은 교회 곁. 늙은 사제가 창가에서 무거운 책을 펼쳐요. 250년 전 바닷가 섬에서 온 책이에요. 펜촉이 양피지를 긁는 사각사각 소리, 오래된 가죽 냄새. 그는 맨 끝 빈자리에 이름을 하나씩 적어 내려가요. 쓴 사람, 묶은 사람, 꾸민 사람, 그리고 자기 이름까지.',
             'kid': '눈을 감아 봐. 할아버지 수도사가 창가에서 커다란 책을 펼쳐. 사각사각, 펜 소리가 나. 책 맨 끝에 이름을 하나씩 적고 있어.'},
 'lines': ['네 사람의 손을 거쳐 완성된 한 권.', '라틴어 줄 위에 얹은, 알아들을 수 있는 말.', '좋은 이야기, godspell.', '이름을 적어 두면 기억이 돼요.'],
 'linesKid': ['쓰고, 묶고, 꾸미고, 뜻을 달고!', '큰 글자 위에 작은 영어!', '좋은 이야기!'],
 'goals': {
  's4': {'t': '앨드레드의 차례대로', 'p': '앨드레드가 적은 차례(쓰기 → 묶고 덮기 → 꾸미기 → 뜻 달기)대로 다 놓으면 카드에 금박이 입혀져요.',
         'how': '앨드레드가 적은 차례대로 책 한 권을 완성해 보세요', 'done': '앨드레드가 적은 차례대로 책을 완성했어요',
         'ways': [{'id': 'plOrder', 't': '쓰기 → 묶고 덮기 → 꾸미기 → 뜻 달기 차례로 놓기'}]},
  's5': {'t': '아이와 함께 끝까지', 'p': '아이와 함께 ‘영화처럼 보기’를 끝까지 보면 카드가 채색돼요.',
         'how': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'done': '아이와 함께 끝까지 봤어요',
         'ways': [{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'place': {
   'items': ITEMS, 'order': '쓰기, 묶고 덮기, 꾸미기, 뜻 달기',
   'intro': '아래에서 하나를 골라 책상 위의 책에 더해 보세요. 앨드레드가 적은 차례는 쓰기, 묶고 덮기, 꾸미기, 뜻 달기예요.',
   'climax': '앨드레드는 다른 쪽 여백에 이렇게도 적었어요. “살아 계신 하나님, 에드프리스와 에셀왈드와 빌프리스와 죄인 앨드레드를 기억하소서. 이 네 사람이 하나님과 함께 이 책에 힘썼어요.”<span class="la">hoc euangelium deo &amp; cuðberhto construxerunt &amp; ornauerunt<br>“하나님과 쿠스버트를 위해 이 복음서를 짓고 꾸몄어요” · 앨드레드의 맺음말(259r·89v쪽), 이 안내서가 옮김</span>',
   'home': None,
   'wrongOrder': '앨드레드가 적은 차례는 이래요: {order}',
   'orderDone': '앨드레드가 적은 차례대로 다 놓았어요',
   'daylight': False,
   'svg': stage_svg()}},
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 놓아 보기</button></div>
  <div class="pl-home" hidden><p></p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>쿠스버트</b> 린디스판의 수도사이자 주교였고, 687년에 세상을 떠났어요. 이 복음서는 그를 기리며 ‘하나님과 성 쿠스버트를 위해’ 만들어졌어요.',
    '<b>앨드레드</b> 970년에는 체스터르스트리트에서 쿠스버트의 유해를 모신 공동체의 책임자(프로보스트)였어요.',
    '<b>은 8오라</b> 오라(ora)는 옛날 은을 다는 단위예요. 앨드레드는 누가복음의 뜻풀이를 공동체에 바치며 공동체에 들어가는 값으로 은 8오라를 냈고, 요한복음과 함께는 은 4오라를 하나님과 성 쿠스버트께 바쳤다고 적었어요.',
    '<b>양탄자 페이지</b> 네 복음서마다 앞에 글자 없이 무늬로만 채운 쪽이 있어요. 한 권 안에서 복음서 하나하나를 따로 여는 속표지 구실을 했을 거라는 해설도 있어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>만든 해</b> 715년 무렵으로 보는 학자가 많지만, 700년 무렵이나 698년 이전으로 보는 학자도 있어요.',
    '<b>보석 표지</b> 빌프리스가 꾸민 처음 표지는 남아 있지 않아요. 바이킹 시대에 잃었을 거라고 보는 설명이 많아요. 지금의 은빛 표지는 1852~1853년 더럼 주교 에드워드 몰트비가 돈을 내 새로 만든 거예요.',
    '<b>네 사람</b> 앨드레드는 250년쯤 뒤의 사람이에요. 그래도 학자들은 그의 맺음말을 대체로 맞고 믿을 만한 기록으로 여겨요.']},
  {'h': '줄 위의 영어 더 보기', 'img': ['luke'], 'p': [
    '누가복음 첫 쪽에도 커다란 글자 사이사이에 앨드레드의 작은 뜻풀이가 있어요. 맨 위 ‘누가의 복음서를 시작해요’라는 줄 위에도 godspell이 보여요.',
    '앨드레드는 라틴어를 그대로 두고 그 위에 낱말마다 뜻을 달았어요. 라틴어를 모르는 형제들도 복음서를 알아듣게 하려는 일이었다고 학자들은 봐요.']},
  {'h': '직접 가 보기', 'img': ['priory'], 'checked': '2026년 11월 18일', 'p': [
    '린디스판 섬은 하루에 두 번 밀물에 둑길이 잠겨요. 섬에 가기 전에 노섬벌랜드 주의 ‘안전하게 건너는 시간’을 꼭 확인해요.',
    '섬에는 수도원 터가 있어요. 복음서 진품은 런던 영국도서관에 있고, 고향 북잉글랜드에서도 몇 차례 전시되었어요.'],
   'links': [{'t': '노섬벌랜드 주: 홀리 아일랜드 둑길, 안전하게 건너는 시간표', 'u': 'https://holyislandcrossingtimes.northumberland.gov.uk', 'm': '영어'},
             {'t': '스마트히스토리: 린디스판 복음서 해설(영상·글)', 'u': SMART, 'm': '영어'},
             {'t': '아트 오브 더 미들 에이지스: 앨드레드의 맺음말 전체 번역', 'u': COLO, 'm': '영어'}]},
 ],
 'src': [
  {'l': '영국도서관 소장 목록: Cotton MS Nero D IV — 259r쪽 맺음말의 영어 번역, 뜻풀이 10세기 3/4분기·앨드레드 970년 무렵, 259장·365×275mm, 1853년 표지, 1996·2000·2013년 북잉글랜드 전시', 'u': BLCAT},
  {'l': 'Art of the Middle Ages: 린디스판 복음서 맺음말 — 앨드레드의 네 복음서 헌정, 은 여덟·네 온스, 89v쪽 ‘살아 계신 하나님, 기억하소서’, 앨프레드의 아들', 'u': COLO},
  {'l': 'Smarthistory: The Lindisfarne Gospels — 한 사람이 쓴 책, 에드프리스(698~721 주교), 낱말마다 단 뜻풀이, 양탄자 페이지', 'u': SMART},
  {'l': 'Anglo-Saxon Manuscripts in Microfiche Facsimile 206번: 875년 에아르둘프와 떠난 일, 883~995년 체스터르스트리트, 970년 프로보스트 앨드레드, 1852~1853년 표지', 'u': SFU},
  {'l': 'Ancient History Sites: 체스터르스트리트 성 마리아·성 쿠스버트 교회 — 일곱 해 떠돎, 883년 정착, 옛 로마 요새, 나무 교회, 1056년 돌 교회', 'u': 'https://www.ancient-history-sites.com/?p=122606'},
  {'l': 'Catholic Answers 백과(옛 가톨릭 백과): 린디스판 — 635년 아이오나에서 온 에이단', 'u': 'https://www.catholic.com/encyclopedia/diocese-and-monastery-of-lindisfarne'},
  {'l': 'EWTN 백과: 린디스판 — 875년 바이킹이 다시 왔을 때 쿠스버트의 유해와 떠난 수도사들, 마지막 주교 에아르둘프', 'u': 'https://www.ewtn.com/catholicism/library/ancient-diocese-and-monastery-of-lindisfarne-10603'},
  {'l': 'Visit Northumberland: 홀리 아일랜드 둑길 — 하루 두 번 밀물에 끊기는 섬', 'u': 'https://visitnorthumberland.com/coast/holy-island/crossing-times'},
  {'l': 'Geograph: 린디스판 수도원 터 — 793년 바이킹, 지금 남은 폐허는 1093년 뒤 다시 세운 수도원', 'u': 'https://www.geograph.org.uk/photo/6850326'},
  {'l': 'Etymonline: gospel — 옛 영어 godspel, ‘좋은 이야기’', 'u': 'https://www.etymonline.com/word/gospel'},
  {'l': 'History Hit: 린디스판 복음서 10가지 — 처음 표지는 바이킹 시대에 잃었을 것, 1852년 몰트비 주교의 새 표지', 'u': 'https://www.historyhit.com/facts-about-the-lindisfarne-gospels'},
  {'l': 'Wikipedia: Lindisfarne Gospels(길잡이) — 715년 무렵, 쿠스버트 687년', 'u': 'https://en.wikipedia.org/wiki/Lindisfarne_Gospels'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 45%', 'p1': '50% 52%', 's0': 1.2, 's1': 1.05, 'kicker': '715년 무렵 · 잉글랜드 린디스판 섬', 'title': '린디스판 복음서',
   'lines': [{'t': '잉글랜드 북쪽의 작은 섬에서 만든 복음서예요.'}, {'t': '이 책 맨 끝에는 만든 사람들의 이름이 적혀 있어요.'}],
   'kid': [{'t': '무늬가 가득한 옛날 성경책이야.'}, {'t': '책 끝에 만든 사람들 이름이 있대!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '물이 빠지면'},
  {'type': 'img', 'ch': 1, 'img': 'causeway', 'fit': 'cover', 'p0': '40% 55%', 'p1': '60% 50%', 's0': 1.2, 's1': 1.05, 'cap': '린디스판 섬으로 가는 둑길',
   'lines': [{'t': '린디스판은 하루에 두 번 밀물에 길이 끊기는 섬이에요.'}, {'t': '635년 수도원이 섰고, 주교 쿠스버트가 687년에 세상을 떠났어요.'}],
   'kid': [{'t': '물이 빠지면 길이 열리는 섬이야!'}, {'t': '섬에 가려면 언제 가야 할까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '한 사람의 책'},
  {'type': 'img', 'ch': 2, 'img': 'matthew', 'fit': 'contain', 'p0': '45% 45%', 'p1': '45% 50%', 's0': 1.0, 's1': 1.1, 'cap': '25v쪽, 글을 쓰는 마태',
   'lines': [{'t': '715년 무렵, 한 사람이 이 책을 다 쓰고 그렸다고 학자들은 봐요.'}, {'t': '아마 주교 에드프리스예요. 하나님과 성 쿠스버트를 위해서요.'}],
   'kid': [{'t': '한 사람이 이 큰 책을 다 쓰고 그렸대.'}, {'t': '마태 아저씨는 무엇을 하고 있어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '섬을 떠나다'},
  {'type': 'img', 'ch': 3, 'img': 'church', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 60%', 's0': 1.15, 's1': 1.0, 'cap': '체스터르스트리트의 교회',
   'lines': [{'t': '875년, 바이킹을 피해 수도사들이 섬을 떠났어요.'}, {'t': '쿠스버트의 유해와 이 책을 들고서요. 883년, 체스터르스트리트에 닿았어요.'}],
   'kid': [{'t': '수도사들이 성인의 관이랑 책을 들고 섬을 떠났대.'}, {'t': '일곱 해 동안 어디를 떠돌았을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '책 끝의 네 사람'},
  {'type': 'mod', 'mod': 'place', 'ch': 4,
   'lines': [{'t': '970년 무렵, 사제 앨드레드가 책 끝 빈자리에 적어요.'},
             {'t': '에드프리스가 처음에 이 책을 썼고,', 'act': 'write'}, {'t': '에셀왈드가 묶고 덮었고,', 'act': 'bind'},
             {'t': '빌프리스가 금과 보석으로 꾸몄고,', 'act': 'lights', 'wait': 1500}, {'t': '나 앨드레드가 줄 위에 영어로 뜻을 적었어요.', 'act': 'gloss'},
             {'t': '살아 계신 하나님, 이 네 사람을 기억하소서.', 'q': True, 'from': '앨드레드의 여백 글에서', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '책 끝에 네 사람이 적혀 있어.'}, {'t': '쓰고!', 'act': 'write'}, {'t': '묶고!', 'act': 'bind'},
           {'t': '반짝반짝 꾸미고!', 'act': 'lights', 'wait': 1500}, {'t': '영어로 뜻을 달았어!', 'act': 'gloss'},
           {'t': '책이 다 됐어!', 'act': 'day', 'wait': 1500}]},
  {'type': 'chapter', 'ch': 5, 'no': 5, 't': '줄 위의 영어'},
  {'type': 'img', 'ch': 5, 'img': 'chirho', 'fit': 'cover', 'p0': '30% 8%', 'p1': '45% 20%', 's0': 2.2, 's1': 1.5, 'cap': '29r쪽, 큰 글자 위의 작은 뜻풀이',
   'lines': [{'t': '큰 라틴어 위의 작은 갈색 글씨, 앨드레드가 적은 옛 영어예요.'}, {'t': '맨 위의 godspell은 ‘좋은 이야기’, 오늘의 gospel이에요.'}],
   'kid': [{'t': '큰 글자 위에 작은 글씨가 보여?'}, {'t': '‘좋은 이야기’를 우리말로 하면?', 'ask': True}]},
  {'type': 'imagine', 'ch': 6,
   'lines': [{'t': '강가 마을의 작은 교회 곁, 늙은 사제가 무거운 책을 펼쳐요.'}, {'t': '사각사각 펜 소리, 오래된 가죽 냄새.'}, {'t': '그는 맨 끝에 이름을 하나씩 적어 내려가요.'}],
   'kid': [{'t': '눈을 감아 봐. 할아버지 수도사가 책을 펼쳐.'}, {'t': '사각사각, 이름을 하나씩 적어.'}]},
  {'type': 'reward', 'ch': 6},
 ],
}
