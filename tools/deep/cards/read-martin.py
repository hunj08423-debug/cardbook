# -*- coding: utf-8 -*-
"""깊은 카드: 구두장이 마르틴(read-martin) · 중심 방식 = 놓아 보기
기준서 2판 · 틀 deep3-4 · 키트 3판 · 2026-11-18 창 3(묶음 16)이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 그날 밤 등잔 아래 복음서를 펴자, 어두운 구석에서 “마르틴, 나를 모르겠느냐?” 하는 소리와 함께 그날 만난 사람들이 하나씩 나와 웃는 순간
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 그날 마르틴이 손님들에게 내준 것을 이야기의 차례대로 놓기(사모바르와 차 → 양배추 수프와 빵 → 낡은 외투 → 사과 하나 → 등잔과 복음서)
카드 크기: 한 장면 카드 — 자유롭게 쓸 그림은 앞면의 마코프스키 그림(이 이야기의 그림이 아님)뿐이라, 장면 2개로 하고 반지하 방 무대는 이 안내서가 그렸어요.
그림 원본: 앞면 그림(site/img/c). 무대는 아래 STAGE(이 안내서가 그린 SVG · /root/work/scripts/martin_stage.py로 만듦)."""
S = 'read-martin/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

CC = 'https://ccel.org/ccel/tolstoy/23_tales/23_tales.iv.iv.html'          # 모드 부부 영역 「Where Love Is, God Is」(1885)
RU = 'https://ru.wikisource.org/wiki/%D0%93%D0%B4%D0%B5_%D0%BB%D1%8E%D0%B1%D0%BE%D0%B2%D1%8C,_%D1%82%D0%B0%D0%BC_%D0%B8_%D0%91%D0%BE%D0%B3_(%D0%A2%D0%BE%D0%BB%D1%81%D1%82%D0%BE%D0%B9)'
WP = 'https://en.wikipedia.org/wiki/Where_Love_Is,_God_Is'
WPS = 'https://en.wikipedia.org/wiki/Ruben_Saillens'
SIZ = 'https://gramota.net/eng/materials/2/2019/8/10.html'
DOLE = 'https://www.marxists.org/archive/tolstoy/1887/where-love-is-there-god-is-also.html'
VOICE = '마르틴, 마르틴! 내일 거리를 내다보아라. 내가 가겠다.'
TOP = '내가 배고플 때 너희가 먹을 것을 주었고, 목마를 때 마실 것을 주었고, 나그네였을 때 맞아들였다.'

