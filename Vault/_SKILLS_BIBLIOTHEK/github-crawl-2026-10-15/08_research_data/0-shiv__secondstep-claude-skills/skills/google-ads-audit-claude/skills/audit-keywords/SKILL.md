---
name: audit-keywords
description: Comprehensive keyword analysis including match type distribution, search term relevancy, cannibalization detection, duplicate identification, N-gram analysis, and keyword-to-ad-group relevance scoring across the entire account.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Keyword Audit

## Overview

Keywords are the targeting backbone of Search campaigns. A poorly managed keyword portfolio bleeds budget through irrelevant traffic, internal competition (cannibalization), and missed opportunities. This skill performs a deep-dive analysis across match types, search terms, ad group relevance, and performance metrics to identify waste and unlock growth.

The keyword audit answers three core questions:
1. Are you targeting the right keywords for your business?
2. Are your keywords organized efficiently to maximize Quality Score?
3. Is your search term traffic relevant and converting?

## Audit Checks (35 Total)

### Match Type Distribution (5 checks)

**Check 1: Match Type Mix Analysis**
- Pass: Account has a deliberate match type strategy — not 100% broad match without smart bidding
- Fail: 100% broad match with manual CPC or Max Clicks (broad match requires smart bidding to work well)
- Scoring: 5 points
- Benchmark: Healthy distribution for most accounts — 30-40% exact, 30-40% phrase, 20-30% broad (with smart bidding)

**Check 2: Broad Match + Smart Bidding Pairing**
- Pass: All broad match keywords are paired with tCPA, tROAS, or Max Conversions bidding
- Fail: Broad match keywords running under Manual CPC or Max Clicks
- Scoring: 5 points
- Benchmark: Broad match without smart bidding typically wastes 30-50% of spend on irrelevant queries

**Check 3: Exact Match Coverage for Top Converters**
- Pass: Top 20 converting search terms have exact match keyword versions
- Fail: High-converting search terms only captured by broad/phrase match (missing bid control)
- Scoring: 4 points

**Check 4: Match Type Performance Comparison**
- Pass: Performance (CPA, ROAS, CVR) tracked and compared across match types
- Fail: No performance differentiation by match type
- Scoring: 3 points

**Check 5: Single Keyword Ad Groups (SKAGs) Assessment**
- Pass: If using SKAGs, they serve a clear purpose; if not, ad groups have tight thematic grouping (5-20 keywords)
- Fail: Ad groups with 50+ unrelated keywords, or excessive SKAGs creating management overhead
- Scoring: 3 points

### Search Term Relevancy (6 checks)

**Check 6: Search Term Relevancy Rate**
- Pass: 80%+ of search terms (by spend) are relevant to the business
- Fail: Less than 70% relevancy rate by spend
- Scoring: 5 points
- Benchmark: Top accounts: 90%+ relevancy | Average: 75% | Poor: < 60%

**Check 7: Search Term to Keyword Mapping Accuracy**
- Pass: Search terms trigger the most relevant keyword in the account
- Fail: Search terms consistently triggering wrong keywords (mapping issues)
- Scoring: 4 points

**Check 8: High-Spend Zero-Conversion Search Terms**
- Pass: Search terms spending > 2x target CPA with zero conversions are identified and negative'd
- Fail: Multiple search terms with significant spend and no conversions still active
- Scoring: 5 points
- Benchmark: Any search term spending > 3x CPA with 0 conversions should be added as negative

**Check 9: Search Term Coverage (Hidden Terms)**
- Pass: Less than 30% of search term report is "(other)" / hidden terms
- Fail: Over 40% of impressions are from hidden search terms (common with broad match)
- Scoring: 3 points

**Check 10: Brand vs Non-Brand Search Term Leakage**
- Pass: Brand terms trigger brand campaigns; non-brand terms trigger non-brand campaigns
- Fail: Significant cross-contamination between brand and non-brand
- Scoring: 4 points

**Check 11: Search Term Intent Alignment**
- Pass: Search terms match the funnel stage of the campaign (informational vs transactional)
- Fail: Informational queries (e.g., "what is...", "how to...") triggering high-intent commercial campaigns
- Scoring: 3 points

### Keyword Cannibalization Detection (5 checks)

