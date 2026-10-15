# Negative Keyword Conflict Detector

## Command: /negatives conflicts

Find where negative keywords are blocking profitable search terms. This is the most dangerous and most overlooked problem in Google Ads accounts — your own negatives silently killing your best traffic.

## The Hidden Danger of Negative Keywords

Every experienced advertiser has seen this: you add "cheap" as a broad match negative because you sell premium products. Six months later, you notice your "cheap flights to hawaii" campaign stopped getting impressions. Your negative "cheap" blocked the entire campaign. You were selling budget travel and didn't connect the dots.

Negative keyword conflicts are silent killers. Google doesn't warn you. There's no alert. Your ads simply stop showing for queries that were making you money. The only way to catch conflicts is to systematically cross-reference your negatives against your active keywords and converting search terms.

## Types of Conflicts

### Type 1: Direct Keyword Block
A negative keyword directly blocks one of your active keywords from triggering.

Example:
- Active keyword: "affordable crm software" (broad match)
- Negative keyword: "affordable" (broad match negative)
- Result: Your keyword can NEVER trigger. Zero impressions. Complete block.
- Severity: CRITICAL

Detection method: For each negative keyword, check if it would match against any active keyword using negative match type logic.

### Type 2: Converting Search Term Block
A negative keyword blocks a search term that has historically converted.

Example:
- Converting search term: "cheap flights to maui" (3 conversions last month, $45 CPA)
- Negative keyword: "cheap" (broad match negative)
- Result: You lose a profitable search term
- Severity: HIGH

Detection method: Cross-reference all negatives against search terms with 1+ conversion in the last 90 days.

### Type 3: Campaign-Level Cross-Block
A campaign-level negative in Campaign A blocks a keyword that should be running in Campaign A but was intended to block terms in Campaign B.

Example:
- Campaign A: "Brand Campaign" with negative "software" at campaign level
- Campaign A keyword: "yourcompany software pricing" (exact match)
- Result: The campaign-level negative blocks your own brand + product keyword
- Severity: HIGH

Detection method: For each campaign, check campaign-level negatives against that campaign's own keywords.

### Type 4: Shared List Overreach
A negative keyword list shared across multiple campaigns blocks keywords in campaigns where the negative shouldn't apply.

Example:
- Shared negative list: "Competitor Names" containing "hubspot"
- Campaign: "Competitor Conquest" targeting competitor keywords
- Keyword: "hubspot alternative"
- Result: Your competitor conquest campaign can't trigger because the shared list blocks it
- Severity: HIGH

Detection method: For each shared negative list, check against keywords in every campaign the list is applied to.

### Type 5: Partial Phrase Conflict
A phrase match negative blocks a longer keyword or search term that contains the negative phrase but has different intent.

Example:
- Negative keyword: "free software" (phrase match negative)
- Active keyword: "free software trial for enterprise" (phrase match)
- Search term: "start free software trial salesforce" — would be blocked
- Intent: The searcher wants a trial (which you offer), but the negative phrase "free software" catches it
- Severity: MEDIUM

Detection method: Check phrase match negatives against longer keywords/terms that contain the phrase.

## Conflict Detection Process

### Step 1: Gather All Negatives
Collect every negative keyword from:
- Campaign-level negatives (each campaign separately)
- Ad group-level negatives (each ad group separately)
- Shared negative keyword lists (with campaign associations)
- Note the match type of each negative (broad, phrase, exact)

### Step 2: Gather All Active Keywords
Collect every enabled keyword from:
- All active campaigns
- All active ad groups within those campaigns
- Note the match type of each positive keyword
- Note performance data: impressions, clicks, conversions, value

### Step 3: Gather Converting Search Terms
Pull search term data for the last 90 days:
- Filter to terms with 1+ conversion
- Include: search term, campaign, ad group, conversions, conversion value, cost

### Step 4: Run Conflict Matrix
For each negative keyword, check against:
1. All active keywords in the same campaign (and ad groups within it)
2. All active keywords in campaigns sharing the same negative list
3. All converting search terms from the last 90 days

Apply negative match type logic:
- Broad negative "X": blocks any keyword/term containing the word "X"
- Phrase negative "X Y": blocks any keyword/term containing "X Y" as a consecutive phrase
- Exact negative [X Y Z]: blocks only the exact keyword/term "X Y Z"

### Step 5: Prioritize by Impact
For each conflict found, calculate impact:

```
Impact Score = Conversion Value at Risk * Confidence Factor

Where:
- Conversion Value at Risk = Historical conversion value from the blocked keyword/term
- Confidence Factor = 1.0 for direct keyword blocks, 0.8 for converting term blocks, 0.5 for partial phrase conflicts
```

Sort conflicts by Impact Score descending.

### Step 6: Generate Resolution Recommendations

For each conflict, recommend one of:
- **Remove the negative** — If the negative is causing more harm than good
- **Change match type** — Switch from broad to phrase or exact to narrow the block
- **Move the negative** — Move from campaign level to ad group level for more precision
- **Remove from shared list** — If the conflict is only in some campaigns
- **Add keyword as exception** — In some cases, restructuring is needed

## Output Format

```
NEGATIVE KEYWORD CONFLICT REPORT
=================================

CRITICAL CONFLICTS (Immediate Action Required):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Negative: "affordable" [broad] in Campaign "Product Search"
   Blocks keyword: "affordable crm software" [broad match]
   Impact: Keyword has 23 conv/mo, $2,300 value
   Resolution: Change negative to phrase match "affordable alternative" or remove

2. Negative: "free" [broad] in Shared List "Universal Negatives"
   Blocks keyword: "free trial enterprise crm" [phrase match] in Campaign "Trial Signups"
   Impact: Keyword has 12 conv/mo, $1,800 value
   Resolution: Remove "free" from shared list. Add to specific campaigns that don't offer trials.

HIGH PRIORITY CONFLICTS:
━━━━━━━━━━━━━━━━━━━━━━━

3. Negative: "review" [broad] in Campaign "Product Search"
   Blocks search term: "crm software review and pricing" (4 conv last 90 days)
   Impact: Losing ~1.3 conv/mo, $195 value
   Resolution: Change to phrase match "write a review" or exact match [review]

TOTAL CONFLICTS FOUND: 7
TOTAL CONVERSION VALUE AT RISK: $4,295/mo ($51,540/yr)
```

## Usage

```bash
# Detect conflicts across all campaigns
/negatives conflicts

# Detect conflicts in specific campaign
/negatives conflicts --campaign "Brand Campaign"

# Check a specific negative keyword for conflicts
/negatives conflicts --check "free"

# Include search term history in analysis
/negatives conflicts --include-search-terms --days 90

# Export conflict report
/negatives conflicts --output conflict-report.md
```

## Common Conflict Patterns

These negative keywords most frequently cause conflicts:
- "free" — Blocks free trial, free consultation, free quote campaigns
- "cheap" — Blocks budget/affordable product lines
- "used" — Blocks "used to" phrases in commercial queries
- "repair" — Blocks "repair service" when you offer repairs
- "old" — Blocks "old navy", "old town", legitimate brand/location terms
- "small" — Blocks "small business" campaigns
- "online" — Blocks legitimate online purchase intent

## Integration with Other Skills

- Receives negative lists from `/negatives mine` and `/negatives ngram`
- Informs `/negatives match-types` about match type changes needed
- Feeds conflict data into `/negatives report` for the full audit
- Cross-references with `/negatives cross-campaign` for campaign-level conflicts