STAGE = r'''<svg class="stage" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" role="img" aria-label="이 안내서가 그린 구두장이 마르틴의 반지하 방. 높은 창으로 눈 덮인 길이 보이고, 그 아래 빈 식탁과 화덕이 있다. 놓은 것들이 식탁과 창밖에 하나씩 나타나고, 끝에는 창이 어두워지며 구석에 그날 만난 사람들이 빛으로 나타난다."><defs>
<linearGradient id="__U__wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#191512"/><stop offset="1" stop-color="#2b231d"/></linearGradient>
<linearGradient id="__U__corner" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#080605" stop-opacity=".9"/><stop offset="1" stop-color="#080605" stop-opacity="0"/></linearGradient>
<linearGradient id="__U__out" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7f8a97"/><stop offset="1" stop-color="#aeb7c1"/></linearGradient>
<linearGradient id="__U__night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070b16"/><stop offset="1" stop-color="#18223a"/></linearGradient>
<linearGradient id="__U__brass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7a5320"/><stop offset=".45" stop-color="#d9a64e"/><stop offset="1" stop-color="#6e4718"/></linearGradient>
<linearGradient id="__U__stove" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#bdb3a3"/><stop offset="1" stop-color="#8e8576"/></linearGradient>
<radialGradient id="__U__warm" cx=".6" cy=".66" r=".6"><stop offset="0" stop-color="#ffd08a" stop-opacity=".5"/><stop offset=".5" stop-color="#d98b3c" stop-opacity=".2"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__lamp" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffe1a0" stop-opacity=".9"/><stop offset=".3" stop-color="#ffbe62" stop-opacity=".4"/><stop offset="1" stop-color="#ff9a3c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__halo" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff0cf" stop-opacity=".32"/><stop offset="1" stop-color="#fff0cf" stop-opacity="0"/></radialGradient>
<linearGradient id="__U__gh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff3dc" stop-opacity=".52"/><stop offset="1" stop-color="#fff3dc" stop-opacity=".16"/></linearGradient>
<radialGradient id="__U__ember" cx=".5" cy=".7" r=".6"><stop offset="0" stop-color="#ff8a3c" stop-opacity=".55"/><stop offset="1" stop-color="#ff8a3c" stop-opacity="0"/></radialGradient>
</defs>
<rect width="800" height="450" fill="url(#__U__wall)"/>
<g><path d="M718 221 l3 -2" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M800 227 l-5 4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M714 102 l0 -3" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M371 104 l-17 0" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M379 170 l-8 -5" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M190 270 l-24 -4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M68 170 l-14 2" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M410 331 l-1 1" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M121 259 l-8 -0" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M25 218 l-25 -4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M562 344 l-16 5" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M731 152 l0 5" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M296 219 l-30 4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M721 138 l-26 -4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M160 270 l-6 -0" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M707 289 l14 -0" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M189 302 l-9 0" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M188 183 l8 -5" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M227 94 l-6 -1" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M769 24 l-25 1" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M761 159 l1 -1" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M748 267 l-27 -4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M750 68 l21 -5" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M737 60 l19 1" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M537 328 l-22 -4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M310 22 l26 5" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M408 172 l1 5" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M686 43 l-19 -4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M551 101 l24 -2" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M68 272 l8 -3" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M146 29 l-23 6" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M579 219 l-17 -0" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M27 87 l-23 6" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M262 155 l-12 4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M84 329 l-14 -2" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M77 228 l-4 -4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M314 267 l0 -0" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M633 185 l-23 2" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M105 13 l-2 -4" stroke="#d8cfc2" stroke-width="1" opacity=".05"/><path d="M234 316 l7 -2" stroke="#d8cfc2" stroke-width="1" opacity=".05"/></g>
<path d="M0 20 L800 20" stroke="#120e0b" stroke-width="10"/>
<rect y="372" width="800" height="78" fill="#120e0b"/>
<g><line x1="0" y1="388" x2="800" y2="388" stroke="#1b1511" stroke-width="1.4"/><line x1="0" y1="410" x2="800" y2="410" stroke="#1b1511" stroke-width="1.4"/><line x1="0" y1="434" x2="800" y2="434" stroke="#1b1511" stroke-width="1.4"/></g>
<!-- 문과 위로 난 계단(왼쪽 끝) -->
<path d="M18 372 L18 170 L92 170 L92 372Z" fill="#241b14" stroke="#4a3828" stroke-width="2"/>
<path d="M28 182 L82 182 L82 268 L28 268Z M28 278 L82 278 L82 362 L28 362Z" fill="none" stroke="#3a2c20" stroke-width="2"/>
<circle cx="80" cy="276" r="3" fill="#6a5a44"/>
<!-- 어두운 구석 -->
<rect x="96" y="20" width="200" height="352" fill="url(#__U__corner)"/>
<!-- 높은 창(바깥은 길과 같은 높이) -->
<rect x="284" y="28" width="232" height="132" fill="#120e0b"/>
<rect x="300" y="42" width="200" height="104" fill="url(#__U__out)"/>
<path d="M300 116 C 340 110 380 118 420 112 C 450 108 480 114 500 110 L500 146 L300 146Z" fill="#e8ecf0"/>
<g><circle cx="431" cy="53" r="1.3" fill="#f3f6fa" opacity="0.69"/><circle cx="363" cy="49" r="1.6" fill="#f3f6fa" opacity="0.54"/><circle cx="398" cy="63" r="1.0" fill="#f3f6fa" opacity="0.68"/><circle cx="427" cy="85" r="1.6" fill="#f3f6fa" opacity="0.66"/><circle cx="464" cy="99" r="1.3" fill="#f3f6fa" opacity="0.47"/><circle cx="412" cy="61" r="1.6" fill="#f3f6fa" opacity="0.46"/><circle cx="398" cy="68" r="1.6" fill="#f3f6fa" opacity="0.48"/><circle cx="414" cy="66" r="1.6" fill="#f3f6fa" opacity="0.71"/><circle cx="353" cy="66" r="1.3" fill="#f3f6fa" opacity="0.60"/><circle cx="473" cy="101" r="1.0" fill="#f3f6fa" opacity="0.69"/><circle cx="341" cy="61" r="1.6" fill="#f3f6fa" opacity="0.39"/><circle cx="417" cy="97" r="1.6" fill="#f3f6fa" opacity="0.75"/><circle cx="409" cy="64" r="1.6" fill="#f3f6fa" opacity="0.70"/><circle cx="421" cy="104" r="1.3" fill="#f3f6fa" opacity="0.39"/><circle cx="473" cy="96" r="1.0" fill="#f3f6fa" opacity="0.42"/><circle cx="491" cy="49" r="1.0" fill="#f3f6fa" opacity="0.50"/><circle cx="319" cy="59" r="1.0" fill="#f3f6fa" opacity="0.43"/><circle cx="311" cy="90" r="1.0" fill="#f3f6fa" opacity="0.47"/><circle cx="454" cy="103" r="1.0" fill="#f3f6fa" opacity="0.48"/><circle cx="389" cy="86" r="1.6" fill="#f3f6fa" opacity="0.66"/></g>
<!-- 창 아래 구두 골 -->
<g><path d="M300 178 L500 178" stroke="#4a3b2e" stroke-width="1.4"/><path d="M305 178 C 303 192 306 202 312 204 C 319 202 321 190 319 178Z" fill="#6b4a32" stroke="#2a2018" stroke-width="1"/><path d="M327 178 C 325 192 328 202 334 204 C 341 202 343 190 341 178Z" fill="#5a3d29" stroke="#2a2018" stroke-width="1"/><path d="M349 178 C 347 192 350 202 356 204 C 363 202 365 190 363 178Z" fill="#7a5a3c" stroke="#2a2018" stroke-width="1"/><path d="M371 178 C 369 192 372 202 378 204 C 385 202 387 190 385 178Z" fill="#6b4a32" stroke="#2a2018" stroke-width="1"/><path d="M393 178 C 391 192 394 202 400 204 C 407 202 409 190 407 178Z" fill="#5a3d29" stroke="#2a2018" stroke-width="1"/><path d="M415 178 C 413 192 416 202 422 204 C 429 202 431 190 429 178Z" fill="#7a5a3c" stroke="#2a2018" stroke-width="1"/><path d="M437 178 C 435 192 438 202 444 204 C 451 202 453 190 451 178Z" fill="#6b4a32" stroke="#2a2018" stroke-width="1"/><path d="M459 178 C 457 192 460 202 466 204 C 473 202 475 190 473 178Z" fill="#5a3d29" stroke="#2a2018" stroke-width="1"/><path d="M481 178 C 479 192 482 202 488 204 C 495 202 497 190 495 178Z" fill="#7a5a3c" stroke="#2a2018" stroke-width="1"/><path d="M310 218 L488 218" stroke="#4a3b2e" stroke-width="1.4"/><path d="M315 218 C 313 232 316 242 322 244 C 329 242 331 230 329 218Z" fill="#8a6a46" stroke="#2a2018" stroke-width="1"/><path d="M337 218 C 335 232 338 242 344 244 C 351 242 353 230 351 218Z" fill="#6b4a32" stroke="#2a2018" stroke-width="1"/><path d="M359 218 C 357 232 360 242 366 244 C 373 242 375 230 373 218Z" fill="#5c4330" stroke="#2a2018" stroke-width="1"/><path d="M381 218 C 379 232 382 242 388 244 C 395 242 397 230 395 218Z" fill="#8a6a46" stroke="#2a2018" stroke-width="1"/><path d="M403 218 C 401 232 404 242 410 244 C 417 242 419 230 417 218Z" fill="#6b4a32" stroke="#2a2018" stroke-width="1"/><path d="M425 218 C 423 232 426 242 432 244 C 439 242 441 230 439 218Z" fill="#5c4330" stroke="#2a2018" stroke-width="1"/><path d="M447 218 C 445 232 448 242 454 244 C 461 242 463 230 461 218Z" fill="#8a6a46" stroke="#2a2018" stroke-width="1"/><path d="M469 218 C 467 232 470 242 476 244 C 483 242 485 230 483 218Z" fill="#6b4a32" stroke="#2a2018" stroke-width="1"/></g>
<!-- 러시아식 화덕(오른쪽) -->
<path d="M612 372 L612 140 C 612 118 640 108 690 108 C 744 108 770 118 770 140 L770 372Z" fill="url(#__U__stove)" stroke="#6a6256" stroke-width="2"/>
<path d="M612 236 L770 236" stroke="#7a7264" stroke-width="2"/>
<path d="M650 330 L650 286 C 650 266 668 256 690 256 C 712 256 730 266 730 286 L730 330Z" fill="#1a1410" stroke="#5a5246" stroke-width="2"/>
<ellipse cx="690" cy="322" rx="34" ry="14" fill="url(#__U__ember)"/>
<path d="M672 318 C 672 304 708 304 708 318 L704 326 L676 326Z" fill="#2a2622" stroke="#4a4642" stroke-width="1.2"/>
<rect x="640" y="330" width="100" height="8" fill="#7a7264"/>
<!-- 화덕 곁 걸상 -->
<path d="M596 338 L668 338 L664 346 L600 346Z" fill="#4a3626" stroke="#6e523a" stroke-width="1.2"/>
<path d="M604 346 L602 372 M660 346 L662 372" stroke="#3a2a1c" stroke-width="6" stroke-linecap="round"/>
<!-- 식탁 -->
<path d="M352 292 L574 292 L594 330 L332 330Z" fill="#3e2c1e" stroke="#7a5a38" stroke-width="1.6"/>
<rect x="332" y="330" width="262" height="9" fill="#2e2016" stroke="#6a4c2e" stroke-width="1.2"/>
<path d="M346 339 L342 372 M580 339 L584 372" stroke="#2e2016" stroke-width="9" stroke-linecap="round"/>
<path class="glow" d="M0 0 H800 V450 H0Z" fill="url(#__U__warm)" opacity=".14"/>
<!-- 1 사모바르와 차 두 잔(하나는 엎어 놓고 설탕 한 조각) -->
<g class="obj" data-o="tea"><path d="M316 42 L354 42 L352 70 L318 70Z" fill="#4f463c"/>
<path d="M322 70 L330 70 L330 98 L322 98Z M338 70 L346 70 L346 98 L338 98Z" fill="#3f372f"/>
<g transform="translate(326 132) scale(0.9)"><path d="M-9 -40 L9 -40 L10 -12 L-10 -12Z" fill="#8b857a" stroke="#4d4842" stroke-width="1"/><path d="M-11 -14 L10 -14 C 14 -8 20 -6 21 0 L-12 0 C -13 -6 -12 -10 -11 -14Z" fill="#3a2a1e" stroke="#21160e" stroke-width="1"/><path d="M-6 -34 L-4 -20 M4 -36 L5 -22" stroke="#6f6a61" stroke-width="1" opacity=".7"/></g><g transform="translate(343 133) scale(0.9)"><path d="M-9 -40 L9 -40 L10 -12 L-10 -12Z" fill="#8b857a" stroke="#4d4842" stroke-width="1"/><path d="M-11 -14 L10 -14 C 14 -8 20 -6 21 0 L-12 0 C -13 -6 -12 -10 -11 -14Z" fill="#3a2a1e" stroke="#21160e" stroke-width="1"/><path d="M-6 -34 L-4 -20 M4 -36 L5 -22" stroke="#6f6a61" stroke-width="1" opacity=".7"/></g>
<path d="M386 42 L372 116" stroke="#6b4c2c" stroke-width="4" stroke-linecap="round"/>
<path d="M362 112 L384 112 L386 136 L364 140Z" fill="#8c9096" stroke="#4e5156" stroke-width="1.2"/><path d="M370 300 L398 300 L394 292 L374 292Z" fill="#6e4718"/>
<path d="M366 292 C 360 270 364 252 384 250 C 404 252 408 270 402 292Z" fill="url(#__U__brass)" stroke="#4a3010" stroke-width="1.2"/>
<path d="M376 250 L392 250 L390 240 L378 240Z" fill="#a8782e" stroke="#4a3010" stroke-width="1"/>
<path d="M372 238 L396 238" stroke="#8a6020" stroke-width="3"/>
<path d="M402 276 L414 278 L414 283" stroke="#8a6020" stroke-width="2.4" fill="none"/>
<path d="M362 262 C 354 262 354 272 362 274 M406 262 C 414 262 414 272 406 274" stroke="#7a5320" stroke-width="2" fill="none"/>
<path d="M422 300 L424 280 L438 280 L440 300Z" fill="rgba(220,235,245,.2)" stroke="#dce8ef" stroke-width="1.2"/>
<path d="M423 290 L439 290 L440 300 L422 300Z" fill="#b9782e" opacity=".85"/>
<path d="M448 300 L446 282 L462 282 L460 300Z" fill="rgba(220,235,245,.2)" stroke="#dce8ef" stroke-width="1.2"/>
<rect x="450" y="276" width="9" height="6" rx="1" fill="#f4efe4" stroke="#b9b0a0" stroke-width=".8"/></g>
<!-- 2 양배추 수프와 빵 -->
<g class="obj" data-o="soup"><path d="M418 42 L462 42 L470 92 L412 92Z" fill="#a7998a" opacity=".95"/>
<path d="M412 92 L470 92" stroke="#8a7c6d" stroke-width="2"/>
<g transform="translate(430 134) scale(0.92)"><path d="M-5 -38 L5 -38 L6 -9 L-6 -9Z" fill="#7d7060" stroke="#4a4036" stroke-width="1"/><path d="M-4 -30 L4 -30 M-4 -22 L5 -22" stroke="#9a8b78" stroke-width="1" opacity=".6"/><path d="M-8 -10 L6 -10 C 11 -6 16 -4 16 0 L-8 0 C -9 -4 -9 -7 -8 -10Z" fill="#2e2620" stroke="#17120e" stroke-width="1"/></g><g transform="translate(448 135) scale(0.92)"><path d="M-5 -38 L5 -38 L6 -9 L-6 -9Z" fill="#7d7060" stroke="#4a4036" stroke-width="1"/><path d="M-4 -30 L4 -30 M-4 -22 L5 -22" stroke="#9a8b78" stroke-width="1" opacity=".6"/><path d="M-8 -10 L6 -10 C 11 -6 16 -4 16 0 L-8 0 C -9 -4 -9 -7 -8 -10Z" fill="#2e2620" stroke="#17120e" stroke-width="1"/></g><path d="M474 296 C 474 312 516 312 516 296Z" fill="#7a5a3a" stroke="#3e2a18" stroke-width="1.2"/>
<ellipse cx="495" cy="296" rx="21" ry="5" fill="#b8a25a" stroke="#6e5a2a" stroke-width="1"/>
<path d="M486 294 l4 -2 M498 295 l5 -1 M492 297 l3 1" stroke="#6f8a3e" stroke-width="2" stroke-linecap="round"/>
<path d="M488 288 C 484 280 492 276 488 268 M500 288 C 496 280 504 276 500 266" stroke="#e8e0d0" stroke-width="1.4" fill="none" opacity=".45"/>
<path d="M522 302 C 520 288 536 282 548 286 C 560 290 562 300 556 304Z" fill="#9a6a36" stroke="#5a3a18" stroke-width="1.2"/>
<path d="M530 292 C 536 290 544 290 550 294" stroke="#c4935e" stroke-width="1.2" fill="none"/></g>
<!-- 3 낡은 외투(화덕 곁 걸상 위에 걸쳐 둠) -->
<g class="obj" data-o="coat"><path d="M598 334 C 606 326 624 322 634 324 C 646 322 664 326 670 334 L678 366 C 670 371 662 365 654 369 C 646 365 638 371 630 367 C 622 371 614 365 606 369 C 600 365 594 369 590 366Z" fill="#4e4434" stroke="#2a241a" stroke-width="1.3"/>
<path d="M610 338 L605 363 M626 336 L623 365 M644 336 L646 365 M661 338 L666 362" stroke="#352d22" stroke-width="1.4" fill="none"/>
<path d="M616 327 C 624 318 644 318 652 327 C 644 332 624 332 616 327Z" fill="#5e5240" stroke="#2a241a" stroke-width="1"/>
<path d="M598 338 C 590 346 588 360 592 371 L601 371 C 599 360 601 350 606 343Z" fill="#463c2e" stroke="#2a241a" stroke-width="1.1"/>
<rect x="633" y="344" width="13" height="10" fill="#6a5c46" stroke="#3a3226" stroke-width="1"/>
<path d="M635 346 L644 352 M644 346 L635 352" stroke="#3a3226" stroke-width=".8"/></g>
<!-- 4 사과 하나(식탁 앞 가장자리) -->
<g class="obj" data-o="apple"><path d="M462 122 L496 122 L492 142 L466 142Z" fill="#8a6234" stroke="#4e3519" stroke-width="1.2"/>
<path d="M462 122 C 466 108 492 108 496 122" fill="none" stroke="#6e4a22" stroke-width="2"/>
<circle cx="472" cy="121" r="5" fill="#b83a2a"/><circle cx="483" cy="120" r="5" fill="#c9502e"/>
<path d="M466 128 L492 128 M467 134 L491 134" stroke="#6e4a22" stroke-width="1"/><circle cx="568" cy="318" r="7.5" fill="#c23f2c" stroke="#6e1c12" stroke-width="1"/>
<path d="M568 311 l1 -4" stroke="#4a2f14" stroke-width="1.4"/><path d="M569 308 C 574 304 578 306 578 308 C 574 310 571 310 569 308Z" fill="#4f7a34"/></g>
<!-- 5 등잔과 펼친 복음서(.lt 무리가 차례로 켜져요) -->
<g class="lt"><circle cx="560" cy="262" r="230" fill="url(#__U__lamp)" opacity=".72"/></g>
<g class="lt"><path d="M552 300 L568 300 L566 292 L554 292Z" fill="#8a6a3a" stroke="#4a3418" stroke-width="1"/>
<path d="M552 292 C 548 280 572 280 568 292Z" fill="#a8823e" stroke="#4a3418" stroke-width="1"/>
<path d="M554 282 C 552 266 556 256 560 254 C 564 256 568 266 566 282Z" fill="rgba(255,240,210,.35)" stroke="#f3e6c8" stroke-width="1.1"/>
<path d="M560 276 C 556 270 558 264 560 260 C 562 264 564 270 560 276Z" fill="#ffd27a"/></g>
<g class="lt"><path d="M428 312 C 444 306 462 306 476 312 L476 326 C 462 320 444 320 428 326Z" fill="#efe4c8" stroke="#a8987a" stroke-width="1"/>
<path d="M476 312 C 490 306 508 306 524 312 L524 326 C 508 320 490 320 476 326Z" fill="#f4ead0" stroke="#a8987a" stroke-width="1"/>
<path d="M436 314 L468 312 M436 318 L468 316 M484 312 L516 314 M484 316 L516 318" stroke="#8a7a5e" stroke-width=".8"/>
<path d="M496 304 L498 320" stroke="#7a2a20" stroke-width="2"/></g>
<!-- 밤이 된 창 -->
<g class="sky2"><rect x="300" y="42" width="200" height="104" fill="url(#__U__night)"/><circle cx="377" cy="90" r="1.0" fill="#c9d3e4" opacity="0.28"/><circle cx="473" cy="93" r="1.0" fill="#c9d3e4" opacity="0.42"/><circle cx="476" cy="52" r="1.0" fill="#c9d3e4" opacity="0.45"/><circle cx="379" cy="101" r="1.4" fill="#c9d3e4" opacity="0.29"/><circle cx="315" cy="47" r="1.0" fill="#c9d3e4" opacity="0.40"/><circle cx="349" cy="75" r="1.4" fill="#c9d3e4" opacity="0.48"/><circle cx="457" cy="135" r="1.0" fill="#c9d3e4" opacity="0.29"/><circle cx="357" cy="74" r="1.4" fill="#c9d3e4" opacity="0.34"/><circle cx="325" cy="99" r="1.4" fill="#c9d3e4" opacity="0.48"/><circle cx="364" cy="117" r="1.0" fill="#c9d3e4" opacity="0.41"/><circle cx="493" cy="69" r="1.0" fill="#c9d3e4" opacity="0.41"/><circle cx="339" cy="136" r="1.0" fill="#c9d3e4" opacity="0.33"/><circle cx="475" cy="59" r="1.0" fill="#c9d3e4" opacity="0.36"/><circle cx="439" cy="127" r="1.0" fill="#c9d3e4" opacity="0.45"/><circle cx="390" cy="97" r="1.4" fill="#c9d3e4" opacity="0.47"/><circle cx="448" cy="73" r="1.4" fill="#c9d3e4" opacity="0.32"/><circle cx="418" cy="68" r="1.0" fill="#c9d3e4" opacity="0.44"/><circle cx="360" cy="133" r="1.0" fill="#c9d3e4" opacity="0.37"/></g>
<path d="M366 42 L366 146 M434 42 L434 146 M300 94 L500 94" stroke="#2a2018" stroke-width="5"/>
<rect x="300" y="42" width="200" height="104" fill="none" stroke="#3a2c20" stroke-width="6"/>
<rect x="290" y="150" width="220" height="9" fill="#3a2c20"/>
<g class="day" style="transition-delay:.6s">
<ellipse cx="142" cy="300" rx="44" ry="96" fill="url(#__U__halo)"/>
<path d="M126 238 C 126 226 158 226 158 238 L156 246 L128 246Z" fill="url(#__U__gh)" stroke="#fff1d6" stroke-opacity=".7" stroke-width="1.2"/>
<path d="M122 240 L162 240 L164 245 L120 245Z" fill="#fff1d6" opacity=".55"/>
<ellipse cx="142" cy="256" rx="12" ry="13" fill="url(#__U__gh)" stroke="#fff1d6" stroke-opacity=".7" stroke-width="1.2"/>
<path d="M124 272 C 128 266 156 266 160 272 L168 336 L116 336Z" fill="url(#__U__gh)" stroke="#fff1d6" stroke-opacity=".7" stroke-width="1.2"/>
<path d="M118 334 L166 334 L162 342 L122 342Z" fill="#fff1d6" opacity=".4"/>
<g transform="translate(133 372) scale(0.78)"><path d="M-9 -40 L9 -40 L10 -12 L-10 -12Z" fill="#8b857a" stroke="#4d4842" stroke-width="1"/><path d="M-11 -14 L10 -14 C 14 -8 20 -6 21 0 L-12 0 C -13 -6 -12 -10 -11 -14Z" fill="#3a2a1e" stroke="#21160e" stroke-width="1"/><path d="M-6 -34 L-4 -20 M4 -36 L5 -22" stroke="#6f6a61" stroke-width="1" opacity=".7"/></g><g transform="translate(153 372) scale(0.78)"><path d="M-9 -40 L9 -40 L10 -12 L-10 -12Z" fill="#8b857a" stroke="#4d4842" stroke-width="1"/><path d="M-11 -14 L10 -14 C 14 -8 20 -6 21 0 L-12 0 C -13 -6 -12 -10 -11 -14Z" fill="#3a2a1e" stroke="#21160e" stroke-width="1"/><path d="M-6 -34 L-4 -20 M4 -36 L5 -22" stroke="#6f6a61" stroke-width="1" opacity=".7"/></g>
</g><g class="day" style="transition-delay:2.2s">
<ellipse cx="196" cy="300" rx="42" ry="98" fill="url(#__U__halo)"/>
<path d="M182 252 C 180 236 212 236 210 252 C 210 262 204 268 196 268 C 188 268 182 262 182 252Z" fill="url(#__U__gh)" stroke="#fff1d6" stroke-opacity=".7" stroke-width="1.2"/>
<path d="M180 252 C 178 232 214 232 212 252 L214 262 C 206 254 186 254 178 262Z" fill="#fff1d6" opacity=".5"/>
<path d="M180 272 C 186 266 206 266 212 272 L224 338 L168 338Z" fill="url(#__U__gh)" stroke="#fff1d6" stroke-opacity=".7" stroke-width="1.2"/>
<path d="M178 290 C 190 280 212 284 214 296 C 214 306 196 312 184 306 C 176 302 174 294 178 290Z" fill="#fff6e6" opacity=".7" stroke="#fff1d6" stroke-width="1"/>
<circle cx="186" cy="292" r="5" fill="#fff6e6" opacity=".85"/>
<g transform="translate(188 372) scale(0.85)"><path d="M-5 -38 L5 -38 L6 -9 L-6 -9Z" fill="#7d7060" stroke="#4a4036" stroke-width="1"/><path d="M-4 -30 L4 -30 M-4 -22 L5 -22" stroke="#9a8b78" stroke-width="1" opacity=".6"/><path d="M-8 -10 L6 -10 C 11 -6 16 -4 16 0 L-8 0 C -9 -4 -9 -7 -8 -10Z" fill="#2e2620" stroke="#17120e" stroke-width="1"/></g><g transform="translate(204 372) scale(0.85)"><path d="M-5 -38 L5 -38 L6 -9 L-6 -9Z" fill="#7d7060" stroke="#4a4036" stroke-width="1"/><path d="M-4 -30 L4 -30 M-4 -22 L5 -22" stroke="#9a8b78" stroke-width="1" opacity=".6"/><path d="M-8 -10 L6 -10 C 11 -6 16 -4 16 0 L-8 0 C -9 -4 -9 -7 -8 -10Z" fill="#2e2620" stroke="#17120e" stroke-width="1"/></g>
</g><g class="day" style="transition-delay:3.8s">
<ellipse cx="246" cy="306" rx="44" ry="92" fill="url(#__U__halo)"/>
<path d="M226 262 C 220 248 236 238 248 240 C 260 242 266 252 262 262 L258 270 L232 270Z" fill="url(#__U__gh)" stroke="#fff1d6" stroke-opacity=".7" stroke-width="1.2"/>
<path d="M236 248 C 230 262 236 272 248 272" fill="none" stroke="#fff1d6" stroke-opacity=".6" stroke-width="1.2"/>
<path d="M228 276 C 234 268 254 268 260 276 L268 370 L222 370Z" fill="url(#__U__gh)" stroke="#fff1d6" stroke-opacity=".7" stroke-width="1.2"/>
<path d="M230 272 C 214 274 206 292 210 308 C 214 318 228 318 234 310Z" fill="#fff6e6" opacity=".42" stroke="#fff1d6" stroke-width="1"/>
<ellipse cx="278" cy="296" rx="9" ry="10" fill="url(#__U__gh)" stroke="#fff1d6" stroke-opacity=".7" stroke-width="1.2"/>
<path d="M266 306 C 270 302 286 302 290 306 L292 346 L264 346Z" fill="url(#__U__gh)" stroke="#fff1d6" stroke-opacity=".7" stroke-width="1.2"/>
<path d="M270 346 L270 372 M286 346 L286 372" stroke="#fff1d6" stroke-opacity=".6" stroke-width="4" stroke-linecap="round"/>
<circle cx="264" cy="318" r="5.2" fill="#c8402e" stroke="#7a1f14" stroke-width=".8"/>
<path d="M264 313 l1 -3" stroke="#4a2f14" stroke-width="1"/>
</g>
</svg>'''

