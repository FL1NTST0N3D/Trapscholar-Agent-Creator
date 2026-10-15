# QS Ad Relevance Analysis

## Command
`/qs relevance`

## Purpose

Deep dive into the Ad Relevance component of Quality Score. Analyze the alignment between keywords, ad copy, and user intent across the account. Identify ad groups with structural relevance problems, audit ad copy for keyword inclusion, and recommend restructuring or rewriting strategies that improve Ad Relevance ratings.

## Ad Relevance Fundamentals

Ad Relevance measures how closely your ad copy matches the intent behind the keyword that triggered it. Google rates this as Above Average, Average, or Below Average relative to other advertisers bidding on the same keyword.

**Weight in Quality Score: ~22%**

While Ad Relevance has the lowest weight of the three QS components, it is often the easiest to fix. Unlike landing page speed improvements (which require developer resources) or Expected CTR improvements (which require sustained performance), Ad Relevance can often be improved immediately by restructuring ad groups and rewriting ad copy.

## The Five Pillars of Ad Relevance

### 1. Keyword in Headline

**Impact: High**

The single most important factor in Ad Relevance is whether the keyword (or a close variant) appears in the ad headline. Google's algorithm checks for direct keyword presence, semantic similarity, and intent alignment.

**Best Practices:**
- Include the primary keyword in Headline 1 (highest visibility position)
- Use Headline 2 for a supporting value proposition that includes keyword variants
- In RSAs, pin the keyword-containing headline to Position 1 to guarantee it shows
- Do not force keywords where they do not read naturally — semantic relevance matters more than exact match insertion

**Common Mistakes:**
- Headline 1 is the brand name with no keyword mention
- All headlines are benefit-focused ("Save 50%!") with no keyword alignment
- RSA headlines are all generic and interchangeable across ad groups

### 2. Keyword in Description

**Impact: Medium**

The keyword or its theme should appear in at least one description line. This reinforces relevance and provides additional context for Google's matching algorithm.

**Best Practices:**
- Include the keyword naturally in Description 1
- Use Description 2 for supporting details, features, or calls to action
- Avoid keyword stuffing — one natural mention per description is sufficient
- For RSAs, ensure at least 2 of 4 descriptions contain keyword variants

### 3. Ad Group Theme Tightness

**Impact: Very High**

This is the structural foundation of Ad Relevance. An ad group should contain keywords that share a single, cohesive theme. When ad groups are too broad, the ads cannot be relevant to all keywords.

**Ad Group Sizing Guidelines:**

| Structure | Keywords/Group | Pros | Cons |
|:--|:--:|:--|:--|
| **SKAGs** (Single Keyword Ad Groups) | 1 | Maximum relevance | High maintenance, limited data per group |
| **STAGs** (Single Theme Ad Groups) | 3-8 | High relevance, manageable | Requires careful keyword grouping |
| **Themed Groups** | 8-15 | Good balance of relevance and management | Some keywords may not align perfectly |
| **Broad Groups** | 15-50+ | Easy to manage | Low relevance, QS penalty likely |

**Recommended approach: STAGs with 3-8 tightly related keywords per ad group.**

**Signs of poor ad group structure:**
- Ad groups with 20+ keywords
- Keywords in the same ad group with different intent (e.g., "buy shoes" and "shoe repair" in one group)
- Same ad copy serving keywords with different meanings
- Catch-all ad groups named "General" or "Other"

### 4. Dynamic Keyword Insertion (DKI)

**Impact: Medium (when used correctly)**

DKI automatically inserts the triggering keyword into your ad copy. This can improve Ad Relevance when used strategically, but can also create problems.

**When DKI Works:**
- Ad groups with 3-5 closely related keywords that all read naturally in a headline
- Short keywords that fit within headline character limits
- Keywords that are grammatically correct as headline text

**When DKI Fails:**
- Long keywords that get truncated (fallback text shows instead)
- Keywords with poor grammar or abbreviations ("plmbr near me")
- Broad match keywords that trigger for unrelated searches
- Ad groups with diverse keyword themes (DKI cannot solve a structural problem)

**DKI Syntax:** `{KeyWord:Default Text}` — capitalizes each word. Alternatives: `{keyword:}` (lowercase), `{KEYWORD:}` (all caps).

### 5. Ad Copy-Keyword Alignment

**Impact: High**

