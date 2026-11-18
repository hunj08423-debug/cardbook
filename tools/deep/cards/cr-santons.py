# -*- coding: utf-8 -*-
"""깊은 카드: 프로방스 상통(cr-santons) · 중심 방식 = 만드는 차례(+두 그림 나란히)
기준서 2판 · 틀 deep3-5 · 키트 3판 보탬 2 · 2026-11-18 6번 묶음 창(창 6)이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 프로방스의 상통 공방에서, 몸무게를 실어 눌러 닫은 석고 틀 두 쪽을 열면
     흙으로 된 작은 사람 하나가 나오는 때(프랑스 문화부 무형문화유산 목록의 ‘만드는 차례’)
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 문화부 목록에 적힌 상통 만드는 차례
     → 만드는 차례(빚기 → 석고 어미 틀 → 흙 눌러 넣기 → 쇠막대 넣고 꺼내기 → 말리기 → 다듬기 → 굽기 → 살빛 → 옷과 모자)
끝맺는 꼴: 그 사람 안에 들어가 보기 · 드릴 것이 없어 기쁨과 웃음만 가지고 온, 두 팔을 든 ‘라비’(마르세유 관광청 · 문화부 목록)
5단계: 아이와 함께 끝까지 보기
카드 크기: 큰 카드(장면 3개) — 자유롭게 쓸 그림이 세 장(라녤의 틀 · 19세기 장터 판화 · 20세기 초 그림엽서)이라
  장면을 넷으로 늘리지 않았어요. 만드는 차례 그림은 이 안내서가 그렸어요(아래 svg()).
그림 원본(src)은 deep_src/cr-santons/ (저장소 밖). 받는 법: commons_get.py"""
S = 'cr-santons/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

WET, DRY, FIRED = '#8d7a63', '#cbb593', '#c4714a'
SKIN, SHIRT, VEST, PANTS, SOCK, SHOE, CAP = '#efc6a2', '#f5f1e8', '#3f6a58', '#7a5232', '#ece5d4', '#3b2a1f', '#b8352b'


def body(c, mask=False):
    """두 팔을 든 라비의 몸(한 가지 색). mask=True면 흰색으로(굽기 덮개용)."""
    f = '#fff' if mask else c
    arm = f'stroke="{f}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    leg = f'stroke="{f}" stroke-width="15" stroke-linecap="round" fill="none"'
    return (f'<path d="M131 141 L110 116 L101 80" {arm}/><path d="M169 141 L190 116 L199 80" {arm}/>'
            f'<circle cx="100" cy="74" r="8.5" fill="{f}"/><circle cx="200" cy="74" r="8.5" fill="{f}"/>'
            f'<path d="M141 212 L139 268 L137 306" {leg}/><path d="M159 212 L161 268 L163 306" {leg}/>'
            f'<path d="M126 136 Q150 128 174 136 L170 214 Q150 220 130 214 Z" fill="{f}"/>'
            f'<rect x="143" y="118" width="14" height="16" rx="5" fill="{f}"/>'
            f'<circle cx="150" cy="104" r="19" fill="{f}"/>'
            f'<ellipse cx="135" cy="309" rx="11" ry="6" fill="{f}"/><ellipse cx="165" cy="309" rx="11" ry="6" fill="{f}"/>'
            f'<rect x="112" y="310" width="76" height="16" rx="6" fill="{f}"/>')


def half_mold(x0, mirror=False):
    """석고 틀 한 쪽: 둥근 지붕 모양 덩이와 그 안의 오목한 사람 모양."""
    cx = x0 + 62
    s = (f'<path d="M{x0} 334 L{x0} 120 Q{x0} 40 {cx} 40 Q{x0 + 124} 40 {x0 + 124} 120 L{x0 + 124} 334 Z" fill="#f1eee6" stroke="#cfc8b8" stroke-width="2"/>'
         f'<path d="M{x0 + 8} 330 L{x0 + 8} 122 Q{x0 + 8} 50 {cx} 50" stroke="#fff" stroke-width="3" fill="none" opacity=".7"/>')
    k = .66
    # 오목한 자리(사람 모양을 줄여 그림)
    hollow = (f'<g transform="translate({cx - 150 * k:.1f} {63:.1f}) scale({k}){" translate(300 0) scale(-1 1)" if mirror else ""}">'
              f'{body("#c9c1ae")}</g>')
    return s + hollow


def clay_in(x0, mirror=False):
    cx = x0 + 62; k = .66
    return (f'<g transform="translate({cx - 150 * k:.1f} {63:.1f}) scale({k}){" translate(300 0) scale(-1 1)" if mirror else ""}">'
            f'{body(WET)}</g>')


