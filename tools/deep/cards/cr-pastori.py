# -*- coding: utf-8 -*-
"""깊은 카드: 나폴리 구유 인형 ‘파스토리’(cr-pastori) · 중심 방식 = 놓아 보기(+두 그림 나란히, 고르기)
기준서 2판 · 틀 deep3-4 · 키트 3판 · 2026-11-18 6번 묶음 창(창 6)이 만듦
두 질문(기준서 ‘만들기 전 두 질문’):
  1. 그 자리에 있고 싶은 한 순간: 18세기 나폴리의 성탄 무렵, 집의 평평한 지붕 위에 차린 구유. 그 뒤로 바다 건너
     베수비오가 뒷배경이 되는 때(괴테 『이탈리아 기행』 1787년 5월 27일 나폴리)
  2. 손으로 하는 한 가지는 이야기 속 무엇에서 나오나: 괴테가 적은 차례 그대로 지붕 위 구유 차리기
     → 놓아 보기(오두막 틀 → 늘푸른 나무와 덤불 → 성모와 아기 → 둘레에 선 이들 → 둘레에 떠 있는 이들 → 뒷배경)
끝맺는 꼴: 기록 한 마디 · 괴테의 “흉내 낼 수 없이 빛나게 하는 것은 … 베수비오와 그 둘레를 품은 뒷배경”
5단계: 고르기(이야기 속 사람의 자리 — 1787년 나폴리 집이라면 누구의 옷에 공을 들일까, 고른 뒤 기록 한 줄) + 아이와 함께
카드 크기: 큰 카드(장면 4개).
무대 그림은 아래 stage_svg()가 그려요(이 안내서가 그림, 괴테의 글 차례를 따름. 둘레에 선 이들은 목자와 왕으로,
떠 있는 이들은 천사로 그렸어요). 앞면 사진은 요즘 만든 인형일 수 있어서 장면·영화에는 18세기 인형 사진을 썼어요.
그림 원본(src)은 deep_src/cr-pastori/ (저장소 밖). 받는 법: commons_get.py"""
S = 'cr-pastori/'
NKRV = 'https://bible.bskorea.or.kr/bible/NKRV/'
def bl(code, label):   # 성경: 풀어 쓰고 개역개정 링크. 예: bl('LUK.2', '누가복음 2장 7절')
    return f'<a href="{NKRV}{code}" target="_blank" rel="noopener">{label}</a>'

import random


def _person(x, y, h, robe, mantle=None, head='#e9cfae', hair='#5a3b26', staff=None, crown=False, vest=None, face_dir=1):
    """서 있는 사람(앞모습에 가까운 옆모습). x: 발 가운데, y: 발 밑, h: 키."""
    w = h * 0.26
    hy = y - h + h * 0.09          # 머리 가운데
    r = h * 0.085
    s = ''
    if staff:
        sx = x + face_dir * w * 0.95
        s += f'<line x1="{sx:.1f}" y1="{y:.1f}" x2="{sx:.1f}" y2="{y - h * 0.98:.1f}" stroke="{staff}" stroke-width="{h * 0.028:.1f}" stroke-linecap="round"/>'
        if staff == '#8a6a43':   # 목자의 굽은 지팡이
            s += f'<path d="M{sx:.1f} {y - h * 0.98:.1f} q{face_dir * h * 0.08:.1f} {-h * 0.06:.1f} {face_dir * h * 0.1:.1f} {h * 0.04:.1f}" stroke="{staff}" stroke-width="{h * 0.028:.1f}" fill="none" stroke-linecap="round"/>'
    # 옷(아래로 퍼지는 겉옷)
    s += (f'<path d="M{x - w * 0.55:.1f} {hy + r * 1.1:.1f} Q{x - w * 0.7:.1f} {y - h * 0.45:.1f} {x - w:.1f} {y:.1f} L{x + w:.1f} {y:.1f} '
          f'Q{x + w * 0.7:.1f} {y - h * 0.45:.1f} {x + w * 0.55:.1f} {hy + r * 1.1:.1f} Z" fill="{robe}"/>')
    if vest:
        s += (f'<path d="M{x - w * 0.5:.1f} {hy + r * 1.3:.1f} L{x - w * 0.62:.1f} {y - h * 0.42:.1f} L{x + w * 0.62:.1f} {y - h * 0.42:.1f} L{x + w * 0.5:.1f} {hy + r * 1.3:.1f} Z" fill="{vest}"/>'
              + ''.join(f'<circle cx="{x + dx * w * 0.42:.1f}" cy="{hy + r * 1.6 + k * h * 0.07:.1f}" r="{h * 0.018:.1f}" fill="#efe7d6" opacity=".55"/>'
                        for k in range(4) for dx in (-1, 0, 1)))
    if mantle:
        s += (f'<path d="M{x - w * 0.6:.1f} {hy + r * 0.6:.1f} Q{x - w * 1.05:.1f} {y - h * 0.38:.1f} {x - w * 0.95:.1f} {y - h * 0.08:.1f} '
              f'L{x - w * 0.3:.1f} {y - h * 0.12:.1f} Q{x - w * 0.2:.1f} {y - h * 0.5:.1f} {x + w * 0.1:.1f} {hy + r * 1.4:.1f} Z" fill="{mantle}"/>')
    # 허리띠
    s += f'<rect x="{x - w * 0.62:.1f}" y="{y - h * 0.47:.1f}" width="{w * 1.24:.1f}" height="{h * 0.028:.1f}" fill="#3b2a1c" opacity=".55"/>'
    # 머리
    s += f'<circle cx="{x:.1f}" cy="{hy:.1f}" r="{r:.1f}" fill="{head}"/>'
    s += f'<path d="M{x - r:.1f} {hy - r * 0.1:.1f} Q{x:.1f} {hy - r * 1.55:.1f} {x + r:.1f} {hy - r * 0.1:.1f} Q{x:.1f} {hy - r * 0.75:.1f} {x - r:.1f} {hy - r * 0.1:.1f}Z" fill="{hair}"/>'
    if crown:
        cw = r * 1.7
        s += (f'<path d="M{x - cw / 2:.1f} {hy - r * 0.75:.1f} l{cw * 0.12:.1f} {-r * 0.75:.1f} l{cw * 0.16:.1f} {r * 0.45:.1f} l{cw * 0.22:.1f} {-r * 0.7:.1f} '
              f'l{cw * 0.22:.1f} {r * 0.7:.1f} l{cw * 0.16:.1f} {-r * 0.45:.1f} l{cw * 0.12:.1f} {r * 0.75:.1f}Z" fill="#e3b53e"/>')
    return s


