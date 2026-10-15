#!/usr/bin/env python3
"""Copy curated skill/agent collections from crawl/repos into the Vault library.
Usage: copy_to_vault.py <repos_dir> <vault_lib_dir> <selection.json>
selection.json: {"<domain>": [{"repo": "<owner>__<repo>", "paths": ["skills/x", "..."] or "ALL_SKILLS"}]}
Copies SKILL.md dirs (and agent .md files) with their sibling files; skips binaries > 2MB, node_modules, .git, tests.
"""
import os, sys, json, shutil, re
repos, vault, sel = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3]))
SKIP = {'.git','node_modules','dist','build','__pycache__','.venv','venv','tests','test','__tests__','.github','examples','example'}
MAXB = 2*1024*1024
TEXT = {'.md','.txt','.json','.yaml','.yml','.py','.js','.ts','.sh','.csv','.toml','.html','.css','.mjs','.cjs','.xml','.svg','.liquid','.graphql','.sql'}
def copy_tree(src, dst):
    n=0
    for dp, dns, fns in os.walk(src):
        dns[:] = [d for d in dns if d not in SKIP]
        for fn in fns:
            sp = os.path.join(dp, fn); ext = os.path.splitext(fn)[1].lower()
            try: sz = os.path.getsize(sp)
            except: continue
            if sz > MAXB: continue
            if ext not in TEXT and ext not in {'.png','.jpg','.jpeg','.webp','.gif','.pdf'}: continue
            if ext in {'.png','.jpg','.jpeg','.webp','.gif','.pdf'} and sz > 512*1024: continue
            rel = os.path.relpath(sp, src); tp = os.path.join(dst, rel)
            os.makedirs(os.path.dirname(tp), exist_ok=True); shutil.copy2(sp, tp); n+=1
    return n
def skill_dirs(repo_dir):
    out=[]
    for dp, dns, fns in os.walk(repo_dir):
        dns[:] = [d for d in dns if d not in SKIP]
        if 'SKILL.md' in fns: out.append(dp); dns[:] = []
    return out
total=0; manifest=[]
for domain, entries in sel.items():
    for e in entries:
        rd = os.path.join(repos, e['repo'])
        if not os.path.isdir(rd): print('MISSING', e['repo']); continue
        dst_repo = os.path.join(vault, domain, e['repo'])
        # always carry README + LICENSE
        for fn in os.listdir(rd):
            if fn.lower().startswith(('readme','license')) and os.path.isfile(os.path.join(rd,fn)):
                os.makedirs(dst_repo, exist_ok=True); shutil.copy2(os.path.join(rd,fn), os.path.join(dst_repo, fn))
        paths = e.get('paths','ALL_SKILLS')
        if paths == 'ALL_SKILLS':
            srcs = skill_dirs(rd)
        elif paths == 'ALL':
            srcs = [rd]
        else:
            srcs = [os.path.join(rd,p) for p in paths]
        for s in srcs:
            if not os.path.exists(s): print('MISSING PATH', e['repo'], s); continue
            rel = os.path.relpath(s, rd) if s != rd else '.'
            d = os.path.join(dst_repo, rel) if rel != '.' else dst_repo
            if os.path.isfile(s):
                os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copy2(s, d); n=1
            else: n = copy_tree(s, d)
            total+=n; manifest.append((domain, e['repo'], rel, n))
json.dump(manifest, open(os.path.join(vault,'_manifest.json'),'w'), indent=1)
print('files copied', total); 
from collections import Counter
print(Counter(m[0] for m in manifest))
