# -*- coding: utf-8 -*-
"""깊은 카드: 크리스마스 캐럴(read-carol) · 중심 방식 = 놓아 보기
기준서 1판(보탬 11) · 틀 deep3-4 · 키트 3판 보탬 · 2026-11-18 창 3(묶음 16)이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 책 속 성탄 날, 현재의 유령과 함께 선 크래칫네 부엌 — 크래칫 부인이 불붙인 푸딩을 들고 들어오고, 밥의 건배 끝에 꼬마 팀이 맨 마지막으로 “하나님, 우리 모두에게 복을 주세요!” 하는 순간
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 3장에 적힌 차례대로 크래칫네 식구들이 성탄 식탁을 차려요(식탁보 → 거위 → 감자와 사과 소스 → 푸딩 → 난롯불과 군밤 → 잔 셋)
카드 크기: 큰 카드 — 손 원고(모건 도서관 66쪽, 한 쪽씩 옮겨 적은 글), 1843년 초판의 리치 판화, 포스터의 전기가 넉넉해요.
그림 원본(src)은 deep_src/read-carol/ (저장소 밖). 무대 그림은 이 안내서가 그렸어요(스크립트로 만든 SVG를 아래 STAGE에 넣음)."""
S = 'read-carol/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

MS = 'https://www.themorgan.org/collections/works/dickens/ChristmasCarol/'   # 모건 도서관: 손 원고 쪽마다(쪽 번호 + 3)
MSREC = 'https://www.themorgan.org/literary-historical/160509'
FORSTER = 'https://archive.org/details/lifeofcharlesdic01forsuoft'
LIT = 'https://etc.usf.edu/lit2go/160/a-christmas-carol/'
GLA = 'https://www.gla.ac.uk/myglasgow/library/files/special/exhibns/month/dec1999.html'
EH = 'https://www.english-heritage.org.uk/visit/inspire-me/blog/blog-posts/how-did-queen-victoria-and-prince-albert-popularise-christmas/'
CAM = 'https://specialcollections-blog.lib.cam.ac.uk/?p=13677'
LAST = '그리하여 꼬마 팀이 말한 대로, 하나님, 우리 모두에게 복을 주세요!'

