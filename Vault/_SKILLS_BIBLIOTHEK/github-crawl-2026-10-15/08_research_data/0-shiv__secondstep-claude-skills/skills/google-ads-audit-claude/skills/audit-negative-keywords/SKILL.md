---
name: audit-negative-keywords
description: Audits negative keyword strategy including N-gram-based candidate identification, coverage per campaign, cross-campaign conflicts, match type usage, shared negative lists, industry-specific pre-built lists, and search term waste quantification.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Negative Keyword Audit

## Overview

Negative keywords are the primary defense against wasted spend. A well-maintained negative keyword strategy typically saves 15-30% of account spend by preventing ads from showing on irrelevant searches. Conversely, a neglected negative keyword list means the account is bleeding budget on queries that will never convert.

**The negative keyword paradox:** They're one of the simplest optimizations in Google Ads, yet one of the most commonly neglected. Most accounts have fewer than 50 negatives when they should have 200-500+.

**Critical rule:** Negative keywords must be reviewed weekly for any campaign using broad or phrase match keywords. Exact match campaigns are inherently protected but still benefit from negatives on close variants.

## Audit Checks (20 Total)

### N-Gram Analysis for Negative Candidates (4 checks)

**Check 1: N-Gram Waste Identification**
- Pass: N-gram analysis has been performed on search term data (last 90 days); irrelevant n-grams identified and negative'd
- Fail: No evidence of systematic n-gram analysis; negatives added ad-hoc or not at all
- Scoring: 7 points
- Method: Extract all search terms → tokenize into 1/2/3-grams → aggregate spend + conversions per n-gram → flag n-grams with high spend, zero conversions, and irrelevant intent

**Check 2: High-Spend Zero-Conversion N-Grams**
- Pass: All n-grams spending > $50 (or 2x CPA) with zero conversions have been evaluated and negative'd if irrelevant
- Fail: Multiple high-spend zero-conversion n-grams still active in the account
- Scoring: 6 points

**Check 3: Intent-Mismatch N-Grams**
- Pass: Informational n-grams ("how to", "what is", "tutorial", "guide", "free") are negative'd on commercial campaigns
- Fail: Informational queries consuming significant budget on conversion-focused campaigns
- Scoring: 5 points

**Check 4: Competitor Brand N-Grams**
- Pass: Competitor brand names are negative'd unless running a deliberate competitor targeting strategy
- Fail: Competitor searches triggering ads unintentionally (typically low CTR and high CPC)
- Scoring: 3 points

### Negative Keyword Coverage (4 checks)

**Check 5: Negative Keyword Volume per Campaign**
- Pass: Each Search campaign has 50+ negative keywords (account-wide, including shared lists)
- Fail: Campaigns with fewer than 20 negatives (indicates neglected negative strategy)
- Scoring: 6 points
- Benchmark: Well-managed campaigns: 100-500 negatives | Average: 20-100 | Poor: < 20

**Check 6: Negative Keyword Freshness**
- Pass: Negatives added within the last 30 days (indicates active management)
- Fail: No negatives added in 60+ days (stale negative strategy)
- Scoring: 4 points

**Check 7: Brand Campaign Negative Protection**
- Pass: Brand campaigns have non-brand terms as negatives to prevent non-brand leakage
- Fail: Brand campaigns triggering on non-brand queries (wasting brand budget on generic terms)
- Scoring: 5 points

**Check 8: Non-Brand Campaign Brand Exclusion**
- Pass: Non-brand campaigns have brand terms as negatives to prevent brand cannibalization
- Fail: Brand terms triggering in non-brand campaigns (inflating non-brand metrics with easy brand conversions)
- Scoring: 4 points

### Cross-Campaign Negative Conflicts (3 checks)

**Check 9: Negative-Positive Keyword Conflicts**
- Pass: No negative keywords are blocking positive keywords in the same or other campaigns
- Fail: Negative keywords inadvertently blocking desired search terms
- Scoring: 7 points
- Detection method: Cross-reference all negative keywords against all positive keywords; flag any matches where the negative match type would block the positive keyword
- Example conflict: Negative broad match "marketing" blocking exact match "digital marketing services"

**Check 10: Cross-Campaign Negative Spillover**
- Pass: Campaign-level negatives don't inadvertently block queries that should go to other campaigns
- Fail: Over-zealous negatives in one campaign preventing traffic from reaching the correct campaign
- Scoring: 4 points

**Check 11: Negative Keyword Match Type Logic**
- Pass: Negative match types are used correctly — negatives are typically phrase or exact to avoid over-blocking
- Fail: Excessive broad match negatives (which block any query containing the word, including relevant variations)
- Scoring: 4 points
- Rules:
  - Negative broad match: Blocks any query containing ALL negative words (in any order)
  - Negative phrase match: Blocks queries containing the exact phrase
  - Negative exact match: Blocks only the exact query
  - NOTE: Negative keywords do NOT use close variants — "running shoe" negative won't block "running shoes" (must add both)

### Shared Negative Keyword Lists (2 checks)

**Check 12: Shared Negative List Usage**
- Pass: Shared negative keyword lists are used to apply account-wide negatives efficiently
- Fail: Same negatives manually added to individual campaigns instead of using shared lists
- Scoring: 4 points
- Best practice: Create shared lists by category (e.g., "Job Seekers", "Free/Cheap", "DIY/Tutorial", "Competitors", "Unrelated Services")

**Check 13: Shared List Organization**
- Pass: Shared lists are logically organized by theme and applied to appropriate campaigns
- Fail: One giant catch-all negative list or no shared lists at all
- Scoring: 2 points

### Industry-Specific Negative Keyword Lists (3 checks)

