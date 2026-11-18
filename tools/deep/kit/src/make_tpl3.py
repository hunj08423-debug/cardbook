# -*- coding: utf-8 -*-
"""[본부 전용] deep2_tpl.html(시나이 시안 2) → ../deep3_tpl.html(모든 깊은 카드가 같이 쓰는 틀).
제작 창은 이 파일을 고치지 않아요. 틀을 바꿀 일이 있으면 status 파일에 적어 본부에 요청해요.
카드마다 다른 부분은 {{...}} 자리와 DATA로 빼고, 손으로 하는 방식 세 가지(화환·소리·놓아 보기)를 더한다."""
import re, sys
import os
W = os.path.dirname(os.path.abspath(__file__))   # 틀 원본(src) 폴더
src = open(f'{W}/deep2_tpl.html', encoding='utf-8').read()   # 시나이 시안 2(바탕)
out = src
def rep(a, b, n=1):
    global out
    c = out.count(a)
    assert c == n, (c, a[:80])
    out = out.replace(a, b)

rep('<title>사본이 완성되는 카드</title>', '<title>{{PAGETITLE}}</title>')
rep('/* 시안 2: 양피지 위에 먹, 붉은 머리글자, 금박, 채색이 차례로 올라가는 카드. 발견의 순간에는 불이 꺼지고 촛불만 남는다. */',
    '/* 깊은 카드 공통 틀(deep3): 양피지 → 먹 글씨 → 붉은 머리글자 → 금박 → 채색. 카드마다 색과 손으로 하는 방식만 다르다. */')
rep('/* 발견의 순간: 불을 끈다 */\nbody.dim{', '/*__THEME__*/\n/* 밤 장면: 불을 끈다 */\nbody.dim{')
rep('<span class="brand"><span class="long"><b>처음 만나는 기독교 문화</b> · </span>카드 뒷면 시안 2</span>',
    '<span class="brand"><span class="long"><b>처음 만나는 기독교 문화</b> · </span>{{BRANDSUB}}</span>')
rep('font-family="Gowun Batang, serif">시</text>', 'font-family="Gowun Batang, serif">{{SEAL}}</text>')
rep('<div class="bk-h">사본이 완성되는 다섯 단계</div>', '<div class="bk-h">카드가 완성되는 다섯 단계</div>')
# 첫머리
i0 = out.index('<div class="where"><b>1892년 2월</b>')
i1 = out.index('<div class="go">', i0)
out = out[:i0] + '''<div class="where">{{WHERE}}</div>
      <h1>{{TITLE}}</h1>
      <p class="lead a">{{LEAD}}</p>
      <p class="lead k">{{LEADKID}}</p>
      ''' + out[i1:]
rep('<p class="meta">영화처럼 약 3분 · 천천히 읽으면 5분 · 더 깊이 읽으면 10분 더</p>', '<p class="meta">{{META}}</p>')
i0 = out.index('<p class="draft">'); i1 = out.index('</p>', i0) + 4
out = out[:i0] + '<p class="draft">{{DRAFT}}</p>' + out[i1:]
# 4·5단계 상자 → 카드마다 다른 목표
i0 = out.index('<div class="steps">'); i1 = out.index('</section>', i0)
out = out[:i0] + '<div class="steps">{{GOALS}}</div>\n  ' + out[i1:]
rep('<p class="foot">‘처음 만나는 기독교 문화’ 안내서의 카드 한 장으로 만든 뒷면 시안 2예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.</p>',
    '<p class="foot">{{FOOT}}</p>')
rep('<p class="f-k">영화처럼 보기 · 약 3분</p>', '<p class="f-k">{{FILMLEN}}</p>')
rep('<p class="f-note" id="fNote" hidden>성가는 정교회 전통 성가 녹음이에요. 시나이에서 녹음한 소리는 아니에요.</p>', '<p class="f-note" id="fNote" hidden>{{SNDNOTE}}</p>')

# ---------- 스크립트 ----------
rep("const KEY = 'deep2-' + DATA.id;", "const KEY = 'deep3-' + DATA.id;")
rep("let P = {ach:{}, seen:{}, visits:[], line:'', pick:'', deepOpened:false, kidShow:false, met:''};",
    "let P = {ach:{}, seen:{}, visits:[], line:'', deepOpened:false, kidShow:false, ev:{}, m:{}};")
rep("const BADGE = ['아직 펼치지 않은 카드', '양피지', '먹 글씨', '붉은 머리글자', '금박', '채색 · 완성된 사본'];",
    "const BADGE = ['아직 펼치지 않은 카드', '양피지', '먹 글씨', '붉은 머리글자', '금박', '채색 · 완성된 카드'];")
