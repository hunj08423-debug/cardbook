# 새 홈페이지(카드 책) 만들기
#  - 원본 데이터: guide_v35.html 안의 DATA (카드 477, 세트 98, 안내 468, 긴 이야기 59)
#  - 결과: site/repo/  (깃허브 저장소에 그대로 올릴 내용: wrangler.jsonc, README.md, site/...)
#          site/preview/index.html (claude.ai 시안용: 문서 머리 없이 본문만)
import json, os, re, shutil, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from chapters import CHAPTERS, DEEP

W = '/home/claude/w'
SITE = os.path.join(W, 'site')
REPO = os.path.join(SITE, 'repo')
OUT = os.path.join(REPO, 'site')
PREV = os.path.join(SITE, 'preview')
TITLE = sys.argv[1] if len(sys.argv) > 1 else '처음 만나는 기독교 문화'
BUILT = datetime.date.today().strftime('%Y년 %-m월 %-d일')

h = open(os.path.join(W, 'guide_v35.html'), encoding='utf-8').read()
D, _ = json.JSONDecoder().raw_decode(h[re.search(r'const DATA=', h).end():])
items = {x['id']: x for x in D['items']}
stories = {x['id']: x for x in D['stories']}
sets = {x['id']: x for x in D['sets']}
cards = {x['id']: x for x in D['setcards']}

# 글자 그림이던 카드에 찾은 그림 넣기(목록: img_fix.py, 그림 파일: out/img/c/<id>.webp)
import img_fix
for cid, f, page, cv, cr, alt in img_fix.FIX:
    c = cards[cid]
    c.update({'cr': cr, 'cru': img_fix.cru_of(cid, f), 'alt': alt, 'cover': cv, 'qf': [cv[0], cv[1], 1]})
    if c.get('by', '').endswith(' · 글자 그림'): c['by'] = c['by'][:-len(' · 글자 그림')]

# 장 ↔ 세트 확인
seen = {}
chapters = []
for ch in CHAPTERS:
    sl = ch['sets'].split()
    for s in sl:
        assert s in sets, s
        assert s not in seen, ('세트가 두 장에 들어감', s)
        seen[s] = ch['id']
    n = sum(len(sets[s]['cards']) for s in sl)
    if ch['cover']: assert ch['cover'] in cards, ch['cover']
    chapters.append({k: ch[k] for k in ('id', 'no', 't', 'color', 'pig', 'intro', 'cover')} | {'sets': sl, 'n': n})
missing = [s for s in sets if s not in seen]
assert not missing, ('장에 안 들어간 세트', missing)
assert sum(c['n'] for c in chapters) == len(cards), '카드 수가 맞지 않아요'

def is_typ(c): return c.get('cr', '').startswith('글자 그림')

# 안내·긴 이야기가 처음 나오는 카드
item_card, story_card = {}, {}
for ch in chapters:
    for s in ch['sets']:
        for cid in sets[s]['cards']:
            c = cards[cid]
            for ref in [c.get('item')] + list(c.get('also') or []):
                if not ref: continue
                if ref in items: item_card.setdefault(ref, cid)
                if ref in stories: story_card.setdefault(ref, cid)
assert len(item_card) == len(items), (len(item_card), len(items))
assert len(story_card) == len(stories), (len(story_card), len(stories))

IX = {
    'chapters': chapters,
    'sets': {sid: {'k': s['k'], 't': s['t'], 'sub': s['sub'], 'ch': seen[sid], 'cards': s['cards']} for sid, s in sets.items()},
    'cards': {cid: {'t': c['t'], 'tag': c['tag'], 'set': c['set'], 'ch': seen[c['set']], 'no': c['no'], 'by': c['by'],
                    'q': c['q'], 'kq': c['kq'], 'cv': c.get('cover') or [50, 50], 'typ': is_typ(c)} for cid, c in cards.items()},
    'items': {iid: {'t': it['t'], 'o': it.get('o') or '', 'g': it.get('g') or '', 'm': it.get('m') or '', 'p': it.get('p') or '', 'y': it.get('y') or '',
                    'h': it.get('h') or '', 'tier': it.get('tier') or '', 'a': it.get('a') or [], 'must': bool(it.get('must')),
                    'ct': sorted({c['t'] for c in (it.get('c') or []) if c.get('t')}), 'card': item_card[iid]} for iid, it in items.items()},
    'must': [m for m in D['must'] if m in items],
    'pil': {'h': D['pilgrim']['headline'], 's': D['pilgrim']['subhead']},
    'stories': {sid: {'t': s['t'], 'k': s['k'], 'lead': s['lead'], 'card': story_card[sid]} for sid, s in stories.items()},
    'storyOrder': [s['id'] for s in D['stories']],
    'deep': DEEP,
}

