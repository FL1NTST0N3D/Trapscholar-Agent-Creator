# CLAUDE.md — Google Ads Copy Skill

## Project Overview

Claude Code skill that turns Claude into a senior Google Ads copywriter. Provides 10 slash commands for RSA generation, headline formulas, description writing, DKI setup, Ad Strength auditing, competitor analysis, emotional trigger scoring, CTA optimization, A/B testing, and full ad copy reports.

## Architecture

```
google-ads-copy-claude/
  SKILL.md                            # Main router — dispatches /copy <subcommand>
  skill.json                          # Manifest: commands, agents, scripts metadata
  skills/                             # Sub-skills (one SKILL.md per command)
    copy-rsa-generator/SKILL.md       # /copy generate — full RSA (15H + 4D)
    copy-headline-formulas/SKILL.md   # /copy headlines — 50+ formula variations
    copy-description-writer/SKILL.md  # /copy descriptions — conversion-optimized
    copy-dki-helper/SKILL.md          # /copy dki — Dynamic Keyword Insertion
    copy-ad-strength/SKILL.md         # /copy strength — Ad Strength audit
    copy-competitor-analysis/SKILL.md # /copy competitor — gap analysis
    copy-emotional-triggers/SKILL.md  # /copy emotional — power word scoring
    copy-cta-optimizer/SKILL.md       # /copy cta — CTA by industry
    copy-ab-testing/SKILL.md          # /copy test — A/B test variations
    copy-report/SKILL.md              # /copy report — full audit report
  agents/                             # Multi-step agent workflows
    full-rsa-workflow.md              # End-to-end RSA creation
    bulk-ad-generator.md              # RSAs for multiple ad groups
    competitor-to-ad.md               # Competitor analysis → differentiated copy
    copy-audit-agent.md               # Account-level copy audit
  scripts/                            # Python utilities
    char_counter.py                   # Character limit validation
    ad_strength_scorer.py             # Ad Strength scoring logic
    rsa_csv_exporter.py               # Export RSAs to CSV
  templates/                          # Output templates
    rsa-template.md                   # RSA output format
    audit-report-template.md          # Audit report format
    ab-test-plan-template.md          # A/B test plan format
    competitor-analysis-template.md   # Competitor analysis format
    rsa-data-sample.json              # Sample RSA data
  docs/                               # Reference documentation
    rsa-best-practices.md             # RSA optimization guide
    google-ads-policies-copy.md       # Policy compliance reference
    industry-benchmarks.md            # CTR/CPC benchmarks by industry
    pmax-copy-guide.md                # Performance Max copy guide
    extensions-copy-guide.md          # Ad extensions copy guide
```

## Commands

| Command | Description |
|---------|-------------|
| `/copy generate` | Generate a full RSA (15 headlines + 4 descriptions) |
| `/copy headlines` | 50+ headline variations using proven formulas |
| `/copy descriptions` | Conversion-optimized descriptions with USP + CTA |
| `/copy dki` | Dynamic Keyword Insertion syntax, rules, IF functions |
| `/copy strength` | Ad Strength audit with uniqueness and relevance scoring |
| `/copy competitor` | Competitor ad copy analysis and differentiation |
| `/copy emotional` | Emotional trigger scoring with 200+ power words |
| `/copy cta` | CTA optimization by industry |
| `/copy test` | A/B test variations with hypothesis framework |
| `/copy report` | Full ad copy audit report with scoring |

## Character Limits (Critical)

- Headline: 30 chars
- Description: 90 chars
- Long Headline (PMax): 90 chars
- Display Path: 15 chars each
- Business Name: 25 chars

## Development Rules

- Every generated headline MUST be 30 characters or fewer. Count carefully.
- Every generated description MUST be 90 characters or fewer.
- Always tag output with the copywriting framework used (AIDA, PAS, FAB, etc.).
- Always include character counts in output.
- Use at least 3 different frameworks across any set of headlines.
- Include pin recommendations (H1, H2, H3) where applicable.
- DKI syntax: `{KeyWord:Default}` — the default text counts toward the character limit.
- Do not modify existing SKILL.md files without explicit instruction.
- Python scripts in `scripts/` are standalone utilities with no external dependencies beyond the standard library.
