# Search Term Mining for Negative Keywords

## Command: /negatives mine

Parse search term reports and classify every term as Relevant (keep), Irrelevant (add as negative), or Ambiguous (needs review). Maps search intent, flags waste categories, and produces a prioritized negative keyword recommendation list.

## Why Search Term Mining Matters

Google Ads shows your ads for queries you never explicitly targeted. Broad match and phrase match keywords trigger on related searches — many of which have nothing to do with your business. Search term mining is the systematic process of reviewing what queries actually triggered your ads and deciding which ones should be blocked.

The difference between a well-mined account and an unmined one is typically 15-30% of total budget. That is not a rounding error. That is the difference between profitable and unprofitable campaigns.

## Classification Framework

### Category 1: Relevant (Keep)
Search terms that match your business intent. These are queries from people who could become customers.

Signals of relevance:
- Contains your product/service keywords
- Shows commercial or transactional intent
- Matches your target audience demographics
- Has conversion history
- Contains branded terms (yours)

Action: Keep. Optionally add as exact match keywords for better control.

### Category 2: Irrelevant (Negative)
Search terms that will never convert for your business. These are wasted clicks.

Signals of irrelevance:
- Wrong industry entirely
- Wrong intent (informational when you sell products)
- Wrong audience (job seekers, students, DIYers)
- Competitor brands (unless you run competitor campaigns)
- Geographic mismatch
- Free/cheap intent when you sell premium

Action: Add as negative keyword with appropriate match type.

### Category 3: Ambiguous (Review)
Search terms where relevance is unclear. Could go either way depending on context.

Signals of ambiguity:
- Generic terms that could be multiple industries
- Terms with some conversion history but poor performance
- New terms with insufficient data (< 10 clicks)
- Terms that are relevant but at a different funnel stage

Action: Flag for manual review. Provide context and recommendation.

## Intent Mapping

Every search term gets mapped to one of four intent categories:

### Informational Intent
- User wants to learn, not buy
- Signals: "how to", "what is", "why does", "guide", "tutorial", "tips", "examples", "definition"
- Negative candidate? Usually YES for bottom-funnel campaigns. Sometimes valuable for top-funnel/content campaigns.
- Priority: Medium (these still cost money but convert at lower rates)

### Commercial Investigation
- User is researching before buying
- Signals: "best", "top", "review", "comparison", "vs", "alternative", "pros and cons"
- Negative candidate? Usually NO — these are mid-funnel prospects
- Priority: Low (keep most of these, they often convert)

### Transactional Intent
- User is ready to buy or take action
- Signals: "buy", "price", "cost", "order", "purchase", "sign up", "get quote", "hire", "book"
- Negative candidate? Almost never — these are your money keywords
- Priority: Very Low (only negative if wrong product/service)

### Navigational Intent
- User is looking for a specific brand or website
- Signals: Competitor brand names, specific URLs, "login", "[brand] support"
- Negative candidate? YES for competitor brands (unless running competitor campaigns). NO for your own brand.
- Priority: High for competitor terms (expensive, rarely convert)

## Waste Pattern Categories

The mining process flags these specific waste patterns:

### 1. Job-Related Terms
People looking for employment, not your product/service.
- Flag words: job, jobs, career, careers, hiring, salary, salaries, resume, interview, internship, intern, employment, employer, recruit, recruitment, glassdoor, indeed, linkedin, vacancy, vacancies, position, positions, work from home, remote job, part time, full time
- Action: Add as broad match negatives (unless you are a staffing/recruiting company)

### 2. DIY / Self-Service Terms
People who want to do it themselves instead of hiring you.
- Flag words: DIY, yourself, homemade, self, template, free template, how to make, how to build, how to create, how to fix, tutorial, course, class, learn, training, certification
- Action: Add as phrase match negatives to preserve related commercial terms

### 3. Competitor Terms
People searching for your competitors by name.
- Detection: Compare search terms against a provided competitor list, or flag terms containing known competitor brand patterns
- Action: Exact match negatives (unless running competitor campaigns intentionally)

