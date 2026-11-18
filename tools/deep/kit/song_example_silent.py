# -*- coding: utf-8 -*-
"""[예시] 「고요한 밤」 1절을 1818년의 편성(기타 · 첫째 목소리 · 둘째 목소리 · 성가대)으로 컴퓨터가 연주한 소리.
가락: 오늘 널리 부르는 가락(그루버 작곡, 퍼블릭 도메인)을 모어의 악보처럼 D장조로. 둘째 목소리와 기타 화음은 이 안내서가 만든 것.
결과: snd3/silent/guitar.mp3, v1.mp3, v2.mp3, choir.mp3 + timing.json"""
import sys; sys.dont_write_bytecode = True   # 사용자 폴더에 __pycache__를 만들지 않아요
import sys, os, json, subprocess, numpy as np, wave
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fsynth
OUT = sys.argv[1] if len(sys.argv) > 1 else 'snd_out'   # 결과 폴더(인자로 줌)
E = 60 / (46 * 3)          # 8분음표 길이(초): 점4분음표 = 46
BAR = 6 * E
rng = np.random.default_rng(1818)
def T(bar, eighth): return (bar * 6 + eighth) * E   # bar 0 = 전주

MEL = {1: [(0,1.5,57),(1.5,.5,59),(2,1,57),(3,3,54)], 3: [(0,2,64),(2,1,64),(3,3,61)], 4: [(0,2,62),(2,1,62),(3,3,57)],
       5: [(0,2,59),(2,1,59),(3,1.5,62),(4.5,.5,61),(5,1,59)], 9: [(0,2,64),(2,1,64),(3,1.5,67),(4.5,.5,64),(5,1,61)],
       10: [(0,3,62),(3,3,66)], 11: [(0,1.5,62),(1.5,.5,57),(2,1,54),(3,1.5,57),(4.5,.5,55),(5,1,52)], 12: [(0,6,50)]}
MEL[2] = MEL[6] = MEL[8] = MEL[1]; MEL[7] = MEL[5]
BAS = {1: [(0,1.5,42),(1.5,.5,43),(2,1,42),(3,3,38)], 3: [(0,2,49),(2,1,49),(3,3,45)], 4: [(0,2,50),(2,1,50),(3,3,42)],
       5: [(0,2,43),(2,1,43),(3,1.5,47),(4.5,.5,45),(5,1,43)], 9: [(0,2,49),(2,1,49),(3,1.5,52),(4.5,.5,49),(5,1,45)],
       10: [(0,3,50),(3,3,50)], 11: [(0,1.5,45),(1.5,.5,42),(2,1,38),(3,1.5,49),(4.5,.5,45),(5,1,40)], 12: [(0,6,38)]}
BAS[2] = BAS[6] = BAS[8] = BAS[1]; BAS[7] = BAS[5]
CH = {0: 'D', 1: 'D', 2: 'D', 3: 'A7', 4: 'D', 5: 'G', 6: 'D', 7: 'G', 8: 'D', 9: 'A7', 10: 'D', 11: ('D', 'A7'), 12: 'D'}
for k in range(13, 17): CH[k] = CH[k - 4]
CHORD = {'D': (50, 45, [57, 62, 66]), 'A7': (45, 40, [55, 61, 64]), 'G': (43, 50, [59, 62, 67])}

def hum(t, amt=0.012): return t + float(rng.normal(0, amt))
def guitar():
    ev = []
    for bar in range(0, 17):
        c = CH[bar]
        for half in (0, 1):
            name = c[half] if isinstance(c, tuple) else c
            root, fifth, up = CHORD[name]
            b0 = T(bar, 3 * half)
            ev.append((hum(b0), 3 * E * 0.98, root if half == 0 else fifth, int(64 + rng.integers(-4, 5))))
            for k in (1, 2):
                t = T(bar, 3 * half + k)
                for j, p in enumerate(up):
                    ev.append((hum(t) + 0.018 * j, 1.9 * E, p, int(46 + rng.integers(-4, 5) + (4 if k == 1 else 0))))
    # 마지막 화음: 천천히 퉁기고 울리게
    t = T(17, 0)
    for j, p in enumerate([50, 57, 62, 66, 69]):
        ev.append((t + 0.07 * j, 3.2, p, 58))
    return ev
