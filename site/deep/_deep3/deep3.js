const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const esc = t => String(t).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const KEY = 'deep3-' + DATA.id;
const today = () => { const d = new Date(); return `${d.getFullYear()}.${String(d.getMonth()+1).padStart(2,'0')}.${String(d.getDate()).padStart(2,'0')}`; };
let P = {ach:{}, seen:{}, visits:[], line:'', deepOpened:false, kidShow:false, ev:{}, m:{}};
try { const v = JSON.parse(localStorage.getItem(KEY) || 'null'); if (v) P = Object.assign(P, v); } catch (e) {}
function save(){ try { localStorage.setItem(KEY, JSON.stringify(P)); } catch (e) {} }
if (!P.visits.includes(today())) { P.visits.push(today()); save(); }

/* 단계 */
const NAMES = ['아직', '양피지', '먹 글씨', '붉은 머리글자', '금박', '채색'];
const BADGE = ['아직 펼치지 않은 카드', '양피지', '먹 글씨', '붉은 머리글자', '금박', '채색 · 완성된 카드'];
const UPT = ['', '양피지 카드를 받았어요', '먹 글씨가 입혀졌어요', '붉은 머리글자가 그려졌어요', '금박이 입혀졌어요', '채색까지, 카드가 완성됐어요'];
let preview = null;
function stageOf(){ let s = 0; for (let n = 1; n <= 5; n++) { if (P.ach['s' + n]) s = n; else break; } return s; }
function shownStage(){ return preview === null ? stageOf() : preview; }
function paintCard(el, lv){ el.className = 'lcard lv' + lv; }
function drawStage(bump){
  const lv = shownStage(), card = $('#lcard');
  paintCard(card, lv);
  if (bump) { card.classList.remove('up'); void card.offsetWidth; card.classList.add('up'); }
  $('#lcBadge').textContent = BADGE[lv];
  $$('#prog i').forEach((d, i) => d.classList.toggle('on', i < lv));
  $('#progName').textContent = NAMES[lv];
  $('#ladder').innerHTML = DATA.stages.map(s => `<li class="${s.n <= lv ? 'done' : ''}"><span class="n">${s.n}</span><span>${esc(s.t)}</span><span class="d">${s.n <= lv && preview === null && P.ach['s' + s.n] ? esc(P.ach['s' + s.n].slice(5)) : ''}</span></li>`).join('');
  const nx = DATA.stages[lv];
  $('#bkNext').innerHTML = nx ? `<b>다음 · ${esc(nx.t)}</b><br>${esc(nx.how)}` : '<b>완성된 카드예요.</b><br>' + esc(DATA.doneNote || '마음이 갈 때 다시 찾아와 보세요.');
  $$('#preview button[data-lv]').forEach(b => b.classList.toggle('on', b.dataset.lv === (preview === null ? 'me' : String(preview))));
  $('#openStory').textContent = '이야기 펼치기';
}
let toastQ = [], toasting = false;
function toast(n){
  toastQ.push(n); if (toasting) return;
  const next = () => {
    const k = toastQ.shift(); if (k === undefined) { toasting = false; return; }
    toasting = true;
    const s = DATA.stages[k - 1];
    $('#toastCard').innerHTML = `<div class="lcard lv${k}"><div class="lc-in"><img src="${DATA.card}" alt=""></div></div>`;
    $('#toastT').textContent = UPT[k];
    $('#toastP').textContent = s.done;
    $('#toast').classList.add('on');
    setTimeout(() => { $('#toast').classList.remove('on'); setTimeout(next, 600); }, 3200);
  };
  next();
}
function achieve(n){
  if (P.ach['s' + n]) return;
  const before = stageOf();
  P.ach['s' + n] = today(); save();
  const after = stageOf();
  // 영화처럼 보기 안에서는 마지막 화면이 카드 강화를 직접 보여 주므로 알림을 띄우지 않아요
  const inFilm = !document.getElementById('film').hidden;
  if (after > before && preview === null) { drawStage(true); if (!inFilm) for (let k = before + 1; k <= after; k++) toast(k); }
  else drawStage(false);
}
function goalDone(g){ return !!(DATA.goals[g] && DATA.goals[g].ways.some(w => w.id === 'kid' ? P.kidShow : P.ev[w.id])); }
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

/* 미리 보기(시안 확인용) */
$$('#preview button[data-lv]').forEach(b => b.onclick = () => { preview = b.dataset.lv === 'me' ? null : +b.dataset.lv; drawStage(true); });
let resetArm = false;
$('#resetBtn').onclick = () => {
  if (!resetArm) { resetArm = true; $('#resetBtn').textContent = '한 번 더 누르면 지워요'; setTimeout(() => { resetArm = false; $('#resetBtn').textContent = '기록 지우기'; }, 3000); return; }
  try { localStorage.removeItem(KEY); } catch (e) {}
  location.hash = ''; location.reload();
};

/* 아이와 함께 */
const kidBtn = $('#kid');
function setKid(v){ document.body.classList.toggle('kid', v); kidBtn.setAttribute('aria-pressed', String(v)); try { localStorage.setItem('deep-kid', JSON.stringify(v)); } catch (e) {} }
kidBtn.onclick = () => setKid(!document.body.classList.contains('kid'));
try { setKid(!!JSON.parse(localStorage.getItem('deep-kid') || 'false')); } catch (e) { setKid(false); }

/* 카드 뒤집기 */
$('#flipBtn').onclick = () => {
  const on = $('#flip').classList.toggle('on');
  $('#flip .front').setAttribute('aria-hidden', String(on)); $('#flip .back').setAttribute('aria-hidden', String(!on));
};
$('#prog').onclick = () => $('#cardcol').scrollIntoView({behavior: 'smooth', block: 'center'});

/* 앞면 이야기(1단계) */
let sti = 0;
const story = $('#story');
function drawStory(){
  const s = DATA.front[sti], kid = document.body.classList.contains('kid'), img = $('#stImg');
  const f = s.f || [55, 35, 1];
  img.style.transformOrigin = `${f[0]}% ${f[1]}%`; img.style.transform = `scale(${f[2] || 1})`;
  $('#stNo').textContent = `${sti + 1} / ${DATA.front.length}`;
  $('#stSay').textContent = kid ? s.kid : s.t;
  $('#stDots').innerHTML = DATA.front.map((x, i) => `<i class="${i <= sti ? 'on' : ''}"></i>`).join('');
  $('#stPrev').disabled = sti === 0;
  $('#stNext').textContent = sti < DATA.front.length - 1 ? '다음' : '카드 받기';
}
function openStory(){ sti = 0; story.hidden = false; document.body.style.overflow = 'hidden'; drawStory(); $('#stNext').focus(); }
function closeStory(){ story.hidden = true; document.body.style.overflow = ''; }
$('#openStory').onclick = openStory; $('#openStory2').onclick = openStory; $('#stX').onclick = closeStory;
$('#stPrev').onclick = () => { if (sti > 0) { sti--; drawStory(); } };
$('#stNext').onclick = () => { if (sti < DATA.front.length - 1) { sti++; drawStory(); } else { closeStory(); achieve(1); check(); } };

/* 장면을 지나며 */
const obs = new IntersectionObserver(es => es.forEach(en => {
  if (!en.isIntersecting) return;
  en.target.classList.add('in');
  const id = en.target.dataset.sc || (en.target.id === 'imagine' ? 'imagine' : null);
  if (id && !P.seen[id]) { P.seen[id] = true; save(); check(); }
}), {threshold: 0.35});
$$('.sc').forEach(s => obs.observe(s)); obs.observe($('#imagine'));
/* 발견의 순간: 불을 끈다 */
$$('.sc.night').forEach(night => new IntersectionObserver(es => es.forEach(en => document.body.classList.toggle('dim', en.isIntersecting && en.intersectionRatio > 0.3 && !document.body.classList.contains('daylight'))), {threshold: [0, 0.3, 0.6]}).observe(night));

/* 그때와 지금, 둘러보기 */
const tn = $('#tn');
if (tn) tn.querySelectorAll('.tn-tabs button').forEach(b => b.onclick = () => {
  tn.dataset.state = b.dataset.v;
  tn.querySelectorAll('.tn-tabs button').forEach(x => x.setAttribute('aria-selected', String(x === b)));
});
function pickSpot(i){
  $$('.spot,.spotname').forEach(b => b.classList.toggle('on', b.dataset.i === String(i)));
  $$('.spotinfo').forEach(d => d.hidden = d.dataset.i !== String(i));
  const h = document.querySelector('.spotbox .hint'); if (h) h.hidden = true;
}
$$('.spot,.spotname').forEach(b => b.onclick = () => pickSpot(b.dataset.i));

/* 촛불 */
const cd = $('#candle');
if (cd) {
  const cells = new Set(); let revealed = false;
  const reveal = () => { if (revealed) return; revealed = true; $('#reveal').classList.add('on'); };
  const move = ev => {
    const r = cd.getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top;
    cd.style.setProperty('--x', x + 'px'); cd.style.setProperty('--y', y + 'px'); cd.classList.add('used');
    cells.add(Math.floor(x / r.width * 5) + ',' + Math.floor(y / r.height * 6));
    if (cells.size >= 9) reveal();
  };
  cd.addEventListener('pointermove', move);
  cd.addEventListener('pointerdown', ev => { move(ev); try { cd.setPointerCapture(ev.pointerId); } catch (e) {} });
  $('#litAll').onclick = () => { cd.style.setProperty('--x', '50%'); cd.style.setProperty('--y', '45%'); cd.style.setProperty('--r', '420px'); cd.style.animation = 'none'; cd.classList.add('used'); reveal(); };
}

/* 소리 */
const snd = $('#snd');
let fadeId = 0;
function fadeTo(v, ms){ if (!snd) return; const id = ++fadeId, a = snd.volume, t0 = performance.now(); const st = t => { if (id !== fadeId) return; const k = Math.min(1, (t - t0) / ms); snd.volume = Math.min(1, Math.max(0, a + (v - a) * k)); if (k < 1) requestAnimationFrame(st); else if (v === 0) snd.pause(); }; requestAnimationFrame(st); }
$$('.sndbtn').forEach(b => b.onclick = () => {
  if (!snd) return;
  const on = snd.paused;
  if (on) { snd.volume = 0; snd.play().then(() => fadeTo(0.8, 1500)).catch(() => {}); } else fadeTo(0, 900);
  $$('.sndbtn').forEach(x => x.setAttribute('aria-pressed', String(on)));
});

/* 나의 자리(3단계) */
$$('.line').forEach(b => b.onclick = () => { $$('.line').forEach(x => x.classList.toggle('on', x === b)); $('#note').value = b.dataset.l; });
function stampSVG(date){
  const s = DATA.stamp;
  return `<svg viewBox="0 0 200 200" aria-hidden="true"><defs><filter id="ink" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2.4"/></filter>
  <path id="arcT" d="M 38 100 A 62 62 0 0 1 162 100"/><path id="arcB" d="M 30 100 A 70 70 0 0 0 170 100"/></defs>
  <g filter="url(#ink)"><circle cx="100" cy="100" r="88" fill="none" stroke="currentColor" stroke-width="5"/><circle cx="100" cy="100" r="77" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <g fill="currentColor" font-family="IBM Plex Sans KR, sans-serif"><text font-size="14" letter-spacing="1"><textPath href="#arcT" startOffset="50%" text-anchor="middle">${s.sub}</textPath></text>
  <text x="100" y="104" text-anchor="middle" font-size="${s.t.length > 3 ? 27 : 36}" font-weight="700" font-family="Gowun Batang, serif">${s.t}</text>
  <text x="100" y="134" text-anchor="middle" font-size="21" letter-spacing="2">${s.y}</text>
  <text font-size="12.5"><textPath href="#arcB" startOffset="50%" text-anchor="middle">다녀온 날 ${date}</textPath></text></g></g></svg>`;
}
function drawStamp(hit){
  const out = $('#stampOut');
  if (!P.line) { out.hidden = true; return; }
  const date = P.ach.s3 || today();
  out.hidden = false; out.classList.toggle('hit', !!hit);
  out.innerHTML = stampSVG(date) + `<p class="my">“${esc(P.line)}”</p><p class="when">카드 뒷면에도 찍혔어요 · 이 기기에만 저장</p>`;
  $('#bkStamp').innerHTML = stampSVG(date);
  $('#note').value = P.line; $('#stampBtn').textContent = '한 줄 고쳐 다시 찍기';
}
$('#stampBtn').onclick = () => {
  const line = $('#note').value.trim();
  if (!line) { $('#stampHint').textContent = '위에서 한 줄을 고르거나, 직접 적어 주세요.'; return; }
  P.line = line; save(); $('#stampHint').textContent = ''; drawStamp(true); check();
};

/* 더 깊이(4단계) */
$$('details.dp').forEach(d => d.addEventListener('toggle', () => { if (d.open && d.closest('#deep')) { P.deepOpened = true; save(); check(); } }));

/* 사진 크게 보기 */
const lb = $('#lb');
function closeOv(el){ el.hidden = true; document.body.style.overflow = ''; }
$$('a.zoom').forEach(a => a.onclick = ev => { ev.preventDefault(); $('#lbImg').src = a.getAttribute('href'); $('#lbImg').alt = a.querySelector('img').alt; $('#lbCap').textContent = a.dataset.cap || ''; lb.hidden = false; document.body.style.overflow = 'hidden'; $('#lbX').focus(); });
$('#lbX').onclick = () => closeOv(lb);

