# 홈 화면 아이콘, 브라우저 탭 아이콘, 링크 미리보기 그림 만들기
#  - 결과: site/brand/ (build_site.py가 홈페이지 폴더로 옮겨요)
#  - 아이콘은 오늘의 카드 뒷면(청금색 바탕에 금빛 마름모와 십자)을 그대로 썼어요.
#  - 미리보기 그림의 카드 세 장은 모두 저작권이 끝난 그림이에요(켈스의 서, 루블료프 「삼위일체」, 보베 미사경본 낱장).
import os, sys, base64, asyncio
from playwright.async_api import async_playwright

SITE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SITE, 'brand')
IMG = os.path.join(SITE, 'repo', 'site', 'img', 'c')
os.makedirs(OUT, exist_ok=True)

FAV = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2D4893"/><stop offset="1" stop-color="#18265A"/></linearGradient></defs><rect width="64" height="64" rx="13" fill="url(#g)"/><path d="M32 9.5L54.5 32 32 54.5 9.5 32z" fill="none" stroke="#EBCB7E" stroke-width="3.4" stroke-linejoin="round"/><path d="M32 22v20M22 32h20" stroke="#EBCB7E" stroke-width="3.6" stroke-linecap="round"/></svg>'''

# 홈 화면용(가장자리까지 꽉 찬 사각형, 무늬는 가운데 60% 안에)
APP = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2D4893"/><stop offset="1" stop-color="#17245A"/></linearGradient><radialGradient id="r" cx="50%" cy="48%" r="42%"><stop offset="0" stop-color="#EBCB7E" stop-opacity=".30"/><stop offset="1" stop-color="#EBCB7E" stop-opacity="0"/></radialGradient></defs><rect width="512" height="512" fill="url(#g)"/><rect width="512" height="512" fill="url(#r)"/><path d="M256 110L402 256 256 402 110 256z" fill="none" stroke="#EBCB7E" stroke-width="11" stroke-linejoin="round"/><path d="M256 168L344 256 256 344 168 256z" fill="none" stroke="#EBCB7E" stroke-width="5" stroke-linejoin="round" opacity=".7"/><path d="M256 196v120M196 256h120" stroke="#EBCB7E" stroke-width="12" stroke-linecap="round"/></svg>'''

def b64(p):
    return 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def card(cid, rot, x, y, w, mat):
    return f'''<div class="cd" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg)"><div class="mat {mat}"><img src="{b64(os.path.join(IMG, cid + '.webp'))}"></div></div>'''

OG = f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0}}
.og{{position:relative;width:1200px;height:600px;overflow:hidden;background:radial-gradient(circle at 74% 46%,rgba(235,203,126,.22),transparent 46%),linear-gradient(150deg,#2B4590,#152257);font-family:"Noto Serif CJK KR","Noto Serif KR",serif}}
.rib{{position:absolute;left:92px;top:0;width:26px;height:132px;background:linear-gradient(90deg,#2F6E50,#24583F);clip-path:polygon(0 0,100% 0,100% 100%,50% 86%,0 100%)}}
.t{{position:absolute;left:92px;top:186px;color:#EFE6D2}}
.t .a{{display:block;font-size:38px;font-weight:700;letter-spacing:.02em;opacity:.92}}
.t .b{{display:block;margin-top:6px;font-size:92px;font-weight:700;line-height:1.1;color:#EBCB7E}}
.t .c{{display:block;margin-top:26px;font-size:30px;font-weight:400;opacity:.86}}
.cd{{position:absolute;aspect-ratio:3/4;border-radius:18px;box-shadow:0 30px 50px -24px rgba(0,0,0,.65),0 4px 10px -4px rgba(0,0,0,.4)}}
.mat{{position:absolute;inset:0;border-radius:18px;padding:12px;box-sizing:border-box}}
.mat.p{{background:linear-gradient(160deg,#F3E6C6,#D8BE86)}}
.mat.g{{background:linear-gradient(150deg,#F6DE9A,#C9A24A 55%,#9C7426)}}
.mat img{{display:block;width:100%;height:100%;object-fit:cover;border-radius:10px}}
</style></head><body><div class="og" id="og"><div class="rib"></div>
<div class="t"><span class="a">처음 만나는</span><span class="b">기독교 문화</span><span class="c">하루 한 편의 이야기, 한 장의 카드</span></div>
{card('il-kells', -9, 688, 120, 236, 'p')}{card('keep-ege', 8, 930, 132, 236, 'p')}{card('orth-trinity', -1, 800, 80, 262, 'g')}
</div></body></html>'''

async def main():
    open(os.path.join(OUT, 'icon.svg'), 'w').write(FAV)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1200, 'height': 600}, device_scale_factor=1)
        await pg.set_content(OG); await pg.wait_for_timeout(600)
        await pg.locator('#og').screenshot(path=os.path.join(OUT, 'og.png'))
        for name, svg, size in (('icon-512.png', APP, 512), ('icon-192.png', APP, 192), ('apple-touch-icon.png', APP, 180), ('icon-32.png', FAV, 32)):
            await pg.set_viewport_size({'width': size, 'height': size})
            await pg.set_content(f'<html><body style="margin:0;background:transparent"><div id="i" style="width:{size}px;height:{size}px">{svg.replace("<svg ", f"<svg width={size} height={size} ")}</div></body></html>')
            await pg.wait_for_timeout(100)
            await pg.locator('#i').screenshot(path=os.path.join(OUT, name), omit_background=True)
        await b.close()
    print('ok', sorted(os.listdir(OUT)))

asyncio.run(main())