def svg(uid='sn'):
    seam = ('<path d="M150 82 Q172 86 170 110 M131 141 L110 116 L101 80 M169 141 L190 116 L199 80 M128 138 L131 214 M172 138 L169 214 '
            'M139 214 L137 306 M161 214 L163 306" stroke="#e6d8bf" stroke-width="2.2" fill="none" stroke-dasharray="3 3" opacity=".9"/>')
    s = (f'<svg viewBox="0 0 300 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="이 안내서가 그린 상통 라비. 흙 한 덩이가 단계마다 빚어지고, 석고 틀에서 찍혀 나와 마르고, 구워지고, 칠해진다.">'
         f'<defs><mask id="{uid}M" maskUnits="userSpaceOnUse" x="0" y="0" width="300" height="360"><rect width="300" height="360" fill="#000"/>{body("", True)}</mask>'
         f'<radialGradient id="{uid}K" cx=".5" cy=".55" r=".55"><stop offset="0" stop-color="#ffb35c" stop-opacity=".55"/><stop offset=".6" stop-color="#ff8a3c" stop-opacity=".18"/><stop offset="1" stop-color="#ff7a2c" stop-opacity="0"/></radialGradient>'
         f'<radialGradient id="{uid}S" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffe7a3"/><stop offset="1" stop-color="#ffcf6a" stop-opacity="0"/></radialGradient></defs>'
         # 작업대
         '<rect x="14" y="326" width="272" height="16" rx="4" fill="#a8825a"/><rect x="14" y="340" width="272" height="8" rx="3" fill="#7d5b3c"/>'
         # 0단계: 흙 한 덩이
         f'<g data-off="1"><path d="M112 326 Q104 300 124 290 Q150 278 178 290 Q198 300 188 326 Z" fill="{WET}"/>'
         '<path d="M126 298 Q148 288 170 296" stroke="#a8957c" stroke-width="2.4" fill="none" opacity=".7"/></g>'
         # 1단계: 손으로 빚은 본(흙 그대로)과 도구
         f'<g data-s="1" data-off="2">{body(WET)}<path d="M150 87 Q160 90 162 100" stroke="#a8957c" stroke-width="2" fill="none" opacity=".6"/></g>'
         '<g data-s="1" data-off="2"><path d="M222 322 L276 300" stroke="#b58d5e" stroke-width="5" stroke-linecap="round"/><ellipse cx="279" cy="299" rx="7" ry="3.5" fill="#b58d5e" transform="rotate(-22 279 299)"/>'
         '<path d="M26 322 L72 306" stroke="#7d8790" stroke-width="3.5" stroke-linecap="round"/><path d="M72 306 l8 -5" stroke="#7d8790" stroke-width="2" stroke-linecap="round"/></g>'
         # 2단계: 석고 어미 틀 두 쪽(3단계에 흙이 들어가고 4단계에 치워져요)
         f'<g data-s="2" data-off="4">{half_mold(22)}{half_mold(154, True)}</g>'
         f'<g data-s="3" data-off="4">{clay_in(22)}{clay_in(154, True)}'
         '<path d="M150 18 L150 34 M142 27 L150 35 L158 27" stroke="#8a6a4a" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".7"/></g>'
         # 4단계: 틀에서 꺼낸 젖은 흙 상통(이음매가 남고, 쇠막대가 몸을 받쳐요)
         f'<g data-s="4">{body(WET)}</g>'
         '<g data-s="4" data-off="6"><line x1="150" y1="96" x2="150" y2="318" stroke="#5f6870" stroke-width="2.2" stroke-dasharray="6 5" opacity=".5"/></g>'
         f'<g data-s="4" data-off="6">{seam}</g>'
         # 5단계: 바람에 말라 빛깔이 밝아져요
         f'<g data-s="5">{body(DRY)}</g>'
         f'<g data-s="5" data-off="6"><circle cx="252" cy="58" r="26" fill="url(#{uid}S)"/><circle cx="252" cy="58" r="11" fill="#ffd77a"/></g>'
         f'<g data-s="5" data-off="6">{seam}</g>'
         # 6단계: 칼·붓·사포로 다듬기(도구가 잠깐 보여요)
         '<g data-s="6" data-off="7"><path d="M30 318 L70 296" stroke="#9aa3ab" stroke-width="4" stroke-linecap="round"/><path d="M70 296 L84 289" stroke="#6b4a2b" stroke-width="6" stroke-linecap="round"/>'
         '<path d="M232 320 L268 286" stroke="#a8825a" stroke-width="4" stroke-linecap="round"/><path d="M268 286 l7 -7 l4 4 l-7 7z" fill="#5a4636"/>'
         '<rect x="236" y="300" width="30" height="18" rx="2" fill="#d9c79f" transform="rotate(-12 251 309)"/></g>'
         # 7단계: 가마에서 굽기 — 구운 흙빛이 아래에서부터 차올라요
         f'<g data-s="7" data-off="8"><ellipse cx="150" cy="200" rx="140" ry="160" fill="url(#{uid}K)"/></g>'
         f'<g mask="url(#{uid}M)"><rect class="dye" data-s="7" x="0" y="0" width="300" height="360" fill="{FIRED}"/></g>'
         # 8단계: 살빛(얼굴과 손)
         f'<g data-s="8"><circle cx="150" cy="104" r="19" fill="{SKIN}"/><rect x="143" y="118" width="14" height="14" rx="5" fill="{SKIN}"/>'
         f'<circle cx="100" cy="74" r="8.5" fill="{SKIN}"/><circle cx="200" cy="74" r="8.5" fill="{SKIN}"/></g>'
         # 9단계: 속옷·셔츠 → 겉옷 → 모자 차례로
         f'<g data-s="9">'
         f'<path d="M141 260 L139 268 L137 306" stroke="{SOCK}" stroke-width="15" stroke-linecap="round" fill="none"/><path d="M159 260 L161 268 L163 306" stroke="{SOCK}" stroke-width="15" stroke-linecap="round" fill="none"/>'
         f'<path d="M131 141 L110 116 L103 88" stroke="{SHIRT}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M169 141 L190 116 L197 88" stroke="{SHIRT}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
         f'<path d="M126 136 Q150 128 174 136 L171 196 Q150 202 129 196 Z" fill="{SHIRT}"/>'
         f'<path d="M126 136 L138 132 L144 190 Q136 192 129 190 Z" fill="{VEST}"/><path d="M174 136 L162 132 L156 190 Q164 192 171 190 Z" fill="{VEST}"/>'
         f'<path d="M129 190 Q150 198 171 190 L170 214 Q150 220 130 214 Z" fill="{PANTS}"/>'
         f'<path d="M141 212 L140 262" stroke="{PANTS}" stroke-width="15" stroke-linecap="round" fill="none"/><path d="M159 212 L160 262" stroke="{PANTS}" stroke-width="15" stroke-linecap="round" fill="none"/>'
         f'<ellipse cx="135" cy="309" rx="11" ry="6" fill="{SHOE}"/><ellipse cx="165" cy="309" rx="11" ry="6" fill="{SHOE}"/>'
         f'<path d="M140 131 Q150 138 160 131 L156 140 Q150 143 144 140 Z" fill="{CAP}" opacity=".9"/>'
         f'<path d="M131 98 Q132 76 150 74 Q170 74 170 98 Q150 90 131 98 Z" fill="{CAP}"/><circle cx="168" cy="80" r="4" fill="{CAP}"/>'
         '<circle cx="143" cy="106" r="1.8" fill="#4a3426"/><circle cx="157" cy="106" r="1.8" fill="#4a3426"/>'
         '<path d="M143 115 Q150 121 157 115" stroke="#7a3b2c" stroke-width="2" fill="none" stroke-linecap="round"/>'
         '<circle cx="139" cy="112" r="3" fill="#e48a74" opacity=".45"/><circle cx="161" cy="112" r="3" fill="#e48a74" opacity=".45"/>'
         '</g>'
         '</svg>')
    return s


