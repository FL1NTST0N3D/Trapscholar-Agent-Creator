# Negative Keyword Match Type Decision Engine

## Command: /negatives match-types

Choose the right match type for every negative keyword. The wrong match type either blocks too much (killing good traffic) or blocks too little (wasting money). This skill provides a systematic decision framework for broad negative, phrase negative, and exact negative selection.

## Why Match Type Selection Matters for Negatives

A negative keyword's match type determines its blast radius. Get it wrong in one direction and you waste money on irrelevant clicks. Get it wrong in the other direction and you block profitable traffic worth thousands per month. There is no undo button — you only discover the mistake weeks later when performance data reveals the gap.

The stakes are asymmetric:
- **Too narrow** (using exact when you need broad): You waste money on variations you didn't block
- **Too broad** (using broad when you need exact): You block profitable traffic silently

Both are expensive. But blocking profitable traffic is usually worse because you don't see the lost conversions — they just never happen.

## The Three Negative Match Types Explained

### Broad Match Negative (no punctuation)
**Syntax:** `free`

**What it blocks:** Any search query that contains ALL the words in the negative keyword, in any order. For multi-word negatives, all words must be present but can be anywhere in the query.

**What it does NOT block:**
- Close variants (plurals, misspellings, synonyms)
- Queries where the word appears as part of another word
- Queries with additional words that change meaning

**Single-word examples:**
- Negative: `free`
- Blocks: "free crm", "crm free trial", "get free software", "free"
- Does NOT block: "freedom crm", "freely available", "freeware" (different word)

**Multi-word examples:**
- Negative: `free trial`
- Blocks: "free trial crm", "crm free trial", "get free 30 day trial"
- Does NOT block: "free crm" (missing "trial"), "trial version free" (wait — this IS blocked, both words present)

**Key insight:** Multi-word broad negatives require ALL words to be present. This makes them narrower than you might expect.

### Phrase Match Negative (quotes)
**Syntax:** `"free trial"`

**What it blocks:** Any search query that contains the negative keyword phrase in that exact word order. Additional words can appear before or after, but not between the words.

**What it does NOT block:**
- Queries with the words in a different order
- Queries with additional words inserted between the phrase words
- Close variants

**Examples:**
- Negative: `"free trial"`
- Blocks: "free trial software", "get free trial", "best free trial crm 2026"
- Does NOT block: "trial for free", "free 30 day trial" (word inserted between), "free crm trial"

**Key insight:** Phrase match negative is your precision tool. It blocks the specific combination that causes waste while allowing the individual words in other contexts.

### Exact Match Negative (brackets)
**Syntax:** `[free crm software]`

**What it blocks:** ONLY the exact query "free crm software" — nothing more, nothing less.

**What it does NOT block:**
- Any variation, addition, or reordering
- "best free crm software" (additional word)
- "free crm" (missing word)
- "crm software free" (different order)

**Key insight:** Exact match negative is surgical. Use it only when you need to block ONE specific query while keeping all variations alive. This is rare but critical when you find a single query that wastes money but its variations convert.

## Decision Tree for Match Type Selection

Follow this decision tree for EVERY negative keyword you add:

### Question 1: Is this word/phrase EVER relevant to your business?

**NO** → Consider **Broad Match Negative**
- The word has zero relevance in any context
- Examples for a SaaS company: "jobs", "salary", "recipe", "lyrics"
- Adding as broad negative eliminates the word from ALL queries

**YES, sometimes** → Go to Question 2

**YES, always** → Do NOT add as negative. This is a positive keyword.

### Question 2: Is the individual word relevant, but a specific phrase containing it is not?

**YES** → Use **Phrase Match Negative**
- The word alone is fine, but a specific phrase is wasteful
- Example: "repair" is fine for an appliance company, but "repair manual" is not (DIY intent)
- Negative: `"repair manual"` (phrase match)
- This blocks "dishwasher repair manual" but allows "dishwasher repair service"

**NO** → Go to Question 3

### Question 3: Is there ONE specific query to block while keeping all variations?

**YES** → Use **Exact Match Negative**
- Example: "salesforce" as a query brings competitor window-shoppers, but "salesforce alternative" brings you customers
- Negative: `[salesforce]` (exact match) — blocks only the naked competitor search
- Allows: "salesforce alternative", "better than salesforce", "salesforce competitor"

**NO** → Reassess. If the word is relevant in some contexts and you can't isolate the waste to a specific phrase or query, you likely need to go back and identify the actual waste pattern more precisely.

## Match Type Selection by Scenario

| Scenario | Recommended Match Type | Rationale |
|----------|----------------------|-----------|
| Completely irrelevant word (e.g., "jobs" for a SaaS company) | Broad | Block all queries containing this word |
| Irrelevant phrase but individual words are fine (e.g., "how to build" for a construction company) | Phrase | Block the phrase, keep individual words |
| One bad query but variations are good (e.g., "salesforce" vs "salesforce alternative") | Exact | Surgical precision, block only that query |
| Industry term that's relevant to competitors but not you | Phrase or Exact | Depends on variation risk |
| Geographic term outside your service area | Phrase | Block "in [city]" phrases |
| Brand misspelling that triggers wrong ads | Exact | Block only the misspelling, keep correct spelling |
| Informational modifier (e.g., "what is") | Phrase | Block "what is [your product]" while keeping "[your product]" |
| Career/job modifier | Broad | "jobs" in any position means job seeker |

## Match Type Escalation Strategy

When in doubt, start narrow and escalate:

1. **Start with Exact Match** — Block only the specific query you identified as wasteful
2. **After 2 weeks**: Check if related queries are also wasting money
3. **If yes, escalate to Phrase Match** — Block the phrase pattern
4. **After 2 more weeks**: Check if even broader variations are wasteful
5. **If yes, escalate to Broad Match** — Block the word entirely

This approach minimizes the risk of blocking profitable traffic while progressively tightening coverage.

## Common Mistakes

1. **Defaulting to broad match for everything**: Aggressive but dangerous. You will block good traffic.
2. **Using phrase match when broad is appropriate**: If "jobs" is never relevant, don't use `"jobs"` — use `jobs`. Phrase match only blocks when "jobs" appears as a standalone phrase, missing compound terms.
3. **Forgetting that negatives don't match close variants**: You need both "job" AND "jobs" as separate negatives.
4. **Not adding plural/singular variations**: "attorney" and "attorneys" are different negatives. Add both.
5. **Using exact match for common waste words**: If "free" wastes money in 47 search terms, adding [free crm software] only blocks 1 of 47. Use broad match `free` instead.

## Usage

```bash
# Analyze a negative list and recommend match types
/negatives match-types path/to/negatives.csv

# Get match type recommendation for specific terms
/negatives match-types --terms "free,jobs,how to,competitor name"

# Audit existing negatives for match type issues
/negatives match-types --audit

# Show decision tree for a specific negative
/negatives match-types --decide "repair"
```

## Integration with Other Skills

- Called by `/negatives ngram` for match type assignment on discovered N-grams
- Called by `/negatives mine` for match type assignment on mined terms
- Verified by `/negatives conflicts` to ensure match types don't cause over-blocking
- Feeds match type accuracy score into `/negatives report`
