# Competitor Analysis Claude

> Know your competitors better than they know themselves. Full competitive intelligence: teardowns, positioning maps, SWOT, pricing analysis & battlecards.

[![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-blueviolet?style=for-the-badge&logo=anthropic)](https://claude.ai)
[![Skills](https://img.shields.io/badge/Skills-9-orange?style=for-the-badge)](./skills/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)

---

## Why Competitive Intelligence Matters

- **90% of Fortune 500** companies invest in competitive intelligence programs
- **61% of businesses** say they've lost deals due to poor competitive knowledge
- Companies with CI programs are **2.3x more likely** to outperform their market
- **73% of sales reps** say they lose deals because they can't effectively position against competitors

Most teams rely on gut feelings and outdated spreadsheets. This skill gives Claude Code a systematic, repeatable framework for competitive analysis that turns raw data into strategic advantage.

---

## Commands

| Command | Description |
|---------|-------------|
| `/comp teardown` | Full competitor teardown: product, pricing, positioning, channels, audience |
| `/comp positioning` | Perceptual mapping & 2x2 positioning matrix with whitespace analysis |
| `/comp swot` | SWOT analysis with strategic implications matrix & action items |
| `/comp pricing` | Pricing comparison: tier matrix, per-unit analysis, hidden costs |
| `/comp ads` | Ad intelligence: Auction Insights, Ad Library analysis, spend estimates |
| `/comp content` | Content gap analysis: topic gaps, volume comparison, SERP overlap |
| `/comp tech` | Technology stack detection: CMS, analytics, martech, hosting |
| `/comp battlecard` | Sales battlecard: objection handling, win themes, landmines |
| `/comp report` | Full competitive intelligence report combining all analyses |

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/0-shiv/competitor-analysis-claude.git

# Navigate to directory
cd competitor-analysis-claude

# Install Python dependencies (for scripts)
pip install -r requirements.txt

# Add to your Claude Code project
cp -r skills/ /path/to/your/project/.claude/skills/
cp competitor/CLAUDE.md /path/to/your/project/.claude/
```

### Usage Examples

```
# Tear down a specific competitor
/comp teardown "Analyze Notion as a competitor to our project management tool"

# Generate a positioning map
/comp positioning "Map us against Asana, Monday, ClickUp on ease-of-use vs power"

# Create a sales battlecard
/comp battlecard "Build a battlecard for our sales team against HubSpot CRM"

# Full competitive report
/comp report "Complete CI report on the email marketing space: Mailchimp, ConvertKit, Beehiiv"
```

---

## Project Structure

```
competitor-analysis-claude/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── CLAUDE.md
├── competitor/
│   └── CLAUDE.md              # Root skill configuration
├── skills/
│   ├── comp-teardown/         # Full competitor teardown
│   │   └── CLAUDE.md
│   ├── comp-positioning/      # Perceptual mapping & positioning
│   │   └── CLAUDE.md
│   ├── comp-swot/             # SWOT analysis framework
│   │   └── CLAUDE.md
│   ├── comp-pricing/          # Pricing intelligence
│   │   └── CLAUDE.md
│   ├── comp-ads-intel/        # Ad spend & creative analysis
│   │   └── CLAUDE.md
│   ├── comp-content-gap/      # Content gap analysis
│   │   └── CLAUDE.md
│   ├── comp-tech-stack/       # Technology detection
│   │   └── CLAUDE.md
│   ├── comp-battlecard/       # Sales battlecard generator
│   │   └── CLAUDE.md
│   └── comp-report/           # Full CI report template
│       └── CLAUDE.md
├── agents/
│   ├── ci-researcher.md       # Research agent persona
│   ├── ci-analyst.md          # Analysis agent persona
│   └── ci-strategist.md       # Strategy agent persona
├── scripts/
│   ├── scrape_pricing.py      # Pricing page data extractor
│   ├── tech_detect.py         # Technology stack detector
│   └── serp_overlap.py        # SERP overlap calculator
├── docs/
│   ├── methodology.md         # CI methodology guide
│   ├── data-sources.md        # Where to find competitor data
│   ├── frameworks.md          # Analysis frameworks reference
│   └── templates.md           # Output templates & examples
└── assets/
    └── .gitkeep
```

---

## Skills Deep Dive

### 1. Competitor Teardown (`/comp teardown`)
Systematic deconstruction of a competitor's entire business: what they sell, to whom, how they position, where they market, and what they charge. The foundation for all other analyses.

### 2. Positioning Analysis (`/comp positioning`)
Build 2x2 perceptual maps to visualize competitive landscapes. Identify whitespace opportunities and category creation potential. Plot competitors on dimensions that matter to buyers.

### 3. SWOT Analysis (`/comp swot`)
Go beyond basic SWOT with a strategic implications matrix. Each quadrant generates specific, actionable recommendations rather than vague observations.

### 4. Pricing Intelligence (`/comp pricing`)
Feature-by-tier comparison matrices, price-per-unit analysis, packaging dissection, free tier evaluation, hidden cost discovery, and switching cost assessment.

### 5. Ad Intelligence (`/comp ads`)
Parse Google Ads Auction Insights, analyze Meta Ad Library creatives, estimate competitor ad spend, identify messaging themes, and map CTA patterns.

### 6. Content Gap Analysis (`/comp content`)
Find topics competitors rank for that you don't, compare content volume and cadence, analyze backlink profiles, and calculate SERP overlap percentages.

### 7. Tech Stack Detection (`/comp tech`)
Identify competitor technology choices: CMS, analytics, marketing automation, CRM, ad platforms, CDN, hosting. Reveals their operational maturity and investment level.

### 8. Sales Battlecard (`/comp battlecard`)
Generate ready-to-use battlecards for sales teams: competitive positioning statements, objection responses, feature comparison tables, win themes, proof points, and landmines to set.

### 9. CI Report (`/comp report`)
Comprehensive competitive intelligence report that synthesizes all analyses into an executive-ready document with strategic recommendations.

---

## Agents

| Agent | Role | Description |
|-------|------|-------------|
| CI Researcher | Data Collection | Gathers raw competitive data from public sources |
| CI Analyst | Analysis | Transforms raw data into structured insights |
| CI Strategist | Strategy | Converts insights into actionable recommendations |

---

## Scripts

| Script | Purpose |
|--------|---------|
| `scrape_pricing.py` | Extract and structure pricing page data |
| `tech_detect.py` | Detect technology stack from HTTP headers & page source |
| `serp_overlap.py` | Calculate SERP overlap between domains |

---

## Data Sources

The skill leverages publicly available data:
- Company websites & pricing pages
- Google Ads Auction Insights (from your Google Ads account)
- Meta Ad Library (ads.facebook.com)
- Job postings (reveal tech stack & priorities)
- G2, Capterra, TrustRadius reviews
- Crunchbase, PitchBook (funding & financials)
- BuiltWith, Wappalyzer (technology detection)
- SEMrush, Ahrefs, SimilarWeb (traffic & SEO)
- SEC filings, press releases, earnings calls
- LinkedIn company pages & employee profiles
- App Store / Play Store listings & reviews

---

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv))

Built for the competitive intelligence workflow at [Second Step](https://getsecondstep.com) -- turning competitor data into strategic advantage.

---

## License

MIT License. See [LICENSE](./LICENSE) for details.
