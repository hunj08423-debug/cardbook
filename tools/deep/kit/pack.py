# -*- coding: utf-8 -*-
"""만든 카드를 사용자 컴퓨터 폴더로 보낼 준비(클라우드 창 전용)

창이 사용자 컴퓨터 폴더를 직접 못 쓰고 ‘가져오기(device_stage_files)·보내기(device_commit_files)’로만 닿을 때 써요.
만든 파일을 /mnt/user-data/outputs/deep/ 로 옮기고, device_commit_files에 그대로 넣을 목록(50개씩)을 만들어요.

쓰는 법(작업 폴더의 cardbook 맨 위에서):
  python3 tools/deep/kit/pack.py --device "<사용자 컴퓨터의 cardbook 폴더 경로>" <카드id> [<카드id> ...]
  예: --device "C:\\Users\\user\\Downloads\\Christ.culture\\cardbook"   (get_device_info의 connectedFolders 경로 + \\cardbook)

보내는 것(그 카드 것만): site/deep/<id>.html, site/deep/<id>/ 안의 파일 전부, tools/deep/cards/<id>.py,
tools/deep/status/<id>.md, 그리고 cardbook 옆 deep_src/<id>/ 의 _sources.json(그림 출처 기록)과 받은 원본, 미리 자른 부분 그림(parts/)
(원본이 사용자 폴더에 있으면 나중에 다시 빌드할 때 다시 받지 않아도 돼요. 사용자 컴퓨터에서 받은 원본은 이미 거기 있어서 빼요).
다른 파일(site/data, index.json, app, list.txt, 공유 틀 site/deep/_deep3 등)은 절대 보내지 않아요. 공유 틀은 본부만 넣어요.
"""
import os, sys, json, shutil, ntpath, posixpath

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))
SRCROOT = os.environ.get('DEEP_SRC') or os.path.abspath(os.path.join(REPO, '..', 'deep_src'))
OUT = os.environ.get('DEEP_PACK_OUT') or '/mnt/user-data/outputs/deep'

def main():
    a = sys.argv[1:]
    if '--device' not in a: print(__doc__); sys.exit(1)
    i = a.index('--device'); dev = a[i + 1].rstrip('\\/'); ids = a[:i] + a[i + 2:]
    P = ntpath if ('\\' in dev or (len(dev) > 1 and dev[1] == ':')) else posixpath
    if not ids: raise SystemExit('카드 id를 하나 이상 적어 주세요')
    files = []
    for cid in ids:
        rel = [('site/deep/' + cid + '.html', os.path.join(REPO, 'site', 'deep', cid + '.html'))]
        ad = os.path.join(REPO, 'site', 'deep', cid)
        if not os.path.exists(rel[0][1]) or not os.path.isdir(ad): raise SystemExit(f'{cid}: 아직 만들지 않았어요(build.py 먼저)')
        rel += [(f'site/deep/{cid}/{f}', os.path.join(ad, f)) for f in sorted(os.listdir(ad))]
        rel.append((f'tools/deep/cards/{cid}.py', os.path.join(REPO, 'tools', 'deep', 'cards', cid + '.py')))
        stp = os.path.join(REPO, 'tools', 'deep', 'status', cid + '.md')
        if os.path.exists(stp): rel.append((f'tools/deep/status/{cid}.md', stp))
        else: print(f'  ⚠ {cid}: status 파일이 없어요(tools/deep/status/{cid}.md) — 상태를 적고 다시 돌려 주세요')
        sj = os.path.join(SRCROOT, cid, '_sources.json')
        if os.path.exists(sj):
            rel.append((f'../deep_src/{cid}/_sources.json', sj))
            try: S = json.load(open(sj, encoding='utf-8'))
            except Exception: S = {}
            sd = os.path.join(SRCROOT, cid)
            for f in sorted(os.listdir(sd)):
                fp = os.path.join(sd, f)
                if f == '_sources.json' or f.startswith('.') or f.endswith('.part') or not os.path.isfile(fp): continue
                if str((S.get(f) or {}).get('via', '')).startswith('사용자 컴퓨터'): continue   # 이미 사용자 폴더에 있어요
                if os.path.getsize(fp) > 300 * 1024 * 1024: print(f'  ⚠ {cid}/{f}: 너무 커서 보내지 않아요'); continue
                rel.append((f'../deep_src/{cid}/{f}', fp))
            pd = os.path.join(sd, 'parts')   # 큰 원본에서 미리 자른 부분 그림(재벌.md 4)도 보내요(2026-11-22)
            if os.path.isdir(pd):
                for f in sorted(os.listdir(pd)):
                    fp = os.path.join(pd, f)
                    if f.startswith('.') or f.endswith('.part') or not os.path.isfile(fp): continue
                    if os.path.getsize(fp) > 300 * 1024 * 1024: print(f'  ⚠ {cid}/parts/{f}: 너무 커서 보내지 않아요'); continue
                    rel.append((f'../deep_src/{cid}/parts/{f}', fp))
        for r, src in rel:
            dst = os.path.normpath(os.path.join(OUT, r.replace('../', '_up/')))
            os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(src, dst)
            if r.startswith('../'):
                devp = P.join(P.dirname(dev), *r[3:].split('/'))
            else:
                devp = P.join(dev, *r.split('/'))
            files.append({'stagedPath': dst, 'devicePath': devp})
    chunks = [files[k:k + 50] for k in range(0, len(files), 50)]
    for n, ch in enumerate(chunks, 1):
        p = os.path.join(OUT, f'commit_{n}.json')
        json.dump(ch, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'보낼 파일 {len(files)}개 → device_commit_files를 {len(chunks)}번 불러요. 목록:')
    for n in range(1, len(chunks) + 1): print('  ' + os.path.join(OUT, f'commit_{n}.json'))
    print('각 목록 파일을 열어 그 내용을 그대로 files 칸에 넣으세요(50개씩).')

if __name__ == '__main__':
    main()
