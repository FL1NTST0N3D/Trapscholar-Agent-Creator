# Google Ads Copy — Main Skill Router

## Commands

Route user requests to the appropriate sub-skill:

| User Says | Route To |
|-----------|----------|
| `/copy generate` | `skills/copy-rsa-generator/SKILL.md` |
| `/copy headlines` | `skills/copy-headline-formulas/SKILL.md` |
| `/copy descriptions` | `skills/copy-description-writer/SKILL.md` |
| `/copy dki` | `skills/copy-dki-helper/SKILL.md` |
| `/copy strength` | `skills/copy-ad-strength/SKILL.md` |
| `/copy competitor` | `skills/copy-competitor-analysis/SKILL.md` |
| `/copy emotional` | `skills/copy-emotional-triggers/SKILL.md` |
| `/copy cta` | `skills/copy-cta-optimizer/SKILL.md` |
| `/copy test` | `skills/copy-ab-testing/SKILL.md` |
| `/copy report` | `skills/copy-report/SKILL.md` |

If the user says just `/copy` with no subcommand, show the command table and ask what they need.

## Required Inputs (Gather Before Any Generation)

Before generating any ad copy, ALWAYS collect:

1. **Business/Product**: What is being advertised?
2. **Target Audience**: Who sees the ad?
3. **Primary Keyword(s)**: What search terms trigger the ad?
4. **USP**: What makes this offer different? (Price, speed, quality, guarantee, etc.)
5. **Goal**: Leads, sales, calls, sign-ups?
6. **Landing Page URL** (optional): To align copy with page content

If the user provides a URL, read the landing page to extract USPs, offers, and tone.

## Copywriting Framework Reference

Use these frameworks systematically when generating ad copy. Never rely on a single framework — mix them for variety and Ad Strength.

| Framework | Structure | Best For |
|-----------|-----------|----------|
| **AIDA** | Attention - Interest - Desire - Action | General awareness + conversion |
| **PAS** | Problem - Agitate - Solve | Pain-point-driven services |
| **FAB** | Features - Advantages - Benefits | Product/feature-heavy offers |
| **Before-After-Bridge** | Current state - Desired state - How to get there | Transformation offers |
| **4Cs** | Clear - Concise - Compelling - Credible | All ad types (quality check) |
| **QUEST** | Qualify - Understand - Educate - Stimulate - Transition | Complex B2B/SaaS |
| **USP-Driven** | Lead with unique differentiator | Competitive markets |
| **Social Proof** | Reviews, numbers, awards, certifications | Trust-building |
| **Urgency/Scarcity** | Limited time, limited supply, deadlines | Promotional/seasonal |
| **Question-Based** | Ask the question the searcher has | High-intent keywords |
| **Number/Stat** | Lead with specific numbers | Data-driven audiences |
| **Comparison** | "Unlike X, we do Y" | Competitive positioning |
| **Risk Reversal** | Money-back, free trial, no commitment | High-consideration purchases |

## Google Ads Character Limits

CRITICAL — every piece of copy MUST respect these limits. Count characters carefully.

| Element | Max Characters | Notes |
|---------|---------------|-------|
| Headline | 30 | RSAs allow up to 15 headlines |
| Long Headline (PMax) | 90 | Performance Max only |
| Description | 90 | RSAs allow up to 4 descriptions |
| Display Path 1 | 15 | Appears after domain in URL |
| Display Path 2 | 15 | Second URL path segment |
| Business Name | 25 | Shows in some ad formats |
| Sitelink Title | 25 | Extension |
| Sitelink Description | 35 | 2 lines allowed |
| Callout | 25 | Extension |
| Structured Snippet Value | 25 | Extension |

## Character Counting Rules

- Spaces count as characters
- Punctuation counts (!, ?, &, etc.)
- DKI syntax `{KeyWord:Default}` — the DEFAULT TEXT is what counts for character limit
- Numbers and symbols each count as 1 character
- Trademark symbols (TM, R) count as characters

## Output Format

When generating ad copy, ALWAYS output in this format:

```
HEADLINE 1 (28 chars) [Framework: AIDA] [Pin: H1]
Get 50% Off Premium Widgets

HEADLINE 2 (26 chars) [Framework: Social Proof]
Trusted by 10,000+ Buyers

...

DESCRIPTION 1 (87 chars) [Framework: PAS]
Tired of unreliable widgets? Our premium line comes with lifetime warranty. Shop now.

DESCRIPTION 2 (82 chars) [Framework: FAB]
Aircraft-grade aluminum construction means 3x durability. Free shipping over $50.
```

Always include: character count, framework tag, and pin recommendation where applicable.

## Quality Checklist

Before delivering any ad copy, verify:

- [ ] All headlines are 30 characters or fewer
- [ ] All descriptions are 90 characters or fewer
- [ ] At least 3 different frameworks used across headlines
- [ ] At least 1 headline includes the primary keyword
- [ ] At least 1 headline includes a number or statistic
- [ ] At least 1 headline includes a CTA verb
- [ ] At least 1 description includes the primary keyword
- [ ] No two headlines are semantically identical
- [ ] Display paths are relevant and within 15 characters each
- [ ] Pin recommendations are included where beneficial
