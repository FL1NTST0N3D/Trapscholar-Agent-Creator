---
name: pmax-creative-scoring
description: "Score Performance Max creative diversity and quality across text, image, and video assets. Analyzes asset combination performance, responsive ad preview quality, and creative strategy alignment."
allowed-tools:
  - Bash
  - Read
  - Grep
---

# PMax Creative Scoring Skill

## Purpose

PMax generates thousands of ad combinations from your assets. The quality and diversity of your creative inputs directly determines the quality of these combinations. This skill evaluates whether your creative strategy provides PMax's machine learning with sufficient raw material to generate high-performing ad combinations across all Google inventory (Search, Shopping, Display, YouTube, Discover, Gmail, Maps).

## Trigger

Activated by `/pmax creative` or as part of `/pmax audit`.

## Data Requirements

Ask the user for:
1. Complete asset inventory per asset group (text, images, videos, logos)
2. Asset performance ratings (Best/Good/Low/Unrated)
3. Asset group combination reports (if available from API)
4. Ad strength indicator per asset group (Excellent/Good/Average/Poor)
5. Screenshots of responsive ad previews (optional but helpful)
6. Creative strategy brief or brand guidelines

## Creative Diversity Assessment

### Why Diversity Matters

PMax's machine learning needs variety to:
- Test different messaging angles across placements
- Match creative to audience intent and funnel stage
- Avoid ad fatigue (same creative shown repeatedly)
- Optimize for different ad formats (Search text, Display banner, YouTube video, etc.)

### Diversity Dimensions

#### 1. Message Angle Diversity

Every asset group should cover these messaging angles in headlines and descriptions:

| Angle | Example | Required |
|---|---|---|
| **Benefit-led** | "Save 3 Hours Every Week" | Yes |
| **Feature-led** | "AI-Powered Dashboard Included" | Yes |
| **Social proof** | "Trusted by 10,000+ Teams" | Yes |
| **Urgency/Scarcity** | "Limited Time: 40% Off" | Recommended |
| **Question/Problem** | "Tired of Manual Reports?" | Recommended |
| **Brand** | "CloudMetrics — Your Data, Simplified" | Yes |
| **CTA-focused** | "Start Free Trial Today" | Yes |
| **Price/Value** | "Plans from $29/month" | Situational |
| **Differentiator** | "The Only Tool with Real-Time Sync" | Recommended |
| **Emotional** | "Finally, Reporting That Makes Sense" | Recommended |

**Scoring**: Each unique angle present = points. Minimum 5 angles, ideal 8+.

#### 2. Visual Content Diversity

Images should cover these visual categories:

| Category | What | Examples |
|---|---|---|
| **Product/Service** | Clear product shots or service visualization | Product on white, product in context |
| **Lifestyle** | People using/benefiting from product | Customer using product, team collaborating |
| **Benefit illustration** | Visual representation of value prop | Before/after, data visualization |
| **Brand** | Logo-centric, brand identity images | Logo on colored background, brand pattern |
| **Testimonial** | Customer quotes overlaid on images | Photo + quote, review screenshot |
| **Seasonal/Promotional** | Time-sensitive creative | Holiday theme, sale banner |

**Scoring**: Each category present (in appropriate orientation) = points. Minimum 3 categories, ideal 5+.

#### 3. Video Content Diversity

| Type | Purpose | Format |
|---|---|---|
| **Product demo** | Show the product/service in action | 15-30s, any orientation |
| **Testimonial** | Customer telling their story | 30-60s, ideally vertical |
| **Brand story** | Company values, mission | 30-60s, horizontal |
| **Tutorial/How-to** | Educational content | 30-90s, horizontal |
| **UGC-style** | Authentic, phone-recorded feel | 15-30s, vertical |
| **Promotional** | Sale, offer, limited-time deal | 15s, any orientation |

**Scoring**: Each type present = points. Minimum 1 video type, ideal 3+.

### Ad Strength Indicator

Google provides an "Ad Strength" rating for each asset group:

| Rating | Meaning | Action |
|---|---|---|
| **Excellent** | Maximum asset diversity and quantity | Maintain, optimize based on performance ratings |
| **Good** | Near-optimal, minor gaps | Add 1-2 more assets in weak areas |
| **Average** | Notable gaps in asset coverage | Significant additions needed |
| **Poor** | Insufficient assets for effective testing | Critical: add assets immediately |

**Note**: Ad Strength is a measure of input diversity, NOT performance. An "Excellent" ad strength can still perform poorly if the messaging is wrong. Conversely, a "Good" ad strength might outperform if messaging is highly resonant. Use Ad Strength as a hygiene check, not a performance predictor.

## Asset Combination Analysis

### How PMax Combines Assets

PMax creates ad combinations by mixing:
- **Search ads**: Headline 1 + Headline 2 + Headline 3 + Description 1 + Description 2
- **Display ads**: Image + Headline + Long Headline + Description + Logo + CTA
- **YouTube ads**: Video + Headline + Long Headline + Description + CTA
- **Discovery ads**: Image(s) + Headline + Description + Logo
- **Gmail ads**: Image + Headline + Description + Logo + CTA

