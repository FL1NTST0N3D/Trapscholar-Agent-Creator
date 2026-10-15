# QS Component Analysis

## Command
`/qs components`

## Purpose

Break down Quality Score into its three constituent components for every keyword in the account. Identify which component is the primary drag on QS for each keyword and ad group, and surface patterns that reveal systemic issues versus isolated problems.

## The Three Components

### Expected Click-Through Rate (Expected CTR)

**Weight: ~39% of Quality Score**

Expected CTR measures how likely your ad is to be clicked when shown for a particular keyword, relative to other advertisers bidding on the same keyword. This is Google's prediction, not your actual CTR.

**Rating levels:**
- **Above Average** — Your expected CTR is better than most competitors for this keyword. No action needed on this component.
- **Average** — Your expected CTR is in line with competitors. Room for improvement but not a priority unless other components are also Average or Above Average.
- **Below Average** — Your expected CTR is significantly worse than competitors. This is actively dragging down your QS and increasing your CPC.

**What drives Expected CTR:**
- Historical CTR performance on this keyword-ad combination
- Ad copy quality and relevance (does the headline grab attention?)
- Ad extensions utilization (sitelinks, callouts, structured snippets)
- Match type performance differences
- Device-specific CTR patterns (mobile vs desktop)
- Geographic CTR variation

**Common root causes of Below Average Expected CTR:**
- Generic ad copy that does not differentiate from competitors
- Missing or poor ad extensions
- Keyword in a loosely themed ad group with irrelevant ads showing
- High-impression, low-CTR match types (broad match without proper negatives)
- Ad fatigue from running the same ads for months without refresh

### Ad Relevance

**Weight: ~22% of Quality Score**

Ad Relevance measures how closely your ad copy matches the intent of the user's search query. Google analyzes the semantic relationship between the keyword, the ad text, and the likely user intent.

**Rating levels:**
- **Above Average** — Your ad is highly relevant to the keyword. The keyword appears in your ad and the messaging aligns with search intent.
- **Average** — Your ad is reasonably relevant but could be more tightly aligned.
- **Below Average** — Your ad does not adequately address the keyword or its intent. This often happens when ad groups contain too many unrelated keywords sharing the same ads.

**What drives Ad Relevance:**
- Keyword presence in Headline 1 or Headline 2
- Keyword presence in at least one description line
- Ad group structure (tight theming with 5-15 closely related keywords)
- Dynamic Keyword Insertion (DKI) when used appropriately
- Match between keyword intent (informational, navigational, transactional) and ad messaging
- Responsive Search Ad (RSA) pin strategy and headline variety

**Common root causes of Below Average Ad Relevance:**
- Ad groups with 50+ keywords spanning multiple topics
- No keyword in any headline
- Ad copy written for the ad group theme but not individual keywords
- Mismatched intent (informational keyword with hard-sell ad copy)
- Single ad per ad group with no RSA testing

### Landing Page Experience

**Weight: ~39% of Quality Score**

Landing Page Experience measures how relevant, useful, and user-friendly your landing page is for people who click your ad. Google uses a combination of automated analysis and user behavior signals.

**Rating levels:**
- **Above Average** — Your landing page provides an excellent experience. Fast, relevant, mobile-friendly, easy to navigate.
- **Average** — Your landing page is acceptable but does not stand out. Functional but not optimized.
- **Below Average** — Your landing page has significant issues. Slow load times, poor mobile experience, irrelevant content, or navigation problems.

**What drives Landing Page Experience:**
- Page load speed (Largest Contentful Paint under 2.5 seconds)
- Mobile responsiveness (works well on all screen sizes)
- Content relevance to the keyword and ad copy
- Easy navigation with clear next steps
- Transparent business information (about page, contact details, privacy policy)
- Original, substantive content (not thin affiliate pages or duplicated content)
- HTTPS security
- No intrusive interstitials or pop-ups that block content

**Common root causes of Below Average Landing Page Experience:**
- Slow server response times or unoptimized images
- Non-responsive design on mobile devices
- Sending all keywords to the homepage instead of dedicated landing pages
- Thin content with little useful information
- Missing trust signals (no reviews, no about page, no contact info)
- Aggressive pop-ups or auto-playing video

## Analysis Methodology

### Step 1: Export and Parse
Request or parse the keyword report with QS component columns. Map each keyword to its three component ratings.

### Step 2: Component Distribution
Calculate the distribution of Above Average, Average, and Below Average across all three components for the entire account:

```
Component Distribution:
                    Above Avg    Average    Below Avg
Expected CTR:         35%         40%         25%
Ad Relevance:         28%         45%         27%
Landing Page:         20%         35%         45%
```

### Step 3: Identify the Weakest Component
Determine which component has the highest percentage of Below Average ratings. This is the systemic weakness.

### Step 4: Cross-Reference with Spend
Weight the component analysis by spend. A Below Average rating on a keyword spending $10/day matters more than one spending $0.50/day.

### Step 5: Pattern Detection
Look for patterns:
- Do all keywords pointing to the same landing page have Below Average Landing Page Experience? (Landing page problem)
- Do all keywords in the same ad group have Below Average Ad Relevance? (Ad group structure problem)
- Do all keywords with a specific match type have Below Average Expected CTR? (Match type problem)

### Step 6: Priority Matrix
Create a priority matrix combining component weakness with spend impact:

| Priority | Criteria |
|----------|----------|
| Critical | Below Average + High Spend (top 20% by cost) |
| High | Below Average + Medium Spend |
| Medium | Average + High Spend |
| Low | Below Average + Low Spend |

## Output Format

Present the analysis as:

1. **Account-Level Component Summary** — Pie or bar chart of component ratings
2. **Weakest Component Identification** — Which component is the biggest drag, with spend-weighted evidence
3. **Campaign-Level Breakdown** — Component ratings rolled up by campaign
4. **Ad Group Hotspots** — Ad groups with the most Below Average ratings
5. **Keyword-Level Detail** — Top 20 keywords by spend with all three component ratings
6. **Root Cause Diagnosis** — Grouped findings (e.g., "15 keywords pointing to /homepage all have Below Average LP Experience")
7. **Fix Recommendations** — Ordered by estimated impact, with specific actions per component