### 4. Freebie-Hunter Terms
People explicitly looking for free alternatives.
- Flag words: free, freeware, open source, opensource, no cost, gratis, complimentary, trial, free trial, demo, sample, free download
- Action: Broad match negatives for "free" and "freeware". Phrase match for "free trial" if you offer trials (you want "your-brand free trial" but not "free crm trial")

### 5. Review / Complaint Terms
People with existing products looking for reviews or support, not new purchases.
- Flag words: review, reviews, complaint, complaints, scam, fraud, lawsuit, problem, issue, broken, refund, return, cancel, cancellation, customer service, support, help
- Action: Phrase match negatives (some review terms can have commercial intent)

### 6. Educational / Academic Terms
Students and researchers, not buyers.
- Flag words: essay, thesis, dissertation, research paper, case study, pdf, definition, meaning, wiki, wikipedia, scholarly, academic, university, college, school, student
- Action: Broad match negatives for clearly academic terms

### 7. Geographic Mismatch
People searching from or for locations you don't serve.
- Detection: Compare location terms in search queries against your service areas
- Action: Phrase match negatives for specific location names outside your service area

## Mining Process Step-by-Step

### Step 1: Ingest Data
Accept search term data in one of these formats:
- CSV file (Google Ads export format)
- Tab-separated paste
- Google Ads API data (if credentials available)

Required fields: Search term, Impressions, Clicks, Cost
Preferred fields: + Conversions, Conversion Value, Campaign, Ad Group

### Step 2: Clean and Normalize
- Convert all search terms to lowercase
- Remove leading/trailing whitespace
- Deduplicate (some terms appear across multiple campaigns — aggregate metrics)
- Flag terms with < 1 click as "insufficient data"

### Step 3: Pattern Matching
Run each search term against all waste pattern categories above. A term can match multiple categories (e.g., "free crm jobs" matches both freebie-hunter and job-related).

### Step 4: Intent Classification
Map each term to Informational / Commercial / Transactional / Navigational intent. Use the signal words listed above plus contextual analysis.

### Step 5: Performance Analysis
For terms not caught by pattern matching, analyze performance:
- Cost > $50 with 0 conversions → Flag as Irrelevant candidate
- CTR > 3x average with 0 conversions → Flag as misleading match (ad is attractive but query is wrong)
- Conversion rate < 25% of account average → Flag as underperforming

### Step 6: Classification
Assign each term: Relevant | Irrelevant | Ambiguous
Include confidence score (0-100) for each classification.

### Step 7: Output
Produce three lists:
1. **Negative keyword recommendations** — Irrelevant terms with suggested match types
2. **Ambiguous terms for review** — Terms needing human judgment with context
3. **Relevant terms to keep** — Optionally, terms worth promoting to exact match keywords

## Usage

```bash
# Mine from CSV file
/negatives mine path/to/search-terms.csv

# Mine with competitor list
/negatives mine --competitors "salesforce,hubspot,zoho"

# Mine specific campaigns only
/negatives mine --campaign "Search - Non-Brand"

# Mine with custom cost threshold
/negatives mine --min-cost 5

# Mine and auto-export negative list
/negatives mine --output negatives.csv
```

## Output Format

```
NEGATIVE KEYWORD MINING REPORT
==============================
Terms Analyzed: 2,341
Classified as Irrelevant: 487 (20.8%)
Classified as Ambiguous: 156 (6.7%)
Classified as Relevant: 1,698 (72.5%)

TOP WASTE CATEGORIES:
  Job-related: 89 terms, $567.40 wasted
  Freebie-hunters: 47 terms, $340.20 wasted
  DIY/Self-service: 34 terms, $178.90 wasted
  Competitor: 23 terms, $234.50 wasted
  Educational: 18 terms, $89.30 wasted

ESTIMATED MONTHLY SAVINGS: $1,410.30
ESTIMATED ANNUAL SAVINGS: $16,923.60

[Full negative list with match types follows...]
```

## Integration with Other Skills

- Feeds classified data into `/negatives ngram` for pattern analysis
- Uses `/negatives match-types` for match type assignment
- Feeds into `/negatives waste` for dollar calculations
- Contributes to `/negatives report` for full audit