With maximum assets (15 headlines, 5 long headlines, 5 descriptions, 20 images, 5 videos, 5 logos), PMax can generate **tens of thousands** of unique combinations.

### Combination Quality Checks

Not all combinations work well. Check for:

1. **Contradictory combinations**: "Free Trial" headline with "$99/month" description
2. **Redundant combinations**: Headline and description saying the same thing
3. **Mismatch combinations**: Product image with service description
4. **Truncation issues**: Long headlines getting cut off on mobile placements
5. **Visual-text mismatch**: Image showing Product A, text describing Product B

### Combination Scoring Factors

| Factor | Weight | Assessment |
|---|---|---|
| No contradictory pairings possible | 25% | Review all headline-description combos |
| No redundant messaging pairings | 20% | Each asset adds unique information |
| Visual-text alignment | 20% | Images match the message themes |
| Format coverage | 20% | Assets cover Search + Display + Video formats |
| Brand consistency | 15% | All combinations feel like the same brand |

## Responsive Ad Preview Analysis

If the user provides screenshots or descriptions of ad previews:

### Preview Quality Checklist
- [ ] Headlines readable and complete (no awkward truncation)
- [ ] Images look good at all sizes (large banner, small square, mobile)
- [ ] Logo visible and properly sized at smallest placement
- [ ] Call-to-action button text appropriate
- [ ] Color contrast sufficient (text readable over images)
- [ ] Brand identity consistent across preview variations
- [ ] No visual clutter (too many elements competing)
- [ ] Text on images readable at all sizes

### Platform-Specific Preview Concerns

| Platform | Key Concern |
|---|---|
| Search | Headlines work in 2-line and 3-line configurations |
| Display | Image quality at 300x250 and 728x90 sizes |
| YouTube | Video thumbnail compelling, first 5 seconds hook |
| Discover | Image and headline create curiosity, feed-native feel |
| Gmail | Subject-line-like headline, preview text engaging |
| Maps | Local relevance clear, distance/address visible |

## Creative Refresh Strategy

### When to Refresh Assets

| Signal | Action | Frequency |
|---|---|---|
| >30% of assets rated "Low" | Replace low-rated assets | Immediately |
| CTR declining week-over-week for 3+ weeks | Introduce new creative angles | Every 2-4 weeks |
| Same assets for 90+ days | Proactive refresh | Quarterly minimum |
| Seasonal changes | Update seasonal creative | Each season |
| New product/service launch | Create dedicated asset group | As needed |
| Competitor creative shift | Match or differentiate | Monitor monthly |

### Refresh Best Practices
1. **Never remove all assets at once** — PMax needs continuity for learning
2. **Replace 20-30% of assets per cycle** — Gradual improvement
3. **Keep "Best" rated assets** — They've earned their place
4. **Replace "Low" rated first** — Lowest hanging fruit
5. **Test new angles** — Don't just make minor variations of existing assets
6. **Document what works** — Build a creative playbook over time

## Scoring Rubric (0-100)

### Creative Diversity (0-40 points)

| Criteria | Points |
|---|---|
| 8+ message angles covered | 15 |
| 4+ visual content categories | 10 |
| 2+ video content types | 8 |
| All three orientations (landscape, square, portrait) for images | 4 |
| All three orientations for video | 3 |

### Asset Quality (0-30 points)

| Criteria | Points |
|---|---|
| Ad Strength: Excellent = 10, Good = 7, Average = 4, Poor = 0 | 10 |
| >30% assets rated Best | 8 |
| <15% assets rated Low | 7 |
| No contradictory asset combinations | 5 |

### Creative Strategy (0-30 points)

| Criteria | Points |
|---|---|
| Different asset groups have different creative themes | 10 |
| Creative refreshed within last 90 days | 8 |
| Creative aligned with audience signals per asset group | 7 |
| Documented creative strategy/brief exists | 5 |

## Output Format

```
## Creative Scoring Results

### Creative Score: XX/100

### Diversity Assessment
| Dimension | Coverage | Status |
|---|---|---|
| Message angles | X/10 | OK/WARNING/CRITICAL |
| Visual categories | X/6 | OK/WARNING/CRITICAL |
| Video types | X/6 | OK/WARNING/CRITICAL |
| Orientation coverage | [list] | OK/WARNING |

### Ad Strength: [Excellent/Good/Average/Poor]

### Asset Performance Distribution
| Rating | Count | % | Status |
|---|---|---|---|
| Best | X | X% | OK/WARNING |
| Good | X | X% | OK/WARNING |
| Low | X | X% | OK/WARNING |
| Unrated | X | X% | OK/WARNING |

### Combination Quality
- Contradictory pairs found: X
- Redundant pairs found: X
- Visual-text mismatches: X

### Creative Refresh Status
- Last asset update: [date]
- Assets older than 90 days: X
- Low-rated assets pending replacement: X

### Critical Issues
- [List findings]

### Recommendations
1. [Prioritized creative action items]
```
