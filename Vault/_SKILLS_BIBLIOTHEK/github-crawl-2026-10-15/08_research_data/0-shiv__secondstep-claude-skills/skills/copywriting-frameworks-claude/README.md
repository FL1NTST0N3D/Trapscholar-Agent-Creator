# Copywriting Frameworks for Claude Code

> 25+ battle-tested copywriting frameworks inside Claude Code. Generate high-converting copy for ads, emails, landing pages, sales pages & social.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skills-blue)](https://docs.anthropic.com)
[![Frameworks](https://img.shields.io/badge/Frameworks-25%2B-green)]()

---

## Why This Exists

- **80% of people** only read the headline. Your headline IS your ad.
- **Top 10% of ads** have 5x higher CTR than the median. Frameworks get you there.
- **Words like "you"** increase conversions by 33%. Word choice is not optional.
- **Structured frameworks** beat "winging it" every single time. Period.

## Quick Start

```bash
# Install
git clone https://github.com/0-shiv/copywriting-frameworks-claude.git
cd copywriting-frameworks-claude
chmod +x install.sh && ./install.sh

# Or manual install
cp -r skills/ ~/.claude/skills/
cp -r agents/ ~/.claude/agents/
cp -r copy/ ~/.claude/copy/
```

## Commands (12 Total)

| Command | What It Does |
|---------|-------------|
| `/copy aida` | Generate copy using AIDA (Attention-Interest-Desire-Action) |
| `/copy pas` | Generate copy using PAS (Problem-Agitate-Solve) |
| `/copy fab` | Generate copy using FAB (Features-Advantages-Benefits) |
| `/copy bab` | Generate copy using BAB (Before-After-Bridge) |
| `/copy 4cs` | Apply the 4Cs framework (Clear-Concise-Compelling-Credible) |
| `/copy story` | Build brand narrative with StoryBrand + PASTOR |
| `/copy power-words` | Get 200+ categorized power words with usage examples |
| `/copy headlines` | Access 50+ headline formulas with fill-in templates |
| `/copy cta` | Get 30+ CTA formulas by objective |
| `/copy objections` | Handle top 10 universal buyer objections |
| `/copy proof` | Build social proof: testimonials, case studies, data |
| `/copy report` | Run a full copy audit with scoring |

## Frameworks Reference

| Framework | Best For | Pattern |
|-----------|----------|---------|
| AIDA | Full-funnel campaigns | Attention > Interest > Desire > Action |
| PAS | Pain-driven offers | Problem > Agitate > Solve |
| FAB | Product-focused copy | Features > Advantages > Benefits |
| BAB | Transformation stories | Before > After > Bridge |
| 4Cs | Clarity & polish | Clear > Concise > Compelling > Credible |
| QUEST | Long-form sales | Qualify > Understand > Educate > Stimulate > Transition |
| StoryBrand | Brand narrative | Character > Problem > Guide > Plan > Action > Success > Failure |
| PASTOR | Sales pages | Problem > Amplify > Story > Transformation > Offer > Response |
| SLAP | Quick-hit copy | Stop > Look > Act > Purchase |
| PPPP | Persuasion pieces | Picture > Promise > Prove > Push |
| Star-Chain-Hook | Emotional appeals | Star > Chain > Hook |
| SSS | Social media | Stop > Story > Sell |

## Agents

| Agent | Purpose |
|-------|---------|
| `copy-strategist` | Analyzes your product/audience, recommends the right framework |
| `copy-reviewer` | Reviews existing copy, scores it, suggests improvements |
| `copy-ab-tester` | Generates A/B test variants with statistical recommendations |

## Project Structure

```
copywriting-frameworks-claude/
├── README.md
├── CLAUDE.md
├── SKILL.md
├── LICENSE
├── install.sh
├── uninstall.sh
├── requirements.txt
├── .gitignore
├── CONTRIBUTING.md
├── CHANGELOG.md
├── copy/
│   └── SKILL.md
├── skills/
│   ├── copy-aida/SKILL.md
│   ├── copy-pas/SKILL.md
│   ├── copy-fab/SKILL.md
│   ├── copy-bab/SKILL.md
│   ├── copy-4cs/SKILL.md
│   ├── copy-storytelling/SKILL.md
│   ├── copy-power-words/SKILL.md
│   ├── copy-headlines/SKILL.md
│   ├── copy-cta-formulas/SKILL.md
│   ├── copy-objection-handling/SKILL.md
│   ├── copy-social-proof/SKILL.md
│   └── copy-report/SKILL.md
├── agents/
│   ├── copy-strategist.md
│   ├── copy-reviewer.md
│   └── copy-ab-tester.md
├── scripts/
│   ├── copy_generator.py
│   └── copy_analyzer.py
├── docs/
│   ├── framework-cheatsheet.md
│   ├── industry-examples.md
│   ├── testing-guide.md
│   └── prompt-engineering.md
└── assets/
    └── .gitkeep
```

## Usage Examples

### Generate Google Ads copy with AIDA
```
/copy aida
Product: SaaS project management tool
Audience: Engineering managers at Series B startups
Channel: Google Ads RSA
```

### Audit existing copy
```
/copy report
[paste your existing copy]
```

### Get headline ideas
```
/copy headlines
Topic: AI-powered email marketing
Benefit: 3x open rates
Audience: E-commerce founders
```

## Stats That Matter

| Metric | Impact |
|--------|--------|
| Headlines with numbers | 36% higher CTR |
| "You" in copy | 33% more conversions |
| Social proof near CTA | 15% lift in conversions |
| Urgency words | 27% higher click rates |
| Question headlines | 23% more engagement |
| Power words in subject lines | 12-25% higher open rates |

## Author

**Shivendra Rawat** ([@0-shiv](https://github.com/0-shiv))

Built for marketers, copywriters, and growth teams who want to ship better copy faster.

## License

[MIT](LICENSE) - Shivendra Rawat, 2026
