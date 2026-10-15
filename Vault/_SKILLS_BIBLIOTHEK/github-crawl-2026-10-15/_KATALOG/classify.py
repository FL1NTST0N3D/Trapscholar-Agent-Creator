#!/usr/bin/env python3
"""Dedupe + classify indexed skills/agents into Vault domains by keyword."""
import json, sys, re, hashlib
from collections import Counter, defaultdict
idx = json.load(open(sys.argv[1]))
DOM = {
 '01_shop_ops': r'shopify|woocommerce|fulfil|order|inventory|refund|return|customer (support|service)|helpdesk|gorgias|zendesk|catalog|product (listing|feed|page)|liquid|theme|printful|printify|gelato|teeinblue|print.on.demand|pod\b|merchant|storefront|checkout|discount|dropship|ecommerce|e-commerce|dtc|d2c|retail|store',
 '02_paid_ads': r'\bads?\b|advertis|meta ads|facebook ads|instagram ads|tiktok ads|google ads|pmax|performance max|roas|\bcpa\b|\bcpm\b|\bmer\b|creative test|ugc|ad creative|ad copy|campaign|pixel|capi|conversion api|retarget|lookalike|advantage\+|ad library',
 '03_pod_marketplaces': r'amazon|merch|kdp|kindle|fba|seller central|\bppc\b|etsy|redbubble|spreadshirt|teepublic|printkk|niche|trademark|uspto|euipo|listing|asin|marketplace|ebay|walmart|tiktok shop',
 '04_design': r'design|brand|logo|typograph|color|colour|palette|aesthetic|visual|illustrat|graphic|mockup|midjourney|flux|dall|ideogram|recraft|stable diffusion|image gen|vector|svg|print.ready|dpi|bleed|t-shirt|tshirt|apparel|textile|canva|figma|poster|ui/ux|ui ux|frontend design|landing page design|art direct',
 '05_social': r'social|instagram|tiktok|pinterest|youtube|shorts|reels|facebook|threads|linkedin|\bx\b|twitter|hashtag|caption|hook|influencer|creator|content calendar|schedul|postiz|buffer|publora|community|comment|\bdm\b|viral|trend',
 '06_email_cro_seo': r'email|klaviyo|newsletter|sms|flow|abandon|winback|win-back|retention|loyalty|review|cro\b|conversion|a/b|ab test|landing page|copywriting|copy\b|headline|seo|keyword|backlink|schema|sitemap|geo\b|ai search|analytics|ga4|report|dashboard|kpi|cohort|ltv|cac|aov|pricing|bundle|upsell|offer',
 '07_agent_arch': r'agent|orchestrat|subagent|sub-agent|workflow|hook|token|context|compact|memory|routing|haiku|sonnet|opus|cost|mcp|skill creat|meta-skill|automation|cron|schedule|pipeline|guardrail|eval|observab|caveman|rtk',
 '08_research_data': r'research|competitor|scrap|crawl|apify|firecrawl|playwright|browser|market|persona|customer research|survey|trend|forecast|finance|cfo|unit economics|margin|profit|cash|budget|sql|pandas|data analy|statistic|spreadsheet|excel|csv',
}
NOISE = r'kubernetes|terraform|docker|rust|golang|\bgo\b lang|java\b|kotlin|swift|ios|android|react native|flutter|unity|unreal|game dev|blockchain|solidity|web3|crypto|devops|ci/cd|jenkins|ansible|helm|aws lambda|azure|gcp|embedded|firmware|arduino|raspberry|quantum|bioinformatics|genomics|medical|legal contract|accounting standard|tax|hr\b|recruit|payroll'
def classify(name, desc):
    t = (name+' '+desc).lower()
    if re.search(NOISE, t) and not re.search(r'ecommerce|e-commerce|shopify|amazon|etsy|ads|design|social|email|marketing', t):
        return []
    return [d for d, rx in DOM.items() if re.search(rx, t)]
seen = {}
out = {'skills':[], 'agents':[]}
dup = 0
for kind in ('skills','agents'):
    for it in idx[kind]:
        key = hashlib.md5((it['name'].lower().strip()+'|'+it['description'][:200].lower().strip()).encode()).hexdigest()
        doms = classify(it['name'], it['description'])
        if not doms: continue
        if key in seen:
            dup += 1; seen[key]['dupes'].append(it['repo']); continue
        it = dict(it); it['domains'] = doms; it['dupes'] = []
        seen[key] = it; out[kind].append(it)
json.dump(out, open(sys.argv[2],'w'), indent=1, ensure_ascii=False)
print('kept skills', len(out['skills']), 'agents', len(out['agents']), 'dupes', dup)
c = Counter(d for k in out for it in out[k] for d in it['domains']); print(c.most_common())
