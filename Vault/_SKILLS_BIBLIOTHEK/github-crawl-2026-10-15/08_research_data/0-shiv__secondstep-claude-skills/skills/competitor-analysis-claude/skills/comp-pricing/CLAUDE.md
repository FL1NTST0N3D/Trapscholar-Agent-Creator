# Skill: Pricing Intelligence (`/comp pricing`)

## Purpose
Conduct thorough pricing analysis of competitors to understand their monetization strategy, packaging logic, and price positioning. This skill goes beyond simply listing prices — it deconstructs the economic architecture of a competitor's offering to reveal their strategic trade-offs, identify pricing vulnerabilities, and inform your own pricing decisions. Pricing is where strategy meets revenue, and understanding competitor pricing reveals their priorities, their target customer, and their growth model.

## When to Use
- Setting or revising your own pricing and packaging strategy
- Preparing for a competitive deal where price is a factor
- Evaluating whether a competitor is underpricing (land-grab) or overpricing (margin-maximizing)
- Analyzing free tier and freemium mechanics to design your own
- Understanding switching costs and lock-in strategies competitors employ
- Preparing pricing objection responses for your sales team

## Framework: 7-Dimension Pricing Analysis

### Dimension 1: Pricing Model Architecture
Identify the fundamental pricing mechanism:
- **Per-Seat / Per-User**: Price scales with team size. Favors adoption-led growth. Creates friction at scale.
- **Usage-Based**: Price scales with consumption (API calls, storage, sends). Aligns cost with value. Hard to predict bills.
- **Flat-Rate**: Single price for full access. Simple. Limits segmentation. Works for narrow products.
- **Freemium**: Free tier with paid upgrades. Optimizes for adoption. Conversion rate is the critical metric.
- **Tiered**: Multiple plans with feature gating. Standard SaaS approach. Balances segmentation with simplicity.
- **Hybrid**: Combines two or more models (e.g., per-seat + usage overage). Increasingly common. Complex to compare.
- **Custom / Quote-Based**: Enterprise pricing. High-touch sales. Hard to benchmark. Signal of deal flexibility.

### Dimension 2: Feature-by-Tier Matrix
Build a complete matrix showing which features are available at each pricing tier:

```
| Feature Category | Feature | Free | Starter | Pro | Enterprise |
|-----------------|---------|------|---------|-----|------------|
| Core | [Feature 1] | Y | Y | Y | Y |
| Core | [Feature 2] | Limited | Y | Y | Y |
| Advanced | [Feature 3] | N | N | Y | Y |
| Premium | [Feature 4] | N | N | N | Y |
```

Key questions to answer:
- What's the **upgrade trigger**? Which features force users from free to paid?
- What's the **expansion trigger**? Which features or limits drive upgrades to higher tiers?
- Is there a **cliff**? A huge feature gap between tiers that feels punitive?
- Are **essential features** gated behind premium tiers (potential customer frustration)?

### Dimension 3: Price-Per-Unit Economics
Calculate normalized pricing metrics for apples-to-apples comparison:
- **Price per user per month** (normalize annual to monthly)
- **Price per unit of value** (per contact, per project, per GB, per 1K API calls)
- **Effective discount for annual billing** (monthly price vs annual price spread)
- **Price per feature** (total price divided by feature count at that tier)
- **Break-even point**: At what usage level does a higher tier become cheaper?

### Dimension 4: Free Tier & Trial Analysis
If a free tier or trial exists, dissect it:
- **Duration**: Time-limited trial vs permanent free tier
- **Limitations**: User count, feature access, storage, usage caps
- **Conversion Mechanics**: What triggers the upgrade prompt? Time-based, usage-based, feature-based?
- **Data Portability**: Can free users export their data easily or is there lock-in?
- **Credit Card Required**: For trial, is CC needed upfront? (Higher conversion but lower trial starts)
- **Onboarding Investment**: How much setup is required before seeing value? (Higher setup = higher switching cost)

