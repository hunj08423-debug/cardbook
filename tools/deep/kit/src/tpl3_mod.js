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
    el.querySelector('.rv-n').textContent = N ? `찾은 표시 ${S.found.length} / ${N}` : '';
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
      el.querySelector('.rv-all').onclick = () => { fillAll(o); box.classList.add('full'); const S = st(); S.full = true; save(); el.querySelectorAll('.rv-tag').forEach(t => t.classList.add('on', 'tap')); done(); };
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
