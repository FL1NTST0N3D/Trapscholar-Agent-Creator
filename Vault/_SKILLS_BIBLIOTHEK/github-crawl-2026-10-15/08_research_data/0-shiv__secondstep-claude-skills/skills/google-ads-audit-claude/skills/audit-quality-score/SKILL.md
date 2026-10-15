---
name: audit-quality-score
description: Deep analysis of Quality Score components (Expected CTR, Ad Relevance, Landing Page Experience), distribution patterns, trends, CPC impact quantification, and match-type-level QS scoring across the account.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Quality Score Audit

## Overview

Quality Score (QS) is Google's 1-10 rating of keyword quality based on three components: Expected Click-Through Rate, Ad Relevance, and Landing Page Experience. QS directly impacts Ad Rank and actual CPC — a keyword with QS 10 can pay 50% less per click than a keyword with QS 5 for the same position. This audit quantifies the cost of low Quality Scores and identifies specific actions to improve each component.

**The QS-CPC relationship:**
- QS 10: ~30% CPC discount vs average
- QS 7: Baseline (average CPC)
- QS 5: ~25% CPC premium
- QS 3: ~67% CPC premium
- QS 1: ~400% CPC premium

A single-point QS improvement on high-spend keywords can save thousands per month.

## Audit Checks (20 Total)

### QS Distribution Analysis (4 checks)

**Check 1: Overall QS Distribution Histogram**
- Pass: 60%+ of keywords (by spend) have QS 7 or above
- Fail: Less than 40% of keywords (by spend) have QS 7+
- Scoring: 8 points
- Benchmark: Top accounts: 70%+ at QS 7+ | Average: 50% | Poor: < 30%
- Method: Create distribution buckets [1-4, 5-6, 7-8, 9-10] and calculate keyword count AND spend percentage in each

**Check 2: Spend-Weighted QS Average**
- Pass: Spend-weighted average QS is 7.0 or above
- Fail: Spend-weighted average QS below 6.0
- Scoring: 7 points
- Calculation: Sum(QS * Spend per keyword) / Total Spend
- Benchmark: Excellent: 8+ | Good: 7-8 | Average: 5.5-7 | Poor: < 5.5

**Check 3: QS Null/Unrated Keywords**
- Pass: Less than 20% of active keywords show QS "—" (null/not enough data)
- Fail: Over 40% of keywords have no QS rating (indicates low-volume keyword bloat)
- Scoring: 3 points

**Check 4: Bottom Quartile QS Spend Concentration**
- Pass: Keywords with QS 1-4 consume less than 15% of total spend
- Fail: Keywords with QS 1-4 consume more than 25% of total spend
- Scoring: 7 points
- Benchmark: Every dollar spent on QS 1-4 keywords costs 2-5x more than it should

### QS Component Breakdown (4 checks)

**Check 5: Expected CTR Component Analysis**
- Pass: 70%+ of keywords rated "Above Average" or "Average" for Expected CTR
- Fail: Over 30% of keywords rated "Below Average" for Expected CTR
- Scoring: 5 points
- Fix indicators: Below Average Expected CTR → improve ad copy, test new headlines, improve offer/CTA
- Benchmark: This component is most influenced by historical CTR performance of the keyword and ad

**Check 6: Ad Relevance Component Analysis**
- Pass: 70%+ of keywords rated "Above Average" or "Average" for Ad Relevance
- Fail: Over 30% of keywords rated "Below Average" for Ad Relevance
- Scoring: 5 points
- Fix indicators: Below Average Ad Relevance → restructure ad groups for tighter themes, include keywords in ad headlines, improve keyword-to-ad mapping

**Check 7: Landing Page Experience Component Analysis**
- Pass: 70%+ of keywords rated "Above Average" or "Average" for Landing Page Experience
- Fail: Over 30% of keywords rated "Below Average" for Landing Page Experience
- Scoring: 5 points
- Fix indicators: Below Average Landing Page → improve page speed, mobile experience, content relevance, add keyword-relevant content, improve trust signals

**Check 8: Weakest Component Identification**
- Pass: Analysis identifies which of the three components is the primary drag on QS across the account
- Fail: No component-level analysis performed
- Scoring: 3 points
- Importance: Fixing the weakest component provides the highest ROI — a "Below Average" to "Average" improvement typically adds 1-2 QS points

### QS Trend Analysis (3 checks)

**Check 9: QS Trend Direction (30/60/90 day)**
- Pass: QS is stable or improving over the last 90 days
- Fail: QS declining over the last 90 days (indicates worsening ad/landing page performance or increased competition)
- Scoring: 5 points
- Method: Compare current QS distribution vs 30/60/90 days ago using QS historical data

**Check 10: QS Volatility Detection**
- Pass: QS is stable (less than 1-point fluctuation over 30 days for high-spend keywords)
- Fail: QS fluctuating by 2+ points on important keywords (indicates inconsistent ad serving or landing page issues)
- Scoring: 3 points

**Check 11: New Keyword QS Trajectory**
- Pass: Keywords added in last 30 days are achieving QS 6+ within 2 weeks
- Fail: New keywords stuck at QS 3-4 after 2+ weeks (indicates poor keyword-ad-landing page alignment)
- Scoring: 2 points

### CPC Impact Analysis (4 checks)

