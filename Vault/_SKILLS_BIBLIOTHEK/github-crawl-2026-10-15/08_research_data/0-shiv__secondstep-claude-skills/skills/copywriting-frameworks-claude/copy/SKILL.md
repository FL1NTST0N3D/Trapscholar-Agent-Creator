# /copy — Copywriting Frameworks Router

## Trigger
When the user types `/copy <subcommand>`, route to the appropriate sub-skill.

## Routing Table

| Subcommand | Skill | Description |
|------------|-------|-------------|
| `aida` | `copy-aida` | AIDA framework (Attention-Interest-Desire-Action) |
| `pas` | `copy-pas` | PAS framework (Problem-Agitate-Solve) |
| `fab` | `copy-fab` | FAB framework (Features-Advantages-Benefits) |
| `bab` | `copy-bab` | BAB framework (Before-After-Bridge) |
| `4cs` | `copy-4cs` | 4Cs clarity check (Clear-Concise-Compelling-Credible) |
| `story` | `copy-storytelling` | StoryBrand + PASTOR + narrative frameworks |
| `power-words` | `copy-power-words` | 200+ categorized power words |
| `headlines` | `copy-headlines` | 50+ headline formulas with templates |
| `cta` | `copy-cta-formulas` | 30+ CTA formulas by objective |
| `objections` | `copy-objection-handling` | Top 10 objection handling patterns |
| `proof` | `copy-social-proof` | Social proof frameworks & templates |
| `report` | `copy-report` | Copy audit report with scoring |

## Behavior

1. If no subcommand is provided, display the routing table and ask the user which framework to use.
2. If the user provides context (product, audience, channel) along with the subcommand, pass that context to the sub-skill.
3. If the user is unsure which framework to use, recommend based on:
   - **Channel**: Google Ads = AIDA/PAS, Email = PAS/AIDA, Landing Page = PASTOR/AIDA, Social = SSS/BAB
   - **Objective**: Lead gen = PAS, Sales = PASTOR, Awareness = StoryBrand, Retention = BAB
   - **Audience temp**: Cold = PAS/BAB, Warm = AIDA/FAB, Hot = CTA/Objections

## Required Context (ask if not provided)

- **Product/Service**: What are we writing about?
- **Audience**: Who are we writing to?
- **Channel**: Where will this copy appear?
- **Objective**: What action do we want the reader to take?
- **Tone**: Formal, casual, urgent, playful, etc.

## Example Usage

```
/copy aida
Product: AI scheduling tool for dentists
Audience: Dental practice owners, 35-55
Channel: Google Ads RSA
Objective: Free trial signup
Tone: Professional but approachable
```

```
/copy pas
My SaaS product helps freelancers track time and invoice clients.
Target: Freelance designers and developers.
For a Facebook ad.
```

```
/copy report
[paste existing copy for audit]
```
