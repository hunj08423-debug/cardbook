# -*- coding: utf-8 -*-
"""새 깊은 카드의 자료 파일 뼈대를 만들어요: tools/deep/cards/<카드id>.py
사이트에 이미 있는 제목·물음·장 색을 채워 두고, 채울 곳은 '__채우기__'로 남겨요(check.py가 남은 곳을 찾아 줘요).

쓰는 법(저장소 맨 위 폴더에서):
  python3 tools/deep/kit/new_card.py <카드id> --mod look      → 중심 방식: 찾아보기(그림 속 작은 것 찾기)
  python3 tools/deep/kit/new_card.py <카드id> --mod reveal    → 비추기(어두운 곳을 빛으로 비춰 드러내기)
  python3 tools/deep/kit/new_card.py <카드id> --mod slider    → 그때와 지금(손잡이를 밀어 겹쳐 보기)
  python3 tools/deep/kit/new_card.py <카드id> --mod route     → 지도 위 길(다음 곳으로 따라가기)
  python3 tools/deep/kit/new_card.py <카드id> --mod voices|place|wreath  → 예시 카드의 방식(예시 카드 파일을 함께 보고 따라 써요)
  python3 tools/deep/kit/new_card.py <카드id> --mod unroll|timeline|steps|doors|gather|trace  → 키트 3판 새 방식(펼쳐 읽기·시간 따라 보기·만드는 차례·날짜 따라 여는 달력·흩어진 조각 모으기·따라 쓰기). kit/examples/ 예시를 함께 봐요
  --size one   → 한 장면 카드(장면 1~2개). 기본은 큰 카드(장면 4~5개)
이미 파일이 있으면 덮어쓰지 않아요.
"""
import os, sys, json, datetime

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))
F = '__채우기__'