/* 영화처럼 보기 */
const film = $('#film'), F = DATA.film;
let fi = 0, li = -1, fT = null, fAuto = (() => { try { const v = localStorage.getItem('deep-fauto'); return v === null ? true : v === '1'; } catch (e) { return true; } })(), fSoundOn = false, fWait = null, fCur = 0, fKid = false, fTimers = [];
function clearT(){ clearTimeout(fT); fTimers.forEach(clearTimeout); fTimers = []; Object.values(MODS).forEach(m => m.filmStop && m.filmStop()); }
function later(fn, ms){ const t = setTimeout(fn, ms); fTimers.push(t); return t; }
function L(s){ return fKid ? (s.kid || []) : (s.lines || []); }
function dur(ln){ return 1700 + 78 * ln.t.length + (ln.q ? 1400 : 0); }
function shotDur(s){ return Math.max(6000, L(s).reduce((a, l) => a + (l.ask ? 4000 : dur(l)), 0) + 1500); }
function layer(){ return fCur === 0 ? $('#fA') : $('#fB'); }
function swap(html){
  const next = fCur === 0 ? $('#fB') : $('#fA'), prev = layer();
  next.innerHTML = html; void next.offsetWidth; next.classList.add('on'); prev.classList.remove('on');
  fCur = fCur === 0 ? 1 : 0;
  later(() => { if (!prev.classList.contains('on')) prev.innerHTML = ''; }, 1300);
  return next;
}
function sub(html, center){ const el = $('#fSub'); el.classList.toggle('center', !!center); el.innerHTML = html; }
function progress(s){
  $('#fProg').innerHTML = Array.from({length: DATA.nch}, (_, i) => `<i class="${i + 1 <= s.ch ? 'on' : ''}"></i>`).join('');
  const c = F.find(x => x.type === 'chapter' && x.ch === s.ch);
  $('#fCh').textContent = c ? `${c.no} · ${c.t}` : (s.ch > DATA.nch ? '마무리' : '여는 장면');
}
function imgHTML(m, sh, d, extra){ return `<img class="f-img${extra || ''}" src="${m.u}" alt="${esc(m.alt)}" style="--fit:${sh.fit || 'cover'};--p0:${sh.p0 || '50% 50%'};--p1:${sh.p1 || sh.p0 || '50% 50%'};--s0:${sh.s0 || 1};--s1:${sh.s1 || 1};--o:${sh.o || '50% 50%'};--dur:${d}ms">`; }
function soundCue(s){
  if (!snd || !fSoundOn) return;
  if (s.sound === 'off') fadeTo(0, 2600);
  else if (s.sound === 'on') { if (snd.paused) { snd.volume = 0; snd.play().catch(() => {}); } fadeTo(0.5, 2600); }
}
function showShot(i){
  clearT(); fWait = null; fi = i; li = -1;
  const s = F[i]; if (!s) return;
  progress(s); soundCue(s); sub(''); film.classList.toggle('at-reward', s.type === 'reward');
  const d = shotDur(s);
  if (s.type === 'open') {
    const el = swap(imgHTML(s.img, s, d) + `<div class="f-shade"></div><div class="f-title"><span class="kk">${esc(s.kicker)}</span><h2>${esc(s.title)}</h2></div>`);
    later(() => { const t = el.querySelector('.f-title'); if (t) t.classList.add('out'); }, 3600);
    fT = later(nextLine, 4600); return;
  }
  else if (s.type === 'chapter') { swap(`<div class="f-chap"><span class="n">${s.no} / ${DATA.nch}</span><h3>${esc(s.t)}</h3></div>`); fT = later(() => showShot(i + 1), 2600); return; }
  else if (s.type === 'map') {
    const el = swap(`<div class="f-map"></div><div class="f-day"><span class="fDayN">1</span>일째<small>낙타로 아흐레</small></div>`);
    const m = $('#mapsvg').cloneNode(true); m.removeAttribute('id');
    const ns = 'http://www.w3.org/2000/svg', pth = document.createElementNS(ns, 'path');
    pth.setAttribute('d', DATA.routeD); pth.setAttribute('pathLength', '100'); pth.setAttribute('class', 'f-route'); m.appendChild(pth);
    const c = document.createElementNS(ns, 'circle'); c.setAttribute('r', '7'); c.setAttribute('fill', '#ffd28a'); c.setAttribute('stroke', '#3a2208'); c.setAttribute('stroke-width', '2');
    const am = document.createElementNS(ns, 'animateMotion'); am.setAttribute('dur', '8s'); am.setAttribute('begin', 'indefinite'); am.setAttribute('fill', 'freeze'); am.setAttribute('path', DATA.routeD); c.appendChild(am); m.appendChild(c);
    el.querySelector('.f-map').appendChild(m);
    later(() => { try { am.beginElement(); } catch (e) {} }, 600);
    for (let k = 2; k <= 9; k++) later(() => { const n = el.querySelector('.fDayN'); if (n) n.textContent = k; }, 600 + (k - 1) * 8000 / 9);
  }
  else if (s.type === 'img') swap(imgHTML(s.img, s, d) + '<div class="f-shade"></div>' + (s.cap ? `<span class="f-cap">${esc(s.cap)}</span>` : ''));
  else if (s.type === 'thennow') swap(imgHTML(s.then, {fit: 'cover', s0: 1.06, s1: 1.0}, d) + `<img class="f-img f-now" src="${s.now.u}" alt="${esc(s.now.alt)}" style="--fit:cover;--s0:1.08;--s1:1.0;--dur:${d}ms;opacity:0;transition:opacity 2.6s ease">` + '<div class="f-shade"></div>' + (s.cap ? `<span class="f-cap">${esc(s.cap)}</span>` : ''));
  else if (s.type === 'black') swap('<div class="f-black"></div>');
  else if (s.type === 'quote') swap(`<div class="f-black"></div><div class="f-quote"><p>“${esc(s.big)}”</p></div>`);
  else if (s.type === 'imagine') swap('<div class="f-imagine"><div class="flame"></div></div>');
  else if (s.type === 'candle') { renderCandle(s); return; }
  else if (s.type === 'mod') { const el = swap('<div class="f-mod"></div>'); const m = MODS[s.mod]; if (m && m.film) m.film(el.querySelector('.f-mod'), s); if (s.sync) { syncLines(s); return; } }
  else if (s.type === 'reward') { renderReward(); return; }
  fT = later(nextLine, 900);
}
function syncLines(s){
  // 소리에 맞춘 장면: 자막을 정해진 때에 띄우고, 끝나면 다음 장면으로
  const ls = L(s);
  ls.forEach((ln, k) => later(() => { li = k; sub(`<span class="ln${ln.q ? ' q' : ''}">${ln.q ? '“' : ''}${esc(ln.t)}${ln.q ? '”' : ''}${ln.from ? `<span class="from">${esc(ln.from)}</span>` : ''}</span>`); }, (ln.at || 0) * 1000));
  fWait = 'sync';
  fT = later(() => { fWait = null; showShot(fi + 1); }, (s.end || 30) * 1000);
}
function nextLine(){
  clearTimeout(fT);
  const s = F[fi], lines = L(s); li++;
  if (li >= lines.length) {
    if (s.type === 'imagine' && li === lines.length) { sub(''); fT = later(() => showShot(fi + 1), 3500); return; }
    showShot(fi + 1); return;
  }
  const ln = lines[li], center = ['black', 'imagine'].includes(s.type);
  if (s.type === 'open') { const t = layer().querySelector('.f-title'); if (t) t.classList.add('out'); }
  if (s.type === 'thennow' && li === 0) { const nw = layer().querySelector('.f-now'); if (nw) nw.style.opacity = '1'; }
  if (!ln.t) { sub(''); if (fAuto) fT = later(nextLine, ln.wait || 3000); return; }
  if (ln.ask) {
    fWait = 'ask';
    sub(`<div class="ask"><b>${esc(typeof ln.ask === 'string' ? ln.ask : '물어보기')}</b><span>${esc(ln.t)}</span><button type="button" class="fGoOn">${esc(ln.go || '이야기 나눈 뒤 이어 보기')}</button></div>`, center);
    $('#fSub .fGoOn').onclick = ev => { ev.stopPropagation(); fWait = null; nextLine(); };
    return;
  }
  sub(`<span class="ln${ln.q ? ' q' : ''}">${ln.q ? '“' : ''}${esc(ln.t)}${ln.q ? '”' : ''}${ln.from ? `<span class="from">${esc(ln.from)}</span>` : ''}</span>`, center);
  if (s.type === 'mod' && ln.act) { const m = MODS[s.mod]; if (m && m.act) m.act(ln.act); }
  if (fAuto) fT = later(nextLine, dur(ln) + (ln.wait || 0));
}
function fNextTap(){
  if (fWait === 'candle' || fWait === 'reward') return;
  if (fWait === 'sync') { fWait = null; showShot(fi + 1); return; }
  if (fWait === 'ask') { fWait = null; nextLine(); return; }
  if (F[fi].type === 'chapter') { showShot(fi + 1); return; }
  nextLine();
}
function fPrevTap(){
  const s = F[fi];
  if (li > 0 && s.type !== 'chapter' && fWait !== 'reward' && fWait !== 'sync') { li -= 2; fWait = null; nextLine(); return; }
  let j = fi - 1; while (j > 0 && F[j].type === 'chapter') j--;
  if (j >= 0) showShot(j);
}
function renderCandle(s){
  const ratio = s.img.w / s.img.h;
  const H = Math.max(160, Math.min(window.innerHeight - 230, (window.innerWidth - 24) / ratio)), Wd = H * ratio;
  const el = swap(`<div class="f-black"></div><div class="f-candle"><div class="f-cbox" style="width:${Wd}px;height:${H}px"><img class="c-base" src="${s.img.u}" alt="${esc(s.img.alt)}"><img class="c-lit" src="${s.img.u}" alt=""><div class="c-glow"></div></div></div>`);
  fWait = 'candle'; sub('');
  const pr = document.createElement('div'); pr.className = 'f-prompt';
  pr.innerHTML = `<p>${esc(s.prompt)}</p><button type="button">다 비춰 봤어요</button>`; el.appendChild(pr);
  const box = el.querySelector('.f-cbox'), cells = new Set();
  const done = () => { if (fWait !== 'candle') return; fWait = null; pr.remove(); box.style.animation = 'none'; box.style.transition = '--r 2.2s ease'; box.style.setProperty('--r', Math.max(Wd, H) * 1.2 + 'px'); fT = later(nextLine, 1400); };
  const mv = ev => { const r = box.getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top; box.style.setProperty('--x', x + 'px'); box.style.setProperty('--y', y + 'px'); cells.add(Math.floor(x / r.width * 5) + ',' + Math.floor(y / r.height * 6)); if (cells.size >= 9) done(); };
  box.addEventListener('pointermove', mv);
  box.addEventListener('pointerdown', ev => { ev.stopPropagation(); mv(ev); try { box.setPointerCapture(ev.pointerId); } catch (e) {} });
  pr.querySelector('button').onclick = ev => { ev.stopPropagation(); done(); };
}
/* 손에 든 카드: 손이 닿을 때만 살짝 기울고 빛이 따라와요. 움직임 줄이기를 켜면 빛을 고정해요. */
function hold(box){
  if (!box || box.dataset.held) return; box.dataset.held = '1';
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let raf = 0, pt = null;
  const paint = () => { raf = 0; if (!pt) return; const r = box.getBoundingClientRect(), x = Math.min(1, Math.max(0, (pt.x - r.left) / r.width)), y = Math.min(1, Math.max(0, (pt.y - r.top) / r.height));
    box.style.setProperty('--ry', ((x - .5) * 12).toFixed(2) + 'deg'); box.style.setProperty('--rx', ((.5 - y) * 10).toFixed(2) + 'deg');
    box.querySelectorAll('.lcard').forEach(k => { k.style.setProperty('--lx', (x * 100).toFixed(1) + '%'); k.style.setProperty('--ly', (y * 100).toFixed(1) + '%'); }); };
  const go = e => { pt = {x: e.clientX, y: e.clientY}; box.classList.add('on', 'live'); if (!raf) raf = requestAnimationFrame(paint); };
  const rest = () => { pt = null; box.classList.remove('on', 'live'); box.style.setProperty('--rx', '0deg'); box.style.setProperty('--ry', '0deg'); };
  box.addEventListener('pointermove', e => { if (e.pointerType === 'mouse' || e.buttons) go(e); });
  box.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') go(e); });
  box.addEventListener('pointerleave', rest); box.addEventListener('pointercancel', rest);
  box.addEventListener('pointerup', e => { if (e.pointerType !== 'mouse') setTimeout(rest, 250); });
}
function cardClone(){ const c = $('#lcard').cloneNode(true); c.removeAttribute('id'); c.querySelectorAll('[id]').forEach(x => x.removeAttribute('id')); return c; }
function renderReward(){
  fWait = 'reward'; sub('');
  if (fKid) { P.kidShow = true; save(); }
  const before = stageOf();
  achieve(1); achieve(2); check();
  const after = stageOf();
  const el = swap('<div class="f-reward"><div class="f-card"></div><span class="f-lvchip"></span><h3 class="fRT"></h3><p class="t fRP"></p><div class="fRBody"></div></div>');
  const rw = el.querySelector('.f-reward'), holder = el.querySelector('.f-card'), chip = el.querySelector('.f-lvchip'), body = el.querySelector('.fRBody'), rt = el.querySelector('.fRT'), rp = el.querySelector('.fRP');
  const card = cardClone(), hw = document.createElement('div'); hw.className = 'hold'; hw.appendChild(card); holder.appendChild(hw); hold(hw);
  // 카드 강화: 원래 단계에서 한 칸씩 올라가요
  const setLv = (k, fx) => {
    paintCard(card, k);
    const bd = card.querySelector('.lc-badge'); if (bd) bd.textContent = BADGE[k];
    chip.textContent = k ? `${k}단계 · ${NAMES[k]}` : '아직 펼치지 않은 카드'; chip.classList.toggle('new', !k);
    if (!fx) return;
    [card, holder, chip].forEach(x => x.classList.remove('up', 'flash', 'pop')); void card.offsetWidth;
    card.classList.add('up'); holder.classList.add('flash'); chip.classList.add('pop');
  };
  setLv(before, false);
  const steps = after - before, t0 = 700, gap = 1300;
  for (let k = before + 1; k <= after; k++) later(() => setLv(k, true), t0 + (k - before - 1) * gap);
  const dl = steps ? (t0 + (steps - 1) * gap + 500) / 1000 : 0;
  [rt, rp, body].forEach(x => { x.classList.add('later'); x.style.setProperty('--dl', dl + 's'); });
  rt.textContent = fKid ? '아이와 함께 끝까지 봤어요' : after >= 2 && before < 2 ? '다섯 장면을 끝까지 걸었어요' : '끝까지 함께 보셨어요';
  rp.textContent = (steps ? `카드가 ‘${NAMES[after]}’ 단계까지 올라왔어요.` : `카드는 지금 ‘${NAMES[after]}’ 단계예요.`) + (P.line ? '' : ' 마지막으로, 마음에 닿는 한 줄을 남겨 도장을 받아 보세요.');
  const ends = `<div class="f-btns"><button type="button" class="f-deep">더 깊이 읽기</button><button type="button" class="ghost f-again">처음부터 다시</button><button type="button" class="ghost f-close">닫기</button></div>`;
  if (P.line) { body.innerHTML = `<p class="t">남긴 한 줄 · “${esc(P.line)}”</p>` + ends; holder.insertAdjacentHTML('beforeend', `<div class="f-stampov">${stampSVG(P.ach.s3 || today())}</div>`); wireEnds(body); return; }
  // 한 줄을 고르는 동안에는 카드를 조금 작게 접어 둬요(도장을 받으면 다시 커져요)
  later(() => { holder.style.setProperty('--sh', card.offsetHeight + 'px'); rw.classList.add('choose'); }, dl * 1000 + 200);
  const ls = fKid ? DATA.linesKid : DATA.lines;
  body.innerHTML = `<div class="f-lines">${ls.map(l => `<button type="button" data-l="${esc(l)}">${esc(l)}</button>`).join('')}</div><textarea class="fLine" maxlength="300" placeholder="또는 직접 적어 보세요." aria-label="나의 한 줄"></textarea><div class="f-btns"><button type="button" class="fStampBtn">이 자리에 도장 받기</button></div>`;
  const ta = body.querySelector('.fLine');
  body.querySelectorAll('.f-lines button').forEach(b => b.onclick = ev => { ev.stopPropagation(); body.querySelectorAll('.f-lines button').forEach(x => x.classList.toggle('on', x === b)); ta.value = b.dataset.l; });
  body.querySelector('.fStampBtn').onclick = ev => {
    ev.stopPropagation(); const line = ta.value.trim();
    if (!line) { rp.textContent = '한 줄을 고르거나 직접 적어 주세요.'; return; }
    const b0 = stageOf();
    P.line = line; save(); drawStamp(false); check();
    const b1 = stageOf();
    rw.classList.remove('choose'); rw.scrollTo({top: 0, behavior: 'smooth'});
    if (b1 > b0) setLv(b1, true);
    holder.insertAdjacentHTML('beforeend', `<div class="f-stampov">${stampSVG(P.ach.s3 || today())}</div>`);
    rt.textContent = '이 자리에 도장이 찍혔어요';
    rp.textContent = b1 > b0 ? `${UPT[b1]}.` : `카드는 지금 ‘${NAMES[b1]}’ 단계예요.`;
    [rt, rp].forEach(x => x.style.setProperty('--dl', '0s'));
    body.innerHTML = `<p class="t">“${esc(line)}”</p>` + ends; wireEnds(body);
  };
}
function wireEnds(body){
  const q = s => body.querySelector(s);
  if (q('.f-deep')) q('.f-deep').onclick = ev => { ev.stopPropagation(); fClose(); setTimeout(() => $('#deep').scrollIntoView({behavior: 'smooth'}), 120); };
  if (q('.f-again')) q('.f-again').onclick = ev => { ev.stopPropagation(); showShot(0); };
  if (q('.f-close')) q('.f-close').onclick = ev => { ev.stopPropagation(); fClose(); };
}
function fOpen(ch){
  fKid = document.body.classList.contains('kid');
  fi = 0; if (ch) { const j = F.findIndex(s => s.type === 'chapter' && s.ch === ch); if (j >= 0) fi = j; }
  film.hidden = false; document.body.style.overflow = 'hidden';
  ['#fA', '#fB'].forEach(x => { $(x).innerHTML = ''; $(x).classList.remove('on'); }); sub('');
  $('#fAuto').setAttribute('aria-pressed', String(fAuto));
  $('#fStart').hidden = false; const hasSnd = !!(snd || DATA.filmSound); $('#fGoSnd').hidden = !hasSnd; $('#fNote').hidden = !hasSnd; $('#fGo').textContent = hasSnd ? '소리 없이 보기' : '시작하기';
  (hasSnd ? $('#fGoSnd') : $('#fGo')).focus();
}
function fBegin(withSound){
  $('#fStart').hidden = true; fSoundOn = !!(withSound && (snd || DATA.filmSound));
  $('#fSnd').hidden = !(snd || DATA.filmSound); $('#fSnd').setAttribute('aria-pressed', String(fSoundOn));
  if (fSoundOn) { snd.volume = 0; snd.play().then(() => fadeTo(0.5, 2500)).catch(() => {}); $$('.sndbtn').forEach(x => x.setAttribute('aria-pressed', 'true')); }
  showShot(fi);
}
function fClose(){
  clearT(); film.hidden = true; document.body.style.overflow = '';
  if (document.fullscreenElement) document.exitFullscreen().catch(() => {});
  if (snd && !snd.paused) { fadeTo(0, 900); $$('.sndbtn').forEach(x => x.setAttribute('aria-pressed', 'false')); }
}
$('#fGoSnd').onclick = ev => { ev.stopPropagation(); fBegin(true); };
$('#fGo').onclick = ev => { ev.stopPropagation(); fBegin(false); };
$('#fX').onclick = ev => { ev.stopPropagation(); fClose(); };
/* 전체 화면(지원하는 컴퓨터 브라우저에서만 보여요) */
const fFull = $('#fFull');
fFull.hidden = !(document.fullscreenEnabled && film.requestFullscreen);
fFull.onclick = ev => { ev.stopPropagation(); if (document.fullscreenElement) document.exitFullscreen().catch(() => {}); else film.requestFullscreen().catch(() => {}); };
document.addEventListener('fullscreenchange', () => fFull.setAttribute('aria-pressed', String(document.fullscreenElement === film)));
$('#fNext').onclick = ev => { ev.stopPropagation(); fNextTap(); };
$('#fPrev').onclick = ev => { ev.stopPropagation(); fPrevTap(); };
$('#fAuto').onclick = ev => { ev.stopPropagation(); fAuto = !fAuto; try { localStorage.setItem('deep-fauto', fAuto ? '1' : '0'); } catch (e) {} $('#fAuto').setAttribute('aria-pressed', String(fAuto)); if (fAuto && !fWait) { clearTimeout(fT); fT = later(nextLine, 1500); } };
$('#fSnd').onclick = ev => { ev.stopPropagation(); if (!snd && !DATA.filmSound) return; fSoundOn = !fSoundOn; Object.values(MODS).forEach(m => m.filmSound && m.filmSound(fSoundOn)); if (!snd) { $('#fSnd').setAttribute('aria-pressed', String(fSoundOn)); return; } $('#fSnd').setAttribute('aria-pressed', String(fSoundOn)); if (fSoundOn) { snd.volume = 0; snd.play().then(() => fadeTo(0.5, 1200)).catch(() => {}); } else fadeTo(0, 700); };
film.addEventListener('click', ev => { if (ev.target.closest('.f-ctrl,.f-top,.f-start,.f-reward,.ask,.f-prompt,.f-cbox,.f-live')) return; fNextTap(); });
$('#filmBtn').onclick = () => fOpen(0); $('#filmBtn2').onclick = () => fOpen(0);
$$('.fromhere').forEach(b => b.onclick = () => fOpen(+b.dataset.ch));