def _kneel(x, y, h, robe, mantle, gift=None, lamb=False, face_dir=1, head='#e9cfae', hair='#5a3b26', crown=False):
    """무릎 꿇은 사람. h: 무릎 꿇은 키."""
    w = h * 0.34
    hy = y - h + h * 0.12
    r = h * 0.11
    s = (f'<path d="M{x - w * 0.9:.1f} {y:.1f} Q{x - w * 1.0:.1f} {y - h * 0.42:.1f} {x - w * 0.35:.1f} {hy + r * 1.2:.1f} '
         f'L{x + w * 0.35:.1f} {hy + r * 1.2:.1f} Q{x + w * 0.75:.1f} {y - h * 0.5:.1f} {x + w * 0.95:.1f} {y:.1f} Z" fill="{robe}"/>')
    if mantle:
        s += (f'<path d="M{x - w * 0.45:.1f} {hy + r * 0.7:.1f} Q{x - w * 1.1:.1f} {y - h * 0.35:.1f} {x - w * 1.05:.1f} {y:.1f} L{x - w * 0.2:.1f} {y:.1f} '
              f'Q{x - w * 0.15:.1f} {y - h * 0.45:.1f} {x + w * 0.25:.1f} {hy + r * 1.3:.1f} Z" fill="{mantle}"/>')
    s += f'<circle cx="{x + face_dir * w * 0.12:.1f}" cy="{hy:.1f}" r="{r:.1f}" fill="{head}"/>'
    s += f'<path d="M{x + face_dir * w * 0.12 - r:.1f} {hy:.1f} Q{x + face_dir * w * 0.12:.1f} {hy - r * 1.6:.1f} {x + face_dir * w * 0.12 + r:.1f} {hy:.1f} Q{x + face_dir * w * 0.12:.1f} {hy - r * 0.7:.1f} {x + face_dir * w * 0.12 - r:.1f} {hy:.1f}Z" fill="{hair}"/>'
    if crown:
        cx0 = x + face_dir * w * 0.12; cw = r * 1.7
        s += (f'<path d="M{cx0 - cw / 2:.1f} {hy - r * 0.7:.1f} l{cw * 0.12:.1f} {-r * 0.75:.1f} l{cw * 0.16:.1f} {r * 0.45:.1f} l{cw * 0.22:.1f} {-r * 0.7:.1f} '
              f'l{cw * 0.22:.1f} {r * 0.7:.1f} l{cw * 0.16:.1f} {-r * 0.45:.1f} l{cw * 0.12:.1f} {r * 0.75:.1f}Z" fill="#e3b53e"/>')
    hx = x + face_dir * w * 0.85
    if gift:
        s += (f'<rect x="{hx - h * 0.07:.1f}" y="{y - h * 0.5:.1f}" width="{h * 0.14:.1f}" height="{h * 0.11:.1f}" rx="1.5" fill="#e3b53e"/>'
              f'<rect x="{hx - h * 0.08:.1f}" y="{y - h * 0.53:.1f}" width="{h * 0.16:.1f}" height="{h * 0.04:.1f}" rx="1" fill="#b98a26"/>')
    if lamb:
        s += (f'<ellipse cx="{hx:.1f}" cy="{y - h * 0.36:.1f}" rx="{h * 0.16:.1f}" ry="{h * 0.1:.1f}" fill="#efe9dc"/>'
              f'<circle cx="{hx + face_dir * h * 0.15:.1f}" cy="{y - h * 0.4:.1f}" r="{h * 0.06:.1f}" fill="#e8e1d2"/>'
              f'<circle cx="{hx + face_dir * h * 0.17:.1f}" cy="{y - h * 0.41:.1f}" r="{h * 0.012:.1f}" fill="#2c2620"/>')
    return s


def _angel(x, y, k, robe, robe2, flip=1):
    """둘레에 떠 있는 천사. (x, y)는 몸 가운데, k는 크기."""
    s = ''
    # 날개(나무로 깎은 날개처럼 금빛 갈색, 깃털 줄)
    for side in (-1, 1):
        X = lambda v: x + side * v * k
        s += (f'<path d="M{X(3):.1f} {y - 12 * k:.1f} C{X(12):.1f} {y - 30 * k:.1f} {X(28):.1f} {y - 41 * k:.1f} {X(41):.1f} {y - 37 * k:.1f} '
              f'C{X(37):.1f} {y - 28 * k:.1f} {X(31):.1f} {y - 19 * k:.1f} {X(23):.1f} {y - 12 * k:.1f} '
              f'C{X(18):.1f} {y - 7 * k:.1f} {X(10):.1f} {y - 3 * k:.1f} {X(3):.1f} {y - 4 * k:.1f} Z" fill="#c49a52"/>'
              f'<path d="M{X(5):.1f} {y - 13 * k:.1f} C{X(13):.1f} {y - 28 * k:.1f} {X(26):.1f} {y - 37 * k:.1f} {X(37):.1f} {y - 35 * k:.1f} '
              f'C{X(27):.1f} {y - 30 * k:.1f} {X(16):.1f} {y - 21 * k:.1f} {X(5):.1f} {y - 13 * k:.1f} Z" fill="#e2c27c" opacity=".75"/>'
              + ''.join(f'<path d="M{X(6 + j * 2):.1f} {y - (9 + j) * k:.1f} Q{X(16 + j * 4):.1f} {y - (16 + j * 5) * k:.1f} {X(27 + j * 4):.1f} {y - (17 + j * 6) * k:.1f}" '
                        f'stroke="#8f6a32" stroke-width="{0.9 * k:.1f}" fill="none" opacity=".55"/>' for j in range(3)))
    # 휘날리는 옷
    s += (f'<path d="M{x - 7 * k:.1f} {y - 14 * k:.1f} Q{x - 12 * k:.1f} {y + 6 * k:.1f} {x - 20 * k * flip:.1f} {y + 26 * k:.1f} '
          f'Q{x - 4 * k:.1f} {y + 22 * k:.1f} {x + 6 * k:.1f} {y + 30 * k:.1f} Q{x + 12 * k:.1f} {y + 8 * k:.1f} {x + 7 * k:.1f} {y - 14 * k:.1f} Z" fill="{robe}"/>')
    s += (f'<path d="M{x - 6 * k:.1f} {y - 12 * k:.1f} Q{x + 2 * k:.1f} {y - 2 * k:.1f} {x + 16 * k * flip:.1f} {y + 4 * k:.1f} '
          f'Q{x + 24 * k * flip:.1f} {y + 10 * k:.1f} {x + 30 * k * flip:.1f} {y + 6 * k:.1f} Q{x + 18 * k * flip:.1f} {y - 4 * k:.1f} {x + 6 * k:.1f} {y - 14 * k:.1f} Z" fill="{robe2}" opacity=".95"/>')
    # 머리와 곱슬머리
    s += f'<circle cx="{x:.1f}" cy="{y - 19 * k:.1f}" r="{5.2 * k:.1f}" fill="#efd4b2"/>'
    s += f'<path d="M{x - 5.5 * k:.1f} {y - 19 * k:.1f} Q{x - 6 * k:.1f} {y - 27 * k:.1f} {x:.1f} {y - 26 * k:.1f} Q{x + 6.5 * k:.1f} {y - 27 * k:.1f} {x + 5.6 * k:.1f} {y - 19 * k:.1f} Q{x:.1f} {y - 23 * k:.1f} {x - 5.5 * k:.1f} {y - 19 * k:.1f}Z" fill="#8a5a2e"/>'
    # 팔
    s += f'<path d="M{x + 5 * k:.1f} {y - 11 * k:.1f} q{6 * k * flip:.1f} {3 * k:.1f} {11 * k * flip:.1f} {-2 * k:.1f}" stroke="#efd4b2" stroke-width="{2.4 * k:.1f}" fill="none" stroke-linecap="round"/>'
    return s