def mix(h, t, k):
    a = [int(h[i:i + 2], 16) for i in (1, 3, 5)]; b = [int(t[i:i + 2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{round(x + (y - x) * k):02x}' for x, y in zip(a, b))

def theme(col):
    r, g, b = (int(col[i:i + 2], 16) for i in (1, 3, 5))
    dk = mix(col, '#ffffff', .48)
    dr, dg, db = (int(dk[i:i + 2], 16) for i in (1, 3, 5))
    return (f":root{{--accent:{col};--accent-ink:#fffaf5;--soft:rgba({r},{g},{b},.09);--stamp:#b0392b}}\n"
            f"@media (prefers-color-scheme: dark){{:root:not([data-theme=\"light\"]){{--accent:{dk};--accent-ink:#14100c;--soft:rgba({dr},{dg},{db},.10);--stamp:#e86f5d}}}}\n"
            f":root[data-theme=\"dark\"]{{--accent:{dk};--accent-ink:#14100c;--soft:rgba({dr},{dg},{db},.10);--stamp:#e86f5d}}")

MODS = {
 'look': ('찾아보기', """ 'mods': {'look': {
   'img': 'card',                      # 크게 볼 그림의 images 키('card' = 사이트 앞면 그림)
   'intro': '그림 속 작은 것들을 하나씩 눌러 보세요.',
   'spots': [                          # 3~7곳. x·y = 그림 왼쪽 위에서 잰 위치(%). 그림을 Read로 열어 보고 정해요
     {'x': 50, 'y': 50, 't': '__채우기__', 'p': '__채우기__(한두 문장, 출처 있는 사실)', 'kid': '__채우기__'},
     {'x': 30, 'y': 30, 't': '__채우기__', 'p': '__채우기__', 'kid': '__채우기__'},
     {'x': 70, 'y': 70, 't': '__채우기__', 'p': '__채우기__', 'kid': '__채우기__'},
   ],
   'done': '__채우기__(다 찾았을 때 한 줄)',
 }},""", "{'id': 'look', 't': '그림 속 __채우기__곳을 모두 찾아 읽기'}", "'act': 'spot:1'"),
 'reveal': ('비추기', """ 'mods': {'reveal': {
   'img': 'card',                      # 어둠 속에서 드러낼 그림의 images 키
   'light': 'candle',                  # 빛 모양: candle(촛불) · torch(횃불) · lamp(등불)
   'intro': '손가락이나 마우스로 문질러 비춰 보세요.',
   'marks': [                          # 선택: 빛이 닿으면 이름이 뜨는 곳 0~5곳(x·y = %)
     {'x': 40, 'y': 40, 't': '__채우기__', 'p': '__채우기__'},
   ],
   'after': '__채우기__(다 비췄을 때 나오는 한두 문장)',
 }},""", "{'id': 'reveal', 't': '__채우기__을 끝까지 비춰 보기'}", "'act': 'light'"),
 'slider': ('그때와 지금', """ 'mods': {'slider': {
   'intro': '가운데 손잡이를 밀어 그때와 지금을 겹쳐 보세요.',
   'pairs': [                          # 1~3쌍. 같은 자리를 비슷한 방향에서 본 두 그림
     {'then': '__채우기__', 'now': '__채우기__', 'thenT': '__채우기__(예: 1850년 무렵)', 'nowT': '__채우기__(예: 2016년)',
      'p': '__채우기__(무엇이 남고 무엇이 바뀌었는지 한두 문장)'},
   ],
 }},""", "{'id': 'slider', 't': '손잡이를 끝까지 밀어 그때와 지금을 다 보기'}", "'act': 'now'"),
 'route': ('지도 위 길', """ 'mods': {'route': {
   'img': '__채우기__',               # 지도 그림의 images 키(옛 지도·오늘 지도). 없으면 'paper'(종이 바탕)
   'intro': '‘다음 곳으로’를 눌러 길을 따라가 보세요.',
   'stops': [                          # 2~8곳, 가는 차례대로. x·y = 지도 위 위치(%)
     {'x': 20, 'y': 60, 't': '__채우기__', 'd': '__채우기__(때)', 'p': '__채우기__'},
     {'x': 70, 'y': 40, 't': '__채우기__', 'd': '__채우기__', 'p': '__채우기__'},
   ],
   'end': '__채우기__(도착했을 때 한 줄)',
 }},""", "{'id': 'route', 't': '처음부터 끝까지 길을 따라가기'}", "'act': 'go'"),
 # 키트 3판 새 방식 여섯 가지(MODULES.md ‘새 방식 여섯 가지’, 예시 kit/examples/)
 'unroll': ('펼쳐 읽기', """ 'mods': {'unroll': {
   'img': '__채우기__',                # 세로로 긴 종이 그림의 images 키
   'textFrom': '__채우기__(원문을 옮겨 적은 믿을 만한 자료 — 그림 속 손글씨를 창이 직접 읽어 옮기지 않아요)',
   'intro': '종이 아래쪽 굴대를 끌어 내리거나 ‘한 줄 더 펼치기’를 눌러 보세요.',
   'lines': [                          # 2~10줄, 위에서 아래 차례. y0·y1 = 그 줄의 높이(위 0 ~ 아래 100)
     {'y0': 5, 'y1': 12, 'o': '__채우기__(원문)', 'k': '__채우기__(우리말)', 'n': '__채우기__(풀이 한두 문장)'},
     {'y0': 12, 'y1': 20, 'o': '__채우기__', 'k': '__채우기__', 'n': '__채우기__'},
   ],
   'done': '__채우기__(끝까지 펼쳤을 때 한 줄)',
 }},""", "{'id': 'unroll', 't': '끝까지 펼쳐 모든 줄 읽기'}", "'act': 'line:1'"),
 'timeline': ('시간 따라 보기', """ 'mods': {'timeline': {
   'intro': '시간 막대를 밀거나 해를 눌러 지나가 보세요.',
   'stops': [                          # 3~6때, 앞에서 뒤로. 같은 곳을 담은 그림이 세 때 넘게 있을 때만
     {'y': '__채우기__(보이는 이름: 1750년대)', 'at': 1750, 'img': '__채우기__', 't': '__채우기__', 'p': '__채우기__'},
     {'y': '__채우기__', 'at': 1850, 'img': '__채우기__', 't': '__채우기__', 'p': '__채우기__'},
     {'y': '__채우기__', 'at': 2000, 'img': '__채우기__', 't': '__채우기__', 'p': '__채우기__'},
   ],
   'done': '__채우기__(다 지나왔을 때 한 줄)',
 }},""", "{'id': 'timeline', 't': '모든 때를 지나 보기'}", "'act': 'stop:2'"),
 'steps': ('만드는 차례', """ 'mods': {'steps': {
   'svg': '__채우기__(이 안내서가 그린 SVG — kit/examples/steps_pysanka_svg.py처럼. 사진이면 이 줄을 지우고 단계마다 img)',
   'alt': '__채우기__', 'cap': '이 안내서가 그린 __채우기__ · __채우기__(무엇을 바탕으로)',
   'intro': '단추를 누를 때마다 한 단계씩 만들어져요.',
   'hint': '__채우기__(첫 단계부터 눌러 보라는 한 줄)',
   'steps': [                          # 3~9단계, 기록에 있는 차례대로
     {'do': '__채우기__(단추에 쓸 말)', 't': '__채우기__', 'p': '__채우기__'},
     {'do': '__채우기__', 't': '__채우기__', 'p': '__채우기__'},
     {'do': '__채우기__', 't': '__채우기__', 'p': '__채우기__'},
   ],
   'done': '__채우기__(다 만들었을 때 한 줄)',
 }},""", "{'id': 'steps', 't': '끝 단계까지 만들어 보기'}", "'act': 'step:1'"),
 'doors': ('날짜 따라 여는 달력', """ 'mods': {'doors': {
   'img': '__채우기__', 'month': 12,
   'needDays': 3,                      # 서로 다른 몇 날에 창을 열면 기록이 되나(1~5)
   'sim': [1, 13, 24],                 # 미리 보기 단추(그날이라고 치고 열어 보기 · 남지 않아요)
   'intro': '그날이 된 창만 열려요. 반짝이는 창을 눌러 보세요.',
   'hint': '반짝이는 창이 오늘 열 수 있는 창이에요.',
   'doors': [                          # d = 날짜(1~31), r = [x, y, 너비, 높이](%) — 그림을 Read로 열어 보고 정해요
     {'d': 1, 'r': [10, 10, 10, 15], 't': '__채우기__', 'p': '__채우기__(그 창에 실제로 보이는 것)'},
   ],
   'done': '__채우기__(기록이 되었을 때 한 줄)',
 }},""", "{'id': 'doors', 't': '서로 다른 세 날에 창 열기'}", "'act': 'open:1'"),
 'gather': ('흩어진 조각 모으기', """ 'mods': {'gather': {
   'img': '__채우기__',
   'split': '__채우기__(실제 또는 빗댐 — 빗댐이면 장면 글이나 그림 설명에 밝혀요)',
   'intro': '흩어진 조각을 하나씩 눌러 제자리로 모아 보세요.',
   'hint': '조각을 눌러 보세요. 그 조각이 지금 어디에 있는지 알려 줘요.',
   'pieces': [                         # 2~8조각. r = [x, y, 너비, 높이](%)
     {'t': '__채우기__(곳 · 기관)', 'lab': '__채우기__(12자 안쪽)', 'r': [5, 5, 40, 90], 'p': '__채우기__'},
     {'t': '__채우기__', 'lab': '__채우기__', 'r': [55, 5, 40, 90], 'p': '__채우기__'},
   ],
   'done': '__채우기__(다 모였을 때 한 줄)',
 }},""", "{'id': 'gather', 't': '흩어진 조각을 모두 모으기'}", "'act': 'piece:1'"),
 'trace': ('따라 쓰기', """ 'mods': {'trace': {
   'glyph': {'vb': '0 0 200 200', 'name': '__채우기__', 'alt': '__채우기__',
             'strokes': [               # 1~8획, 쓰는 차례대로. d = M으로 시작하는 SVG 선
               {'d': 'M50 50 L150 150', 't': '__채우기__', 'p': '__채우기__'},
             ]},
   'intro': '빨간 점에서 시작해, 흐린 선을 따라 그어 보세요.',
   'hint': '__채우기__', 'done': '__채우기__(다 썼을 때 한 줄)',
 }},""", "{'id': 'trace', 't': '모든 획을 따라 쓰기'}", "'act': 'stroke:1'"),
}
OLD = {'voices': 'sil-score', 'place': 'cus-greccio', 'wreath': 'lig-wreath'}

def main():
    a = sys.argv[1:]
    if not a or a[0].startswith('-'): print(__doc__); sys.exit(0)
    cid = a[0]
    mod = a[a.index('--mod') + 1] if '--mod' in a else 'look'
    size = a[a.index('--size') + 1] if '--size' in a else 'big'
    out = os.path.join(KIT, '..', 'cards', cid + '.py')
    if os.path.exists(out): raise SystemExit(f'이미 있어요: {out}')
    cards = {}
    import glob
    for f in glob.glob(os.path.join(REPO, 'site', 'data', 'ch-*.json')):
        cards.update(json.load(open(f, encoding='utf-8'))['cards'])
    ix = json.load(open(os.path.join(REPO, 'site', 'data', 'index.json'), encoding='utf-8'))
    if cid not in cards: raise SystemExit(f'site/data에 없는 카드 id예요: {cid}')
    c = cards[cid]; st = ix['sets'][c['set']]; ch = next(x for x in ix['chapters'] if x['id'] == st['ch'])
    today = datetime.date.today().isoformat()
    if mod in OLD:
        print(f"이 방식은 예시 카드 tools/deep/cards/{OLD[mod]}.py 를 복사해서 고쳐 쓰는 게 가장 빨라요. 뼈대는 찾아보기 모양으로 만들고 mods·modhtml 칸만 예시에서 옮겨 오세요.")
    name, modblock, way4, act = MODS.get(mod, MODS['look'])
    nsc = 2 if size == 'one' else 4
    scenes, film = [], [f"""  {{'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '50% 45%', 'p1': '55% 50%', 's0': 1.2, 's1': 1.05, 'kicker': '{F}(때 · 곳)', 'title': {json.dumps(c['t'], ensure_ascii=False)},
   'lines': [{{'t': '{F}'}}, {{'t': '{F}'}}],
   'kid': [{{'t': '{F}'}}, {{'t': '{F}'}}]}},"""]
    for i in range(1, nsc + 1):
        center = (i == (2 if size == 'one' else 3))
        if center:
            scenes.append(f"""  {{'id': 'sc{i}', 'label': '{F}', 'kind': 'mod', 'mod': '{mod}', 'night': False,   # ← 그 자리에 있고 싶은 한 순간(한가운데 장면)
   'text': ['{F}', '{F}'],
   'kid': '{F}', 'kidq': '{F}'}},""")
            film.append(f"""  {{'type': 'chapter', 'ch': {i}, 'no': {i}, 't': '{F}'}},
  {{'type': 'mod', 'mod': '{mod}', 'ch': {i},
   'lines': [{{'t': '{F}', {act}}}, {{'t': '{F}'}}, {{'t': '{F}'}}],
   'kid': [{{'t': '{F}'}}, {{'t': '{F}', 'ask': True}}]}},""")
        else:
            scenes.append(f"""  {{'id': 'sc{i}', 'label': '{F}', 'kind': 'photo', 'img': '{F}',
   'text': ['{F}', '{F}'],
   'kid': '{F}', 'kidq': '{F}'}},""")
            film.append(f"""  {{'type': 'chapter', 'ch': {i}, 'no': {i}, 't': '{F}'}},
  {{'type': 'img', 'ch': {i}, 'img': '{F}', 'fit': 'cover', 'p0': '50% 50%', 'p1': '50% 45%', 's0': 1.15, 's1': 1.0, 'cap': '{F}',
   'lines': [{{'t': '{F}'}}, {{'t': '{F}'}}],
   'kid': [{{'t': '{F}'}}, {{'t': '{F}', 'ask': True}}]}},""")
    film.append(f"""  {{'type': 'imagine', 'ch': {nsc + 1},
   'lines': [{{'t': '{F}'}}, {{'t': '{F}'}}, {{'t': '{F}'}}],
   'kid': [{{'t': '{F}'}}, {{'t': '{F}'}}]}},
  {{'type': 'reward', 'ch': {nsc + 1}}},""")
    body = f'''# -*- coding: utf-8 -*-
"""깊은 카드: {c['t']}({cid}) · 중심 방식 = {name}
기준서 2판 · 틀 deep3-4 · 키트 3판 · {today} 만들기 시작
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: {F}
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: {F}
카드 크기: {'한 장면 카드' if size == 'one' else '큰 카드'} — 재료가 정해요(재료가 적은데 큰 카드로 늘리지 않아요).
그림 원본(src)은 deep_src/{cid}/ (저장소 밖). 받는 법: commons_get.py"""
S = '{cid}/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{{NKRV}}{{code}}" target="_blank" rel="noopener">{{label}}</a>'

CARD = {{
 'id': '{cid}', 'mode': '{name}',
 'pagetitle': {json.dumps(c['t'], ensure_ascii=False)},
 'brandsub': '깊은 카드 · {name}',
 'where': '<b>{F}(때)</b><span>{F}(나라 · 곳)</span>',
 'lead': '{F}(세 문장 안: 때와 곳 → 무슨 일 → 손으로 해 볼 일)',
 'leadKid': '{F}',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 2판). 장면에는 기록에 있는 것만 옮겼고, 전해지는 이야기는 그렇다고 밝혔어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 # 화면 색: 기본은 {ch['no']}장 색이에요. 이야기에 맞는 색으로 바꿔도 돼요(밝게·어둡게 두 벌 모두).
 'theme': """{theme(ch['color'])}""",
 'stamp': {{'t': '{F}(두세 글자)', 'y': '{F}(해)', 'sub': '{F}(곳)'}},
 'doneNote': '{F}(다 마쳤을 때 한 줄)',
 'images': {{
  # 'card'는 따로 적지 않으면 사이트 앞면 그림을 써요.
  # 'key': {{'src': S + '파일.jpg', 'cap': '무엇인지, 언제', 'cr': '누가 · 라이선스 · 위키미디어 공용', 'u': '파일 페이지 주소', 'alt': '눈으로 보이는 것을 그대로'}},
 }},
 'scenes': [
{chr(10).join(scenes)}
 ],
 'imagine': {{'t': '{F}(감각: 소리·냄새·빛. 기록에 없는 마음은 여기에만)', 'kid': '{F}'}},
 'lines': ['{F}', '{F}', '{F}'],
 'linesKid': ['{F}', '{F}'],
 'close': {{'form': '{F}(끝맺는 꼴: 열 가지 가운데 하나 — MODULES.md ‘마무리’)', 'from': '{F}(이야기 속 무엇에서: 기록의 말·사람·날짜·그림)',
           'ask': '{F}(나의 자리·영화 끝 물음 — 이 카드의 한가운데 장면에서. 다른 카드에 옮겨 붙여도 말이 되면 다시)', 'askKid': '{F}'}},
 'goals': {{
  's4': {{'t': '{F}', 'p': '{F}(무엇을 하면 금박이 되는지)', 'how': '{F}', 'done': '{F}',
         'ways': [{way4}]}},
  's5': {{'t': '{F}', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.', 'how': '{F}', 'done': '{F}',
         'ways': [{{'id': '{F}', 't': '{F}(이야기 안의 행동)'}},
                  {{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}}]}},
 }},
{modblock}
 'deep': [
  {{'h': '알고 보면', 'p': ['<b>{F}</b> {F}']}},
  {{'h': '기록마다 다른 점', 'p': ['<b>{F}</b> {F}']}},
  {{'h': '직접 가 보기', 'checked': '{today[:4]}년 {int(today[5:7])}월 {int(today[8:])}일', 'p': ['{F}'], 'links': [{{'t': '{F}', 'u': '{F}'}}]}},
 ],
 'src': [
  {{'l': '{F}(누가 · 무엇 — 이 출처로 확인한 사실)', 'u': '{F}'}},
 ],
 'film': [
{chr(10).join(film)}
 ],
}}
'''
    open(out, 'w', encoding='utf-8').write(body)
    print(f'만들었어요: tools/deep/cards/{cid}.py · {name} · {"한 장면" if size == "one" else "큰"} 카드 뼈대')
    print('채울 곳은 __채우기__ 로 표시했어요. 다 채운 뒤 build.py → check.py 차례로 돌려요.')

if __name__ == '__main__':
    main()