document.addEventListener('keydown', ev => {
  if (!film.hidden) {
    if (ev.key === 'Escape') { fClose(); return; }
    if (!$('#fStart').hidden) return;
    if (ev.key === 'ArrowRight' || (ev.key === ' ' && !/TEXTAREA|BUTTON/.test(document.activeElement.tagName))) { ev.preventDefault(); fNextTap(); }
    else if (ev.key === 'ArrowLeft') fPrevTap();
    return;
  }
  const open = [story, lb].find(o => !o.hidden); if (!open) return;
  if (ev.key === 'Escape') closeOv(open);
  else if (ev.key === 'ArrowRight' && open === story) $('#stNext').click();
  else if (ev.key === 'ArrowLeft' && open === story) $('#stPrev').click();
});

/* ===== 손으로 하는 방식(모듈): 카드마다 이야기에서 나온 한 가지 ===== */
const MODS = {};
function initMods(){ $$('[data-mod]').forEach(el => { const m = MODS[el.dataset.mod]; if (m && m.init) m.init(el, (DATA.mods || {})[el.dataset.mod] || {}); }); }
const pad2 = n => String(n).padStart(2, '0');
const ymd = d => `${d.getFullYear()}.${pad2(d.getMonth() + 1)}.${pad2(d.getDate())}`;
const mdK = d => `${d.getMonth() + 1}월 ${d.getDate()}일`;

/* --- 날짜 따라가기: 수레바퀴 화환 --- */
function wreathSVG(o){
  const W = 420, H = 292, cx = 210, cy = 172, rx = 166, ry = 74, u = o.uid, now = o.look === 'now';
  let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(o.aria || '수레바퀴 위에 초가 둥글게 꽂힌 대림절 화환')}"><defs>
<radialGradient id="${u}h"><stop offset="0" stop-color="#ffd98f" stop-opacity=".9"/><stop offset=".45" stop-color="#ffb35c" stop-opacity=".32"/><stop offset="1" stop-color="#ff9a3c" stop-opacity="0"/></radialGradient>
<linearGradient id="${u}f" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ff7a1f"/><stop offset=".5" stop-color="#ffc45e"/><stop offset="1" stop-color="#fff6d8"/></linearGradient></defs>`;
  if (now) s += `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="none" stroke="#1d3a22" stroke-width="30"/><ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="none" stroke="#3f7445" stroke-width="18" stroke-dasharray="2 3"/><ellipse cx="${cx}" cy="${cy - 2}" rx="${rx}" ry="${ry}" fill="none" stroke="#5c9a5a" stroke-width="6" stroke-dasharray="1 6" opacity=".7"/>`;
  else s += `<ellipse cx="${cx}" cy="${cy + 3}" rx="${rx}" ry="${ry}" fill="none" stroke="#2e1d0e" stroke-width="17"/><ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="none" stroke="#7a4f27" stroke-width="13"/><ellipse cx="${cx}" cy="${cy - 2}" rx="${rx}" ry="${ry}" fill="none" stroke="#a87443" stroke-width="3" opacity=".7"/>`;
  for (let k = 0; k < 8; k++) { const a = Math.PI * k / 4, c = Math.cos(a), si = Math.sin(a); s += `<line x1="${(cx + 20 * c).toFixed(1)}" y1="${(cy + 9 * si).toFixed(1)}" x2="${(cx + (rx - 7) * c).toFixed(1)}" y2="${(cy + (ry - 3) * si).toFixed(1)}" stroke="${now ? '#2a1a0c' : '#5a3818'}" stroke-width="5" stroke-linecap="round"/>`; }
  s += `<ellipse cx="${cx}" cy="${cy}" rx="22" ry="10" fill="#3d2610"/><ellipse cx="${cx}" cy="${cy - 2}" rx="13" ry="6" fill="#6b4424"/>`;
  const cs = [];
  for (let i = 0; i < o.n; i++) {
    const th = Math.PI / 2 + 2 * Math.PI * i / o.n, x = cx + rx * Math.cos(th), y = cy + ry * Math.sin(th), dp = (Math.sin(th) + 1) / 2, sc = .78 + .32 * dp;
    cs.push({i, x, y, sc, lx: cx + (rx - 34) * Math.cos(th), ly: cy + (ry - 17) * Math.sin(th) + 4});
  }
  cs.sort((a, b) => a.y - b.y);
  for (const c of cs) {
    const sun = o.sun && o.sun[c.i], st = o.states[c.i];
    const h = (now ? (sun ? 42 : 27) : 31) * c.sc, w = (now ? (sun ? 12 : 8) : 9) * c.sc;
    const fill = now ? (sun ? '#f7f3ea' : '#b8322a') : '#eadbb2', edge = now ? (sun ? '#cfc6b3' : '#7d1d17') : '#b49863';
    const fy = -h - 2;
    s += `<g class="c ${st}${o.fresh === c.i ? ' new' : ''}" data-i="${c.i}" transform="translate(${c.x.toFixed(1)},${c.y.toFixed(1)})">`
      + `<g class="hit${st === 'today' ? ' today' : ''}"${st === 'today' ? ` role="button" tabindex="0" aria-label="${esc(o.todayLabel || '오늘의 초 켜기')}"` : ''}>`
      + `<rect x="-19" y="${(-h - 30).toFixed(1)}" width="38" height="${(h + 40).toFixed(1)}" fill="transparent"/>`
      + (st === 'today' ? `<ellipse class="ring" cx="0" cy="${(-h / 2).toFixed(1)}" rx="${(w * 1.3).toFixed(1)}" ry="${(h * .62).toFixed(1)}"/>` : '')
      + `<rect class="wax" x="${(-w / 2).toFixed(1)}" y="${(-h).toFixed(1)}" width="${w.toFixed(1)}" height="${h.toFixed(1)}" rx="${(w * .32).toFixed(1)}" fill="${fill}" stroke="${edge}" stroke-width="1"/>`
      + `<line x1="0" y1="${(-h).toFixed(1)}" x2="0" y2="${(-h - 3.5).toFixed(1)}" stroke="#2b1c0e" stroke-width="1.2"/>`
      + `<g class="fl"><circle cx="0" cy="${(fy - 7).toFixed(1)}" r="${(17 * c.sc).toFixed(1)}" fill="url(#${u}h)"/><path class="flame" d="M0 ${fy.toFixed(1)} C ${(4.2 * c.sc).toFixed(1)} ${(fy - 4).toFixed(1)} ${(3.4 * c.sc).toFixed(1)} ${(fy - 10 * c.sc).toFixed(1)} 0 ${(fy - 17 * c.sc).toFixed(1)} C ${(-3.4 * c.sc).toFixed(1)} ${(fy - 10 * c.sc).toFixed(1)} ${(-4.2 * c.sc).toFixed(1)} ${(fy - 4).toFixed(1)} 0 ${fy.toFixed(1)} Z" fill="url(#${u}f)"/></g>`
      + `</g>`;
    s += `</g>`;
    if (o.labels && o.labels[c.i]) s += `<text class="dlab${sun ? ' sun' : ''}" x="${c.lx.toFixed(1)}" y="${c.ly.toFixed(1)}">${esc(o.labels[c.i])}</text>`;
  }
  return s + '</svg>';
}
MODS.wreath = (() => {
  let el, cfg, sim = null, look = 'then', fresh = -1, simLit = [], fRoot = null, fN = 24;
  const ws = () => { P.m.wreath = P.m.wreath || {lit: []}; return P.m.wreath; };
  const lits = () => sim ? simLit : ws().lit;
  function advent1(y){ const c = new Date(y, 11, 25), w = c.getDay(); return new Date(y, 11, 25 - (w === 0 ? 7 : w) - 21); }
  function season(now){
    let y = now.getFullYear(); if (now > new Date(y, 11, 24, 23, 59, 59)) y++;
    const a = advent1(y), days = [];
    for (let d = new Date(a); d <= new Date(y, 11, 24); d = new Date(d.getFullYear(), d.getMonth(), d.getDate() + 1)) days.push(d);
    return {y, a, days, inAdv: now >= a};
  }
  function model(){
    const now = sim ? new Date(sim) : new Date(), S = season(now), n = S.days.length, td = ymd(now);
    const ss = ymd(new Date(S.y - 1, 11, 25)), L = lits();
    const litThis = L.filter(x => x >= ss && x <= td), litToday = L.includes(td);
    const states = new Array(n).fill('off'); let ti = -1;
    if (S.inAdv) {
      const k = S.days.findIndex(d => ymd(d) === td);
      for (let i = 0; i < k; i++) states[i] = 'lit';
      ti = k; states[k] = litToday ? 'lit' : 'today';
    } else {
      const c = Math.min(n, litThis.length);
      for (let i = 0; i < c; i++) states[i] = 'lit';
      if (!litToday && c < n) { ti = c; states[c] = 'today'; }
    }
    return {now, S, n, states, ti, litToday, td};
  }
  function say(h){ el.querySelector('.wr-say').innerHTML = h; }
  function render(){
    const M = model(), sun = M.S.days.map(d => d.getDay() === 0);
    let wk = 0; const labels = M.S.days.map((d, i) => (d.getDay() === 0 ? `대림 ${++wk}` : (i === M.ti ? '오늘' : '')));
    el.querySelector('.wr-svg').innerHTML = wreathSVG({n: M.n, states: M.states, look, sun, uid: 'wp', fresh, labels, todayLabel: `오늘(${mdK(M.now)})의 초 켜기`});
    const litN = M.states.filter(x => x === 'lit').length;
    el.style.setProperty('--wglow', (0.05 + 0.42 * litN / M.n).toFixed(3));
    el.querySelector('.wr-count').innerHTML = `${M.S.y}년 대림절 화환 · 초 ${M.n}개 중 <b>${litN}</b>개 켜짐 · 내가 켠 날 <b>${lits().length}</b>번`;
    if (fresh < 0) {
      if (M.ti >= 0 && M.states[M.ti] === 'today') say(M.S.inAdv ? `오늘은 ${mdK(M.now)}이에요. 오늘의 초가 기다리고 있어요.<br>깜박이는 초를 눌러 켜 보세요.` : `${M.S.y}년 대림절은 ${mdK(M.S.a)}에 시작해요. 그때까지는 찾아온 날마다 초를 하나씩 켤 수 있어요.<br>깜박이는 초를 눌러 보세요.`);
      else if (M.litToday) say(afterLit(M));
      else say(`${M.n}개 초가 모두 켜졌어요. 성탄을 기다리는 화환이 다 찼어요.`);
    }
    fresh = -1;
    el.querySelectorAll('.c').forEach(g => {
      const i = +g.dataset.i, hit = g.querySelector('.hit');
      const go = () => {
        const N = model();
        if (i === N.ti && N.states[i] === 'today') {
          lits().push(N.td); if (!sim) save(); fresh = i; render(); say(afterLit(model(), true)); goals();
        } else {
          const d = N.S.days[i];
          if (N.S.inAdv) say(i < N.ti || N.states[i] === 'lit' ? `${mdK(d)}의 초예요. 이미 불이 켜진 날이에요.` : `${mdK(d)}의 초예요. 그날이 오면 켤 수 있어요.`);
          else say(N.states[i] === 'lit' ? `이미 켠 ${i + 1}번째 초예요.` : `${i + 1}번째 초예요. 하루에 하나씩, 찾아온 날마다 켤 수 있어요.`);
        }
      };
      hit.addEventListener('click', go);
      hit.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); } });
    });
  }
  function afterLit(M, justNow){
    const left = M.S.inAdv ? Math.round((new Date(M.S.y, 11, 24) - new Date(M.now.getFullYear(), M.now.getMonth(), M.now.getDate())) / 864e5) : 0;
    if (M.S.inAdv && left === 0) return `오늘은 성탄 전야예요. 화환의 초 ${M.n}개가 모두 켜졌어요.<br><span style="color:#ffe2ad">“${esc(cfg.eve || '')}”</span>`;
    if (M.S.inAdv) return `${justNow ? '오늘의 초가 켜졌어요. ' : '오늘의 초는 이미 켰어요. '}성탄 전야까지 ${left}일 남았어요.`;
    return `${justNow ? '오늘의 초를 켰어요. ' : '오늘의 초는 이미 켰어요. '}다른 날 다시 오면 다음 초를 켤 수 있어요.`;
  }
  function goals(){
    if (sim) return;
    const L = ws().lit.length;
    if (L >= 3) mark('wr3'); if (L >= 7) mark('wr7');
    if (ws().lit.some(x => x.slice(5) === '12.24')) mark('wr24');
  }
  MODS_STATUS.wr3 = () => { const L = ws().lit.length; return L >= 3 ? `서로 다른 날 ${L}번 켰어요` : `켠 날 ${L} / 3`; };
  MODS_STATUS.wr7 = () => { const L = ws().lit.length; return L >= 7 ? `서로 다른 날 ${L}번 켰어요` : `켠 날 ${L} / 7`; };
  MODS_STATUS.wr24 = () => P.ev.wr24 ? '성탄 전야의 초를 켰어요' : '12월 24일에 마지막 초를 켜면 채워져요';
  return {
    init(e, c){
      el = e; cfg = c;
      el.querySelectorAll('.wr-tabs button').forEach(b => b.onclick = () => { look = b.dataset.look; el.querySelectorAll('.wr-tabs button').forEach(x => x.setAttribute('aria-pressed', String(x === b))); el.querySelector('.wr-look').innerHTML = cfg.looks[look]; render(); });
      el.querySelector('.wr-look').innerHTML = cfg.looks[look];
      el.querySelectorAll('.sim button').forEach(b => b.onclick = () => { sim = b.dataset.d === 'today' ? null : b.dataset.d; simLit = []; el.querySelectorAll('.sim button').forEach(x => x.classList.toggle('on', x === b)); render(); });
      render(); goals();
    },
    film(layer, s){ fN = s.n || 24; layer.innerHTML = `<div class="wr">${wreathSVG({n: fN, states: new Array(fN).fill('off'), look: s.look || 'then', uid: 'wf', sun: null})}</div><div class="f-day2"><span class="fdn">${esc(s.d0 || '')}</span><small>${esc(s.dsub || '')}</small></div>`; fRoot = layer; },
    act(a){
      if (!fRoot) return;
      if (a === 'run') { for (let k = 0; k < fN; k++) later(() => { const g = fRoot.querySelector(`.c[data-i="${k}"]`); if (g) g.classList.add('lit', 'new'); const d = fRoot.querySelector('.fdn'); if (d) d.textContent = `12월 ${k + 1}일`; }, 400 + 290 * k); }
      if (a === 'now') { const st = new Array(fN).fill('lit'), sun = new Array(fN).fill(false); [0, 7, 14, 21].forEach(k => { if (k < fN) sun[k] = true; }); fRoot.querySelector('.wr').innerHTML = wreathSVG({n: fN, states: st, look: 'now', uid: 'wf2', sun}); const d = fRoot.querySelector('.fdn'); if (d) d.textContent = '오늘의 화환'; }
    },
    filmStop(){ fRoot = null; }
  };
})();

