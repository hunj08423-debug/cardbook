# -*- coding: utf-8 -*-
"""[본부 전용] 깊은 카드 모아 보기 쪽(site/deep/index.html)을 만들어요.

사용자가 휴대폰·태블릿·컴퓨터에서 지금까지 만든 깊은 카드를 장·묶음별로 한눈에 보고,
카드마다 느낀 점을 적어 한꺼번에 복사해 본부에 보낼 수 있게 해요.

쓰는 법(저장소 맨 위에서):
  python3 tools/deep/kit/deep_index.py            → site/deep/index.html 다시 만들기
읽는 것: site/data/index.json(카드 제목·장·이어진 깊은 카드), tools/deep/BATCHES.md(묶음),
        tools/deep/status/*.md(상태·중심 방식·끝맺는 꼴), site/deep/*.html(만들어진 카드)
본부 점검 때마다 link_deep.py --write 다음에 돌려요. 사용자에게 GitHub Desktop으로 올려 달라고 해요.
"""
import os, re, json, glob, datetime, html

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))
e = lambda s: html.escape(str(s or ''), quote=True)

def batches():
    out = {}
    for line in open(os.path.join(REPO, 'tools', 'deep', 'BATCHES.md'), encoding='utf-8'):
        m = re.match(r'\|\s*(\d+)\s*\|\s*([^|]+)\|(.*)\|\s*\d+\s*\|', line)
        if not m: continue
        name = m.group(2).strip().split(' — ')[0]
        for cid in re.findall(r'`([a-z0-9-]+)`', m.group(3)): out[cid] = (int(m.group(1)), name)
    return out

def status(cid):
    p = os.path.join(REPO, 'tools', 'deep', 'status', cid + '.md')
    if not os.path.exists(p): return {}
    t = open(p, encoding='utf-8').read()
    def line(k):
        m = re.search(r'^- ' + k + r'\s*:\s*(.+)$', t, re.M)
        return m.group(1).strip() if m else ''
    st = line('상태')
    if '## 다듬기' in t: state = '다듬기 끝'
    elif '## 검수' in t: state = '검수 끝'
    elif re.search(r'예시|기준 카드', st) or (len(t) < 900 and '기준' in t): state = '기준 카드'
    elif re.search(r'만드는 중|조사 중|그림 허락|방식 기다림|만들기 전|그림 기다림', st): state = '만드는 중'
    else: state = '검토 전'
    meth = re.split(r'[(·]', line('중심 방식'))[0].strip()
    close = re.split(r'[(·]', line('끝맺는 꼴'))[0].strip()
    upd = line('마지막 갱신')
    return {'state': state, 'meth': meth, 'close': close, 'upd': upd, 'raw': st[:80]}