### Dimension 5: Hidden Costs & Surcharges
Look for costs not immediately visible on the pricing page:
- **Onboarding / Implementation fees**: One-time setup costs
- **Overage charges**: What happens when you exceed tier limits?
- **Add-on pricing**: Features sold separately from core tiers
- **Support tiers**: Is premium support an additional cost?
- **Training costs**: Required training or certification programs
- **Integration fees**: Costs for connecting to other tools
- **Data migration**: Costs to import existing data
- **Minimum commitments**: Minimum seats, minimum contract length, minimum spend

### Dimension 6: Switching Cost Analysis
Assess the total cost of switching from the competitor:
- **Financial**: Contract penalties, overlapping subscription periods, migration costs
- **Operational**: Data migration effort, workflow reconfiguration, integration rebuilding
- **Learning**: Team retraining time, productivity dip during transition
- **Political**: Internal stakeholder resistance, change management overhead
- **Data Risk**: Potential data loss or format incompatibility during migration
- **Customization Loss**: Custom configurations, automations, templates that don't transfer

### Dimension 7: Pricing Strategy Signals
Interpret what the pricing structure reveals about their strategy:
- **Land-and-expand**: Low entry price, high expansion revenue (usage-based or per-seat growth)
- **Premium positioning**: High prices, fewer features gated, emphasis on quality/support
- **Market share grab**: Aggressive pricing, generous free tier, below-cost entry points
- **Margin optimization**: High prices, minimal discounting, premium features at every tier
- **Platform play**: Low core price, revenue from ecosystem (marketplace, add-ons, integrations)

## Output Template

```markdown
# Pricing Intelligence: [Competitor Name]
**Date**: [YYYY-MM-DD]
**Pricing Page URL**: [URL]
**Currency**: [USD/EUR/etc.]

## Executive Summary
- [Pricing model type and strategic intent]
- [Key pricing vulnerability or advantage]
- [Recommended pricing counter-strategy]

## Pricing Model: [Type]
[Description of how they charge]

## Tier Comparison
| Tier | Monthly Price | Annual Price | Per-User? | Key Limits |
|------|-------------|-------------|-----------|------------|

## Feature-by-Tier Matrix
| Feature | [Tier 1] | [Tier 2] | [Tier 3] | [Tier 4] |
|---------|----------|----------|----------|----------|

## Price-Per-Unit Economics
| Metric | [Tier 1] | [Tier 2] | [Tier 3] | Your Price |
|--------|----------|----------|----------|------------|
| Per user/mo | | | | |
| Per [unit]/mo | | | | |
| Annual discount | | | | |

## Free Tier / Trial Analysis
[Detailed breakdown]

## Hidden Costs
| Cost Type | Amount | When Incurred |
|-----------|--------|---------------|

## Switching Cost Assessment
| Factor | Difficulty (1-5) | Notes |
|--------|------------------|-------|

## Strategic Interpretation
[What their pricing reveals about their strategy]

## Pricing Vulnerabilities
1. [Where their pricing creates buyer friction]
2. [Where you can win on price/value]

## Recommendations for Your Pricing
1. [Specific pricing action]
2. [Packaging recommendation]

## Sources
- [Pricing page, date accessed]
- [Any third-party pricing data sources]
```

## Best Practices
1. Always capture a snapshot of the pricing page with the date — pricing changes frequently and you need a baseline for comparison
2. Normalize all prices to monthly per-user (or per-unit) for valid comparison across different billing models
3. Calculate the total cost of ownership at 3 team sizes (5 users, 25 users, 100 users) to reveal how pricing scales
4. Look at the pricing page alongside the features page — sometimes feature access differs from what the pricing page implies
5. Check for recent pricing changes via the Wayback Machine — frequent changes signal pricing uncertainty
6. Read G2 and Capterra reviews specifically filtered to mentions of "pricing" and "cost" for buyer sentiment
7. Remember that listed prices are often not the actual prices paid — enterprise deals routinely include 20-40% discounts