**Check 12: QS-Adjusted CPC Premium Calculation**
- Pass: Total monthly CPC premium from low QS is calculated and quantified
- Fail: No quantification of QS cost impact
- Scoring: 5 points
- Calculation method:
  - For each keyword: Actual CPC vs Estimated CPC at QS 7
  - QS Premium = Actual CPC * (1 - (QS/7)) approximately
  - More precise: Use the QS multiplier table below
  - Monthly QS Tax = Sum of all keyword-level premiums

**QS CPC Multiplier Table:**
| Quality Score | CPC Multiplier (vs QS 7 baseline) |
|--------------|-----------------------------------|
| 10 | 0.70x (30% discount) |
| 9 | 0.78x (22% discount) |
| 8 | 0.88x (12% discount) |
| 7 | 1.00x (baseline) |
| 6 | 1.25x (25% premium) |
| 5 | 1.50x (50% premium) |
| 4 | 1.67x (67% premium) |
| 3 | 2.00x (100% premium) |
| 2 | 2.50x (150% premium) |
| 1 | 4.00x (300% premium) |

**Check 13: Top 10 QS Improvement Opportunities**
- Pass: Top 10 keywords by "savings if QS improved" are identified with specific fix recommendations
- Fail: No prioritized QS improvement list
- Scoring: 4 points
- Method: Sort keywords by (Monthly Spend * QS Premium %) descending

**Check 14: QS Impact on Impression Share**
- Pass: Keywords with QS < 5 are analyzed for impression share lost to rank
- Fail: Low QS keywords showing > 40% impression share lost to rank with no action plan
- Scoring: 3 points

**Check 15: QS ROI Projection**
- Pass: Projected monthly savings from improving QS by 1-2 points on target keywords is calculated
- Fail: No ROI projection for QS improvement efforts
- Scoring: 3 points

### QS by Segment Analysis (5 checks)

**Check 16: QS by Match Type**
- Pass: QS analyzed by match type to identify patterns (exact typically highest, broad lowest)
- Fail: No match-type QS segmentation
- Scoring: 3 points
- Benchmark: Exact match keywords typically have 0.5-1.0 higher QS than broad match equivalents

**Check 17: QS by Campaign**
- Pass: Campaign-level average QS calculated to identify structural issues in specific campaigns
- Fail: No campaign-level QS analysis
- Scoring: 3 points

**Check 18: QS for Brand vs Non-Brand**
- Pass: Brand keywords have QS 8+ (expected); non-brand QS analyzed separately
- Fail: Brand keywords dragging up account average, masking poor non-brand QS
- Scoring: 4 points
- Benchmark: Brand QS should be 8-10; non-brand 6+ is good, 7+ is excellent

**Check 19: QS by Ad Group Size**
- Pass: Correlation between ad group keyword count and QS is analyzed (larger ad groups often have lower QS)
- Fail: No analysis of structural QS drivers
- Scoring: 2 points

**Check 20: QS for Top Spend Keywords**
- Pass: Top 20 keywords by spend all have QS 6+ (ideally 7+)
- Fail: High-spend keywords with QS < 5 (maximum waste)
- Scoring: 5 points
- Benchmark: Top spending keywords should be the first QS optimization priority

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | QS is a competitive advantage; minimal CPC premium |
| 75-89 | Good | Above-average QS with specific improvement targets |
| 60-74 | Average | QS is not a drag but not a differentiator |
| 40-59 | Below Average | Significant CPC premium from QS issues |
| 0-39 | Poor | QS is severely impacting performance and cost |

**Total possible points: 90** (normalized to 100-point scale)

## Benchmark Data

| Metric | Excellent | Good | Average | Poor |
|--------|-----------|------|---------|------|
| Spend-weighted avg QS | 8+ | 7-8 | 5.5-7 | < 5.5 |
| % keywords QS 7+ | > 70% | 55-70% | 40-55% | < 40% |
| % spend on QS 1-4 | < 5% | 5-15% | 15-30% | > 30% |
| Monthly CPC premium from low QS | < 5% | 5-12% | 12-25% | > 25% |
| Brand keyword avg QS | 9-10 | 8-9 | 7-8 | < 7 |
| Non-brand keyword avg QS | 7+ | 6-7 | 5-6 | < 5 |

## Output Format

```markdown
## Quality Score Audit Results

**Overall Score: [X]/100 — [Rating]**

### QS Distribution
| QS Range | Keyword Count | % of Spend | Avg CPC |
|----------|--------------|------------|---------|
| 9-10 | X | X% | $X |
| 7-8 | X | X% | $X |
| 5-6 | X | X% | $X |
| 1-4 | X | X% | $X |
| N/A | X | X% | $X |

### Component Weakness Heat Map
| Component | Above Avg | Average | Below Avg | Primary Issue? |
|-----------|----------|---------|-----------|---------------|
| Expected CTR | X% | X% | X% | Yes/No |
| Ad Relevance | X% | X% | X% | Yes/No |
| Landing Page | X% | X% | X% | Yes/No |

### Monthly QS Tax: $[X]
(Extra cost paid due to QS below 7)

### Top 10 QS Improvement Opportunities
| Keyword | Current QS | Spend | Monthly Savings if QS +2 | Fix |
|---------|-----------|-------|-------------------------|-----|
| ... | ... | ... | ... | ... |

### Recommendations
1. [Fix weakest component first]
2. [Priority keyword fixes]
3. [Structural changes]
```
