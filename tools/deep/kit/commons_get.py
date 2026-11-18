# -*- coding: utf-8 -*-
"""위키미디어 공용(Commons)에서 그림·소리를 찾고, 라이선스를 확인하고, 받아 두는 도구

쓰는 법(저장소 맨 위 폴더에서):
  python3 tools/deep/kit/commons_get.py --nettest                             → 위키미디어 세 주소에 닿는지 보기(파일은 받지 않음)
  python3 tools/deep/kit/commons_get.py --search "Greccio presepe"            → 파일 찾기(라이선스·크기와 함께 20개)
  python3 tools/deep/kit/commons_get.py --info "File:Santuario di Greccio.jpg"  → 한 파일의 정보만 보기
  python3 tools/deep/kit/commons_get.py --plan <카드id> "File:…" "File:…"      → 받기 전 목록(이름·크기·라이선스): 사용자 허락받을 때 보여 줘요
  python3 tools/deep/kit/commons_get.py --plan-file need.txt                   → 묶음 전체 목록 한 번에(줄마다 ‘카드id File:이름.jpg’)
  python3 tools/deep/kit/commons_get.py --fetch-file need.txt                  → 허락받은 뒤 묶음 전체를 한 번에 받기(가장 아껴 쓰는 방법)
  python3 tools/deep/kit/commons_get.py <카드id> "File:이름.jpg" ["File:이름2.ogg" ...]
        → 라이선스가 맞으면 원본 폴더(deep_src/<카드id>/)에 받고, _sources.json에 출처를 적고,
          카드 자료(images)에 붙여 넣을 줄을 보여 줘요.
  --thumb-only   원본 주소가 자주 막힐 때: 원본 대신 표준 너비 미리보기(3840, 원본이 그보다 작으면 한 단계 작은 너비)로 받아요
  python3 tools/deep/kit/commons_get.py --user-bat need.txt --name 묶음17 --device "<사용자 cardbook 경로>"
        → 위키미디어가 이 창의 받기를 계속 막을 때: 사용자가 더블클릭해 자기 컴퓨터로 받는 ‘그림 받기 파일’(.bat)과 목록(.json)을 만들어요
  python3 tools/deep/kit/commons_get.py --import <목록 .json> [<가져온 deep_src 폴더>]
        → 사용자가 받은 파일을 가져온(device_stage_files) 뒤: 작업 공간 deep_src로 옮기고 _sources.json에 출처를 적어요
  기본은 원본 그대로 받아요(기준서 2판 보탬 2 · 사용자님 결정 2026-11-18). 원본이 100MB를 넘으면 받지 않고 멈춰요:
               사용자님께 파일 이름·크기·출처를 보여 드리고 허락을 받으면 --allow-big, 허락이 없으면 --width 3840
  --width 3840   원본 대신 미리보기 너비로 받기(위키미디어 표준 너비: 330 500 960 1280 1920 3840). 꼭 필요할 때만
  python3 tools/deep/kit/commons_get.py --orig-bat [<카드 폴더> <deep_src 폴더> [카드id ...]] --name 원본받기 --device "<cardbook 경로>"
        → [본부] 예전에 줄여 준 판으로 받은 그림의 원본을 사용자 컴퓨터로 받는 파일(.bat). 원본은 deep_src/<카드>/_orig/로

쓸 수 있는 라이선스: 퍼블릭 도메인(PD) · CC0 · CC BY · CC BY-SA · 공공누리 제1유형. (NC·ND·GFDL만·'저작권 있음'은 안 돼요)
사람 얼굴이 나온 실제 사진(인물 사진)은 받지 말고 사용자에게 맡겨요(GUIDE.md 참고).
인터넷이 막혀 있으면 무엇을 해야 하는지 알려 주고 멈춰요.
"""
import os, sys, re, json, time, ssl, html, urllib.parse, urllib.request, urllib.error, datetime, shutil, ntpath, posixpath

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))
SRCROOT = os.environ.get('DEEP_SRC') or os.path.abspath(os.path.join(REPO, '..', 'deep_src'))
API = 'https://commons.wikimedia.org/w/api.php'
# 위키미디어는 연락할 수 있는 주소를 User-Agent에 적어 달라고 해요. 개인 정보 대신 공개된 사이트 주소를 적어요.
UA = 'CardbookDeepKit/1.0 (+https://cardbook.hunji08423.workers.dev/; educational, non-commercial) python-urllib'
STD_W = (330, 500, 960, 1280, 1920, 3840)
PAUSE = 1.0                      # 요청 사이 쉬는 시간(초): 위키미디어에 부담을 주지 않게
MAX_ORIG = 100 * 1024 * 1024     # 원본이 이보다 크면(100MB) 받기 전에 사용자님께 여쭤요(사용자님 결정 2026-11-18)

def ctx():
    for k in ('SSL_CERT_FILE', 'REQUESTS_CA_BUNDLE', 'CURL_CA_BUNDLE', 'NODE_EXTRA_CA_CERTS'):
        f = os.environ.get(k)
        if f and os.path.exists(f):
            try: return ssl.create_default_context(cafile=f)
            except Exception: pass
    return ssl.create_default_context()

class Blocked(Exception):
    pass

class Deferred(Exception):
    """위키미디어가 아주 오래(예: 10분) 기다려 달라고 할 때: 기다리지 않고 그 파일을 뒤로 미뤄요"""
    pass

LONG_WAIT = 90                   # 이보다 오래 기다려 달라고 하면(초) 파일 받기는 미뤄요(창이 멈추지 않게)