ITEMS = [
 {'id': 'tea', 't': '사모바르와 차', 'la': 'two tumblers of tea',
  'say': '스테파니치가 힘이 부쳐 삽을 벽에 기대고 쉬어요. 마르틴은 창을 두드려 손짓하고, 문을 열어 그를 들여요. 그리고 차를 두 잔 따라요. 스테파니치가 다 마신 잔을 엎고 남은 설탕 조각을 올려놓아도, 마르틴은 또 따라 줘요.'},
 {'id': 'soup', 't': '양배추 수프와 빵', 'la': 'cabbage soup and bread',
  'say': '얇은 여름옷 차림의 엄마가 아기를 안고, 벽 곁에 서서 바람을 등지고 있어요. 마르틴은 계단을 올라가 그녀를 불러들여요. 화덕에서 양배추 수프를 떠 빵과 함께 식탁에 차려 주고, 그녀가 먹는 동안 아기를 안아 줘요.'},
 {'id': 'coat', 't': '낡은 외투', 'la': 'an old cloak',
  'say': '그녀는 병사의 아내예요. 남편은 여덟 달 전 먼 곳으로 떠난 뒤 소식이 없대요. 어제는 마지막 숄마저 맡기고 돈을 빌렸대요. 마르틴은 벽에 걸린 낡은 외투를 내려 건네고, 숄을 찾을 돈도 쥐여 줘요.'},
 {'id': 'apple', 't': '사과 하나', 'la': 'an apple',
  'say': '해진 모자를 쓴 소년이 사과 장수 할머니의 바구니에서 사과 하나를 집어요. 할머니가 소년의 머리채를 잡자, 마르틴은 송곳을 떨어뜨리고 뛰어나가요. 그리스도를 위해서라도 용서해 달라고 할머니에게 부탁하고, 소년에게는 용서를 빌게 해요. 그러고는 바구니에서 사과 하나를 꺼내 소년에게 주며, 값은 자기가 치르겠다고 해요.'},
 {'id': 'lights', 't': '등잔과 복음서', 'la': 'the lamp and the Gospels',
  'say': '날이 저물어요. 마르틴은 연장을 치우고 가죽 부스러기를 쓸어요. 등잔을 내려 탁자에 놓고, 선반에서 복음서를 꺼내요. 표시해 둔 곳을 펴려는데, 책은 다른 곳이 펼쳐져요.'},
]