FICHE = 'https://www.culture.gouv.fr/fr/Media/Medias-creation-rapide/Les-savoir-faire-des-santonniers-de-Provence-Bouches-du-Rhone-VD.pdf'
OTM = 'https://www.marseille-tourisme.com/decouvrez-marseille/traditions/les-santons-en-provence/'
FT = 'https://francetoday.com/culture/the_santons_of_provence/'
FOIRE = 'https://www.myprovence.fr/agenda/foire-salon/marseille/224e-foire-aux-santons-et-aux-creches-de-marseille'
CMS = 'https://commons.wikimedia.org/wiki/File:'

STEPS = [
 {'do': '손으로 빚기', 't': '처음 본 빚기', 'p': '장인은 먼저 흙으로 인형을 손으로 빚어요. 나무나 쇠로 손수 만든 도구를 써요. 마음에 들지 않으면 다시 빚어요.'},
 {'do': '석고 틀 뜨기', 't': '어미 틀', 'p': '빚은 인형으로 석고 틀을 떠요. 이 ‘어미 틀’ 하나로 상통을 300~400개쯤 찍어 낼 수 있어요.'},
 {'do': '흙 눌러 넣기', 't': '두 쪽에 흙을 꾹', 'p': '틀 두 쪽에 보드라운 활석 가루를 바르고 흙을 넣어요. 그리고 몸무게를 실어 꾹 눌러 틀을 닫아요.'},
 {'do': '쇠막대 넣고 꺼내기', 't': '틀에서 꺼내기', 'p': '삐져나온 흙을 걷어 내고, 상통의 몸 길이만큼 쇠막대를 꽂아 단단하게 해요. 그다음 틀에서 꺼내요.'},
 {'do': '바람에 말리기', 't': '말리기', 'p': '바람이 통하는 곳에서 말려요. 크기와 철, 습기에 따라 닷새에서 몇 주까지 걸려요.'},
 {'do': '이음매 다듬기', 't': '다듬기', 'p': '틀 두 쪽이 만난 자리에 생긴 흙 테두리를 칼로 걷어 내요. 붓과 물로 매끈하게 다듬고, 받침은 사포로 문질러요.'},
 {'do': '가마에 굽기', 't': '굽기', 'p': '도자기 가마에 넣어요. 열두 시간에 걸쳐 980°C까지 온도를 올리고, 이틀쯤 천천히 식혀요.'},
 {'do': '살빛 칠하기', 't': '살빛부터', 'p': '물감은 손으로 한 색씩 칠해요. 맨 먼저 얼굴과 손의 살빛이에요.'},
 {'do': '옷과 모자 칠하기', 't': '속옷 → 셔츠 → 겉옷 → 모자', 'p': '살빛 다음은 속옷, 셔츠, 겉옷, 모자 차례예요. 칠은 흔히 칠하는 사람이 따로 맡고, 집에서 칠하기도 해요. 다 칠하면 팔 준비가 끝나요.'},
]

