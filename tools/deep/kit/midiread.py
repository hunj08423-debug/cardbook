# -*- coding: utf-8 -*-
"""작은 MIDI 읽개: 트랙별 음표(시작 박, 길이 박, 음높이, 세기)를 돌려줌."""
import struct

def _vlq(b, i):
    v = 0
    while True:
        c = b[i]; i += 1
        v = (v << 7) | (c & 0x7F)
        if not c & 0x80:
            return v, i

def read(path):
    b = open(path, 'rb').read()
    assert b[:4] == b'MThd'
    hl = struct.unpack('>I', b[4:8])[0]
    fmt, ntr, div = struct.unpack('>HHH', b[8:14])
    i = 8 + hl
    tracks, tempos, names, timesig = [], [], {}, []
    for t in range(ntr):
        assert b[i:i+4] == b'MTrk', b[i:i+4]
        ln = struct.unpack('>I', b[i+4:i+8])[0]
        j, end = i + 8, i + 8 + ln
        tick, run, on, notes = 0, None, {}, []
        while j < end:
            d, j = _vlq(b, j); tick += d
            st = b[j]
            if st == 0xFF:
                typ = b[j+1]; l, k = _vlq(b, j+2); data = b[k:k+l]; j = k + l
                if typ == 0x51: tempos.append((tick, int.from_bytes(data, 'big')))
                elif typ == 0x03: names[t] = data.decode('latin-1', 'replace')
                elif typ == 0x58: timesig.append((tick, data[0], 2 ** data[1]))
                continue
            if st in (0xF0, 0xF7):
                l, k = _vlq(b, j+1); j = k + l; continue
            if st & 0x80: run = st; j += 1
            ev, ch = run & 0xF0, run & 0x0F
            if ev in (0xC0, 0xD0):
                j += 1; continue
            a1, a2 = b[j], b[j+1]; j += 2
            if ev == 0x90 and a2 > 0:
                on[(ch, a1)] = (tick, a2)
            elif ev == 0x80 or (ev == 0x90 and a2 == 0):
                if (ch, a1) in on:
                    s, v = on.pop((ch, a1)); notes.append((s / div, (tick - s) / div, a1, v, ch))
        tracks.append(sorted(notes))
        i = end
    return {'div': div, 'fmt': fmt, 'tracks': tracks, 'tempos': tempos, 'names': names, 'timesig': timesig}

if __name__ == '__main__':
    import sys
    m = read(sys.argv[1])
    print('div', m['div'], 'tempos', m['tempos'][:3], 'timesig', m['timesig'], 'names', m['names'])
    N = 'C C# D D# E F F# G G# A A# B'.split()
    for t, tr in enumerate(m['tracks']):
        if not tr: continue
        print('track', t, m['names'].get(t), len(tr), 'notes')
        print('  ', ' '.join(f"{N[p%12]}{p//12-1}@{s:g}/{d:g}" for s, d, p, v, c in tr[:80]))