def voice(tab, bars, shift=0, vel=78, legato=0.04):
    ev = []
    for bar in bars:
        for (s, d, p) in tab[bar]:
            ev.append((T(bar, s) + float(rng.normal(0, 0.006)), d * E + legato, p + shift, vel + int(rng.integers(-3, 4))))
    return ev
def choir():
    ev = []
    for bar in range(13, 17):
        src = bar - 4
        for (s, d, p) in MEL[src]: ev.append((T(bar, s), d * E + 0.05, p + 12, 72))          # 소프라노
        for (s, d, p) in BAS[src]: ev.append((T(bar, s), d * E + 0.05, p + 24, 64))          # 알토
        for (s, d, p) in MEL[src]: ev.append((T(bar, s), d * E + 0.05, p, 56))               # 테너(가락을 한 옥타브 아래로)
        c = CH[bar]
        names = c if isinstance(c, tuple) else (c, c)
        for half in (0, 1):
            root = CHORD[names[half]][0] - 12 if CHORD[names[half]][0] > 47 else CHORD[names[half]][0]
            ev.append((T(bar, 3 * half), 3 * E + 0.05, root, 62))                         # 베이스
    return ev
TOTAL = T(17, 0) + 3.6
stems = {
  'guitar': fsynth.render(guitar(), 24, TOTAL, pan=56, vol=110),
  'v1': fsynth.render(voice(MEL, range(1, 13)), 53, TOTAL, pan=76, vol=112),
  'v2': fsynth.render(voice(BAS, range(1, 13), vel=74), 53, TOTAL, pan=50, vol=112),
  'choir': fsynth.render(choir(), 52, TOTAL, pan=64, vol=104),
}
# 작은 성당 울림(모든 소리에 같게)
sr = fsynth.SR
n = int(1.7 * sr); t = np.arange(n) / sr
ir = (rng.normal(0, 1, (n, 2)) * np.exp(-t * 4.2)[:, None]).astype(np.float32); ir[:, 0] /= np.abs(ir[:, 0]).sum() ** .5; ir[:, 1] /= np.abs(ir[:, 1]).sum() ** .5
from scipy.signal import fftconvolve
for k, a in stems.items():
    wet = np.stack([fftconvolve(a[:, c], ir[:, c])[:len(a)] for c in (0, 1)], 1)
    stems[k] = a + 0.16 * wet / (np.abs(wet).max() + 1e-9) * np.abs(a).max()
gain = {'guitar': 0.42, 'v1': 0.40, 'v2': 0.36, 'choir': 0.40}
for k in stems: stems[k] = stems[k] / (np.abs(stems[k]).max() + 1e-9) * gain[k]
mix = sum(stems.values()); pk = float(np.abs(mix).max())
sc = min(1.0, 0.92 / pk)
os.makedirs(OUT, exist_ok=True)
for k, a in stems.items():
    a = np.clip(a * sc, -1, 1)
    fade = np.ones(len(a)); fl = int(1.2 * sr); fade[-fl:] = np.linspace(1, 0, fl)
    a = (a * fade[:, None] * 32767).astype(np.int16)
    w = wave.open(f'{OUT}/{k}.wav', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(a.tobytes()); w.close()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{OUT}/{k}.wav', '-codec:a', 'libmp3lame', '-b:a', '80k', f'{OUT}/{k}.mp3'], check=True)
    os.remove(f'{OUT}/{k}.wav')
lines = []
for n_, (b0, e0) in enumerate([(1, 0), (3, 0), (5, 0), (7, 0), (9, 0), (10, 3)]):
    nxt = [(3, 0), (5, 0), (7, 0), (9, 0), (10, 3), (13, 0)][n_]
    lines.append({'n': n_, 'at': round(T(b0, e0), 2), 'end': round(T(*nxt), 2), 'choir': False})
lines.append({'n': 4, 'at': round(T(13, 0), 2), 'end': round(T(14, 3), 2), 'choir': True})
lines.append({'n': 5, 'at': round(T(14, 3), 2), 'end': round(T(17, 0), 2), 'choir': True})
json.dump({'dur': round(TOTAL, 2), 'lines': lines, 'peak_mix': pk, 'scale': sc}, open(f'{OUT}/timing.json', 'w'), indent=1)
print(json.dumps({'dur': round(TOTAL, 2), 'pk': pk, 'sc': sc, 'lines': lines}))
print({k: os.path.getsize(f'{OUT}/{k}.mp3') for k in stems})
