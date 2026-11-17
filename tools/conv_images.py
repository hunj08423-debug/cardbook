# 카드 대표 사진 477장을 WebP로 줄여 site/out/img/c/<카드id>.webp 로 저장
import json, os, sys
from PIL import Image
from concurrent.futures import ProcessPoolExecutor
D = json.load(open('out/sets_all.json', encoding='utf-8'))
OUT = 'site/out/img/c'
MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
Q = int(sys.argv[2]) if len(sys.argv) > 2 else 74
def one(c):
    src, dst = c['img'], os.path.join(OUT, c['id'] + '.webp')
    if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src): return (c['id'], os.path.getsize(dst), 'skip')
    im = Image.open(src)
    if im.mode not in ('RGB', 'L'): im = im.convert('RGB')
    im.thumbnail((MAX, MAX), Image.LANCZOS)
    im.save(dst, 'WEBP', quality=Q, method=6)
    return (c['id'], os.path.getsize(dst), f'{im.width}x{im.height}')
if __name__ == '__main__':
    cards = D['setcards']
    with ProcessPoolExecutor() as ex:
        res = list(ex.map(one, cards))
    tot = sum(r[1] for r in res)
    print(len(res), 'files', round(tot / 1024 / 1024, 1), 'MB', 'avg KB', round(tot / len(res) / 1024))