**Check 14: Industry-Relevant Negative Foundation**
- Pass: Account has industry-standard negative keywords applied
- Fail: Common industry irrelevant terms not excluded
- Scoring: 5 points

**Pre-Built Industry Negative Keyword Lists:**

**E-Commerce:**
free, cheap, discount code, coupon, clearance, used, refurbished, wholesale, bulk, DIY, homemade, recipe, how to make, tutorial, review, vs, comparison, alternative, reddit, forum, jobs, career, salary, hiring, internship, volunteer, PDF, download, template, open source, craigslist, ebay, amazon, walmart, alibaba, wish, return policy, complaint, lawsuit, scam, fake

**Legal / Law Firms:**
free consultation (if not offered), pro bono, legal aid, public defender, law school, paralegal jobs, attorney salary, bar exam, LSAT, legal internship, law clerk, how to sue, DIY legal, legal templates, free legal advice, reddit, avvo, nolo, quora, what is, definition, example, essay, research paper

**Healthcare / Medical:**
free, home remedy, natural cure, DIY, self-treat, symptoms, WebMD, Mayo Clinic, Wikipedia, medical school, nursing jobs, residency, MCAT, salary, how to become, volunteer, clinical trial, research study, definition, what is, causes of, images, pictures, YouTube

**SaaS / Software:**
free, open source, free trial (if not offered), cracked, pirated, torrent, github, tutorial, how to code, developer jobs, salary, internship, certification, course, vs, alternative, comparison, review, reddit, quora, stack overflow, API documentation, SDK, npm, template, boilerplate

**Real Estate:**
free, cheap, foreclosure (if not relevant), section 8, HUD, public housing, rent to own (if not offered), mobile home, trailer, tiny house, roommate, Zillow, Trulia, Craigslist, Airbnb, VRBO, real estate license, agent salary, broker exam, how to become, DIY, FSBO (if agent)

**Check 15: Negative Keyword Completeness for Business Model**
- Pass: Negatives cover all major irrelevant intent categories for the business (job seekers, info seekers, DIYers, wrong geography, wrong service)
- Fail: Major intent categories not excluded
- Scoring: 3 points
- Universal negative categories (apply to most businesses):
  - Job-related: jobs, careers, hiring, salary, internship, resume, glassdoor
  - Educational: how to, what is, tutorial, course, certification, definition, example
  - Free/cheap: free, cheap, discount, coupon, promo code
  - Informational: reddit, quora, forum, wiki, YouTube, blog, article
  - Competitor: [specific competitor brand names]
  - Negative geography: [locations you don't serve]

**Check 16: Seasonal/Trending Negative Updates**
- Pass: Negatives updated for seasonal irrelevant terms or trending queries that don't apply
- Fail: No seasonal negative keyword maintenance
- Scoring: 2 points

### Search Term Waste Calculation (4 checks)

**Check 17: Total Search Term Waste Quantification**
- Pass: Dollar amount wasted on irrelevant search terms in last 30/60/90 days is calculated
- Fail: No waste quantification
- Scoring: 5 points
- Calculation: Sum spend on all search terms categorized as irrelevant (not matching business intent)

**Check 18: Waste as Percentage of Total Spend**
- Pass: Irrelevant search term spend is < 10% of total spend
- Fail: > 20% of spend going to irrelevant search terms
- Scoring: 5 points
- Benchmark: Excellent: < 5% waste | Good: 5-10% | Average: 10-20% | Poor: > 20%

**Check 19: Waste Trend Direction**
- Pass: Waste percentage is declining over time (indicates active negative keyword management)
- Fail: Waste percentage stable or increasing (indicates neglected negative strategy)
- Scoring: 3 points

**Check 20: Preventable Waste Analysis**
- Pass: Analysis of how much of the waste could have been prevented with proper negatives (hindsight calculation)
- Fail: No analysis of preventable waste
- Scoring: 2 points
- Method: For each wasted search term, identify if a single negative keyword would have prevented it and calculate the savings

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | Comprehensive negative strategy with minimal waste |
| 75-89 | Good | Strong negative coverage with some gaps |
| 60-74 | Average | Basic negatives present but significant waste remains |
| 40-59 | Below Average | Neglected negative strategy causing substantial waste |
| 0-39 | Poor | Virtually no negative keyword management |

**Total possible points: 96** (normalized to 100-point scale)

## Output Format

```markdown
## Negative Keyword Audit Results

**Overall Score: [X]/100 — [Rating]**

### Waste Summary
| Period | Total Spend | Wasted Spend | Waste % |
|--------|------------|-------------|---------|
| Last 30 days | $X | $X | X% |
| Last 90 days | $X | $X | X% |

### Negative Coverage
| Campaign | Negatives Count | Shared Lists Applied | Last Updated |
|----------|----------------|---------------------|-------------|
| ... | ... | ... | ... |

### Top Negative Keyword Candidates
| Keyword/N-Gram | Search Term Spend | Conversions | Recommendation |
|---------------|------------------|-------------|----------------|
| "free" | $X | 0 | Add as phrase negative |
| "jobs" | $X | 0 | Add to shared list |
| ... | ... | ... | ... |

### Conflicts Found
| Negative | Blocked Positive Keyword | Campaign | Impact |
|----------|------------------------|----------|--------|
| ... | ... | ... | ... |

### Recommended Shared Negative Lists
1. [Job Seekers]: jobs, careers, hiring, salary, internship...
2. [Informational]: how to, what is, tutorial, guide...
3. [Free/Cheap]: free, cheap, discount, coupon...
4. [Industry-specific]: [list]

### Monthly Savings Potential: $[X]
```