if os.path.exists(OUT): shutil.rmtree(os.path.join(OUT, 'data'), ignore_errors=True)
os.makedirs(os.path.join(OUT, 'data'), exist_ok=True)
def dump(path, obj):
    with open(path, 'w', encoding='utf-8') as f: json.dump(obj, f, ensure_ascii=False, separators=(',', ':'))
dump(os.path.join(OUT, 'data', 'index.json'), IX)
dump(os.path.join(OUT, 'data', 'pilgrim.json'), D['pilgrim'])
for ch in chapters:
    cc, ii, ss = {}, {}, {}
    for s in ch['sets']:
        for cid in sets[s]['cards']:
            c = cards[cid]; cc[cid] = c
            for ref in [c.get('item')] + list(c.get('also') or []):
                if ref in items: ii[ref] = items[ref]
                if ref in stories: ss[ref] = stories[ref]
    dump(os.path.join(OUT, 'data', f"ch-{ch['id']}.json"), {'cards': cc, 'items': ii, 'stories': ss})

# 카드 사진(미리 WebP로 바꿔 둔 것)
src_img = os.path.join(SITE, 'out', 'img', 'c')
dst_img = os.path.join(OUT, 'img', 'c')
os.makedirs(dst_img, exist_ok=True)
for cid in cards:
    a, b = os.path.join(src_img, cid + '.webp'), os.path.join(dst_img, cid + '.webp')
    assert os.path.exists(a), ('사진 없음', cid)
    if not os.path.exists(b) or os.path.getmtime(b) < os.path.getmtime(a): shutil.copy2(a, b)

# 직접 넣은 사진 자리(img/my/list.txt). 처음 한 번만 만들어요. 그 뒤로는 사용자가 고쳐 쓰는 파일이라 덮어쓰지 않아요.
my_dir = os.path.join(OUT, 'img', 'my')
os.makedirs(my_dir, exist_ok=True)
if not os.path.exists(os.path.join(my_dir, 'list.txt')):
    shutil.copy2(os.path.join(SITE, 'my', 'list.txt'), os.path.join(my_dir, 'list.txt'))

# 깊이 읽기 시안(시나이) 옮기기
deep_src = os.path.join(W, 'deep', 'out2')
deep_dst = os.path.join(OUT, 'deep')
for sub in ('img', 'snd'):
    os.makedirs(os.path.join(deep_dst, sub), exist_ok=True)
    for f in os.listdir(os.path.join(deep_src, sub)):
        shutil.copy2(os.path.join(deep_src, sub, f), os.path.join(deep_dst, sub, f))
dh = open(os.path.join(deep_src, 'sinai2.html'), encoding='utf-8').read()
old_brand = '<span class="brand"><span class="long"><b>처음 만나는 기독교 문화</b> · </span>카드 뒷면 시안 2</span>'
assert dh.count(old_brand) == 1
dh = dh.replace(old_brand, '<a class="brand" href="../#c-keep-sinai" style="text-decoration:none">← <span class="long"><b>처음 만나는 기독교 문화</b> · </span>카드 책으로</a>')
HEAD = '<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="robots" content="noindex,nofollow">\n'
open(os.path.join(deep_dst, 'sinai.html'), 'w', encoding='utf-8').write(HEAD + '<link rel="icon" href="../icon.svg" type="image/svg+xml">\n<link rel="icon" href="../icon-32.png" sizes="32x32" type="image/png">\n<link rel="apple-touch-icon" href="../apple-touch-icon.png">\n</head>\n<body>\n' + dh + '\n</body>\n</html>\n')

# 아이콘, 링크 미리보기 그림, 홈 화면 설정(만드는 법: make_brand.py)
SITE_URL = 'https://cardbook.hunji08423.workers.dev/'
OG_DESC = '하루 한 편, 기독교 문화와 역사의 이야기를 읽고 카드를 한 장씩 모아 가는 책이에요.'
for f in os.listdir(os.path.join(SITE, 'brand')):
    shutil.copy2(os.path.join(SITE, 'brand', f), os.path.join(OUT, f))
