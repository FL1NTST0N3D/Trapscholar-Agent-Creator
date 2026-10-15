---
name: audit-ad-copy
description: Evaluates RSA completeness, headline diversity, pin strategy, Ad Strength distribution, dynamic keyword insertion, CTA analysis, emotional triggers, USP presence, competitive differentiation, character utilization, and A/B testing coverage.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Ad Copy Audit

## Overview

Ad copy is the first interaction a user has with your brand on Google. In the RSA (Responsive Search Ad) era, ad copy is both an art and a science — you provide the raw materials (headlines and descriptions) and Google's machine learning assembles the combinations. The quality, diversity, and relevance of your assets directly impact CTR, Quality Score, conversion rate, and ultimately cost per acquisition.

**Post-ETA reality:** Since June 2022, Responsive Search Ads (RSAs) are the only available text ad format. There is no going back to Expanded Text Ads (ETAs). Existing ETAs may still run but cannot be created or edited. This audit focuses entirely on RSA optimization.

**Ad Strength matters:** While Ad Strength is not a direct ranking factor, Google has confirmed that ads with "Excellent" Ad Strength get more impressions. The delta between "Poor" and "Excellent" Ad Strength can mean 10-15% more impressions served.

## Audit Checks (25 Total)

### RSA Completeness (4 checks)