CARD = {
 'id': 'read-martin', 'mode': '놓아 보기',
 'pagetitle': '마르틴이 기다린 하루',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>어느 겨울날</b><span>러시아의 한 도시 · 구두장이 마르틴의 반지하 방</span>',
 'lead': '러시아의 한 도시, 반지하 방에 사는 늙은 구두장이 마르틴은 어느 밤 “내일 거리를 내다보아라, 내가 가겠다” 하는 목소리를 들어요. 이튿날 그는 창가에서 일하며 하루 종일 그분을 기다려요. 그날 마르틴이 손님들에게 내준 것을 이야기의 차례대로 그 방에 놓아 보세요.',
 'leadKid': '구두장이 마르틴 할아버지가 꿈결에 ‘내일 너를 찾아가마’ 하는 목소리를 들었대. 다음 날 할아버지는 창밖을 보며 기다렸어. 그날 할아버지가 누구에게 무엇을 내줬는지, 하나씩 놓아 보자.',
 'meta': '영화처럼 약 3분 · 천천히 읽으면 5분',
 'draft': '검수 전 시안이에요(기준서 2판). 장면은 톨스토이의 이야기를 모드 부부가 영어로 옮긴 글(1906)을 따랐고, 우리말은 이 안내서가 옮겼어요. 반지하 방 무대는 이 안내서가 그렸어요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 실제 인물의 사진은 쓰지 않았어요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 3분',
 'theme': """:root{--accent:#3d5a73;--accent-ink:#f6fafc;--soft:rgba(61,90,115,.09);--stamp:#b0392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#a3bdd4;--accent-ink:#0e1620;--soft:rgba(163,189,212,.10);--stamp:#e86f5d}}
:root[data-theme="dark"]{--accent:#a3bdd4;--accent-ink:#0e1620;--soft:rgba(163,189,212,.10);--stamp:#e86f5d}""",
 'stamp': {'t': '손님', 'y': '1885', 'sub': '러시아 · 톨스토이'},
 'doneNote': '오늘 내 곁을 지나간 신발들과, 그 위의 얼굴들을 하나씩 떠올려 보세요.',
 'images': {},
 'extra_credits': [{'cr': '마르틴의 반지하 방 무대: 이 안내서가 그린 그림 · 톨스토이 「사랑이 있는 곳에 하나님이 계시다」(모드 부부 영역)를 바탕으로', 'u': CC}],
 'scenes': [
  {'id': 'window', 'label': '반지하 방의 창', 'kind': 'photo', 'img': 'card',
   'cap': '높은 창 아래의 일자리',
   'text': ['어느 도시에 구두장이 마르틴 아브데이치가 살았어요. 그의 방은 반지하에 있었고, 창은 길 쪽으로 하나뿐이었어요. 창으로는 지나가는 사람들의 발만 보였어요.',
            '그래도 마르틴은 신발만 보고 누구인지 알았어요. 동네 신발 거의 모두가 한 번쯤 그의 손을 거쳤거든요. 창 너머로 자기가 고친 신발이 지나가는 것도 자주 보았어요.',
            '마르틴은 아내를 잃고, 세 살 아들을 혼자 키웠어요. 그 아들마저 병으로 세상을 떠나자, 그는 하나님을 원망하고 교회에도 가지 않았어요.'],
   'text2': ['어느 날, 여덟 해째 순례 길을 걷던 고향 마을의 노인이 찾아와요. 이제 살고 싶지도 않다는 마르틴에게, 노인은 하나님을 위해 살라고, 복음서를 사서 읽어 보라고 말해요.',
             '마르틴은 큰 글씨 신약 성경을 사서 읽기 시작해요. 처음에는 쉬는 날에만 읽으려 했지만, 곧 날마다 일을 마치면 등잔 아래서 읽었어요.',
             '어느 밤, 누가복음 7장을 읽어요. 부자 바리새인이 예수님을 집에 청하고도 발 씻을 물조차 내주지 않은 대목이에요(' + bl('LUK.7', '누가복음 7장 44절') + '). 마르틴은 생각해요. ‘그 바리새인은 나 같은 사람이었구나. 자기만 생각했지. 그분이 내게 오신다면, 나도 그렇게 맞을까?’',
             '그러다 깜빡 잠든 그의 귀에 목소리가 들려요. “' + VOICE + '”'],
   'kid': '마르틴 할아버지는 반지하 방에 살았어. 창으로는 지나가는 사람들의 발만 보였대. 그래도 신발만 보고 누군지 다 알았어!',
   'kidq': '너는 신발만 보고도 누구인지 알아맞힐 수 있는 사람이 있어?'},
  {'id': 'day', 'label': '기다린 하루', 'kind': 'mod', 'mod': 'place',
   'text': ['이튿날, 마르틴은 날이 밝기 전에 일어나 기도해요. 화덕에 불을 지펴 양배추 수프와 메밀죽을 끓이고, 사모바르에 불을 붙이고, 앞치마를 두르고 창가에 앉아요. 그러고는 일보다 창밖을 더 많이 내다봐요. 낯선 신발이 지나가면 몸을 숙여 얼굴을 올려다봐요.',
            '새 펠트 장화를 신은 문지기가 지나가고, 물장수가 지나가요. 그리고 늙은 병사 스테파니치가 와서 창 앞의 눈을 치워요. 마르틴은 낡은 펠트 장화에 가죽 덧신을 댄 그 신발을 보고 그를 알아봐요.',
            '그날 마르틴이 손님들에게 내준 것을, 아래 무대에 이야기의 차례대로 놓아 보세요. 창밖에는 그때마다 누가 서 있었는지도 보여요.'],
   'quote': {'t': TOP, 'from': '그날 밤 펼쳐진 복음서 맨 위에서 마르틴이 읽은 말씀 · 마태복음 25장 35절을 풀어 씀', 'u': NKRV + 'MAT.25'},
   'text2': ['그 쪽 맨 아래에는 이런 말씀도 있었어요. 가장 작은 이 하나에게 해 준 것이 곧 나에게 해 준 것이라는 말씀이에요(' + bl('MAT.25', '마태복음 25장 40절') + ').',
             '마르틴은 알았어요. 꿈이 헛되지 않았다는 것을요. 그날 구세주가 정말 그를 찾아왔고, 그가 그분을 맞아들였다는 것을요.',
             '그날 아침 창 너머로 발부터 보았던 사람들이, 그날 밤에는 웃는 얼굴로 그 앞에 나타났어요.'],
   'kid': '차 한 잔, 따뜻한 수프, 낡은 외투, 사과 하나! 그리고 밤이 되자 등잔을 켰어. 하나씩 놓아 보자.',
   'kidq': '어두운 구석에서 “나를 모르겠니?” 하고 나온 사람들은 누구였을까?'},
 ],
 'imagine': {'t': '반지하 방에 양배추 수프 냄새가 배어 있어요. 사모바르가 낮게 끓고, 송곳이 가죽을 뚫는 소리가 들려요. 창밖으로는 눈 밟는 발소리가 지나가요. 밤이 되자 등잔 불빛이 펼친 복음서 위에 고여요.',
             'kid': '눈을 감아 봐. 사모바르가 보글보글, 창밖에서 뽀드득뽀드득 발소리. 누가 지나갈까?'},
 'lines': ['신발만 보이던 창, 얼굴로 돌아온 사람들.', '차 한 잔, 수프 한 그릇, 낡은 외투, 사과 하나.', '“마르틴, 나를 모르겠느냐?”'],
 'linesKid': ['차 한 잔, 수프 한 그릇!', '“나를 모르겠니?”'],
 'close': {'form': '처음으로 돌아가기',
           'from': '첫 장면의 창 — 마르틴은 반지하 창으로 사람들의 발만 보고도 누구인지 알았고, 그날 아침에는 낯선 신발이 지날 때마다 몸을 숙여 얼굴을 올려다봤어요. 그날 밤 그 사람들이 어두운 구석에서 나와 웃어요(모드 부부 영역).',
           'ask': '마르틴은 낯선 신발이 지날 때마다 몸을 숙여 얼굴을 올려다봤어요. 오늘 내 곁을 지나간 신발의 주인은 누구였을까요?',
           'askKid': '마르틴 할아버지는 신발만 보고도 누군지 알았대. 오늘 네 곁을 지나간 신발의 주인은 누구누구였어?'},
 'goals': {
  's4': {'t': '이야기의 차례대로', 'p': '그날 마르틴이 내준 것을 이야기의 차례(아침의 차 한 잔부터 저녁의 등잔까지)대로 다 놓으면 카드에 금박이 입혀져요.',
         'how': '이야기의 차례대로 마르틴의 하루를 다 놓아 보세요', 'done': '이야기의 차례대로 마르틴의 하루를 놓았어요',
         'ways': [{'id': 'plOrder', 't': '사모바르와 차 → 양배추 수프와 빵 → 낡은 외투 → 사과 하나 → 등잔과 복음서 차례로 놓기'}]},
  's5': {'t': '우리 집 차 한 잔 자리', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '우리 집 차 한 잔 자리를 고르거나, 아이와 함께 끝까지 보세요', 'done': '우리 집 차 한 잔 자리를 정했어요',
         'ways': [{'id': 'home', 't': '우리 집이라면 찾아온 사람에게 차 한 잔을 어디서 내줄지 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {'place': {
   'items': ITEMS, 'order': '사모바르와 차, 양배추 수프와 빵, 낡은 외투, 사과 하나, 등잔과 복음서',
   'intro': '아래에서 하나를 골라 마르틴의 방에 놓아 보세요. 이야기의 차례는 아침의 차 한 잔부터예요.',
   'climax': '어두운 구석에서 누군가 움직이는 소리가 나요. “마르틴, 마르틴, 나를 모르겠느냐?” “누구세요?” “나다.” 스테파니치가 걸어 나와 웃고는 구름처럼 사라져요. 이어 아기를 안은 엄마가 나와 웃고 아기도 웃더니 사라지고, 할머니와 사과를 든 소년이 나와 웃고는 사라져요.<span class="la">“It is I,” said the voice.<br>「사랑이 있는 곳에 하나님이 계시다」 모드 부부 영역 · 이 안내서가 옮김</span>',
   'home': ['식탁', '부엌', '거실', '현관 앞', '창가'],
   'homeLabel': '우리 집 차 한 잔 자리',
   'homeWait': '마르틴의 하루를 다 놓아 본 뒤 고를 수 있어요',
   'wrongOrder': '이야기의 차례는 이래요: {order}',
   'orderDone': '이야기의 차례대로 다 놓았어요',
   'daylight': False,
   'svg': STAGE}},
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 놓아 보기</button></div>
  <div class="pl-home" hidden><p>우리 집이라면, 찾아온 사람에게 따뜻한 차 한 잔을 어디서 내줄까요?</p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>바탕이 된 이야기</b> 톨스토이가 바탕으로 삼은 이야기가 따로 있어요. 프랑스 개신교 목사이자 작가인 뤼벤 사양스(Ruben Saillens)의 성탄 이야기 「마르탱 할아버지」(Le Père Martin)예요. 러시아 고리키 세계문학연구소의 시조바는 2019년 논문에서 톨스토이의 원고를 모두 살펴, 톨스토이가 이 이야기를 어떻게 받아들였는지 새로 짚었어요.',
    '<b>잊어버린 사과값</b> 마르틴은 사과값을 치르겠다고 했지만, 할머니는 그 돈 받는 것을 그만 잊어버려요. 소년은 할머니의 자루를 대신 메고, 둘은 나란히 걸어가요.',
    '<b>다른 제목의 오페라</b> 체코 작곡가 보후슬라프 마르티누는 1952년, 이 이야기로 한 막짜리 오페라를 지었어요. 그런데 제목은 톨스토이의 다른 이야기 제목인 「사람은 무엇으로 사는가」예요.',
    '<b>점토 인형 영화</b> 1977년 윌 빈턴은 이 이야기를 점토 인형 영화 「구두장이 마르틴」(Martin the Cobbler)으로 만들었어요. 톨스토이의 딸 알렉산드라 톨스타야가 이야기를 소개하고 들려줘요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>제목</b> 모드 부부는 「Where Love Is, God Is」로, 1887년 미국에서 나온 네이선 해스컬 돌의 번역은 「Where Love Is, There God Is Also」로 옮겼어요. 영어권에서는 「구두장이 마르틴」(Martin the Cobbler)이라고도 불러요.',
    '<b>이름</b> 러시아어 원문의 이름은 마르틴 아브데이치(Мартын Авдеич)예요. 모드 부부는 Martin Avdéitch로, 돌은 Martuin Avdyeitch로 적었어요. 우리말 그림책은 ‘마틴’으로 옮겼어요.']},
  {'h': '원문 읽기', 'checked': '2026년 11월 18일', 'p': [
    '이 이야기는 러시아어 원문과 모드 부부의 영어 번역 모두 저작권이 끝나 누구나 읽을 수 있어요.'],
   'links': [{'t': '기독교 고전 전자 도서관(CCEL): 모드 부부의 영어 번역 「Where Love Is, God Is」(『스물세 이야기』 7번째 이야기)', 'u': CC, 'm': '영어'},
             {'t': '위키문헌: 러시아어 원문 「Где любовь, там и Бог」', 'u': RU, 'm': '러시아어'}]},
 ],
 'src': [
  {'l': '기독교 고전 전자 도서관(CCEL): 『스물세 이야기』(L. and A. Maude 옮김) — Where Love Is, God Is (1885) — 반지하 방의 창, 신발로 사람을 앎, 아내와 세 살 아들, 순례자 노인, 큰 글씨 신약, 누가복음 6·7장과 바리새인, 목소리, 이튿날 아침(기도·화덕·양배추 수프와 메밀죽·사모바르·앞치마·창가), 문지기와 물장수, 스테파니치(펠트 장화와 가죽 덧신·삽·차 두 잔·엎은 잔과 설탕), 엄마와 아기(여름옷·계단·수프와 빵·식탁·여덟 달·숄·낡은 외투), 할머니와 소년(해진 모자·송곳·용서·사과값·자루), 저녁(등잔·복음서·표시해 둔 곳·구석의 목소리·구름처럼), 마태복음 25장 35·40절, 마지막 문장', 'u': CC},
  {'l': '위키문헌(러시아어): 「Где любовь, там и Бог」 — 창으로 발만 보였지만 신발로 사람을 알아봄, 자기가 고친 신발을 창으로 자주 봄, 이름 Мартын Авдеич', 'u': RU},
  {'l': '위키백과(영어): Where Love Is, God Is — 1885년, 다른 영어 제목들, 마르티누의 오페라(1952), 윌 빈턴의 점토 인형 영화(1977)와 알렉산드라 톨스타야', 'u': WP},
  {'l': '위키백과(영어): Ruben Saillens — 프랑스 개신교 목사이자 작가, 성탄 이야기 「Le Père Martin」', 'u': WPS},
  {'l': '시조바(고리키 세계문학연구소, 2019), 「톨스토이 「사랑이 있는 곳에 하나님이 계시다」의 탄생과 시학」 요약 — 알려진 원고 전체, 바탕 이야기 사양스의 「Father Martin」', 'u': SIZ},
  {'l': '톨스토이 아카이브: 네이선 해스컬 돌의 번역 「Where Love is There God is Also」(T. Y. 크로웰, 1887) — Martuin Avdyeitch', 'u': DOLE},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'card', 'fit': 'cover', 'p0': '30% 35%', 'p1': '50% 55%', 's0': 1.25, 's1': 1.05, 'kicker': '어느 겨울 · 러시아의 한 도시', 'title': '구두장이 마르틴',
   'lines': [{'t': '늙은 구두장이 마르틴은 반지하 방에 살아요.'}, {'t': '창으로는 지나가는 사람들의 발만 보여요.'}],
   'kid': [{'t': '구두장이 할아버지네 방이야.'}, {'t': '창으로 사람들 발만 보여!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '창 너머 신발'},
  {'type': 'img', 'ch': 1, 'img': 'card', 'fit': 'contain', 'p0': '50% 50%', 'p1': '45% 40%', 's0': 1.0, 's1': 1.1, 'cap': '마코프스키 「구두장이」(이 이야기의 그림은 아니에요)',
   'lines': [{'t': '그래도 신발만 보고 누구인지 알아요. 거의 다 그의 손을 거친 신발이에요.'},
             {'t': '아들을 잃은 뒤, 그는 저녁마다 등잔 아래서 복음서를 읽어요.'},
             {'t': VOICE, 'q': True, 'from': '꿈결에 들은 목소리'}],
   'kid': [{'t': '할아버지는 신발만 보고도 누군지 다 알았대.'}, {'t': '‘내일 너를 찾아가마!’ 누구 목소리였을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '기다린 하루'},
  {'type': 'mod', 'mod': 'place', 'ch': 2,
   'lines': [{'t': '아침, 늙은 병사 스테파니치가 창 앞의 눈을 치워요. 마르틴은 그를 불러 차를 따라요.', 'act': 'tea'},
             {'t': '아기를 안은 엄마에게는 양배추 수프와 빵을,', 'act': 'soup'},
             {'t': '벽에 걸린 낡은 외투도 내려 줘요.', 'act': 'coat'},
             {'t': '사과를 집은 소년과 할머니를 화해시키고, 소년에게 사과를 줘요.', 'act': 'apple'},
             {'t': '날이 저물자 등잔을 탁자에 놓고, 복음서를 펴요.', 'act': 'lights'},
             {'t': '“마르틴, 나를 모르겠느냐?” 구석에서 그날 만난 사람들이 하나씩 나와 웃어요.', 'act': 'day', 'wait': 5200}],
   'kid': [{'t': '추운 할아버지에게 따뜻한 차!', 'act': 'tea'}, {'t': '아기 엄마에게 수프랑 빵,', 'act': 'soup'}, {'t': '낡은 외투도!', 'act': 'coat'},
           {'t': '사과 하나는 그 아이에게.', 'act': 'apple'}, {'t': '밤이 되자 등잔을 켜고,', 'act': 'lights'},
           {'t': '“나를 모르겠니?” 오늘 만난 사람들이 웃으며 나타났어!', 'act': 'day', 'wait': 5200},
           {'t': '할아버지가 기다리던 분은 어디 계셨을까?', 'ask': True}]},
  {'type': 'imagine', 'ch': 3,
   'lines': [{'t': '사모바르 끓는 소리, 송곳이 가죽을 뚫는 소리.'}, {'t': '창밖으로 눈 밟는 발소리가 지나가요.'}, {'t': '밤, 등잔 불빛이 복음서 위에 고여요.'}],
   'kid': [{'t': '보글보글, 뽀드득뽀드득.'}, {'t': '누가 지나갈까?'}]},
  {'type': 'quote', 'ch': 3, 'big': '배고플 때 먹을 것을 주고, 나그네였을 때 맞아들였다.',
   'lines': [{'t': '그날 밤 펼쳐진 복음서 · 마태복음 25장 35절을 풀어 씀', 'wait': 2600}],
   'kid': [{'t': '복음서에 이렇게 쓰여 있었대. 배고픈 사람에게 먹을 걸 주면, 예수님께 드린 거래.', 'wait': 2600}]},
  {'type': 'img', 'ch': 3, 'img': 'card', 'fit': 'cover', 'p0': '28% 30%', 'p1': '30% 32%', 's0': 1.5, 's1': 1.6, 'cap': '창 너머로',
   'lines': [{'t': '그날 아침 창 너머로 발부터 보았던 사람들이,'}, {'t': '그날 밤에는 웃는 얼굴로 그 앞에 나타났어요.'}],
   'kid': [{'t': '창으로 발만 보던 사람들이,'}, {'t': '웃는 얼굴로 찾아왔어!'}]},
  {'type': 'reward', 'ch': 3},
 ],
}