json.dump({'name': '처음 만나는 기독교 문화', 'short_name': '카드 책', 'description': OG_DESC, 'lang': 'ko', 'start_url': './', 'scope': './', 'display': 'standalone',
           'background_color': '#EAE5DB', 'theme_color': '#233A7C',
           'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
                     {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}]},
          open(os.path.join(OUT, 'manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
ICONS = lambda pre='': (f'<link rel="icon" href="{pre}icon.svg" type="image/svg+xml">\n<link rel="icon" href="{pre}icon-32.png" sizes="32x32" type="image/png">\n'
                        f'<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">\n')
SHARE = ('<meta property="og:type" content="website">\n<meta property="og:locale" content="ko_KR">\n'
         '<meta property="og:site_name" content="처음 만나는 기독교 문화">\n<meta property="og:title" content="처음 만나는 기독교 문화">\n'
         f'<meta property="og:description" content="{OG_DESC}">\n'
         f'<meta property="og:image" content="{SITE_URL}og.jpg?v=1">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="600">\n'
         '<meta property="og:image:alt" content="청금색 바탕에 금빛 글씨로 쓴 ‘처음 만나는 기독교 문화’와 옛 그림 카드 세 장">\n'
         '<meta name="twitter:card" content="summary_large_image">\n'
         '<link rel="manifest" href="manifest.json">\n<meta name="apple-mobile-web-app-title" content="카드 책">\n')

# 첫 화면
app = open(os.path.join(SITE, 'app.html'), encoding='utf-8').read().replace('{{TITLE}}', TITLE).replace('{{BUILT}}', BUILT).replace('{{PREVIEW}}', 'false')
cut = app.index('</style>') + len('</style>')
head_part, body_part = app[:cut], app[cut:]
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(
    HEAD + '<meta name="theme-color" content="#233A7C">\n' + ICONS() + SHARE + head_part + '\n</head>\n<body>\n' + body_part + '\n</body>\n</html>\n')
os.makedirs(PREV, exist_ok=True)
PTITLE = os.environ.get('PREVIEW_TITLE', TITLE)
open(os.path.join(PREV, 'index.html'), 'w', encoding='utf-8').write(open(os.path.join(SITE, 'app.html'), encoding='utf-8').read().replace('{{TITLE}}', PTITLE).replace('{{BUILT}}', BUILT).replace('{{PREVIEW}}', 'true'))
# 검색엔진에는 싣지 않되, 카카오톡·페이스북 링크 미리보기는 볼 수 있게
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: kakaotalk-scrap\nAllow: /\n\nUser-agent: facebookexternalhit\nAllow: /\n\nUser-agent: *\nDisallow: /\n')

# 저장소 바깥 파일
open(os.path.join(REPO, 'wrangler.jsonc'), 'w', encoding='utf-8').write(
    '{\n  // 클라우드플레어 Workers가 site 폴더를 그대로 홈페이지로 보여 줘요\n  "name": "cardbook",\n  "compatibility_date": "2026-11-01",\n  "assets": { "directory": "./site" }\n}\n')
open(os.path.join(REPO, 'README.md'), 'w', encoding='utf-8').write(
    '# 처음 만나는 기독교 문화\n\n카드 477장으로 펼쳐 보는 기독교 문화 입문서예요.\n\n- `site/` 폴더가 홈페이지 전체예요.\n- `tools/` 폴더는 홈페이지를 만드는 도구예요(홈페이지에는 나오지 않아요).\n- 사진과 그림은 저작권이 끝났거나 자유 이용이 허락된 것만 쓰고, 카드마다 출처를 적었어요.\n')

# 만드는 도구도 저장소에 함께(홈페이지에는 안 나가요: site 폴더 밖)
os.makedirs(os.path.join(REPO, 'tools'), exist_ok=True)
for f in ('app.html', 'build_site.py', 'chapters.py', 'conv_images.py', 'make_brand.py', 'img_fix.py'):
    shutil.copy2(os.path.join(SITE, f), os.path.join(REPO, 'tools', f))

# 요약
nfiles = sum(len(fs) for _, _, fs in os.walk(OUT))
size = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(OUT) for f in fs)
print('built', BUILT, '| files', nfiles, '| MB', round(size / 1024 / 1024, 1),
      '| index KB', round(os.path.getsize(os.path.join(OUT, 'data', 'index.json')) / 1024),
      '| chapters', len(chapters))