def main():
    ix = json.load(open(os.path.join(REPO, 'site', 'data', 'index.json'), encoding='utf-8'))
    B = batches(); deep = ix.get('deep', {})
    have = {os.path.basename(f)[:-5] for f in glob.glob(os.path.join(REPO, 'site', 'deep', '*.html'))} - {'index', 'sinai'}
    ids = sorted(set(deep) | have, key=lambda c: (B.get(c, (999, ''))[0], ix['sets'][ix['cards'][c]['set']]['cards'].index(c) if c in ix['cards'] else 0))
    ch_of = {c['id']: c for c in ix['chapters']}
    rows, counts = [], {}
    for cid in ids:
        if cid not in ix['cards']: continue
        c = ix['cards'][cid]; s = status(cid); b = B.get(cid, (0, ''))
        href = os.path.basename(deep.get(cid) or f'{cid}.html')
        st = s.get('state') or ('기준 카드' if cid == 'keep-sinai' else '검토 전')
        counts[st] = counts.get(st, 0) + 1
        rows.append({'id': cid, 't': c['t'], 'ch': c['ch'], 'b': b[0], 'bn': b[1], 'href': href, 'st': st,
                     'meth': s.get('meth', ''), 'close': s.get('close', ''), 'upd': s.get('upd', '')})
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%-m월 %-d일 %H:%M')
    groups = []
    for ch in ix['chapters']:
        rs = [r for r in rows if r['ch'] == ch['id']]
        if not rs: continue
        body = ''; last = None
        for r in rs:
            if r['b'] != last:
                if last is not None: body += '</ul>'
                body += f'<h3 class="bt">{"묶음 " + str(r["b"]) + " · " if r["b"] else ""}{e(r["bn"])}</h3><ul class="cards">'
                last = r['b']
            sub = ' · '.join(x for x in (r['meth'], ('끝맺기: ' + r['close']) if r['close'] else '') if x)
            body += (f'<li class="row" data-st="{e(r["st"])}" data-upd="{e(r["upd"])}" data-id="{e(r["id"])}">'
                     f'<a class="go" href="{e(r["href"])}"><img src="../img/c/{e(r["id"])}.webp" alt="" loading="lazy" width="56" height="70">'
                     f'<span class="tx"><b>{e(r["t"])}</b><span class="sub">{e(sub)}</span></span>'
                     f'<span class="chip c-{e(r["st"]).replace(" ", "")}">{e(r["st"])}</span></a>'
                     f'<button type="button" class="memo-b" aria-expanded="false">느낀 점</button>'
                     f'<div class="memo" hidden><textarea rows="3" aria-label="{e(r["t"])} 느낀 점" placeholder="이 카드를 보며 느낀 점을 적어 두세요. 이 기기에만 남아요."></textarea></div></li>')
        body += '</ul>'
        groups.append(f'<section class="chap"><h2>{ch["no"]}장 {e(ch["t"])} <span>{len(rs)}장</span></h2>{body}</section>')
    total = len(rows)
    summary = ' · '.join(f'{k} {counts[k]}' for k in ('검토 전', '만드는 중', '검수 끝', '다듬기 끝', '기준 카드') if counts.get(k))
    page = TPL.replace('{{GROUPS}}', '\n'.join(groups)).replace('{{TOTAL}}', str(total)).replace('{{SUMMARY}}', e(summary)).replace('{{NOW}}', now)
    out = os.path.join(REPO, 'site', 'deep', 'index.html')
    open(out, 'w', encoding='utf-8').write(page)
    print(f'만들었어요: site/deep/index.html · 카드 {total}장 · {summary}')

