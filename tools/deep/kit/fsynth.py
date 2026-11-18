# -*- coding: utf-8 -*-
"""fluidsynth(라이브러리)로 음표 목록을 WAV로 만드는 작은 도구. 오디오 장치 없이 메모리에서만 그림."""
import ctypes, numpy as np
_fs = ctypes.CDLL('libfluidsynth.so.3')
_fs.new_fluid_settings.restype = ctypes.c_void_p
_fs.new_fluid_synth.restype = ctypes.c_void_p
_fs.new_fluid_synth.argtypes = [ctypes.c_void_p]
_fs.fluid_settings_setnum.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_double]
_fs.fluid_settings_setint.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
_fs.fluid_synth_sfload.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
_fs.fluid_synth_program_select.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
_fs.fluid_synth_noteon.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
_fs.fluid_synth_noteoff.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
_fs.fluid_synth_cc.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
_fs.fluid_synth_write_float.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
_fs.fluid_synth_set_reverb_on.argtypes = [ctypes.c_void_p, ctypes.c_int]
_fs.fluid_synth_set_chorus_on.argtypes = [ctypes.c_void_p, ctypes.c_int]
_fs.delete_fluid_synth.argtypes = [ctypes.c_void_p]
_fs.delete_fluid_settings.argtypes = [ctypes.c_void_p]
SF2 = b'/usr/share/sounds/sf2/TimGM6mb.sf2'
SR = 44100

def render(events, program, total_sec, bank=0, vol=100, pan=64, sr=SR):
    """events: [(시작초, 길이초, 음높이, 세기)] → (n,2) float32"""
    st = _fs.new_fluid_settings()
    _fs.fluid_settings_setnum(st, b'synth.sample-rate', float(sr))
    _fs.fluid_settings_setnum(st, b'synth.gain', 0.5)
    sy = _fs.new_fluid_synth(st)
    _fs.fluid_synth_set_reverb_on(sy, 0); _fs.fluid_synth_set_chorus_on(sy, 0)
    sfid = _fs.fluid_synth_sfload(sy, SF2, 1)
    assert sfid >= 0, 'sf2 load failed'
    _fs.fluid_synth_program_select(sy, 0, sfid, bank, program)
    _fs.fluid_synth_cc(sy, 0, 7, vol); _fs.fluid_synth_cc(sy, 0, 10, pan)
    ev = []
    for s, d, p, v in events:
        ev.append((s, 1, p, v)); ev.append((s + d, 0, p, 0))
    ev.sort(key=lambda x: (x[0], x[1]))
    n = int(total_sec * sr)
    L = np.zeros(n, np.float32); R = np.zeros(n, np.float32)
    pos = 0
    def adv(to):
        nonlocal pos
        to = min(n, to)
        while pos < to:
            k = min(4096, to - pos)
            _fs.fluid_synth_write_float(sy, k, L.ctypes.data, pos, 1, R.ctypes.data, pos, 1)
            pos += k
    for t, on, p, v in ev:
        adv(int(t * sr))
        if on: _fs.fluid_synth_noteon(sy, 0, p, v)
        else: _fs.fluid_synth_noteoff(sy, 0, p)
    adv(n)
    _fs.delete_fluid_synth(sy); _fs.delete_fluid_settings(st)
    return np.stack([L, R], 1)