CARD = {
 'id': 'cr-santons', 'mode': '만드는 차례 · 두 그림',
 'pagetitle': '작은 성인',
 'brandsub': '깊은 카드 · 만드는 차례',
 'where': '<b>1800년 무렵부터</b><span>프랑스 프로방스 · 마르세유</span>',
 'lead': '프로방스 사람들은 구유 인형을 ‘상통’이라고 불러요. ‘작은 성인’이라는 뜻이에요. 흙으로 빚어 석고 틀로 찍어 내고, 굽고, 한 색씩 칠해 만들어요. 두 팔을 번쩍 든 ‘라비’를 차례대로 만들어 보세요.',
 'leadKid': '프로방스에는 흙으로 만든 작은 구유 인형이 있대. 두 팔을 번쩍 든 라비를 같이 만들어 볼까?',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 2판). 장면에는 기록에 있는 것만 옮겼어요. 만드는 차례 그림은 프랑스 문화부 무형문화유산 목록의 차례를 따라 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 # 화면 색: 프로방스의 구운 흙빛
 'theme': """:root{--accent:#8a5a2b;--accent-ink:#fffaf5;--soft:rgba(138,90,43,.09);--stamp:#a8392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#c2a991;--accent-ink:#17110b;--soft:rgba(194,169,145,.10);--stamp:#e46e5c}}
:root[data-theme="dark"]{--accent:#c2a991;--accent-ink:#17110b;--soft:rgba(194,169,145,.10);--stamp:#e46e5c}""",
 'stamp': {'t': '상통', 'y': '1803', 'sub': '마르세유 · 프로방스'},
 'doneNote': '프로방스 구유를 만나면, 두 팔을 든 라비를 찾아보세요.',
 'images': {
  # 'card'는 사이트 앞면 그림 그대로예요(카드 앞면에만 나와요). 요즘 만든 상통이라 장면·영화에는 옛 틀과 옛 그림을 썼어요(본부 소식 8번).
  'molds': {'src': S + 'Moule_de_Lagnel.jpg', 'cap': '장루이 라녤의 상통 틀 · 마르셀 카르보넬 상통 박물관',
            'cr': '사진: Philippe Renoux-Carbonel · CC BY-SA 3.0 · 위키미디어 공용', 'u': CMS + 'Moule_de_Lagnel.jpg',
            'alt': '나무 벽 진열장 두 칸에 둥근 지붕 모양의 하얀 석고 틀들이 서 있다. 틀은 두 쪽으로 열려 있고 안쪽에 사람 모양이 오목하게 파여 있다. 틀 사이에 구운 흙빛 상통들이 서 있고, 아래 칸 가운데에는 남자 상통 하나가 큰 틀 두 쪽 사이에 서 있다.'},
  'fair': {'src': S + 'Foire_aux_santons_Marseille_dessin_de_M.Crapelet.jpg', 'max': 1200, 'big': False,
           'cap': '마르세유의 상통 장터 · 19세기 중엽 · 크라플레의 그림을 새긴 판화',
           'cr': '그림: M. 크라플레 · 퍼블릭 도메인 · 위키미디어 공용', 'u': CMS + 'Foire_aux_santons_à_Marseille_dessin_de_M.Crapelet.jpg',
           'alt': '색을 입힌 옛 판화. 하얀 길가에 지붕 달린 가게들이 줄지어 있고, 넓은 치마를 입은 여인들과 모자를 쓴 남자들, 아이들이 오간다. 왼쪽 가게 위에 삼색기가 걸려 있고, 잎을 떨군 큰 나무들이 길을 따라 서 있다.'},
  'postcard': {'src': S + 'Cr_che_proven_ale_lou_boumian_margarido_et_lou_ravi.jpg', 'max': 1200, 'big': False,
               'cap': '보미앙, 마르가리도, 라비 · 20세기 초 마르세유 그림엽서',
               'cr': '그림엽서 · 퍼블릭 도메인 · 위키미디어 공용', 'u': CMS + 'Crèche_provençale_lou_boumian,_margarido_et_lou_ravi.jpg',
               'alt': '빛바랜 그림엽서. 받침 위에 선 상통 셋: 망토를 두르고 챙 넓은 모자를 쓴 수염 난 남자, 모자를 쓰고 바구니와 우산을 든 할머니, 줄무늬 모자를 쓰고 한 손에 등불을 든 젊은이. 왼쪽 위에 우표와 소인이 찍혀 있다.'},
 },
 'scenes': [
  {'id': 'little', 'label': '작은 성인의 틀', 'kind': 'photo', 'img': 'molds',
   'text': ['프로방스 말로 ‘상통’은 ‘작은 성인’이라는 뜻이에요. ‘성인’이라는 말에 ‘작은’을 뜻하는 꼬리를 붙인 낱말이에요.',
            '프로방스 사람들은 집 안에 작은 구유를 차렸어요. 프랑스 문화부 목록에 따르면, 집 구유가 처음 글에 나오는 것은 1692년이에요.',
            '1800년 무렵, 마르세유의 장루이 라녤(1764~1822)은 이 인형을 흙으로 만들었어요. 흙은 틀로 찍어 내기 좋아서 같은 인형을 여럿 만들 수 있었어요. 라녤의 흙 인형에서 키 10~14cm쯤의 틀들이 나왔어요.'],
   'text2': ['사진은 마르셀 카르보넬 상통 박물관에 있는 라녤의 틀이에요. 둥근 지붕 모양의 석고 덩이를 두 쪽으로 열면, 그 안에 사람 모양이 오목하게 파여 있어요.',
             '라녤 때의 상통은 굽지 않은 흙이었어요. 흙으로 찍어 말리기만 했지요.'],
   'kid': '상통은 ‘작은 성인’이라는 뜻이래. 흙으로 만든 구유 인형이야.',
   'kidq': '석고 틀을 열면 무엇이 나올까?'},
  {'id': 'fair', 'label': '장터에서 집 구유로', 'kind': 'duo', 'imgs': ['fair', 'postcard'],
   'caps': ['마르세유의 상통 장터 · 19세기 중엽', '보미앙, 마르가리도, 라비 · 20세기 초 그림엽서'],
   'text': ['마르세유는 프랑스에서 처음으로 상통 장터를 연 도시예요. 1803년의 일이에요. 프랑스 투데이는 그때 상인이 세 사람이었다고 전해요.',
            '사람들은 성탄을 앞두고 장터에 와서 집 구유에 더할 새 인물을 찾아요. 프로방스 구유의 바탕은 성가족, 소와 나귀, 세 박사, 가브리엘 천사, 양을 치는 목자예요. 그 둘레에 온 마을을 지어 올려요.'],
   'text2': ['왼쪽은 19세기 중엽 마르세유의 상통 장터를 그린 판화예요. 오른쪽은 20세기 초 마르세유의 그림엽서예요. 엽서에는 ‘보미앙, 마르가리도, 라비’라고 적혀 있어요. 그 차례대로라면 맨 오른쪽 젊은이가 라비예요. 보미앙은 떠돌며 사는 보헤미안이에요.'],
   'kid': '옛날 마르세유에는 상통 장터가 열렸대. 지금도 열린대!',
   'kidq': '장터에서 너라면 어떤 상통을 데려올래?'},
  {'id': 'make', 'label': '라비 하나 만들기', 'kind': 'mod', 'mod': 'steps',   # ← 그 자리에 있고 싶은 한 순간(한가운데 장면)
   'text': ['프랑스 문화부는 2021년 상통 장인의 솜씨를 무형문화유산 목록에 적으며, 오늘 장인들이 상통을 만드는 차례를 남겼어요.',
            '그 차례대로 라비를 만들어 보세요. 라비는 마을의 ‘놀란 사람’이에요. 놀라서 두 팔을 번쩍 들었어요. 구유에 드릴 것이 없어서 기쁨과 웃음만 가지고 왔대요.'],
   'text2': ['그림은 문화부 목록의 차례를 따라 이 안내서가 그렸어요. 가마에 굽는 차례는 20세기에 들어왔어요. 오바뉴의 상통 장인 테레즈 뇌뵈(1866~1946)가 처음 구웠어요.'],
   'kid': '흙을 틀에 꾹 눌러 찍고, 구워서, 색을 칠해!',
   'kidq': '라비는 왜 두 팔을 번쩍 들었을까?'},
 ],
 'imagine': {'t': '흙 냄새가 나는 작은 공방이에요. 석고 틀 두 쪽을 열면 촉촉한 흙 사람이 나와요. 선반에는 마르는 상통들이 줄지어 서 있고, 가마에서 막 나온 라비는 아직 따뜻해요. 붓끝에서 붉은 모자가 피어나요.',
             'kid': '눈을 감아 봐. 흙 냄새가 나. 틀을 열면 작은 사람이 쏙! 붓으로 빨간 모자를 칠해.'},
 'lines': ['드릴 것 없이 기쁨만 들고 온 사람.', '흙 한 덩이에서 작은 성인으로.', '틀 하나로 삼사백, 그래도 칠은 한 색씩 손으로.', '장터에서 집 구유로 걸어 들어온 마을 사람들.'],
 'linesKid': ['라비는 두 팔을 번쩍!', '흙으로 만든 작은 성인.', '틀에 꾹, 가마에 쏙.'],
 'close': {'form': '그 사람 안에 들어가 보기',
           'from': '라비 — 마르세유 관광청: 마을의 ‘놀란 사람’, 두 팔을 들어 놀람을 보이고, 드릴 것이 없어 기쁨과 웃음만 가지고 옴 · 문화부 목록: 두 팔을 든 순박한 사람(한가운데 장면에서 만든 바로 그 상통)',
           'ask': '드릴 것 하나 없이 두 팔을 번쩍 든 라비는, 구유 앞에서 무엇을 보았을까요?',
           'askKid': '라비는 아기 예수님을 보고 왜 두 팔을 번쩍 들었을까?'},
 'goals': {
  's4': {'t': '아홉 단계 끝까지', 'p': '빚기부터 칠하기까지 아홉 단계를 끝까지 해 보면 카드에 금박이 입혀져요.',
         'how': '‘손으로 빚기’부터 아홉 단계를 끝까지 해 보세요', 'done': '라비를 끝까지 만들어 봤어요',
         'ways': [{'id': 'steps', 't': '빚기 → 틀 → 흙 넣기 → 꺼내기 → 말리기 → 다듬기 → 굽기 → 살빛 → 옷과 모자'}]},
  's5': {'t': '아이와 함께', 'p': '아이와 함께 ‘영화처럼 보기’를 끝까지 보면 카드가 채색돼요.',
         'how': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'done': '아이와 함께 끝까지 봤어요',
         'ways': [{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'steps': {
   'svg': svg(),
   'alt': '이 안내서가 그린 상통 라비. 흙 한 덩이가 빚어지고, 석고 틀로 찍혀 나와 마르고, 구워지고, 한 색씩 칠해진다.',
   'cap': '이 안내서가 그린 상통 라비 · 프랑스 문화부 무형문화유산 목록(2021)의 만드는 차례를 바탕으로',
   'intro': '단추를 누를 때마다 한 단계씩 만들어져요. 흙 한 덩이에서 시작해요.',
   'hint': '아래 ‘손으로 빚기’부터 눌러 보세요.',
   'steps': STEPS,
   'marksLabel': '흙과 물감의 빛깔',
   'marks': [{'t': '젖은 흙', 'c': WET, 's': 1}, {'t': '흰 석고', 'c': '#f1eee6', 's': 2}, {'t': '마른 흙', 'c': DRY, 's': 5},
             {'t': '구운 흙 · 980°C', 'c': FIRED, 's': 7}, {'t': '살빛', 'c': SKIN, 's': 8}, {'t': '붉은 모자', 'c': CAP, 's': 9}],
   'done': '라비가 다 만들어졌어요. 흙 한 덩이가 빚기와 틀, 말리기와 굽기, 칠하기를 지나 두 팔을 든 작은 성인이 되었어요.',
 }},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>굽는 상통이 퍼지기까지</b> 테레즈 뇌뵈가 상통을 굽기 시작했을 때는 값이 올라 따라 하는 사람이 적었어요. 제2차 세계 대전 뒤 전기 가마가 나오면서 널리 퍼졌어요.',
    '<b>오늘의 공방</b> 마르세유 관광청은 마르세유에서 오바뉴, 엑상프로방스까지 상통 공방이 120곳쯤 있다고 소개해요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>‘상통’이라는 낱말</b> 문화부 목록은 이 낱말이 1733년의 글에 처음 나온다고 적었어요. 2024년 프랑스 투데이의 글은 1826년에야 기록에 나온다고 했어요.',
    '<b>혁명 때의 집 구유</b> 프랑스 투데이는 혁명 때 구유가 금지되었고, 1794년 성당이 닫힌 뒤 사람들이 집에서 몰래 구유를 만들었다고 적었어요. 문화부 목록은 1794년에 성탄 자정 미사가 금지되어 집 안의 작은 제단이 늘었다는 것을 ‘몇몇 사람이 내놓은 생각’이라고 조심스럽게 적었어요.',
    '<b>라비의 두 팔</b> 문화부 목록과 마르세유 관광청은 라비를 두 팔을 든 사람으로 적어요. 20세기 초 그림엽서에 적힌 이름 차례대로라면 라비는 맨 오른쪽 젊은이예요. 이 라비는 한 손에 등불을 들고 다른 손만 들었어요.']},
  {'h': '직접 가 보기', 'checked': '2026년 11월 18일', 'p': [
    '2026년 마르세유 상통 장터는 224번째예요. 11월 14일부터 2027년 1월 3일까지 옛 항구의 부두에서 열려요. 월~목요일과 일요일은 10~19시, 금·토요일은 10~20시이고, 들어가는 값은 없어요.',
    '공식 개막은 11월 15일 일요일 낮 12시예요. 그 앞 10시 30분에 생페레올 레 오귀스탱 성당에서 상통 장인들의 미사가 열려요. 일정은 아직 확정 전이라 바뀔 수 있어요.'],
   'links': [{'t': '마이 프로방스: 제224회 마르세유 상통 장터 일정', 'u': FOIRE, 'm': '프랑스어'},
             {'t': '프랑스 문화부: 상통 장인의 솜씨(무형문화유산 목록, PDF)', 'u': FICHE, 'm': '프랑스어'},
             {'t': '마르세유 관광청: 프로방스의 상통', 'u': OTM, 'm': '프랑스어'}]},
 ],
 'src': [
  {'l': '프랑스 문화부 무형문화유산 목록 「프로방스 상통 장인의 솜씨」(2021, 안토냉 샤베르) — 만드는 차례(빚기·어미 틀 300~400개·두 쪽에 흙·쇠막대·닷새~몇 주 말리기·칼과 붓과 사포·12시간 980°C와 48시간 식히기·살빛부터 칠하기), 1733년의 낱말, 1692년의 집 구유, 1794년에 대한 조심스러운 생각, 라녤의 흙과 10~14cm 틀, 뇌뵈의 굽기, 1803년 장터, 두 팔을 든 라비', 'u': FICHE},
  {'l': '마르세유 관광청: 프로방스의 상통 — 라비(놀란 사람, 두 팔, 기쁨과 웃음), 보헤미안 부부, 구유의 바탕 인물, 공방 120곳쯤', 'u': OTM},
  {'l': '프랑스 투데이(티르자 발루아, 2024.12.14): 프로방스의 상통 — 1826년의 낱말, 혁명 때의 집 구유, 라녤의 흙 인형, 1803년 장터와 상인 세 사람, 굽지 않은 상통', 'u': FT},
  {'l': '마이 프로방스: 제224회 마르세유 상통 장터 — 2026년 11월 14일~2027년 1월 3일, 옛 항구 부두, 여는 시간, 개막과 미사, 무료(2026년 11월 18일 확인)', 'u': FOIRE},
  {'l': '위키미디어 공용: 라녤의 틀 사진 설명 — 장루이 라녤(1764~1822)의 틀, 마르셀 카르보넬 상통 박물관', 'u': CMS + 'Moule_de_Lagnel.jpg'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'molds', 'fit': 'cover', 'p0': '50% 70%', 'p1': '50% 52%', 's0': 1.3, 's1': 1.06, 'kicker': '1800년 무렵부터 · 프랑스 마르세유', 'title': '작은 성인',
   'lines': [{'t': '프로방스 사람들은 구유 인형을 ‘상통’이라고 불러요.'}, {'t': '‘작은 성인’이라는 뜻이에요.'}],
   'kid': [{'t': '프로방스에는 흙으로 만든 구유 인형이 있대.'}, {'t': '이름은 상통, ‘작은 성인’이래.'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '작은 성인의 틀'},
  {'type': 'img', 'ch': 1, 'img': 'molds', 'fit': 'cover', 'p0': '30% 30%', 'p1': '62% 78%', 's0': 1.4, 's1': 1.15, 'cap': '장루이 라녤의 상통 틀',
   'lines': [{'t': '1800년 무렵, 마르세유의 라녤은 이 인형을 흙으로 만들었어요.'},
             {'t': '흙은 석고 틀로 찍어 내기 좋았어요. 같은 인형을 여럿 만들 수 있었지요.'},
             {'t': '라녤 때의 상통은 굽지 않은 흙이었어요.'}],
   'kid': [{'t': '석고 틀 안에 사람 모양이 오목하게 파여 있어.'}, {'t': '틀을 열면 무엇이 나올까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '장터에서 집 구유로'},
  {'type': 'img', 'ch': 2, 'img': 'fair', 'fit': 'contain', 'p0': '50% 50%', 'p1': '50% 50%', 's0': 1.0, 's1': 1.0, 'cap': '마르세유의 상통 장터 · 19세기 중엽',
   'lines': [{'t': '1803년, 마르세유는 프랑스에서 처음으로 상통 장터를 열었어요.'},
             {'t': '사람들은 장터에서 집 구유에 더할 새 인물을 찾았어요.'}],
   'kid': [{'t': '옛날 마르세유에는 상통 장터가 열렸대.'}]},
  {'type': 'img', 'ch': 2, 'img': 'postcard', 'fit': 'contain', 'p0': '50% 50%', 'p1': '50% 50%', 's0': 1.0, 's1': 1.0, 'cap': '보미앙, 마르가리도, 라비 · 20세기 초 그림엽서',
   'lines': [{'t': '성가족과 목자 둘레로, 온 마을 사람들이 모여들어요.'},
             {'t': '엽서에 적힌 이름 차례대로면, 맨 오른쪽 젊은이가 라비예요.'}],
   'kid': [{'t': '오른쪽 젊은이가 라비래. 등불을 들고 있어.'}, {'t': '장터에서 너라면 어떤 상통을 데려올래?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '라비 하나 만들기'},
  {'type': 'mod', 'mod': 'steps', 'ch': 3,
   'lines': [{'t': '문화부 기록에 남은 차례대로 만들어요.'},
             {'t': '흙으로 라비를 빚고,', 'act': 'step:1'},
             {'t': '석고로 어미 틀을 떠요. 이 틀 하나로 300~400개.', 'act': 'step:2'},
             {'t': '두 쪽에 흙을 넣고, 몸무게로 꾹 눌러 닫아요.', 'act': 'step:3'},
             {'t': '쇠막대를 꽂아 꺼내고, 바람에 말려요.', 'act': 'step:5'},
             {'t': '이음매를 다듬고, 980°C 가마에 구워요.', 'act': 'step:7'},
             {'t': '살빛부터, 속옷·셔츠·겉옷·모자 차례로.', 'act': 'step:9', 'wait': 2200},
             {'t': '드릴 것 없이 기쁨만 가지고 온 라비예요.'}],
   'kid': [{'t': '흙을 빚어!', 'act': 'step:1'}, {'t': '석고 틀에 꾹!', 'act': 'step:3'},
           {'t': '말리고, 다듬고, 구워!', 'act': 'step:7'}, {'t': '살빛, 옷, 빨간 모자!', 'act': 'step:9', 'wait': 1600},
           {'t': '라비는 왜 두 팔을 들었을까?', 'ask': True}]},
  {'type': 'imagine', 'ch': 4,
   'lines': [{'t': '흙 냄새가 나는 작은 공방이에요.'}, {'t': '틀을 열면 촉촉한 흙 사람이 나와요.'}, {'t': '가마에서 막 나온 라비는 아직 따뜻해요.'}],
   'kid': [{'t': '눈을 감아 봐. 흙 냄새가 나.'}, {'t': '틀을 열면, 작은 사람이 쏙!'}]},
  {'type': 'reward', 'ch': 4},
 ],
}