TPL = '''<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>깊은 카드 모아 보기</title>
<meta name="robots" content="noindex">
<link rel="icon" href="../icon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=IBM+Plex+Sans+KR:wght@400;500;600&display=swap">
<style>
:root{--ground:#EAE5DB;--leaf:#F7F4EE;--ink:#2A231C;--ink2:#62584B;--ink3:#8D8374;--rule:#D8CFC0;--lapis:#233A7C;--verm:#AE3328;--gold:#B38B3D;--green:#2E6B4F;
 --serif:"Gowun Batang","Noto Serif KR","Nanum Myeongjo",serif;--sans:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif;color-scheme:light}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ground:#11162C;--leaf:#181E38;--ink:#EAE3D3;--ink2:#ABA290;--ink3:#7E7767;--rule:#2B3254;--lapis:#8EA6EA;--verm:#E26C5F;--gold:#D3B067;--green:#7CC39F;color-scheme:dark}}
:root[data-theme="dark"]{--ground:#11162C;--leaf:#181E38;--ink:#EAE3D3;--ink2:#ABA290;--ink3:#7E7767;--rule:#2B3254;--lapis:#8EA6EA;--verm:#E26C5F;--gold:#D3B067;--green:#7CC39F;color-scheme:dark}
*{box-sizing:border-box}[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ground);color:var(--ink);font:16px/1.65 var(--sans);word-break:keep-all;overflow-wrap:break-word}
a{color:inherit}button{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--verm);outline-offset:2px;border-radius:6px}
.wrap{max-width:820px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header{padding-top:calc(env(safe-area-inset-top,0px) + 18px);padding-bottom:6px}
.back{font:500 14px var(--sans);color:var(--ink2);text-decoration:none}
h1{font:700 clamp(26px,7vw,34px)/1.25 var(--serif);margin:10px 0 4px}
.lead{margin:0 0 4px;color:var(--ink2)}
.meta{margin:0;font-size:13px;color:var(--ink3)}
.bar{position:sticky;top:0;z-index:5;background:var(--ground);padding-top:calc(env(safe-area-inset-top,0px) + 8px);padding-bottom:8px;border-bottom:1px solid var(--rule)}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chips button{border:1px solid var(--rule);background:var(--leaf);border-radius:999px;padding:5px 12px;font-size:14px;cursor:pointer}
.chips button[aria-pressed="true"]{background:var(--ink);color:var(--ground);border-color:var(--ink)}
.tools{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:8px;font-size:14px;color:var(--ink2)}
.tools button{border:0;background:var(--lapis);color:var(--ground);border-radius:999px;padding:6px 14px;font-weight:600;cursor:pointer}
.tools button:disabled{opacity:.45;cursor:default}
.chap h2{font:700 21px/1.35 var(--serif);margin:26px 0 4px}.chap h2 span{font:500 13px var(--sans);color:var(--ink3);margin-left:4px}
.bt{font:600 14px/1.4 var(--sans);color:var(--ink2);margin:16px 0 6px}
.cards{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.row{background:var(--leaf);border:1px solid var(--rule);border-radius:12px;padding:8px;display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:6px 8px}
.go{display:grid;grid-template-columns:56px minmax(0,1fr) auto;align-items:center;gap:10px;text-decoration:none;min-width:0}
.go img{width:56px;height:70px;object-fit:cover;border-radius:6px;background:var(--rule)}
.tx{min-width:0}.tx b{display:block;font:700 16px/1.4 var(--serif)}.sub{display:block;font-size:13px;color:var(--ink3)}
.chip{font-size:12px;font-weight:600;border-radius:999px;padding:3px 9px;white-space:nowrap;border:1px solid currentColor}
.c-검토전{color:var(--verm)}.c-만드는중{color:var(--ink3)}.c-검수끝{color:var(--green)}.c-다듬기끝{color:var(--ink)}.c-기준카드{color:var(--gold)}
.memo-b{border:1px solid var(--rule);background:transparent;border-radius:8px;padding:6px 10px;font-size:13px;cursor:pointer;white-space:nowrap}
.row.has .memo-b{border-color:var(--gold);color:var(--gold);font-weight:600}
.memo{grid-column:1/-1}.memo textarea{width:100%;border:1px solid var(--rule);border-radius:8px;background:var(--ground);color:var(--ink);padding:8px 10px;font:15px/1.6 var(--serif);resize:vertical}
.empty{color:var(--ink3);text-align:center;padding:30px 0}
.copybox{margin-top:10px}.copybox textarea{width:100%;min-height:160px;border:1px solid var(--rule);border-radius:8px;background:var(--leaf);color:var(--ink);padding:8px;font:13px/1.6 var(--sans)}
footer{color:var(--ink3);font-size:13px;padding:30px 0 calc(env(safe-area-inset-bottom,0px) + 30px)}
@media (max-width:420px){.row{grid-template-columns:minmax(0,1fr)}.memo-b{justify-self:end}}
</style></head><body>
<header class="wrap"><a class="back" href="../">← 카드 책으로</a>
<h1>깊은 카드 모아 보기</h1>
<p class="lead">지금까지 만든 깊은 카드 {{TOTAL}}장이에요. 눌러서 열고, 보면서 느낀 점을 적어 두었다가 한꺼번에 복사해 본부에 보내 주세요.</p>
<p class="meta">{{SUMMARY}} · 본부가 {{NOW}}에 맞춤</p></header>
<div class="bar"><div class="wrap">
<div class="chips" role="group" aria-label="상태로 걸러 보기"><button type="button" data-f="" aria-pressed="true">전체</button><button type="button" data-f="검토 전" aria-pressed="false">검토 전</button><button type="button" data-f="만드는 중" aria-pressed="false">만드는 중</button><button type="button" data-f="검수 끝" aria-pressed="false">검수 끝</button><button type="button" data-f="다듬기 끝" aria-pressed="false">다듬기 끝</button><button type="button" data-f="memo" aria-pressed="false">느낀 점 적은 카드</button></div>
<div class="tools"><span id="mc">적은 느낀 점 0개</span><button type="button" id="copyAll" disabled>느낀 점 모두 복사</button></div>
<div class="copybox" id="copyBox" hidden><p class="meta">복사가 안 되면 아래 글을 길게 눌러 모두 선택해 복사해 주세요.</p><textarea id="copyText" readonly></textarea></div>
</div></div>
<main class="wrap" id="list">
{{GROUPS}}
<p class="empty" id="none" hidden>이 조건에 맞는 카드가 없어요.</p>
</main>
<footer class="wrap">느낀 점은 이 기기의 브라우저에만 남아요. 다른 기기에서 적은 것은 그 기기에서 복사해 주세요.</footer>
<script>
(function(){
  var K = 'deep-memo-', rows = [].slice.call(document.querySelectorAll('.row'));
  function get(id){ try { return localStorage.getItem(K + id) || ''; } catch (e) { return ''; } }
  function put(id, v){ try { if (v.trim()) localStorage.setItem(K + id, v); else localStorage.removeItem(K + id); } catch (e) {} }
  function count(){ var n = rows.filter(function(r){ return r.classList.contains('has'); }).length;
    document.getElementById('mc').textContent = '적은 느낀 점 ' + n + '개'; document.getElementById('copyAll').disabled = !n; }
  rows.forEach(function(r){
    var id = r.dataset.id, ta = r.querySelector('textarea'), b = r.querySelector('.memo-b'), box = r.querySelector('.memo');
    ta.value = get(id); r.classList.toggle('has', !!ta.value.trim());
    b.onclick = function(){ var open = box.hidden; box.hidden = !open; b.setAttribute('aria-expanded', String(open)); if (open) ta.focus(); };
    ta.oninput = function(){ put(id, ta.value); r.classList.toggle('has', !!ta.value.trim()); count(); };
  });
  count();
  var chips = [].slice.call(document.querySelectorAll('.chips button'));
  chips.forEach(function(c){ c.onclick = function(){
    chips.forEach(function(x){ x.setAttribute('aria-pressed', String(x === c)); });
    var f = c.dataset.f, shown = 0;
    rows.forEach(function(r){ var ok = !f || (f === 'memo' ? r.classList.contains('has') : r.dataset.st === f); r.hidden = !ok; if (ok) shown++; });
    [].slice.call(document.querySelectorAll('.cards')).forEach(function(u){ var v = [].slice.call(u.children).some(function(li){ return !li.hidden; }); u.hidden = !v; u.previousElementSibling.hidden = !v; });
    [].slice.call(document.querySelectorAll('.chap')).forEach(function(s){ s.hidden = ![].slice.call(s.querySelectorAll('.row')).some(function(li){ return !li.hidden; }); });
    document.getElementById('none').hidden = !!shown;
  }; });
  document.getElementById('copyAll').onclick = function(){
    var lines = ['[깊은 카드 느낀 점]'];
    rows.forEach(function(r){ var v = get(r.dataset.id).trim(); if (v) lines.push('· ' + r.querySelector('b').textContent + ' (' + r.dataset.id + '): ' + v.replace(/\\n+/g, ' / ')); });
    var text = lines.join('\\n'), box = document.getElementById('copyBox'), ta = document.getElementById('copyText');
    function fallback(){ box.hidden = false; ta.value = text; ta.focus(); ta.select(); }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(function(){ document.getElementById('mc').textContent = '복사했어요. 본부 창에 붙여 넣어 주세요.'; }, fallback); else fallback();
  };
})();
</script>
</body></html>
'''

if __name__ == '__main__':
    main()