_last = [0.0]
def get(url, binary=False, tries=7, max_wait=None):
    """위키미디어는 2026년부터 요청 수를 제한해요(로그인 없는 요청은 한 시간에 수백 번 수준, 동시 요청은 3개 이하 권장).
    429(너무 많음)를 받으면 Retry-After만큼, 없으면 5·10·20·40·60초씩 늘려 가며 기다렸다 다시 해요."""
    for t in range(tries):
        wait = PAUSE - (time.time() - _last[0])
        if wait > 0: time.sleep(wait)
        _last[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Encoding': 'identity'})
            with urllib.request.urlopen(req, timeout=60, context=ctx()) as r:
                b = r.read()
                return b if binary else json.loads(b.decode('utf-8'))
        except urllib.error.HTTPError as ex:
            if ex.code in (429, 503) and t < tries - 1:
                try: ra = int(ex.headers.get('Retry-After') or 0)
                except ValueError: ra = 0
                if max_wait is not None and ra > max_wait:
                    raise Deferred(ra)
                w = max(ra, min(60, 5 * 2 ** t))
                print(f'  (위키미디어가 잠깐 쉬어 달라고 해요: {w}초 기다렸다 다시 해요)', file=sys.stderr)
                time.sleep(w); continue
            raise
        except (urllib.error.URLError, OSError) as ex:
            if re.search(r'Tunnel connection failed: 40[37]|Forbidden|Proxy Authentication', str(ex)):
                raise Blocked(urllib.parse.urlparse(url).hostname)      # 막힌 주소는 다시 시도하지 않아요
            if t < tries - 1: time.sleep(2); continue
            raise

DOMAINS = 'commons.wikimedia.org, upload.wikimedia.org, thumb.wikimedia.org'
def no_net(ex):
    host = ex.args[0] if isinstance(ex, Blocked) and ex.args else ''
    print('\n[인터넷이 막혀 있어요] ' + (f'{host} 주소가 막혀 있어요(허용 목록에 없음).' if host else '위키미디어 공용에 닿지 않아요: ' + str(ex)[:160]))
    print('이렇게 해 주세요(같은 주소로 다시 시도하지 마세요):')
    print('  1) 받을 파일 이름을 status/<카드id>_need.txt 에 한 줄에 하나씩 적어요(예: File:Santuario di Greccio.jpg).')
    print('  2) 사용자에게 이렇게 알려요: “이 창은 ' + (host or '위키미디어') + '에 닿지 않아요. 설정 › 기능(Capabilities)의 허용 도메인에')
    print('     ' + DOMAINS + ' 세 개가 다 있는지 봐 주시고, 새 창을 열어 주세요. 급하면 본부 창에 need 파일을 받아 달라고 해 주세요.”')
    print('  3) 그동안 글(장면·자막·근거)은 계속 써도 돼요. 그림 없이 빌드는 멈춰요.')
    sys.exit(2)

def title_of(x):
    x = x.strip()
    if x.startswith('http'):
        p = urllib.parse.urlparse(x)
        if '/wiki/' in p.path: x = urllib.parse.unquote(p.path.split('/wiki/', 1)[1])
        elif 'title=' in p.query: x = urllib.parse.parse_qs(p.query)['title'][0]
        else: x = urllib.parse.unquote(p.path.rsplit('/', 1)[-1])
    x = x.replace('_', ' ')
    if not re.match(r'(?i)^(file|파일):', x): x = 'File:' + x
    return 'File:' + x.split(':', 1)[1]

def plain(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

def lic_ok(meta):
    """(쓸 수 있나, 한국어 라이선스 이름, 까닭)"""
    short = plain(meta.get('LicenseShortName', {}).get('value', ''))
    code = plain(meta.get('License', {}).get('value', '')).lower()
    terms = plain(meta.get('UsageTerms', {}).get('value', ''))
    blob = ' '.join([short, code, terms]).lower()
    parts = re.split(r'[\s\-_/]+', blob)
    if 'nc' in parts or 'nd' in parts or 'noncommercial' in blob or 'non-commercial' in blob or 'noderiv' in blob:
        return False, short, '비영리(NC)나 변경 금지(ND) 조건이 있어요'
    if code in ('pd',) or code.startswith('pd') or 'public domain' in blob:
        return True, '퍼블릭 도메인', ''
    if 'cc0' in blob:
        return True, 'CC0', ''
    m = re.search(r'cc[ -]by(?:[ -]sa)?[ -]\d\.\d(?:[ -][a-z]{2,3})?', blob)
    if m or code.startswith('cc-by'):
        name = short if short.upper().startswith('CC BY') else (m.group(0).upper().replace('CC-BY', 'CC BY').replace('-SA', '-SA') if m else short)
        return True, name, ''
    if 'kogl' in blob and ('type 1' in blob or 'type1' in blob or '제1유형' in blob or 'type-1' in blob):
        return True, '공공누리 제1유형', ''
    if 'gfdl' in blob:
        return False, short, 'GFDL만 보여요. 파일 페이지에 CC BY-SA도 함께 있는지 사람이 확인해야 해요'
    return False, short or code or '알 수 없음', '허용 목록(PD·CC0·CC BY·CC BY-SA·공공누리 1유형)에 없어요'

def info(titles, width=0):
    out = {}
    for i in range(0, len(titles), 40):
        q = {'action': 'query', 'format': 'json', 'formatversion': '2', 'prop': 'imageinfo',
             'iiprop': 'url|size|mime|extmetadata', 'iiurlwidth': str(width or 3840), 'titles': '|'.join(titles[i:i + 40])}
        d = get(API + '?' + urllib.parse.urlencode(q))
        norm = {n['to']: n['from'] for n in d.get('query', {}).get('normalized', [])}
        for p in d.get('query', {}).get('pages', []):
            out[norm.get(p['title'], p['title'])] = p
            out[p['title']] = p
    return out

def describe(p):
    if p.get('missing') or not p.get('imageinfo'):
        return None
    ii = p['imageinfo'][0]; m = ii.get('extmetadata', {})
    ok, lic, why = lic_ok(m)
    artist = plain(m.get('Artist', {}).get('value', '')) or plain(m.get('Credit', {}).get('value', ''))
    restr = plain(m.get('Restrictions', {}).get('value', ''))
    return {'title': p['title'], 'page': ii.get('descriptionurl', ''), 'url': ii.get('url', ''), 'thumb': ii.get('thumburl', ''),
            'w': ii.get('width'), 'h': ii.get('height'), 'size': ii.get('size'), 'tw': ii.get('thumbwidth'), 'th': ii.get('thumbheight'),
            'mime': ii.get('mime', ''), 'ok': ok, 'license': lic, 'why': why,
            'license_url': plain(m.get('LicenseUrl', {}).get('value', '')), 'artist': artist[:120],
            'date': plain(m.get('DateTimeOriginal', {}).get('value', ''))[:40], 'desc': plain(m.get('ImageDescription', {}).get('value', ''))[:300],
            'restrictions': restr, 'categories': plain(m.get('Categories', {}).get('value', ''))[:300]}

def warn_people(d):
    w = []
    r = (d.get('restrictions') or '').lower()
    if 'personality' in r: w.append('인물 권리(personality rights) 표시가 있어요 → 실제 사람 사진이면 쓰지 말고 사용자에게 맡겨요')
    if 'trademark' in r: w.append('상표 표시가 있어요 → 로고가 중심인 그림이면 쓰지 않아요')
    if re.search(r'(?i)\b(portraits?|people|men|women|children|persons|selfies?|crowds?|faces?)\b', d.get('categories', '') + ' ' + d.get('desc', '')) and re.search(r'(?i)jpe?g', d.get('mime', '') + d['title']):
        w.append('사람이 나오는 사진일 수 있어요 → 얼굴이 알아볼 만하게 크면 쓰지 않아요(그림·조각·옛 판화는 괜찮아요)')
    return w

def cr_line(d):
    who = d['artist']
    if re.fullmatch(r'(?i)(unknown|anonymous|unknown author|author unknown)?', who or ''): who = ''
    who = re.sub(r'(?i)^own work\b.*', '', who).strip()
    return ' · '.join([x for x in [who, d['license'], '위키미디어 공용'] if x])

def safe(name):
    name = name.split(':', 1)[1]
    base, ext = os.path.splitext(name)
    base = re.sub(r'[^A-Za-z0-9가-힣._-]+', '_', base).strip('_')[:80] or 'file'
    return base + ext.lower()

def search(q, n=20):
    d = get(API + '?' + urllib.parse.urlencode({'action': 'query', 'format': 'json', 'formatversion': '2', 'list': 'search', 'srsearch': q, 'srnamespace': '6', 'srlimit': str(n)}))
    ts = [x['title'] for x in d.get('query', {}).get('search', [])]
    if not ts: print('찾은 파일이 없어요. 다른 낱말(영어·현지어)로 찾아보세요.'); return
    I = info(ts, 330)
    for t in ts:
        x = describe(I.get(t, {}))
        if not x: continue
        print(('  쓸 수 있음 ' if x['ok'] else '  안 됨      ') + f"{x['license'][:22]:22} {x['w']}×{x['h']}  {t}")
        print(f"             {x['page']}")
        if x['desc']: print(f"             {x['desc'][:110]}")

def est(x, width):
    is_img = x['mime'].startswith('image/') and not x['mime'].endswith('svg+xml')
    if x['mime'].endswith('svg+xml') and x.get('tw'): return int(x['tw'] * (x['th'] or x['tw']) * 0.5)   # SVG는 위키미디어가 그린 PNG로
    if not width: return x.get('size') or 0                      # 원본
    if is_img and x.get('tw') and x['w'] and x['w'] > width:
        return int(x['tw'] * (x['th'] or x['tw']) * 0.25)          # 받는 원본(JPEG) 크기 어림. 사이트에는 WebP로 줄여 넣어요
    return x.get('size') or 0

def read_list(path):
    """묶음 목록 파일: 한 줄에 ‘카드id File:이름.jpg’ (# 뒤는 메모)"""
    pairs = []
    for ln in open(path, encoding='utf-8'):
        ln = ln.split('#', 1)[0].strip()
        if not ln: continue
        cid, t = ln.split(None, 1)
        pairs.append((cid, t.strip()))
    return pairs

def plan(pairs, width=0):
    """받기 전에 사용자에게 보여 줄 목록(이름 · 어디서 · 크기 · 라이선스). 아무것도 받지 않아요. 위키미디어에 한 번만 물어요."""
    I = info(sorted({title_of(t) for _, t in pairs}), width)
    tot, n = 0, 0
    print('받을 파일 목록 · 출처: 위키미디어 공용(commons.wikimedia.org) · 받는 곳: 이 창의 작업 공간(사용자 컴퓨터 아님)')
    last = None
    for cid, t in pairs:
        if cid != last: print(f'[{cid}]'); last = cid
        x = describe(I.get(title_of(t), {}))
        if not x: print(f'  ✗ 없는 파일: {title_of(t)}'); continue
        if not x['ok']: print(f"  ✗ 못 씀: {x['title']} — {x['license']} ({x['why']})"); continue
        b = est(x, width); tot += b; n += 1
        print(f"  · {x['title'][5:]} — 약 {max(1, b // 1024)}KB · {x['license']}" + ('  ⚠ 100MB 넘는 원본: 사용자님 허락을 받은 뒤 --allow-big(허락이 없으면 --width 3840)' if not width and b > MAX_ORIG else ''))
        for w in warn_people(x): print(f'      ⚠ {w}')
    print(f'모두 {n}개 · 약 {tot / 1024 / 1024:.1f}MB')

def thumb_alts(pairs, I, width):
    if not width:                                   # 원본 모드: 큰 원본은 3840 미리보기, 작은 원본은 한 단계 작은 표준 너비
        alt = {t: d['thumb'] for t, d in ((title_of(t), describe(I[title_of(t)]) if I.get(title_of(t)) else None) for _, t in pairs) if d and d['ok'] and d['thumb'] and d['thumb'] != d['url']}
        width = 3840
        rest = [(c, t) for c, t in pairs if title_of(t) not in alt]
        alt.update(thumb_alts(rest, I, width) if rest else {})
        return alt
    """--thumb-only: 원본이 받을 너비보다 작은 그림은 원본보다 한 단계 작은 표준 너비 미리보기 주소로(원본 주소가 더 자주 막혀요)"""
    alt, groups = {}, {}
    for _, t in pairs:
        tt = title_of(t); p = I.get(tt); x = describe(p) if p else None
        if not x or not x['ok']: continue
        if x['mime'].startswith('image/') and not x['mime'].endswith('svg+xml') and x['w'] and x['w'] <= width:
            c = [w2 for w2 in STD_W if 500 <= w2 < x['w']]
            if c: groups.setdefault(max(c), set()).add(tt)
    for w2, ts in groups.items():
        I2 = info(sorted(ts), w2)
        for tt in ts:
            y = describe(I2[tt]) if I2.get(tt) else None
            if y and y['thumb'] and y['thumb'] != y['url']: alt[tt] = y['thumb']
    return alt

def target(x, width, alt):
    """(그림인가, 받을 주소, 저장할 파일 이름) — 받기·받기 파일이 같은 규칙을 써요. width 0: 원본(SVG는 위키미디어가 그린 3840 PNG)"""
    svg = x['mime'].endswith('svg+xml')
    is_img = x['mime'].startswith('image/') and not svg
    if svg and x['thumb']: url = x['thumb']; is_img = True
    elif not width: url = alt.get(x['title'], x['url'])
    else: url = x['thumb'] if (is_img and x['thumb'] and x['w'] and x['w'] > width) else alt.get(x['title'], x['url'])
    fn = safe(x['title'])
    if is_img and url != x['url']:
        tx = os.path.splitext(urllib.parse.urlparse(url).path)[1].lower() or '.jpg'
        if not fn.lower().endswith(tx): fn += tx
    return is_img, url, fn

def too_big(x, width, url, allow_big):
    """원본이 100MB를 넘는데 아직 허락이 없으면 True(받지 않고 사용자님께 여쭤요)"""
    return (not allow_big) and url == x['url'] and (x.get('size') or 0) > MAX_ORIG

def snippet_line(cid, fn, xx, is_img):
    key = re.sub(r'[^a-z0-9]+', '', os.path.splitext(fn)[0].lower())[:10] or 'img'
    if is_img:
        return f"    '{key}': {{'src': '{cid}/{fn}', 'cap': '', 'cr': {json.dumps(cr_line(xx), ensure_ascii=False)}, 'u': {json.dumps(xx['page'])}, 'alt': ''}},"
    return f"    # 소리: {{'file': '{cid}/{fn}', 'cr': {json.dumps(cr_line(xx), ensure_ascii=False)}, 'u': {json.dumps(xx['page'])}}}"

def print_snippets(snippet):
    for cid, sn in snippet.items():
        print(f'\n[{cid}] 카드 자료 images에 붙여 넣을 줄(이름표·cap·alt는 직접 채우고, cr 작가 이름 앞에 “사진:”이나 뒤에 “그림”을 붙여요):')
        print('\n'.join(sn))

# ---------- 사용자 컴퓨터로 받기(그림 받기 파일) ----------
# 여러 창이 같은 인터넷 길로 받으면 위키미디어가 오래 막아요. 사용자 컴퓨터는 다른 길이라, 사용자가 더블클릭 한 번으로 받게 해요.
USER_OUT = os.environ.get('DEEP_USER_OUT') or '/mnt/user-data/outputs/deep/user_get'
BAT_UA = 'CardbookDeepKit/1.0 (+https://cardbook.hunji08423.workers.dev/; run by the site owner) curl'
KEEP = ('title', 'page', 'url', 'thumb', 'w', 'h', 'size', 'tw', 'th', 'mime', 'ok', 'license', 'why', 'license_url', 'artist', 'date', 'desc', 'restrictions', 'categories')

def ascii_name(fn, title):
    """받기 파일(.bat)에 쓸 이름은 영문·숫자로만(한글이 있으면 짧은 표시를 붙여 바꿔요)"""
    if all(ord(c) < 128 for c in fn): return fn
    import hashlib
    base, ext = os.path.splitext(fn)
    a = re.sub(r'[^A-Za-z0-9._-]+', '_', base).strip('_')[:60]
    return (a + '_' if a else 'file_') + hashlib.sha1(title.encode('utf-8')).hexdigest()[:8] + ext

def bat_text(name, items):
    """사용자 컴퓨터(윈도우)에서 더블클릭으로 도는 받기 파일. curl.exe(윈도우 10·11에 들어 있음)로 한 파일씩 천천히 받아요.
    받는 곳: 이 파일이 있는 ‘그림_받기’ 폴더 옆의 deep_src/<카드id>/. 이미 있는 파일은 건너뛰어요(다시 더블클릭하면 남은 것만)."""
    L = ['@echo off', 'chcp 949 >nul', 'setlocal', f'title 그림 받기 - {name}',
         'echo ================================================',
         f'echo  그림 받기 - {name} : 위키미디어 공용에서 {len(items)}개',
         'echo  받는 곳: Christ.culture 폴더 안 deep_src',
         'echo  끝날 때까지 이 창을 닫지 말아 주세요.',
         'echo ================================================',
         'where curl.exe >nul 2>nul || goto nocurl',
         'if not exist "%~dp0..\\deep_src" mkdir "%~dp0..\\deep_src"',
         'cd /d "%~dp0..\\deep_src" || goto nodir',
         f'set "UA={BAT_UA}"',
         f'set /a TOTAL={len(items)}', 'set /a N=0', 'set /a OKN=0', 'set /a BAD=0', 'set /a HAVE=0']
    for it in items:
        L += [f'set "F={it["cid"]}\\{it["file"]}"', 'set "U=' + it['from'].replace('%', '%%') + '"', 'call :get']
    L += ['echo.', 'echo ------------------------------------------------',
          'echo  새로 받음 %OKN%개, 이미 있음 %HAVE%개, 받지 못함 %BAD%개',
          'if %BAD% GTR 0 goto somebad',
          'echo  다 받았어요. Claude 창에 "받았어요"라고 알려 주세요.',
          'goto end',
          ':somebad',
          'echo  받지 못한 파일이 있어요. 10분쯤 뒤 이 파일을 다시 더블클릭하면',
          'echo  남은 것만 이어서 받아요. 그래도 안 되면 창에 그대로 알려 주세요.',
          'goto end',
          ':nocurl',
          'echo  이 컴퓨터에서 curl을 찾지 못했어요. Claude 창에 "curl이 없대요"라고 알려 주세요.',
          'goto end',
          ':nodir',
          'echo  deep_src 폴더를 열지 못했어요. Claude 창에 그대로 알려 주세요.',
          'goto end',
          ':get',
          'set /a N+=1',
          'if exist "%F%" goto have',
          'echo  [%N%/%TOTAL%] %F%',
          'curl.exe -f -L -sS --connect-timeout 20 --max-time 300 --retry 2 --retry-max-time 90 -A "%UA%" --create-dirs -o "%F%.part" "%U%"',
          'if errorlevel 1 goto bad',
          'move /y "%F%.part" "%F%" >nul',
          'set /a OKN+=1',
          'call :rest 2',
          'exit /b 0',
          ':have',
          'echo  [%N%/%TOTAL%] 이미 있음: %F%',
          'set /a HAVE+=1',
          'exit /b 0',
          ':bad',
          'if exist "%F%.part" del "%F%.part" >nul 2>nul',
          'echo             받지 못했어요. 나중에 다시 받아요.',
          'set /a BAD+=1',
          'call :rest 5',
          'exit /b 0',
          ':rest',
          'timeout /t %1 /nobreak >nul 2>nul || ping -n %1 127.0.0.1 >nul',
          'exit /b 0',
          ':end',
          'echo.',
          'pause',
          'endlocal']
    return '\r\n'.join(L) + '\r\n'

def ask_big(asks):
    if not asks: return
    print(f'\n100MB 넘는 원본 {len(asks)}개는 받지 않았어요. 사용자님께 이렇게 여쭤요(허락하시면 같은 명령에 --allow-big, 아니면 --width 3840):')
    print('[큰 원본 허락 부탁] 위키미디어 공용 · ' + ' / '.join(f"{x['title'][5:]} 약 {(x.get('size') or 0) / 1e6:.0f}MB ({x['w']}×{x['h']}px)" for x in asks))
    for x in asks: print('   ' + x['page'])

def user_bat(pairs, name, device=None, width=0, thumb_only=False, allow_big=False):
    """받기 파일(.bat)과 목록(.json)을 만들어요. 위키미디어 API(정보)에만 물어요. 파일은 받지 않아요."""
    if width and width not in STD_W: print(f'너비 {width}은 표준이 아니라 3840으로 바꿨어요'); width = 3840
    if not re.fullmatch(r'[0-9A-Za-z가-힣_-]{1,30}', name or ''): raise SystemExit('--name은 ‘묶음17’처럼 짧게(글자·숫자·_-만) 적어요')
    I = info(sorted({title_of(t) for _, t in pairs}), width)
    alt = thumb_alts(pairs, I, width) if thumb_only else {}
    items, seen, have, asks = [], set(), 0, []
    for cid, t in pairs:
        tt = title_of(t); p = I.get(tt); x = describe(p) if p else None
        if not x: print(f'✗ 없는 파일: {tt}'); continue
        if not x['ok']: print(f"✗ 넣지 않음: {tt} — {x['license']} ({x['why']})"); continue
        is_img, url, fn = target(x, width, alt)
        if too_big(x, width, url, allow_big): asks.append(x); continue
        fn = ascii_name(fn, tt)
        if (cid, fn) in seen: continue
        seen.add((cid, fn))
        try: S = json.load(open(os.path.join(SRCROOT, cid, '_sources.json'), encoding='utf-8'))
        except Exception: S = {}
        if os.path.exists(os.path.join(SRCROOT, cid, fn)) and fn in S: have += 1; continue
        for w in warn_people(x): print(f'  ⚠ {tt}: {w}')
        it = {k: x.get(k) for k in KEEP}; it.update({'cid': cid, 'file': fn, 'from': url, 'is_img': is_img})
        items.append(it)
    if have: print(f'= 작업 공간에 이미 있는 파일 {have}개는 넣지 않았어요')
    ask_big(asks)
    if not items: print('받기 파일에 넣을 것이 없어요(모두 이미 있거나 쓸 수 없어요).'); return
    os.makedirs(USER_OUT, exist_ok=True)
    bp, mp, tp = os.path.join(USER_OUT, name + '.bat'), os.path.join(USER_OUT, name + '.json'), os.path.join(USER_OUT, name + '.txt')
    open(bp, 'w', encoding='cp949', errors='replace', newline='').write(bat_text(name, items))
    # 손으로 넣을 때를 위한 목록(더블클릭이 안 될 때만): 주소는 이미 알맞은 크기예요
    T = [f'그림 받기 목록 · {name} (위키미디어 공용)',
         '더블클릭이 안 될 때만 이 목록을 써요. 주소를 열어 그림을 ‘다른 이름으로 저장’하고, ‘넣을 곳’에 적힌 폴더와 이름 그대로 넣어 주세요.',
         '주소는 이미 알맞은 크기예요(더 크게 받지 않아도 돼요).', '']
    for k, it in enumerate(items, 1):
        T += [f"{k}. {it['from']}", f"   → 넣을 곳: Christ.culture\\deep_src\\{it['cid']}\\{it['file']}", '']
    open(tp, 'w', encoding='utf-8-sig', newline='\r\n').write('\n'.join(T))
    json.dump({'name': name, 'made': datetime.date.today().isoformat(), 'width': width, 'items': items}, open(mp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    est_mb = sum(est(dict(it), width) for it in items) / 1024 / 1024
    print(f'\n받기 파일을 만들었어요: 그림·소리 {len(items)}개 · 약 {est_mb:.1f}MB')
    print('  ' + bp + '\n  ' + mp + '\n  ' + tp)
    if device:
        dev = device.rstrip('\\/'); P = ntpath if ('\\' in dev or (len(dev) > 1 and dev[1] == ':')) else posixpath
        cc = P.dirname(dev)
        cm = [{'stagedPath': bp, 'devicePath': P.join(cc, '그림_받기', name + '.bat')},
              {'stagedPath': mp, 'devicePath': P.join(cc, '그림_받기', name + '.json')},
              {'stagedPath': tp, 'devicePath': P.join(cc, '그림_받기', name + '.txt')}]
        json.dump(cm, open(os.path.join(USER_OUT, f'commit_{name}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        paths = [P.join(cc, 'deep_src', it['cid'], it['file']) for it in items]
        sl = [paths[k:k + 50] for k in range(0, len(paths), 50)]
        for n, ch in enumerate(sl, 1):
            json.dump(ch, open(os.path.join(USER_OUT, f'stage_{name}_{n}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print(f'\n1) 사용자 폴더에 넣기: {os.path.join(USER_OUT, f"commit_{name}.json")} 내용을 그대로 device_commit_files의 files에')
        print(f'2) 사용자가 “받았어요” 하면 가져오기: stage_{name}_1.json …의 경로 목록을 device_stage_files의 paths에(50개씩, {len(sl)}번)')
        print(f'3) 그다음: python3 tools/deep/kit/commons_get.py --import {mp}')
    print(f'\n사용자에게 보낼 말(GUIDE.md 3-3):\n[그림 받기 부탁] {name} · 그림 {len(items)}개 · 약 {est_mb:.0f}MB(위키미디어 공용)')

# ---------- 이미 받은 그림의 원본 다시 받기(본부 · 2026-11-18) ----------
# 2026-11-18까지는 위키미디어가 줄여 준 판(긴 쪽 1920px 안팎)을 받았어요. 사용자님 결정: 처음부터 원본으로 다시 받아요.
# 원본은 같은 카드 폴더의 _orig/에 받아요(지금 파일은 그대로 둬요). build.py는 _orig/에 원본이 있으면 그것으로 그림을 만들어요.
ORIG_DER = ('derived', 'derived_from', 'basis', 'how', 'edit')       # 창이 자르거나 붙여 만든 그림: 원본으로 바꾸면 안 돼요(손으로 다시 만들어요)
EXT_OF = {'image/jpeg': ('.jpg', '.jpeg'), 'image/png': ('.png',), 'image/tiff': ('.tif', '.tiff'), 'image/gif': ('.gif',), 'image/webp': ('.webp',)}

def orig_name(fn, mime):
    """받아 둔 파일 이름 → _orig/ 안의 원본 이름(형식이 달라 ‘.jpg’를 붙였던 것은 원래 확장자로)"""
    ext = EXT_OF.get(mime, ())
    if not ext or fn.lower().endswith(ext): return fn
    st = fn[:-4] if fn.lower().endswith('.jpg') else fn
    return st if st.lower().endswith(ext) else st + ext[0]

def orig_items(card_dir=None, src_root=None, only=None):
    """카드가 쓰는 그림 가운데 줄여 준 판(…/thumb/…)으로 받은 것의 원본 목록. 위키미디어에 묻지 않아요(_sources.json의 원본 주소·크기)."""
    import glob, importlib.util
    card_dir = card_dir or os.path.join(REPO, 'tools', 'deep', 'cards'); src_root = src_root or SRCROOT
    sys.path.insert(0, KIT)
    uses = {}
    for p in sorted(glob.glob(os.path.join(card_dir, '*.py'))):
        try:
            spec = importlib.util.spec_from_file_location('oc_' + os.path.basename(p)[:-3].replace('-', '_'), p)
            m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); C = m.CARD
        except Exception as ex:
            print(f'  (카드 파일을 읽지 못했어요: {os.path.basename(p)} — {type(ex).__name__})'); continue
        if only and C['id'] not in only: continue
        for k, im in (C.get('images') or {}).items():
            if im.get('src') and not os.path.isabs(im['src']): uses.setdefault(im['src'].replace('\\', '/'), []).append((C['id'], k))
    items, skip = [], {}
    for s, us in sorted(uses.items()):
        cid, fn = s.split('/', 1)
        try: S = json.load(open(os.path.join(src_root, cid, '_sources.json'), encoding='utf-8'))
        except Exception: S = {}
        r = S.get(fn)
        why = None
        if not isinstance(r, dict): why = '출처 기록 없음(직접 그린 그림 등)'
        elif any(k in r for k in ORIG_DER): why = '자르거나 붙여 만든 그림(손으로 다시 만들어요)'
        elif '/thumb/' not in (r.get('from') or ''): why = '이미 원본'
        elif not (r.get('mime') or '').startswith('image/') or r.get('mime') == 'image/svg+xml': why = '그림 아님·SVG'
        elif not r.get('url') or '/thumb/' in r['url']: why = '원본 주소 없음'
        if why: skip.setdefault(why, []).append(s); continue
        items.append({'cid': cid, 'src': fn, 'file': '_orig/' + orig_name(fn, r['mime']), 'from': r['url'].split('?', 1)[0], 'size': int(r.get('size') or 0),
                      'w': r.get('w'), 'h': r.get('h'), 'mime': r['mime'], 'title': r.get('title'), 'page': r.get('page'), 'keys': [k for _, k in us]})
    return items, skip

def orig_bat_text(name, items):
    """원본 받기 파일(2판): 셋씩 함께 받아요(위키미디어 권장 동시 3개 이하). 받는 동안 진행 줄이 보여요.
    다 받은 파일만 제 이름이 돼요(받는 중에는 .part). 중간에 닫아도 다시 더블클릭하면 받던 데서 이어 받아요.
    curl이 함께 받기를 모르면(옛 윈도우) 하나씩 받아요."""
    tot = sum(it['size'] for it in items) / 1024 / 1024
    for it in items:
        bad = [c for c in it['from'] + it['file'] if c in '!^&<>|" ']
        if bad: raise SystemExit(f'받기 파일에 쓸 수 없는 글자: {it["cid"]}/{it["file"]} {bad}')
    L = ['@echo off', 'chcp 949 >nul', 'setlocal EnableDelayedExpansion', f'title 원본 받기 - {name}',
         'echo ================================================',
         f'echo  원본 받기 - {name} : 위키미디어 공용에서 {len(items)}개 (모두 약 {tot / 1024:.1f}GB)',
         'echo  받는 곳: Christ.culture 폴더 안 deep_src\\카드\\_orig',
         'echo  지금 있는 그림은 지우지 않아요. 중간에 닫아도 다시 더블클릭하면 이어서 받아요.',
         'echo ================================================',
         'where curl.exe >nul 2>nul || goto nocurl',
         'if not exist "%~dp0..\\deep_src" goto nodir',
         'cd /d "%~dp0..\\deep_src" || goto nodir',
         f'set "UA={BAT_UA}"',
         'set "CFG=%TEMP%\\cardbook_orig_get.txt"',
         'set "SEQ="',
         'curl.exe --parallel --version >nul 2>nul || set "SEQ=1"',
         'echo  남은 파일을 세는 중이에요...',
         'if exist "%CFG%" del "%CFG%"',
         'set /a NEED=0', 'set /a HAVE=0', 'set /a OKN=0', 'set /a BAD=0',
         'set "MODE=add"', 'call :items',
         'if %NEED% EQU 0 goto fin',
         'echo  받을 파일 %NEED%개 · 이미 받은 파일 %HAVE%개',
         'if defined SEQ goto seq',
         'echo  셋씩 함께 받아요. 아래 줄의 Xfers는 남은 파일 수, Speed는 받는 속도예요.',
         'echo  (어떤 파일은 위키미디어가 천천히 보내요. 멈춘 것처럼 보여도 Dled 숫자가 늘면 받는 중이에요)',
         'curl.exe --parallel --parallel-max 3 -f -L -C - --retry 4 --connect-timeout 30 --speed-limit 2000 --speed-time 300 -A "%UA%" --create-dirs --config "%CFG%"',
         'goto fin',
         ':seq',
         'echo  하나씩 받아요(이 컴퓨터의 curl은 함께 받기를 몰라요).',
         'set "MODE=seq"', 'call :items',
         ':fin',
         'set /a OKN=0', 'set /a BAD=0', 'set "MODE=fin"', 'call :items',
         'if exist "%CFG%" del "%CFG%"',
         'echo.', 'echo ------------------------------------------------',
         'echo  다 받은 원본 %OKN%개, 받지 못함 %BAD%개',
         'if %BAD% GTR 0 goto somebad',
         'echo  다 받았어요. Claude 창에 "원본 다 받았어요"라고 알려 주세요.',
         'goto end',
         ':somebad',
         'echo  받지 못한 파일이 있어요. 10분쯤 뒤 이 파일을 다시 더블클릭하면',
         'echo  받던 데서 이어서 받아요. 그래도 안 되면 창에 그대로 알려 주세요.',
         'goto end',
         ':nocurl',
         'echo  이 컴퓨터에서 curl을 찾지 못했어요. Claude 창에 "curl이 없대요"라고 알려 주세요.',
         'goto end',
         ':nodir',
         'echo  deep_src 폴더를 찾지 못했어요. 이 파일이 Christ.culture\\그림_받기 폴더에 있는지 봐 주세요.',
         'goto end',
         ':items']
    for it in items:
        win = f'{it["cid"]}\\' + it['file'].replace('/', '\\')
        L += [f'set "F={win}"', f'set "G={it["cid"]}/{it["file"]}"', 'set "U=' + it['from'].replace('%', '%%') + '"', f'set "SZ={it["size"]}"', 'call :one']
    L += ['exit /b 0',
          ':one',
          'set "CUR=0"',
          'if exist "!F!" for %%A in ("!F!") do set "CUR=%%~zA"',
          'if "%MODE%"=="add" goto one_add',
          'if "%MODE%"=="seq" goto one_seq',
          'if exist "!F!.part" for %%A in ("!F!.part") do if %%~zA GEQ !SZ! move /y "!F!.part" "!F!" >nul',
          'set "CUR=0"',
          'if exist "!F!" for %%A in ("!F!") do set "CUR=%%~zA"',
          'if !CUR! GEQ !SZ! (set /a OKN+=1) else (set /a BAD+=1)',
          'exit /b 0',
          ':one_add',
          'if !CUR! GEQ !SZ! (set /a HAVE+=1 & exit /b 0)',
          '>>"%CFG%" echo url = !U!',
          '>>"%CFG%" echo output = !G!.part',
          'set /a NEED+=1',
          'exit /b 0',
          ':one_seq',
          'if !CUR! GEQ !SZ! exit /b 0',
          'echo  !F!',
          'curl.exe -f -L -C - --progress-bar --retry 4 --connect-timeout 30 --speed-limit 2000 --speed-time 300 -A "%UA%" --create-dirs -o "!F!.part" "!U!"',
          'timeout /t 2 /nobreak >nul 2>nul || ping -n 2 127.0.0.1 >nul',
          'exit /b 0',
          ':end',
          'echo.',
          'pause',
          'endlocal']
    return '\r\n'.join(L) + '\r\n'

def orig_bat(name, device=None, card_dir=None, src_root=None, only=None, allow_big=False):
    """원본 받기 파일(.bat)·목록(.json)·손으로 받을 때의 목록(.txt)을 만들어요. 아무것도 받지 않아요."""
    if not re.fullmatch(r'[0-9A-Za-z가-힣_-]{1,30}', name or ''): raise SystemExit('--name은 ‘원본받기’처럼 짧게(글자·숫자·_-만) 적어요')
    items, skip = orig_items(card_dir, src_root, only)
    for it in items:
        if not all(ord(c) < 128 for c in it['file']): raise SystemExit(f'영문이 아닌 파일 이름: {it["cid"]}/{it["file"]}')
    seen = {}
    for it in items:
        kk = (it['cid'], it['file'].lower())
        if kk in seen: raise SystemExit(f'원본 이름이 겹쳐요: {it["cid"]}/{it["file"]} ({seen[kk]} · {it["src"]})')
        seen[kk] = it['src']
    big = [it for it in items if it['size'] > MAX_ORIG]
    if big and not allow_big:
        print('100MB 넘는 원본은 넣지 않았어요(사용자님께 이름·크기·출처를 보여 드리고 허락을 받은 뒤 --allow-big):')
        for it in big: print(f"  · {it['cid']}/{it['src']} — 약 {it['size'] / 1e6:.0f}MB · {it['page']}")
        items = [it for it in items if it['size'] <= MAX_ORIG]
    print(f'원본 받기: {len(items)}개 · 모두 약 {sum(i["size"] for i in items) / 1e9:.2f}GB' + (f' (100MB 넘는 것 {len(big)}개 포함 · 사용자님 허락)' if big and allow_big else ''))
    for why, ss in skip.items(): print(f'  넣지 않음 · {why}: {len(ss)}개')
    os.makedirs(USER_OUT, exist_ok=True)
    bp, mp, tp = (os.path.join(USER_OUT, name + x) for x in ('.bat', '.json', '.txt'))
    open(bp, 'w', encoding='cp949', errors='strict', newline='').write(orig_bat_text(name, items))
    json.dump({'name': name, 'made': datetime.date.today().isoformat(), 'kind': 'orig', 'items': items}, open(mp, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    T = [f'원본 받기 목록 · {name} (위키미디어 공용)', '더블클릭이 안 될 때만 이 목록을 써요. 주소를 열어 ‘다른 이름으로 저장’하고, ‘넣을 곳’에 그대로 넣어 주세요.', '']
    for k, it in enumerate(items, 1):
        T += [f"{k}. {it['from']}  (약 {max(1, round(it['size'] / 1024 / 1024))}MB)", f"   → 넣을 곳: Christ.culture\\deep_src\\{it['cid']}\\{it['file'].replace('/', chr(92))}", '']
    open(tp, 'w', encoding='utf-8-sig', newline='\r\n').write('\n'.join(T))
    print('  ' + bp + '\n  ' + mp + '\n  ' + tp)
    if device:
        dev = device.rstrip('\\/'); P = ntpath if ('\\' in dev or (len(dev) > 1 and dev[1] == ':')) else posixpath
        cc = P.dirname(dev)
        cm = [{'stagedPath': x, 'devicePath': P.join(cc, '그림_받기', os.path.basename(x))} for x in (bp, mp, tp)]
        json.dump(cm, open(os.path.join(USER_OUT, f'commit_{name}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print(f'사용자 폴더에 넣기: {os.path.join(USER_OUT, f"commit_{name}.json")} 내용을 그대로 device_commit_files의 files에')
    return items

def import_user(manifest, folder=None):
    """사용자가 받은 파일을 작업 공간 deep_src로 옮기고 _sources.json에 출처를 적어요."""
    M = json.load(open(manifest, encoding='utf-8'))
    folder = folder or '/mnt/user-data/uploads/Christ.culture/deep_src'
    books, snippet, missing, bad = {}, {}, [], []
    def save(cid):
        json.dump(books[cid], open(os.path.join(SRCROOT, cid, '_sources.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for it in M['items']:
        cid, fn = it['cid'], it['file']
        src = os.path.join(folder, cid, fn)
        if not os.path.exists(src): missing.append(f'{cid}/{fn}'); continue
        nb = os.path.getsize(src)
        if it.get('is_img'):
            try:
                from PIL import Image
                with Image.open(src) as im: im.verify()
            except Exception:
                bad.append(f'{cid}/{fn}'); continue
        elif nb < 1000:
            bad.append(f'{cid}/{fn}'); continue
        od = os.path.join(SRCROOT, cid); os.makedirs(od, exist_ok=True)
        dst = os.path.join(od, fn)
        if os.path.abspath(src) != os.path.abspath(dst): shutil.copy2(src, dst)
        if cid not in books:
            try: books[cid] = json.load(open(os.path.join(od, '_sources.json'), encoding='utf-8'))
            except Exception: books[cid] = {}
        rec = {k: it.get(k) for k in KEEP}
        rec.update({'file': fn, 'got': datetime.date.today().isoformat(), 'bytes': nb, 'from': it['from'], 'via': '사용자 컴퓨터에서 받음(그림 받기 파일 ' + M['name'] + ')'})
        books[cid][fn] = rec; save(cid)
        snippet.setdefault(cid, []).append(snippet_line(cid, fn, rec, it.get('is_img')))
        print(f"✓ 가져옴: {cid}/{fn}  ({nb // 1024}KB, {rec['license']})")
    print_snippets(snippet)
    if books: print('\n출처 기록:', ', '.join(os.path.join(SRCROOT, c, '_sources.json') for c in books))
    if bad: print(f'\n열리지 않는 파일 {len(bad)}개(받다가 깨졌을 수 있어요). 사용자 폴더의 그 파일을 지워 달라고 하지 말고, 받기 파일을 다시 만들어(--user-bat) 새 이름으로 받게 해요:\n  ' + '\n  '.join(bad))
    if missing: print(f'\n아직 없는 파일 {len(missing)}개: 사용자에게 받기 파일을 한 번 더 더블클릭해 달라고 하거나, 가져오기(device_stage_files)를 빠뜨렸는지 봐요.\n  ' + '\n  '.join(missing))

def fetch(pairs, width=0, thumb_only=False, allow_big=False):
    """목록의 파일을 받아요. 라이선스가 맞지 않거나 없는 파일은 건너뛰어요. 위키미디어 API에는 한 번만 물어요.
    - 파일 하나를 받을 때마다 _sources.json에 바로 적어요(중간에 멈춰도 출처가 남아요).
    - 위키미디어가 아주 오래 기다려 달라고 하면 그 파일은 미루고 다음 파일로 가요. 같은 명령을 나중에 다시 돌리면 남은 것만 받아요.
    - thumb_only: 원본이 받을 너비보다 작아 원본 주소로 받아야 할 때, 원본보다 한 단계 작은 표준 너비 미리보기로 받아요(원본 주소가 더 자주 막혀요)."""
    if width and width not in STD_W: print(f'너비 {width}은 표준이 아니라 3840으로 바꿨어요'); width = 3840
    I = info(sorted({title_of(t) for _, t in pairs}), width)
    alt = thumb_alts(pairs, I, width) if thumb_only else {}
    books, snippet, deferred, asks = {}, {}, [], []
    def save(cid):
        json.dump(books[cid], open(os.path.join(SRCROOT, cid, '_sources.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    try:
        for cid, t in pairs:
            od = os.path.join(SRCROOT, cid); os.makedirs(od, exist_ok=True)
            sj = os.path.join(od, '_sources.json')
            if cid not in books:
                try: books[cid] = json.load(open(sj, encoding='utf-8'))
                except Exception: books[cid] = {}
            S = books[cid]
            tt = title_of(t); p = I.get(tt)
            x = describe(p) if p else None
            if not x: print(f'✗ 없는 파일: {tt}'); continue
            if not x['ok']:
                print(f"✗ 받지 않음: {tt}\n   라이선스: {x['license']} — {x['why']}"); continue
            for w in warn_people(x): print(f'  ⚠ {tt}: {w}')
            is_img, url, fn = target(x, width, alt)
            if too_big(x, width, url, allow_big): asks.append(x); continue
            dst = os.path.join(od, fn)
            if os.path.exists(dst) and fn in S:
                print(f'= 이미 있음: {cid}/{fn}')
            else:
                try:
                    b = get(url, binary=True, max_wait=LONG_WAIT)
                except Deferred as d:
                    deferred.append((cid, t)); print(f'… 미룸: {cid}/{fn} (위키미디어가 {d.args[0]}초 기다려 달라고 해요)'); continue
                open(dst, 'wb').write(b)
                x['file'] = fn; x['got'] = datetime.date.today().isoformat(); x['bytes'] = len(b); x['from'] = url
                S[fn] = x; save(cid)
                print(f"✓ 받음: {cid}/{fn}  ({len(b)//1024}KB, {x['license']})")
            snippet.setdefault(cid, []).append(snippet_line(cid, fn, S.get(fn, x), is_img))
    finally:
        for cid in books: save(cid)
    print_snippets(snippet)
    if books: print('\n출처 기록:', ', '.join(os.path.join(SRCROOT, c, '_sources.json') for c in books))
    ask_big(asks)
    if deferred:
        print(f'\n미룬 파일 {len(deferred)}개: 위키미디어가 오래 기다려 달라고 했어요. 10분쯤 글을 쓰다가 같은 명령을 다시 돌리면, 이미 받은 파일은 건너뛰고 남은 것만 받아요.')
        print('계속 막히면 --thumb-only를 붙여 보세요(원본 대신 3840 미리보기로 받아요 · 나중에 본부가 원본으로 다시 받아요).')
        print('그래도 막히면 사용자 컴퓨터로 받아요: --user-bat (GUIDE.md 3-3 ‘그림 받기 부탁’).')
        for cid, t in deferred: print(f'  {cid} {title_of(t)}')

def nettest():
    """파일은 받지 않고, 세 주소에 닿는지만 봐요."""
    ok = True
    try:
        get(API + '?action=query&format=json&meta=siteinfo'); print('  ✓ commons.wikimedia.org (찾기·정보)')
    except Exception as ex:
        ok = False; print('  ✗ commons.wikimedia.org:', ex.args[0] if isinstance(ex, Blocked) else str(ex)[:120])
    for host in ('upload.wikimedia.org', 'thumb.wikimedia.org'):
        try:
            req = urllib.request.Request(f'https://{host}/', method='HEAD', headers={'User-Agent': UA})
            try:
                urllib.request.urlopen(req, timeout=30, context=ctx()).close()
            except urllib.error.HTTPError:
                pass                                   # 404 같은 답도 ‘닿았다’는 뜻이에요
            print(f'  ✓ {host} (파일 받기)')
        except (urllib.error.URLError, OSError) as ex:
            ok = False
            print(f'  ✗ {host}: 막혀 있어요' if re.search(r'Tunnel connection failed: 40[37]|Forbidden', str(ex)) else f'  ✗ {host}: {str(ex)[:120]}')
    print('인터넷 점검: ' + ('세 주소 모두 열려 있어요' if ok else '막힌 주소를 사용자에게 알려 주세요(설정 › 기능 › 허용 도메인)'))
    return ok

if __name__ == '__main__':
    a = sys.argv[1:]
    width = 0                     # 0 = 원본(기본)
    thumb_only = '--thumb-only' in a
    if thumb_only: a.remove('--thumb-only')
    if '--width' in a:
        i = a.index('--width'); width = int(a[i + 1]); del a[i:i + 2]
    name = device = None
    if '--name' in a:
        i = a.index('--name'); name = a[i + 1]; del a[i:i + 2]
    if '--device' in a:
        i = a.index('--device'); device = a[i + 1]; del a[i:i + 2]
    allow_big = '--allow-big' in a
    if allow_big: a.remove('--allow-big')
    if not a: print(__doc__); sys.exit(0)
    try:
        if a[0] == '--nettest': sys.exit(0 if nettest() else 2)
        elif a[0] == '--search': search(' '.join(a[1:]))
        elif a[0] == '--plan': plan([(a[1], t) for t in a[2:]], width)
        elif a[0] == '--plan-file': plan(read_list(a[1]), width)
        elif a[0] == '--fetch-file': fetch(read_list(a[1]), width, thumb_only, allow_big)
        elif a[0] == '--user-bat': user_bat(read_list(a[1]), name, device, width, thumb_only, allow_big)
        elif a[0] == '--import': import_user(a[1], a[2] if len(a) > 2 else None)
        elif a[0] == '--orig-bat': orig_bat(name, device, *(a[1:3] + [None] * (2 - len(a[1:3]))), set(a[3:]) or None, allow_big)
        elif a[0] == '--info':
            I = info([title_of(t) for t in a[1:]], width)
            for t in a[1:]:
                x = describe(I.get(title_of(t), {}))
                print(json.dumps(x, ensure_ascii=False, indent=1) if x else f'없는 파일: {t}')
                if x: [print('  ⚠', w) for w in warn_people(x)]
        else:
            fetch([(a[0], t) for t in a[1:]], width, thumb_only, allow_big)
    except (Blocked, urllib.error.URLError, OSError, ssl.SSLError) as ex:
        if isinstance(ex, urllib.error.HTTPError) and ex.code not in (403, 407):
            print('위키미디어가 오류를 돌려줬어요:', ex.code, ex.reason); sys.exit(1)
        no_net(ex)