/* --- 소리: 그날 밤의 소리(기타·두 목소리·성가대) --- */
MODS.voices = (() => {
  let el, cfg, ctx = null, bufs = null, loading = null, srcs = [], gains = [], anas = [], master = null, t0 = 0, off = 0, playing = false, raf = 0, verse = 1, inFilm = false, fRoot = null, fT0 = 0, fRaf = 0;
  const on = {};
  const vs = () => { P.m.voices = P.m.voices || {seen: {}}; return P.m.voices; };
  const dur = () => bufs ? Math.max(...bufs.map(b => b.duration)) : (cfg.dur || 50);
  async function load(){
    if (bufs) return bufs;
    if (!loading) {
      const AC = window.AudioContext || window.webkitAudioContext; if (!AC) throw new Error('no audio');
      ctx = ctx || new AC();
      loading = Promise.all(cfg.parts.map(p => fetch(p.u).then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.arrayBuffer(); }).then(b => new Promise((res, rej) => ctx.decodeAudioData(b, res, rej)))))
        .then(bs => (bufs = bs)).catch(e => { loading = null; throw e; });
    }
    return loading;
  }
  function halt(){ srcs.forEach(s => { try { s.onended = null; s.stop(); } catch (e) {} }); srcs = []; anas = []; if (master) { try { master.disconnect(); } catch (e) {} } master = null; playing = false; cancelAnimationFrame(raf); }
  const pos = () => playing ? ctx.currentTime - t0 : off;
  function start(from, all){
    halt(); if (window.__oldSnd) window.__oldSnd.pause();
    master = ctx.createGain(); master.gain.value = 0.95; master.connect(ctx.destination);
    let li = 0; bufs.forEach((b, i) => { if (b.duration > bufs[li].duration) li = i; });
    cfg.parts.forEach((p, i) => {
      const s = ctx.createBufferSource(); s.buffer = bufs[i];
      const g = ctx.createGain(); g.gain.value = (all || on[p.id]) ? 1 : 0;
      const a = ctx.createAnalyser(); a.fftSize = 512;
      s.connect(g); g.connect(a); a.connect(master);
      s.start(0, Math.min(from, bufs[i].duration - 0.01));
      srcs.push(s); gains.push(g); anas.push(a);
    });
    srcs[li].onended = () => { if (playing) finish(); };
    t0 = ctx.currentTime - from; playing = true; loop();
  }
  function finish(){ halt(); off = 0; if (!inFilm && on.guitar && on.v1 && on.v2) mark('vo3'); setBtn(false); paint(); }
  function setBtn(v){ if (!el) return; const b = el.querySelector('.vo-play'); b.setAttribute('aria-pressed', String(v)); b.setAttribute('aria-label', v ? '멈추기' : '들어 보기'); b.innerHTML = v ? '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1" fill="currentColor"/><rect x="14" y="5" width="4" height="14" rx="1" fill="currentColor"/></svg>' : '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z" fill="currentColor"/></svg>'; }
  function loop(){ paint(); raf = requestAnimationFrame(loop); }
  function level(i){ const a = anas[i]; if (!a) return 0; const b = new Float32Array(a.fftSize); a.getFloatTimeDomainData(b); let r = 0; for (let k = 0; k < b.length; k++) r += b[k] * b[k]; return Math.min(1, Math.sqrt(r / b.length) * 10); }
  function lineAt(t){ return cfg.lines.find(L => t >= L.at && t < L.end); }
  function paint(){
    if (inFilm) return;
    const t = pos(), D = dur();
    el.querySelector('.vo-bar i').style.width = Math.min(100, 100 * t / D).toFixed(2) + '%';
    const L = (playing || off > 0) ? lineAt(t) : null;
    el.querySelectorAll('.vo-lines li').forEach(li => { const on2 = !!L && +li.dataset.n === L.n; li.classList.toggle('on', on2); const w = li.querySelector('.who'); if (w) w.textContent = on2 && L.choir ? '성가대가 따라 불러요' : ''; });
    el.querySelectorAll('.vo-part').forEach((b, i) => { const lv = playing && on[cfg.parts[i].id] ? level(i) : 0; b.querySelectorAll('.lv i').forEach((x, k) => { x.style.height = Math.max(14, Math.min(100, lv * (80 + 25 * Math.sin(t * 7 + k * 2)))) + '%'; }); });
  }
  function drawVerse(){
    const V = cfg.verses[verse - 1];
    el.querySelector('.vo-lines').innerHTML = V.de.map((d, n) => `<li data-n="${n}"><span class="de">${esc(d)}</span><span class="ko">${esc(V.ko[n])}<span class="who"></span></span></li>`).join('');
    el.querySelectorAll('.vo-vs button').forEach(b => { b.setAttribute('aria-pressed', String(+b.dataset.v === verse)); b.classList.toggle('seen', !!vs().seen[b.dataset.v]); });
    const cap = el.querySelector('.vo-vcap'); if (cap) cap.textContent = V.cap || '';
    paint();
  }
  function hint(t){ const h = el.querySelector('.vo-hint'); if (h) h.textContent = t; }
  MODS_STATUS.vo6 = () => { const n = Object.keys(vs().seen).length; return n >= 6 ? '여섯 절을 다 읽었어요' : `읽은 절 ${n} / 6`; };
  MODS_STATUS.vo3 = () => P.ev.vo3 ? '셋이 함께 울리는 소리를 끝까지 들었어요' : '기타·첫째·둘째 목소리를 모두 켜고 끝까지 들어 보세요';
  function fpaint(){
    if (!fRoot) return;
    const t = playing ? pos() : (performance.now() - fT0) / 1000;
    const L = lineAt(t);
    fRoot.querySelectorAll('.row').forEach((r, i) => {
      const id = cfg.parts[i].id;
      let act = id === 'guitar' ? t > 0.2 && t < dur() - 1 : (id === 'choir' ? !!(L && L.choir) : !!(L && !L.choir));
      if (playing) act = level(i) > 0.06;
      r.classList.toggle('on', act);
    });
    fRaf = requestAnimationFrame(fpaint);
  }
  async function fplay(from){ try { await load(); if (ctx.state === 'suspended') await ctx.resume(); if (inFilm) start(from, true); } catch (e) {} }
  return {
    init(e, c){
      el = e; cfg = c;
      cfg.parts.forEach(p => { on[p.id] = !!p.on; });
      el.querySelector('.vo-parts').innerHTML = cfg.parts.map(p => `<button type="button" class="vo-part" data-p="${p.id}" aria-pressed="${on[p.id]}"><span class="lv" aria-hidden="true"><i></i><i></i><i></i></span><span class="tx2"><b>${esc(p.t)}</b><span>${esc(p.who || '')}</span></span></button>`).join('');
      el.querySelectorAll('.vo-part').forEach((b, i) => b.onclick = () => {
        const p = cfg.parts[i]; on[p.id] = !on[p.id]; b.setAttribute('aria-pressed', String(on[p.id]));
        if (gains[i] && ctx) gains[i].gain.setTargetAtTime(on[p.id] ? 1 : 0, ctx.currentTime, 0.06);
        hint(on[p.id] ? (p.say || '') : `${p.t}를 껐어요.`);
        if (!playing && on[p.id]) el.querySelector('.vo-play').focus();
      });
      el.querySelector('.vo-play').onclick = async () => {
        if (playing) { off = pos(); halt(); setBtn(false); return; }
        hint('소리를 불러오는 중이에요…');
        try { await load(); if (ctx.state === 'suspended') await ctx.resume(); }
        catch (err) { hint('이 브라우저에서는 소리를 불러오지 못했어요. 다른 브라우저에서 열어 보세요.'); return; }
        hint(cfg.startHint || ''); if (off >= dur() - 0.1) off = 0;
        inFilm = false; start(off, false); setBtn(true);
      };
      el.querySelectorAll('.vo-vs button').forEach(b => b.onclick = () => { verse = +b.dataset.v; vs().seen[verse] = true; save(); drawVerse(); if (Object.keys(vs().seen).length >= 6) mark('vo6'); else check(); });
      vs().seen[1] = true; save();
      setBtn(false); drawVerse(); hint(cfg.firstHint || '');
    },
    pauseAll(){ if (playing && !inFilm) { off = pos(); halt(); setBtn(false); } },
    film(layer, s){
      if (playing) { halt(); off = 0; setBtn(false); }
      inFilm = true; fT0 = performance.now();
      layer.innerHTML = `<div class="f-vo">${cfg.parts.map(p => `<div class="row" data-p="${p.id}"><i></i><b>${esc(p.t)}</b><span>${esc(p.who || '')}</span></div>`).join('')}</div>`;
      fRoot = layer; cancelAnimationFrame(fRaf); fpaint();
      if (fSoundOn) fplay(0);
    },
    filmSound(v){ if (!inFilm || !fRoot) return; if (v) fplay((performance.now() - fT0) / 1000); else halt(); },
    filmStop(){ if (inFilm) { halt(); off = 0; inFilm = false; setBtn(false); } fRoot = null; cancelAnimationFrame(fRaf); }
  };
})();

/* --- 옛 소리 상자(진짜 녹음) --- */
(function(){
  const a = new Audio(); a.preload = 'none'; let cur = null; window.__oldSnd = a;
  const reset = () => { $$('.snd1').forEach(x => x.setAttribute('aria-pressed', 'false')); cur = null; };
  $$('.snd1').forEach(b => b.onclick = () => {
    if (cur === b && !a.paused) { a.pause(); reset(); return; }
    if (MODS.voices && MODS.voices.pauseAll) MODS.voices.pauseAll();
    reset(); a.src = b.dataset.u; a.currentTime = 0;
    a.play().then(() => { cur = b; b.setAttribute('aria-pressed', 'true'); if (b.dataset.ev) mark(b.dataset.ev); }).catch(() => {});
  });
  a.addEventListener('ended', reset); a.addEventListener('pause', () => { if (!a.ended) reset(); });
})();

