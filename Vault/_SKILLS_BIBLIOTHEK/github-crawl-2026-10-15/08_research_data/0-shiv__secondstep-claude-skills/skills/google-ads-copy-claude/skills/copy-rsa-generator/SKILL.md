# RSA Generator — Full Responsive Search Ad Creation

## Command: `/copy generate`

Generate a complete Responsive Search Ad with 15 headlines and 4 descriptions, each tagged with the copywriting framework used and pin recommendations.

## Required Inputs

Before generating, collect from the user:
- **Business/Product name**
- **Primary keyword** (the search term this ad targets)
- **Secondary keywords** (2-3 related terms)
- **USP** (what makes the offer unique — price, speed, guarantee, etc.)
- **Target audience** (who is searching)
- **Offer** (discount, free trial, free consultation, etc.)
- **Location** (if local business)
- **Goal** (leads, sales, calls, sign-ups)

## Headline Generation Strategy

Generate exactly 15 headlines (30 characters max each) using this distribution:

### Headline Categories (MUST include all 6):

**1. Benefit-Focused Headlines (3 headlines)**
Lead with the outcome the customer wants, not the feature.
- "Save 40% on Energy Bills"
- "Grow Revenue 3x Faster"
- "Pain-Free in 30 Days"

**2. Number/Stat Headlines (2 headlines)**
Specific numbers build credibility and catch the eye.
- "Trusted by 50,000+ Teams"
- "4.9-Star Rated Service"
- "15 Years of Excellence"

**3. Question Headlines (2 headlines)**
Mirror the searcher's intent as a question.
- "Need a Reliable Plumber?"
- "Looking for Better ROI?"
- "Ready to Scale Your Ads?"

**4. Urgency/Scarcity Headlines (2 headlines)**
Create time pressure or limited availability.
- "Limited Spots — Book Today"
- "Sale Ends This Friday"
- "Only 3 Openings Left"

**5. Social Proof Headlines (2 headlines)**
Leverage reviews, awards, certifications.
- "#1 Rated by Customers"
- "Award-Winning Service"
- "As Seen in Forbes"

**6. CTA Headlines (2 headlines)**
Direct action verbs that tell the searcher what to do next.
- "Get Your Free Quote Now"
- "Start Your Free Trial"
- "Book a Free Consultation"

**7. Keyword-Rich Headlines (2 headlines)**
Include the primary keyword naturally.
- "{Primary Keyword} Experts"
- "Best {Primary Keyword} Near You"
- "Affordable {Primary Keyword}"

## Description Generation Strategy

Generate exactly 4 descriptions (90 characters max each) using this structure:

**Description 1 — Problem + Solution + CTA**
Address the pain point, present your solution, end with CTA.
Example: "Tired of slow shipping? We deliver in 24 hours with free tracking. Order now and save 20%."

**Description 2 — USP + Social Proof + CTA**
Lead with differentiator, back with proof, end with action.
Example: "Only provider with lifetime warranty. Rated 4.9/5 by 10,000+ customers. Get started today."

**Description 3 — Features + Benefits**
List 2-3 key features and tie each to a benefit.
Example: "AI-powered analytics, real-time dashboards & custom reports. Make smarter decisions faster."

**Description 4 — Offer + Urgency + CTA**
Lead with the offer, add time pressure, close with CTA.
Example: "Save 30% this month only. Free setup, no contracts, cancel anytime. Claim your discount now."

## Pin Strategy Recommendations

Pinning locks a headline or description to a specific position. Use sparingly — over-pinning hurts Ad Strength.

**Recommended Pins:**
- Pin your **brand name headline** to H1 if brand awareness is critical
- Pin your **strongest CTA headline** to H1 or H2
- Pin your **offer headline** to H2 or H3
- Pin your **primary CTA description** to D1
- NEVER pin more than 2-3 elements total per RSA

**When to Pin:**
- Regulated industries (healthcare, finance) where certain disclosures must appear
- Brand guidelines require brand name in first position
- Specific offer must always be visible

**When NOT to Pin:**
- Standard lead gen or e-commerce campaigns
- When you want Google to optimize combinations (usually best)
- When you have fewer than 10 headlines (pinning further limits Google)

## Display Path Recommendations

Generate 2 display paths (15 characters each) that:
- Include the primary keyword or category
- Are readable and professional
- Example: `yoursite.com/Plumbing/Emergency` or `yoursite.com/Free-Quote/Today`

## Output Format

```
=== RESPONSIVE SEARCH AD ===
Campaign: [Campaign Name]
Ad Group: [Ad Group Name]
Primary Keyword: [keyword]

--- HEADLINES ---
H1  (XX chars) [Framework] [Pin: None]  "Headline text here"
H2  (XX chars) [Framework] [Pin: None]  "Headline text here"
...
H15 (XX chars) [Framework] [Pin: None]  "Headline text here"

--- DESCRIPTIONS ---
D1  (XX chars) [Framework] [Pin: D1]   "Description text here"
D2  (XX chars) [Framework] [Pin: None] "Description text here"
D3  (XX chars) [Framework] [Pin: None] "Description text here"
D4  (XX chars) [Framework] [Pin: None] "Description text here"

--- DISPLAY PATHS ---
Path 1: [path]
Path 2: [path]

--- AD STRENGTH PREDICTION ---
Uniqueness: X/10
Keyword Relevance: X/10
CTA Variety: X/10
Predicted Ad Strength: [Poor/Average/Good/Excellent]
```

## Post-Generation Checklist

After generating, verify:
- All 15 headlines are unique (no semantic duplicates)
- Character limits respected (count carefully — spaces and punctuation included)
- At least 5 of the 6 headline categories represented
- Primary keyword appears in at least 2 headlines
- At least 2 different CTAs used across headlines and descriptions
- No more than 3 items pinned
- Descriptions complement (not repeat) headline messaging
- Display paths are relevant and within 15 characters

## Variations

If the user asks for variations:
- Generate a second RSA with entirely different angles
- Swap frameworks (if first used AIDA, second uses PAS)
- Change the emotional tone (first = professional, second = casual)
- Test different USP emphasis (first = price, second = quality)
