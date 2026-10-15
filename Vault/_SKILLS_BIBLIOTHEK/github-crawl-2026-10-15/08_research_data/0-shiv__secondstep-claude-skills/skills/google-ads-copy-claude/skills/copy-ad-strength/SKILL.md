# Ad Strength Optimizer — Hit "Excellent" on Every RSA

## Command: `/copy strength`

Audit an existing RSA's Ad Strength, identify weaknesses, and provide specific fixes to reach "Excellent" rating. Also works proactively when generating new ads.

## What Is Ad Strength?

Ad Strength is Google's quality rating for Responsive Search Ads. It ranges from "Poor" to "Excellent" and directly impacts ad serving — ads with higher Ad Strength get more impressions and better placements.

| Rating | Impact | What It Means |
|--------|--------|--------------|
| Poor | -50% impressions (estimated) | Major issues: too few headlines, no keyword relevance, duplicates |
| Average | Baseline | Meets minimum requirements but lacks variety or relevance |
| Good | +20% impressions | Solid variety, keyword usage, and uniqueness |
| Excellent | +40% impressions | Maximum variety, strong keyword integration, diverse CTAs |

## The 5 Pillars of Ad Strength

Google evaluates these factors. Score each 1-10 when auditing:

### Pillar 1: Headline Uniqueness (Weight: High)

Google checks whether your headlines say different things. Two headlines that are semantically similar count as duplicates.

**Failing examples:**
- "Best Plumber in Dallas" + "Top Plumber in Dallas" (same meaning)
- "Get a Free Quote" + "Request a Free Quote" (same meaning)
- "Save 20% Today" + "20% Off Today" (same meaning)

**Passing examples:**
- "Best Plumber in Dallas" + "24/7 Emergency Service" (different message)
- "Get a Free Quote" + "Licensed & Insured" (different message)
- "Save 20% Today" + "Trusted by 5,000+ Homes" (different message)

**Scoring:**
- 1-3: More than 3 semantically similar pairs
- 4-6: 1-2 similar pairs, most headlines unique
- 7-8: All headlines convey distinct messages
- 9-10: Every headline covers a different angle AND different framework

### Pillar 2: Keyword Relevance (Weight: High)

Headlines and descriptions should include keywords from the ad group naturally.

**Scoring criteria:**
- Primary keyword appears in at least 2 headlines
- Primary keyword appears in at least 1 description
- Secondary keywords appear in 1-2 headlines
- Keywords are used naturally, not stuffed
- Keywords appear in different positions (beginning, middle, end)

**Scoring:**
- 1-3: No keywords in headlines or descriptions
- 4-6: Primary keyword in 1 headline only
- 7-8: Primary keyword in 2+ headlines AND 1+ description
- 9-10: Primary + secondary keywords distributed naturally across headlines and descriptions

### Pillar 3: CTA Diversity (Weight: Medium)

Google wants to see different calls-to-action across your headlines and descriptions.

**Failing:** Every CTA says "Call Now"
**Passing:** Mix of "Call Now", "Get a Quote", "Book Online", "Learn More"

**Scoring:**
- 1-3: Same CTA repeated or no CTA at all
- 4-6: 1-2 different CTAs
- 7-8: 3+ different CTAs across headlines and descriptions
- 9-10: 4+ distinct CTAs with varied action verbs

### Pillar 4: Popular Keywords (Weight: Medium)

Google suggests "popular" keywords that are commonly searched in your category. Including these terms (when relevant) boosts Ad Strength.

**How to check:** In the Google Ads editor, the Ad Strength panel shows suggested keywords. Include at least 2-3 of these in your headlines.

**Scoring:**
- 1-3: None of Google's suggested keywords included
- 4-6: 1-2 suggested keywords included
- 7-8: 3+ suggested keywords included naturally
- 9-10: All relevant suggested keywords included without forced phrasing

### Pillar 5: Headline Quantity & Description Quantity (Weight: Low-Medium)

More assets = more combinations = better optimization.

| Assets | Impact |
|--------|--------|
| 3-5 headlines | Poor — too few combinations |
| 6-10 headlines | Average — decent but not optimal |
| 11-14 headlines | Good — strong variety |
| 15 headlines | Excellent — maximum combinations |
| 2 descriptions | Average |
| 3 descriptions | Good |
| 4 descriptions | Excellent |

## Ad Strength Audit Process

When the user provides an existing RSA or asks for an audit:

### Step 1: Collect the current ad
Ask for all headlines, descriptions, display paths, and final URL.

### Step 2: Score each pillar

```
=== AD STRENGTH AUDIT ===

PILLAR SCORES:
1. Headline Uniqueness:    X/10  [Details]
2. Keyword Relevance:      X/10  [Details]
3. CTA Diversity:          X/10  [Details]
4. Popular Keywords:       X/10  [Details]
5. Asset Quantity:         X/10  [Details]

OVERALL SCORE: XX/50
PREDICTED AD STRENGTH: [Poor/Average/Good/Excellent]
```

### Step 3: Identify specific issues

For each pillar scoring below 7, list the exact problem:
- Which headlines are semantically similar?
- Which keywords are missing?
- What CTAs are repeated?
- How many more headlines are needed?

### Step 4: Provide fixes

For every issue identified, provide a specific replacement headline or description:

```
ISSUES & FIXES:

Issue 1: H3 "Top Dallas Plumber" is too similar to H1 "Best Plumber in Dallas"
Fix:     Replace H3 with "24/7 Emergency Repairs" (22 chars) [Framework: Benefit]

Issue 2: No headline includes the keyword "drain cleaning"
Fix:     Add H12 "Expert Drain Cleaning" (21 chars) [Framework: Keyword]

Issue 3: Only 1 CTA used ("Call Now") across 3 headlines
Fix:     Replace H8 CTA with "Book Online Today" (17 chars)
         Replace H11 CTA with "Get a Free Estimate" (19 chars)
```

### Step 5: Show before/after

Present the complete revised RSA with all fixes applied and re-score.

## Headline Variety Checklist

Use this checklist to ensure maximum variety across 15 headlines:

- [ ] At least 2 headlines with the primary keyword
- [ ] At least 1 headline with a secondary keyword
- [ ] At least 2 headlines with numbers/statistics
- [ ] At least 2 headlines with benefit statements
- [ ] At least 2 headlines with CTA verbs (and different CTAs)
- [ ] At least 1 headline with social proof
- [ ] At least 1 headline with urgency/scarcity
- [ ] At least 1 question headline
- [ ] At least 1 headline mentioning price/offer (if applicable)
- [ ] At least 1 headline with location (if local business)
- [ ] No two headlines start with the same word
- [ ] No two headlines use the same framework
- [ ] Short headlines (15-20 chars) mixed with long ones (28-30 chars)
- [ ] No headline is a subset of another headline

## Common Ad Strength Killers

Avoid these patterns that consistently drag Ad Strength down:

1. **"Our [Product] is the Best"** — too generic, no proof
2. **Starting 3+ headlines with the same word** — kills uniqueness
3. **Using the same CTA everywhere** — "Call Now" in 4 headlines
4. **Keyword stuffing** — forcing keywords unnaturally
5. **All headlines same length** — no variation in short vs long
6. **Missing numbers entirely** — no stats, years, or figures
7. **No question headlines** — missing a whole engagement category
8. **Descriptions that repeat headline messages** — wasted space
9. **Pinning everything** — over-pinning limits Google's optimization
10. **Ignoring Google's keyword suggestions** — easy Ad Strength boost