/* --- 놓아 보기: 그레초의 밤 --- */
MODS.place = (() => {
  let el, cfg, placed = [], inOrder = true, fRoot = null;
  const stage = u => cfg.svg.replace(/__U__/g, u);
  function apply(root, id){
    if (id === 'lights') root.querySelectorAll('.lt').forEach((x, k) => setTimeout(() => x.classList.add('on'), 120 * k));
    else { const o = root.querySelector(`[data-o="${id}"]`); if (o) o.classList.add('on'); }
    const g = root.querySelector('.glow'); const k = root.querySelectorAll('.obj.on').length + (id === 'lights' || root.querySelector('.lt.on') ? 1 : 0);
    if (g) g.style.opacity = Math.min(1, 0.14 + 0.15 * k).toFixed(2);
  }
  const say = h => { el.querySelector('.pl-say').innerHTML = h; };
  function markNext(){ const nx = cfg.items[placed.length]; el.querySelectorAll('.pl-item').forEach(b => b.classList.toggle('next', !!nx && b.dataset.id === nx.id)); }
  function put(id){
    if (placed.includes(id)) return;
    const exp = cfg.items[placed.length].id, it = cfg.items.find(x => x.id === id);
    if (id !== exp) inOrder = false;
    placed.push(id); apply(el, id);
    el.querySelector(`.pl-item[data-id="${id}"]`).setAttribute('aria-pressed', 'true');
    markNext();
    const wrong = cfg.wrongOrder ? esc(cfg.wrongOrder).replace('{order}', esc(cfg.order)) : `기록에 적힌 차례는 ${esc(cfg.order)}예요.`;
    say(esc(it.say) + (id !== exp ? `<span class="la">${wrong}</span>` : `<span class="la">${esc(it.la)}</span>`));
    if (placed.length === cfg.items.length) setTimeout(climax, 1500);
  }
  function climax(){
    el.querySelector('.pl').classList.add('lit'); if (cfg.daylight !== false) document.body.classList.add('daylight'); document.body.classList.remove('dim');
    say(cfg.climax);
    if (inOrder) mark('plOrder');
    el.querySelector('.pl-row').hidden = false;
    const hm = el.querySelector('.pl-home');
    if (hm && hasHome()) { hm.hidden = false; drawHome(); }
  }
  const hasHome = () => Array.isArray(cfg.home) && cfg.home.length > 0;
  const homeLabel = () => (cfg && cfg.homeLabel) || '우리 집 구유 자리';
  function drawHome(){
    const box = el.querySelector('.pl-home .ch'), cur = P.ev.home || '';
    box.innerHTML = cfg.home.map(h => `<button type="button" aria-pressed="${cur === h}">${esc(h)}</button>`).join('') + `<span class="own"><input type="text" maxlength="30" placeholder="다른 곳이라면 직접 적기" aria-label="${esc(homeLabel())} 직접 적기"><button type="button" class="pl-mine">적기</button></span>`;
    box.querySelectorAll('button:not(.pl-mine)').forEach(b => b.onclick = () => { mark('home', b.textContent); drawHome(); });
    const inp = box.querySelector('input'); box.querySelector('.pl-mine').onclick = () => { const v = inp.value.trim(); if (v) { mark('home', v); drawHome(); } };
    el.querySelector('.pl-home .got').textContent = cur ? `${homeLabel()} · ${cur}` : '';
  }
  function reset(){
    placed = []; inOrder = true; document.body.classList.remove('daylight');
    el.querySelector('.pl-stage').innerHTML = stage('pp'); el.querySelector('.pl').classList.remove('lit');
    el.querySelectorAll('.pl-item').forEach(b => b.setAttribute('aria-pressed', 'false'));
    el.querySelector('.pl-row').hidden = true; const hm = el.querySelector('.pl-home'); if (hm) hm.hidden = true;
    markNext(); say(cfg.intro);
  }
  MODS_STATUS.home = () => P.ev.home ? `${homeLabel()} · ${P.ev.home}` : ((cfg && cfg.homeWait) || '그레초의 밤을 다 놓아 본 뒤 고를 수 있어요');
  MODS_STATUS.plOrder = () => P.ev.plOrder ? ((cfg && cfg.orderDone) || '기록 차례대로 다 놓았어요') : `차례: ${cfg ? cfg.order : ''}`;
  return {
    init(e, c){
      el = e; cfg = c;
      el.querySelector('.pl-tray').innerHTML = cfg.items.map(it => `<button type="button" class="pl-item" data-id="${it.id}" aria-pressed="false"><b>${esc(it.t)}</b><small>${esc(it.la)}</small></button>`).join('');
      el.querySelectorAll('.pl-item').forEach(b => b.onclick = () => put(b.dataset.id));
      el.querySelector('.pl-again').onclick = reset;
      reset();
    },
    film(layer, s){ layer.innerHTML = `<div class="pl">${stage('pf')}</div>`; fRoot = layer.querySelector('.pl'); },
    act(a){ if (!fRoot) return; if (a === 'day') fRoot.classList.add('lit'); else apply(fRoot, a); },
    filmStop(){ fRoot = null; }
  };
})();

/* ===== 자료만 적으면 되는 공통 방식(키트 2판): 찾아보기 · 비추기 · 그때와 지금 · 지도 위 길 · 고르기 ===== */
const modState = name => { P.m[name] = P.m[name] || {}; return P.m[name]; };
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
function fitBox(layer, w, h){  // 영화 화면 안에 그림 비율 그대로 들어가는 상자
  const r = layer.getBoundingClientRect(), cs = getComputedStyle(layer);
  const aw = r.width - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight), ah = r.height - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
  const k = Math.min(aw / w, ah / h); return {w: Math.max(80, w * k), h: Math.max(60, h * k)};
}

/* --- 찾아보기: 그림 속 작은 것들을 하나씩 --- */
MODS.look = (() => {
  let el, cfg, fRoot = null, cur = -1, zoomed = false;
  const st = () => { const s = modState('look'); s.found = s.found || []; return s; };
  function zoom(root, i){
    const z = root.querySelector('.lk-zoom'); if (!z) return;
    if (i == null || i < 0) { z.style.setProperty('--z', 1); root.classList.remove('zoomed'); return; }
    const sp = cfg.spots[i]; z.style.setProperty('--ox', sp.x + '%'); z.style.setProperty('--oy', sp.y + '%'); z.style.setProperty('--z', cfg.zoom || 2); root.classList.add('zoomed');
  }
  function zbtn(){ const b = el.querySelector('.lk-zoombtn'); b.disabled = cur < 0; b.textContent = zoomed ? '전체 보기' : '가까이 보기'; b.setAttribute('aria-pressed', String(zoomed)); }
  function show(i){
    const sp = cfg.spots[i], S = st(); cur = i;
    if (!S.found.includes(i)) { S.found.push(i); save(); }
    el.querySelectorAll('.lk-spot').forEach(b => { b.classList.toggle('on', +b.dataset.i === i); b.classList.toggle('got', S.found.includes(+b.dataset.i)); });
    el.querySelectorAll('.lk-list button').forEach(b => { const k = +b.dataset.i, got = S.found.includes(k); b.classList.toggle('got', got); b.classList.toggle('on', k === i); b.textContent = `${k + 1}. ${got ? cfg.spots[k].t : '?'}`; });
    el.querySelector('.lk-info').innerHTML = `<b>${i + 1}. ${esc(sp.t)}</b><p class="a">${sp.p}</p><p class="k">${esc(sp.kid || sp.p.replace(/<[^>]+>/g, ''))}</p>`;
    if (zoomed) zoom(el, i);
    zbtn(); count();
  }
  function count(){
    const n = st().found.length, N = cfg.spots.length;
    el.querySelector('.lk-n').textContent = `찾은 곳 ${n} / ${N}`;
    if (n >= N) { el.querySelector('.lk-done').hidden = false; mark('look'); }
  }
  MODS_STATUS.look = () => cfg ? (P.ev.look ? `${cfg.spots.length}곳을 다 찾았어요` : `찾은 곳 ${st().found.length} / ${cfg.spots.length}`) : '';
  return {
    init(e, c){
      el = e; cfg = c;
      el.querySelectorAll('.lk-spot,.lk-list button').forEach(b => b.onclick = () => show(+b.dataset.i));
      el.querySelector('.lk-zoombtn').onclick = () => { zoomed = !zoomed && cur >= 0; zoom(el, zoomed ? cur : -1); zbtn(); };
      const S = st(); el.querySelectorAll('.lk-spot').forEach(b => b.classList.toggle('got', S.found.includes(+b.dataset.i)));
      el.querySelectorAll('.lk-list button').forEach(b => { const k = +b.dataset.i; if (S.found.includes(k)) { b.classList.add('got'); b.textContent = `${k + 1}. ${cfg.spots[k].t}`; } });
      zbtn(); count();
    },
    film(layer, s){
      const im = cfg.img, b = fitBox(layer, im.w, im.h);
      layer.innerHTML = `<div class="lk lk-f" style="width:${b.w}px;height:${b.h}px"><div class="lk-zoom"><img src="${im.u}" alt="${esc(im.alt)}">${cfg.spots.map((sp, i) => `<span class="lk-ring" data-i="${i}" style="left:${sp.x}%;top:${sp.y}%"></span>`).join('')}</div></div>`;
      fRoot = layer.querySelector('.lk');
    },
    act(a){
      if (!fRoot) return;
      const m = /^spot:(\d+)$/.exec(a);
      fRoot.querySelectorAll('.lk-ring').forEach(r => r.classList.toggle('on', !!m && +r.dataset.i === +m[1] - 1));
      zoom(fRoot, m ? +m[1] - 1 : -1);
    },
    filmStop(){ fRoot = null; }
  };
})();

/* --- 비추기: 어둠 속 그림을 빛으로 --- */
MODS.reveal = (() => {
  let el, cfg, img = null, fx = null;
  const cells = new Set(); let lastMarkShown = -1;
  const st = () => { const s = modState('reveal'); s.found = s.found || []; return s; };
  function setup(box){
    const cv = box.querySelector('canvas.rv-lit'), mk = document.createElement('canvas');
    const ctx = cv.getContext('2d'), mctx = mk.getContext('2d');
    const o = {box, cv, mk, ctx, mctx, scale: 1};
    const size = () => { const r = box.getBoundingClientRect(); const dpr = Math.min(2, window.devicePixelRatio || 1);
      const W = Math.max(1, Math.round(r.width * dpr)), H = Math.max(1, Math.round(r.height * dpr));
      if (cv.width === W && cv.height === H) return;
      const old = document.createElement('canvas'); old.width = mk.width; old.height = mk.height; if (mk.width) old.getContext('2d').drawImage(mk, 0, 0);
      cv.width = mk.width = W; cv.height = mk.height = H; if (old.width) mctx.drawImage(old, 0, 0, W, H); o.scale = dpr; paint(o); };
    o.size = size; size(); new ResizeObserver(size).observe(box);
    return o;
  }
  function paint(o){
    const {cv, ctx, mk} = o; if (!img || !img.complete || !cv.width) return;
    ctx.globalCompositeOperation = 'source-over'; ctx.clearRect(0, 0, cv.width, cv.height);
    ctx.drawImage(img, 0, 0, cv.width, cv.height);
    ctx.globalCompositeOperation = 'destination-in'; ctx.drawImage(mk, 0, 0);
    ctx.globalCompositeOperation = 'source-over';
  }
  function light(o, px, py, r){   // px,py: 상자 안 0~1
    const {mk, mctx} = o, X = px * mk.width, Y = py * mk.height, R = r * Math.max(mk.width, mk.height);
    const g = mctx.createRadialGradient(X, Y, 0, X, Y, R);
    g.addColorStop(0, 'rgba(0,0,0,1)'); g.addColorStop(.55, 'rgba(0,0,0,.85)'); g.addColorStop(1, 'rgba(0,0,0,0)');
    mctx.fillStyle = g; mctx.beginPath(); mctx.arc(X, Y, R, 0, Math.PI * 2); mctx.fill();
    paint(o);
  }
  function fillAll(o){ o.mctx.fillStyle = '#000'; o.mctx.fillRect(0, 0, o.mk.width, o.mk.height); paint(o); }
  function glow(box, px, py){ box.style.setProperty('--gx', (px * 100).toFixed(1) + '%'); box.style.setProperty('--gy', (py * 100).toFixed(1) + '%'); box.classList.add('lit'); }
  function info(i){
    const m = cfg.marks[i]; el.querySelector('.rv-info').innerHTML = `<b>${esc(m.t)}</b><p>${m.p || ''}</p>`;
  }
  function found(i){
    const S = st();
    el.querySelectorAll(`.rv-tag[data-i="${i}"]`).forEach(t => t.classList.add('on'));
    if (!S.found.includes(i)) { S.found.push(i); save(); info(i); }
    else if (lastMarkShown !== i) info(i);
    lastMarkShown = i; done();
  }
  function done(){
    const S = st(), N = (cfg.marks || []).length;
    el.querySelector('.rv-n').textContent = N ? `찾은 표시 ${S.found.length} / ${N}` + (S.full && S.found.length < N ? ' · 이름표를 눌러 읽어 보세요' : '') : '';
    const all = N ? S.found.length >= N : (S.full || cells.size >= 48);
    if (all) { el.querySelector('.rv-after').hidden = false; mark('reveal'); }
  }
  MODS_STATUS.reveal = () => { if (!cfg) return ''; const N = (cfg.marks || []).length; return P.ev.reveal ? '끝까지 비춰 봤어요' : (N ? `찾은 표시 ${st().found.length} / ${N}` : '그림을 끝까지 비춰 보세요'); };
  let o = null;
  return {
    init(e, c){
      el = e; cfg = c; cfg.marks = cfg.marks || [];
      const box = el.querySelector('.rv-box');
      img = new Image(); img.decoding = 'async'; img.src = cfg.img.u;
      o = setup(box); img.onload = () => paint(o);
      const R = {candle: .11, lamp: .14, torch: .17}[cfg.light] || .12;
      const at = ev => { const r = box.getBoundingClientRect(); return [clamp((ev.clientX - r.left) / r.width, 0, 1), clamp((ev.clientY - r.top) / r.height, 0, 1)]; };
      const move = ev => {
        const [px, py] = at(ev); glow(box, px, py); light(o, px, py, R);
        cells.add(Math.floor(px * 10) + ',' + Math.floor(py * 8));
        cfg.marks.forEach((m, i) => { const dx = (m.x / 100 - px) * box.clientWidth, dy = (m.y / 100 - py) * box.clientHeight; if (Math.hypot(dx, dy) < box.clientWidth * .09) found(i); });
        if (!cfg.marks.length) done();
      };
      box.addEventListener('pointermove', ev => { if (ev.pointerType === 'mouse' || ev.buttons || ev.pressure) move(ev); });
      box.addEventListener('pointerdown', ev => { move(ev); try { box.setPointerCapture(ev.pointerId); } catch (x) {} });
      box.addEventListener('pointerleave', () => box.classList.remove('lit'));
      el.querySelector('.rv-all').onclick = () => { fillAll(o); box.classList.add('full'); const S = st(); S.full = true; save(); el.querySelectorAll('.rv-tag').forEach(t => t.classList.add('on', 'tap')); done();
        if (cfg.marks.length && S.found.length < cfg.marks.length) el.querySelector('.rv-info').innerHTML = '<p>모두 밝혔어요. 이름표를 하나씩 눌러 읽으면 ‘찾은 표시’로 세어져요.</p>'; };
      el.querySelectorAll('.rv-tag').forEach(t => t.onclick = () => found(+t.dataset.i));
      const S = st(); S.found.forEach(i => el.querySelectorAll(`.rv-tag[data-i="${i}"]`).forEach(t => t.classList.add('on')));
      if (S.full) { img.addEventListener('load', () => fillAll(o)); box.classList.add('full'); el.querySelectorAll('.rv-tag').forEach(t => t.classList.add('on', 'tap')); }
      done();
    },
    film(layer, s){
      const im = cfg.img, b = fitBox(layer, im.w, im.h);
      layer.innerHTML = `<div class="rv rv-f"><div class="rv-box" style="width:${b.w}px;height:${b.h}px"><img class="rv-base" src="${im.u}" alt="${esc(im.alt)}"><canvas class="rv-lit"></canvas>${(cfg.marks || []).map((m, i) => `<span class="rv-tag" data-i="${i}" style="left:${m.x}%;top:${m.y}%">${esc(m.t)}</span>`).join('')}<span class="rv-glow"></span></div></div>`;
      fx = setup(layer.querySelector('.rv-box')); fx.raf = 0;
      if (!img || !img.complete) { const i2 = new Image(); i2.src = im.u; i2.onload = () => { if (!img || !img.complete) img = i2; paint(fx); }; }
    },
    act(a){
      if (!fx) return;
      const R = {candle: .11, lamp: .14, torch: .17}[cfg.light] || .12, box = fx.box;
      cancelAnimationFrame(fx.raf);
      const go = (pts, ms, end) => { const t0 = performance.now(); const step = t => { if (!fx) return; const k = clamp((t - t0) / ms, 0, 1), f = k * (pts.length - 1), i = Math.min(pts.length - 2, Math.floor(f)), u = f - i;
        const px = pts[i][0] + (pts[i + 1][0] - pts[i][0]) * u, py = pts[i][1] + (pts[i + 1][1] - pts[i][1]) * u; glow(box, px, py); light(fx, px, py, R * 1.15);
        if (k < 1) fx.raf = requestAnimationFrame(step); else if (end) end(); }; fx.raf = requestAnimationFrame(step); };
      let m;
      if (a === 'light') go([[.12, .25], [.5, .18], [.85, .32], [.6, .55], [.2, .7], [.5, .85], [.88, .78]], 5200);
      else if ((m = /^mark:(\d+)$/.exec(a))) { const k = +m[1] - 1, mk = cfg.marks[k]; if (mk) go([[.5, .5], [mk.x / 100, mk.y / 100]], 1600, () => box.querySelectorAll(`.rv-tag[data-i="${k}"]`).forEach(t => t.classList.add('on'))); }
      else if (a === 'all') { box.classList.add('full'); fillAll(fx); box.querySelectorAll('.rv-tag').forEach(t => t.classList.add('on')); }
    },
    filmStop(){ if (fx) cancelAnimationFrame(fx.raf); fx = null; }
  };
})();

