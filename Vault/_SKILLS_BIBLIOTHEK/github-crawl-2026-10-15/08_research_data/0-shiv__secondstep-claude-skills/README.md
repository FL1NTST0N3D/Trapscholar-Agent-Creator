<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Skills-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0wIDE4Yy00LjQxIDAtOC0zLjU5LTgtOHMzLjU5LTggOC04IDggMy41OSA4IDgtMy41OSA4LTggNHoiLz48L3N2Zz4=" alt="Claude Code Skills"/>
  <img src="https://img.shields.io/badge/Skills-23-orange?style=for-the-badge" alt="23 Skills"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Files-600+-purple?style=for-the-badge" alt="600+ Files"/>
</p>

<h1 align="center">Second Step Claude Skills</h1>

<p align="center">
  <strong>23 production-ready Claude Code skills for performance marketing, advertising & growth.</strong><br/>
  Google Ads, Meta Ads, LinkedIn, TikTok, YouTube, GA4, SEO, CRO, Email, Copywriting & more.
</p>

<p align="center">
  <em>Built by <a href="https://getsecondstep.com">Second Step</a> — a performance marketing agency that manages $2M+ in annual ad spend.</em>
</p>

---

## What's Inside

Every skill is a self-contained Claude Code module with its own sub-skills, AI agents, Python scripts, and documentation. Install one or install all.

### Google Ads (6 skills)

| Skill | Description | Files |
|-------|-------------|-------|
| [**pmax-claude**](skills/pmax-claude/) | Performance Max auditing — asset scoring, search cannibalization, audience signals, budget split | 30 |
| [**google-ads-audit-claude**](skills/google-ads-audit-claude/) | Full Google Ads account audit — 13 sub-skills covering structure, keywords, QS, bidding, extensions | 41 |
| [**negative-keywords-claude**](skills/negative-keywords-claude/) | Negative keyword discovery, conflict detection, n-gram analysis & industry lists | 41 |
| [**quality-score-claude**](skills/quality-score-claude/) | Quality Score diagnosis — CTR, ad relevance, landing page experience & CPC impact | 36 |
| [**smart-bidding-claude**](skills/smart-bidding-claude/) | Smart Bidding optimization — tCPA, tROAS, learning phase, portfolio strategies | 22 |
| [**google-ads-scripts-claude**](skills/google-ads-scripts-claude/) | Generate production-ready Google Ads Scripts for automation | 16 |

### Meta Ads (1 skill)

| Skill | Description | Files |
|-------|-------------|-------|
| [**meta-ads-audit-claude**](skills/meta-ads-audit-claude/) | 150+ point Meta Ads audit — Pixel/CAPI, creative fatigue, EMQ, Advantage+ | 51 |

### Other Ad Platforms (3 skills)

| Skill | Description | Files |
|-------|-------------|-------|
| [**linkedin-ads-claude**](skills/linkedin-ads-claude/) | LinkedIn B2B advertising — audience targeting, lead gen forms, ABM strategy | 24 |
| [**tiktok-ads-claude**](skills/tiktok-ads-claude/) | TikTok Ads auditing — creative scoring, Spark Ads, pixel health, TikTok Shop | 17 |
| [**youtube-ads-claude**](skills/youtube-ads-claude/) | YouTube Ads audit — ABCD creative scoring, targeting, bidding & campaign structure | 26 |

### Analytics & Tracking (3 skills)

| Skill | Description | Files |
|-------|-------------|-------|
| [**ga4-audit-claude**](skills/ga4-audit-claude/) | GA4 implementation audit — event tracking, conversions, data quality & reporting | 29 |
| [**conversion-tracking-claude**](skills/conversion-tracking-claude/) | Cross-platform conversion tracking — GTM, pixels, server-side, enhanced conversions | 29 |
| [**saas-metrics-claude**](skills/saas-metrics-claude/) | SaaS metrics dashboard — MRR, churn, LTV, CAC, cohort analysis | 17 |

### SEO (3 skills)

| Skill | Description | Files |
|-------|-------------|-------|
| [**local-seo-claude**](skills/local-seo-claude/) | Local SEO audit — GBP optimization, NAP consistency, reviews, citations, schema | 25 |
| [**schema-markup-claude**](skills/schema-markup-claude/) | JSON-LD schema generator — LocalBusiness, Product, FAQ, HowTo & more | 26 |
| [**aeo-claude**](skills/aeo-claude/) | AI Engine Optimization — get your brand into ChatGPT, Gemini & Perplexity answers | 19 |

### CRO & Landing Pages (2 skills)

| Skill | Description | Files |
|-------|-------------|-------|
| [**landing-page-audit-claude**](skills/landing-page-audit-claude/) | Landing page CRO — 100+ checks for speed, message match, forms, trust & mobile UX | 26 |
| [**ab-testing-claude**](skills/ab-testing-claude/) | A/B test planning, sample size calculation & statistical analysis | 21 |

### Copywriting & Creative (2 skills)

| Skill | Description | Files |
|-------|-------------|-------|
| [**google-ads-copy-claude**](skills/google-ads-copy-claude/) | Google Ads copy optimization — RSA formulas, headline scoring, ad extensions | 37 |
| [**copywriting-frameworks-claude**](skills/copywriting-frameworks-claude/) | 12 proven frameworks — AIDA, PAS, BAB, 4Ps, storytelling & more | 16 |

### E-Commerce (1 skill)

| Skill | Description | Files |
|-------|-------------|-------|
| [**product-feed-claude**](skills/product-feed-claude/) | Google Merchant Center feed optimization — titles, attributes, disapprovals | 27 |

### Strategy (2 skills)

| Skill | Description | Files |
|-------|-------------|-------|
| [**competitor-analysis-claude**](skills/competitor-analysis-claude/) | Competitive intelligence — SWOT, battlecards, pricing, SERP overlap, tech detection | 32 |
| [**email-marketing-claude**](skills/email-marketing-claude/) | Email marketing audit — deliverability, automation flows, list health, campaigns | 26 |

---

## Installation

### Install a Single Skill

Each skill has its own `install.sh`. Navigate to any skill directory and run:

```bash
cd skills/pmax-claude
bash install.sh
```

### Install All Skills

```bash
git clone https://github.com/0-shiv/secondstep-claude-skills.git
cd secondstep-claude-skills
bash install-all.sh
```

### Manual Install

Copy any skill's contents to `~/.claude/skills/`:

```bash
cp -r skills/pmax-claude/pmax ~/.claude/skills/
cp -r skills/pmax-claude/skills/* ~/.claude/skills/
cp skills/pmax-claude/agents/*.md ~/.claude/agents/
```

---

## How Skills Work

Each skill follows a consistent architecture:

```
skill-name/
├── README.md              # What it does, commands, scoring
├── SKILL.md or */SKILL.md # Main orchestrator (routes commands)
├── skills/                # Sub-skills (specialized modules)
├── agents/                # AI agent personas
├── scripts/               # Python utilities
├── docs/                  # Reference documentation
├── templates/             # Output templates
├── install.sh             # One-command installer
├── uninstall.sh           # Clean removal
├── LICENSE                # MIT
└── requirements.txt       # Python dependencies
```

When you type a command like `/pmax audit`, the main SKILL.md routes it to the appropriate sub-skill, which may delegate to agents for parallel analysis.

---

## Requirements

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code)
- Python 3.8+ (for scoring scripts)
- Git

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome new skills, improvements to existing ones, and bug fixes.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv))
[Second Step](https://getsecondstep.com) — Performance Marketing & AI Automation

---

<p align="center">
  <em>Stop auditing manually. Let Claude do it.</em>
</p>
