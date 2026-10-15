# N-Gram Analysis for Negative Keyword Discovery

## Command: /negatives ngram

Extract 1-gram, 2-gram, and 3-gram patterns from search term reports to surface the root words and phrases driving wasted spend. A single bad N-gram can hide across hundreds of individual search terms — this skill finds them all.

## Why N-Gram Analysis Matters

Looking at search terms one-by-one is the slow, expensive way to find negatives. N-gram analysis flips the approach: instead of evaluating 2,000 individual search terms, you evaluate 200 root patterns. One N-gram like "free" might appear across 47 different search terms costing $340/month with zero conversions. Adding one negative eliminates all 47 at once.

The power of N-gram analysis is compression. You go from thousands of data points to dozens of actionable patterns.

## N-Gram Methodology

### Step 1: Data Preparation
- Import search term report (CSV or pasted data)
- Required columns: Search Term, Impressions, Clicks, Cost, Conversions, Conversion Value
- Optional columns: Campaign, Ad Group, Match Type
- Clean data: lowercase all terms, remove punctuation, trim whitespace
- Filter: minimum 1 click (zero-click terms are noise at this stage)

### Step 2: Tokenization
Split every search term into individual words (tokens):
- "best crm software for small business" → ["best", "crm", "software", "for", "small", "business"]
- Remove stop words ONLY if they are pure noise (a, an, the, and, or, in, on, at, to, for, of, is, it)
- WARNING: Do NOT remove "how", "what", "why", "free", "cheap" — these carry intent signal
- Keep all tokens lowercase for consistent aggregation

### Step 3: N-Gram Extraction

**1-Gram (Unigrams):**
Extract every individual word across all search terms. Aggregate metrics:
- Count: How many unique search terms contain this word
- Total Impressions: Sum of impressions across all terms containing this word
- Total Clicks: Sum of clicks
- Total Cost: Sum of cost
- Total Conversions: Sum of conversions
- Cost Per Conversion: Total Cost / Total Conversions (infinity if 0 conversions)

Example output:
```
| 1-Gram   | Count | Impressions | Clicks | Cost    | Conversions | CPC   | CPConv  |
|----------|-------|-------------|--------|---------|-------------|-------|---------|
| free     | 47    | 12,340      | 892    | $340.20 | 0           | $0.38 | ∞       |
| software | 234   | 45,670      | 3,450  | $2,100  | 89          | $0.61 | $23.60  |
| jobs     | 31    | 8,900       | 456    | $178.50 | 0           | $0.39 | ∞       |
| best     | 156   | 34,200      | 2,100  | $1,890  | 67          | $0.90 | $28.21  |
```

**2-Gram (Bigrams):**
Extract every consecutive two-word combination:
- "best crm software" → ["best crm", "crm software"]
- Aggregate same metrics as 1-grams
- 2-grams reveal phrase-level patterns invisible in 1-gram analysis

Example:
```
| 2-Gram          | Count | Cost    | Conversions | CPConv |
|-----------------|-------|---------|-------------|--------|
| free trial      | 23    | $189.40 | 0           | ∞      |
| how to           | 18    | $67.20  | 0           | ∞      |
| crm software    | 89    | $1,200  | 45          | $26.67 |
| near me         | 34    | $456.00 | 12          | $38.00 |
```

**3-Gram (Trigrams):**
Extract every consecutive three-word combination:
- "best crm software for small business" → ["best crm software", "crm software for", "software for small", "for small business"]
- 3-grams catch very specific intent patterns
- Fewer data points but higher precision

### Step 4: Waste Scoring

For each N-gram, calculate a **Waste Score (0-100)**:

```
Waste Score = (Cost Weight * 0.4) + (Zero Conv Weight * 0.3) + (Frequency Weight * 0.2) + (CTR Weight * 0.1)

Where:
- Cost Weight = (N-gram Cost / Total Account Cost) * 100, capped at 100
- Zero Conv Weight = 100 if conversions = 0, else (1 - Conv Rate / Avg Conv Rate) * 100
- Frequency Weight = (N-gram Count / Total Terms) * 100, capped at 100
- CTR Weight = 100 if CTR > 2x account avg (high CTR + no conversions = expensive waste)
```

### Step 5: Prioritization

Sort all N-grams by Waste Score descending. The output tiers:

**Tier 1 — Immediate Negatives (Waste Score 70-100):**
High spend, zero or near-zero conversions, appears in many search terms. Add these as negatives TODAY.

**Tier 2 — Strong Candidates (Waste Score 40-69):**
Moderate spend with poor conversion performance. Review and add within the week.

**Tier 3 — Monitor (Waste Score 20-39):**
Some waste signal but not conclusive. May need more data. Review monthly.

**Tier 4 — Keep (Waste Score 0-19):**
Converting well relative to cost. These are your good N-grams. Do NOT add as negatives.

### Step 6: Match Type Assignment

For each recommended negative N-gram:
- **1-Gram → Broad match negative** (unless it's a word that appears in converting terms too — then skip or use phrase/exact)
- **2-Gram → Phrase match negative** (the word order matters for the waste pattern)
- **3-Gram → Phrase match negative** (captures the specific intent phrase)
- **Exception**: If a 1-gram appears in BOTH converting and non-converting terms, do NOT add as broad negative. Instead, identify the 2-gram or 3-gram patterns that isolate the waste.

### Step 7: Conflict Check

Before finalizing, cross-reference every recommended negative against:
- Active keywords in the account
- Converting search terms from the last 90 days
- Flag any conflicts for manual review

## Example Full Analysis

Input: 1,847 search terms from a SaaS CRM account, last 60 days.

Analysis results:
```
Total search terms analyzed: 1,847
Total cost analyzed: $14,230
Total conversions: 234

Top waste N-grams found:
1. "free" — 47 terms, $340/mo, 0 conv — Waste Score: 94
2. "jobs" — 31 terms, $178/mo, 0 conv — Waste Score: 87
3. "how to" — 18 terms, $67/mo, 0 conv — Waste Score: 72
4. "salary" — 12 terms, $45/mo, 0 conv — Waste Score: 68
5. "review" — 28 terms, $234/mo, 2 conv — Waste Score: 61

Recommended negatives: 23 terms
Estimated monthly savings: $864
Estimated annual savings: $10,368
```

## Usage

```bash
# Analyze from CSV
/negatives ngram path/to/search-terms.csv

# Analyze with date range
/negatives ngram --days 30

# Analyze specific campaign
/negatives ngram --campaign "Search - Non-Brand"

# Set minimum spend threshold
/negatives ngram --min-cost 10

# Export results
/negatives ngram --output negatives-report.csv
```

## Script Reference

The Python script `scripts/ngram_analyzer.py` handles the heavy computation. It accepts CSV input and produces N-gram frequency tables with all metrics calculated.

## Integration with Other Skills

- Feeds into `/negatives conflicts` for conflict checking
- Feeds into `/negatives waste` for dollar-amount waste calculation
- Feeds into `/negatives report` for the full audit output
- Uses `/negatives match-types` logic for match type assignment