**Check 1: Maximum Headlines Provided**
- Pass: RSAs have 15 headlines (maximum allowed) — gives Google maximum combinations to test
- Fail: RSAs with fewer than 10 headlines (limiting Google's ability to optimize combinations)
- Scoring: 6 points
- Benchmark: 15 headlines = optimal | 10-14 = acceptable | < 10 = underutilized
- Math: 15 headlines x 4 descriptions = 43,680 possible ad combinations (vs 3 headlines x 2 descriptions = 6 combinations for an ETA equivalent)

**Check 2: Maximum Descriptions Provided**
- Pass: RSAs have 4 descriptions (maximum allowed)
- Fail: RSAs with fewer than 3 descriptions
- Scoring: 4 points

**Check 3: RSA Per Ad Group**
- Pass: Each ad group has at least 1 RSA (maximum 3 RSAs per ad group recommended by Google)
- Fail: Ad groups with no active RSA or using only legacy ETAs
- Scoring: 5 points
- Note: Google recommends 1-3 RSAs per ad group. Having 2+ with different messaging themes allows A/B testing at the ad level

**Check 4: Character Limit Utilization**
- Pass: Headlines use 25+ of 30 characters; descriptions use 70+ of 90 characters (utilizing available space)
- Fail: Short headlines (< 20 chars) or short descriptions (< 60 chars) wasting valuable ad real estate
- Scoring: 3 points
- Benchmark: Ads using full character limits see 5-10% higher CTR on average

### Headline Diversity (4 checks)

**Check 5: Headline Theme Diversity**
- Pass: Headlines cover at least 5 distinct themes: keyword inclusion, benefits, features, CTA, social proof, urgency, brand name, USP, price/offer, question format
- Fail: Headlines are repetitive — same message rephrased multiple times
- Scoring: 6 points
- Required themes (at least 1 headline each):
  1. Keyword-focused (include target keyword)
  2. Benefit-focused (what the user gains)
  3. CTA-focused (action verb: "Get", "Start", "Book", "Request")
  4. Trust/proof (numbers, awards, years in business)
  5. Differentiator (what makes you unique vs competitors)

**Check 6: Headline Length Variation**
- Pass: Mix of short headlines (15-20 chars) and long headlines (25-30 chars) to fit different ad formats and positions
- Fail: All headlines the same length (limits where Google can place them)
- Scoring: 3 points

**Check 7: No Redundant Headlines**
- Pass: No two headlines convey the same message (e.g., "Free Shipping" and "We Ship Free" are redundant)
- Fail: Multiple headlines that are semantically identical (Google won't show them together, but they waste headline slots)
- Scoring: 4 points

**Check 8: Headline-Level Performance Review**
- Pass: Headline asset performance ratings reviewed (Best, Good, Low) and low-performers replaced
- Fail: No performance review of individual headline assets
- Scoring: 3 points
- Note: Google provides asset-level performance ratings after sufficient impressions (typically 5,000+)

### Pin Strategy (3 checks)

**Check 9: Pin Usage Assessment**
- Pass: Pins used strategically — only pin when legally required (disclaimers), for brand name in position 1, or for critical CTA
- Fail: Excessive pinning (3+ pins) that restricts Google's optimization ability
- Scoring: 5 points
- Rule of thumb: Every pin reduces potential ad combinations by ~70%. Pin 1 headline = 43,680 → ~13,000 combinations. Pin all 3 positions = ~1,000 combinations
- Google's guidance: "Pinning is not recommended unless necessary"

**Check 10: Position 1 Pin Strategy**
- Pass: If pinned, headline 1 contains the primary keyword or brand name (most visible position)
- Fail: Irrelevant or weak headline pinned to position 1
- Scoring: 3 points

**Check 11: Pin Impact on Ad Strength**
- Pass: Pinning has not dropped Ad Strength below "Good"
- Fail: Excessive pinning causing "Average" or "Poor" Ad Strength
- Scoring: 2 points

### Ad Strength Distribution (3 checks)

**Check 12: Ad Strength Distribution Across Account**
- Pass: 70%+ of RSAs have "Good" or "Excellent" Ad Strength
- Fail: Over 30% of RSAs have "Average" or "Poor" Ad Strength
- Scoring: 5 points
- Benchmark distribution (healthy account):
  - Excellent: 20-40%
  - Good: 40-50%
  - Average: 10-20%
  - Poor: 0-5%

**Check 13: "Poor" Ad Strength RSAs**
- Pass: Zero RSAs with "Poor" Ad Strength
- Fail: Any RSA with "Poor" Ad Strength (immediate fix required — add more headlines/descriptions, improve diversity)
- Scoring: 4 points

**Check 14: Ad Strength Improvement Actions**
- Pass: Google's specific Ad Strength suggestions have been reviewed and either implemented or deliberately rejected with reasoning
- Fail: Ad Strength suggestions ignored
- Scoring: 2 points

### Dynamic Keyword Insertion & Customizers (2 checks)

**Check 15: DKI Usage**
- Pass: Dynamic Keyword Insertion ({KeyWord:Default}) used in at least 1-2 headlines per RSA for relevance matching
- Fail: No DKI used when ad groups have multiple keyword themes, or DKI overused (every headline is DKI, reducing messaging control)
- Scoring: 3 points
- Best practice: 1-2 DKI headlines + 13 static headlines for balance between relevance and message control
- Caution: DKI can insert competitor names, misspellings, or long keywords — always set a good default text

**Check 16: Ad Customizer Usage**
- Pass: Ad customizers (countdown, location, IF functions) used where applicable for dynamic relevance
- Fail: Missing opportunity to use customizers (especially countdown for promotions, location for multi-geo)
- Scoring: 2 points

### CTA & Messaging Analysis (5 checks)

**Check 17: CTA Presence in Every RSA**
- Pass: Every RSA has at least 2 CTA-focused headlines and 1 CTA-focused description
- Fail: RSAs without clear calls to action
- Scoring: 4 points
- Effective CTAs: "Get Your Free Quote", "Schedule a Demo", "Shop Now — Free Shipping", "Call Today", "Start Your Free Trial", "Download the Guide"
- Weak CTAs: "Learn More", "Click Here", "Visit Our Website"

**Check 18: Emotional Trigger Analysis**
- Pass: Ad copy includes emotional triggers appropriate for the audience (urgency, exclusivity, fear of missing out, trust, curiosity)
- Fail: All copy is rational/feature-based with no emotional appeal
- Scoring: 3 points
- Emotional trigger examples:
  - Urgency: "Limited Time Offer", "Only 3 Left", "Ends Friday"
  - Exclusivity: "Members Only", "By Invitation", "Exclusive Access"
  - Trust: "Trusted by 10,000+ Businesses", "5-Star Rated", "Since 2005"
  - Curiosity: "See Why 90% of Users Switch", "The Secret to..."
  - Fear/Loss Aversion: "Don't Lose Another Lead", "Stop Wasting Ad Spend"

**Check 19: USP (Unique Selling Proposition) Presence**
- Pass: Ads clearly communicate what makes the business different from competitors (not just "best" or "great")
- Fail: Generic claims with no specific differentiator
- Scoring: 4 points
- Strong USPs: "3x Faster Than Competitors", "No Setup Fee — Ever", "Same-Day Installation", "The Only AI-Powered Solution For..."
- Weak USPs: "Best Service", "Top Quality", "Great Prices"

**Check 20: Competitive Differentiation**
- Pass: Ad copy addresses competitive landscape — why choose this business over alternatives
- Fail: Copy could be for any competitor in the space (completely interchangeable)
- Scoring: 3 points

**Check 21: Offer/Value Clarity**
- Pass: Ads clearly state what the user gets (offer, benefit, outcome) — not just what the company does
- Fail: Company-centric copy ("We are the leading...") instead of user-centric copy ("Get your custom plan in 24 hours")
- Scoring: 3 points

### A/B Testing (4 checks)

**Check 22: A/B Testing Coverage**
- Pass: At least 50% of ad groups have 2+ RSAs for A/B testing different messaging approaches
- Fail: Most ad groups with only 1 RSA (no testing possible)
- Scoring: 4 points

**Check 23: A/B Test Differentiation**
- Pass: A/B test variants have clearly different messaging strategies (e.g., benefit-focused vs feature-focused, emotional vs rational)
- Fail: A/B variants are nearly identical (testing minor word changes instead of meaningful differences)
- Scoring: 3 points

**Check 24: Test Winner Implementation**
- Pass: A/B tests with statistically significant winners have been acted on (winner kept, loser improved or replaced)
- Fail: Tests running indefinitely with no action on results
- Scoring: 3 points

**Check 25: Ad Rotation Setting**
- Pass: Ad rotation set to "Optimize" (Google's default, lets ML serve best-performing combinations)
- Fail: Set to "Do not optimize" without deliberate testing methodology
- Scoring: 2 points

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | Highly optimized ad copy driving strong CTR and engagement |
| 75-89 | Good | Solid ad copy with specific improvement areas |
| 60-74 | Average | Functional ads but missing diversity, emotion, or testing |
| 40-59 | Below Average | Significant ad copy weaknesses impacting CTR and QS |
| 0-39 | Poor | Ad copy requires complete overhaul |

**Total possible points: 93** (normalized to 100-point scale)

## Benchmark Data

| Metric | Excellent | Good | Average | Poor |
|--------|-----------|------|---------|------|
| Avg headlines per RSA | 15 | 12-14 | 8-11 | < 8 |
| Avg descriptions per RSA | 4 | 3-4 | 2-3 | < 2 |
| Ad Strength "Good"+ rate | > 80% | 60-80% | 40-60% | < 40% |
| Search CTR (non-brand) | > 8% | 5-8% | 3-5% | < 3% |
| Search CTR (brand) | > 15% | 10-15% | 5-10% | < 5% |
| RSAs per ad group | 2-3 | 1-2 | 1 | 0 or ETA only |

## Output Format

```markdown
## Ad Copy Audit Results

**Overall Score: [X]/100 — [Rating]**

### Ad Strength Distribution
| Rating | RSA Count | % of Total |
|--------|----------|-----------|
| Excellent | X | X% |
| Good | X | X% |
| Average | X | X% |
| Poor | X | X% |

### RSA Completeness
| Ad Group | RSAs | Avg Headlines | Avg Descriptions | Ad Strength | Pins |
|----------|------|--------------|-----------------|-------------|------|
| ... | ... | ... | ... | ... | ... |

### Messaging Analysis
- USP clearly communicated: Yes/No
- Emotional triggers used: [List]
- CTA strength: Strong/Average/Weak
- Competitive differentiation: Yes/No

### Top Recommendations
1. [Add headlines to reach 15/RSA]
2. [Improve diversity with X theme]
3. [Set up A/B tests in X ad groups]
4. [Fix "Poor" Ad Strength RSAs]
```
