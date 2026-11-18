# -*- coding: utf-8 -*-
"""키트 3판 예시: 만드는 차례(steps)의 단계 그림을 SVG로 그리는 법 — 이 안내서가 그린 피산카 단계 그림.
이 파일은 cards/ 폴더에 넣지 않아요. 카드에서는 이 함수처럼 그림 문자열을 만들어 'mods'→'steps'→'svg'에 넣어요.
 data-s="n": n단계에 나타남, data-off="n": n단계에 사라짐.
층(아래→위): 흰 달걀 → 염료(노랑 2·빨강 4·검정 6, 아래부터 차오름) → 지켜 둔 색(빨강 5·노랑 3·흰 선 1)
→ 반쯤 비치는 밀랍(1·3·5단계에 바르고 7단계에 닦임) → 빛.
밀랍 밑에 지켜 둔 색이 그 뒤의 염료 위에 그대로 남아 비쳐 보이게 해서, ‘밀랍이 물감을 막는다’가 눈에 보여요."""
import math
EGG = "M150 40 C 214 40 254 150 254 212 C 254 278 208 322 150 322 C 92 322 46 278 46 212 C 46 150 86 40 150 40 Z"
WHITE, YELLOW, RED, BLACK = '#fbf7ee', '#f0bd2c', '#c4302a', '#1e1814'
WAX = 'rgba(58,36,16,.58)'
def up(x): t = (x - 40) / 220; return 196 + 52 * t * (1 - t)
def lo(x): t = (x - 40) / 220; return 214 + 52 * t * (1 - t)
def star(cx, cy, R, r, n=8):
    pts = []
    for k in range(2 * n):
        a = -math.pi / 2 + math.pi * k / n; rr = R if k % 2 == 0 else r
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return ' '.join(pts)
def geo():
    """세 가지 지킬 모양: 흰 선(선), 노란 별·점(면), 빨간 톱니 띠·동그라미(면)."""
    S = star(150, 120, 48, 20)
    belt = '<path d="M40 196 Q150 222 260 196"/><path d="M40 214 Q150 240 260 214"/>'
    wave = 'M46 268 ' + ' '.join(f'Q{x + 13:.0f} {250 if (i % 2 == 0) else 286} {x + 26:.0f} 268' for i, x in enumerate(range(46, 254, 26)))
    lines = f'{belt}<polygon points="{S}"/><circle cx="150" cy="120" r="8"/><path d="{wave}"/>'
    dots = ''.join(f'<circle cx="{150 + 64 * math.cos(math.pi / 8 + math.pi * k / 4):.1f}" cy="{120 + 64 * math.sin(math.pi / 8 + math.pi * k / 4):.1f}" r="5"/>' for k in range(8))
    dots += ''.join(f'<circle cx="{x + 13:.0f}" cy="{291 if (i % 2 == 0) else 245}" r="4.5"/>' for i, x in enumerate(range(46, 254, 26)))
    yellow = f'<polygon points="{S}"/>{dots}'
    tri = ''.join(f'<polygon points="{x:.1f},{lo(x):.1f} {x + 9:.1f},{up(x + 9) + 1:.1f} {x + 18:.1f},{lo(x + 18):.1f}"/>' for x in range(40, 260, 18))
    red = f'{tri}<circle cx="118" cy="306" r="5"/><circle cx="150" cy="311" r="5"/><circle cx="182" cy="306" r="5"/>'
    return lines, yellow, red
LINE = 'fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="4"'
def svg(final=False, uid='py'):
    lines, yellow, red = geo()
    kept = (f'<g fill="{RED}">{red}</g><g fill="{YELLOW}">{yellow}</g><g {LINE} stroke="{WHITE}">{lines}</g>')
    s = (f'<svg viewBox="0 0 300 360" xmlns="http://www.w3.org/2000/svg">'
         f'<defs><clipPath id="{uid}C"><path d="{EGG}"/></clipPath>'
         f'<radialGradient id="{uid}H" cx=".36" cy=".28" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".5"/><stop offset=".42" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".32"/></radialGradient></defs>'
         f'<ellipse cx="150" cy="334" rx="90" ry="10" fill="rgba(70,48,14,.2)"/>'
         f'<g clip-path="url(#{uid}C)"><rect width="300" height="360" fill="#f8f2e4"/>')
    if final:
        s += f'<rect width="300" height="360" fill="{BLACK}"/>' + kept
    else:
        s += (f'<rect class="dye" data-s="2" width="300" height="360" fill="{YELLOW}"/>'
              f'<rect class="dye" data-s="4" width="300" height="360" fill="{RED}"/>'
              f'<rect class="dye" data-s="6" width="300" height="360" fill="{BLACK}"/>'
              # 지켜 둔 색: 밀랍을 바른 그 단계부터 그 뒤 염료 위에 남아요(먼저 지킨 색이 위)
              f'<g data-s="5" fill="{RED}">{red}</g><g data-s="3" fill="{YELLOW}">{yellow}</g><g data-s="1" {LINE} stroke="{WHITE}">{lines}</g>'
              # 반쯤 비치는 밀랍: 밑에 지켜 둔 색이 비쳐 보여요
              f'<g data-s="1" data-off="7" {LINE} stroke="{WAX}">{lines}</g>'
              f'<g data-s="3" data-off="7" fill="{WAX}">{yellow}</g>'
              f'<g data-s="5" data-off="7" fill="{WAX}">{red}</g>')
    s += f'</g><path d="{EGG}" fill="url(#{uid}H)"/><path d="{EGG}" fill="none" stroke="rgba(70,50,20,.38)" stroke-width="1.5"/></svg>'
    return s
if __name__ == '__main__':
    open('pysanka_final.svg', 'w').write(svg(True, 'pf'))   # 다 만든 모습(앞면·영화용)
    open('pysanka_steps.svg', 'w').write(svg(False))        # 단계 그림('svg'에 넣는 것)
    print('ok')
