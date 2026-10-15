# Negative Keyword Waste Calculator

## Command: /negatives waste

Calculate the total monthly budget wasted due to insufficient negative keyword coverage. Quantifies waste from irrelevant search terms, competitor clicks, informational queries, and geographic leakage. Outputs dollar amounts, percentage of budget, and projected annual savings.

## Why Quantifying Waste Matters

Telling an advertiser they have "bad negative keyword coverage" doesn't drive action. Telling them they're wasting $2,847 per month on irrelevant clicks — that drives action. This skill converts abstract negative keyword problems into concrete dollar amounts that justify the optimization work.

The waste calculator also provides ROI justification for negative keyword management. When a client asks "is it worth spending 4 hours on negative keyword research?" the answer becomes clear when you show them they'll save $2,847/month ($34,164/year) for 4 hours of work.

## Waste Categories

### Category 1: Irrelevant Search Term Waste
Clicks from search terms that have zero chance of converting because they're completely unrelated to the business.

**How to calculate:**
1. Pull all search terms from the analysis period
2. Classify each as Relevant or Irrelevant (using `/negatives mine` classification)
3. Sum the cost of all Irrelevant search terms
4. This is your Irrelevant Search Term Waste

**Typical range:** 10-25% of total search spend
**Example:** Account spends $10,000/mo. 487 irrelevant search terms cost $2,340. Waste = $2,340/mo.

### Category 2: Competitor Click Waste
Clicks from users searching for competitor brands who clicked your ad by mistake or for comparison but almost never convert.

**How to calculate:**
1. Identify all search terms containing competitor brand names
2. Calculate conversion rate for competitor terms vs account average
3. Cost of competitor terms * (1 - competitor_conv_rate / account_conv_rate) = waste
4. If competitor conv rate is 0%, the entire cost is waste
5. If competitor conv rate is 50% of account average, half the cost is waste

**Typical range:** 3-8% of total search spend
**Note:** If running intentional competitor campaigns, exclude those from waste calculation

### Category 3: Informational Query Waste
Clicks from users seeking information rather than looking to buy. These queries convert at a fraction of the account average.

**How to calculate:**
1. Identify search terms with informational intent signals ("how to", "what is", "guide", "tutorial", "tips", "definition")
2. Calculate conversion rate for informational terms
3. If informational conv rate < 25% of account average, calculate waste:
4. Waste = Info Cost * (1 - info_conv_rate / account_conv_rate)
5. If purely informational with 0 conversions, 100% is waste

**Typical range:** 5-15% of total search spend
**Caveat:** Some informational queries have long-term value (content marketing). Apply judgment.

### Category 4: Geographic Leakage Waste
Clicks from users in locations you don't serve or can't serve profitably.

**How to calculate:**
1. Identify search terms containing geographic modifiers outside your service area
2. Check user location data if available (geographic report in Google Ads)
3. Sum cost of clicks from non-serviceable locations
4. Additional: Apply "presence or interest" targeting analysis — are you set to "presence" only?

**Typical range:** 2-10% of total search spend (varies wildly by targeting setup)

### Category 5: Job Seeker Waste
Clicks from people looking for employment, not your product or service.

**How to calculate:**
1. Identify search terms containing job/career signals
2. Sum total cost of these clicks
3. Job seeker clicks almost never convert (assume 100% waste unless you're a staffing company)

**Typical range:** 2-7% of total search spend

### Category 6: Cross-Campaign Cannibalization Waste
Money wasted when campaigns compete against each other, driving up CPCs.

**How to calculate:**
1. Identify search terms that triggered multiple campaigns
2. Calculate the CPC difference between the campaign that served and the campaign that should have served
3. Waste = Clicks * (Actual CPC - Optimal CPC)

**Typical range:** 3-12% of total search spend
**Note:** Requires cross-campaign search term data

## Total Waste Calculation

```
Total Monthly Waste =
    Irrelevant Term Waste
  + Competitor Click Waste
  + Informational Query Waste
  + Geographic Leakage Waste
  + Job Seeker Waste
  + Cross-Campaign Waste

Waste Percentage = (Total Monthly Waste / Total Monthly Spend) * 100

Annual Waste Projection = Total Monthly Waste * 12

Savings After Optimization = Total Monthly Waste * Recovery Rate
  (Recovery Rate typically 70-85% — not all waste is eliminable)

Net Annual Savings = Annual Waste Projection * Recovery Rate
```

## Waste Report Output Format

```
NEGATIVE KEYWORD WASTE CALCULATOR REPORT
==========================================

Account: [Account Name]
Period: [Date Range]
Total Spend: $[amount]

WASTE BREAKDOWN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Category                    | Monthly Waste | % of Budget
─────────────────────────────────────────────────────────
Irrelevant Search Terms     | $2,340.00     | 23.4%
Competitor Clicks           | $567.00       | 5.7%
Informational Queries       | $890.00       | 8.9%
Geographic Leakage          | $234.00       | 2.3%
Job Seeker Clicks           | $178.00       | 1.8%
Cross-Campaign Cannibalize  | $456.00       | 4.6%
─────────────────────────────────────────────────────────
TOTAL MONTHLY WASTE         | $4,665.00     | 46.7%

SAVINGS PROJECTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Recovery Rate (estimated):    80%
Monthly Savings:              $3,732.00
Annual Savings:               $44,784.00

WHAT THOSE SAVINGS COULD BUY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

At current CPA ($45.00):
  Additional conversions/mo:  83
  Additional conversions/yr:  996

At current ROAS (4.2x):
  Additional revenue/mo:      $15,674.40
  Additional revenue/yr:      $188,092.80
```

## Confidence Levels

Every waste estimate includes a confidence level:

| Confidence | When Applied | Meaning |
|------------|-------------|---------|
| HIGH | 0 conversions, 50+ clicks, clear irrelevance | Very likely waste. Safe to act on. |
| MEDIUM | Low conversions, pattern-based classification | Probable waste. Review before acting. |
| LOW | < 10 clicks, ambiguous relevance | Possible waste. Need more data. |

## Data Requirements

**Minimum data for useful calculation:**
- 30 days of search term data
- At least 100 search terms
- Cost and conversion data per search term

**Ideal data for precise calculation:**
- 90 days of search term data
- 500+ search terms
- Cost, conversions, conversion value per search term
- Campaign and ad group attribution
- Geographic data
- Cross-campaign search term overlap data

## Usage

```bash
# Calculate waste from CSV
/negatives waste path/to/search-terms.csv

# Calculate with specific date range
/negatives waste --days 60

# Calculate for specific campaign
/negatives waste --campaign "Search - Non-Brand"

# Include geographic analysis
/negatives waste --include-geo

# Set custom CPA for savings calculation
/negatives waste --cpa 45

# Export waste report
/negatives waste --output waste-report.md
```

## Integration with Other Skills

- Uses classifications from `/negatives mine` to categorize waste
- Uses N-gram data from `/negatives ngram` to quantify pattern-level waste
- Feeds dollar amounts into `/negatives report` for the full audit
- References `/negatives cross-campaign` for cannibalization waste