Beyond keyword inclusion, the overall ad message must align with the keyword's intent. A keyword about "price" should have pricing information in the ad. A keyword about "reviews" should mention reviews or ratings. A keyword about "near me" should emphasize local presence.

**Intent Categories and Ad Copy Alignment:**

| Keyword Intent | Ad Copy Should Include |
|:--|:--|
| **Transactional** ("buy," "order," "hire") | Pricing, offers, CTA to purchase/book |
| **Informational** ("how to," "what is," "guide") | Educational angle, resources, expertise signals |
| **Navigational** (brand terms, specific products) | Brand name, product details, direct links |
| **Local** ("near me," city names) | Location, service area, local phone number |
| **Comparison** ("vs," "best," "review") | Differentiators, social proof, comparison data |

## Analysis Methodology

### Step 1: Ad Group Audit

For each ad group, calculate:
- Number of keywords
- Keyword theme cohesion score (how semantically similar are the keywords?)
- Number of distinct intents represented
- Ad copy keyword coverage (what % of keywords appear in any ad?)

### Step 2: Ad Copy-Keyword Matrix

Create a matrix showing which keywords are represented in which ad headlines and descriptions:

```
Ad Group: "Plumbing Services"
Keywords (12):
  emergency plumber        → In Headline 1? YES | In Description? YES
  plumber near me          → In Headline 1? NO  | In Description? YES
  affordable plumber       → In Headline 1? NO  | In Description? NO  ← Gap!
  plumbing repair          → In Headline 1? NO  | In Description? NO  ← Gap!
  fix leaky faucet         → In Headline 1? NO  | In Description? NO  ← Gap!
  drain cleaning service   → In Headline 1? NO  | In Description? NO  ← Gap!
  ...

Coverage: 2/12 keywords (17%) → POOR
Recommendation: Split into 3 ad groups by theme
```

### Step 3: RSA Headline Analysis

For Responsive Search Ads, analyze headline variety and keyword coverage:

```
RSA Analysis — Ad Group "Emergency Plumber"
Headlines (15 max, current: 8):
  H1: "Emergency Plumber Available 24/7"     — Contains keyword ✓
  H2: "Fast Response, Licensed Plumbers"     — Partial match ✓
  H3: "Call Now for Immediate Help"          — No keyword ✗
  H4: "Trusted Since 2005"                   — No keyword ✗
  H5: "Free Estimates Available"             — No keyword ✗
  H6: "Save 15% on First Visit"             — No keyword ✗
  H7: "Local Emergency Plumbing Experts"     — Contains keyword ✓
  H8: "5-Star Rated Plumbing Service"        — Partial match ✓

Keyword coverage: 4/8 headlines (50%)
Recommendation: Add 4-5 more headlines with keyword variations.
Pin H1 to Position 1 for guaranteed keyword visibility.
```

### Step 4: Competitor Ad Analysis

Where possible, note what competitors' ads look like for the same keywords. If competitors consistently include the keyword in Headline 1 and your ads do not, your Ad Relevance will be rated lower relatively.

### Step 5: Fix Prioritization

Rank fixes by:
1. Monthly spend on affected keywords
2. Current Ad Relevance rating (Below Average first)
3. Fix complexity (ad copy rewrite = low effort, ad group restructure = medium effort)

## Restructuring Playbook

When an ad group needs restructuring:

1. **Export all keywords** from the overloaded ad group
2. **Cluster by theme** — Group keywords that share the same root topic and intent
3. **Create new ad groups** — One per theme, with 3-8 keywords each
4. **Write new ads** — Each ad group gets dedicated ads with the theme keyword in Headline 1
5. **Set up negatives** — Cross-negative between the new ad groups to prevent overlap
6. **Pause old ad group** — Do not delete (preserve historical data)
7. **Monitor for 2-3 weeks** — Allow Google to recalculate QS for the new structure

## Output Format

1. **Account-Level Ad Relevance Summary** — Distribution of Above Avg / Avg / Below Avg
2. **Ad Group Health Report** — Each ad group graded on theme tightness and keyword coverage
3. **Keyword-Ad Gap Analysis** — Keywords with no representation in ad copy
4. **Restructuring Recommendations** — Specific ad groups to split, with proposed new structure
5. **Ad Copy Rewrites** — Suggested new headlines and descriptions for priority ad groups
6. **Estimated Impact** — Monthly savings from improved Ad Relevance ratings
