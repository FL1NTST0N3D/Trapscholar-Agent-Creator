# Negative Keywords — Main Skill Router

## Command: /negatives

The master negative keyword intelligence system. Routes to specialized sub-skills for mining, analysis, conflict detection, industry lists, cross-campaign strategy, match type selection, waste calculation, and audit reporting.

## Command Routing

| User Command | Route To | Description |
|---|---|---|
| `/negatives mine` | `neg-search-term-mining` | Parse and classify search term reports |
| `/negatives ngram` | `neg-ngram-analysis` | N-gram pattern extraction and analysis |
| `/negatives conflicts` | `neg-conflict-detector` | Find negative-positive keyword conflicts |
| `/negatives lists` | `neg-industry-lists` | Pre-built industry negative keyword lists |
| `/negatives cross-campaign` | `neg-cross-campaign` | Cross-campaign negative strategy |
| `/negatives match-types` | `neg-match-types` | Match type selection for negatives |
| `/negatives waste` | `neg-waste-calculator` | Calculate budget waste from poor negatives |
| `/negatives report` | `neg-report` | Full negative keyword audit report |

## Negative Keyword Fundamentals

Understanding the three negative match types is critical. They work DIFFERENTLY from positive keyword match types.

### Broad Match Negative
- **Syntax**: `free` (no brackets, no quotes)
- **Blocks**: Any query containing the word "free" in any position
- **Does NOT block**: Close variants, synonyms, or misspellings (unlike positive broad match)
- **Example**: Negative `free` blocks "free software", "software free trial", "get it free today"
- **Does NOT block**: "freely available" (different word form — negatives don't match variants)
- **Key insight**: Broad negative is more restrictive than you think. It only blocks the EXACT word, not synonyms or related terms. But it blocks it in ANY position within the query.

### Phrase Match Negative
- **Syntax**: `"free trial"` (in quotes)
- **Blocks**: Any query containing "free trial" as a phrase, in that exact word order
- **Does NOT block**: Queries where the words appear but not as a phrase
- **Example**: Negative `"free trial"` blocks "get free trial now", "free trial software"
- **Does NOT block**: "trial for free", "free software trial" (word order matters)
- **Key insight**: Use phrase negative when individual words are fine but the combination is bad.

### Exact Match Negative
- **Syntax**: `[free crm software]` (in brackets)
- **Blocks**: ONLY the exact query "free crm software" — nothing else
- **Does NOT block**: Any variation, addition, or reordering
- **Example**: Negative `[free crm software]` blocks only "free crm software"
- **Does NOT block**: "free crm", "crm software free", "best free crm software"
- **Key insight**: Use exact negative only when you want to block one specific query while keeping all variations active. This is precision surgery.

### Critical Difference from Positive Match Types
Negative keywords do NOT match:
- Close variants (misspellings, plurals for broad/phrase)
- Synonyms
- Related searches
- Implied words

This means you need to add BOTH "free" AND "fre" (common misspelling) as separate negatives. You need "job" AND "jobs" AND "career" AND "careers" as separate negatives.

## Orchestration Flow

The system uses 3 specialized agents that work together:

### Agent 1: Mining Agent (`agents/mining-agent.md`)
- Ingests raw search term data (CSV, paste, or API)
- Classifies each term: Relevant | Irrelevant | Ambiguous
- Maps search intent: Informational | Commercial | Transactional | Navigational
- Flags pattern categories: job-seekers, DIY, competitors, freebie-hunters, complaints
- Output: Classified search term dataset with recommendations

### Agent 2: Analysis Agent (`agents/analysis-agent.md`)
- Runs N-gram analysis on classified data
- Extracts 1-gram, 2-gram, 3-gram frequency tables
- Cross-references with spend, impressions, conversions
- Identifies high-waste N-grams (high spend + zero conversions)
- Runs cross-campaign overlap analysis
- Output: Prioritized N-gram waste report

### Agent 3: Audit Agent (`agents/audit-agent.md`)
- Calculates Negative Keyword Coverage Score (0-100)
- Detects negative-positive conflicts
- Matches account to industry lists
- Calculates total waste in dollars
- Generates formatted audit report
- Output: Complete audit with score, recommendations, savings projection

### Orchestration Sequence

```
User Input (search term data)
        │
        ▼
  ┌─────────────┐
  │ Mining Agent │ ──→ Classified terms
  └─────────────┘
        │
        ▼
  ┌──────────────────┐
  │ Analysis Agent   │ ──→ N-gram patterns + waste quantification
  └──────────────────┘
        │
        ▼
  ┌──────────────┐
  │ Audit Agent  │ ──→ Score + Report + Recommendations
  └──────────────┘
        │
        ▼
  Final Output: Audit report with actionable negative keyword list
```

## Input Formats Accepted

1. **CSV file path** — Standard Google Ads search term report export
2. **Pasted data** — Tab-separated or comma-separated search term data
3. **Manual keyword list** — List of keywords to analyze for conflicts
4. **Industry name** — For pre-built list retrieval

## Output Formats

- Negative keyword lists (ready to upload to Google Ads)
- Audit reports (Markdown formatted)
- Conflict reports (prioritized by risk)
- Waste calculations (monthly and annual projections)

## Scoring Methodology

The Negative Keyword Coverage Score evaluates:

| Factor | Weight | Measurement |
|--------|--------|-------------|
| Search term relevance rate | 30% | % of search terms that are relevant to the business |
| N-gram coverage | 25% | % of high-waste N-grams already covered by negatives |
| Conflict absence | 15% | Absence of negative-positive conflicts |
| Industry list coverage | 15% | Coverage of applicable industry-standard negatives |
| Match type accuracy | 15% | Correct match type usage across negative list |

## Quick Usage Examples

```
# Mine search terms from a CSV
/negatives mine path/to/search-terms.csv

# Run N-gram analysis on last 30 days
/negatives ngram --days 30

# Check for conflicts
/negatives conflicts

# Get industry list for SaaS
/negatives lists saas

# Full audit
/negatives report
```