**Check 12: Cross-Campaign Keyword Overlap**
- Pass: Same keyword does not exist in multiple campaigns targeting the same location
- Fail: Duplicate keywords across campaigns compete against each other in auction
- Scoring: 5 points
- Benchmark: Cannibalization typically increases CPC by 10-25% on affected keywords

**Check 13: Cross-Ad-Group Keyword Overlap**
- Pass: No duplicate keywords within the same campaign across different ad groups
- Fail: Same keyword in multiple ad groups within one campaign
- Scoring: 4 points

**Check 14: Match Type Overlap Within Ad Group**
- Pass: If same root keyword exists in multiple match types, they're in the same ad group with proper negatives
- Fail: Same keyword in exact + broad across different ad groups without negative keyword isolation
- Scoring: 3 points

**Check 15: Cannibalization Impact Quantification**
- Pass: Any identified cannibalization has quantified CPC/CPA impact
- Fail: Cannibalization exists but impact not measured
- Scoring: 3 points

**Check 16: Priority Keyword Auction Conflict**
- Pass: High-priority keywords have no internal competition; lower-priority variants are negative'd appropriately
- Fail: Multiple keywords compete for same search queries, splitting conversion data
- Scoring: 3 points

### Duplicate Keyword Analysis (3 checks)

**Check 17: Exact Duplicate Keywords**
- Pass: No exact duplicate keywords (same keyword, same match type) across the account
- Fail: Exact duplicates found, causing internal auction competition
- Scoring: 4 points

**Check 18: Near-Duplicate Keywords**
- Pass: Near-duplicates (e.g., "running shoes" vs "shoes running") consolidated
- Fail: Multiple near-duplicates splitting data and creating inefficiency
- Scoring: 3 points

**Check 19: Close Variant Consolidation**
- Pass: Close variants (plurals, misspellings, reordering) accounted for — no unnecessary keyword bloat
- Fail: Excessive keyword variations that Google already matches via close variants
- Scoring: 2 points

### Low-Performing Keyword Analysis (5 checks)

**Check 20: Low Impression Share Keywords**
- Pass: Keywords with < 10% impression share are reviewed for bid/budget issues or relevance
- Fail: Multiple keywords with minimal impression share and no optimization plan
- Scoring: 3 points

**Check 21: High-Spend Low-Conversion Keywords**
- Pass: Keywords spending > 3x CPA with < 1 conversion in 30 days are paused or adjusted
- Fail: Keywords with significant spend and no conversions still active beyond 30 days
- Scoring: 5 points

**Check 22: Zero-Impression Keywords (30+ days)**
- Pass: Keywords with 0 impressions for 30+ days are reviewed (may indicate low search volume, disapproval, or outbid)
- Fail: Large number of zero-impression keywords cluttering the account
- Scoring: 2 points

**Check 23: Below-First-Page-Bid Keywords**
- Pass: Keywords below first page bid are either increased or paused if not strategically valuable
- Fail: Multiple keywords running below first page bid with no action taken
- Scoring: 2 points

**Check 24: Keyword Status Review**
- Pass: All active keywords have "Eligible" status; any issues (low search volume, disapproved, below bid) addressed
- Fail: Multiple keywords with status issues unresolved
- Scoring: 2 points

### Keyword-to-Ad-Group Relevance (5 checks)

**Check 25: Thematic Tightness Score**
- Pass: Each ad group contains keywords with a single, clear theme (semantic similarity > 80%)
- Fail: Ad groups mix unrelated themes (e.g., "plumber" and "electrician" in same ad group)
- Scoring: 5 points
- Benchmark: Tight ad groups = higher QS, higher CTR, lower CPC (typically 15-30% CPC improvement)

**Check 26: Keywords Per Ad Group Count**
- Pass: 5-20 keywords per ad group (optimal range)
- Fail: Ad groups with 1 keyword (over-segmented) or 50+ keywords (too broad)
- Scoring: 3 points
- Benchmark: Optimal: 5-20 | Acceptable: 3-30 | Poor: 1-2 or 30+

**Check 27: Keyword-to-Ad Headline Relevance**
- Pass: At least one RSA headline contains or closely matches the ad group's primary keyword
- Fail: Ad headlines don't reference the keyword theme of the ad group
- Scoring: 4 points