rep("const UPT = ['', '양피지 카드를 받았어요', '먹 글씨가 입혀졌어요', '붉은 머리글자가 그려졌어요', '금박이 입혀졌어요', '채색까지, 사본이 완성됐어요'];",
    "const UPT = ['', '양피지 카드를 받았어요', '먹 글씨가 입혀졌어요', '붉은 머리글자가 그려졌어요', '금박이 입혀졌어요', '채색까지, 카드가 완성됐어요'];")
rep("'<b>완성된 사본이에요.</b><br>계절이 바뀌면 다시 찾아와 보세요.'", "'<b>완성된 카드예요.</b><br>' + esc(DATA.doneNote || '마음이 갈 때 다시 찾아와 보세요.')")
# check(): 4·5단계는 카드마다
i0 = out.index('function check(){'); i1 = out.index('\n}\n', i0) + 3
out = out[:i0] + '''function goalDone(g){ return !!(DATA.goals[g] && DATA.goals[g].ways.some(w => w.id === 'kid' ? P.kidShow : P.ev[w.id])); }
function mark(id, val){ if (!id) return; if (!P.ev[id] || (val && P.ev[id] !== val)) { P.ev[id] = val || today(); save(); } check(); }
function check(){
  const seenAll = DATA.scenes.every(id => P.seen[id]) && P.seen.imagine;
  if (seenAll) achieve(2);
  if (P.line) achieve(3);
  if (goalDone('s4')) achieve(4);
  if (goalDone('s5')) achieve(5);
  ['s4', 's5'].forEach(g => (DATA.goals[g] ? DATA.goals[g].ways : []).forEach(w => {
    const el = document.getElementById('w-' + w.id); if (!el) return;
    const ok = w.id === 'kid' ? P.kidShow : !!P.ev[w.id];
    el.classList.toggle('ok', ok);
    const em = el.querySelector('em'); if (!em) return;
    const st = MODS_STATUS[w.id] ? MODS_STATUS[w.id]() : '';
    em.textContent = st || (ok ? (w.okt || '했어요') : (w.hint || ''));
  }));
}
const MODS_STATUS = {};
''' + out[i1:]
# 예전 4·5단계 버튼 연결 지우기
rep("$$('.pick').forEach(b => b.onclick = () => { P.pick = b.dataset.p; save(); check(); });\n", '')
rep("/* 채색(5단계) */\n$('#metBtn').onclick = () => { P.met = $('#metNote').value.trim() || '직접 보거나 가 봤어요'; save(); check(); };\n", '')
# 밤 장면: 어느 카드든 .sc.night
rep("const night = $('#sc-closet');\nif (night) new IntersectionObserver(es => es.forEach(en => document.body.classList.toggle('dim', en.isIntersecting && en.intersectionRatio > 0.3)), {threshold: [0, 0.3, 0.6]}).observe(night);",
    "$$('.sc.night').forEach(night => new IntersectionObserver(es => es.forEach(en => document.body.classList.toggle('dim', en.isIntersecting && en.intersectionRatio > 0.3 && !document.body.classList.contains('daylight'))), {threshold: [0, 0.3, 0.6]}).observe(night));")
# 영화: 장 수, 자동 넘김 기억, 모듈 장면, 아이와 함께 끝까지
rep("let fi = 0, li = -1, fT = null, fAuto = true,", "let fi = 0, li = -1, fT = null, fAuto = (() => { try { const v = localStorage.getItem('deep-fauto'); return v === null ? true : v === '1'; } catch (e) { return true; } })(),")
rep("$('#fProg').innerHTML = Array.from({length: 5}, (_, i) =>", "$('#fProg').innerHTML = Array.from({length: DATA.nch}, (_, i) =>")
rep("(s.ch >= 6 ? '마무리' : '여는 장면')", "(s.ch > DATA.nch ? '마무리' : '여는 장면')")
rep('<span class="n">${s.no} / 5</span>', '<span class="n">${s.no} / ${DATA.nch}</span>')
rep("  else if (s.type === 'candle') { renderCandle(s); return; }",
    "  else if (s.type === 'candle') { renderCandle(s); return; }\n  else if (s.type === 'mod') { const el = swap('<div class=\"f-mod\"></div>'); const m = MODS[s.mod]; if (m && m.film) m.film(el.querySelector('.f-mod'), s); if (s.sync) { syncLines(s); return; } }")
rep("function clearT(){ clearTimeout(fT); fTimers.forEach(clearTimeout); fTimers = []; }",
    "function clearT(){ clearTimeout(fT); fTimers.forEach(clearTimeout); fTimers = []; Object.values(MODS).forEach(m => m.filmStop && m.filmStop()); }")
