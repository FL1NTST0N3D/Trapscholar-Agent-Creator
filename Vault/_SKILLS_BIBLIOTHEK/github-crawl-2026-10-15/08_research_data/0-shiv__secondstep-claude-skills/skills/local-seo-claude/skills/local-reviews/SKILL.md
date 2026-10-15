# Local Reviews — Review Profile Analysis & Strategy

## Description

Analyzes a business's review profile across Google, Yelp, Facebook, and industry-specific platforms. Evaluates review count, average rating, review velocity, owner response rate, sentiment distribution, and competitive benchmarks. Reviews are the second most important local ranking factor (16% of the local algorithm) and the #1 factor in consumer trust.

## Command

```
/local reviews "Business Name"
/local reviews "Business Name" --competitors "Competitor 1, Competitor 2, Competitor 3"
```

## What Gets Analyzed

### 1. Review Volume & Rating (5 points)

| Metric | Benchmark | Points |
|--------|-----------|--------|
| Google review count | 50+ reviews = full marks | 2 |
| Average Google rating | 4.2+ stars | 1 |
| Multi-platform reviews | Present on 3+ platforms | 1 |
| Rating consistency | Within 0.3 stars across platforms | 1 |

**Review Count Benchmarks by Industry:**

| Industry | Minimum Competitive | Strong | Dominant |
|----------|-------------------|--------|----------|
| Restaurants | 50 | 150 | 500+ |
| Home Services | 25 | 75 | 200+ |
| Healthcare | 20 | 50 | 150+ |
| Legal | 15 | 40 | 100+ |
| Hotels/Lodging | 50 | 200 | 500+ |
| Retail | 20 | 60 | 200+ |
| Automotive | 30 | 100 | 300+ |

**Rating Impact:**
- 4.0-4.5 stars is the sweet spot for conversions (perceived as authentic)
- A perfect 5.0 can reduce trust (looks fake)
- Below 4.0 stars: 67% of consumers will not consider the business
- Each 0.1-star increase = ~5% increase in conversion rate

### 2. Review Velocity (4 points)

| Metric | Benchmark | Points |
|--------|-----------|--------|
| Reviews per month (last 6 months) | 4+ per month | 2 |
| Velocity trend | Increasing or stable | 1 |
| Recency | At least 1 review in last 7 days | 1 |

**Why Velocity Matters:**
- Google values fresh reviews over historical volume
- A business with 30 reviews in the last 6 months outranks one with 200 reviews but none recent
- Sudden drops in velocity signal problems to Google
- Sudden spikes can trigger spam filters

**Healthy Velocity Patterns:**
- Steady 4-8 reviews per month (for most local businesses)
- No month with zero reviews
- No single month with 50% of all reviews (looks gated/incentivized)

### 3. Owner Response Rate (4 points)

| Metric | Benchmark | Points |
|--------|-----------|--------|
| Response to negative reviews (1-2 stars) | 100% responded | 2 |
| Response to positive reviews (4-5 stars) | 50%+ responded | 1 |
| Response time | Within 24-48 hours | 1 |

**Response Best Practices:**
- Respond to ALL negative reviews within 24 hours
- Acknowledge the issue, apologize, offer to resolve offline
- Never argue, never reveal private information
- Include the business name and location naturally (helps SEO)
- Respond to at least 50% of positive reviews with personalized thanks
- Avoid copy-paste identical responses (Google notices)

**Negative Review Response Template:**
```
Thank you for sharing your experience, [Name]. We're sorry to hear that
[specific issue]. At [Business Name], we strive to [positive value].
We'd love the opportunity to make this right — please reach out to us
at [phone/email] so we can address this directly.
```

### 4. Sentiment Analysis (4 points)

| Metric | Benchmark | Points |
|--------|-----------|--------|
| Positive sentiment ratio | 80%+ positive | 1.5 |
| Common complaint themes | Identified and addressed | 1 |
| Keyword presence in reviews | Service/location keywords appear naturally | 1 |
| Photo reviews | 10%+ of reviews include photos | 0.5 |

**Sentiment Categories:**
- **Positive signals:** "friendly staff," "fast service," "great quality," "highly recommend"
- **Negative signals:** "rude," "waited too long," "overpriced," "never coming back"
- **Neutral signals:** factual descriptions, questions, moderate opinions