def stage_svg():
    R = random.Random(1787)
    W, H = 800, 450
    stars = ''.join(f'<circle cx="{R.uniform(110, 690):.0f}" cy="{R.uniform(14, 120):.0f}" r="{R.choice([.6, .8, 1.0]):.1f}" fill="#fff" opacity="{R.uniform(.25, .6):.2f}"/>' for _ in range(18))
    # 뒤쪽 이웃 지붕들(평평한 지붕, 낮은 난간, 성당 둥근 지붕 하나, 종탑 하나)
    roofs, x = '', -10
    while x < W + 10:
        bw = R.choice([46, 58, 64, 72, 84]); top = R.choice([288, 294, 300, 306, 312])
        roofs += f'<rect x="{x}" y="{top}" width="{bw + 1}" height="{352 - top}" fill="#2a2433"/><rect x="{x}" y="{top - 4}" width="{bw + 1}" height="4" fill="#3a3346"/>'
        for wx in range(x + 8, x + bw - 8, 14):
            if R.random() < .32:
                roofs += f'<rect x="{wx}" y="{top + R.choice([12, 22, 30])}" width="5" height="7" fill="#f3c27a" opacity="{R.uniform(.35, .75):.2f}"/>'
        x += bw
    dome = ('<path d="M138 300 L138 262 Q138 226 172 222 Q206 226 206 262 L206 300Z" fill="#2f2938"/>'
            '<rect x="166" y="204" width="12" height="20" fill="#2f2938"/><path d="M164 205 L172 192 L180 205Z" fill="#2f2938"/>'
            '<path d="M150 252 Q172 236 194 252" stroke="#3d3649" stroke-width="2" fill="none"/>')
    tower = ('<rect x="618" y="232" width="28" height="80" fill="#2f2938"/><path d="M614 234 L632 212 L650 234Z" fill="#2f2938"/>'
             '<rect x="626" y="246" width="12" height="16" rx="6" fill="#1c1826"/>')
    # 우리 지붕: 난간과 바닥(타일)
    tiles = ''.join(f'<line x1="{400 + (xx - 400) * .42:.1f}" y1="366" x2="{xx}" y2="450" stroke="#5a4033" stroke-width="1.2" opacity=".55"/>' for xx in range(-300, 1101, 70))
    tiles += ''.join(f'<line x1="0" y1="{yy}" x2="800" y2="{yy}" stroke="#5a4033" stroke-width="1" opacity=".45"/>' for yy in (376, 390, 408, 430))
    pots = ('<path d="M96 344 L124 344 L120 366 L100 366Z" fill="#a4553a"/><path d="M92 334 Q110 300 128 334Z" fill="#2f5a3a" opacity=".85"/>'
            '<path d="M680 344 L708 344 L704 366 L684 366Z" fill="#a4553a"/><circle cx="694" cy="334" r="13" fill="#3d6b45" opacity=".85"/>')

    # ---- 놓을 것 ----
    hut = ('<g class="obj" data-o="hut">'
           # 뒤 기둥과 갈대 벽
           '<line x1="346" y1="372" x2="346" y2="236" stroke="#7b5a38" stroke-width="4"/><line x1="454" y1="372" x2="454" y2="236" stroke="#7b5a38" stroke-width="4"/>'
           + ''.join(f'<line x1="{xx}" y1="246" x2="{xx}" y2="370" stroke="#a88b5e" stroke-width="2" opacity=".42"/>' for xx in range(352, 450, 8))
           + '<line x1="346" y1="300" x2="454" y2="300" stroke="#8a6a43" stroke-width="2.4" opacity=".7"/>'
           # 앞 기둥
           '<line x1="324" y1="374" x2="324" y2="244" stroke="#9c7748" stroke-width="5.5" stroke-linecap="round"/>'
           '<line x1="476" y1="374" x2="476" y2="244" stroke="#9c7748" stroke-width="5.5" stroke-linecap="round"/>'
           # 지붕 틀과 이엉
           '<path d="M306 248 L400 198 L494 248" stroke="#8a6a43" stroke-width="5" fill="none" stroke-linejoin="round"/>'
           '<path d="M300 252 L400 194 L500 252 L488 258 L476 252 L462 260 L450 252 L436 261 L422 253 L410 262 L398 254 L386 262 L374 253 L360 261 L348 252 L334 260 L322 252 L310 258Z" fill="#c29a5c"/>'
           '<path d="M318 246 L400 202 L482 246" stroke="#e0bd7c" stroke-width="1.6" fill="none" opacity=".6"/>'
           '<line x1="306" y1="248" x2="494" y2="248" stroke="#7b5a38" stroke-width="3"/>'
           '</g>')
    def cypress(cx, base, h):
        return (f'<path d="M{cx} {base - h} Q{cx + h * .2:.1f} {base - h * .55:.1f} {cx + h * .14:.1f} {base} L{cx - h * .14:.1f} {base} Q{cx - h * .2:.1f} {base - h * .55:.1f} {cx} {base - h}Z" fill="#2e5a3a"/>'
                f'<path d="M{cx} {base - h + 6} Q{cx + h * .1:.1f} {base - h * .55:.1f} {cx + h * .05:.1f} {base - 6}" stroke="#4f8250" stroke-width="2.2" fill="none" opacity=".7"/>')
    def bush(cx, cy, r):
        return (f'<circle cx="{cx - r * .7:.1f}" cy="{cy}" r="{r * .7:.1f}" fill="#335f3e"/><circle cx="{cx + r * .7:.1f}" cy="{cy + 1}" r="{r * .65:.1f}" fill="#335f3e"/>'
                f'<circle cx="{cx}" cy="{cy - r * .35:.1f}" r="{r * .8:.1f}" fill="#3f7048"/><circle cx="{cx - r * .25:.1f}" cy="{cy - r * .55:.1f}" r="{r * .3:.1f}" fill="#5b8f55" opacity=".8"/>')
    leaves = ''.join(f'<ellipse cx="{xx:.0f}" cy="{248 - (100 - abs(xx - 400)) * .53 + 3:.0f}" rx="5" ry="2.6" fill="#3f7048" transform="rotate({-28 if xx < 400 else 28} {xx:.0f} {248 - (100 - abs(xx - 400)) * .53 + 3:.0f})"/>'
                     for xx in range(312, 492, 12) if abs(xx - 400) > 6)
    green = ('<g class="obj" data-o="green">' + cypress(268, 374, 128) + cypress(534, 374, 116) + leaves
             + bush(300, 364, 15) + bush(500, 365, 14) + bush(352, 368, 9) + bush(452, 368, 9) + '</g>')
    mother = ('<g class="obj" data-o="mother">'
              '<circle cx="412" cy="352" r="40" fill="url(#__U__lg)"/>'
              # 구유와 아기
              '<path d="M404 356 L440 356 L436 370 L408 370Z" fill="#8a6238"/><path d="M402 356 Q422 349 442 356" stroke="#e2c27a" stroke-width="3" fill="none"/>'
              '<ellipse cx="422" cy="352" rx="12" ry="5.2" fill="#f4ecdb"/><circle cx="432" cy="350.5" r="4" fill="#f0d6b4"/>'
              # 무릎 꿇은 성모(푸른 망토, 붉은 옷)
              + _kneel(383, 372, 58, '#a3393a', '#35558f', face_dir=1, hair='#3d2a1c') +
              '<circle cx="385.9" cy="320.5" r="9.5" fill="none" stroke="#e8c45e" stroke-width="1.2" opacity=".75"/>'
              '</g>')
    stand = ('<g class="obj" data-o="stand">'
             # 요셉(오두막 안 오른쪽)
             + _person(458, 372, 70, '#7a4f2c', mantle='#a8743a', staff='#9c7748', face_dir=-1, hair='#6b6157')
             # 목자 둘(왼쪽): 선 목자와 어린양을 안은 목자
             + _person(292, 374, 66, '#6e5d44', vest='#d9cdb3', staff='#8a6a43', face_dir=1)
             + _kneel(337, 375, 44, '#5a6b4a', None, lamb=True, face_dir=1, hair='#4a3423')
             # 왕 둘(오른쪽): 선물을 든 왕, 서 있는 왕
             + _kneel(505, 375, 50, '#8e2a3a', '#d7b456', gift=True, face_dir=-1, hair='#9a9a9a', crown=True)
             + _person(552, 376, 76, '#2f5a7a', mantle='#b58a2c', face_dir=-1, hair='#2c2219', crown=True)
             + '</g>')
    floating = ('<g class="obj" data-o="float">'
                + _angel(400, 150, 1.08, '#e9b23d', '#e46f63', flip=1)
                + _angel(330, 182, .78, '#f0c9b8', '#7fa6a0', flip=-1)
                + _angel(472, 176, .8, '#f3e3b0', '#c9827a', flip=1)
                + '</g>')
    # 뒷배경: 베수비오(몬테 솜마와 큰 원뿔), 연기, 바닷가 마을 불빛
    puffs = ''.join(f'<circle cx="{626 - k * 13 + R.uniform(-6, 6):.0f}" cy="{160 - k * 19:.0f}" r="{10 + k * 4.2:.0f}" fill="url(#__U__smk)"/>' for k in range(7))
    lights = ''.join(f'<circle cx="{xx:.0f}" cy="{R.uniform(266, 271):.1f}" r="{R.choice([.9, 1.1, 1.4]):.1f}" fill="#ffd38a" opacity="{R.uniform(.45, .9):.2f}"/>' for xx in [R.uniform(470, 780) for _ in range(26)])
    back = ('<g class="obj bk" data-o="back">'
            '<path d="M-10 270 L120 262 Q200 258 260 264 L340 270Z" fill="#34374f"/>'
            '<path d="M420 272 Q470 236 506 206 Q526 192 548 210 L566 220 Q590 186 606 170 L644 168 Q676 196 708 228 Q744 256 810 268 L810 276 L420 276Z" fill="url(#__U__mtn)"/>'
            '<path d="M506 206 Q526 192 548 210 L566 220" stroke="#7d7398" stroke-width="1.6" fill="none" opacity=".6"/>'
            '<path d="M606 170 L644 168" stroke="#a79bbd" stroke-width="2" opacity=".7"/>'
            '<path d="M644 168 Q676 196 708 228" stroke="#7d7398" stroke-width="1.4" fill="none" opacity=".5"/>'
            + puffs + lights +
            '</g>')
    style = '.pl .obj.bk{transform:none;transition:opacity 2.4s ease}'
    return f'''<svg class="stage" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" role="img" aria-label="나폴리 집의 평평한 지붕 위. 가벼운 오두막 틀을 늘푸른 나무와 덤불로 꾸미고, 그 아래 성모와 아기, 둘레에 선 목자와 왕들, 머리 위에 떠 있는 천사들을 놓으면, 지붕 너머 바다 건너로 베수비오 화산이 뒷배경으로 드러난다."><style>{style}</style><defs>
<linearGradient id="__U__sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#121a30"/><stop offset=".55" stop-color="#2b2d47"/><stop offset="1" stop-color="#4a3c4c"/></linearGradient>
<linearGradient id="__U__sky2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6a7fa8" stop-opacity=".0"/><stop offset=".45" stop-color="#c98f86" stop-opacity=".28"/><stop offset="1" stop-color="#f3b27a" stop-opacity=".78"/></linearGradient>
<linearGradient id="__U__sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#303a58"/><stop offset="1" stop-color="#1c2236"/></linearGradient>
<linearGradient id="__U__mtn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5b5577"/><stop offset="1" stop-color="#363a56"/></linearGradient>
<radialGradient id="__U__lg"><stop offset="0" stop-color="#ffe9b8" stop-opacity=".55"/><stop offset=".5" stop-color="#ffd58a" stop-opacity=".18"/><stop offset="1" stop-color="#ffc870" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__smk"><stop offset="0" stop-color="#d9d0cc" stop-opacity=".42"/><stop offset="1" stop-color="#d9d0cc" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__warm" cx=".5" cy=".6" r=".55"><stop offset="0" stop-color="#ffd59a" stop-opacity=".55"/><stop offset=".55" stop-color="#d98d4a" stop-opacity=".22"/><stop offset="1" stop-color="#3a1f0c" stop-opacity="0"/></radialGradient>
<radialGradient id="__U__day" cx=".72" cy=".55" r=".8"><stop offset="0" stop-color="#ffe2b0" stop-opacity=".3"/><stop offset=".5" stop-color="#ffbe86" stop-opacity=".18"/><stop offset="1" stop-color="#ff9f5a" stop-opacity="0"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#__U__sky)"/>{stars}
<rect class="sky2" width="{W}" height="300" fill="url(#__U__sky2)"/>
{back}
<rect x="0" y="266" width="{W}" height="90" fill="url(#__U__sea)"/>
<path d="M0 282 L800 282 M60 296 L740 296" stroke="#4a5677" stroke-width="1" opacity=".35"/>
{dome}{tower}{roofs}
<rect x="0" y="334" width="{W}" height="30" fill="#8d6c52"/><rect x="0" y="329" width="{W}" height="7" fill="#a8866b"/>
<rect x="0" y="364" width="{W}" height="86" fill="#6c5040"/>{tiles}{pots}
<ellipse class="glow" cx="400" cy="300" rx="270" ry="190" fill="url(#__U__warm)" opacity=".14"/>
<path d="M214 376 L586 376 L594 392 L206 392Z" fill="#7a573a"/><rect x="206" y="392" width="388" height="9" fill="#4f3624"/>
{hut}{green}{mother}{stand}{floating}
<rect class="day" width="{W}" height="{H}" fill="url(#__U__day)"/>
</svg>'''


