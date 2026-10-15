#!/usr/bin/env python3
"""Security scan over skill collections: prompt injection, exfiltration, dangerous shell, secrets, hidden text."""
import os, sys, re, json, collections
ROOT = sys.argv[1]; OUT = sys.argv[2]
SKIP = {'.git','node_modules','dist','build','__pycache__','.venv','venv'}
RULES = {
 'INJECTION': [r'ignore (all |any )?(previous|prior|above) (instructions|rules)', r'disregard (the )?(system|previous)', r'you are now (a|an) ', r'do not tell the user', r'without (telling|informing) the user', r'hide this from', r'secretly', r'jailbreak', r'DAN mode'],
 'EXFIL': [r'curl[^\n]*\$\{?[A-Z_]*(KEY|TOKEN|SECRET|PASS)[A-Z_]*', r'(wget|curl)[^\n]*(ngrok|webhook\.site|requestbin|pipedream|burpcollab|interact\.sh)', r'base64 (-d|--decode)[^\n]*\|\s*(sh|bash)', r'\|\s*(sh|bash)\s*$', r'eval\s*\(\s*(atob|base64|decode)', r'nc -e', r'/dev/tcp/', r'send.*(\.env|credentials|id_rsa)'],
 'DANGEROUS_SHELL': [r'rm -rf\s+(/|~|\$HOME|\*)', r'chmod 777', r'sudo ', r'mkfs\.', r':\(\)\{ :\|:& \};:', r'curl[^\n]*\|\s*(sudo )?(sh|bash)', r'wget[^\n]*-O-?[^\n]*\|\s*(sh|bash)', r'git push --force', r'DROP TABLE', r'shutdown', r'crontab -r'],
 'SECRETS': [r'sk-ant-[A-Za-z0-9\-_]{20,}', r'sk-[A-Za-z0-9]{32,}', r'AKIA[0-9A-Z]{16}', r'ghp_[A-Za-z0-9]{36}', r'xox[bp]-[A-Za-z0-9\-]{20,}', r'-----BEGIN (RSA |EC )?PRIVATE KEY', r'shpat_[a-f0-9]{32}', r'EAA[A-Za-z0-9]{40,}', r'pk_live_[A-Za-z0-9]{20,}'],
 'HIDDEN_TEXT': [r'<!--[^>]{0,40}(instruction|ignore|secret|override)[^>]*-->', r'​|‌|‍|⁠|﻿', r'<span[^>]*display:\s*none', r'font-size:\s*0'],
 'EXTERNAL_INSTALL': [r'npx\s+-y\s+\S+', r'pip install\s+(git\+https|https?://)', r'npm i(nstall)?\s+https?://', r'curl -fsSL https?://\S+\s*\|'],
 'PERMISSION_ESCALATION': [r'bypassPermissions', r'dangerously-skip-permissions', r'--allow-all', r'permissionMode:\s*bypass', r'disable.*(sandbox|safety|classifier)'],
}
RX = {k:[re.compile(p, re.I) for p in v] for k,v in RULES.items()}
findings = []; files=0; perrepo = collections.defaultdict(collections.Counter)
for dp, dns, fns in os.walk(ROOT):
    dns[:] = [d for d in dns if d not in SKIP]
    for fn in fns:
        if os.path.splitext(fn)[1].lower() not in {'.md','.txt','.json','.yaml','.yml','.py','.js','.ts','.sh','.mjs','.cjs','.toml','.html'}: continue
        p = os.path.join(dp, fn)
        try:
            if os.path.getsize(p) > 3*1024*1024: continue
            txt = open(p, errors='ignore').read()
        except: continue
        files+=1
        rel = os.path.relpath(p, ROOT); repo = rel.split(os.sep)[0]
        for cat, rxs in RX.items():
            for rx in rxs:
                for m in rx.finditer(txt):
                    line = txt.count('\n', 0, m.start())+1
                    ctx = txt[max(0,m.start()-80):m.end()+80].replace('\n',' ')
                    findings.append({'cat':cat,'repo':repo,'file':rel,'line':line,'match':m.group(0)[:80],'ctx':ctx[:200]})
                    perrepo[repo][cat]+=1
json.dump(findings, open(OUT,'w'), indent=1, ensure_ascii=False)
print('files scanned', files, 'findings', len(findings))
print(collections.Counter(f['cat'] for f in findings))
for repo, c in sorted(perrepo.items(), key=lambda x:-sum(x[1].values()))[:40]:
    print(f"{sum(c.values()):4d} {repo:50s} {dict(c)}")