**Check 28: Keyword-to-Landing-Page Relevance**
- Pass: Keywords point to landing pages that match their intent and include the keyword theme
- Fail: Generic landing pages used across all keyword themes
- Scoring: 4 points

**Check 29: Ad Group Count per Campaign**
- Pass: 5-20 ad groups per campaign (manageable with distinct themes)
- Fail: Campaigns with 1 ad group (underutilized) or 50+ ad groups (unmanageable)
- Scoring: 2 points

### N-Gram Analysis (6 checks)

**Check 30: Single-Word N-Gram Analysis**
- Pass: Top single-word n-grams in search terms are all relevant to the business
- Fail: High-frequency irrelevant single words appearing across search terms (e.g., "free", "jobs", "salary" for a SaaS product)
- Scoring: 3 points

**Check 31: Two-Word N-Gram Analysis**
- Pass: Two-word n-grams identify clear theme clusters aligned with ad groups
- Fail: Irrelevant two-word combinations consuming significant spend
- Scoring: 3 points

**Check 32: Three-Word N-Gram Analysis**
- Pass: Three-word n-grams surface high-intent phrases that should be exact match keywords
- Fail: Missed opportunities — high-converting 3-word phrases not added as keywords
- Scoring: 3 points

**Check 33: Negative Keyword Candidates from N-Grams**
- Pass: N-gram analysis has been used to systematically identify negative keyword candidates
- Fail: No evidence of N-gram-driven negative keyword strategy
- Scoring: 3 points

**Check 34: N-Gram Performance Segmentation**
- Pass: N-grams are analyzed by conversion rate and CPA, not just volume
- Fail: N-gram analysis (if any) only looks at impressions/clicks, not conversions
- Scoring: 2 points

**Check 35: Emerging Query Trends**
- Pass: New search term patterns (emerging n-grams) identified and incorporated into keyword strategy
- Fail: No monitoring of emerging search trends from search term data
- Scoring: 2 points

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | Highly optimized keyword portfolio with minimal waste |
| 75-89 | Good | Well-managed keywords with specific improvement areas |
| 60-74 | Average | Functional but significant optimization opportunities exist |
| 40-59 | Below Average | Substantial keyword management issues causing waste |
| 0-39 | Poor | Keyword strategy requires fundamental overhaul |

**Total possible points: 115** (normalized to 100-point scale)

## Benchmark Data

| Metric | Excellent | Good | Average | Poor |
|--------|-----------|------|---------|------|
| Search term relevancy rate | > 90% | 80-90% | 65-80% | < 65% |
| Keyword duplication rate | 0% | < 5% | 5-15% | > 15% |
| Cannibalization rate | 0% | < 3% | 3-10% | > 10% |
| Avg keywords per ad group | 5-15 | 3-20 | 20-40 | 40+ |
| Zero-conversion keyword spend % | < 10% | 10-20% | 20-35% | > 35% |
| Exact match for top converters | 100% | 80%+ | 50-80% | < 50% |

## N-Gram Analysis Methodology

### Step-by-step process:
1. Export search term report (last 90 days minimum)
2. Tokenize all search terms into 1-gram, 2-gram, and 3-gram components
3. Aggregate metrics (impressions, clicks, cost, conversions) by n-gram
4. Calculate CPA, CVR, and CTR for each n-gram
5. Sort by cost descending to find highest-spend n-grams
6. Flag irrelevant n-grams as negative keyword candidates
7. Flag high-converting n-grams as keyword expansion candidates
8. Cross-reference n-gram negatives against existing keyword list to avoid conflicts

## Output Format

```markdown
## Keyword Audit Results

**Overall Score: [X]/100 — [Rating]**

### Match Type Distribution
| Match Type | Keywords | Spend % | Conv % | CPA |
|------------|----------|---------|--------|-----|
| Exact | X | X% | X% | $X |
| Phrase | X | X% | X% | $X |
| Broad | X | X% | X% | $X |

### Critical Findings
1. [Highest impact issue]
2. ...

### Cannibalization Report
| Keyword | Campaign A | Campaign B | Est. CPC Inflation |
|---------|-----------|-----------|-------------------|
| ... | ... | ... | ... |

### Top N-Gram Waste
| N-Gram | Spend | Conversions | Recommendation |
|--------|-------|-------------|----------------|
| ... | ... | ... | Add as negative |

### Action Items
1. [Priority fixes]
```
