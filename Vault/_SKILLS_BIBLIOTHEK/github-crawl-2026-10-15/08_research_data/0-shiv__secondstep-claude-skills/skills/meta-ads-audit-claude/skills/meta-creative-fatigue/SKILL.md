# Meta Creative Fatigue Audit

## Command
`/meta creative`

## Description
Detects creative fatigue across Meta ad accounts by analyzing frequency trends, CTR decline curves, creative refresh cadence, format diversity, and A/B testing coverage. Creative fatigue is the single largest silent budget killer in Meta Ads — it costs advertisers an average 23% performance drop before they notice.

## Why Creative Fatigue Detection Matters

Meta's algorithm delivers your best-performing ads to your most receptive audiences. Over time, those audiences see the same ads repeatedly, leading to:

- **Banner blindness**: Users unconsciously ignore familiar ad creative
- **CTR decay**: Click-through rates decline 20-40% over 2-3 weeks for static images
- **CPM inflation**: Meta charges more to show fatigued ads (lower relevance = higher costs)
- **Negative feedback spikes**: Hide/report rates increase, damaging account quality
- **ROAS erosion**: Same spend, fewer conversions, higher cost per result

The average Meta ad has a **creative lifespan of 2-4 weeks** for prospecting and **1-2 weeks** for retargeting before fatigue sets in.

## Audit Checklist (35 Points)

### 1. Frequency Analysis (10 points)

Frequency is the average number of times each person in your audience sees your ad.

| Campaign Type | Healthy Frequency | Warning | Critical |
|--------------|-------------------|---------|----------|
| Awareness/Reach | < 2.0 / 7 days | 2.0-3.0 | > 3.0 |
| Prospecting (Conversions) | < 3.0 / 7 days | 3.0-4.0 | > 4.0 |
| Retargeting | < 5.0 / 7 days | 5.0-7.0 | > 7.0 |
| Retention/Upsell | < 4.0 / 7 days | 4.0-6.0 | > 6.0 |

**Checks:**
- [ ] **7-Day Frequency**: Pull frequency for all active ad sets over last 7 days
- [ ] **28-Day Frequency**: Compare 28-day frequency to spot accumulation
- [ ] **Frequency by Ad Set**: Identify ad sets with frequency > thresholds above
- [ ] **Frequency by Ad**: Individual ads within ad sets may have higher frequency than the set average
- [ ] **Frequency Trend**: Is frequency increasing week-over-week? (indicates audience saturation)
- [ ] **Frequency Cap Setup**: Check if frequency caps are configured (especially for awareness campaigns)
- [ ] **Reach vs Impressions Ratio**: Impressions / Reach > 4.0 in 7 days = over-delivery

### 2. CTR Decline Detection (8 points)

CTR (Click-Through Rate) is the first metric to decline when creative fatigues.

- [ ] **Day 1-3 CTR Baseline**: Establish initial CTR for each active ad
- [ ] **Current CTR vs Baseline**: Flag ads where CTR has dropped > 20% from baseline
- [ ] **CTR Trend (14 days)**: Plot CTR over last 14 days — look for consistent decline
- [ ] **CTR vs Industry Benchmark**: Compare to industry benchmarks (see main SKILL.md)
- [ ] **CTR by Placement**: Some placements fatigue faster (Feed > Stories > Reels)
- [ ] **Cost Per Click Trend**: Rising CPC alongside falling CTR = confirmed fatigue
- [ ] **Relevance Score / Quality Ranking**: Check if Meta's quality metrics are declining
- [ ] **Engagement Rate Decline**: Likes, comments, shares trending down = fatigue signal

**CTR Fatigue Classification:**
| CTR Change | Status | Action |
|-----------|--------|--------|
| Within 10% of baseline | Healthy | Monitor |
| 10-20% below baseline | Early fatigue | Prepare replacement creative |
| 20-40% below baseline | Active fatigue | Replace creative within 3 days |
| > 40% below baseline | Severe fatigue | Replace immediately |

### 3. Creative Refresh Scheduling (5 points)

- [ ] **Last Creative Refresh Date**: When was the most recent new creative added to each campaign?
- [ ] **Refresh Cadence**: How often are new creatives introduced? (Target: every 2-3 weeks)
- [ ] **Creative Pipeline**: Does the advertiser have a creative production pipeline?
- [ ] **Evergreen vs Seasonal**: Identify which ads are meant to be evergreen vs time-limited
- [ ] **Creative Retirement Policy**: Are old, fatigued ads being paused/archived regularly?

### 4. Format Diversity Analysis (7 points)

Meta rewards creative diversity. Accounts using 3+ formats see 20-30% lower CPMs.

