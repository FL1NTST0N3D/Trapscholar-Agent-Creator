# Google Ads Copy — Claude Code Skill

> Stop writing mediocre Google Ads copy. 25+ proven frameworks, RSA optimization, headline formulas & Ad Strength maximizer for Claude Code.

## The Problem

- **90% of RSAs** have Ad Strength below "Good" — Google penalizes them with lower impressions
- **Headlines account for 80%** of ad performance — yet most advertisers phone them in
- **Top 10% of ads** achieve 5x CTR compared to average — the difference is systematic copywriting frameworks

This skill turns Claude Code into your senior Google Ads copywriter. Every headline follows proven formulas. Every description is conversion-optimized. Every RSA hits "Excellent" Ad Strength.

## Commands

| Command | What It Does |
|---------|-------------|
| `/copy generate` | Generate a full RSA (15 headlines + 4 descriptions) with framework tagging |
| `/copy headlines` | Get 50+ headline variations using proven formulas |
| `/copy descriptions` | Write conversion-optimized descriptions with USP + CTA |
| `/copy dki` | Dynamic Keyword Insertion setup — syntax, rules, IF functions, countdowns |
| `/copy strength` | Ad Strength audit — uniqueness, keyword relevance, CTA diversity scoring |
| `/copy competitor` | Analyze competitor ad copy, find gaps, build differentiation |
| `/copy emotional` | Score ads for emotional triggers using 200+ power words |
| `/copy cta` | CTA optimization — which CTAs work for which industries |
| `/copy test` | Generate A/B test variations with hypothesis framework |
| `/copy report` | Full ad copy audit report with scoring and recommendations |

## Character Limits Quick Reference

| Element | Max Characters |
|---------|---------------|
| Headline | 30 |
| Long Headline (PMax) | 90 |
| Description | 90 |
| Display Path (each) | 15 |
| Business Name | 25 |

## Installation

```bash
# Add to your Claude Code project
claude skill install 0-shiv/google-ads-copy-claude
```

Or manually add to `.claude/skills/`:

```bash
git clone https://github.com/0-shiv/google-ads-copy-claude.git .claude/skills/google-ads-copy
```

## Skill Architecture

```
google-ads-copy-claude/
  SKILL.md                          # Main router + framework reference
  skills/
    copy-rsa-generator/SKILL.md     # Full RSA generation
    copy-headline-formulas/SKILL.md # 50+ headline formulas
    copy-description-writer/SKILL.md# Description optimization
    copy-dki-helper/SKILL.md        # Dynamic Keyword Insertion
    copy-ad-strength/SKILL.md       # Ad Strength maximizer
    copy-competitor-analysis/SKILL.md# Competitor copy analysis
    copy-emotional-triggers/SKILL.md# Power words & emotional scoring
    copy-cta-optimizer/SKILL.md     # CTA analysis by industry
    copy-ab-testing/SKILL.md        # A/B test framework
    copy-report/SKILL.md            # Audit report generator
  agents/                           # Multi-step agent workflows
  scripts/                          # Python utilities
  templates/                        # Output templates
  docs/                             # Reference documentation
```

## Frameworks Included

AIDA, PAS, FAB, Before-After-Bridge, 4Cs (Clear-Concise-Compelling-Credible), QUEST, USP-Driven, Social Proof, Urgency/Scarcity, Question-Based, Number/Stat-Based, Comparison, and more.

## Who This Is For

- Google Ads managers writing RSAs at scale
- Agencies managing 10+ client accounts
- Freelancers who need "Excellent" Ad Strength on every RSA
- Performance marketers who want systematic, repeatable copy frameworks

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv))
Founder, [Second Step](https://getsecondstep.com) — Performance Marketing & AI Automation

---

*Built for Claude Code. Works with any Google Ads account structure.*
