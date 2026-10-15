# Copy Report — Ad Copy Audit Report Generator

## Command: `/copy report`

Generate a comprehensive ad copy audit report with scoring across multiple dimensions, specific issues, and prioritized recommendations.

## Required Inputs

- **Account/Campaign name**: For report labeling
- **Current RSA copy**: All headlines and descriptions for each ad
- **Keywords**: Ad group keywords (to check relevance)
- **Performance data** (optional): CTR, conversion rate, impressions, Ad Strength rating
- **Competitor ads** (optional): For competitive context
- **Landing page URL** (optional): To check copy-to-landing-page alignment

## Report Structure

### Section 1: Executive Summary

One paragraph summarizing the overall health of the ad copy, the biggest issue, and the single most impactful fix.

```
=== AD COPY AUDIT REPORT ===
Account: [name]
Campaign: [name]
Date: [date]
Audited by: Claude Code — Google Ads Copy Skill

EXECUTIVE SUMMARY:
[2-3 sentences: overall assessment, biggest gap, recommended action]

OVERALL SCORE: XX/100
RATING: [Critical / Needs Work / Solid / Excellent]
```

### Section 2: Scorecard

Score each dimension on a 1-10 scale with letter grades:

```
=== SCORECARD ===

| Dimension | Score | Grade | Status |
|-----------|-------|-------|--------|
| Headline Uniqueness | X/10 | [A-F] | [pass/fail icon] |
| Keyword Relevance | X/10 | [A-F] | |
| CTA Diversity | X/10 | [A-F] | |
| Emotional Impact | X/10 | [A-F] | |
| Character Utilization | X/10 | [A-F] | |
| Framework Variety | X/10 | [A-F] | |
| Ad Strength Prediction | X/10 | [A-F] | |
| Landing Page Alignment | X/10 | [A-F] | |
| Competitive Differentiation | X/10 | [A-F] | |
| Offer Clarity | X/10 | [A-F] | |

OVERALL: XX/100 | Grade: [A-F]
```

### Scoring Rubric

**Headline Uniqueness (1-10)**
- 1-3: Multiple semantic duplicates, fewer than 8 unique messages
- 4-6: Some overlap, 8-11 unique messages
- 7-8: All headlines distinct, 12-14 unique messages
- 9-10: 15 completely unique headlines with different frameworks

**Keyword Relevance (1-10)**
- 1-3: Primary keyword missing from all headlines and descriptions
- 4-6: Primary keyword in 1 headline only
- 7-8: Primary keyword in 2+ headlines AND 1+ description
- 9-10: Primary + secondary keywords naturally distributed

**CTA Diversity (1-10)**
- 1-3: Same CTA repeated or no CTA
- 4-6: 1-2 unique CTAs
- 7-8: 3-4 unique CTAs with varied verbs
- 9-10: 5+ CTAs tailored to different user intents

**Emotional Impact (1-10)**
- 1-3: No power words, flat tone throughout
- 4-6: 1-2 power words, mild emotional charge
- 7-8: Multiple emotions represented, strong power words
- 9-10: Strategic emotion mix matching industry best practices

**Character Utilization (1-10)**
- 1-3: Most headlines under 15 characters (wasted space)
- 4-6: Average headline length 18-22 characters
- 7-8: Good mix of short (15-20) and long (27-30) headlines
- 9-10: Optimal distribution with all descriptions at 85-90 characters

**Framework Variety (1-10)**
- 1-3: All headlines use the same approach
- 4-6: 2-3 frameworks represented
- 7-8: 5-6 frameworks represented
- 9-10: 7+ frameworks with strategic distribution

**Ad Strength Prediction (1-10)**
- 1-3: Predicted Poor
- 4-5: Predicted Average
- 6-7: Predicted Good
- 8-10: Predicted Excellent

**Landing Page Alignment (1-10)**
- 1-3: Ad promises don't match landing page content
- 4-6: Partial alignment, some messaging gaps
- 7-8: Strong alignment, consistent messaging
- 9-10: Perfect alignment — every ad claim is supported on the page

**Competitive Differentiation (1-10)**
- 1-3: Generic copy that any competitor could use
- 4-6: Some unique elements but mostly category-standard messaging
- 7-8: Clear differentiators, specific proof points
- 9-10: Ownable positioning that competitors can't easily replicate

**Offer Clarity (1-10)**
- 1-3: No clear offer or value proposition
- 4-6: Vague offer ("great deals")
- 7-8: Clear, specific offer with terms
- 9-10: Compelling offer with urgency, specifics, and risk reversal

### Section 3: Detailed Findings

For each dimension scoring below 7, provide:

