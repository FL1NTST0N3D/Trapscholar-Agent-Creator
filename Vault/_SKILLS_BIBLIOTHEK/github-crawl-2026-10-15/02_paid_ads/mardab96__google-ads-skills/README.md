# 20 Claude Skills for Google Ads

A pack of 20 production-ready Claude Skills that help agencies, freelancers, and in-house performance marketers run rigorous Google Ads work: account triage, wasted spend, structure, search terms, Quality Score, impression share, conversion tracking, offline conversion imports, Shopping feed quality, anomaly detection and root-cause diagnosis, RSA copy, Performance Max, bidding, landing page match, competitive pressure, forecasting, scaling, and recurring reporting.

Each skill is a self-contained `SKILL.md` with explicit triggers, required inputs, analysis workflow, decision rules with unit-carrying thresholds (the RSA generator carries a mandatory verification pass instead), routing to the next skill, a practical example, output format, and guardrails. Drop them into Claude and they activate automatically when their use case matches the conversation.

Full guide: [20 Claude Skills for Google Ads](https://adlume.co/blog/google-ads-claude-skills) explains the workflow behind this pack and how to use the skills in real Google Ads audits.

## What changed in v2

Version 1 shipped 10 diagnostic and creative skills. Version 2 doubles the pack to 20 and closes three gaps that mattered more than the count:

1. **An entry point.** `account-triage-google-ads` establishes what to check first and routes to the right deep-dive skill. Most audits fail because they start in the wrong place, not because the analysis is weak.
2. **The data layer nobody audits.** Shopping feed quality and offline conversion imports decide what Smart Bidding actually learns from. Both were missing.
3. **2026 platform reality.** Dynamic Search Ads, automatically created assets, and campaign-level broad match are scheduled to auto-upgrade to AI Max from September 2026. Skills that recommend structural work now flag upgrade exposure before you rebuild something the upgrade will change.

## What's inside

### Start here

| # | Skill | Folder | Purpose |
|---|-------|--------|---------|
| 1 | Account Triage | `account-triage-google-ads` | Ordered triage of an unfamiliar account; establishes what is broken and which skill to run next |

### Diagnose

| # | Skill | Folder | Purpose |
|---|-------|--------|---------|
| 2 | Wasted Spend Finder | `wasted-spend-finder-google-ads` | Find segments that spend without converting across search terms, devices, dayparts, geos, demographics |
| 3 | Account Structure Audit | `account-structure-audit-google-ads` | Map structure, flag under-volume / fragmented / duplicated campaigns, propose consolidation |
| 4 | Search Terms Hygiene | `search-terms-hygiene-google-ads` | Build a layered negative keyword plan from search terms reports |
| 5 | Quality Score Analysis | `quality-score-analysis-google-ads` | Break down QS components, find which keywords drag the account, prioritise by revenue impact |
| 6 | Impression Share Gap Finder | `impression-share-gap-finder-google-ads` | Separate impression share lost to budget from lost to rank, and size the opportunity |
| 7 | Anomaly Detection | `anomaly-detection-google-ads` | Baseline deviation detection across CPA, ROAS, CVR, CTR, CPC, conversion volume |
| 8 | CPA Spike Diagnosis | `cpa-spike-diagnosis-google-ads` | Rank the probable causes of a CPA spike with supporting evidence, where anomaly detection only flags it |
| 9 | PMax Performance Diagnosis | `pmax-performance-diagnosis-google-ads` | Diagnose Performance Max: asset groups, audience signals, search insights, cannibalization |

### Measure

| # | Skill | Folder | Purpose |
|---|-------|--------|---------|
| 10 | Conversion Tracking Audit | `conversion-tracking-audit-google-ads` | Audit tracking using GA4 + GTM data: deduplication, primary vs secondary, attribution windows |
| 11 | Offline Conversion Import Audit | `offline-conversion-import-audit-google-ads` | Check that real lead quality reaches Smart Bidding: click ID capture, CRM mapping, import latency, value assignment |
| 12 | Shopping Feed QA | `shopping-feed-qa-google-ads` | Audit the Merchant Center feed that gates Shopping and Performance Max delivery |

### Optimise

| # | Skill | Folder | Purpose |
|---|-------|--------|---------|
| 13 | RSA Ad Copy Review | `rsa-ad-copy-review-google-ads` | Score existing RSAs for intent match, asset diversity, compliance, landing page alignment |
| 14 | RSA Ad Copy Generator | `rsa-ad-copy-generator-google-ads` | Produce headlines and descriptions matched to brand voice, intent, and offer |
| 15 | Landing Page Match Scorer | `landing-page-match-scorer-google-ads` | Score message match, intent alignment, CTA clarity, trust, mobile, form friction; rewrite the weakest |
| 16 | Bidding Strategy Sanity Check | `bidding-strategy-sanity-check-google-ads` | Match bid strategy to conversion volume, tracking quality, budget, and account stage |

### Plan and report

| # | Skill | Folder | Purpose |
|---|-------|--------|---------|
| 17 | Scaling Planner | `scaling-planner-google-ads` | Decide where to add budget, hold, reduce, or pause, with reallocation and monitoring plan |
| 18 | ROAS Forecast Scenarios | `roas-forecast-scenarios-google-ads` | Project 30/60/90 day outcomes with confidence bands and three spend scenarios |
| 19 | Competitor Benchmark | `competitor-benchmark-auction-insights-google-ads` | Read auction insights over time; separate competitive shifts from internal changes |
| 20 | Weekly Operator Digest | `weekly-operator-digest-google-ads` | Recurring readout serving both the operator who needs detail and the stakeholder who needs the headline |

## Suggested order

If you are new to the pack, run them in this sequence rather than picking at random:

1. `account-triage-google-ads` to find out what is actually wrong.
2. Whatever triage routes you to, usually measurement first: `conversion-tracking-audit`, then `offline-conversion-import-audit` for lead gen or `shopping-feed-qa` for ecommerce.
3. Only then the performance skills. Optimising on top of broken measurement produces confident, wrong answers.

## How to install

### Option A — Claude Code (recommended)

```bash
git clone https://github.com/mardab96/google-ads-skills.git
mkdir -p ~/.claude/skills
cp -r google-ads-skills/*-google-ads google-ads-skills/scripts ~/.claude/skills/
```

That copies the 20 skill folders into your user-level skills directory. Use `.claude/skills/` at the root of a project instead if you want them scoped to one project. Start a new Claude Code session and the skills activate automatically when their description matches the conversation.

### Option B — Other Claude environments

The skills are plain Markdown with YAML frontmatter and work anywhere Claude can read files. Paste the relevant `SKILL.md` content into context when you want to use it.

## How to use

Once installed, just describe what you want in natural language. Skills self-trigger on the patterns documented in their `## Use this skill when` section.

Examples:

- "We just took over this account, where do we start?" → activates Account Triage.
- "Find wasted spend in this Google Ads account, here are the CSV exports from the last 60 days." → activates Wasted Spend Finder.
- "CPA jumped 40% last week and I don't know why." → activates CPA Spike Diagnosis.
- "Are we losing impressions to budget or to rank?" → activates Impression Share Gap Finder.
- "Is Smart Bidding actually learning from our qualified leads?" → activates Offline Conversion Import Audit.

## Bring your data

Every skill is data-first. They work best when you provide actual exports: search terms reports, performance CSVs, asset reports, conversion action lists, Merchant Center diagnostics, CRM stage data. Each `SKILL.md` documents exactly which exports it expects under `## Required input`.

For users with the Google Ads MCP server connected, skills can pull live data directly. For everyone else, CSV exports from the Google Ads UI or Google Ads Editor work fine.

## A note on thresholds

Numeric thresholds in these skills are starting heuristics, not Google-published rules. Conversion volume, vertical, seasonality, and account maturity all move them. Every skill says so in its guardrails or decision rules, and each one is written to tell you when it adjusted a threshold and why. Treat any skill that hands you a confident number without stating its assumptions as a skill worth ignoring, including these.

## License & attribution

Free to use, modify, and redistribute for personal and commercial work. If you ship something built on top of these skills, a credit is appreciated but not required.

Built and maintained by [AdLume](https://adlume.co) — performance marketing infrastructure for AI-native agencies.
