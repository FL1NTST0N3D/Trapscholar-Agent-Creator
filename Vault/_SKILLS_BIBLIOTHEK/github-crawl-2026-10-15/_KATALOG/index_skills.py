#!/usr/bin/env python3
"""Index SKILL.md skills and Claude subagent .md files across cloned repos."""
import os, re, json, sys, csv
ROOT = sys.argv[1]
OUT = sys.argv[2]
SKIP = {'.git','node_modules','dist','build','__pycache__','.venv','venv','tests','test','__tests__','.github'}
FM = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.S)

def frontmatter(text):
    m = FM.match(text)
    if not m: return {}
    d = {}
    for line in m.group(1).splitlines():
        mm = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if mm:
            k, v = mm.group(1), mm.group(2).strip().strip('"').strip("'")
            d[k] = v
    return d

def license_of(repo_dir):
    for n in os.listdir(repo_dir):
        if n.lower().startswith('license'):
            try:
                head = open(os.path.join(repo_dir,n),errors='ignore').read(400)
            except: return n
            for key in ['MIT','Apache','GPL','BSD','MPL','CC0','Creative Commons','Unlicense','AGPL']:
                if key.lower() in head.lower(): return key
            return 'other'
    return ''

skills, agents = [], []
for repo in sorted(os.listdir(ROOT)):
    rd = os.path.join(ROOT, repo)
    if not os.path.isdir(rd): continue
    lic = license_of(rd)
    for dp, dns, fns in os.walk(rd):
        dns[:] = [d for d in dns if d not in SKIP]
        rel = os.path.relpath(dp, ROOT)
        for fn in fns:
            if not fn.endswith('.md'): continue
            p = os.path.join(dp, fn)
            try: txt = open(p, errors='ignore').read(20000)
            except: continue
            fm = frontmatter(txt)
            if fn == 'SKILL.md':
                skills.append({'repo':repo,'path':os.path.join(rel,fn),'name':fm.get('name',os.path.basename(dp)),
                    'description':fm.get('description','')[:400],'license':lic,
                    'size':os.path.getsize(p)})
            elif fm.get('name') and fm.get('description') and ('agents' in rel.split(os.sep) or 'subagents' in rel.split(os.sep) or fm.get('tools') or fm.get('model')):
                agents.append({'repo':repo,'path':os.path.join(rel,fn),'name':fm['name'],
                    'description':fm['description'][:400],'model':fm.get('model',''),'tools':fm.get('tools','')[:120],'license':lic})
json.dump({'skills':skills,'agents':agents}, open(os.path.join(OUT,'index.json'),'w'), indent=1, ensure_ascii=False)
for key, rows in (('skills',skills),('agents',agents)):
    with open(os.path.join(OUT, key+'.csv'),'w',newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ['repo'])
        w.writeheader(); w.writerows(rows)
print('skills', len(skills), 'agents', len(agents))
from collections import Counter
print(Counter(s['repo'] for s in skills).most_common(40))
print(Counter(a['repo'] for a in agents).most_common(20))
print('models:', Counter(a['model'] for a in agents).most_common(10))