**Review Keyword Impact:**
- Reviews mentioning specific services help rank for those terms
- Reviews mentioning the city/neighborhood boost local relevance
- You cannot ask for specific keywords, but you can ask about specific experiences

### 5. Competitive Comparison (3 points)

| Metric | Benchmark | Points |
|--------|-----------|--------|
| Review count vs top 3 competitors | At or above median | 1 |
| Rating vs top 3 competitors | At or above median | 1 |
| Velocity vs top 3 competitors | At or above median | 1 |

**Competitive Analysis Process:**
1. Identify top 3 competitors in Google Maps local pack for primary keyword
2. Record each competitor's review count, rating, and last review date
3. Calculate monthly review velocity for each
4. Benchmark the target business against all three
5. Identify the gap to close (or the lead to maintain)

## Review Generation Strategy

### Ethical Review Solicitation

**Do:**
- Ask happy customers for reviews at the point of delight
- Send a follow-up email/SMS 1-2 hours after service completion
- Use a short URL or QR code that goes directly to the Google review form
- Train front-line staff to ask: "Would you mind sharing your experience on Google?"

**Do NOT:**
- Offer incentives for reviews (violates Google ToS)
- Use review gating (filtering who gets to leave a review)
- Buy reviews or use review farms
- Ask employees to leave reviews
- Review your own business

**Google Review Link Generator:**
```
https://search.google.com/local/writereview?placeid=[PLACE_ID]
```

### Review Diversification
- 70% of reviews on Google
- 15% on Yelp or industry-specific platform
- 10% on Facebook
- 5% on other platforms (BBB, Angi, etc.)

## Output Format

```
REVIEW ANALYSIS: [Business Name]
Score: [X]/20 ([Grade])

REVIEW SNAPSHOT:
  Google:   [X] reviews | [X.X] stars | [X] reviews/month
  Yelp:     [X] reviews | [X.X] stars
  Facebook: [X] reviews | [X.X] stars
  Total:    [X] reviews across [X] platforms

VELOCITY:
  [PASS] 6 reviews/month (last 6 months)
  [PASS] Most recent review: 2 days ago
  [WARN] Velocity declining — was 8/month 6 months ago

RESPONSE RATE:
  [PASS] 100% of negative reviews responded (12/12)
  [FAIL] Only 20% of positive reviews responded (need 50%+)
  [WARN] Average response time: 72 hours (target: 24-48h)

SENTIMENT:
  Positive: 82% | Neutral: 10% | Negative: 8%
  Top praise: "friendly staff" (23x), "fast service" (18x)
  Top complaints: "parking" (7x), "wait time" (5x)
  [PASS] No recurring unresolved complaint themes

COMPETITIVE BENCHMARK:
  | Business     | Reviews | Rating | Velocity |
  |-------------|---------|--------|----------|
  | You          | 87      | 4.4    | 6/mo     |
  | Competitor A | 124     | 4.2    | 4/mo     |
  | Competitor B | 65      | 4.6    | 3/mo     |
  | Competitor C | 203     | 4.1    | 8/mo     |
  [WARN] Behind Competitor C in volume — close the gap

PRIORITY ACTIONS:
1. [High] Increase positive review response rate to 50%+
2. [High] Reduce response time to under 48 hours
3. [Medium] Implement post-service review request via SMS
4. [Medium] Address "parking" complaints in review responses
5. [Low] Encourage reviews on Yelp to diversify platforms
```

## Common Review Issues

1. **Review gating** — Filtering unhappy customers away from review pages violates Google ToS and FTC guidelines
2. **Fake reviews** — Google's algorithm detects patterns; penalties include review removal and listing suspension
3. **No responses** — Signals the business does not care about customer feedback
4. **Review bombing** — Competitors or disgruntled employees leaving fake negatives; report to Google
5. **Incentivized reviews** — Offering discounts for reviews is a ToS violation on every major platform
6. **Stale profile** — No reviews in 90+ days makes the business look inactive or closed

## Author

Shivendra Rawat ([@0-shiv](https://github.com/0-shiv)) | [Second Step](https://getsecondstep.com)