```
=== DETAILED FINDINGS ===

ISSUE 1: [Dimension Name] — Score: X/10
  Problem: [Specific description of what's wrong]
  Evidence:
    - H3 "Top Plumber in Dallas" duplicates H1 "Best Plumber in Dallas"
    - H7 "Call Us Today" duplicates H12 "Call Now"
  Impact: [How this hurts performance]
  Priority: [Critical / High / Medium / Low]

ISSUE 2: [Dimension Name] — Score: X/10
  [same structure]
```

### Section 4: Headline-by-Headline Analysis

Analyze every single headline:

```
=== HEADLINE ANALYSIS ===

H1  (28 chars) "Best Plumber in Dallas TX"
    Framework: Social Proof + Local
    Keyword: "plumber" (primary) — PRESENT
    Emotion: Trust (mild) — Score: 4/10
    Uniqueness: Unique
    Issues: None

H2  (22 chars) "Top Plumber in Dallas"
    Framework: Social Proof + Local
    Keyword: "plumber" (primary) — PRESENT
    Emotion: Trust (mild) — Score: 3/10
    Uniqueness: DUPLICATE of H1 (same meaning)
    Issues: Replace with different angle

[Continue for all headlines]
```

### Section 5: Description Analysis

Same detailed analysis for each description:

```
=== DESCRIPTION ANALYSIS ===

D1  (87 chars) "Licensed & insured Dallas plumber. 24/7 emergency service. Call now for a free estimate."
    Framework: Trust + CTA
    Keywords: "plumber" (present), "emergency" (present)
    USPs mentioned: Licensed, insured, 24/7, free estimate
    CTA: "Call now" — Strong, appropriate for emergency services
    Emotion: Trust — Score: 6/10
    Character utilization: 87/90 — Good
    Issues: None — strong description

[Continue for all descriptions]
```

### Section 6: Recommendations (Prioritized)

```
=== RECOMMENDATIONS ===

PRIORITY 1 — CRITICAL (Do immediately):
  1. Replace H2 "Top Plumber in Dallas" with "24/7 Emergency Repairs" (22 chars)
     Reason: Eliminates semantic duplicate, adds benefit messaging

  2. Add keyword "drain cleaning" to at least 1 headline
     Suggestion: H8 "Expert Drain Cleaning" (21 chars)
     Reason: Primary keyword missing, hurting relevance score

PRIORITY 2 — HIGH (Do this week):
  3. Add urgency to at least 2 headlines
     Suggestion: H10 "Book Today — Save 15%" (21 chars)
     Reason: No urgency in current copy, missing conversion driver

  4. Diversify CTAs — currently only "Call Now" used
     Suggestion: Add "Book Online Now" and "Get Free Estimate"
     Reason: CTA diversity improves Ad Strength

PRIORITY 3 — MEDIUM (Do this month):
  5. Increase description character utilization
     D3 is only 62 characters — expand to 85-90
     Suggestion: [rewritten description]

PRIORITY 4 — LOW (Nice to have):
  6. Test emotional trigger variation
     Current copy is 90% trust-focused
     Add 2-3 urgency or curiosity headlines for variety
```

### Section 7: Revised Ad (Complete)

Present the full corrected RSA with all recommendations applied:

```
=== REVISED RSA ===

H1  (XX chars) [Framework] "..." [Changed/Kept]
H2  (XX chars) [Framework] "..." [Changed/Kept]
...
H15 (XX chars) [Framework] "..." [Changed/Kept]

D1  (XX chars) [Framework] "..." [Changed/Kept]
D2  (XX chars) [Framework] "..." [Changed/Kept]
D3  (XX chars) [Framework] "..." [Changed/Kept]
D4  (XX chars) [Framework] "..." [Changed/Kept]

Path 1: [path]
Path 2: [path]

REVISED SCORES:
| Dimension | Before | After | Change |
|-----------|--------|-------|--------|
| Headline Uniqueness | X | Y | +Z |
| Keyword Relevance | X | Y | +Z |
| ... | | | |
| OVERALL | XX | YY | +ZZ |

PREDICTED AD STRENGTH: [Excellent]
```

### Section 8: Next Steps

```
=== NEXT STEPS ===

1. Implement Priority 1 changes immediately
2. Monitor Ad Strength in Google Ads (should update within 24 hours)
3. Run for 14 days before evaluating performance changes
4. After 14 days, run A/B test on [specific element]
5. Schedule next audit in 30 days
```

## Report Formatting Notes

- Use tables for scanability
- Bold the most critical issues
- Include character counts on every headline and description
- Color-code scores if output format supports it (green 8-10, yellow 5-7, red 1-4)
- Keep recommendations actionable — always include the exact replacement text
- The revised ad at the end should be copy-paste ready for Google Ads