rep("function nextLine(){",
    '''function syncLines(s){
  // 소리에 맞춘 장면: 자막을 정해진 때에 띄우고, 끝나면 다음 장면으로
  const ls = L(s);
  ls.forEach((ln, k) => later(() => { li = k; sub(`<span class="ln${ln.q ? ' q' : ''}">${ln.q ? '“' : ''}${esc(ln.t)}${ln.q ? '”' : ''}${ln.from ? `<span class="from">${esc(ln.from)}</span>` : ''}</span>`); }, (ln.at || 0) * 1000));
  fWait = 'sync';
  fT = later(() => { fWait = null; showShot(fi + 1); }, (s.end || 30) * 1000);
}
function nextLine(){''')
rep("  if (fWait === 'candle' || fWait === 'reward') return;", "  if (fWait === 'candle' || fWait === 'reward') return;\n  if (fWait === 'sync') { fWait = null; showShot(fi + 1); return; }")
rep("  if (li > 0 && s.type !== 'chapter' && fWait !== 'reward') { li -= 2; fWait = null; nextLine(); return; }",
    "  if (li > 0 && s.type !== 'chapter' && fWait !== 'reward' && fWait !== 'sync') { li -= 2; fWait = null; nextLine(); return; }")
rep("$('#fAuto').onclick = ev => { ev.stopPropagation(); fAuto = !fAuto; $('#fAuto').setAttribute('aria-pressed', String(fAuto));",
    "$('#fAuto').onclick = ev => { ev.stopPropagation(); fAuto = !fAuto; try { localStorage.setItem('deep-fauto', fAuto ? '1' : '0'); } catch (e) {} $('#fAuto').setAttribute('aria-pressed', String(fAuto));")
rep("  $('#fStart').hidden = false; $('#fGoSnd').hidden = !snd;",
    "  $('#fAuto').setAttribute('aria-pressed', String(fAuto));\n  $('#fStart').hidden = false; $('#fGoSnd').hidden = !snd;")
rep("film.addEventListener('click', ev => { if (ev.target.closest('.f-ctrl,.f-top,.f-start,.f-reward,.ask,.f-prompt,.f-cbox')) return; fNextTap(); });",
    "film.addEventListener('click', ev => { if (ev.target.closest('.f-ctrl,.f-top,.f-start,.f-reward,.ask,.f-prompt,.f-cbox,.f-live')) return; fNextTap(); });")
rep("  if (fAuto) fT = later(nextLine, dur(ln));\n}", "  if (s.type === 'mod' && ln.act) { const m = MODS[s.mod]; if (m && m.act) m.act(ln.act); }\n  if (fAuto) fT = later(nextLine, dur(ln) + (ln.wait || 0));\n}")
# 소리가 있는 카드: 영화 시작 화면의 '소리 켜고 보기'
rep("$('#fGoSnd').hidden = !snd; $('#fNote').hidden = !snd; $('#fGo').textContent = snd ? '소리 없이 보기' : '시작하기';\n  (snd ? $('#fGoSnd') : $('#fGo')).focus();",
    "const hasSnd = !!(snd || DATA.filmSound); $('#fGoSnd').hidden = !hasSnd; $('#fNote').hidden = !hasSnd; $('#fGo').textContent = hasSnd ? '소리 없이 보기' : '시작하기';\n  (hasSnd ? $('#fGoSnd') : $('#fGo')).focus();")
rep("  $('#fStart').hidden = true; fSoundOn = !!(withSound && snd);\n  $('#fSnd').hidden = !snd;",
    "  $('#fStart').hidden = true; fSoundOn = !!(withSound && (snd || DATA.filmSound));\n  $('#fSnd').hidden = !(snd || DATA.filmSound);")
rep("$('#fSnd').onclick = ev => { ev.stopPropagation(); if (!snd) return; fSoundOn = !fSoundOn;",
    "$('#fSnd').onclick = ev => { ev.stopPropagation(); if (!snd && !DATA.filmSound) return; fSoundOn = !fSoundOn; Object.values(MODS).forEach(m => m.filmSound && m.filmSound(fSoundOn)); if (!snd) { $('#fSnd').setAttribute('aria-pressed', String(fSoundOn)); return; }")

# 모듈 자리
css = open(f'{W}/tpl3_mod.css', encoding='utf-8').read()
js = open(f'{W}/tpl3_mod.js', encoding='utf-8').read()
rep('@media (min-width:860px){\n  .hero{', css + '\n@media (min-width:860px){\n  .hero{')
rep("drawStage(false); drawStamp(false); check(); hold($('#lcHold'));",
    js + "\ninitMods();\ndrawStage(false); drawStamp(false); check(); hold($('#lcHold'));")
# 도장 글자 크기: 글자가 길면 작게
rep('<text x="100" y="104" text-anchor="middle" font-size="36" font-weight="700" font-family="Gowun Batang, serif">${s.t}</text>',
    '<text x="100" y="104" text-anchor="middle" font-size="${s.t.length > 3 ? 27 : 36}" font-weight="700" font-family="Gowun Batang, serif">${s.t}</text>')
assert '사본' not in out.replace('사본이', ''), [m.start() for m in re.finditer('사본', out)]
open(os.path.join(os.path.dirname(W), 'deep3_tpl.html'), 'w', encoding='utf-8').write(out)
print('ok', len(out))