STAGE = r'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="이 안내서가 그린 크래칫네 부엌. 꺼진 난로와 눈 오는 창 사이에 빈 식탁이 있고, 놓은 것들이 식탁과 난로에 하나씩 나타난다."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#17110e"/><stop offset="1" stop-color="#2a1f18"/></linearGradient>
<linearGradient id="__U__win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b2436"/><stop offset="1" stop-color="#34445f"/></linearGradient>
<linearGradient id="__U__win2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c1220"/><stop offset="1" stop-color="#1f2a40"/></linearGradient>
<radialGradient id="__U__warm" cx=".55" cy=".66" r=".6"><stop offset="0" stop-color="#ffcf8a" stop-opacity=".55"/><stop offset=".5" stop-color="#d9893c" stop-opacity=".22"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__fire" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd27a" stop-opacity=".85"/><stop offset=".35" stop-color="#ff9a3c" stop-opacity=".42"/><stop offset="1" stop-color="#ff7a1c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".42" cy=".68" r=".8"><stop offset="0" stop-color="#ffe7b8" stop-opacity=".5"/><stop offset=".55" stop-color="#ffb866" stop-opacity=".22"/><stop offset="1" stop-color="#ff9f4a" stop-opacity="0"/></radialGradient>
<linearGradient id="__U__goose" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d79a52"/><stop offset=".55" stop-color="#a8642a"/><stop offset="1" stop-color="#6e3d17"/></linearGradient>
<radialGradient id="__U__pud" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="#6a3f22"/><stop offset="1" stop-color="#2c170b"/></radialGradient>
</defs>
<rect width="800" height="450" fill="url(#__U__wall)"/>
<rect y="296" width="800" height="6" fill="#33261d"/>
<g><line x1="20" y1="300" x2="20" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="84" y1="300" x2="84" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="148" y1="300" x2="148" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="212" y1="300" x2="212" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="276" y1="300" x2="276" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="340" y1="300" x2="340" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="404" y1="300" x2="404" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="468" y1="300" x2="468" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="532" y1="300" x2="532" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="596" y1="300" x2="596" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="660" y1="300" x2="660" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="724" y1="300" x2="724" y2="368" stroke="#2c211a" stroke-width="2"/><line x1="788" y1="300" x2="788" y2="368" stroke="#2c211a" stroke-width="2"/></g>
<rect y="368" width="800" height="82" fill="#140e0b"/>
<g><line x1="0" y1="384" x2="800" y2="384" stroke="#211812" stroke-width="1.4"/><line x1="0" y1="404" x2="800" y2="404" stroke="#211812" stroke-width="1.4"/><line x1="0" y1="428" x2="800" y2="428" stroke="#211812" stroke-width="1.4"/></g>
<!-- 난로 -->
<rect x="112" y="150" width="216" height="16" rx="2" fill="#4b3728" stroke="#6e5138" stroke-width="1.5"/>
<path d="M124 166 L316 166 L316 370 L124 370Z" fill="#33261d" stroke="#5c4330" stroke-width="1.5"/>
<path d="M154 370 L154 236 C 154 208 182 196 220 196 C 258 196 286 208 286 236 L286 370Z" fill="#0b0807"/>
<g stroke="#4a4642" stroke-width="3" stroke-linecap="round"><line x1="170" y1="318" x2="270" y2="318"/><line x1="170" y1="330" x2="270" y2="330"/><line x1="170" y1="342" x2="270" y2="342"/></g>
<g stroke="#4a4642" stroke-width="2.4"><line x1="178" y1="312" x2="178" y2="350"/><line x1="220" y1="312" x2="220" y2="350"/><line x1="262" y1="312" x2="262" y2="350"/></g>
<path d="M170 350 L270 350 L276 362 L164 362Z" fill="#2a2522"/>
<g opacity=".9"><ellipse cx="220" cy="314" rx="44" ry="6" fill="#3a140a"/><circle cx="204" cy="313" r="3" fill="#8a2a12"/><circle cx="222" cy="312" r="3.4" fill="#a8361a"/><circle cx="238" cy="314" r="2.8" fill="#7a2410"/></g>
<!-- 창 -->
<rect x="562" y="108" width="116" height="142" fill="#3b2b20"/>
<rect x="570" y="116" width="100" height="126" fill="url(#__U__win)"/>
<g><circle cx="610" cy="149" r="1.8" fill="#e9eef6" opacity="0.71"/><circle cx="631" cy="209" r="1.8" fill="#e9eef6" opacity="0.65"/><circle cx="599" cy="227" r="1.1" fill="#e9eef6" opacity="0.48"/><circle cx="578" cy="217" r="1.1" fill="#e9eef6" opacity="0.76"/><circle cx="657" cy="150" r="1.1" fill="#e9eef6" opacity="0.73"/><circle cx="666" cy="193" r="1.8" fill="#e9eef6" opacity="0.35"/><circle cx="638" cy="205" r="1.8" fill="#e9eef6" opacity="0.39"/><circle cx="589" cy="144" r="1.4" fill="#e9eef6" opacity="0.75"/><circle cx="619" cy="171" r="1.8" fill="#e9eef6" opacity="0.37"/><circle cx="580" cy="181" r="1.4" fill="#e9eef6" opacity="0.78"/><circle cx="652" cy="229" r="1.1" fill="#e9eef6" opacity="0.45"/><circle cx="642" cy="220" r="1.4" fill="#e9eef6" opacity="0.53"/><circle cx="648" cy="185" r="1.8" fill="#e9eef6" opacity="0.67"/><circle cx="597" cy="124" r="1.4" fill="#e9eef6" opacity="0.63"/><circle cx="585" cy="170" r="1.4" fill="#e9eef6" opacity="0.52"/><circle cx="646" cy="153" r="1.8" fill="#e9eef6" opacity="0.75"/><circle cx="655" cy="141" r="1.1" fill="#e9eef6" opacity="0.78"/><circle cx="635" cy="146" r="1.1" fill="#e9eef6" opacity="0.50"/><circle cx="617" cy="156" r="1.1" fill="#e9eef6" opacity="0.61"/><circle cx="589" cy="219" r="1.8" fill="#e9eef6" opacity="0.47"/><circle cx="653" cy="191" r="1.1" fill="#e9eef6" opacity="0.70"/><circle cx="627" cy="201" r="1.8" fill="#e9eef6" opacity="0.41"/><circle cx="646" cy="136" r="1.4" fill="#e9eef6" opacity="0.66"/><circle cx="648" cy="211" r="1.1" fill="#e9eef6" opacity="0.38"/><circle cx="595" cy="140" r="1.1" fill="#e9eef6" opacity="0.48"/><circle cx="631" cy="126" r="1.8" fill="#e9eef6" opacity="0.41"/></g>
<rect class="sky2" x="570" y="116" width="100" height="126" fill="url(#__U__win2)"/>
<g class="sky2"><circle cx="661" cy="221" r="2.4" fill="#f4f7fb" opacity="0.88"/><circle cx="625" cy="185" r="2.0" fill="#f4f7fb" opacity="0.63"/><circle cx="617" cy="199" r="1.6" fill="#f4f7fb" opacity="0.70"/><circle cx="666" cy="154" r="2.0" fill="#f4f7fb" opacity="0.57"/><circle cx="577" cy="156" r="2.0" fill="#f4f7fb" opacity="0.75"/><circle cx="596" cy="211" r="2.4" fill="#f4f7fb" opacity="0.91"/><circle cx="580" cy="177" r="2.4" fill="#f4f7fb" opacity="0.81"/><circle cx="645" cy="166" r="2.0" fill="#f4f7fb" opacity="0.81"/><circle cx="610" cy="227" r="1.6" fill="#f4f7fb" opacity="0.84"/><circle cx="587" cy="149" r="2.4" fill="#f4f7fb" opacity="0.77"/><circle cx="665" cy="138" r="1.6" fill="#f4f7fb" opacity="0.90"/><circle cx="612" cy="220" r="2.4" fill="#f4f7fb" opacity="0.86"/><circle cx="603" cy="194" r="2.0" fill="#f4f7fb" opacity="0.59"/><circle cx="655" cy="171" r="2.0" fill="#f4f7fb" opacity="0.70"/><circle cx="585" cy="134" r="2.4" fill="#f4f7fb" opacity="0.87"/><circle cx="629" cy="156" r="2.4" fill="#f4f7fb" opacity="0.63"/><circle cx="617" cy="199" r="2.0" fill="#f4f7fb" opacity="0.61"/><circle cx="581" cy="193" r="2.0" fill="#f4f7fb" opacity="0.94"/><circle cx="657" cy="178" r="2.0" fill="#f4f7fb" opacity="0.73"/><circle cx="632" cy="195" r="1.6" fill="#f4f7fb" opacity="0.62"/><circle cx="619" cy="177" r="2.0" fill="#f4f7fb" opacity="0.83"/><circle cx="633" cy="220" r="2.4" fill="#f4f7fb" opacity="0.89"/><circle cx="657" cy="176" r="2.0" fill="#f4f7fb" opacity="0.90"/><circle cx="606" cy="192" r="2.0" fill="#f4f7fb" opacity="0.87"/><circle cx="646" cy="189" r="1.6" fill="#f4f7fb" opacity="0.68"/><circle cx="595" cy="147" r="2.0" fill="#f4f7fb" opacity="0.66"/><circle cx="645" cy="126" r="1.6" fill="#f4f7fb" opacity="0.75"/><circle cx="639" cy="127" r="1.6" fill="#f4f7fb" opacity="0.76"/><circle cx="583" cy="219" r="2.0" fill="#f4f7fb" opacity="0.71"/><circle cx="615" cy="136" r="2.4" fill="#f4f7fb" opacity="0.86"/><circle cx="614" cy="128" r="2.0" fill="#f4f7fb" opacity="0.79"/><circle cx="656" cy="143" r="1.6" fill="#f4f7fb" opacity="0.78"/><circle cx="587" cy="169" r="2.0" fill="#f4f7fb" opacity="0.57"/><circle cx="620" cy="201" r="2.4" fill="#f4f7fb" opacity="0.82"/></g>
<path d="M620 116 L620 242 M570 179 L670 179" stroke="#3b2b20" stroke-width="5"/>
<rect x="556" y="248" width="128" height="8" fill="#4b3728"/>
<!-- 꼬마 팀의 작은 의자와 목발 -->
<g fill="#3e2c20" stroke="#7a5a36" stroke-width="1.2"><rect x="288" y="366" width="46" height="7" rx="2"/></g>
<g stroke="#3e2c20" stroke-width="5" stroke-linecap="round"><line x1="294" y1="373" x2="290" y2="404"/><line x1="328" y1="373" x2="332" y2="404"/></g>
<g stroke="#7a5a36" stroke-width="1" fill="none"><line x1="294" y1="373" x2="290" y2="404"/><line x1="328" y1="373" x2="332" y2="404"/></g>
<g stroke="#6e5034" stroke-width="3.6" stroke-linecap="round" fill="none"><path d="M318 290 L344 400"/><path d="M309 292 L327 288"/></g>
<!-- 식탁 -->
<path d="M368 300 L676 300 L698 326 L346 326Z" fill="#3a281c" stroke="#7a5a36" stroke-width="1.6"/>
<rect x="346" y="326" width="352" height="10" fill="#2e2016" stroke="#6a4c2e" stroke-width="1.2"/>
<g stroke="#2e2016" stroke-width="9" stroke-linecap="round"><line x1="362" y1="336" x2="358" y2="398"/><line x1="682" y1="336" x2="686" y2="398"/><line x1="414" y1="330" x2="412" y2="384"/><line x1="630" y1="330" x2="632" y2="384"/></g>
<path class="glow" d="M0 0 H800 V450 H0Z" fill="url(#__U__warm)" opacity=".14"/>
<!-- 1 식탁보 -->
<g class="obj" data-o="cloth"><path d="M366 297 L678 297 L702 325 L342 325Z" fill="#ece4d2" stroke="#c9bea4" stroke-width="1.2"/>
<path d="M342 325 L702 325 L696 352 C 650 346 610 356 570 349 C 530 344 490 355 450 348 C 410 343 380 354 348 350Z" fill="#e2d9c3" stroke="#c4b89c" stroke-width="1.2"/>
<path d="M388 328 L386 350 M456 328 L454 348 M530 328 L530 349 M604 328 L606 350 M672 328 L676 349" stroke="#cdbf9f" stroke-width="1.1"/></g>
<!-- 6 잔 셋과 주전자(식탁 왼쪽 끝, 난로 쪽) -->
<g class="obj" data-o="glass"><path d="M376 300 L374 276 C 372 266 380 260 388 260 C 396 260 402 266 400 276 L398 300Z" fill="#8a5a34" stroke="#4a2c14" stroke-width="1.2"/>
<path d="M374 266 L366 260 L378 262Z" fill="#8a5a34" stroke="#4a2c14" stroke-width="1"/><path d="M400 270 C 412 270 412 290 399 291" stroke="#4a2c14" stroke-width="3.2" fill="none"/>
<path d="M406 280 L424 280 L421 304 L409 304Z" fill="rgba(220,235,245,.18)" stroke="#dce8ef" stroke-width="1.2"/><path d="M407 290 L423 290 L421 304 L409 304Z" fill="#c98a3a" opacity=".8"/>
<path d="M428 282 L446 282 L443 304 L431 304Z" fill="rgba(220,235,245,.18)" stroke="#dce8ef" stroke-width="1.2"/><path d="M429 291 L445 291 L443 304 L431 304Z" fill="#c98a3a" opacity=".8"/>
<path d="M450 294 C 450 307 468 307 468 294Z" fill="#ece3cf" stroke="#a99d83" stroke-width="1.1"/><ellipse cx="459" cy="294" rx="9" ry="2.4" fill="#c98a3a" opacity=".85"/></g>
<!-- 2 거위 -->
<g class="obj" data-o="goose"><ellipse cx="532" cy="305" rx="60" ry="10.5" fill="#d9d1bd" stroke="#a99d83" stroke-width="1.2"/>
<path d="M484 299 C 484 275 508 261 536 262 C 566 263 584 279 582 297 C 572 305 500 307 484 299Z" fill="url(#__U__goose)" stroke="#5a3112" stroke-width="1.3"/>
<path d="M504 275 C 520 267 550 267 566 279" stroke="#e8b678" stroke-width="2.2" fill="none" opacity=".7" stroke-linecap="round"/>
<path d="M578 289 C 590 283 598 285 600 291 C 597 296 588 297 580 296" fill="#b9773a" stroke="#5a3112" stroke-width="1.1"/><circle cx="601" cy="292" r="3.2" fill="#efe6d2" stroke="#8a7a60" stroke-width=".8"/>
<path d="M490 293 C 478 289 472 292 472 297 C 476 301 484 301 490 299" fill="#b9773a" stroke="#5a3112" stroke-width="1.1"/><circle cx="470" cy="297" r="3.2" fill="#efe6d2" stroke="#8a7a60" stroke-width=".8"/></g>
<!-- 4 불붙인 푸딩과 호랑가시(식탁 오른쪽 안) -->
<g class="obj" data-o="pudding"><ellipse cx="634" cy="292" rx="32" ry="7" fill="#d9d1bd" stroke="#a99d83" stroke-width="1.1"/>
<path d="M608 268 C 608 250 620 242 634 242 C 650 242 660 252 660 270 C 660 285 650 292 634 292 C 618 292 608 285 608 268Z" fill="url(#__U__pud)" stroke="#1d0f06" stroke-width="1.2"/>
<circle cx="631.9" cy="269.2" r="1.9" fill="#1a0e07" opacity=".85"/><circle cx="632.3" cy="260.6" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="637.9" cy="261.8" r="1.2" fill="#1a0e07" opacity=".85"/><circle cx="621.2" cy="267.5" r="1.2" fill="#1a0e07" opacity=".85"/><circle cx="640.6" cy="256.4" r="1.9" fill="#1a0e07" opacity=".85"/><circle cx="643.7" cy="260.1" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="625.0" cy="266.8" r="1.9" fill="#1a0e07" opacity=".85"/><circle cx="626.2" cy="259.3" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="647.9" cy="259.8" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="633.0" cy="272.6" r="1.2" fill="#1a0e07" opacity=".85"/><circle cx="627.8" cy="258.7" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="625.2" cy="268.5" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="650.3" cy="269.7" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="634.3" cy="256.3" r="1.9" fill="#1a0e07" opacity=".85"/><circle cx="639.3" cy="258.9" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="645.1" cy="258.9" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="647.8" cy="273.9" r="1.2" fill="#1a0e07" opacity=".85"/><circle cx="619.8" cy="276.1" r="1.9" fill="#1a0e07" opacity=".85"/><circle cx="637.9" cy="269.7" r="1.2" fill="#1a0e07" opacity=".85"/><circle cx="629.5" cy="268.4" r="1.2" fill="#1a0e07" opacity=".85"/><circle cx="618.6" cy="262.2" r="1.9" fill="#1a0e07" opacity=".85"/><circle cx="633.4" cy="279.4" r="1.9" fill="#1a0e07" opacity=".85"/><circle cx="640.9" cy="258.5" r="1.2" fill="#1a0e07" opacity=".85"/><circle cx="636.8" cy="258.2" r="1.2" fill="#1a0e07" opacity=".85"/><circle cx="634.5" cy="268.4" r="1.5" fill="#1a0e07" opacity=".85"/><circle cx="643.4" cy="257.2" r="1.2" fill="#1a0e07" opacity=".85"/><circle cx="623.1" cy="268.8" r="1.1" fill="#7a4a26" opacity=".8"/><circle cx="635.6" cy="260.9" r="1.1" fill="#7a4a26" opacity=".8"/><circle cx="634.9" cy="278.9" r="1.1" fill="#7a4a26" opacity=".8"/><circle cx="627.4" cy="274.5" r="1.1" fill="#7a4a26" opacity=".8"/><circle cx="634.0" cy="266.4" r="1.1" fill="#7a4a26" opacity=".8"/><circle cx="625.6" cy="266.3" r="1.1" fill="#7a4a26" opacity=".8"/><circle cx="645.0" cy="268.3" r="1.1" fill="#7a4a26" opacity=".8"/><circle cx="644.2" cy="277.6" r="1.1" fill="#7a4a26" opacity=".8"/><circle cx="625.0" cy="261.0" r="1.1" fill="#7a4a26" opacity=".8"/><circle cx="626.7" cy="269.5" r="1.1" fill="#7a4a26" opacity=".8"/>
<g opacity=".78"><path d="M612 276 C 602 264 612 254 610 244 C 618 252 620 262 618 272Z" fill="#7fb2ff"/><path d="M656 276 C 666 264 658 252 662 242 C 652 252 650 264 652 274Z" fill="#7fb2ff"/>
<path d="M624 252 C 620 240 628 234 626 224 C 634 234 634 244 632 252Z" fill="#ffc46b"/><path d="M644 252 C 648 240 640 234 644 226 C 636 234 636 244 638 252Z" fill="#ffc46b"/></g>
<path d="M634 242 C 624 232 614 236 610 230 C 622 228 630 232 634 242Z" fill="#2f6b3a" stroke="#1c4424" stroke-width=".8"/>
<path d="M634 242 C 644 232 654 236 658 230 C 646 228 638 232 634 242Z" fill="#2f6b3a" stroke="#1c4424" stroke-width=".8"/>
<circle cx="631" cy="239" r="3" fill="#c62f2f"/><circle cx="637" cy="238" r="3" fill="#d43a35"/><circle cx="634" cy="234" r="2.8" fill="#b92a2a"/></g>
<!-- 3 감자 · 끓인 소스 · 사과 소스(앞줄) -->
<g class="obj" data-o="sides"><path d="M408 314 C 408 329 452 329 452 314Z" fill="#cfc7b3" stroke="#9a8f77" stroke-width="1.2"/>
<path d="M411 314 C 415 301 430 297 438 302 C 446 299 451 307 448 314Z" fill="#f2e8c8" stroke="#cdbf95" stroke-width="1"/>
<path d="M466 318 C 468 310 494 310 498 314 C 506 312 512 308 514 306 C 512 314 506 322 496 324 C 484 326 468 325 466 318Z" fill="#d8d0bc" stroke="#9a8f77" stroke-width="1.1"/>
<ellipse cx="482" cy="314" rx="12" ry="3" fill="#6b3d1c"/>
<path d="M612 316 C 612 331 658 331 658 316Z" fill="#c4bca7" stroke="#958a72" stroke-width="1.2"/>
<ellipse cx="635" cy="316" rx="23" ry="5" fill="#d6b45e" stroke="#a8893f" stroke-width="1"/></g>
<!-- 5 난롯불 · 군밤 · 사과와 오렌지(.lt 무리가 차례로 켜져요) -->
<g class="lt"><circle cx="220" cy="300" r="190" fill="url(#__U__fire)" opacity=".7"/></g>
<g class="lt"><path d="M182 318 C 180 296 196 290 194 272 C 206 286 208 300 204 318Z" fill="#ff9b3d"/><path d="M204 318 C 200 290 220 280 216 256 C 232 276 236 298 230 318Z" fill="#ffb347"/><path d="M228 318 C 228 296 244 290 242 270 C 254 286 258 302 252 318Z" fill="#ff9b3d"/>
<path d="M196 318 C 196 304 206 300 205 290 C 212 300 214 310 211 318Z" fill="#ffe08a"/><path d="M220 318 C 218 300 230 294 228 280 C 238 294 238 308 234 318Z" fill="#ffe08a"/></g>
<g class="lt"><path d="M222 324 L262 316 L300 286" stroke="#5a5650" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M222 316 L262 308 L264 322 L224 330Z" fill="#4a4642"/><ellipse cx="233" cy="318" rx="5.2" ry="4.2" fill="#6e3b1c" stroke="#2a150a" stroke-width=".8"/><ellipse cx="243" cy="316" rx="5.2" ry="4.2" fill="#6e3b1c" stroke="#2a150a" stroke-width=".8"/><ellipse cx="252" cy="319" rx="5.2" ry="4.2" fill="#6e3b1c" stroke="#2a150a" stroke-width=".8"/><ellipse cx="238" cy="312" rx="5.2" ry="4.2" fill="#6e3b1c" stroke="#2a150a" stroke-width=".8"/><ellipse cx="248" cy="311" rx="5.2" ry="4.2" fill="#6e3b1c" stroke="#2a150a" stroke-width=".8"/></g>
<g class="lt"><ellipse cx="566" cy="322" rx="26" ry="5" fill="#cfc7b3" stroke="#9a8f77" stroke-width="1"/><circle cx="554" cy="315" r="7.5" fill="#b8352a" stroke="#6d1c15" stroke-width=".8"/><circle cx="568" cy="314" r="7.5" fill="#e08a2c" stroke="#8a4f12" stroke-width=".8"/><circle cx="580" cy="316" r="7" fill="#c0402e" stroke="#6d1c15" stroke-width=".8"/><circle cx="562" cy="308" r="6.5" fill="#e9952f" stroke="#8a4f12" stroke-width=".8"/></g>
<rect class="day" width="800" height="450" fill="url(#__U__day)"/>
</svg>'''

ITEMS = [
 {'id': 'cloth', 't': '식탁보', 'la': 'the cloth', 'say': '크래칫 부인이 식탁보를 깔고, 둘째 딸 벨린다가 거들어요. 부인은 두 번이나 뒤집어 고쳐 지은 옷을 입고, 값싼 리본으로 한껏 멋을 냈어요.'},
 {'id': 'goose', 't': '거위', 'la': 'the goose', 'say': '피터와 꼬마 둘이 거위를 받아 왔어요. 아까 빵집 앞에서 냄새만 맡고도 ‘우리 거위다!’ 하고 알아본 그 거위예요.'},
 {'id': 'sides', 't': '감자와 사과 소스', 'la': 'apple-sauce', 'say': '부인은 소스를 지글지글 데우고, 피터는 감자를 힘껏 으깨고, 벨린다는 사과 소스에 단맛을 내요. 맏딸 마사는 데운 접시를 닦아요.'},
 {'id': 'pudding', 't': '불붙인 푸딩', 'la': 'the pudding', 'say': '부인이 혼자 나가 푸딩을 들고 들어와요. 얼굴이 발그레한 채 자랑스럽게 웃으며요. 얼룩무늬 대포알처럼 단단한 푸딩이 브랜디 불꽃에 싸여 타오르고, 꼭대기에는 호랑가시나무가 꽂혀 있어요.'},
 {'id': 'lights', 't': '난롯불과 군밤', 'la': 'chestnuts on the fire', 'say': '식탁을 치우고 난로를 쓸고 불을 돋워요. 사과와 오렌지를 식탁에 올리고, 군밤 한 삽을 불 위에 얹어요. 식구들은 난로 둘레에 둘러앉아요. 밥은 ‘동그랗게’라고 했지만, 사실은 반원이에요.'},
 {'id': 'glass', 't': '잔 셋', 'la': 'the family display of glass', 'say': '밥 곁에 이 집의 잔이 모두 나왔어요. 유리잔 둘, 손잡이 없는 커스터드 컵 하나. 주전자의 따뜻한 음료를 담으니 금잔 못지않아요.'},
]

CARD = {
 'id': 'read-carol', 'mode': '놓아 보기',
 'pagetitle': '크래칫네 성탄 식탁',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>1843년 겨울</b><span>영국 런던 · 디킨스의 『크리스마스 캐럴』</span>',
 'lead': '1843년 겨울, 디킨스는 6주 만에 성탄 이야기 하나를 썼어요. 구두쇠 스크루지는 유령을 따라가 자기 서기 밥 크래칫의 작은 집을 들여다봐요. 책에 적힌 차례대로, 그 집 식구들이 차린 성탄 식탁을 하나씩 차려 보세요.',
 'leadKid': '아주 옛날 영국 이야기야. 욕심쟁이 스크루지 할아버지가 유령이랑 같이 가난한 밥 아저씨네 집을 몰래 들여다봤대. 우리도 그 집 성탄 식탁을 차려 볼까?',
 'meta': '영화처럼 약 4분 · 천천히 읽으면 6분',
 'draft': '검수 전 시안이에요(기준서 1판 보탬 11). 소설 속 장면은 디킨스의 손 원고(모건 도서관이 쪽마다 옮겨 적은 글)와 책의 글을 따랐고, 쓰던 때의 일은 친구 포스터의 전기와 도서관 자료를 따랐어요. 책 속 대사는 이 안내서가 우리말로 옮겼고, 부엌 무대는 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 4분',
 'theme': """:root{--accent:#7b3f1d;--accent-ink:#fff8f2;--soft:rgba(123,63,29,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#e0a46a;--accent-ink:#1d1207;--soft:rgba(224,164,106,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#e0a46a;--accent-ink:#1d1207;--soft:rgba(224,164,106,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '캐럴', 'y': '1843', 'sub': '런던 · 디킨스'},
 'doneNote': '성탄 저녁, 식구들과 이 책의 3장을 소리 내어 읽어 보세요. 마지막 한마디는 막내에게 맡기고요.',
 'images': {
  'ms': {'src': S + 'A_Christmas_Carol_Manuscript.jpg', 'cap': '디킨스의 손 원고, 2장이 시작되는 17쪽 · 뉴욕 모건 도서관',
         'cr': '사진: Jack1956 · CC0 · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:A_Christmas_Carol_Manuscript.jpg',
         'alt': '전시장 유리 아래 펼쳐 놓은 손 원고. 오른쪽 쪽은 맨 위 제목 아래로 잉크 손글씨가 빽빽하고, 줄마다 긋고 고쳐 쓴 자국이 가득하다. 왼쪽 쪽에는 뒷장 글씨가 비쳐 보이고, 아래쪽에 고리 모양으로 지운 줄들이 거꾸로 보인다.'},
  'marley': {'src': S + 'Marley_s_Ghost-John_Leech_1843.jpg', 'cap': '「말리의 유령」 · 1843년 초판에 실린, 손으로 색칠한 판화',
             'cr': '그림: 존 리치 · 퍼블릭 도메인 · 위키미디어 공용', 'u': "https://commons.wikimedia.org/wiki/File:Marley%27s_Ghost-John_Leech,_1843.jpg",
             'alt': '벽난로 곁 분홍 안락의자에 흰 잠옷과 수면 모자 차림의 노인이 앉아, 손을 들고 몸을 움츠린다. 난로 둘레에는 작은 그림 타일이 붙어 있고, 작은 탁자 위에 그릇과 숟가락, 파랗게 타는 촛불이 있다. 오른쪽에는 머리와 턱을 천으로 동여맨 잿빛 유령이 서 있고, 몸에 감긴 사슬 끝의 자물쇠와 상자들이 바닥까지 끌린다.'},
  'last': {'src': S + 'The_Last_of_the_Spirits-John_Leech_1843.jpg', 'cap': '「마지막 유령」 · 1843년 초판에 실린, 손으로 색칠한 판화',
           'cr': '그림: 존 리치 · 퍼블릭 도메인 · 위키미디어 공용', 'u': 'https://commons.wikimedia.org/wiki/File:The_Last_of_the_Spirits-John_Leech,_1843.jpg',
           'alt': '어두운 교회 묘지. 왼쪽에 검은 천을 머리까지 덮어쓴 키 큰 형체가 손을 내밀어 아래를 가리키고, 오른쪽에 잠옷 차림의 노인이 무릎을 꿇고 두 손으로 얼굴을 감싼다. 둘 사이 풀숲 땅에 ‘EBENEZER SCROOGE’라고 새긴 묘비가 누워 있다.'},
 },
 'extra_credits': [{'cr': '크래칫네 부엌 무대: 이 안내서가 그린 그림 · 『크리스마스 캐럴』 3장(디킨스 손 원고 36~40쪽)을 바탕으로', 'u': MS + '39'}],
 'scenes': [
  {'id': 'ms', 'label': '여섯 주의 원고', 'kind': 'photo', 'img': 'ms',
   'text': ['1843년 10월, 서른한 살의 찰스 디킨스는 맨체스터에 다녀온 지 일주일쯤 지나 이 이야기를 쓰기 시작했어요. 그리고 11월이 다 가기 전에 끝냈어요.',
            '친구 존 포스터는 디킨스가 이 이야기를 쓰며 울고 웃고 또 울었다고 적었어요. 사람들이 다 잠든 밤이면 이야기를 생각하며 런던의 어두운 거리를 24~32킬로미터씩 걸었대요.'],
   'text2': ['손 원고는 모두 66쪽이에요. 줄마다 긋고 고친 자국이 가득해요. 이 이야기의 하나뿐인 손 원고예요. 디킨스도 첫 장에 ‘이 책의, 나의 하나뿐인 원고’라고 적었어요.',
             '책은 12월 19일에 나왔어요. 디킨스는 원고를 붉은 가죽으로 묶어, 돈을 빌려준 오랜 친구 토머스 미턴에게 선물했어요.'],
   'kid': '디킨스 아저씨가 손으로 쓴 진짜 원고야. 줄을 긋고 고친 자국이 엄청 많지?',
   'kidq': '이야기를 쓰다가 고치고 또 고친 적 있어? 왜 고쳤어?'},
  {'id': 'marley', 'label': '쇠사슬을 끄는 유령', 'kind': 'photo', 'img': 'marley', 'night': True,
   'text': ['이야기는 성탄 전야에 시작해요. 춥고 매섭고 안개 낀 날, 스크루지의 사무실에서 서기 밥 크래칫은 석탄 한 덩이만 한 불 곁에서 일해요. 성탄 인사를 하러 온 조카에게 스크루지는 “흥, 허튼소리!” 하고 말해요.',
            '그날 밤, 감기에 걸린 스크루지는 작은 불 곁에 죽 냄비를 올려 두고 앉아 있어요. 그때 7년 전 바로 이날 밤에 세상을 떠난 동업자 말리의 유령이 들어와요. 머리와 턱을 천으로 동여매고, 돈궤와 열쇠, 자물쇠, 장부, 문서, 쇠로 만든 무거운 돈주머니를 엮은 사슬을 끌면서요.'],
   'quote': {'t': '나는 살면서 내가 만든 사슬을 차고 있네.', 'from': '『크리스마스 캐럴』 1장, 말리의 유령 · 이 안내서가 옮김', 'u': LIT + '2824/stave-i/'},
   'text2': ['말리는 사람들이 바로 자기 일이었어야 했다고 뉘우쳐요. 그리고 세 유령이 찾아올 거라고 말해요. 첫째 유령은 내일, 종이 한 번 울릴 때 와요.'],
   'kid': '스크루지 할아버지 앞에 쇠사슬을 칭칭 감은 유령이 나타났어! 옛 친구 말리 할아버지래.',
   'kidq': '말리 유령은 왜 무거운 사슬을 끌고 다닐까?'},
  {'id': 'table', 'label': '크래칫네 식탁', 'kind': 'mod', 'mod': 'place',
   'text': ['둘째 유령, 현재의 유령은 스크루지를 데리고 성탄 날 아침 거리로 나가요. 그리고 밥 크래칫의 집 문턱에서 횃불을 흩뿌려 그 집에 복을 빌어요. 밥은 일주일에 15실링을 받아요. 그래도 유령은 방 네 칸짜리 그 집에 복을 빌었어요.',
            '교회에서 돌아온 밥의 어깨에는 꼬마 팀이 타고 있어요. 팀은 작은 목발을 짚고, 다리는 쇠틀로 받치고 다녀요. 이제 식구들이 저마다 일을 맡아 성탄 식탁을 차려요. 아래 무대에 책에 적힌 차례대로 놓아 보세요.'],
   'text2': ['팀은 교회에서 사람들이 자기를 보았으면 했다고 아버지에게 말했대요. 성탄 날에, 다리를 저는 사람을 걷게 하고 눈먼 사람을 보게 하신 분을 떠올리면 사람들이 기쁠 것 같아서요(' + bl('MAT.11', '마태복음 11장 5절') + ').',
             '밥은 스크루지를 위해서도 잔을 들어요. “이 잔치를 차려 주신 스크루지 씨를 위하여!” 크래칫 부인은 얼굴을 붉혀요. 그래도 남편과 성탄 날을 위해 잔을 들어요. 그 사람을 위해서는 아니라면서요.'],
   'kid': '식탁보, 거위, 감자, 푸딩, 난롯불, 잔! 하나씩 차려 보자.',
   'kidq': '불붙은 푸딩이 들어오면, 너는 뭐라고 외칠 것 같아?'},
  {'id': 'last', 'label': '마지막 유령, 그리고 아침', 'kind': 'quote', 'img': 'last',
   'text': ['식탁 곁에서 스크루지는 꼬마 팀이 살 수 있겠느냐고 물어요. 유령은 가난한 난롯가에 빈자리 하나와, 주인 없이 고이 간직된 목발이 보인다고 대답해요.',
            '셋째 유령은 검은 옷으로 온몸을 덮고, 말없이 손으로 가리키기만 해요. 그 끝에서 스크루지는 돌보는 이 없는 무덤에 새겨진 자기 이름을 읽어요. 그는 무릎을 꿇고 말해요. 성탄을 마음에 모시고, 한 해 내내 지키겠다고요.',
            '눈을 뜨니 자기 침대, 바로 성탄 날 아침이었어요. 스크루지는 꼬마 팀보다 두 배나 큰 칠면조를 크래칫네로 보내고, 이튿날 밥의 봉급을 올려 줘요. 죽지 않은 꼬마 팀에게 그는 둘째 아버지가 되었어요.',
            '그리고 책은 이렇게 끝나요. 크래칫네 식탁에서 꼬마 팀이 맨 마지막에 했던 그 말이에요.'],
   'quote': {'t': LAST, 'from': '『크리스마스 캐럴』의 마지막 문장 · 디킨스 손 원고 66쪽 · 이 안내서가 옮김', 'u': MS + '69'},
   'kid': '마지막 유령은 아무 말도 없이 손으로만 가리켜. 스크루지 할아버지는 그 뒤로 완전히 달라졌대!',
   'kidq': '큰 칠면조가 도착했을 때, 꼬마 팀네 식구들은 어떤 얼굴이었을까?'},
 ],
 'imagine': {'t': '좁은 부엌에 김이 가득해요. 빨래하는 날 같은 냄새가 나더니, 음식점과 과자 가게가 나란히 붙은 듯한 냄새가 퍼져요. 파란 불꽃을 두른 푸딩이 들어오는 순간 모두 숨을 멈춰요. 난롯불에서 군밤이 탁탁 튀고, 창밖에는 눈이 내리기 시작해요.',
             'kid': '눈을 감아 봐. 부엌에 김이 모락모락, 푸딩에 파란 불이 활활. 난로에서 군밤이 탁탁 튀어!'},
 'lines': ['하나님, 우리 모두에게 복을 주세요!', '유리잔 둘과 손잡이 없는 컵 하나, 그래도 금잔 못지않게.', '석탄 한 덩이만 한 불에서, 군밤이 튀는 난롯불까지.', '성탄을 마음에 모시고, 한 해 내내.'],
 'linesKid': ['우리 모두에게 복을!', '푸딩에 불이 활활!', '스크루지 할아버지가 달라졌어.'],
 'close': {'form': '기록 한 마디',
           'from': '책의 마지막 문장 “And so, as Tiny Tim observed, God bless Us, Every One!” — 3장 크래칫네 식탁에서 꼬마 팀이 맨 마지막에 한 말이 책의 마지막 말이 돼요(디킨스 손 원고 39·66쪽)',
           'ask': '밥은 그 식탁에서 스크루지를 위해서도 잔을 들었어요. 꼬마 팀이 말한 ‘우리 모두’에, 나라면 누구까지 넣을 수 있을까요?',
           'askKid': '꼬마 팀은 ‘우리 모두에게 복을!’ 하고 말했어. 너라면 그 ‘모두’에 누구누구를 넣고 싶어?'},
 'goals': {
  's4': {'t': '책의 차례대로', 'p': '3장에 적힌 차례(식탁보부터 잔 셋까지)대로 크래칫네 식탁을 다 차리면 카드에 금박이 입혀져요.',
         'how': '책에 적힌 차례대로 크래칫네 식탁을 다 차려 보세요', 'done': '책의 차례대로 크래칫네 식탁을 차렸어요',
         'ways': [{'id': 'plOrder', 't': '식탁보 → 거위 → 감자와 사과 소스 → 불붙인 푸딩 → 난롯불과 군밤 → 잔 셋 차례로 놓기'}]},
  's5': {'t': '아이와 함께', 'p': '아이와 함께 ‘영화처럼 보기’를 끝까지 보면 카드가 채색돼요.', 'how': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'done': '아이와 함께 끝까지 봤어요',
         'ways': [{'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'place': {
   'items': ITEMS, 'order': '식탁보, 거위, 감자와 사과 소스, 불붙인 푸딩, 난롯불과 군밤, 잔 셋',
   'intro': '아래에서 하나를 골라 크래칫네 부엌에 놓아 보세요. 책에 적힌 차례는 식탁보부터예요.',
   'climax': '“얘들아, 우리 모두 즐거운 성탄! 하나님, 우리에게 복을 주세요!” 밥이 잔을 들자 온 식구가 따라 말했어요. 그리고 맨 마지막에 꼬마 팀이 말했어요. “하나님, 우리 모두에게 복을 주세요!”<span class="la">“God bless us every one!” said Tiny Tim, the last of all.<br>디킨스 손 원고 39쪽 · 이 안내서가 옮김</span>',
   'home': None,
   'wrongOrder': '책에 적힌 차례는 이래요: {order}',
   'orderDone': '책에 적힌 차례대로 다 차렸어요',
   'daylight': False,
   'svg': STAGE}},
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 차려 보기</button></div>
  <div class="pl-home" hidden><p></p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>노래 한 절, 한 절</b> 책의 온 제목은 『산문으로 쓴 크리스마스 캐럴: 성탄 유령 이야기』예요. 디킨스는 다섯 장을 ‘절’(stave, 노래의 한 절)이라고 불렀어요. 노래처럼 한 절씩 읽히는 이야기예요.',
    '<b>빵집 화덕</b> 그때 영국에는 집에 화덕이 없는 집이 많았어요. 그런 집은 성탄 날 거위를 동네 빵집에 맡겨 구웠어요. 3장에도 저녁거리를 들고 빵집으로 가는 사람들이 나와요. 유령은 그 사람들 위에도 횃불을 뿌려 줘요.',
    '<b>성경 그림 타일</b> 1장은 스크루지 방의 벽난로 둘레에 성경 이야기를 그린 옛 네덜란드 타일이 붙어 있었다고 적어요. 리치의 「말리의 유령」에도 난로 둘레에 작은 그림 타일이 보여요.',
    '<b>15실링</b> 실링은 그때 영국 돈의 단위예요. 20실링이 1파운드였어요. 밥은 일주일에 15실링을 받았어요.',
    '<b>책 한 권에 들인 정성</b> 디킨스는 책 만드는 일을 모두 직접 맡아, 존 리치에게 손으로 색칠한 판화 네 점과 목판화 네 점을 그리게 했어요. 책값은 5실링이었어요. 글래스고 대학 도서관은 이 값으로는 들인 돈만큼 이익이 나지 않았다고 적어요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>나온 날</b> 모건 도서관은 1843년 12월 19일, 글래스고 대학 도서관은 12월 17일이라고 적어요.',
    '<b>얼마나 빨리 팔렸나</b> 포스터의 전기는 첫 6,000부가 나온 첫날에 다 팔렸다고 적었고, 글래스고 대학 도서관은 성탄까지 다 팔렸다고 적어요.',
    '<b>마지막 문장</b> 손 원고에는 ‘God Bless Us Every One!’으로, 인쇄된 책에는 ‘God bless Us, Every One!’으로 적혀 있어요.',
    '<b>원고 쪽수</b> 모건 도서관의 해설은 66쪽짜리 원고라고 하고, 같은 목록의 묶음 설명에는 68쪽이라고 적어요.']},
  {'h': '원고와 그림을 직접 보기', 'checked': '2026년 11월 18일', 'p': [
    '뉴욕 모건 도서관은 이 손 원고를 누리집에서 한 쪽씩 넘겨 볼 수 있게 열어 두었어요. 쪽마다 옮겨 적은 글도 함께 있어요. 크래칫네 식탁은 36~40쪽이에요.',
    '모건 도서관은 해마다 성탄 무렵 이 원고를 펼쳐 전시하고, 해마다 한 쪽씩 넘겨요. 전시 때는 미리 확인해 주세요.'],
   'links': [{'t': '모건 도서관: 디킨스 손 원고를 한 쪽씩 넘겨 보기(옮겨 적은 글과 함께)', 'u': MS[:-1], 'm': '영어'},
             {'t': '케임브리지 대학 도서관: 『크리스마스 캐럴』 그림 150년(리치부터 래컴까지)', 'u': CAM, 'm': '영어'},
             {'t': '잉글리시 헤리티지: 빅토리아 시대 사람들의 성탄(거위와 빵집 화덕)', 'u': EH, 'm': '영어'}]},
 ],
 'src': [
  {'l': '모건 도서관 목록: 『크리스마스 캐럴』 손 원고(MA 97) — 6주 만에 씀, 66쪽, 하나뿐인 원고, 12월 19일 출간, 미턴에게 선물, 표제지의 ‘My own, and only, MS of the Book’', 'u': MSREC},
  {'l': '모건 도서관: 손 원고 쪽마다 옮겨 적은 글 — 36쪽(밥의 15실링·방 네 칸 집·식탁보·빵집 앞 거위 냄새)', 'u': MS + '39'},
  {'l': '모건 도서관: 손 원고 37쪽 — 교회에서 돌아온 밥과 팀(어깨 위·목발·쇠틀), 팀이 교회에서 한 바람, 주전자, 거위를 가지러 감', 'u': MS + '40'},
  {'l': '모건 도서관: 손 원고 38쪽 — 대포알 같은 푸딩, 브랜디 불꽃, 호랑가시나무', 'u': MS + '41'},
  {'l': '모건 도서관: 손 원고 39쪽 — 식탁 치우기, 사과·오렌지·군밤, 잔 셋, 밥의 건배와 팀의 말, 빈자리와 목발', 'u': MS + '42'},
  {'l': '모건 도서관: 손 원고 40쪽 — 크래칫 부인의 건배', 'u': MS + '43'},
  {'l': '모건 도서관: 손 원고 66쪽 — 책의 마지막 문장(손 원고의 글자 모양)', 'u': MS + '69'},
  {'l': '모건 도서관: 손 원고 17쪽 — 2장이 시작되는 쪽(사진 속 쪽)', 'u': MS + '20'},
  {'l': '모건 도서관 전시: 2025~26 『크리스마스 캐럴』 — 1843년 10월부터 6주, 붉은 가죽 제본, 해마다 한 쪽씩 넘김', 'u': 'https://www.themorgan.org/exhibitions/charles-dickenss-christmas-carol'},
  {'l': '존 포스터, 『찰스 디킨스의 생애』 1권(1872, 1876 판) 4부 1~2장 — 쓰기 시작한 때와 끝낸 때, 울고 웃으며 밤거리를 걸은 일, 첫날의 판매', 'u': FORSTER},
  {'l': 'Lit2Go(사우스플로리다 대학): 『크리스마스 캐럴』 1장 — 추운 날, 석탄 한 덩이 불, “Bah! Humbug!”, 7년 전 이날 밤, 말리의 사슬', 'u': LIT + '2824/stave-i/'},
  {'l': 'Lit2Go: 3장 — 크래칫네 식탁의 차례', 'u': LIT + '2826/stave-iii/'},
  {'l': 'Lit2Go: 4장 — 검은 옷의 유령, 무덤의 이름, 성탄을 한 해 내내 지키겠다는 말', 'u': LIT + '2828/stave-iv/'},
  {'l': 'Lit2Go: 5장 — 성탄 날 아침, 팀보다 두 배 큰 칠면조, 봉급, 둘째 아버지, 마지막 문장', 'u': LIT + '2829/stave-v/'},
  {'l': '글래스고 대학 도서관: 이달의 책(1999년 12월) — 12월 17일, 성탄까지 6,000부, 리치의 판화 여덟 점, 5실링', 'u': GLA},
  {'l': '잉글리시 헤리티지(샘 빌턴, 2025): 화덕이 없으면 거위를 빵집에 맡겨 구움', 'u': EH},
  {'l': '케임브리지 대학 도서관 특별 장서 블로그(2016): 『크리스마스 캐럴』 그림의 역사', 'u': CAM},
  {'l': '위키미디어 공용: 손 원고 사진 정보(CC0)', 'u': 'https://commons.wikimedia.org/wiki/File:A_Christmas_Carol_Manuscript.jpg'},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'ms', 'fit': 'cover', 'p0': '70% 40%', 'p1': '62% 55%', 's0': 1.3, 's1': 1.1, 'kicker': '1843년 겨울 · 영국 런던', 'title': '크리스마스 캐럴',
   'lines': [{'t': '1843년 겨울, 디킨스는 6주 만에 성탄 이야기 하나를 썼어요.'}, {'t': '구두쇠 스크루지가 유령을 따라가 들여다본 이야기예요.'}],
   'kid': [{'t': '아주 옛날 영국에서 쓴 이야기야.'}, {'t': '욕심쟁이 할아버지랑 유령이 나와!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '여섯 주'},
  {'type': 'img', 'ch': 1, 'img': 'ms', 'fit': 'cover', 'p0': '74% 30%', 'p1': '70% 70%', 's0': 1.6, 's1': 1.35, 'cap': '디킨스의 손 원고, 17쪽',
   'lines': [{'t': '10월에 쓰기 시작해, 11월이 가기 전에 끝냈어요. 하나뿐인 손 원고예요.'},
             {'t': '울고 웃고 또 울며 썼고, 밤이면 런던 거리를 24~32킬로미터씩 걸었대요.'}],
   'kid': [{'t': '디킨스 아저씨는 이 이야기를 쓰면서 울다가 웃다가 또 울었대.'}, {'t': '너는 이야기를 읽다가 울어 본 적 있어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '말리의 유령'},
  {'type': 'img', 'ch': 2, 'img': 'marley', 'fit': 'contain', 'p0': '50% 45%', 'p1': '50% 40%', 's0': 1.0, 's1': 1.1, 'cap': '「말리의 유령」, 1843년 초판',
   'lines': [{'t': '성탄 전야, 스크루지는 성탄 인사를 하러 온 조카에게 말해요. “흥, 허튼소리!”'},
             {'t': '그날 밤, 7년 전에 세상을 떠난 동업자 말리가 사슬을 끌고 찾아와요.'},
             {'t': '나는 살면서 내가 만든 사슬을 차고 있네.', 'q': True, 'from': '말리의 유령, 1장에서'}],
   'kid': [{'t': '쇠사슬을 칭칭 감은 유령이 나타났어!'}, {'t': '말리 유령은 왜 사슬을 끌고 다닐까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '크래칫네 식탁'},
  {'type': 'mod', 'mod': 'place', 'ch': 3,
   'lines': [{'t': '성탄 날, 유령은 스크루지를 밥 크래칫의 작은 집으로 데려가요.'},
             {'t': '식탁보를 깔고,', 'act': 'cloth'},
             {'t': '빵집에서 거위를 받아 오고,', 'act': 'goose'},
             {'t': '감자를 으깨고, 사과 소스에 단맛을 내요.', 'act': 'sides'},
             {'t': '부인이 불붙인 푸딩을 들고 들어와요. 꼭대기에는 호랑가시나무!', 'act': 'pudding', 'wait': 1500},
             {'t': '난롯불을 돋우고, 군밤 한 삽을 불 위에 얹어요.', 'act': 'lights', 'wait': 1200},
             {'t': '유리잔 둘과 손잡이 없는 컵 하나에 따뜻한 음료를 담아요.', 'act': 'glass'},
             {'t': '“얘들아, 우리 모두 즐거운 성탄! 하나님, 우리에게 복을 주세요!”', 'act': 'day', 'wait': 1200},
             {'t': '하나님, 우리 모두에게 복을 주세요!', 'q': True, 'from': '꼬마 팀, 맨 마지막에'}],
   'kid': [{'t': '꼬마 팀네 집이야. 하나씩 차려 보자!'},
           {'t': '식탁보!', 'act': 'cloth'}, {'t': '거위!', 'act': 'goose'}, {'t': '감자랑 사과 소스!', 'act': 'sides'},
           {'t': '푸딩에 불이 활활!', 'act': 'pudding', 'wait': 1500}, {'t': '난로에서 군밤이 탁탁!', 'act': 'lights', 'wait': 1200},
           {'t': '잔을 들고 다 같이!', 'act': 'glass'}, {'t': '“우리 모두에게 복을!”', 'act': 'day', 'wait': 1200},
           {'t': '너라면 누구랑 이 식탁에 앉고 싶어?', 'ask': True}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '마지막 유령'},
  {'type': 'img', 'ch': 4, 'img': 'last', 'fit': 'contain', 'p0': '50% 55%', 'p1': '52% 62%', 's0': 1.0, 's1': 1.12, 'cap': '「마지막 유령」, 1843년 초판',
   'lines': [{'t': '셋째 유령은 말없이 손으로 가리키기만 해요.'},
             {'t': '그 끝, 돌보는 이 없는 무덤에 스크루지의 이름이 새겨져 있어요.'},
             {'t': '성탄을 마음에 모시고, 한 해 내내 지키겠어요.', 'q': True, 'from': '스크루지, 4장에서'},
             {'t': '눈을 뜨니 성탄 날 아침. 스크루지는 크래칫네로 큰 칠면조를 보내요.'},
             {'t': '죽지 않은 꼬마 팀에게, 그는 둘째 아버지가 되었어요.'}],
   'kid': [{'t': '마지막 유령은 아무 말도 안 하고 손으로만 가리켜.'}, {'t': '스크루지 할아버지가 아침에 큰 칠면조를 보냈대!'},
           {'t': '칠면조가 도착했을 때 꼬마 팀은 뭐라고 했을까?', 'ask': True}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '좁은 부엌에 김이 가득해요.'}, {'t': '파란 불꽃을 두른 푸딩이 들어오는 순간, 모두 숨을 멈춰요.'}, {'t': '군밤이 탁탁 튀고, 창밖에는 눈이 내려요.'}],
   'kid': [{'t': '부엌에 김이 모락모락.'}, {'t': '푸딩에 파란 불이 활활, 군밤이 탁탁!'}]},
  {'type': 'quote', 'ch': 5, 'big': LAST,
   'lines': [{'t': '『크리스마스 캐럴』의 마지막 문장 · 크래칫네 식탁에서 꼬마 팀이 한 그 말', 'wait': 2600}],
   'kid': [{'t': '책의 맨 마지막 말도, 꼬마 팀이 식탁에서 한 그 말이래.', 'wait': 2600}]},
  {'type': 'reward', 'ch': 5},
 ],
}
