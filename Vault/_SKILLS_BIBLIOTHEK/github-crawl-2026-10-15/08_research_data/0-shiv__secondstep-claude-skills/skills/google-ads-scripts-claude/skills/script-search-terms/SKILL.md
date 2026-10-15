# Search Term Mining Scripts

## Command: `/script search-terms`

## Overview

The search terms report reveals exactly what users typed into Google before clicking your ads. This data is gold for optimization: high-performing search terms should be added as exact match keywords, and irrelevant terms should be added as negative keywords. Yet most advertisers review search terms manually — once a week at best — missing opportunities and wasting spend on irrelevant queries daily.

Search term mining scripts automate this analysis. They scan search term data, identify terms worth adding as keywords or negatives, and either take action automatically or compile a prioritized recommendation report. The N-gram analysis variant breaks search terms into word fragments to find patterns that single-term analysis misses.

## Script Templates

### 1. High-Performer Mining
Identifies search terms with strong conversion performance that are not yet added as keywords. Recommends or automatically adds them as exact match keywords.

**Key Configuration:**
- `MIN_CONVERSIONS` — Minimum conversions for a term to qualify (default: 2)
- `MIN_CTR` — Minimum CTR for consideration (default: 0.03 = 3%)
- `MAX_CPA` — Maximum acceptable CPA for the term (default: account target CPA)
- `AUTO_ADD` — Whether to automatically add terms as keywords (default: false — report only)
- `MATCH_TYPE` — Match type for added keywords (default: "EXACT")
- `ALERT_EMAIL` — Email for the recommendation report
- `LOOKBACK_DAYS` — Days of data to analyze (default: 30)

**How it works:**
1. Queries the search terms report for the lookback period
2. Filters for terms with conversions >= MIN_CONVERSIONS, CTR >= MIN_CTR, and CPA <= MAX_CPA
3. Cross-references against existing keywords to avoid duplicates
4. If AUTO_ADD is true, adds qualifying terms as exact match keywords in the appropriate ad group
5. Compiles a report of all recommendations/additions and emails it

### 2. Negative Keyword Flagger
Identifies search terms that are spending money without converting — or converting at unacceptable CPAs — and flags them as negative keyword candidates.

**Key Configuration:**
- `SPEND_THRESHOLD` — Minimum spend with zero conversions to flag (default: $50)
- `CPA_MULTIPLIER` — Flag terms with CPA > (account avg CPA * this multiplier) (default: 3.0)
- `AUTO_NEGATE` — Whether to automatically add negatives (default: false — report only)
- `NEGATIVE_LIST_NAME` — Shared negative keyword list to add terms to
- `ALERT_EMAIL` — Email for the negative keyword report
- `LOOKBACK_DAYS` — Days of data to analyze (default: 30)

**How it works:**
1. Queries search terms with spend > 0 for the lookback period
2. Identifies terms matching criteria: high spend with zero conversions, or CPA far above target
3. Cross-references against existing negative keyword lists
4. If AUTO_NEGATE is true, adds terms to the specified shared negative list
5. Emails a prioritized report (sorted by wasted spend)

### 3. N-Gram Analysis
Breaks search terms into individual words (unigrams), two-word pairs (bigrams), and three-word sequences (trigrams). Aggregates performance by n-gram to find patterns invisible at the full-term level.

**Key Configuration:**
- `NGRAM_SIZES` — Array of n-gram sizes to analyze (default: [1, 2, 3])
- `MIN_IMPRESSIONS` — Minimum impressions for an n-gram to be included (default: 50)
- `SPREADSHEET_URL` — Google Sheet for the n-gram analysis output
- `LOOKBACK_DAYS` — Days of data to analyze (default: 60)

**How it works:**
1. Queries all search terms for the lookback period
2. Splits each term into words, then generates unigrams, bigrams, and trigrams
3. Aggregates metrics (impressions, clicks, cost, conversions) by n-gram
4. Calculates CTR, CPC, CPA, and conversion rate for each n-gram
5. Writes results to Google Sheets with separate tabs for each n-gram size
6. Highlights n-grams with high spend and zero conversions (negative candidates) and high conversion rate (positive opportunities)

### 4. Search Term Cost Analysis
Finds the most expensive search terms with no conversions. Sorted by total spend, this report shows exactly where money is being wasted.

**Key Configuration:**
- `ALERT_EMAIL` — Email for the waste report
- `MIN_SPEND` — Minimum spend to include (default: $10)
- `LOOKBACK_DAYS` — Days of data (default: 30)
- `TOP_N` — Number of terms to include in report (default: 50)

## Best Practices

- **Run weekly with a 30-day lookback**: Gives enough data volume while catching issues early. Daily runs create noise; monthly runs miss too much.
- **Never auto-add or auto-negate on the first run**: Start with report-only mode. Review the recommendations manually for 2-3 weeks before enabling auto-actions.
- **Use exact match for additions**: Adding terms as broad match can trigger them for even more unwanted queries. Start with exact match and expand later.
- **Use shared negative lists**: Adding negatives to a shared list applies them across all campaigns. This is more maintainable than campaign-level negatives.
- **Watch for close variants**: Google shows your ads for close variants of exact match keywords. A search term that looks like your keyword but performs poorly might be a close variant issue, not a negative keyword issue.
- **Pair with N-gram analysis**: Single-term analysis misses patterns. If the word "free" appears in 50 different non-converting search terms, the N-gram analysis will catch it.
- **Set realistic thresholds**: Requiring 10 conversions for a single search term is too aggressive for most accounts. Start with 2-3 conversions minimum.

## Common Pitfalls

1. **Hidden search terms**: Google no longer shows all search terms — many are bucketed as "Other search terms." Your analysis is limited to what Google reports.
2. **Cross-campaign conflicts**: A search term may convert well in Campaign A but poorly in Campaign B. Account-level analysis can mask this. Consider campaign-level mining.
3. **Brand term negatives**: Be extremely careful about negating brand terms or close variants. Always exclude branded campaigns from negative keyword scripts.
4. **N-gram noise**: Single-word n-grams like "the", "a", "for" will appear everywhere. Filter out stop words to focus on meaningful patterns.
5. **Lookback period mismatch**: Conversion attribution can take 7-30 days. A search term from 3 days ago may show zero conversions but convert next week.

## GAQL Queries Used

```sql
-- Search terms report
SELECT search_term_view.search_term, search_term_view.status,
       campaign.name, ad_group.name,
       metrics.impressions, metrics.clicks, metrics.cost_micros,
       metrics.conversions, metrics.conversions_value
FROM search_term_view
WHERE segments.date DURING LAST_30_DAYS
AND metrics.impressions > 0
ORDER BY metrics.cost_micros DESC
```

## Template Reference

See `templates/search-term-miner.js` for the complete search term mining script with N-gram analysis.
