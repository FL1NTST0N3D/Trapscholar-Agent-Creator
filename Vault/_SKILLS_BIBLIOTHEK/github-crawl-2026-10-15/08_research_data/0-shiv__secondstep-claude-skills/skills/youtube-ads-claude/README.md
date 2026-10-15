# YouTube Ads Audit & Optimization Skill for Claude Code

> YouTube is the world's second-largest search engine and most underutilized ad platform. This skill audits campaigns across TrueView, Bumper, Shorts & Demand Gen.

## Why YouTube Ads?

| Stat | Value |
|------|-------|
| Monthly Active Users | 2.5 Billion |
| Shorts Daily Views | 70 Billion |
| Video Ads CTR vs Banners | 27x Higher |
| Small Businesses Advertising | Only 9% |
| Average View Rate | 31.9% |
| Cost Per View (CPV) | $0.10 - $0.30 |
| Shorts CPM | ~$4.00 |
| Non-Skip In-Stream CPM | $4.00 - $10.00 |

YouTube reaches more 18-49 year-olds than any broadcast or cable TV network. Yet only 9% of small businesses run YouTube ads. This is the single biggest arbitrage opportunity in digital advertising right now.

## YouTube Ads Score (0-100)

Every audit produces a composite score across 8 dimensions:

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| Campaign Structure | 15% | Objective alignment, format mix, naming conventions |
| Creative Quality | 20% | Hook strength, ABCD compliance, CTA clarity |
| Targeting Precision | 15% | Audience layering, Custom Intent usage, exclusions |
| Bidding Strategy | 10% | Bid type alignment, conversion maturity, seasonal adjustments |
| Placement Hygiene | 10% | Channel exclusions, brand safety, inventory type |
| Remarketing Depth | 10% | Funnel stages, sequential messaging, list freshness |
| Shorts Readiness | 10% | Vertical creative, mobile-first, native feel |
| Measurement Setup | 10% | Conversion tracking, view-through windows, attribution |

**Score Ranges:**
- **90-100** — Elite. Top 2% of YouTube advertisers.
- **70-89** — Strong. Minor optimizations needed.
- **50-69** — Average. Significant improvement opportunities.
- **30-49** — Weak. Fundamental issues in strategy or setup.
- **0-29** — Critical. Campaign is likely wasting budget.

## Benchmarks Reference

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| View Rate (Skippable) | <20% | 20-31% | 31-45% | >45% |
| CPV | >$0.30 | $0.15-$0.30 | $0.10-$0.15 | <$0.10 |
| CTR (In-Stream) | <0.3% | 0.3-0.5% | 0.5-1.0% | >1.0% |
| CTR (In-Feed) | <0.5% | 0.5-1.0% | 1.0-2.0% | >2.0% |
| Shorts CPM | >$8.00 | $4.00-$8.00 | $2.00-$4.00 | <$2.00 |
| Non-Skip CPM | >$12.00 | $6.00-$12.00 | $4.00-$6.00 | <$4.00 |
| Conversion Rate | <0.5% | 0.5-1.5% | 1.5-3.0% | >3.0% |
| View-Through Conv Rate | <0.1% | 0.1-0.3% | 0.3-0.8% | >0.8% |

## Commands

| Command | Description |
|---------|-------------|
| `/yt audit` | Full YouTube campaign audit across all dimensions |
| `/yt creative` | Video ad creative scoring with ABCD framework |
| `/yt targeting` | Targeting strategy analysis and recommendations |
| `/yt shorts` | Shorts ad readiness assessment and optimization |
| `/yt bumper` | 6-second bumper ad strategy and sequential planning |
| `/yt bidding` | Bidding strategy analysis by campaign objective |
| `/yt placements` | Placement hygiene audit and brand safety review |
| `/yt remarketing` | Remarketing funnel analysis and sequential messaging |
| `/yt report` | Generate full YouTube audit report with scores |

## Quick Start

```bash
# Clone the repo
git clone https://github.com/0-shiv/youtube-ads-claude.git

# Run the installer
cd youtube-ads-claude
chmod +x install.sh
./install.sh

# Or manual install — copy to your Claude Code skills directory
cp -r youtube-ads-claude ~/.claude/skills/
```

## Usage

Once installed, use any command in Claude Code:

```
/yt audit

Paste your YouTube campaign data (export from Google Ads > Campaigns > Video campaigns):
- Campaign name, type, status
- Budget, bid strategy, bid amount
- Impressions, views, view rate, CPV
- Clicks, CTR, conversions, cost/conversion
- Audience segments applied
- Placement reports
```

## Project Structure

```
youtube-ads-claude/
├── README.md
├── SKILL.md                    # Main skill router
├── CLAUDE.md                   # Claude Code configuration
├── CONTRIBUTING.md             # Contribution guidelines
├── CHANGELOG.md                # Version history
├── LICENSE                     # MIT License
├── install.sh                  # Installation script
├── uninstall.sh                # Uninstallation script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── youtube/                    # Core YouTube ads logic
├── skills/                     # 9 sub-skills
│   ├── yt-campaign-audit/      # Full campaign audit
│   ├── yt-creative-scoring/    # Video creative analysis
│   ├── yt-targeting-strategy/  # Audience targeting
│   ├── yt-shorts-ads/          # Shorts ad optimization
│   ├── yt-bumper-ads/          # 6-second bumper strategy
│   ├── yt-bidding/             # Bid strategy analysis
│   ├── yt-placements/          # Placement hygiene
│   ├── yt-remarketing/         # Remarketing funnels
│   └── yt-report/              # Report generation
├── agents/                     # Autonomous audit agents
├── scripts/                    # Python analysis scripts
├── docs/                       # Documentation
└── assets/                     # Templates and resources
```

## Requirements

- Claude Code CLI
- Python 3.9+ (for analysis scripts)
- Google Ads API access (optional, for automated data pull)

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv))

## License

MIT License - see [LICENSE](LICENSE) for details.
