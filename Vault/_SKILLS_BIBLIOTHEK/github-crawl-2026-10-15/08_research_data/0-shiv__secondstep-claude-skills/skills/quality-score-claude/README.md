# Quality Score Claude

**Your Quality Score is costing you money. This skill shows you exactly how much — and how to fix it.**

A comprehensive Claude Code skill for deep Google Ads Quality Score analysis, optimization, and reporting. Built for performance marketers who refuse to overpay for clicks.

---

## The Problem

| Stat | Reality |
|------|---------|
| QS 5 vs QS 10 | **50% higher CPCs** |
| Annual waste on low QS keywords | **$1.5 billion** across advertisers |
| Advertisers actively optimizing QS | **Only 22%** |

Most advertisers treat Quality Score as a vanity metric. It is not. It is the single biggest lever you have to reduce cost per click without changing your bid.

## How Quality Score Affects Your Ad Rank

Google's Ad Rank formula:

```
Ad Rank = Max CPC Bid x Quality Score x Expected Impact of Extensions
```

Quality Score is a **multiplier** on your bid. A QS of 10 effectively doubles the power of every dollar you spend compared to a QS of 5.

## CPC Impact Table

| Quality Score | CPC Adjustment | Example (base $2.00) |
|:---:|:---:|:---:|
| 10 | **-50%** | $1.00 |
| 9 | **-33%** | $1.34 |
| 8 | **-17%** | $1.66 |
| 7 | Baseline | $2.00 |
| 6 | +25% | $2.50 |
| 5 | +67% | $3.34 |
| 4 | +100% | $4.00 |
| 3 | +200% | $6.00 |
| 2 | +300% | $8.00 |
| 1 | +400% | $10.00 |

A keyword with QS 1 costs you **5x more per click** than the same keyword at QS 10. That is not a rounding error. That is a budget fire.

## Quality Score Components

Quality Score is built from three components, each rated Above Average, Average, or Below Average:

1. **Expected Click-Through Rate (CTR)** — ~39% weight
2. **Landing Page Experience** — ~39% weight
3. **Ad Relevance** — ~22% weight

This skill breaks down each component, identifies the weakest links, and gives you an actionable fix list sorted by dollar impact.

---

## Commands

| Command | Description |
|---------|-------------|
| `/qs analyze` | Full QS analysis across your account |
| `/qs components` | Break down QS into 3 components per keyword |
| `/qs impact` | Calculate CPC waste from low Quality Scores |
| `/qs trends` | Track QS changes over time, spot declines |
| `/qs distribution` | Histogram of QS across all keywords |
| `/qs keywords` | Per-keyword audit sorted by savings potential |
| `/qs landing-pages` | Landing Page Experience analysis |
| `/qs relevance` | Ad Relevance deep dive |
| `/qs ctr` | Expected CTR analysis and benchmarks |
| `/qs optimize` | Actionable optimization playbook |
| `/qs report` | Full QS audit report with estimated savings |

## Installation

### From GitHub

```bash
claude skill install 0-shiv/quality-score-claude
```

### Manual

Clone this repository into your Claude Code skills directory:

```bash
git clone https://github.com/0-shiv/quality-score-claude.git ~/.claude/skills/quality-score-claude
```

## Project Structure

```
quality-score-claude/
├── README.md
├── SKILL.md                          # Main skill definition
├── qs/                               # Core QS logic
├── skills/                           # 10 sub-skills
│   ├── qs-component-analysis/        # Component breakdown
│   ├── qs-cpc-impact/                # CPC waste calculator
│   ├── qs-trend-tracker/             # QS trend monitoring
│   ├── qs-distribution/              # QS histogram analysis
│   ├── qs-keyword-level/             # Per-keyword audit
│   ├── qs-landing-page/              # Landing page factors
│   ├── qs-ad-relevance/              # Ad relevance analysis
│   ├── qs-expected-ctr/              # Expected CTR factors
│   ├── qs-optimizer/                 # Optimization playbook
│   └── qs-report/                    # Audit report generator
├── agents/                           # Agent definitions
├── scripts/                          # Python analysis scripts
├── templates/                        # Report templates
├── docs/                             # Documentation
└── assets/                           # Static assets
```

## Requirements

- Claude Code CLI
- Python 3.9+ (for analysis scripts)
- Google Ads API access or CSV export capability

## Data Input

This skill works with:
- **Google Ads CSV exports** — Download from Google Ads UI (Keywords tab, modify columns to include QS components)
- **Google Ads API** — Direct API connection for automated analysis
- **Manual input** — Paste keyword data directly into the conversation

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv))

Built at [Second Step](https://getsecondstep.com) — Performance marketing, powered by AI.

## License

MIT