GOETHE = 'https://projekt-gutenberg.org/authors/johann-wolfgang-von-goethe/books/johann-wolfgang-goethe-italienische-reise/chapter/55'
MIC = 'https://cultura.gov.it/luogo/certosa-e-museo-di-san-martino'
ICCD = 'https://catalogo.beniculturali.it/detail/HistoricOrArtisticProperty/1500323375'
MET_ANGEL = 'https://www.metmuseum.org/art/collection/search/204109'
MET_KING = 'https://www.metmuseum.org/art/collection/search/204184'
MET_MAN = 'https://www.metmuseum.org/art/collection/search/204180'
MET_ESSAY = 'https://www.metmuseum.org/art/collection/search/204205'
AGSA = 'https://www.agsa.sa.gov.au/collection-publications/collection/works/a-view-of-vesuvius-from-posillipo-naples/23807/'
CMS = 'https://commons.wikimedia.org/wiki/File:'

ITEMS = [
 {'id': 'hut', 't': '오두막 틀', 'la': 'ein leichtes hüttenartiges Gerüste', 'say': '평평한 지붕 위에 가벼운 오두막 틀을 세웠어요. 괴테가 맨 먼저 적은 것이에요.'},
 {'id': 'green', 't': '늘푸른 나무', 'la': 'immergrüne Bäume und Sträucher', 'say': '틀을 늘푸른 나무와 덤불로 꾸몄어요.'},
 {'id': 'mother', 't': '성모와 아기', 'la': 'die Mutter Gottes, das Kind', 'say': '오두막 아래 성모와 아기를 모셨어요. 값진 옷을 차려입혔어요.'},
 {'id': 'stand', 't': '둘레에 선 이들', 'la': 'die Umstehenden', 'say': '둘레에 선 이들을 세웠어요. 그림에서는 목자와 왕들이에요.'},
 {'id': 'float', 't': '둘레에 떠 있는 이들', 'la': 'die Umschwebenden', 'say': '둘레에 떠 있는 이들을 띄웠어요. 그림에서는 천사들이에요.'},
 {'id': 'back', 't': '뒷배경', 'la': 'der Hintergrund', 'say': '끝으로 뒷배경이에요. 지붕 너머 바다 건너로 베수비오와 그 둘레가 펼쳐져요.'},
]
ORDER = '오두막 틀 → 늘푸른 나무 → 성모와 아기 → 둘레에 선 이들 → 둘레에 떠 있는 이들 → 뒷배경'