/* --- 그때와 지금: 손잡이를 밀어 겹쳐 보기 --- */
MODS.slider = (() => {
  let el, cfg, cur = 0, fRoot = null, fRaf = 0;
  const st = () => { const s = modState('slider'); s.seen = s.seen || {}; return s; };
  function setP(root, p){ root.querySelector('.sl-box').style.setProperty('--p', p + '%'); }
  function pick(i){
    cur = i; const pr = cfg.pairs[i];
    el.querySelectorAll('.sl-tab').forEach(b => b.setAttribute('aria-pressed', String(+b.dataset.i === i)));
    el.querySelectorAll('.sl-pair').forEach(d => d.hidden = +d.dataset.i !== i);
    const r = el.querySelector(`.sl-pair[data-i="${i}"] .sl-range`); r.value = 50; setP(el.querySelector(`.sl-pair[data-i="${i}"]`), 50);
    status();
  }
  function status(){
    const S = st(), N = cfg.pairs.length, ok = cfg.pairs.filter((_, i) => S.seen[i] && S.seen[i].lo && S.seen[i].hi).length;
    el.querySelector('.sl-n').textContent = N > 1 ? `${cfg.pairsLabel || '끝까지 밀어 본 쌍'} ${ok} / ${N}` : (ok ? (cfg.doneText || '그때와 지금을 끝까지 다 봤어요') : (cfg.hint || '손잡이를 양쪽 끝까지 밀어 보세요'));
    if (ok >= N) mark('slider');
  }
  MODS_STATUS.slider = () => cfg ? (P.ev.slider ? (cfg.doneText || '그때와 지금을 끝까지 다 봤어요') : (cfg.hint || '손잡이를 양쪽 끝까지 밀어 보세요')) : '';
  return {
    init(e, c){
      el = e; cfg = c;
      el.querySelectorAll('.sl-pair').forEach(d => {
        const i = +d.dataset.i, r = d.querySelector('.sl-range');
        r.addEventListener('input', () => { const p = +r.value; setP(d, p); const S = st(); S.seen[i] = S.seen[i] || {}; if (p <= 6) S.seen[i].lo = 1; if (p >= 94) S.seen[i].hi = 1; save(); status(); });
      });
      el.querySelectorAll('.sl-tab').forEach(b => b.onclick = () => pick(+b.dataset.i));
      pick(0);
    },
    film(layer, s){
      const pr = cfg.pairs[0], b = fitBox(layer, pr.now.w, pr.now.h);
      layer.innerHTML = `<div class="sl sl-f" style="width:${b.w}px;height:${b.h}px"><div class="sl-box" style="--p:100%"><img class="sl-now" src="${pr.now.u}" alt="${esc(pr.now.alt)}"><div class="sl-then"><img src="${pr.then.u}" alt="${esc(pr.then.alt)}"></div><div class="sl-handle"></div><span class="sl-lab l">${esc(pr.thenT || '')}</span><span class="sl-lab r">${esc(pr.nowT || '')}</span></div></div>`;
      fRoot = layer.querySelector('.sl'); fRoot._pair = 0;
    },
    act(a){
      if (!fRoot) return; cancelAnimationFrame(fRaf);
      const box = fRoot.querySelector('.sl-box'), from = parseFloat(box.style.getPropertyValue('--p')) || 100;
      const to = (a2, ms) => { const t0 = performance.now(); const step = t => { if (!fRoot) return; const k = clamp((t - t0) / ms, 0, 1), e2 = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; box.style.setProperty('--p', (from + (a2 - from) * e2).toFixed(2) + '%'); if (k < 1) fRaf = requestAnimationFrame(step); }; fRaf = requestAnimationFrame(step); };
      let m;
      if (a === 'now') to(0, 2600); else if (a === 'then') to(100, 2600); else if (a === 'half') to(50, 1600);
      else if ((m = /^pair:(\d+)$/.exec(a)) && cfg.pairs[+m[1] - 1]) {
        const pr = cfg.pairs[+m[1] - 1]; box.querySelector('.sl-now').src = pr.now.u; box.querySelector('.sl-then img').src = pr.then.u;
        box.querySelector('.sl-lab.l').textContent = pr.thenT || ''; box.querySelector('.sl-lab.r').textContent = pr.nowT || ''; box.style.setProperty('--p', '100%');
      }
    },
    filmStop(){ cancelAnimationFrame(fRaf); fRoot = null; }
  };
})();

/* --- 지도 위 길: 한 곳씩 따라가기 --- */
MODS.route = (() => {
  let el, cfg, at = 0, fRoot = null, fAt = 0;
  function seg(root, i, on, anim){  // i번째 구간(i → i+1)
    const p = root.querySelector(`.rt-seg[data-i="${i}"]`); if (!p) return;
    p.classList.toggle('on', on); if (anim) { p.classList.remove('draw'); void p.getBoundingClientRect(); p.classList.add('draw'); }
  }
  function dots(root, upto){ root.querySelectorAll('.rt-dot').forEach(d => { const k = +d.dataset.i; d.classList.toggle('been', k <= upto); d.classList.toggle('here', k === upto); }); root.querySelectorAll('.rt-name').forEach((n, k) => n.classList.toggle('on', k <= upto)); }
  function tell(i){
    const s = cfg.stops[i]; el.querySelector('.rt-info').innerHTML = `<b>${i + 1}. ${esc(s.t)}</b>${s.d ? `<small>${esc(s.d)}</small>` : ''}<p>${s.p || ''}</p>`;
  }
  function go(){
    if (at >= cfg.stops.length - 1) return;
    seg(el, at, true, true); at++; dots(el, at); tell(at);
    if (at === cfg.stops.length - 1) { el.querySelector('.rt-next').hidden = true; el.querySelector('.rt-again').hidden = false; el.querySelector('.rt-end').hidden = false; mark('route'); }
    else el.querySelector('.rt-next').textContent = `다음 곳으로 (${at + 1} / ${cfg.stops.length})`;
  }
  function reset(){
    at = 0; el.querySelectorAll('.rt-seg').forEach(p => p.classList.remove('on', 'draw')); dots(el, 0); tell(0);
    el.querySelector('.rt-next').hidden = false; el.querySelector('.rt-again').hidden = true; el.querySelector('.rt-end').hidden = true;
    el.querySelector('.rt-next').textContent = `다음 곳으로 (1 / ${cfg.stops.length})`;
  }
  MODS_STATUS.route = () => cfg ? (P.ev.route ? '길을 끝까지 따라갔어요' : `‘다음 곳으로’를 눌러 ${cfg.stops.length}곳을 따라가 보세요`) : '';
  return {
    init(e, c){
      el = e; cfg = c;
      el.querySelector('.rt-next').onclick = go; el.querySelector('.rt-again').onclick = reset;
      el.querySelectorAll('.rt-dot').forEach(d => d.onclick = () => { const k = +d.dataset.i; if (k <= at) tell(k); });
      reset();
    },
    film(layer, s){
      const src = el.querySelector('.rt-box'), w = +src.dataset.w || 4, h = +src.dataset.h || 3, b = fitBox(layer, w, h);
      layer.innerHTML = `<div class="rt rt-f" style="width:${b.w}px;height:${b.h}px">${src.outerHTML}</div>`;
      fRoot = layer.querySelector('.rt'); fAt = 0;
      fRoot.querySelectorAll('.rt-seg').forEach(p => p.classList.remove('on', 'draw')); dots(fRoot, 0);
      fRoot.querySelectorAll('.rt-name').forEach((n, k) => n.classList.toggle('on', k === 0));
    },
    act(a){
      if (!fRoot) return; let m;
      const upto = k => { while (fAt < Math.min(k, cfg.stops.length - 1)) { seg(fRoot, fAt, true, true); fAt++; } dots(fRoot, fAt); fRoot.querySelectorAll('.rt-name').forEach((n, j) => n.classList.toggle('on', j <= fAt)); };
      if (a === 'go') upto(fAt + 1); else if (a === 'all') upto(cfg.stops.length - 1); else if ((m = /^stop:(\d+)$/.exec(a))) upto(+m[1] - 1);
    },
    filmStop(){ fRoot = null; }
  };
})();

