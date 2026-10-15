# LinkedIn B2B Ads Audit Skill for Claude Code

> **LinkedIn Ads deliver 113% ROAS for B2B SaaS -- outperforming Google (98%) and Meta (104%). This skill audits your B2B campaigns across 25+ checks.**

A comprehensive Claude Code skill that turns Claude into a LinkedIn Ads strategist. Run structured audits, get actionable recommendations, and benchmark your B2B campaigns against industry standards.

## Why LinkedIn for B2B?

| Metric | Value |
|--------|-------|
| LinkedIn Members | 1B+ professionals |
| Avg B2B CPL (Lead Gen Forms) | $75 - $150 |
| Document Ads Form Completion | 22.73% |
| LinkedIn ROAS (B2B SaaS) | 113% |
| Google ROAS (B2B SaaS) | 98% |
| Meta ROAS (B2B SaaS) | 104% |

## Key Benchmarks

| Metric | Benchmark Range |
|--------|----------------|
| CTR (Sponsored Content) | ~0.5% (0.4% - 0.7%) |
| CPC (Single Image) | $3 - $7 |
| CPL (Lead Gen Forms) | $75 - $600 (depends on targeting) |
| Video View Rate | 25% - 35% |
| Conversation Ad Open Rate | 50%+ |
| InMail Response Rate | 10% - 25% |

## Commands

| Command | Description |
|---------|-------------|
| `/li audit` | Full 25-point LinkedIn Ads health audit |
| `/li targeting` | Targeting layer analysis & ABM review |
| `/li lead-gen` | Lead Gen Form optimization audit |
| `/li formats` | Content format mix & performance review |
| `/li budget` | Budget allocation & CPL benchmark analysis |
| `/li audiences` | Matched Audiences & retargeting audit |
| `/li tracking` | Conversion tracking & attribution review |
| `/li report` | Generate full audit report with scores |

## LinkedIn Ads Health Score (0-100)

The audit produces a composite health score across 8 dimensions:

| Dimension | Weight | Max Points |
|-----------|--------|------------|
| Campaign Structure | 15% | 15 |
| Targeting Quality | 20% | 20 |
| Lead Gen Forms | 15% | 15 |
| Content Formats | 10% | 10 |
| Budget & CPL | 15% | 15 |
| Audience Building | 10% | 10 |
| Conversion Tracking | 10% | 10 |
| Reporting Setup | 5% | 5 |

**Score Interpretation:**
- **90-100**: Elite -- top 5% of LinkedIn advertisers
- **70-89**: Strong -- well-optimized with minor gaps
- **50-69**: Average -- significant optimization opportunities
- **30-49**: Weak -- major structural issues
- **0-29**: Critical -- fundamental setup problems

## Quick Start

```bash
# Clone the repo
git clone https://github.com/0-shiv/linkedin-ads-claude.git

# Install the skill
cd linkedin-ads-claude
chmod +x install.sh
./install.sh

# Run your first audit
# In Claude Code, type:
/li audit
```

## Project Structure

```
linkedin-ads-claude/
  README.md
  SKILL.md                          # Main skill definition
  CLAUDE.md                         # Claude Code project config
  CONTRIBUTING.md
  CHANGELOG.md
  LICENSE
  install.sh
  uninstall.sh
  requirements.txt
  .gitignore
  linkedin/                         # Core LinkedIn Ads logic
  skills/
    li-campaign-structure/SKILL.md  # Full-funnel campaign structure
    li-targeting/SKILL.md           # Targeting & ABM
    li-lead-gen-forms/SKILL.md      # Lead Gen Form optimization
    li-content-formats/SKILL.md     # Ad format selection
    li-budget-cpl/SKILL.md          # Budget & CPL benchmarks
    li-audience-building/SKILL.md   # Matched Audiences
    li-conversion-tracking/SKILL.md # Insight Tag & CAPI
    li-report/SKILL.md              # Audit report generation
  agents/
    linkedin-auditor.md             # Full audit agent
    linkedin-strategist.md          # Strategy recommendation agent
    linkedin-reporter.md            # Report generation agent
  scripts/
    li_health_score.py              # Health score calculator
    li_benchmark.py                 # Benchmark comparison engine
  docs/
    linkedin-ads-glossary.md        # LinkedIn Ads terminology
    funnel-framework.md             # Full-funnel B2B framework
    industry-benchmarks.md          # CPL/CTR by industry
    abm-playbook.md                 # Account-Based Marketing guide
  assets/
```

## Industry CPL Benchmarks

| Industry | CPL Range | Notes |
|----------|-----------|-------|
| Technology / SaaS | $100 - $200 | Lower with Document Ads |
| Financial Services | $150 - $300 | Compliance adds friction |
| Healthcare / Pharma | $200 - $400 | Narrow audiences |
| Manufacturing | $80 - $150 | Less competition |
| Professional Services | $75 - $175 | Broad targeting works |
| Education / EdTech | $50 - $120 | High volume available |
| Staffing / HR Tech | $100 - $250 | Competitive space |

## Requirements

- Claude Code CLI
- Python 3.9+ (for scoring scripts)
- LinkedIn Campaign Manager access (for live audits)

## License

MIT License - Shivendra Rawat 2026

## Author

**Shivendra Rawat** -- Second Step (getsecondstep.com)
