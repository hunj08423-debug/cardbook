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
그림 원본(src)은 deep_src/book-lindisfarne/ (저장소 밖). 받는 법: commons_get.py
재벌(2026-11-22 · 27번 묶음 창): 열쇠 물음 셋(qs) · 뒷이야기 세 꾸러미(qx) · 후보(qcand)를 얹고, 본 카드에 길잡이 몇 줄을 넣었어요.
새 그림은 받지 않았어요. 고양이 · 점 · 날개 달린 사람은 이미 받은 139r · 25v쪽의 부분이에요(crop)."""
import random
S = 'book-lindisfarne/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

BLCAT = 'https://searcharchives.bl.uk/catalog/040-001102725'
COLO = 'https://artofthemiddleages.com/s/main/item/4425'
SMART = 'https://smarthistory.org/the-lindisfarne-gospels/'
SFU = 'https://journals.lib.sfu.ca/index.php/asmmf/article/download/5513/4594/19960'
EH = 'https://www.english-heritage.org.uk/visit/places/lindisfarne-priory/history/'
EHV = 'https://www.english-heritage.org.uk/visit/places/lindisfarne-priory/History/viking-raid/'
HT = 'https://www.historytoday.com/archive/st-cuthbert-reburied-durham-cathedral'
DWHS = 'https://www.durhamworldheritagesite.com/history/st-cuthbert/body'
SYM = 'https://ecatholic2000.com/bede3/untitled-97.shtml'
PEN = 'https://penelope.uchicago.edu/~grout/encyclopaedia_romana/Britannia/anglo-saxon/lindisfarne/lindisfarnegospels.html'
BLCC = 'https://britishlibrary.typepad.co.uk/collectioncare/2013/07/under-the-microscope-with-the-lindisfarne-gospels.html'
BACK = 'https://www.lindisfarne.org.uk/gospels/gospels3.htm'
BLCG = 'https://www.bl.uk/stories/blogs/posts/st-cuthbert-gospel-saved-for-the-nation'
TCD = 'https://www.futurelearn.com/info/courses/book-of-kells/0/steps/50082'
ONE = 'https://employees.oneonta.edu/farberas/arth/arth212/book_of_kells.html'
BRIT = 'https://www.britannica.com/topic/Vulgate'
SLSA = 'https://digital.collections.slsa.sa.gov.au/nodes/view/2099'
GEOP = 'https://www.geograph.org.uk/photo/6849697'
NOTT = 'https://www.nottingham.ac.uk/manuscriptsandspecialcollections/researchguidance/medievalbooks/quires.aspx'
NLM = 'https://www.newliturgicalmovement.org/2015/09/st-matthew-evangelist-from-lindisfarne.html'
HH = 'https://www.historyhit.com/facts-about-the-lindisfarne-gospels'
LUKEU = 'https://commons.wikimedia.org/wiki/File:Lindisfarne_Gospels_folio_139r.jpg'
MATU = 'https://commons.wikimedia.org/wiki/File:St._Matthew_-_Lindisfarne_Gospels_(710-721),_f.25v_-_BL_Cotton_MS_Nero_D_IV.jpg'


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
  'say': '린디스판 섬사람들의 주교 에셀왈드가 책장을 묶고 겉을 씌웠어요. 앨드레드는 ‘그가 잘 아는 솜씨대로’라고 적었어요.'},
 {'id': 'lights', 't': '꾸미기', 'la': 'Billfrith · 빌프리스',
  'say': '은둔 수도자(홀로 떨어져 기도하며 사는 수도자) 빌프리스가 겉표지의 장식을 두드려 만들고, 금과 보석, 금을 입힌 은으로 꾸몄어요.'},
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
  'chirho': {'src': S + 'LindisfarneChiRiho.jpg', 'cap': '린디스판 복음서 29r쪽, 마태복음 1장 18절이 시작되는 ‘키로’ 쪽(키로는 그리스도를 뜻하는 그리스어의 첫 두 글자 X·P)',
             'cr': '퍼블릭 도메인 · 위키미디어 공용(영국도서관 Cotton MS Nero D IV)', 'u': 'https://commons.wikimedia.org/wiki/File:LindisfarneChiRiho.jpg',
             'alt': '커다란 X와 P 모양 글자가 매듭과 소용돌이 무늬로 쪽의 위쪽을 가득 채웠고, 아래에 굵은 라틴어 글줄 세 줄이 이어진다. 큰 글자들 위와 오른쪽 여백에 갈색의 작은 글씨가 적혀 있다.'},
  'luke': {'src': S + 'Lindisfarne_Gospels_folio_139r.jpg', 'cap': '139r쪽, 누가복음 첫 쪽',
           'cr': '퍼블릭 도메인 · 위키미디어 공용(영국도서관 Cotton MS Nero D IV)', 'u': 'https://commons.wikimedia.org/wiki/File:Lindisfarne_Gospels_folio_139r.jpg',
           'alt': '왼쪽에 매듭 무늬로 채운 커다란 Q 글자가 서 있고, 오른쪽에 붉은 점으로 테를 두른 라틴어 글자들이 줄지어 있다. 글줄 사이사이에 갈색의 작은 글씨가 적혀 있다.'},
  'cat': {'src': S + 'Lindisfarne_Gospels_folio_139r.jpg', 'crop': [0.62, 0.52, 0.90, 0.80], 'max': 1600, 'cap': '139r쪽 오른쪽 아래, 테두리 끝의 고양이 머리',
          'cr': '퍼블릭 도메인 · 위키미디어 공용(영국도서관 Cotton MS Nero D IV) · 139r쪽의 오른쪽 아래 부분', 'u': LUKEU,
          'alt': '붉은 점으로 둘러싼 라틴어 글자들 오른쪽, 세로 테두리 맨 아래에 귀가 쫑긋한 고양이 머리가 왼쪽 글줄을 바라본다. 그 위로 파란 쉼표 모양 가슴을 한 새들이 테두리를 따라 줄지어 있다.'},
  'dots': {'src': S + 'Lindisfarne_Gospels_folio_139r.jpg', 'crop': [0.44, 0.30, 0.86, 0.54], 'max': 1600, 'cap': '139r쪽, 붉은 점으로 둘러싸 남긴 NIAM 네 글자',
           'cr': '퍼블릭 도메인 · 위키미디어 공용(영국도서관 Cotton MS Nero D IV) · 139r쪽의 가운데 부분', 'u': LUKEU,
           'alt': '붉은 점이 빽빽하게 찍힌 바탕에서, 점을 찍지 않고 남긴 양피지 빛깔로 N, I, A, M 네 글자가 드러난다. 위에는 매듭 무늬로 채운 큰 글자 두 개가, 오른쪽 테두리에는 새들이 이어진다.'},
  'angel': {'src': S + 'St._Matthew_-_Lindisfarne_Gospels_710-721_f.25v_-_BL_Cotton_MS_Nero_D_IV.jpg', 'crop': [0.07, 0.05, 0.68, 0.42], 'max': 1600,
            'cap': '25v쪽 왼쪽 위, 나팔을 부는 날개 달린 사람',
            'cr': '퍼블릭 도메인 · 위키미디어 공용(영국도서관 Cotton MS Nero D IV) · 25v쪽의 왼쪽 위 부분', 'u': MATU,
            'alt': '둥근 금빛 후광을 두른 날개 달린 사람이 긴 나팔을 불며 초록 책을 안고 있다. 왼쪽 위에 imagohominis라는 글자가, 오른쪽에 큰 글자로 마태의 이름이 적혀 있고, 아래에 머리와 수염이 하얀 마태의 얼굴이 보인다.'},
  'priory': {'src': S + 'Lindisfarne_Priory_2016-05-29.jpg', 'cap': '린디스판 수도원 터. 지금 남은 붉은 돌 폐허는 뒷날(11~12세기) 다시 지은 수도원이에요',
             'cr': '사진: August Schwerdfeger · CC BY 4.0 · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:Lindisfarne_Priory_2016-05-29.jpg',
             'alt': '붉은 사암으로 지은 아치와 벽이 반쯤 무너진 채 서 있고, 가운데로 높은 반원 아치 하나가 흐린 하늘을 가로지른다. 바닥은 푸른 잔디다.'},
 },
 'scenes': [
  {'id': 'island', 'label': '물이 빠지면 열리는 섬', 'kind': 'photo', 'img': 'causeway',
   'text': ['잉글랜드 북동쪽 바닷가의 린디스판은 하루에 두 번 밀물에 길이 끊기는 섬이에요. 바닷물이 빠졌을 때만 둑길로 건널 수 있어요.',
            '635년, 스코틀랜드 아이오나 섬에서 온 수도사 에이단이 이곳에 수도원을 세웠어요. 이 수도원의 주교(한 지역의 교회들을 맡은 성직자)였던 쿠스버트는 687년에 세상을 떠났어요. 사람들은 그를 성인(교회가 거룩한 삶을 기리는 사람)으로 기렸어요.'],
   'kid': '물이 빠지면 길이 열리는 섬이래! 하루에 두 번 길이 물에 잠겨.',
   'kidq': '이 섬에 가려면 언제 출발해야 할까?'},
  {'id': 'scribe', 'label': '한 사람이 쓰고 그린 책', 'kind': 'photo', 'img': 'matthew',
   'text': ['715년 무렵, 이 섬에서 네 복음서를 담은 큰 책이 만들어졌어요. 복음서는 예수님의 삶과 가르침을 적은 책으로, 마태·마가·누가·요한복음 넷이 있어요. 학자들은 한 사람이 이 책의 글과 그림을 다 했다고 봐요. 아마 698년부터 721년까지 린디스판의 주교였던 에드프리스예요.',
            '양피지 259장, 한 장의 크기는 세로 36.5cm, 가로 27.5cm쯤이에요. 마태복음 앞의 그림에서는, 이 복음서를 썼다고 전해지는 마태가 무릎 위 책에 글을 쓰고 있어요.'],
   'text2': ['책 끝의 기록은 이 책이 ‘하나님과 성 쿠스버트를 위해’ 만들어졌다고 적었어요.',
             '그림 아래 ‘25v쪽’은 25번째 장의 뒷면이라는 뜻이에요. 필사본은 장마다 번호를 매기고, 앞면은 r, 뒷면은 v로 적어요.'],
   'kid': '한 사람이 이 큰 책을 다 쓰고 그렸대. 그림 속 마태 아저씨도 글을 쓰고 있어.',
   'kidq': '마태 아저씨 머리 위에서 나팔을 부는 건 누구일까?'},
  {'id': 'leave', 'label': '섬을 떠난 책', 'kind': 'photo', 'img': 'church',
   'text': ['793년, 바이킹이 이 섬의 수도원을 덮쳤어요. 875년 바이킹이 다시 오자, 주교 에아르둘프와 수도사들은 섬을 떠났어요. 쿠스버트의 유해와, 에드프리스와 그 뒤를 이은 주교 에셀왈드의 뼈, 그리고 이 복음서를 들고서요.',
            '일곱 해를 떠돈 끝에 883년, 그들은 옛날 로마 군대의 요새가 있던 체스터르스트리트에 자리를 잡았어요. 이 책은 그 뒤 112년 동안 이곳에 있었어요.'],
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
   'text2': ['앨드레드는 네 복음서의 뜻풀이를 저마다 누군가에게 바쳤어요. 마태복음은 하나님과 성 쿠스버트께, 마가복음은 주교에게, 누가복음은 공동체 형제들에게, 요한복음은 자기 자신을 위해서요. 여백에는 자기를 이렇게 소개했어요. “앨프레드에게서 태어나 앨드레드라 불리는 나, 좋은 여인의 아들이 말해요.” 앨프레드는 아버지의 이름이에요.'],
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
 'qs': [   # 열쇠 물음 셋(재벌 2026-11-22): ① 앞면 물음 ② 셋째 장면(왜 관을 들고 떠났나) ③ 다섯째 장면(왜 라틴어, 왜 영어 뜻풀이)
  {'q': '글자가 하나도 없는 이 쪽은 왜 만들었을까요?',
   'img': 'card', 'pos': '50% 40%',
   'a': ['이런 쪽을 ‘양탄자 쪽’이라고 해요. 이 책에는 다섯 장이 있는데, 맨 앞에 하나, 그리고 네 복음서 앞에 하나씩 놓였어요.',
         '영국도서관의 큐레이터 도일은 이 쪽이 복음서 하나하나를 따로 여는 속표지였을 거라고 봐요. 미술사학자 우드빌은 수도사들이 이 무늬를 따라가며 묵상에 잠겼을 거라고 상상해요.'],
   'see': '앞면 카드의 양탄자 쪽이, 복음서로 들어가기 전에 지나는 무늬의 문으로 보여요.', 'seeAt': 'front',
   'film': [
    {'type': 'img', 'img': 'card', 'fit': 'contain', 'p0': '50% 50%', 'p1': '50% 50%', 's0': 1.0, 's1': 1.08,
     'lines': [{'t': '글자 없이 무늬로만 채운 이런 쪽을 ‘양탄자 쪽’이라고 해요.'}, {'t': '이 책에는 다섯 장이 있어요. 맨 앞에 하나, 복음서마다 하나씩.'}],
     'kid': [{'t': '글자 없이 무늬만 가득한 쪽을 양탄자 쪽이라고 해.'}]},
    {'type': 'img', 'img': 'card', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 34%', 's0': 1.2, 's1': 1.45,
     'lines': [{'t': '영국도서관의 도일은, 복음서마다 따로 여는 속표지였을 거라고 봐요.'}, {'t': '한 권 안에 복음서 네 권이 저마다 문을 달고 있는 셈이에요.'}],
     'kid': [{'t': '책 속에 숨은 또 하나의 표지래.'}]},
    {'type': 'black',
     'lines': [{'t': '수도사들은 이 무늬를 따라가며 묵상에 잠겼을지도 몰라요.'}, {'t': '미술사학자 우드빌의 상상이에요.'}],
     'kid': [{'t': '무늬를 따라가며 조용히 기도했을지도 몰라.'}]},
    {'type': 'img', 'img': 'card', 'fit': 'cover', 'p0': '50% 50%', 'p1': '50% 50%', 's0': 1.02, 's1': 1.1,
     'lines': [{'t': '이제 앞면 카드를 다시 볼까요?'}, {'t': '복음서를 펼치기 전에 지나는, 무늬로 짠 문이에요.'}],
     'kid': [{'t': '이제 다시 보면, 복음서로 들어가는 무늬 문이야!'}]},
   ]},
  {'q': '쿠스버트는 누구길래, 그 몸까지 들고 피난을 갔을까요?',
   'img': 'church', 'pos': '50% 55%',
   'a': ['쿠스버트는 린디스판의 수도사로, 작은 섬에서 홀로 기도하며 살기도 했어요. 687년에 세상을 떠나고 11년 뒤 무덤을 열자, 몸이 썩지 않은 채였대요.',
         '수도사들은 이를 거룩함의 표시로 여겼고, 그의 관을 찾아 순례자가 몰려들었어요. 바이킹을 피해 떠날 때도 수도사들은 가장 귀한 것으로 그의 유해를 챙겼어요.'],
   'see': '셋째 장면의 피난길이, 섬의 가장 귀한 것을 지키러 떠난 길로 보여요.', 'seeAt': 'leave',
   'film': [
    {'type': 'img', 'img': 'priory', 'fit': 'cover', 'p0': '50% 30%', 'p1': '50% 45%', 's0': 1.15, 's1': 1.0,
     'lines': [{'t': '쿠스버트는 이 섬의 수도사이자 주교였어요.'}, {'t': '687년에 세상을 떠나 섬의 교회에 묻혔어요.'}],
     'kid': [{'t': '쿠스버트는 이 섬에서 기도하며 살았어.'}]},
    {'type': 'black',
     'lines': [{'t': '11년 뒤 무덤을 열자, 몸이 썩지 않은 채였대요.'}, {'t': '수도사들은 이를 거룩함의 표시로 여겼어요.'}],
     'kid': [{'t': '무덤을 열었더니, 잠든 것 같았대.'}]},
    {'type': 'img', 'img': 'causeway', 'fit': 'cover', 'p0': '30% 70%', 'p1': '55% 60%', 's0': 1.1, 's1': 1.0,
     'lines': [{'t': '그의 관을 찾아 순례자들이 섬으로 몰려왔어요.'}, {'t': '섬은 잉글랜드 북쪽에서 가장 큰 순례지가 되었어요.'}],
     'kid': [{'t': '많은 사람이 쿠스버트를 만나러 섬에 왔대.'}]},
    {'type': 'img', 'img': 'church', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 60%', 's0': 1.15, 's1': 1.0,
     'lines': [{'t': '이제 셋째 장면을 다시 볼까요?'}, {'t': '바이킹을 피해 떠나면서도, 수도사들은 성인의 관을 두고 가지 않았어요.'}],
     'kid': [{'t': '이제 다시 보면, 성인을 모시고 떠난 길이야!'}]},
   ]},
  {'q': '영국에서 만든 책인데, 왜 라틴어로 썼을까요?',
   'img': 'luke', 'pos': '50% 40%',
   'a': ['이 책의 글은 4세기에 히에로니무스가 교황의 부탁으로 옮긴 라틴어 성경, 불가타예요. 로마 교회가 6세기 무렵부터 두루 쓰던 성경이라, 린디스판에서도 이 라틴어를 베꼈어요.',
         '250년쯤 뒤 앨드레드는 라틴어를 그대로 두고, 낱말마다 그 위에 옛 영어 뜻을 달았어요. 이것이 지금 남아 있는 가장 오래된 영어 복음서예요.'],
   'see': '다섯째 장면 큰 라틴어 위의 갈색 글씨가, 지금 남은 가장 오래된 영어 복음서로 보여요.', 'seeAt': 'gloss',
   'film': [
    {'type': 'black',
     'lines': [{'t': '이 책의 라틴어는 4세기 히에로니무스가 옮긴 성경, 불가타예요.'}, {'t': '로마 교회가 오랫동안 두루 쓴 성경이에요.'}],
     'kid': [{'t': '옛날 교회는 라틴어 성경을 읽었대.'}]},
    {'type': 'img', 'img': 'luke', 'fit': 'cover', 'p0': '45% 35%', 'p1': '55% 50%', 's0': 1.15, 's1': 1.35,
     'lines': [{'t': '린디스판의 수도사들도 이 라틴어를 그대로 베꼈어요.'}, {'t': '누가복음 첫 쪽의 큰 글자들도 라틴어예요.'}],
     'kid': [{'t': '커다란 글자는 라틴어야.'}]},
    {'type': 'img', 'img': 'chirho', 'fit': 'cover', 'p0': '25% 6%', 'p1': '40% 8%', 's0': 2.4, 's1': 2.0, 'o': '30% 6%',
     'lines': [{'t': '250년쯤 뒤, 앨드레드가 낱말마다 위에 옛 영어 뜻을 달았어요.'}, {'t': '지금 남은 가장 오래된 영어 복음서예요.'}],
     'kid': [{'t': '작은 글씨가 가장 오래된 영어 복음서래!'}]},
    {'type': 'img', 'img': 'chirho', 'fit': 'cover', 'p0': '50% 20%', 'p1': '50% 55%', 's0': 1.3, 's1': 1.05,
     'lines': [{'t': '이제 다섯째 장면을 다시 볼까요?'}, {'t': '큰 라틴어 위의 작은 갈색 글씨를 찾아보세요.'}],
     'kid': [{'t': '이제 다시 보면, 작은 글씨가 보물이야!'}]},
   ]},
 ],
 'qx': [   # 뒷이야기 꾸러미(재벌 2026-11-22): 1 = 사람·그림 속 ‘저건 뭐지?’ · 2 = 1에서 이어짐(점·키로·물감·떠돎·길·런던) · 3 = 2에서 이어짐(편지·관 속의 책·걸린 시간)
  {'id': 'sea', 'pack': 1, 'q': '바다에 빠진 복음서가 다시 돌아왔다고요?', 'hook': '바다에 빠진 책',
   'img': 'causeway', 'pos': '70% 60%',
   'a': ['12세기 초 더럼의 수도사 시므온이 전하는 이야기예요. 떠돌던 무리가 아일랜드로 건너가려 배를 띄웠는데, 폭풍에 금과 보석으로 꾸민 복음서가 바다로 떨어졌대요.',
         '환상 속에 나타난 쿠스버트의 말대로 썰물 때 3마일 넘게 걸어 나가 책을 찾았고, 바닷물 자국도 없었대요. 사흘 뒤 바닷가로 밀려왔고 얼룩이 졌다는 글도 있어 자료마다 달라요. 학자들은 이 이야기를 전설로 봐요.'],
   'see': '셋째 장면의 일곱 해 떠돎이, 바다에 빠진 책을 다시 건졌다는 전설까지 품은 길로 보여요.', 'seeAt': 'leave',
   'src': [{'t': '더럼의 시므온이 쓴 더럼 교회의 역사(12세기 초) · 영어 번역', 'm': '영어 · ecatholic2000(베다 저작 모음 안에 실림) · 아일랜드로 가려던 배, 폭풍에 바다로 떨어진 금·보석 복음서, 환상 속 쿠스버트, 썰물에 3마일 넘게 걸어 나가 찾음, 바닷물 자국 없음', 'u': SYM},
           {'t': 'Anglo-Saxon Manuscripts in Microfiche Facsimile 206', 'm': '영어 · 일곱 해 떠돎에 시므온이 전하는 ‘전설 같은’ 바다 구조 이야기가 들어 있음', 'u': SFU},
           {'t': 'Encyclopaedia Romana: Lindisfarne Gospels', 'm': '영어 · 시카고 대학 누리집 · 아일랜드 바다에 빠졌다가 사흘 뒤 바닷가로 밀려옴, 얼룩졌지만 상하지 않음', 'u': PEN}]},
  {'id': 'angel', 'pack': 1, 'q': '마태 머리 위에서 나팔을 부는 날개 달린 사람은 누구예요?', 'hook': '나팔 부는 날개 사람',
   'img': 'angel', 'pos': '35% 35%',
   'a': ['네 복음서에는 저마다 상징이 있어요. 잉글랜드의 학자 비드는 마태에게 사람을 맞추며, 사람은 그리스도의 사람으로서의 모습을 뜻한다고 풀었어요.',
         '그래서 왼쪽 위에 라틴어로 ‘이마고 호미니스(imago hominis)’, 곧 ‘사람의 모습’이라고 적었어요. 오른쪽 큰 글자는 마태의 이름인데, 앞의 ‘하기오스’는 성인을 뜻하는 그리스어예요.'],
   'see': '둘째 장면 마태 위의 날개 달린 사람이, 마태복음을 알리는 상징으로 보여요.', 'seeAt': 'scribe',
   'src': [{'t': 'Smarthistory: The Lindisfarne Gospels', 'm': '영어 · 루이자 우드빌의 글: 비드가 정한 네 복음서의 상징(마태는 사람, 그리스도의 사람다운 모습) · 영국도서관 도일의 영상: 이름 일부가 그리스어, 상징에도 이름표', 'u': SMART},
           {'t': 'New Liturgical Movement: St Matthew the Evangelist from the Lindisfarne Gospels(2015)', 'm': '영어 · 데이비드 클레이턴 · imago hominis는 ‘사람의 모습’, 그리스어 ‘하기오스(Hagios)’로 성인이라 부름', 'u': NLM}]},
  {'id': 'cat', 'pack': 1, 'q': '누가복음 첫 쪽 구석에 고양이가 숨어 있다고요?', 'hook': '새 여덟 마리와 고양이',
   'img': 'cat', 'pos': '55% 70%',
   'a': ['누가복음 첫 쪽의 오른쪽 아래, 테두리 끝에 고양이 머리가 있어요. 그 위로 테두리를 따라 새들이 줄지어 올라가요.',
         '미술사학자 우드빌은 이 고양이가 방금 새 여덟 마리를 삼켰다고 풀어요. 에드프리스는 왜가리 가슴을 쉼표 모양으로 그리고, 그 모양을 아래로 되풀이하다가 고양이의 앞발로 바꾸어 놓았대요.'],
   'see': '다섯째 장면 P 글자 끝의 작은 짐승 머리도, 무늬 속에 짐승을 숨겨 둔 같은 손으로 보여요.', 'seeAt': 'gloss',
   'src': [{'t': 'Smarthistory: The Lindisfarne Gospels', 'm': '영어 · 루이자 우드빌의 글: 누가복음 첫 쪽은 짐승으로 가득함, 왜가리 가슴의 쉼표 모양이 고양이 앞발로, 새 여덟 마리를 막 삼킨 고양이', 'u': SMART}]},
  {'id': 'aldred', 'pack': 1, 'q': '앨드레드는 왜 은까지 내며 뜻풀이를 바쳤을까요?', 'hook': '공동체에 들어가는 값',
   'img': 'chirho', 'pos': '92% 68%',
   'a': ['앨드레드는 누가복음의 뜻풀이를 공동체 형제들에게 바치며, 공동체에 들어가는 값으로 은 8오라를 냈다고 적었어요. 오라(ora)는 옛날 은의 무게를 재던 단위예요.',
         '요한복음의 뜻풀이는 자기 몫으로 삼아, 은 4오라와 함께 하나님과 쿠스버트께 바쳤어요. 그 덕에 하늘나라에 들기를 바란다고요. 그는 970년 무렵 체스터르스트리트 공동체의 책임자(프로보스트)로도 기록에 남았어요.'],
   'see': '다섯째 장면 오른쪽 여백의 갈색 글씨가, 은을 내고 공동체에 들어간 한 사제의 손글씨로 보여요.', 'seeAt': 'gloss',
   'src': [{'t': 'Art of the Middle Ages: 린디스판 복음서 맺음말', 'm': '영어 · 누가복음 뜻풀이는 공동체에, 들어가는 값으로 은 8오라 · 요한복음은 자기 몫, 은 4오라, 하늘나라 가는 길을 바람', 'u': COLO},
           {'t': 'Anglo-Saxon Manuscripts in Microfiche Facsimile 206', 'm': '영어 · 앨드레드는 『더럼 예식서』에 체스터르스트리트의 프로보스트로 이름이 나옴', 'u': SFU}]},
  {'id': 'bill', 'pack': 1, 'q': '금과 보석으로 꾸민 겉표지는 지금도 남아 있어요?', 'hook': '사라진 보석 표지',
   'img': 'card', 'pos': '50% 6%',
   'a': ['앨드레드는 은둔 수도자 빌프리스가 책 겉의 장식을 두드려 만들고, 금과 보석, 금을 입힌 은으로 꾸몄다고 적었어요. 속의 글과 그림은 에드프리스, 겉은 빌프리스의 솜씨예요.',
         '그 표지는 남아 있지 않아요. 바이킹 시대에 잃었다는 설명도, 16세기에 수도원들이 문을 닫을 때 잃었다는 설명도 있어요. 양탄자 쪽의 무늬가 그 시대의 금속 장신구를 닮았다는 해설도 있어요.'],
   'see': '넷째 장면 책상 위의 금과 보석이, 지금은 사라진 진짜 겉표지의 자리로 보여요.', 'seeAt': 'colophon',
   'src': [{'t': '영국도서관 소장 목록: Cotton MS Nero D IV', 'm': '영어 · 맺음말 번역: 은둔 수도자 빌프리스가 바깥의 장식을 두드려 만들고 금·보석·금 입힌 은으로 꾸밈', 'u': BLCAT},
           {'t': 'History Hit: 린디스판 복음서 10가지', 'm': '영어 · 처음 표지는 바이킹 시대에 잃었을 것', 'u': HH},
           {'t': 'Encyclopaedia Romana: Lindisfarne Gospels', 'm': '영어 · 빌프리스의 금·보석·금 입힌 은은 수도원 해산 때 잃었을 것 · 양탄자 쪽은 서턴 후의 금속 장신구를 닮음', 'u': PEN},
           {'t': 'Smarthistory: The Lindisfarne Gospels', 'm': '영어 · 양탄자 쪽이 서턴 후 버클 같은 금속 공예를 닮음', 'u': SMART}]},
  {'id': 'dragon', 'pack': 1, 'q': '바이킹이 오기 전, 하늘에 불 용이 날았다고요?', 'hook': '하늘을 나는 불 용',
   'img': 'priory', 'pos': '50% 25%',
   'a': ['뒷날 북잉글랜드의 기록자들은 793년 초, 엄청난 회오리바람과 번개, 하늘을 나는 불 용을 보았다고 적었어요. 큰 굶주림이 뒤따랐고, 6월 8일 바이킹이 린디스판의 교회를 덮쳤어요.',
         '바이킹이 서유럽을 처음 크게 덮친 일이라 온 유럽이 놀랐어요. 프랑크 왕국의 궁정에 있던 요크 출신 학자 앨퀸은, 성 쿠스버트와 그 많은 성인이 자기 사람들을 지키지 못했다며 탄식하는 편지를 썼어요.'],
   'see': '셋째 장면 첫 줄의 ‘793년’이, 온 유럽을 놀라게 한 소식의 해로 보여요.', 'seeAt': 'leave',
   'src': [{'t': 'English Heritage: The Viking Raid on Lindisfarne', 'm': '영어 · 뒷날의 기록자들이 전한 793년의 회오리바람·번개·불 용, 굶주림, 6월 8일의 습격, 앨퀸의 편지', 'u': EHV},
           {'t': 'English Heritage: History of Lindisfarne Priory', 'm': '영어 · 서유럽에서 바이킹의 첫 큰 습격, 온 유럽이 놀람, 앨퀸: ‘성 쿠스버트와 그 많은 성인이 자기 사람들을 지키지 못한다면’', 'u': EH}]},
  {'id': 'dots', 'pack': 2, 'q': '누가복음 첫 쪽의 빨간 점은 모두 몇 개일까요?', 'hook': '점 1만 600개',
   'img': 'dots', 'pos': '50% 55%',
   'a': ['누가복음 첫 쪽에는 납을 구워 만든 붉은 물감 점이 1만 600개쯤 찍혀 있대요. 1분에 30개씩 찍어도 적어도 여섯 시간이 걸리는 일이에요.',
         '영국도서관이 컴퓨터로 세어 보니 ‘NIAM’ 네 글자 둘레에만 1,939개였어요. 이 네 글자는 물감으로 쓴 게 아니라, 점으로 둘러싸 남겨 둔 양피지 바탕이에요.'],
   'see': '다섯째 장면 큰 글자 둘레의 빨간 점들이, 한 점 한 점 찍어 나간 긴 시간으로 보여요.', 'seeAt': 'gloss',
   'src': [{'t': 'Lindisfarne.org.uk: The Lindisfarne Gospels', 'm': '영어 · 재닛 백하우스가 쓴 글 · 누가복음 첫 쪽의 붉은 납 점 10,600개, 1분에 30개, 적어도 여섯 시간', 'u': BACK},
           {'t': '영국도서관 보존 블로그: Under the microscope with the Lindisfarne Gospels(2013)', 'm': '영어 · 크리스티나 더피 · 구운 납으로 만든 붉은 점, 139r쪽 NIAM 둘레에서 1,939개를 셈', 'u': BLCC},
           {'t': 'Smarthistory: The Lindisfarne Gospels', 'm': '영어 · NIAM 네 글자는 양피지 바탕 그대로 남긴 글자', 'u': SMART}]},
  {'id': 'chirho', 'pack': 2, 'q': '‘키로’ 쪽은 왜 이렇게 크게 꾸몄을까요?', 'hook': 'X와 P, 그리스도의 이름',
   'img': 'chirho', 'pos': '50% 28%',
   'a': ['X와 P처럼 보이는 두 글자는 그리스어 ‘그리스도’의 첫 두 글자, 키(χ)와 로(ρ)예요. 옛 필사본은 그리스도의 이름을 이렇게 줄여 썼어요.',
         bl('MAT.1', '마태복음') + '은 1장 17절까지 조상의 이름을 늘어놓고, 18절에서 예수님이 태어나신 이야기를 시작해요. 그 첫 낱말이 ‘그리스도의’예요. 「켈스의 서」도 이 자리를 가장 화려하게 꾸몄어요.'],
   'see': '다섯째 장면의 커다란 X와 P가, 예수님 탄생 이야기를 여는 그리스도의 이름으로 보여요.', 'seeAt': 'gloss',
   'go': {'t': '「켈스의 서」 카드로 가기', 'cid': 'il-kells'},
   'src': [{'t': 'FutureLearn · 더블린 트리니티 칼리지: The Book of Kells', 'm': '영어 · 키(χ)와 로(ρ)는 그리스어 ‘그리스도’의 첫 두 글자, 이름을 줄여 쓰는 데 두루 씀 · 켈스의 서 34r쪽(마태복음 1장 18절)의 화려한 키로', 'u': TCD},
           {'t': 'SUNY 오니언타 미술사 강의 자료: Book of Kells', 'm': '영어 · 마태복음 1장 1~17절은 아브라함까지의 조상, 18절에서 그리스도의 탄생이 시작됨 · 첫머리 XPI autem generatio', 'u': ONE}]},
  {'id': 'paint', 'pack': 2, 'q': '이 색들은 무엇으로 만들었을까요?', 'hook': '달걀흰자로 갠 물감',
   'img': 'card', 'pos': '25% 62%',
   'a': ['영국도서관 과학자들이 현미경으로 살펴본 물감이에요. 초록에는 식초 위에 구리를 매달아 얻은 녹청이, 노랑에는 비소가 든 광물 웅황이 쓰였고, 붉은 점은 납을 구워 만들었어요.',
         '가루 물감은 달걀흰자를 저어 만든 풀(글레어)에 개어 썼어요. 오랜 세월에 물감이 줄어들며 아주 가는 금이 갔는데, 노란 웅황에 가장 많이 갔대요.'],
   'see': '앞면 카드의 초록과 노랑이, 구리와 광물을 달걀흰자에 갠 색으로 보여요.', 'seeAt': 'front',
   'src': [{'t': '영국도서관 보존 블로그: Under the microscope with the Lindisfarne Gospels(2013)', 'm': '영어 · 녹청(식초 위에 매단 구리), 웅황(비소가 든 노랑), 구운 납의 붉은 점, 달걀흰자 풀(글레어), 오래되어 물감이 줄며 생긴 잔금 — 웅황에 가장 많음', 'u': BLCC}]},
  {'id': 'wander', 'pack': 2, 'q': '일곱 해 동안, 누가 관을 메고 떠돌았을까요?', 'hook': '관 속에 왕의 머리가?',
   'img': 'church', 'pos': '50% 70%',
   'a': ['수도사들만 떠난 게 아니에요. 아내와 아이들까지 함께, 일곱 해 동안 잉글랜드 북쪽 곳곳을 떠돌았어요.',
         '쿠스버트의 관 속에는 섬을 수도원에 내준 오스왈드 왕의 머리와, 수도원을 세운 에이단의 뼈도 함께 넣었어요. 883년에야 체스터르스트리트에 자리를 잡았어요.'],
   'see': '셋째 장면의 피난길이, 아이들과 옛 성인들의 뼈까지 함께한 긴 행렬로 보여요.', 'seeAt': 'leave',
   'src': [{'t': 'History Today: St Cuthbert Reburied in Durham Cathedral', 'm': '영어 · 수도사와 아내·아이들이 일곱 해 동안 노섬브리아와 컴브리아를 떠돎, 오스왈드 왕의 머리와 에이단의 뼈를 쿠스버트의 관에 넣음', 'u': HT},
           {'t': 'English Heritage: History of Lindisfarne Priory', 'm': '영어 · 오스왈드 왕이 에이단에게 린디스판 섬을 내줌 · 일곱 해 떠돈 끝에 체스터르스트리트에 정착', 'u': EH},
           {'t': 'Durham World Heritage Site: The Body of Cuthbert', 'm': '영어 · 875년 가장 귀한 것과 쿠스버트의 유해를 챙겨 떠남, 883년까지 꼬박 일곱 해', 'u': DWHS}]},
  {'id': 'road', 'pack': 2, 'q': '둑길이 생기기 전에는 어떻게 섬에 건너갔을까요?', 'hook': '1954년에야 생긴 길',
   'img': 'causeway', 'pos': '40% 70%',
   'a': ['지금의 둑길은 1954년에야 놓였어요. 그 전에는 갯벌에 줄지어 세운 나무 기둥들이 안전한 길을 알려 주었어요. ‘순례자의 길’이라 불리는 이 길로 지금도 걸어서 건너는 사람이 있어요.',
         '그 길에는 물이 갑자기 차오를 때 올라가 기다리는 나무 피난 탑도 있어요. 그래서 건너기 전에 꼭 물때를 확인해요.'],
   'see': '첫째 장면의 아스팔트 길이, 1954년에야 갯벌 위에 놓인 새 길로 보여요.', 'seeAt': 'island',
   'src': [{'t': "Geograph: Holy Island Sands, Refuge on the Lindisfarne Pilgrims' Path", 'm': '영어 · 데이비드 딕슨(2021) · 길은 1954년에야 놓임, 그 전에는 기둥이 안전한 길을 알림, 지금도 걷는 순례자의 길, 밀물에 갇힌 사람을 위한 나무 피난 탑', 'u': GEOP},
           {'t': '노섬벌랜드 주: 홀리 아일랜드 둑길, 안전하게 건너는 시간표', 'm': '영어 · 건너기 전에 물때 확인', 'u': 'https://holyislandcrossingtimes.northumberland.gov.uk'}]},
  {'id': 'london', 'pack': 2, 'q': '이 책은 어떻게 런던까지 갔을까요?', 'hook': '큰불에서 살아남은 책',
   'img': 'luke', 'pos': '50% 30%',
   'a': ['995년부터 이 책은 더럼에 있었어요. 16세기 헨리 8세가 수도원들을 닫을 때 런던으로 옮겨졌고, 뒷날 수집가 로버트 코튼의 손에 들어갔어요.',
         '코튼 집안의 책들이 1731년 큰불을 만났을 때도 이 책은 상하지 않았어요. 1753년 영국박물관이 세워질 때 처음 소장품 가운데 하나가 되었고, 지금은 영국도서관에 있어요.'],
   'see': '첫째 장면의 섬에서 시작한 책이, 더럼과 런던을 거쳐 온 1,300년의 길로 보여요.', 'seeAt': 'island',
   'go': {'t': '「대영도서관 보물실」 카드로 가기', 'cid': 'lib-british'},
   'src': [{'t': 'Anglo-Saxon Manuscripts in Microfiche Facsimile 206', 'm': '영어 · 995년 더럼에 자리 잡음, 1731년 코튼 장서 화재에도 상하지 않음, 1753년 영국박물관으로', 'u': SFU},
           {'t': 'Encyclopaedia Romana: Lindisfarne Gospels', 'm': '영어 · 헨리 8세가 수도원 해산 때 런던으로 옮기게 함, 로버트 코튼이 얻어 나라에 남김', 'u': PEN},
           {'t': '영국도서관 소장 목록: Cotton MS Nero D IV', 'm': '영어 · 1753년 영국박물관의 첫 소장품 가운데 하나', 'u': BLCAT}]},
  {'id': 'letter', 'pack': 3, 'q': '이 책의 맨 앞은 복음서가 아니라 편지라고요?', 'hook': '교황에게 쓴 편지로 시작',
   'img': 'card', 'pos': '50% 85%',
   'a': ['맨 앞 양탄자 쪽을 넘기면, 히에로니무스가 교황 다마수스에게 쓴 편지 ‘새로운 일(Novum opus)’이 나와요. 382년 교황에게서 표준 라틴어 성경을 만드는 일을 맡은 그가 교황에게 쓴 글이에요.',
         '이 책의 라틴어가 바로 그가 옮긴 성경이라, 책이 옮긴 사람의 편지로 문을 여는 셈이에요. 그 뒤로 네 복음서의 같은 대목을 나란히 찾아보는 표가 이어져요.'],
   'see': '다섯째 장면의 큰 라틴어가, 맨 앞 편지를 쓴 히에로니무스가 옮긴 글로 보여요.', 'seeAt': 'gloss',
   'go': {'t': '「히에로니무스와 불가타 성경」 카드로 가기', 'cid': 'ob-vulgate'},
   'src': [{'t': '영국도서관 소장 목록: Cotton MS Nero D IV', 'm': '영어 · 2v쪽 첫 양탄자 쪽, 3r~5v쪽 히에로니무스가 교황 다마수스에게 쓴 편지(Novum opus), 머리말, 10r~17v쪽 대조표', 'u': BLCAT},
           {'t': 'Britannica: Vulgate', 'm': '영어 · 382년 교황 다마수스가 히에로니무스에게 표준 라틴어 성경을 맡김', 'u': BRIT},
           {'t': 'Smarthistory: The Lindisfarne Gospels', 'm': '영어 · 대조표: 네 복음서의 같은 대목을 나란히 놓음', 'u': SMART}]},
  {'id': 'pocket', 'pack': 3, 'q': '쿠스버트의 관 속에서 또 다른 책이 나왔다고요?', 'hook': '관 속의 작은 요한복음',
   'img': 'priory', 'pos': '25% 55%',
   'a': ['1104년 더럼 대성당에서 쿠스버트의 유해를 새 성소로 옮기려고 관을 열었을 때, 작은 요한복음 한 권이 나왔어요. 698년 무렵 관에 넣은 것으로 보여요.',
         '처음 만든 붉은 가죽 표지까지 그대로 남은, 유럽에서 가장 오래된 온전한 책이에요. 영국도서관이 2012년에 큰 모금으로 사들였어요.'],
   'see': '셋째 장면 수도사들이 메고 간 관이, 또 한 권의 복음서를 품은 관으로 보여요.', 'seeAt': 'leave',
   'src': [{'t': '영국도서관 블로그: St Cuthbert Gospel saved for the nation(2012)', 'm': '영어 · 요한복음 필사본, 유럽에서 가장 오래된 온전한 책, 처음의 붉은 가죽 표지, 698년 무렵 관에 넣음, 1104년 더럼 대성당에서 관을 열 때 발견, 영국도서관 역대 가장 큰 모금', 'u': BLCG}]},
  {'id': 'time', 'pack': 3, 'q': '259장을 혼자 쓰려면 얼마나 걸렸을까요?', 'hook': '본문만 6년쯤',
   'img': 'matthew', 'pos': '50% 75%',
   'a': ['미술사학자 우드빌은 에드프리스가 라틴어 본문을 베끼는 데만 6년쯤 걸렸을 거라고 봐요.',
         '영국도서관의 큐레이터 도일은 한 사람이 썼다는 데에는 학자들이 뜻을 모으지만, 그 사람이 주교 에드프리스라는 확실한 증거는 없다고 말해요.'],
   'see': '둘째 장면에서 글을 쓰는 마태가, 몇 해를 책상 앞에서 보낸 한 사람의 손으로도 보여요.', 'seeAt': 'scribe',
   'src': [{'t': 'Smarthistory: The Lindisfarne Gospels', 'm': '영어 · 우드빌의 글: 본문을 베끼는 데 6년쯤 · 도일의 영상: 한 사람이 썼다고 보지만 주교였다는 확실한 증거는 없음', 'u': SMART}]},
 ],
 'qcand': [   # 후보 모두(재벌 2026-11-22) — 열쇠는 pick, 뒷이야기는 x, 녹이거나 보낸 것은 at에
  {'q': '글자가 하나도 없는 이 쪽은 왜 만들었을까요?', 'at': '창 · 앞면 물음(답하지 않으면 낚였다고 느낌) · 악마의 대변인 B14 · 옛 ‘알고 보면’의 양탄자 페이지', 'a': '다섯 장, 맨 앞과 복음서마다 · 복음서마다 따로 여는 속표지(도일) · 묵상(우드빌) — 영국도서관 목록·Smarthistory', 'see': '앞면 카드가 복음서로 들어가는 무늬의 문으로 보여요.', 'pick': 1},
  {'q': '쿠스버트는 누구길래, 그 몸까지 들고 피난을 갔을까요?', 'at': '악마의 대변인 · B1·B2(무슨 일을 한 사람인지, 왜 몸을 들고 갔는지) · A(성인·주교) · 옛 ‘알고 보면’의 쿠스버트', 'a': '은수자·주교, 687년, 11년 뒤 썩지 않은 몸, 순례지, 가장 귀한 것으로 유해를 챙김 — 잉글리시 헤리티지·히스토리 투데이·더럼 세계유산', 'see': '셋째 장면의 피난길이 가장 귀한 것을 지키러 떠난 길로 보여요.', 'pick': 1},
  {'q': '영국에서 만든 책인데, 왜 라틴어로 썼을까요?', 'at': '악마의 대변인 · B8(왜 라틴어, 250년 동안 못 읽었나) · 옛 ‘줄 위의 영어 더 보기’', 'a': '히에로니무스의 불가타, 로마 교회가 6세기부터 두루 씀, 앨드레드의 낱말별 옛 영어, 가장 오래된 영어 복음서 — 브리태니커·남호주 주립도서관·Smarthistory', 'see': '다섯째 장면의 갈색 글씨가 가장 오래된 영어 복음서로 보여요.', 'pick': 1},
  {'x': 'sea', 'q': '바다에 빠진 복음서가 다시 돌아왔다고요?', 'at': '창 · 악마의 대변인 B3(일곱 해 동안 책이 젖지는 않았나)', 'a': '시므온: 아일랜드로 가던 배, 폭풍, 썰물 3마일 · 사흘 뒤 밀려옴(엔사이클로피디아 로마나) — 전설', 'see': '셋째 장면의 떠돎이 전설까지 품은 길로 보여요.'},
  {'x': 'angel', 'q': '마태 머리 위에서 나팔을 부는 날개 달린 사람은 누구예요?', 'at': '악마의 대변인 · C(날개 달린 나팔수, imagohominis와 큰 글자) · 둘째 장면 아이 물음의 답', 'a': '마태의 상징인 사람(비드), imago hominis, 하기오스 — Smarthistory·NLM', 'see': '둘째 장면의 날개 달린 사람이 마태복음의 상징으로 보여요.'},
  {'x': 'cat', 'q': '누가복음 첫 쪽 구석에 고양이가 숨어 있다고요?', 'at': '창 · 옛 ‘줄 위의 영어 더 보기’의 139r쪽 · 악마의 대변인 C(키로 쪽의 새 머리)', 'a': '새 여덟 마리를 삼킨 고양이, 왜가리 가슴의 쉼표가 고양이 앞발로 — Smarthistory', 'see': '키로 쪽의 짐승 머리도 같은 손으로 보여요(약해요).'},
  {'x': 'aldred', 'q': '앨드레드는 왜 은까지 내며 뜻풀이를 바쳤을까요?', 'at': '악마의 대변인 · B12(왜 요한복음은 자기 몫) · G(앨드레드라는 사람) · 옛 ‘알고 보면’의 은 8오라·프로보스트', 'a': '누가: 공동체에 들어가는 값 은 8오라 · 요한: 자기 몫, 은 4오라, 하늘나라 · 프로보스트 — Art of the Middle Ages·ASMMF', 'see': '다섯째 장면 여백의 글씨가 한 사제의 손글씨로 보여요.'},
  {'x': 'bill', 'q': '금과 보석으로 꾸민 겉표지는 지금도 남아 있어요?', 'at': '악마의 대변인 · B6·B7(에셀왈드와 빌프리스는 언제, 보석은 지금도) · A(빌프리스가 ‘한 사람’과 부딪침)', 'a': '빌프리스 = 겉 장식, 속은 에드프리스 · 바이킹 때 / 수도원 해산 때 — 자료마다 다름 · 금속 장신구를 닮은 양탄자 쪽', 'see': '넷째 장면의 금과 보석이 사라진 겉표지의 자리로 보여요.'},
  {'x': 'dragon', 'q': '바이킹이 오기 전, 하늘에 불 용이 날았다고요?', 'at': '창 · 셋째 장면의 793년(악마의 대변인 D: 그래서 뭐?)', 'a': '회오리바람·번개·불 용, 굶주림, 6월 8일, 온 유럽이 놀람, 앨퀸의 편지 — 잉글리시 헤리티지', 'see': '셋째 장면의 793년이 온 유럽을 놀라게 한 해로 보여요.'},
  {'x': 'dots', 'q': '누가복음 첫 쪽의 빨간 점은 모두 몇 개일까요?', 'at': '악마의 대변인 · C(키로 쪽의 수천 개 빨간 점)', 'a': '10,600개, 1분에 30개, 여섯 시간(백하우스) · NIAM 둘레 1,939개(영국도서관)', 'see': '다섯째 장면의 빨간 점이 긴 시간으로 보여요.'},
  {'x': 'chirho', 'q': '‘키로’ 쪽은 왜 이렇게 크게 꾸몄을까요?', 'at': '악마의 대변인 · A(‘키로’가 뭔지, 왜 1장 18절) · C(X와 P 글자) · 「켈스의 서」 카드로 길을 놓음', 'a': '키·로 = 그리스도의 첫 두 글자, 1장 18절에서 탄생 이야기 시작 · 켈스의 서 34r — 트리니티 칼리지·오니언타', 'see': '커다란 X와 P가 그리스도의 이름으로 보여요.'},
  {'x': 'paint', 'q': '이 색들은 무엇으로 만들었을까요?', 'at': '악마의 대변인 · C(양탄자 쪽의 물감)', 'a': '녹청·웅황·구운 납·달걀흰자 풀, 웅황에 잔금 — 영국도서관 보존 블로그', 'see': '앞면 카드의 색이 구리와 광물의 색으로 보여요.'},
  {'x': 'wander', 'q': '일곱 해 동안, 누가 관을 메고 떠돌았을까요?', 'at': '악마의 대변인 · B3(일곱 해 동안 어떻게 살았나) · G(일곱 해 떠돎)', 'a': '아내·아이들까지, 잉글랜드 북쪽 곳곳, 관 속의 오스왈드 왕 머리·에이단의 뼈, 883년 — 히스토리 투데이·잉글리시 헤리티지·더럼 세계유산', 'see': '셋째 장면의 피난길이 긴 행렬로 보여요.'},
  {'x': 'road', 'q': '둑길이 생기기 전에는 어떻게 섬에 건너갔을까요?', 'at': '악마의 대변인 · C(둑길이 요즘 도로, 길가의 기둥)', 'a': '1954년 둑길, 그 전에는 기둥이 안전한 길, 순례자의 길, 피난 탑 — 지오그래프', 'see': '첫째 장면의 길이 1954년에 생긴 새 길로 보여요.'},
  {'x': 'london', 'q': '이 책은 어떻게 런던까지 갔을까요?', 'at': '악마의 대변인 · B15(지금 어디 있나, 볼 수 있나) · 「대영도서관 보물실」 카드로 길을 놓음', 'a': '더럼 995 → 헨리 8세 → 코튼 → 1731년 불에도 무사 → 1753년 영국박물관 → 영국도서관', 'see': '섬에서 런던까지의 길로 보여요.'},
  {'x': 'letter', 'q': '이 책의 맨 앞은 복음서가 아니라 편지라고요?', 'at': '창 · 열쇠 셋째(라틴어)에서 이어짐 · 「히에로니무스와 불가타 성경」 카드로 길을 놓음', 'a': '2v 첫 양탄자 쪽, 3r 히에로니무스가 교황 다마수스에게 쓴 편지, 대조표 — 영국도서관 목록·브리태니커', 'see': '다섯째 장면의 라틴어가 히에로니무스가 옮긴 글로 보여요(약해요).'},
  {'x': 'pocket', 'q': '쿠스버트의 관 속에서 또 다른 책이 나왔다고요?', 'at': '창 · 열쇠 둘째(쿠스버트의 관)에서 이어짐', 'a': '1104년 관을 열 때 나온 요한복음, 698년 무렵, 처음 표지 그대로, 가장 오래된 온전한 책, 2012년 영국도서관 — 영국도서관 블로그', 'see': '셋째 장면의 관이 또 한 권의 복음서를 품은 관으로 보여요.'},
  {'x': 'time', 'q': '259장을 혼자 쓰려면 얼마나 걸렸을까요?', 'at': '악마의 대변인 · B4(주교가 259장을 직접 썼다면 얼마나)', 'a': '본문만 6년쯤(우드빌), 한 사람이지만 주교라는 확실한 증거는 없음(도일) — Smarthistory', 'see': '둘째 장면의 마태가 한 사람의 긴 손일로 보여요(약해요).'},
  {'q': '앨드레드는 250년 뒤 사람인데 어떻게 알았고, 믿을 만해요?', 'at': '악마의 대변인 · B5 · ‘기록마다 다른 점’의 ‘네 사람’에 이미 있음', 'a': '맺음말은 대체로 맞고 믿을 만한 기록으로 여김 — ASMMF 206', 'see': '넷째 장면의 맺음말이 학자들이 믿는 기록으로 보여요.'},
  {'q': '에셀왈드와 빌프리스는 같이 일했나요, 나중에 했나요?', 'at': '악마의 대변인 · B6 · 셋째 장면(‘그 뒤를 이은 주교 에셀왈드’)과 ‘기록마다 다른 점’(에셀왈드)에 녹임', 'a': '에셀왈드는 에드프리스의 다음 주교(엔사이클로피디아 로마나·EWTN 주교 목록) · 시므온은 남에게 맡겨 묶게 했다고 적음(ASMMF)', 'see': '셋째 장면의 뼈 두 사람이 앞뒤 주교로 보여요.'},
  {'q': 'god과 spell을 합치면 정말 ‘좋은 이야기’예요?', 'at': '악마의 대변인 · B10 · 다섯째 장면에 이미 있음(Etymonline)', 'a': '옛 영어 godspel = 좋은 이야기 — Etymonline', 'see': '맨 위의 godspell이 좋은 이야기로 보여요.'},
  {'q': '복음서는 뭐고, 왜 넷이에요?', 'at': '악마의 대변인 · A · 둘째 장면에 길잡이 한 줄로 녹임(왜 넷인지는 다루지 않음)', 'a': '예수님의 삶과 가르침을 적은 책, 마태·마가·누가·요한 — Smarthistory(도일)', 'see': '둘째 장면의 마태가 네 권 가운데 한 권을 쓴 사람으로 보여요.'},
  {'q': '25v, 259r 같은 쪽 번호의 v와 r은 뭐예요?', 'at': '악마의 대변인 · A · 둘째 장면에 길잡이 한 줄로 녹임', 'a': 'r은 장의 앞면, v는 뒷면 — 노팅엄 대학 필사본 안내', 'see': '그림 아래 쪽 번호가 장의 앞뒤로 보여요.'},
  {'q': '그림 속 휘장 뒤에서 내다보는 사람은 누구예요?', 'at': '악마의 대변인 · C · 답을 찾지 못한 물음(블로그의 짐작만 있음)', 'a': '정해진 답을 찾지 못함 — 데이비드 클레이턴(NLM 2015)도 모른다고 적음', 'see': '둘째 장면 휘장 뒤의 사람이 아직 풀리지 않은 수수께끼로 보여요(약해요).'},
  {'q': '날개 달린 사람은 왜 나팔을 불어요?', 'at': '악마의 대변인 · C · 답을 찾지 못한 물음', 'a': '근거를 찾지 못함', 'see': '없음'},
  {'q': '양탄자 쪽의 하얀 동그라미 여섯 개는 뭐예요?', 'at': '악마의 대변인 · C · 답을 찾지 못한 물음', 'a': '근거를 찾지 못함', 'see': '없음'},
  {'q': '앨드레드는 왜 스스로를 ‘가장 비참한 사제’라고 불렀어요?', 'at': '악마의 대변인 · B11 · 답을 찾지 못한 물음', 'a': '근거를 찾지 못함', 'see': '없음'},
  {'q': '귀한 책에 글씨를 덧써도 괜찮았어요?', 'at': '악마의 대변인 · B9 · 답을 찾지 못한 물음(의견 글만 있음)', 'a': '근거를 찾지 못함', 'see': '없음'},
  {'q': '색을 칠하지 않은 큰 글자들은 덜 끝낸 거예요?', 'at': '악마의 대변인 · C · ‘기록마다 다른 점’의 ‘덜 끝낸 곳’에 녹임(이 글자들을 콕 집은 근거는 없음)', 'a': '덜 끝낸 곳이 있다 — 마치지 못했다 / 일부러 완벽을 피했다(백하우스, lindisfarne.org.uk)', 'see': '다섯째 장면의 빈 글자가 풀리지 않은 자리로 보여요(약해요).'},
 ],
 'deep': [
  {'h': '기록마다 다른 점', 'p': [
    '<b>만든 해</b> 715년 무렵으로 보는 학자가 많지만, 700년 무렵이나 698년 이전으로 보는 학자도 있어요.',
    '<b>보석 표지</b> 빌프리스가 꾸민 처음 표지는 남아 있지 않아요. 바이킹 시대에 잃었다는 설명도, 16세기에 수도원들이 문을 닫을 때 잃었다는 설명도 있어요. 지금의 은빛 표지는 1852~1853년 더럼 주교 에드워드 몰트비가 돈을 내 새로 만든 거예요.',
    '<b>에셀왈드</b> 앨드레드는 에셀왈드가 손수 책을 묶고 겉을 씌웠다고 적었어요. 12세기 더럼의 시므온은 그가 남에게 맡겨 묶게 했다고 적었어요.',
    '<b>덜 끝낸 곳</b> 무늬 몇 군데는 덜 끝나 있거나 둘레와 어울리지 않아요. 에드프리스가 책을 마치지 못하고 세상을 떠났다고 보는 학자도 있고, 빈틈이 너무 작아 일부러 완벽을 피한 겸손이었을 거라고 보는 연구자(재닛 백하우스)도 있어요.',
    '<b>네 사람</b> 앨드레드는 250년쯤 뒤의 사람이에요. 그래도 학자들은 그의 맺음말을 대체로 맞고 믿을 만한 기록으로 여겨요.']},
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
  {'l': 'Anglo-Saxon Manuscripts in Microfiche Facsimile 206번: 875년 에아르둘프와 떠난 일, 883~995년 체스터르스트리트, 970년 프로보스트 앨드레드, 1852~1853년 표지, 시므온의 바다 전설과 ‘남에게 맡겨 묶게 함’, 1731년 불에도 무사, 1753년 영국박물관', 'u': SFU},
  {'l': 'Ancient History Sites: 체스터르스트리트 성 마리아·성 쿠스버트 교회 — 일곱 해 떠돎, 883년 정착, 옛 로마 요새, 나무 교회, 1056년 돌 교회', 'u': 'https://www.ancient-history-sites.com/?p=122606'},
  {'l': 'Catholic Answers 백과(옛 가톨릭 백과): 린디스판 — 635년 아이오나에서 온 에이단', 'u': 'https://www.catholic.com/encyclopedia/diocese-and-monastery-of-lindisfarne'},
  {'l': 'EWTN 백과: 린디스판 — 875년 바이킹이 다시 왔을 때 쿠스버트의 유해와 떠난 수도사들, 마지막 주교 에아르둘프, 주교 목록(에드프리스 698 → 에셀왈드 724)', 'u': 'https://www.ewtn.com/catholicism/library/ancient-diocese-and-monastery-of-lindisfarne-10603'},
  {'l': 'Visit Northumberland: 홀리 아일랜드 둑길 — 하루 두 번 밀물에 끊기는 섬', 'u': 'https://visitnorthumberland.com/coast/holy-island/crossing-times'},
  {'l': 'Geograph: 린디스판 수도원 터 — 793년 바이킹, 지금 남은 폐허는 1093년 뒤 다시 세운 수도원', 'u': 'https://www.geograph.org.uk/photo/6850326'},
  {'l': 'Etymonline: gospel — 옛 영어 godspel, ‘좋은 이야기’', 'u': 'https://www.etymonline.com/word/gospel'},
  {'l': 'History Hit: 린디스판 복음서 10가지 — 처음 표지는 바이킹 시대에 잃었을 것, 1852년 몰트비 주교의 새 표지', 'u': 'https://www.historyhit.com/facts-about-the-lindisfarne-gospels'},
  {'l': 'English Heritage: History of Lindisfarne Priory — 은수자 쿠스버트, 685년 주교, 687년 3월 20일, 11년 뒤 썩지 않은 몸, 관을 올린 성소와 기적·순례, 복음서는 쿠스버트 숭배에서 나옴, 793년 6월 8일, 앨퀸의 편지, 오스왈드 왕이 섬을 내줌', 'u': EH},
  {'l': 'English Heritage: The Viking Raid on Lindisfarne — 793년 초의 회오리바람·번개·불 용, 굶주림, 6월 8일', 'u': EHV},
  {'l': 'History Today: St Cuthbert Reburied in Durham Cathedral — 비드가 전한 잠든 듯한 몸, 아내·아이들과 일곱 해, 관 속의 오스왈드 왕 머리와 에이단의 뼈', 'u': HT},
  {'l': 'Durham World Heritage Site: The Body of Cuthbert — 698년, 몰려든 순례자, 존경받고 부유했지만 바이킹의 표적, 875~883년', 'u': DWHS},
  {'l': '더럼의 시므온이 쓴 더럼 교회의 역사(12세기 초, 영어 번역 · ecatholic2000) — 바다에 빠진 복음서 이야기', 'u': SYM},
  {'l': 'Encyclopaedia Romana(시카고 대학): Lindisfarne Gospels — 양탄자 쪽 다섯 장, 에셀왈드는 에드프리스의 후임, 사흘 뒤 밀려온 책, 표지를 잃은 때, 헨리 8세와 코튼', 'u': PEN},
  {'l': '영국도서관 보존 블로그(2013): Under the microscope with the Lindisfarne Gospels — 구운 납의 붉은 점, NIAM 둘레 1,939개, 녹청·웅황·글레어, 잔금', 'u': BLCC},
  {'l': 'Lindisfarne.org.uk: The Lindisfarne Gospels(재닛 백하우스의 글) — 붉은 점 10,600개·여섯 시간, 덜 끝낸 곳', 'u': BACK},
  {'l': '영국도서관 블로그(2012): St Cuthbert Gospel saved for the nation — 관 속의 요한복음', 'u': BLCG},
  {'l': 'FutureLearn · 더블린 트리니티 칼리지: 키(χ)와 로(ρ), 켈스의 서 34r쪽', 'u': TCD},
  {'l': 'SUNY 오니언타 미술사 강의 자료: 켈스의 서 키로 쪽과 마태복음 1장 18절', 'u': ONE},
  {'l': 'Britannica: Vulgate — 382년 다마수스가 맡김, 6세기 중반부터 두루 씀, 로마 교회의 라틴어 성경', 'u': BRIT},
  {'l': '남호주 주립도서관 디지털 컬렉션: 린디스판 복음서 — 히에로니무스의 불가타, 가장 오래된 영어 복음서 번역', 'u': SLSA},
  {'l': "Geograph: Holy Island Sands, Refuge on the Lindisfarne Pilgrims' Path — 1954년 둑길, 기둥과 피난 탑", 'u': GEOP},
  {'l': '노팅엄 대학 필사본 안내: Forming quires — r(앞면)·v(뒷면)', 'u': NOTT},
  {'l': 'New Liturgical Movement(2015): St Matthew the Evangelist from the Lindisfarne Gospels — imago hominis, 하기오스', 'u': NLM},
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
   'lines': [{'t': '715년 무렵, 이 책의 글과 그림을 한 사람이 다 했다고 학자들은 봐요.'}, {'t': '아마 주교 에드프리스예요. 그림 속 인물은 마태복음을 썼다는 마태고요.'}],
   'kid': [{'t': '한 사람이 이 큰 책을 다 쓰고 그렸대.'}, {'t': '마태 아저씨는 무엇을 하고 있어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '섬을 떠나다'},
  {'type': 'img', 'ch': 3, 'img': 'church', 'fit': 'cover', 'p0': '50% 40%', 'p1': '50% 60%', 's0': 1.15, 's1': 1.0, 'cap': '체스터르스트리트의 교회',
   'lines': [{'t': '875년, 바이킹을 피해 수도사들이 섬을 떠났어요.'}, {'t': '쿠스버트의 유해와 이 책을 들고서요. 883년, 체스터르스트리트에 닿았어요.'}],
   'kid': [{'t': '수도사들이 성인의 관이랑 책을 들고 섬을 떠났대.'}, {'t': '일곱 해 동안 어디를 떠돌았을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '책 끝의 네 사람'},
  {'type': 'mod', 'mod': 'place', 'ch': 4,
   'lines': [{'t': '970년 무렵, 사제 앨드레드가 책 끝 빈자리에 적어요.'},
             {'t': '에드프리스가 처음에 이 책을 썼고,', 'act': 'write'}, {'t': '에셀왈드가 책을 묶어 겉을 씌웠고,', 'act': 'bind'},
             {'t': '빌프리스가 겉표지를 금과 보석으로 꾸몄고,', 'act': 'lights', 'wait': 1500}, {'t': '나 앨드레드가 줄 위에 영어로 뜻을 적었어요.', 'act': 'gloss'},
             {'t': '살아 계신 하나님, 이 네 사람을 기억하소서.', 'q': True, 'from': '앨드레드의 여백 글에서', 'act': 'day', 'wait': 1500}],
   'kid': [{'t': '책 끝에 네 사람이 적혀 있어.'}, {'t': '쓰고!', 'act': 'write'}, {'t': '묶고!', 'act': 'bind'},
           {'t': '반짝반짝 꾸미고!', 'act': 'lights', 'wait': 1500}, {'t': '영어로 뜻을 달았어!', 'act': 'gloss'},
           {'t': '책이 다 됐어!', 'act': 'day', 'wait': 1500}]},
  {'type': 'chapter', 'ch': 5, 'no': 5, 't': '줄 위의 영어'},
  {'type': 'img', 'ch': 5, 'img': 'chirho', 'fit': 'cover', 'p0': '30% 8%', 'p1': '45% 20%', 's0': 2.2, 's1': 1.5, 'o': '35% 8%', 'cap': '29r쪽, 큰 글자 위의 작은 뜻풀이',
   'lines': [{'t': '큰 라틴어 위의 작은 갈색 글씨, 앨드레드가 적은 옛 영어예요.'}, {'t': '맨 위의 godspell은 ‘좋은 이야기’, 오늘의 gospel이에요.'}],
   'kid': [{'t': '큰 글자 위에 작은 글씨가 보여?'}, {'t': '‘좋은 이야기’를 우리말로 하면?', 'ask': True}]},
  {'type': 'imagine', 'ch': 6,
   'lines': [{'t': '강가 마을의 작은 교회 곁, 늙은 사제가 무거운 책을 펼쳐요.'}, {'t': '사각사각 펜 소리, 오래된 가죽 냄새.'}, {'t': '그는 맨 끝에 이름을 하나씩 적어 내려가요.'}],
   'kid': [{'t': '눈을 감아 봐. 할아버지 수도사가 책을 펼쳐.'}, {'t': '사각사각, 이름을 하나씩 적어.'}]},
  {'type': 'reward', 'ch': 6},
 ],
}