/* --- 고르기(도우미): 이야기 속 행동을 ‘우리라면?’으로 --- */
MODS.choose = (() => {
  let el, cfg;
  function draw(){
    const cur = P.ev.choose || '';
    el.querySelectorAll('.ch2-opts button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.t === cur)));
    const o = cfg.opts.find(x => x.t === cur); el.querySelector('.ch2-r').innerHTML = o ? `<b>${esc(o.t)}</b> ${o.r || ''}` : '';
  }
  MODS_STATUS.choose = () => P.ev.choose ? `고른 것 · ${P.ev.choose}` : '';
  return {
    init(e, c){ el = e; cfg = c; el.querySelectorAll('.ch2-opts button').forEach(b => b.onclick = () => { mark('choose', b.dataset.t); draw(); }); draw(); }
  };
})();

/* ===== 새 방식(키트 3판 후보 · 견본): 펼쳐 읽기 · 시간 따라 보기 · 만드는 차례 · 날짜 따라 여는 달력 · 흩어진 조각 모으기 · 따라 쓰기 ===== */
const reduceMotion = () => !!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
function tween(from, to, ms, step, done){   // 부드럽게 움직이기. 멈추는 함수를 돌려줘요
  let raf = 0; const t0 = performance.now();
  if (ms <= 1) { step(to); if (done) done(); return () => {}; }
  const f = t => { const k = clamp((t - t0) / ms, 0, 1), e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; step(from + (to - from) * e); if (k < 1) raf = requestAnimationFrame(f); else if (done) done(); };
  raf = requestAnimationFrame(f); return () => cancelAnimationFrame(raf);
}

/* --- 펼쳐 읽기: 옛 문서를 위에서부터 펼치며 한 줄씩 --- */
MODS.unroll = (() => {
  let el, cfg, p = 0, stopT = null, fRoot = null, fP = 0, fStop = null;
  const st = () => { const s = modState('unroll'); s.read = s.read || []; return s; };
  const L = () => cfg.lines || [];
  const start = () => cfg.start != null ? cfg.start : Math.max(6, L()[0] ? L()[0].y0 - 2 : 10);
  function setP(root, v){ root.querySelector('.ur-cover').style.top = v + '%'; }
  function band(root, i){ root.querySelectorAll('.ur-band').forEach(b => b.classList.toggle('on', +b.dataset.i === i)); }
  function lineHTML(i){ const l = L()[i]; return `<b class="ur-o">${esc(l.o)}</b><p>${l.k}</p>${l.n ? `<p class="ur-note">${l.n}</p>` : ''}`; }
  function list(){
    const S = st(), ol = el.querySelector('.ur-list');
    ol.innerHTML = L().map((l, i) => S.read.includes(i) ? `<li><button type="button" data-i="${i}"><span class="ur-lo">${esc(l.o)}</span><span class="ur-lk">${esc(String(l.k).replace(/<[^>]+>/g, ''))}</span></button></li>` : '').join('');
    ol.querySelectorAll('button').forEach(b => b.onclick = () => { const i = +b.dataset.i; band(el, i); el.querySelector('.ur-info').innerHTML = lineHTML(i); });
  }
  function count(){
    const S = st(), N = L().length, all = S.read.length >= N;
    el.querySelector('.ur-n').textContent = `읽은 줄 ${S.read.length} / ${N}`;
    el.querySelector('.ur-more').hidden = all; el.querySelector('.ur-allbtn').hidden = all;
    if (all) { el.querySelector('.ur-done').hidden = false; mark('unroll'); }
  }
  function upd(v){
    p = clamp(v, start(), 100); setP(el, p); el.classList.toggle('moved', p > start() + 1.5);
    const S = st(); let last = -1;
    L().forEach((l, i) => { if (p >= l.y1 - .4 && !S.read.includes(i)) { S.read.push(i); last = i; } });
    if (last >= 0) { S.read.sort((a, b) => a - b); save(); band(el, last); el.querySelector('.ur-info').innerHTML = lineHTML(last); list(); }
    count();
  }
  function to(v, ms){ if (stopT) stopT(); stopT = tween(p, v, reduceMotion() ? 1 : ms, upd); }
  MODS_STATUS.unroll = () => cfg ? (P.ev.unroll ? '끝까지 펼쳐 읽었어요' : `읽은 줄 ${st().read.length} / ${L().length}`) : '';
  return {
    init(e, c){
      el = e; cfg = c;
      const box = el.querySelector('.ur-box'), cover = el.querySelector('.ur-cover'), roll = el.querySelector('.ur-roll');
      const S = st(), seen = S.read.length ? Math.max(...S.read.map(i => L()[i].y1)) + 1.2 : start();
      p = clamp(seen, start(), 100); setP(el, p); el.classList.toggle('moved', p > start() + 1.5); list(); count();
      if (S.read.length) el.querySelector('.ur-info').innerHTML = lineHTML(S.read[S.read.length - 1]);
      const at = ev => { const r = box.getBoundingClientRect(); return (ev.clientY - r.top) / r.height * 100; };
      let drag = false;
      roll.addEventListener('pointerdown', ev => { drag = true; roll.setPointerCapture(ev.pointerId); if (stopT) stopT(); ev.preventDefault(); ev.stopPropagation(); });
      roll.addEventListener('pointermove', ev => { if (drag) upd(at(ev)); });
      const end = () => { drag = false; };
      roll.addEventListener('pointerup', end); roll.addEventListener('pointercancel', end);
      cover.addEventListener('click', ev => { if (ev.target === roll) return; to(Math.max(p, at(ev)), 700); });
      box.addEventListener('keydown', ev => { if (ev.key === 'ArrowDown') { ev.preventDefault(); upd(p + 4); } else if (ev.key === 'ArrowUp') { ev.preventDefault(); upd(p - 4); } });
      el.querySelector('.ur-more').onclick = () => { const S2 = st(), i = L().findIndex((l, k) => !S2.read.includes(k)); to(i < 0 ? 100 : Math.min(100, L()[i].y1 + 1.2), 900); };
      el.querySelector('.ur-allbtn').onclick = () => to(100, 2400);
    },
    film(layer, s){
      const im = cfg.img, b = fitBox(layer, im.w, im.h);
      const bands = L().map((l, i) => `<span class="ur-band" data-i="${i}" style="top:${l.y0}%;height:${l.y1 - l.y0}%;left:${l.x0 || 0}%;width:${(l.x1 || 100) - (l.x0 || 0)}%"></span>`).join('');
      layer.innerHTML = `<div class="ur ur-f" style="width:${b.w}px;height:${b.h}px"><div class="ur-box"><img src="${im.u}" alt="${esc(im.alt)}">${bands}<div class="ur-cover"><span class="ur-roll"></span></div></div></div>`;
      fRoot = layer.querySelector('.ur'); fP = start(); setP(fRoot, fP);
    },
    act(a){
      if (!fRoot) return; let m, v = null, bi = -1;
      if (a === 'open') { v = L()[0] ? L()[0].y1 + 1 : 20; bi = 0; }
      else if (a === 'all') v = 100;
      else if ((m = /^line:(\d+)$/.exec(a)) && L()[+m[1] - 1]) { bi = +m[1] - 1; v = L()[bi].y1 + 1.2; }
      if (v == null) return;
      if (fStop) fStop(); const root = fRoot;
      fStop = tween(fP, v, 2200, x => { fP = x; setP(root, x); });
      band(fRoot, bi);
    },
    filmStop(){ if (fStop) fStop(); fRoot = null; }
  };
})();

/* --- 시간 따라 보기: 같은 자리의 여러 때를 시간 막대로 --- */
MODS.timeline = (() => {
  let el, cfg, pos = [], cur = -1, v = 0, stopT = null, fRoot = null, fv = 0, fStop = null;
  const st = () => { const s = modState('timeline'); s.seen = s.seen || []; return s; };
  const S_ = () => cfg.stops || [];
  function layout(){
    const S = S_(), n = S.length;
    const at = S.map((s, i) => { const x = s.at != null ? +s.at : parseFloat(String(s.y).replace(/[^0-9.\-]/g, '')); return isFinite(x) ? x : i; });
    const a0 = at[0], span = (at[n - 1] - a0) || 1;
    pos = at.map((x, i) => n > 1 ? 5 + 90 * (.6 * (x - a0) / span + .4 * i / (n - 1)) : 50);
  }
  function frame(root, val){
    const S = S_(); let i = 0;
    while (i < S.length - 2 && val > pos[i + 1]) i++;
    const t = S.length > 1 ? clamp((val - pos[i]) / ((pos[i + 1] - pos[i]) || 1), 0, 1) : 0;
    root.querySelectorAll('.tm-img').forEach((im, k) => { im.style.opacity = k === i ? Math.min(1, 2 * (1 - t)) : (k === i + 1 ? Math.min(1, 2 * t) : 0); im.style.zIndex = k === i + 1 ? 2 : 1; });
    const near = t < .5 ? i : Math.min(i + 1, S.length - 1);
    const kn = root.querySelector('.tm-knob'); if (kn) kn.style.left = val + '%';
    const fill = root.querySelector('.tm-fill'); if (fill) fill.style.width = val + '%';
    const yr = root.querySelector('.tm-year'); if (yr) yr.textContent = S[near].y;
    root.querySelectorAll('.tm-tick').forEach((b, k) => b.classList.toggle('on', k === near));
    return near;
  }
  function show(i){
    const s = S_()[i], S = st();
    if (!S.seen.includes(i)) { S.seen.push(i); save(); }
    el.querySelector('.tm-info').innerHTML = `<b>${esc(s.y)} · ${esc(s.t)}</b><p>${s.p || ''}</p>`;
    el.querySelectorAll('.tm-c').forEach(c => c.hidden = +c.dataset.i !== i);
    el.querySelectorAll('.tm-tick').forEach((b, k) => b.classList.toggle('seen', S.seen.includes(k)));
    count();
  }
  function count(){
    const n = st().seen.length, N = S_().length;
    el.querySelector('.tm-n').textContent = `지나온 때 ${n} / ${N}`;
    if (n >= N) { el.querySelector('.tm-done').hidden = false; mark('timeline'); }
  }
  function set(val){ v = clamp(val, pos[0], pos[pos.length - 1]); const k = frame(el, v); el.querySelector('.tm-range').value = Math.round(v * 10); if (k !== cur) { cur = k; show(k); } }
  function go(i){ if (stopT) stopT(); stopT = tween(v, pos[i], reduceMotion() ? 1 : 1300, set); }
  MODS_STATUS.timeline = () => cfg ? (P.ev.timeline ? `${S_().length}개의 때를 다 지나왔어요` : `지나온 때 ${st().seen.length} / ${S_().length}`) : '';
  return {
    init(e, c){
      el = e; cfg = c; layout();
      el.querySelectorAll('.tm-tick').forEach((b, k) => { b.style.left = pos[k] + '%'; b.onclick = () => go(k); });
      const r = el.querySelector('.tm-range');
      r.addEventListener('input', () => { if (stopT) stopT(); set(r.value / 10); });
      r.addEventListener('change', () => { let k = 0; pos.forEach((x, j) => { if (Math.abs(x - v) < Math.abs(pos[k] - v)) k = j; }); go(k); });
      r.addEventListener('keydown', ev => { if (ev.key === 'ArrowRight' || ev.key === 'ArrowUp') { ev.preventDefault(); go(Math.min(S_().length - 1, cur + 1)); } else if (ev.key === 'ArrowLeft' || ev.key === 'ArrowDown') { ev.preventDefault(); go(Math.max(0, cur - 1)); } });
      v = pos[0]; set(v);
    },
    film(layer, s){
      const im = S_()[0].img, b = fitBox(layer, im.w, im.h);
      layer.innerHTML = `<div class="tm tm-f" style="width:${b.w}px;height:${b.h}px"><div class="tm-stage">${S_().map((x, k) => `<img class="tm-img" src="${x.img.u}" alt="${esc(x.img.alt)}" style="opacity:${k ? 0 : 1}">`).join('')}<span class="tm-year">${esc(S_()[0].y)}</span></div></div>`;
      fRoot = layer.querySelector('.tm'); fv = pos[0]; frame(fRoot, fv);
    },
    act(a){
      if (!fRoot) return; let m, to = null;
      if (a === 'go') { const k = pos.findIndex(x => x > fv + .5); to = k < 0 ? pos[pos.length - 1] : pos[k]; }
      else if (a === 'all') to = pos[pos.length - 1];
      else if ((m = /^stop:(\d+)$/.exec(a)) && pos[+m[1] - 1] != null) to = pos[+m[1] - 1];
      if (to == null) return;
      if (fStop) fStop(); const root = fRoot;
      fStop = tween(fv, to, a === 'all' ? 6000 : 2600, x => { fv = x; frame(root, x); });
    },
    filmStop(){ if (fStop) fStop(); fRoot = null; }
  };
})();

/* --- 만드는 차례: 단추를 누를 때마다 한 단계씩 --- */
MODS.steps = (() => {
  let el, cfg, k = 0, fRoot = null, fk = 0;
  const N = () => (cfg.steps || []).length;
  function apply(root, n){   // n: 끝낸 단계 수(0~N)
    root.querySelectorAll('[data-s]').forEach(g => g.classList.toggle('on', +g.dataset.s <= n));
    root.querySelectorAll('[data-off]').forEach(g => g.classList.toggle('gone', +g.dataset.off <= n));
    const ims = [...root.querySelectorAll('.sp-img')]; let best = null;
    ims.forEach(im => { const i = +im.dataset.i; if (i <= n && (!best || i > +best.dataset.i)) best = im; });
    ims.forEach(im => im.classList.toggle('on', im === best));
    root.querySelectorAll('.sp-dots li').forEach((d, j) => { d.classList.toggle('done', j < n); d.classList.toggle('next', j === n); });
  }
  function draw(){
    apply(el, k);
    const btn = el.querySelector('.sp-do');
    if (k < N()) { btn.hidden = false; btn.textContent = cfg.steps[k].do; } else btn.hidden = true;
    el.querySelector('.sp-back').hidden = k === 0;
    el.querySelector('.sp-n').textContent = `${k} / ${N()} 단계`;
    if (k > 0) { const s = cfg.steps[k - 1]; el.querySelector('.sp-info').innerHTML = `<b>${k}. ${esc(s.t)}</b><p>${s.p || ''}</p>`; }
    else el.querySelector('.sp-info').innerHTML = `<p>${esc(cfg.hint || '아래 단추를 눌러 첫 단계부터 해 보세요.')}</p>`;
    el.querySelector('.sp-done').hidden = k < N();
    if (k >= N()) mark('steps');
  }
  MODS_STATUS.steps = () => cfg ? (P.ev.steps ? `${N()}단계를 끝까지 해 봤어요` : `‘${cfg.steps[0].do}’부터 차례로 해 보세요`) : '';
  return {
    init(e, c){
      el = e; cfg = c; k = 0;
      el.querySelector('.sp-do').onclick = () => { if (k < N()) { k++; draw(); } };
      el.querySelector('.sp-back').onclick = () => { k = 0; draw(); };
      draw();
    },
    film(layer, s){
      layer.innerHTML = `<div class="sp sp-f">${el.querySelector('.sp-stage').outerHTML}</div>`;
      fRoot = layer.querySelector('.sp'); fk = 0; apply(fRoot, 0);
    },
    act(a){
      if (!fRoot) return; let m;
      if (a === 'next') fk = Math.min(N(), fk + 1);
      else if (a === 'all') fk = N();
      else if ((m = /^step:(\d+)$/.exec(a))) fk = clamp(+m[1], 0, N());
      else return;
      apply(fRoot, fk);
    },
    filmStop(){ fRoot = null; }
  };
})();

/* --- 날짜 따라 여는 달력: 그날이 되어야 열리는 창 --- */
MODS.doors = (() => {
  let el, cfg, sim = null, simOpen = [], fRoot = null, fTimers = [];
  const st = () => { const s = modState('doors'); s.open = s.open || {}; s.visits = s.visits || []; return s; };
  const D = () => cfg.doors || [];
  const LAST = () => Math.max(...D().map(x => x.d));
  const MON = () => (cfg.month || 12) - 1;
  function now(){ if (sim) { const t = new Date(); return new Date(t.getFullYear(), MON(), sim); } return new Date(); }
  function upto(){   // 오늘 열 수 있는 마지막 날
    const n = now();
    if (n.getMonth() === MON()) return Math.min(n.getDate(), LAST()) ;
    if (sim) return 0;
    return Math.min(LAST(), Math.max(1, st().visits.length));   // 그 달이 아니면 찾아온 날마다 한 칸씩
  }
  const isOpen = d => sim ? simOpen.includes(d) : !!st().open[d];
  function paint(){
    const u = upto();
    el.querySelectorAll('.dr-door').forEach(b => {
      const d = +b.dataset.d, o = isOpen(d);
      b.classList.toggle('open', o); b.classList.toggle('ok', !o && d <= u); b.classList.toggle('lock', !o && d > u);
      b.setAttribute('aria-label', `${d}일 창${o ? ' · 열림' : (d > u ? ' · 아직 잠김' : ' · 열 수 있어요')}`);
    });
    const n = now(), inM = n.getMonth() === MON();
    el.querySelector('.dr-say').textContent = sim ? `미리 보기 · ${mdK(n)}: ${u}일까지의 창을 열 수 있어요(미리 보기로 연 창은 남지 않아요)`
      : inM ? `오늘은 ${mdK(n)} · ${u}일까지의 창을 열 수 있어요`
      : `지금은 ${(cfg.month || 12)}월이 아니라서, 찾아온 날마다 한 칸씩 열려요 · 오늘까지 ${u}칸`;
    const S = st(), days = new Set(Object.values(S.open)).size, N = D().length, opened = Object.keys(S.open).length;
    el.querySelector('.dr-n').textContent = `연 창 ${opened} / ${N} · 연 날 ${days}`;
    if (days >= (cfg.needDays || 3)) { el.querySelector('.dr-done').hidden = false; mark('doors'); }
  }
  function tell(d){
    const x = D().find(y => y.d === d) || {};
    el.querySelector('.dr-info').innerHTML = `<b>${d}일${x.t ? ' · ' + esc(x.t) : ''}</b><p>${x.p || ''}</p>`;
  }
  function open(d){
    const u = upto();
    if (isOpen(d)) { tell(d); return; }
    if (d > u) { el.querySelector('.dr-info').innerHTML = `<b>${d}일 창</b><p>${(cfg.month || 12)}월 ${d}일이 되면 열 수 있어요. 기다림도 이야기의 한 부분이에요.</p>`; return; }
    if (sim) simOpen.push(d); else { st().open[d] = ymd(new Date()); save(); }
    paint(); tell(d);
  }
  MODS_STATUS.doors = () => cfg ? (P.ev.doors ? `서로 다른 ${cfg.needDays || 3}날에 창을 열었어요` : `창을 연 날 ${new Set(Object.values(st().open)).size} / ${cfg.needDays || 3}`) : '';
  return {
    init(e, c){
      el = e; cfg = c;
      const S = st(), td = ymd(new Date()); if (!S.visits.includes(td)) { S.visits.push(td); save(); }
      el.querySelectorAll('.dr-door').forEach(b => b.onclick = () => open(+b.dataset.d));
      el.querySelectorAll('.dr-sim button').forEach(b => b.onclick = () => {
        sim = b.dataset.sim ? +b.dataset.sim : null; simOpen = [];
        el.querySelectorAll('.dr-sim button').forEach(x => x.classList.toggle('on', x === b)); paint();
        el.querySelector('.dr-info').innerHTML = `<p>${sim ? '미리 보기예요. 그날이 되었다고 치고 창을 열어 보세요.' : '오늘 날짜로 돌아왔어요.'}</p>`;
      });
      paint();
    },
    film(layer, s){
      const im = cfg.img, b = fitBox(layer, im.w, im.h), box = el.querySelector('.dr-box');
      layer.innerHTML = `<div class="dr dr-f" style="width:${b.w}px;height:${b.h}px">${box.outerHTML}</div>`;
      fRoot = layer.querySelector('.dr');
      fRoot.querySelectorAll('.dr-door').forEach(x => { x.classList.remove('open', 'ok', 'lock'); x.tabIndex = -1; });
    },
    act(a){
      if (!fRoot) return; let m;
      const openF = d => { const x = fRoot && fRoot.querySelector(`.dr-door[data-d="${d}"]`); if (x) x.classList.add('open'); };
      if ((m = /^open:(\d+)$/.exec(a))) openF(+m[1]);
      else if ((m = /^upto:(\d+)$/.exec(a)) || a === 'all') { const n = m ? +m[1] : LAST(); for (let d = 1; d <= n; d++) fTimers.push(setTimeout(() => openF(d), (d - 1) * 140)); }
    },
    filmStop(){ fTimers.forEach(clearTimeout); fTimers = []; fRoot = null; }
  };
})();

/* --- 흩어진 조각 모으기: 여러 곳에 나뉜 것을 한자리에 --- */
MODS.gather = (() => {
  let el, cfg, fRoot = null, fGot = [], ros = [];
  const st = () => { const s = modState('gather'); s.got = s.got || []; return s; };
  const PC = () => cfg.pieces || [];
  function auto(root, i){
    const r = root.querySelector('.ga-stage').getBoundingClientRect(), n = PC().length, wide = r.width >= r.height * 1.15;
    if (wide) { const half = Math.ceil(n / 2), left = i < half, k = left ? i : i - half, m = left ? half : n - half; return [left ? 14 : 86, m > 1 ? 24 + 52 * k / (m - 1) : 50]; }
    const cols = Math.min(n, 2), row = Math.floor(i / cols), rows = Math.ceil(n / cols);
    return [cols > 1 ? (i % cols ? 73 : 27) : 50, rows > 1 ? 64 + 22 * row / (rows - 1) : 76];
  }
  function place(root, got){
    const stage = root.querySelector('.ga-stage'), hm = root.querySelector('.ga-home');
    const sr = stage.getBoundingClientRect(), hr = hm.getBoundingClientRect();
    if (!sr.width || !hr.width) return;
    const hx = hr.left - sr.left, hy = hr.top - sr.top, hw = hr.width, hh = hr.height;
    root.querySelectorAll('.ga-piece').forEach(pc => {
      const i = +pc.dataset.i, P2 = PC()[i], [x, y, w, h] = P2.r, W = hw * w / 100, H = hh * h / 100;
      pc.style.width = W + 'px'; pc.style.height = H + 'px';
      if (got.includes(i)) { pc.style.left = (hx + hw * x / 100) + 'px'; pc.style.top = (hy + hh * y / 100) + 'px'; pc.style.transform = 'none'; pc.classList.add('home'); }
      else {
        const tall = sr.width < sr.height * 1.15, [ax, ay] = P2.at || auto(root, i), s = Math.min(1, (sr.width * .24) / W, (sr.height * (tall ? .17 : .3)) / H);
        pc.style.setProperty('--s', s.toFixed(3));
        pc.style.left = (sr.width * ax / 100 - W / 2) + 'px'; pc.style.top = (sr.height * ay / 100 - H / 2) + 'px';
        pc.style.transform = `rotate(${P2.rot != null ? P2.rot : (i % 2 ? 6 : -6)}deg) scale(${s.toFixed(3)})`; pc.classList.remove('home');
      }
    });
    root.classList.toggle('whole', got.length >= PC().length);
  }
  function tell(i){ const p = PC()[i]; el.querySelector('.ga-info').innerHTML = `<b>${esc(p.t)}</b><p>${p.p || ''}</p>`; }
  function count(){
    const n = st().got.length, N = PC().length;
    el.querySelector('.ga-n').textContent = `모은 조각 ${n} / ${N}`;
    if (n >= N) { el.querySelector('.ga-done').hidden = false; mark('gather'); }
  }
  MODS_STATUS.gather = () => cfg ? (P.ev.gather ? '흩어진 조각을 다 모았어요' : `모은 조각 ${st().got.length} / ${PC().length}`) : '';
  return {
    init(e, c){
      el = e; cfg = c;
      el.querySelectorAll('.ga-piece').forEach(pc => pc.onclick = () => {
        const i = +pc.dataset.i, S = st();
        if (!S.got.includes(i)) { S.got.push(i); save(); place(el, S.got); count(); }
        tell(i);
      });
      el.querySelector('.ga-again').onclick = () => { st().got = []; save(); place(el, []); el.querySelector('.ga-done').hidden = true; count(); el.querySelector('.ga-info').innerHTML = `<p>${esc(cfg.hint || '조각을 하나씩 눌러 보세요.')}</p>`; };
      const ro = new ResizeObserver(() => place(el, st().got)); ro.observe(el.querySelector('.ga-stage')); ros.push(ro);
      place(el, st().got); count();
    },
    film(layer, s){
      const src = el.querySelector('.ga-stage');
      layer.innerHTML = `<div class="ga ga-f">${src.outerHTML}</div>`;
      fRoot = layer.querySelector('.ga'); fGot = [];
      fRoot.querySelectorAll('.ga-piece').forEach(pc => pc.tabIndex = -1);
      requestAnimationFrame(() => fRoot && place(fRoot, fGot));
    },
    act(a){
      if (!fRoot) return; let m;
      if ((m = /^piece:(\d+)$/.exec(a))) { const i = +m[1] - 1; if (!fGot.includes(i)) fGot.push(i); }
      else if (a === 'all') fGot = PC().map((_, i) => i);
      else return;
      place(fRoot, fGot);
    },
    filmStop(){ fRoot = null; }
  };
})();

/* --- 따라 쓰기: 흐린 선을 손가락으로 따라 긋기 --- */
MODS.trace = (() => {
  let el, cfg, cur = 0, cov = [], pts = [], drawing = false, last = null, cv = null, ctx = null, fRoot = null, fTimers = [];
  const st = () => { const s = modState('trace'); s.done = s.done || []; return s; };
  const ST = () => cfg.glyph.strokes;
  const vb = () => cfg.glyph.vb.split(/[ ,]+/).map(Number);
  function samples(path){ const n = 40, Lp = path.getTotalLength(), a = []; for (let i = 0; i <= n; i++) { const q = path.getPointAtLength(Lp * i / n); a.push([q.x, q.y]); } return a; }
  function svgPt(svg, ev){ const p = svg.createSVGPoint(); p.x = ev.clientX; p.y = ev.clientY; return p.matrixTransform(svg.getScreenCTM().inverse()); }
  function ink(root, i, ms){
    const k = root.querySelector(`.tr-k[data-i="${i}"]`); if (!k) return;
    const Lk = k.getTotalLength(); k.style.transition = 'none'; k.style.strokeDasharray = Lk; k.style.strokeDashoffset = Lk; k.classList.add('on');
    k.getBoundingClientRect(); k.style.transition = `stroke-dashoffset ${ms}ms ease`; k.style.strokeDashoffset = 0;
  }
  function size(){ const r = el.querySelector('.tr-pad').getBoundingClientRect(), dpr = Math.min(2, window.devicePixelRatio || 1); cv.width = Math.round(r.width * dpr); cv.height = Math.round(r.height * dpr); ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
  function clearPad(){ if (ctx) ctx.clearRect(0, 0, cv.width, cv.height); }
  function next(){ const S = st(); const i = ST().findIndex((_, k) => !S.done.includes(k)); return i; }
  function guide(){
    const S = st();
    el.querySelectorAll('.tr-g').forEach((g, j) => { g.classList.toggle('cur', j === cur); g.classList.toggle('done', S.done.includes(j)); });
    const dot = el.querySelector('.tr-dot');
    if (cur < 0) { dot.style.display = 'none'; return; }
    const g = el.querySelector(`.tr-g[data-i="${cur}"]`), q = g.getPointAtLength(0); dot.style.display = ''; dot.setAttribute('cx', q.x); dot.setAttribute('cy', q.y);
    pts = samples(g); cov = pts.map(() => false);
  }
  function tell(i){ const s = ST()[i]; el.querySelector('.tr-info').innerHTML = `<b>${i + 1}. ${esc(s.t)}</b><p>${s.p || ''}</p>`; }
  function count(){
    const n = st().done.length, N = ST().length;
    el.querySelector('.tr-n').textContent = `쓴 획 ${n} / ${N}`;
    if (n >= N) { el.querySelector('.tr-done').hidden = false; mark('trace'); }
  }
  function finish(i, ms){
    const S = st(); if (!S.done.includes(i)) { S.done.push(i); save(); }
    ink(el, i, ms || 500); clearPad(); tell(i); cur = next(); guide(); count();
  }
  function move(ev){
    if (!drawing || cur < 0) return;
    const r = cv.getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top;
    if (last) { ctx.strokeStyle = 'rgba(160,60,30,.55)'; ctx.lineWidth = Math.max(5, r.width / 40); ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(last[0], last[1]); ctx.lineTo(x, y); ctx.stroke(); }
    last = [x, y];
    const q = svgPt(el.querySelector('.tr-svg'), ev), tol = vb()[2] * .085;
    pts.forEach((p, j) => { if (!cov[j] && Math.hypot(p[0] - q.x, p[1] - q.y) < tol) cov[j] = true; });
    const k = cov.filter(Boolean).length / cov.length;
    if (k >= .82 && cov[0] && cov[cov.length - 1]) { drawing = false; last = null; finish(cur); }
  }
  MODS_STATUS.trace = () => cfg ? (P.ev.trace ? `${cfg.glyph.name || '글자'}를 끝까지 써 봤어요` : `쓴 획 ${st().done.length} / ${ST().length}`) : '';
  return {
    init(e, c){
      el = e; cfg = c; cv = el.querySelector('.tr-cv'); size(); new ResizeObserver(size).observe(el.querySelector('.tr-pad'));
      const S = st(); S.done.forEach(i => { const k = el.querySelector(`.tr-k[data-i="${i}"]`); if (k) k.classList.add('on'); });
      cur = next(); guide(); count();
      const pad = el.querySelector('.tr-pad');
      pad.addEventListener('pointerdown', ev => { if (cur < 0) return; drawing = true; last = null; pad.setPointerCapture(ev.pointerId); move(ev); });
      pad.addEventListener('pointermove', move);
      const end = () => { drawing = false; last = null; if (cur >= 0 && cov.filter(Boolean).length / cov.length < .82) setTimeout(() => { if (!drawing) clearPad(); }, 900); };
      pad.addEventListener('pointerup', end); pad.addEventListener('pointercancel', end);
      el.querySelector('.tr-show').onclick = () => { const rest = ST().map((_, i) => i).filter(i => !st().done.includes(i)); rest.forEach((i, n) => setTimeout(() => { cur = i; finish(i, 900); }, n * 1000)); };
      el.querySelector('.tr-clear').onclick = () => { st().done = []; save(); el.querySelectorAll('.tr-k').forEach(k => { k.classList.remove('on'); k.style.transition = 'none'; }); clearPad(); el.querySelector('.tr-done').hidden = true; cur = next(); guide(); count(); el.querySelector('.tr-info').innerHTML = `<p>${esc(cfg.hint || '빨간 점에서 시작해 흐린 선을 따라 그어 보세요.')}</p>`; };
    },
    film(layer, s){
      const svg = el.querySelector('.tr-svg').cloneNode(true);
      svg.querySelectorAll('.tr-k').forEach(k => { k.classList.remove('on'); k.style.transition = 'none'; k.style.strokeDasharray = ''; k.style.strokeDashoffset = ''; });
      svg.querySelectorAll('.tr-g').forEach(g => g.classList.remove('cur', 'done'));
      const d = svg.querySelector('.tr-dot'); if (d) d.remove();
      layer.innerHTML = '<div class="tr tr-f"><div class="tr-pad"></div></div>'; layer.querySelector('.tr-pad').appendChild(svg);
      fRoot = layer.querySelector('.tr');
    },
    act(a){
      if (!fRoot) return; let m;
      if ((m = /^stroke:(\d+)$/.exec(a))) ink(fRoot, +m[1] - 1, 1400);
      else if (a === 'all') ST().forEach((_, i) => fTimers.push(setTimeout(() => fRoot && ink(fRoot, i, 1100), i * 1200)));
    },
    filmStop(){ fTimers.forEach(clearTimeout); fTimers = []; fRoot = null; }
  };
})();

/* ===== 틀 고침(키트 3판) — 이미 만든 카드에도 공유 파일로 바로 반영돼요 ===== */
/* 첫머리 ‘천천히 읽기 ↓’: 옛 틀은 #sc-road(시나이 카드의 첫 장면)로 고정돼 있었어요 → 이 카드의 첫 장면으로 */
(() => { try {
  const a = document.querySelector('a.btn[href="#sc-road"]');
  if (a && !document.getElementById('sc-road')) { const f = document.querySelector('section[id^="sc-"]'); if (f) a.setAttribute('href', '#' + f.id); }
} catch (x) {} })();
/* 앞면 카드: 그림이 가로로 길거나 정사각형이면 카드가 납작해져 ‘이야기 펼치기’ 단추가 제목·물음을 가려요 → 4:5 세로 틀로(그림은 가운데를 보여 줘요) */
(() => { try {
  const r = document.documentElement, v = getComputedStyle(r).getPropertyValue('--card-ar').trim(), m = /^([\d.]+)\s*\/\s*([\d.]+)$/.exec(v);
  if (m && +m[1] > +m[2] * 0.8) r.style.setProperty('--card-ar', '4 / 5');
} catch (x) {} })();

initMods();
drawStage(false); drawStamp(false); check(); hold($('#lcHold'));