| Format | Best For | Typical Lifespan |
|--------|----------|-----------------|
| Static Image | Product showcases, offers | 2-3 weeks |
| Single Video | Storytelling, demos, testimonials | 3-4 weeks |
| Carousel | Multiple products, features, steps | 3-4 weeks |
| Collection | E-commerce catalogs | 4-6 weeks |
| Instant Experience | Immersive brand stories | 4-6 weeks |
| Reels/Short Video | UGC, trends, quick hooks | 1-2 weeks |
| Slideshow | Low-budget video alternative | 2-3 weeks |

**Checks:**
- [ ] **Format Count**: How many unique formats are active? (Minimum 3 recommended)
- [ ] **Format Distribution**: Is budget heavily skewed to one format? (No single format > 60%)
- [ ] **Video Coverage**: At least 40% of active ads should be video (video gets priority delivery)
- [ ] **Carousel Usage**: Carousels typically have highest CTR — are they being tested?
- [ ] **Reels/Short Video**: Active Reels content for mobile-first placements?
- [ ] **Aspect Ratio Coverage**: 1:1, 4:5, 9:16 aspect ratios all covered?
- [ ] **Dynamic Creative**: Is dynamic creative optimization (DCO) being utilized?

### 5. A/B Testing Coverage (5 points)

- [ ] **Active Tests**: How many A/B tests are currently running?
- [ ] **Test Velocity**: How many tests completed in the last 30 days? (Target: 2+ per month)
- [ ] **Test Methodology**: Are tests using Meta's built-in A/B test tool or manual split testing?
- [ ] **Statistical Significance**: Are tests running long enough to reach significance? (Minimum 7 days)
- [ ] **Test Variables**: What is being tested? (Creative, copy, audience, placement — one variable per test)

## Creative Fatigue Detection Algorithm

The skill uses this logic to flag fatigued creatives:

```
FOR each active ad:
  1. Calculate baseline CTR (first 3 days of delivery)
  2. Calculate current 3-day rolling CTR
  3. Calculate CTR_decline = (baseline - current) / baseline
  4. Pull 7-day frequency
  5. Check cost_per_result trend (7-day vs 14-day)

  IF CTR_decline > 20% AND frequency > threshold:
    STATUS = "FATIGUED"
    PRIORITY = "Replace within 3 days"

  ELIF CTR_decline > 10% AND frequency approaching threshold:
    STATUS = "EARLY FATIGUE"
    PRIORITY = "Prepare replacement"

  ELIF ad_age > 21 days AND no_CTR_decline:
    STATUS = "MONITOR"
    PRIORITY = "Evergreen candidate — continue monitoring"

  ELSE:
    STATUS = "HEALTHY"
```

## Common Issues & Fixes

### Issue: All Ads Fatigued Simultaneously
**Symptom**: Every ad in the account shows fatigue signals at the same time
**Root Cause**: All ads launched on the same date with no staggered refresh
**Fix**: Stagger creative launches — introduce 2-3 new ads every 2 weeks rather than refreshing everything at once.

### Issue: High Frequency on Small Audiences
**Symptom**: Retargeting audience frequency > 10 in 7 days
**Root Cause**: Retargeting audience is too small (< 5,000 people)
**Fix**: Expand retargeting window (7-day to 30-day), add engagement-based audiences, or reduce retargeting budget.

### Issue: Only Static Images Used
**Symptom**: 100% of ads are single static images, CPMs are high
**Root Cause**: No video production capability
**Fix**: Use Meta's built-in video creation tools, create slideshow ads from existing images, or test UGC-style phone videos.

## Output Format

```
## Creative Fatigue Audit Results

**Score: XX/100** (Grade: X)
**Active Ads Analyzed: XX**
**Fatigued Ads: XX (XX%)**
**Format Diversity: X/7 formats active**
**Average Frequency: X.X (7-day)**

### Fatigue Status by Ad
| Ad Name | CTR Baseline | Current CTR | Decline | Frequency | Status |
|---------|-------------|-------------|---------|-----------|--------|
| Ad 1 | 1.45% | 0.92% | -37% | 4.2 | FATIGUED |
| Ad 2 | 2.10% | 1.85% | -12% | 2.1 | EARLY |
| Ad 3 | 1.80% | 1.75% | -3% | 1.8 | HEALTHY |

### Critical Findings (P0)
- [e.g., 6/10 ads show > 30% CTR decline with frequency > 4.0]

### Recommendations
1. [Action item — e.g., Replace top 3 fatigued ads within 48 hours]
2. [Action item — e.g., Add video and carousel formats to diversify]
```