CARD = {
 'id': 'cr-pastori', 'mode': '놓아 보기 · 두 그림 · 고르기',
 'pagetitle': '지붕 위의 구유',
 'brandsub': '깊은 카드 · 놓아 보기',
 'where': '<b>18세기 · 괴테의 기록은 1787년</b><span>이탈리아 나폴리</span>',
 'lead': '18세기 나폴리 사람들은 구유를 온 마을로 채웠어요. 철사와 나무와 구운 흙으로 만든 인형들이 값진 옷을 입고 베들레헴으로 모여들었지요. 1787년 괴테가 적은 차례대로, 나폴리 집의 평평한 지붕 위에 구유를 차려 보세요.',
 'leadKid': '나폴리 사람들은 옥상에도 구유를 차렸대. 우리도 지붕 위에 오두막을 세우고 천사를 띄워 볼까?',
 'meta': '영화처럼 약 4분 · 천천히 읽으면 6분',
 'draft': '검수 전 시안이에요(기준서 2판). 장면에는 기록에 있는 것만 옮겼어요. 지붕 위 구유 무대는 괴테의 글을 따라 이 안내서가 그린 그림이에요. 상상은 ‘눈 감고 상상해 보기’에만 썼어요.',
 'foot': '‘처음 만나는 기독교 문화’의 깊은 카드예요. 카드 단계와 남긴 글은 이 기기에만 저장돼요.',
 'filmlen': '영화처럼 보기 · 약 4분',
 # 화면 색: 나폴리 바다의 짙은 청록
 'theme': """:root{--accent:#2f5d6e;--accent-ink:#f6fbfc;--soft:rgba(47,93,110,.09);--stamp:#a8392b}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--accent:#93abb4;--accent-ink:#0f1719;--soft:rgba(147,171,180,.10);--stamp:#e46e5c}}
:root[data-theme="dark"]{--accent:#93abb4;--accent-ink:#0f1719;--soft:rgba(147,171,180,.10);--stamp:#e46e5c}""",
 'stamp': {'t': '지붕 위', 'y': '1787', 'sub': '나폴리 · 괴테의 기록'},
 'doneNote': '나폴리 구유를 만나면, 인형들 뒤로 펼쳐진 뒷배경을 찾아보세요.',
 'images': {
  # 'card'는 사이트 앞면 그림 그대로예요(카드 앞면에만 나와요). 요즘 만든 인형일 수 있어서 장면·영화에는 18세기 인형을 썼어요(본부 소식 8번).
  'crowd': {'src': S + 'Cuciniello_San_Martino_17.jpg', 'cap': '쿠치니엘로 구유의 마을 사람들 · 나폴리 산 마르티노 박물관',
            'cr': '사진: Miguel Hermoso Cuesta · CC BY-SA 4.0 · 위키미디어 공용', 'u': CMS + 'Cuciniello_San_Martino_17.JPG',
            'alt': '어두운 바위 앞에 옛 옷을 입은 인형들이 모여 있다. 여인들이 과일과 채소를 담은 바구니를 들었고, 아이 둘도 작은 바구니를 들었다. 뒤로 지팡이를 짚은 남자와 모자를 쓴 남자가 서 있고, 오른쪽 아래에는 붉은 옷을 입은 여인이 앉아 있다.'},
  'magi': {'src': S + 'Cuciniello_San_Martino_11.jpg', 'cap': '쿠치니엘로 구유의 동방박사 행렬',
           'cr': '사진: Miguel Hermoso Cuesta · CC BY-SA 4.0 · 위키미디어 공용', 'u': CMS + 'Cuciniello_San_Martino_11.JPG',
           'alt': '바위 언덕 위, 금빛 술이 달린 차양 아래 화려한 옷의 인형이 앉아 있다. 둘레에 터번을 쓴 악사와 시종들이 서 있고, 오른쪽에서는 한 사람이 하얀 짐 꾸러미를 실은 낙타를 끌고 온다.'},
  'gold': {'src': S + 'Cuciniello_San_Martino_06.jpg', 'cap': '동방박사의 시종들과 금빛 상자 · 쿠치니엘로 구유',
           'cr': '사진: Miguel Hermoso Cuesta · CC BY-SA 4.0 · 위키미디어 공용', 'u': CMS + 'Cuciniello_San_Martino_06.JPG',
           'alt': '터번을 쓰고 붉은 조끼를 입은 악사들이 나팔과 뿔피리를 분다. 위쪽 바위에는 금빛으로 꾸민 상자 세 개가 놓여 있고, 그 곁에 작은 원숭이를 데린 인형이 서 있다.'},
  'angel': {'src': S + 'Angel_MET_DP257979.jpg', 'cap': '천사 · 주세페 산마르티노 · 18세기 후반 · 메트로폴리탄 미술관',
            'cr': '사진: 메트로폴리탄 미술관 · CC0 · 위키미디어 공용', 'u': CMS + 'Angel_MET_DP257979.jpg',
            'alt': '회색 바탕 앞에 떠 있는 천사 인형. 금빛 갈색 날개를 펴고, 노란 비단 옷 위에 붉은 분홍빛 겉옷을 걸쳤다. 한 손에 쇠사슬이 달린 금빛 향로를 들었고, 옷자락 아래로 맨발이 보인다.'},
  'woman': {'src': S + 'Peasant_woman_MET_182694.jpg', 'cap': '시골 아낙 · 18세기 후반 · 메트로폴리탄 미술관',
            'cr': '사진: 메트로폴리탄 미술관 · CC0 · 위키미디어 공용', 'u': CMS + 'Peasant_woman_MET_182694.jpg',
            'alt': '흑백 사진. 머릿수건을 두른 여인 인형이 한 팔에 과일 바구니를 걸고, 다른 손을 앞으로 내민다. 발치에 포도와 과일, 채소를 가득 담은 바구니 네 개가 놓여 있다.'},
  'king': {'src': S + 'Elderly_king_MET_DP101478.jpg', 'crop': (0.04, 0.03, 0.97, 0.7), 'cap': '늙은 왕 · 18세기 후반 · 메트로폴리탄 미술관',
           'cr': '사진: 메트로폴리탄 미술관 · CC0 · 위키미디어 공용 · 일부 잘라 씀', 'u': CMS + 'Elderly_king_MET_DP101478.jpg',
           'alt': '검은 바탕 앞, 앞발을 든 검은 말에 탄 늙은 왕 인형. 진주를 두른 하얀 관 위에 금관을 썼고, 금실로 수놓은 크림색 겉옷과 붉은 소매를 입었다. 회색 수염이 나 있고, 한 손을 앞으로 들었다.'},
  'vesuvio': {'src': S + 'Joseph_WRIGHT_of_Derby_-_A_view_of_Vesuvius_from_Posillipo_Naples_-_Google_Art_P.jpg',
              'cap': '포실리포에서 본 베수비오 · 조지프 라이트 · 1788~1790년쯤 · 사우스오스트레일리아 미술관',
              'cr': '그림: 조지프 라이트 · 퍼블릭 도메인 · 위키미디어 공용', 'u': CMS + 'Joseph_WRIGHT_of_Derby_-_A_view_of_Vesuvius_from_Posillipo,_Naples_-_Google_Art_Project.jpg',
              'alt': '달밤의 바닷가. 왼쪽 언덕에 하얀 집들이 서 있고 달빛이 물 위에 비친다. 오른쪽 멀리 베수비오 화산이 붉게 타오르며 하늘을 분홍빛으로 물들이고, 물 위에 돛단배가 떠 있다.'},
 },
 'scenes': [
  {'id': 'crowd', 'label': '온 마을이 모여드는 구유', 'kind': 'photo', 'img': 'crowd',
   'text': ['나폴리 구유 인형은 이탈리아 말로 ‘파스토리’라고 해요. 본디 ‘목자들’이라는 뜻이에요. 그런데 목자가 아닌 인형도 모두 이렇게 불러요.',
            '뉴욕 메트로폴리탄 미술관은 18세기 나폴리 구유가 세 장면으로 이루어진다고 설명해요. 첫째는 아기가 태어난 자리예요. 천사와 목자와 양이 함께 있어요.',
            '둘째는 동방박사 세 사람의 행렬이에요. 화려한 옷을 입은 시종들이 길게 뒤따라요. 셋째는 베들레헴 여관 앞에 몰려든 시골 사람과 도시 사람들이에요.'],
   'text2': ['그 여관은 성경에 나오는 곳이에요. 그 밤 마리아와 요셉이 머물 자리가 없었던 곳이지요(' + bl('LUK.2', '누가복음 2장 7절') + ').',
             '사진은 나폴리 산 마르티노 박물관의 ‘쿠치니엘로 구유’예요. 수집가 미켈레 쿠치니엘로가 인형과 동물과 소품 800점쯤을 나라에 기증했어요. 그는 구유를 차리고 세우는 일을 손수 챙겼고, 구유는 1879년에 문을 열었어요.'],
   'kid': '구유에 온 마을 사람들이 모였어. 바구니도 들고 왔네!',
   'kidq': '바구니에 무엇을 담아 왔을까?'},
  {'id': 'make', 'label': '철사와 나무와 구운 흙', 'kind': 'duo', 'imgs': ['angel', 'woman'],
   'caps': ['천사 · 주세페 산마르티노 · 18세기 후반', '시골 아낙 · 18세기 후반'],
   'text': ['메트로폴리탄 미술관에는 1964년 로레타 하인스 하워드가 기증한 18세기 나폴리 구유 인형이 140점 넘게 있어요.',
            '인형의 몸은 철사에 거친 삼 섬유를 감아 만들었어요. 팔다리는 나무로 곱게 깎고, 머리와 어깨는 테라코타로 빚었어요. 테라코타는 흙을 빚어 구운 것이에요.',
            '미술관은 몸이 철사라서 얼굴 표정에 맞게 몸짓을 마음대로 줄 수 있다고 설명해요. 키는 대개 30~38cm예요. 30cm 자 하나쯤이지요. 무대 앞에 설지 멀리 설지에 따라 크기를 달리했대요.'],
   'text2': ['왼쪽 천사는 미술관이 나폴리의 조각가 주세페 산마르티노(1720~1793)가 만든 것으로 적은 인형이에요. 나무로 깎은 날개를 달고 향로를 들었어요. 오른쪽 시골 아낙은 과일과 채소 바구니를 늘어놓았어요.'],
   'kid': '인형 몸 안에는 철사가 들어 있대. 그래서 팔다리를 구부릴 수 있어.',
   'kidq': '너라면 이 인형에게 어떤 몸짓을 시킬래?'},
  {'id': 'magi', 'label': '동방박사의 긴 행렬', 'kind': 'photo', 'img': 'magi',
   'text': ['나폴리 구유에서 가장 화려한 무리는 동방박사의 행렬이에요. 성경은 동방에서 온 박사들이 별을 따라 아기를 찾아왔다고 전해요(' + bl('MAT.2', '마태복음 2장') + ').',
            '나폴리 사람들은 그 먼 길을 긴 행렬로 꾸몄어요. 사진 속 행렬에는 터번을 쓴 악사들과 짐을 실은 낙타가 보여요.'],
   'text2': ['메트로폴리탄 미술관의 ‘늙은 왕’ 인형은 비단과 새틴 옷에 금실과 은실을 둘렀어요. 유리 단추를 달고, 은에 금을 입힌 칼과 왕관을 지녔어요. 새틴은 윤이 나게 짠 비단이에요.'],
   'kid': '박사님들이 낙타랑 악사들이랑 줄지어 오고 있어!',
   'kidq': '행렬 맨 앞에서는 무슨 소리가 날까?'},
  {'id': 'roof', 'label': '지붕 위의 구유', 'kind': 'mod', 'mod': 'place',   # ← 그 자리에 있고 싶은 한 순간(한가운데 장면)
   'text': ['독일 시인 괴테(Goethe)는 1787년 봄 나폴리에 머물렀어요. 그해 5월 27일에 쓴 글에 나폴리 사람들이 아끼는 구유가 나와요.',
            '성탄이면 어느 성당에서나 구유를 볼 수 있대요. 목자와 천사와 왕들이 아기에게 경배하는 모습을 값지게 꾸민 구유예요.',
            '밝은 도시 나폴리에서는 이 구유가 집의 평평한 지붕 위까지 올라갔다고 괴테는 적었어요. 괴테가 적은 차례대로 지붕 위에 구유를 차려 보세요.'],
   'quote': {'t': '그러나 이 모든 것을 흉내 낼 수 없이 빛나게 하는 것은 뒷배경, 베수비오와 그 둘레를 품은 뒷배경이다.',
             'from': '괴테, 『이탈리아 기행』 1787년 5월 27일 나폴리 · 독일어를 이 안내서가 옮김', 'u': GOETHE},
   'text2': ['괴테는 성모와 아기와 둘레의 모든 이들을 값지게 차려입혔다고 적었어요. 그 옷에 집안이 큰돈을 썼대요.',
             '무대 그림은 괴테의 글을 따라 이 안내서가 그렸어요. 괴테는 ‘둘레에 선 이들’과 ‘둘레에 떠 있는 이들’이라고만 적었어요. 그림에서는 선 이들을 목자와 왕으로, 떠 있는 이들을 천사로 그렸어요.'],
   'choose': True,
   'kid': '나폴리 사람들은 옥상에도 구유를 차렸대!',
   'kidq': '천사들은 어떻게 하늘에 떠 있을까?'},
 ],
 'imagine': {'t': '좁은 계단을 올라 평평한 지붕에 서요. 늘푸른 가지 냄새가 나고, 비단옷 자락이 바람에 사락거려요. 지붕 너머 바다 건너로 베수비오가 희미한 연기를 올려요. 아래 골목에서는 성탄을 앞둔 사람들 소리가 올라와요.',
             'kid': '눈을 감아 봐. 옥상에 올라왔어. 초록 가지 냄새가 나. 멀리 바다 건너에서 화산이 연기를 뿜어.'},
 'lines': ['지붕 위까지 올라간 베들레헴.', '흉내 낼 수 없는 뒷배경, 베수비오.', '철사와 나무와 구운 흙으로 빚은 마을 사람들.', '여관에 자리가 없던 그 밤, 온 마을이 모여들었어요.'],
 'linesKid': ['옥상에도 구유가 있대!', '인형 몸 안에 철사가 있어.', '뒤에는 커다란 화산!'],
 'close': {'form': '기록 한 마디',
           'from': '괴테 『이탈리아 기행』 1787년 5월 27일 나폴리 — 지붕 위 구유를 “흉내 낼 수 없이 빛나게 하는 것은 베수비오와 그 둘레를 품은 뒷배경”이라는 한 줄(한가운데 장면인 지붕 위 무대의 마지막 물건)',
           'ask': '내가 사는 곳의 지붕 위에 구유를 차린다면, 뒷배경에는 무엇이 들어올까요?',
           'askKid': '우리 집 옥상에 구유를 놓으면, 뒤에 무엇이 보일까?'},
 'goals': {
  's4': {'t': '괴테가 적은 차례대로', 'p': '괴테가 적은 차례(' + ORDER + ')대로 지붕 위에 구유를 차리면 카드에 금박이 입혀져요.',
         'how': '괴테가 적은 차례대로 지붕 위에 구유를 차려 보세요', 'done': '괴테가 적은 차례대로 지붕 위 구유를 차렸어요',
         'ways': [{'id': 'plOrder', 't': ORDER}]},
  's5': {'t': '1787년 나폴리 집의 옷장', 'p': '둘 가운데 하나만 해도 카드가 채색돼요.',
         'how': '1787년 나폴리 집이라면 누구의 옷에 공을 들일지 고르거나, 아이와 함께 끝까지 보세요', 'done': '지붕 위 구유의 옷을 골랐어요',
         'ways': [{'id': 'choose', 't': '1787년 나폴리 집이라면, 누구의 옷에 가장 공을 들일지 고르기'},
                  {'id': 'kid', 't': '아이와 함께 ‘영화처럼 보기’를 끝까지 보기', 'hint': '‘아이와 함께’를 켜고 ‘영화처럼 보기’를 끝까지 보세요', 'okt': '아이와 함께 끝까지 봤어요'}]},
 },
 'mods': {
  'place': {
   'items': ITEMS, 'order': ORDER,
   'intro': '아래에서 하나를 골라 지붕 위에 놓아 보세요. 괴테는 오두막 틀부터 적고, 뒷배경을 맨 끝에 적었어요.',
   'climax': '하늘이 밝아지며 베수비오가 구유를 품었어요. 괴테가 맨 끝에 적은 뒷배경이에요.<span class="la">der Vesuv mit seinen Umgebungen · 베수비오와 그 둘레</span>',
   'home': None,
   'wrongOrder': '괴테의 글에 적힌 차례는 이래요: {order}',
   'orderDone': '괴테가 적은 차례대로 지붕 위 구유를 차렸어요',
   'daylight': False,
   'svg': stage_svg()},
  'choose': {
   'q': '1787년 나폴리, 지붕 위에 구유를 차리는 집이라면 누구의 옷에 가장 공을 들일까요?',
   'opts': [{'t': '성모와 아기', 'r': '괴테는 성모와 아기와 둘레의 모든 이들을 값지게 차려입혔고, 그 옷에 집안이 큰돈을 썼다고 적었어요.'},
            {'t': '동방박사', 'r': '메트로폴리탄 미술관의 늙은 왕은 비단과 새틴 옷에 금실과 은실을 둘렀고, 은에 금을 입힌 칼과 왕관을 지녔어요.'},
            {'t': '천사', 'r': '메트로폴리탄 미술관의 천사들은 나무로 깎은 날개를 달고, 여러 가지 천으로 지은 옷을 입었어요.'},
            {'t': '마을 사람', 'r': '메트로폴리탄 미술관의 한 남자 인형은 여러 가지 천으로 지은 옷에 금실을 두르고 은단추를 달았어요.'}]},
 },
 'modhtml': {'place': '''<div class="mod" data-mod="place"><div class="pl">
  <div class="pl-stage"></div>
  <div class="pl-tray" role="group" aria-label="놓을 것 고르기"></div>
  <p class="pl-say" aria-live="polite"></p>
  <div class="pl-row" hidden><button type="button" class="pl-again">처음부터 다시 놓아 보기</button></div>
  <div class="pl-home" hidden><p></p><div class="ch"></div><p class="got" aria-live="polite"></p></div>
</div></div>'''},
 'deep': [
  {'h': '알고 보면', 'p': [
    '<b>파스토레와 파스토리</b> 구유 인형 하나는 ‘파스토레’, 여럿은 ‘파스토리’예요. 이탈리아 국가 문화재 목록은 산 마르티노 박물관의 한 인형(1780~1825년쯤)을 ‘도시 사람을 나타낸 구유의 파스토레’라고 적었어요. 목자가 아니어도 구유 인형이면 파스토레예요.',
    '<b>살아 있는 사람</b> 괴테는 지붕 위 구유의 인형들 사이에 때로 살아 있는 사람이 끼어들었다고도 적었어요. 이것이 점점 부잣집의 큰 즐거움이 되었대요. 저녁이면 궁전에서 역사나 시 속의 장면을 사람이 직접 꾸며 보였다고 해요.',
    '<b>미술관의 구유</b> 메트로폴리탄 미술관은 하워드의 기증 뒤로 성탄 철마다 이 인형들로 나폴리 구유를 다시 차려 왔다고 소개해요.']},
  {'h': '그림 속 베수비오', 'img': ['vesuvio'], 'p': [
    '영국 화가 조지프 라이트(1734~1797)는 1773년부터 1775년까지 이탈리아를 여행했어요. 1774년 나폴리 바닷가에서 본 베수비오에 크게 마음이 움직였대요.',
    '이 그림은 1788~1790년쯤 영국 더비에서 그렸어요. 라이트는 화산이 터지는 것을 직접 보지는 못했어요. 그 힘을 상상해서 그렸대요. 그는 평생 이 장면을 서른 번이나 다르게 그렸어요.',
    '괴테가 지붕 위 구유를 적은 지 한두 해 뒤에 그린 그림이에요.']},
  {'h': '기록마다 다른 점', 'p': [
    '<b>세 장면</b> 메트로폴리탄 미술관은 나폴리 구유의 세 장면을 ‘아기가 태어난 자리, 동방박사의 행렬, 여관 앞 사람들’로 설명해요. 산 마르티노 박물관을 맡은 이탈리아 문화부는 쿠치니엘로 구유의 세 장면을 ‘가운데의 탄생, 양옆의 목자들에게 알리는 장면과 여관’으로 소개해요.',
    '<b>누가 빚었나</b> 메트로폴리탄 미술관의 늙은 왕과 한 남자 인형에는 만든 이가 적혀 있지 않아요. 미술관은 몇몇 천사의 머리를 산마르티노와 그 제자들이 빚었다고 전해진다고 설명해요. 나폴리와 뮌헨에 있는 인형들과 솜씨를 견주어 보면 그 이야기가 맞아 보인다고 해요.']},
  {'h': '직접 가 보기', 'img': ['gold'], 'checked': '2026년 11월 18일', 'p': [
    '쿠치니엘로 구유는 나폴리 보메로 언덕의 산 마르티노 박물관에 있어요. 옛 수도원 건물이에요. 구유는 거짓 동굴 안에 차려 두었고, 불빛이 새벽과 한낮, 노을과 밤을 차례로 흉내 내요.',
    '박물관은 화요일만 쉬고 8시 30분부터 18시 30분까지 열어요(마지막 입장 17시 30분). 구유 전시실은 9시 30분에 열어요. 입장료는 6유로, 18~25세는 2유로, 18세 아래는 무료예요.'],
   'links': [{'t': '이탈리아 문화부: 산 마르티노 수도원과 박물관(쿠치니엘로 구유)', 'u': MIC, 'm': '이탈리아어'},
             {'t': '괴테 『이탈리아 기행』 1787년 5월 나폴리 편 원문', 'u': GOETHE, 'm': '독일어'},
             {'t': '사우스오스트레일리아 미술관: 라이트의 ‘포실리포에서 본 베수비오’', 'u': AGSA, 'm': '영어'}]},
 ],
 'src': [
  {'l': '괴테, 『이탈리아 기행』 1787년 5월 27일 나폴리(프로젝트 구텐베르크 독일어판) — 성당의 구유, 평평한 지붕 위 구유의 차례(오두막 틀·늘푸른 나무와 덤불·성모와 아기·둘레에 선 이들과 떠 있는 이들·베수비오를 품은 뒷배경), 옷에 쓴 큰돈, 살아 있는 사람', 'u': GOETHE},
  {'l': '이탈리아 문화부: 산 마르티노 수도원과 박물관 — 쿠치니엘로가 기증한 800점쯤, 손수 챙긴 차림, 1879년, 가운데의 탄생과 양옆의 두 장면, 거짓 동굴과 불빛, 여는 때와 입장료(2026년 11월 18일 확인)', 'u': MIC},
  {'l': '이탈리아 국가 문화재 목록: ‘도시 사람을 나타낸 구유의 파스토레’(나폴리 공방, 1780~1825년쯤, 산 마르티노 박물관)', 'u': ICCD},
  {'l': '메트로폴리탄 미술관 소장품 설명(하워드 기증 나폴리 구유 인형) — 1964년 140점 넘게, 세 장면, 30~38cm와 무대 속 자리, 철사·삼 섬유 몸과 나무 팔다리와 테라코타 머리, 산마르티노와 제자들', 'u': MET_ESSAY},
  {'l': '메트로폴리탄 미술관 ‘천사’(64.164.8, 주세페 산마르티노, 43.8cm, 테라코타 머리·나무 팔다리와 날개·삼 섬유를 감은 철사 몸)', 'u': MET_ANGEL},
  {'l': '메트로폴리탄 미술관 ‘늙은 왕’(64.164.83, 비단과 새틴 옷·금실과 은실·유리 단추·은에 금을 입힌 칼과 왕관, 만든 이 적히지 않음)', 'u': MET_KING},
  {'l': '메트로폴리탄 미술관 ‘남자’(64.164.79, 여러 가지 천·금실·은단추, 만든 이 적히지 않음)', 'u': MET_MAN},
  {'l': '사우스오스트레일리아 미술관: 조지프 라이트 ‘포실리포에서 본 베수비오’ — 1788~1790년쯤 더비, 1773~1775년 이탈리아 여행, 1774년 나폴리, 분화를 직접 보지 못함, 서른 가지 그림', 'u': AGSA},
 ],
 'film': [
  {'type': 'open', 'ch': 0, 'img': 'crowd', 'fit': 'cover', 'p0': '40% 40%', 'p1': '55% 52%', 's0': 1.28, 's1': 1.06, 'kicker': '18세기 · 이탈리아 나폴리', 'title': '지붕 위의 구유',
   'lines': [{'t': '18세기 나폴리 사람들은 구유를 온 마을로 채웠어요.'}, {'t': '값진 옷을 입은 인형들이 베들레헴으로 모여들었어요.'}],
   'kid': [{'t': '나폴리 사람들은 구유에 온 마을 사람들을 세웠대.'}, {'t': '다들 멋진 옷을 입었어!'}]},
  {'type': 'chapter', 'ch': 1, 'no': 1, 't': '온 마을이 모여드는 구유'},
  {'type': 'img', 'ch': 1, 'img': 'crowd', 'fit': 'cover', 'p0': '30% 45%', 'p1': '62% 50%', 's0': 1.35, 's1': 1.12, 'cap': '쿠치니엘로 구유의 마을 사람들',
   'lines': [{'t': '이 인형들을 ‘파스토리’라고 불러요. 본디 ‘목자들’이라는 뜻이에요.'},
             {'t': '아기가 태어난 자리, 동방박사의 행렬, 여관 앞 사람들.'},
             {'t': '그 밤, 마리아와 요셉이 머물 자리가 없던 여관이에요.'}],
   'kid': [{'t': '이 인형들 이름은 ‘파스토리’야. 목자들이라는 뜻이래.'}, {'t': '바구니에 무엇을 담아 왔을까?', 'ask': True}]},
  {'type': 'chapter', 'ch': 2, 'no': 2, 't': '철사와 나무와 구운 흙'},
  {'type': 'img', 'ch': 2, 'img': 'angel', 'fit': 'cover', 'p0': '50% 30%', 'p1': '50% 55%', 's0': 1.25, 's1': 1.04, 'cap': '천사 · 주세페 산마르티노 · 18세기 후반',
   'lines': [{'t': '몸은 철사에 삼 섬유를 감고, 팔다리는 나무로 깎았어요.'},
             {'t': '머리와 어깨는 흙으로 빚어 구운 테라코타예요.'},
             {'t': '철사 몸이라, 표정에 맞게 몸짓을 줄 수 있었어요.'}],
   'kid': [{'t': '인형 몸 안에 철사가 있대. 그래서 팔을 구부릴 수 있어.'}]},
  {'type': 'img', 'ch': 2, 'img': 'woman', 'fit': 'cover', 'p0': '50% 38%', 'p1': '50% 70%', 's0': 1.2, 's1': 1.04, 'cap': '시골 아낙 · 18세기 후반',
   'lines': [{'t': '키는 대개 30~38cm. 30cm 자 하나쯤이에요.'},
             {'t': '무대 앞에 설 인형은 크게, 멀리 설 인형은 작게 만들었대요.'}],
   'kid': [{'t': '이 아주머니는 과일 바구니를 늘어놓았어.'}, {'t': '너라면 이 인형에게 어떤 몸짓을 시킬래?', 'ask': True}]},
  {'type': 'chapter', 'ch': 3, 'no': 3, 't': '동방박사의 긴 행렬'},
  {'type': 'img', 'ch': 3, 'img': 'magi', 'fit': 'cover', 'p0': '30% 50%', 'p1': '70% 55%', 's0': 1.3, 's1': 1.1, 'cap': '쿠치니엘로 구유의 동방박사 행렬',
   'lines': [{'t': '가장 화려한 무리는 동방박사의 행렬이에요.'},
             {'t': '터번을 쓴 악사들과 짐을 실은 낙타가 뒤따라요.'}],
   'kid': [{'t': '박사님들이 낙타랑 악사들이랑 줄지어 와!'}, {'t': '행렬 맨 앞에서는 무슨 소리가 날까?', 'ask': True}]},
  {'type': 'img', 'ch': 3, 'img': 'king', 'fit': 'cover', 'p0': '40% 30%', 'p1': '45% 45%', 's0': 1.2, 's1': 1.04, 'cap': '늙은 왕 · 18세기 후반 · 메트로폴리탄 미술관',
   'lines': [{'t': '늙은 왕은 비단과 새틴 옷에 금실과 은실을 둘렀어요.'},
             {'t': '은에 금을 입힌 칼과 왕관도 지녔어요.'}],
   'kid': [{'t': '왕님은 금실로 수놓은 옷에 금관을 썼어.'}]},
  {'type': 'chapter', 'ch': 4, 'no': 4, 't': '지붕 위의 구유'},
  {'type': 'img', 'ch': 4, 'img': 'vesuvio', 'fit': 'cover', 'p0': '35% 50%', 'p1': '72% 55%', 's0': 1.25, 's1': 1.08, 'cap': '포실리포에서 본 베수비오 · 조지프 라이트, 1788~1790년쯤',
   'lines': [{'t': '1787년 5월, 괴테는 나폴리에서 이 도시의 구유를 적었어요.'},
             {'t': '나폴리에서는 구유가 집의 평평한 지붕 위까지 올라갔대요.'}],
   'kid': [{'t': '여기는 바닷가 도시 나폴리야. 멀리 화산이 보여.'}]},
  {'type': 'mod', 'mod': 'place', 'ch': 4,
   'lines': [{'t': '먼저 가벼운 오두막 틀을 세우고,', 'act': 'hut'},
             {'t': '늘푸른 나무와 덤불로 꾸며요.', 'act': 'green'},
             {'t': '성모와 아기,', 'act': 'mother'},
             {'t': '둘레에 선 이들,', 'act': 'stand'},
             {'t': '둘레에 떠 있는 이들.', 'act': 'float'},
             {'t': '그리고 맨 끝에 적은 뒷배경.', 'act': 'back', 'wait': 1800},
             {'t': '지붕 너머 베수비오가 구유를 품어요.', 'act': 'day', 'wait': 3000}],
   'kid': [{'t': '지붕 위에 오두막을 세워!', 'act': 'hut'}, {'t': '초록 나무도!', 'act': 'green'},
           {'t': '성모님과 아기 예수님.', 'act': 'mother'}, {'t': '목자들과 왕들!', 'act': 'stand'},
           {'t': '하늘에는 천사들!', 'act': 'float'}, {'t': '마지막으로 무엇을 놓을까?', 'ask': True},
           {'t': '커다란 화산, 베수비오!', 'act': 'back', 'wait': 1800}, {'t': '하늘이 환해져.', 'act': 'day', 'wait': 3000}]},
  {'type': 'imagine', 'ch': 5,
   'lines': [{'t': '좁은 계단을 올라 평평한 지붕에 서요.'}, {'t': '늘푸른 가지 냄새, 비단옷 자락이 바람에 사락거려요.'}, {'t': '바다 건너로 베수비오가 희미한 연기를 올려요.'}],
   'kid': [{'t': '눈을 감아 봐. 옥상에 올라왔어.'}, {'t': '초록 가지 냄새가 나.'}, {'t': '멀리 화산이 연기를 뿜어.'}]},
  {'type': 'quote', 'ch': 5, 'big': '그러나 이 모든 것을 흉내 낼 수 없이 빛나게 하는 것은 뒷배경, 베수비오와 그 둘레를 품은 뒷배경이다.',
   'lines': [{'t': '괴테, 『이탈리아 기행』 · 1787년 5월 27일 나폴리'}],
   'kid': [{'t': '괴테 아저씨는 이렇게 썼어.'}, {'t': '나폴리 구유가 제일 멋진 건, 뒤에 보이는 화산 덕분이래.'}]},
  {'type': 'reward', 'ch': 5},
 ],
}
