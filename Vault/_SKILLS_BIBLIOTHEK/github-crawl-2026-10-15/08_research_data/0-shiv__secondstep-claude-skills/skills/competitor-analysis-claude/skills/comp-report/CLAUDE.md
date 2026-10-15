# Skill: Competitive Intelligence Report (`/comp report`)

## Purpose
Generate a comprehensive competitive intelligence report that synthesizes all available analyses into an executive-ready document. This is the master output that combines teardowns, positioning analysis, SWOT, pricing intelligence, ad analysis, content gaps, tech stack detection, and battlecard insights into a unified strategic document with clear recommendations.

## When to Use
- Quarterly or annual strategic planning sessions
- Board meetings requiring competitive landscape overview
- New market entry decisions
- Major product strategy pivots
- Investor due diligence materials
- Executive briefings on competitive dynamics

## Framework: CI Report Structure

### Part 1: Executive Brief (1 page)
The most critical section — many stakeholders will only read this:
- **Market Context**: Industry, TAM, growth rate, key trends (2-3 sentences)
- **Competitive Landscape Summary**: Number of competitors analyzed, market concentration, competitive intensity
- **Top 3 Findings**: The most important discoveries with strategic implications
- **Recommended Actions**: The 3-5 highest-priority moves
- **Overall Threat Assessment**: Low / Moderate / Elevated / High / Critical

### Part 2: Competitive Landscape Map
A visual overview of the competitive environment:
- **Positioning Map**: 2x2 matrix plotting all competitors on the most relevant dimensions
- **Market Share Estimates**: Relative size indicators (if available)
- **Competitive Tiers**: Categorize competitors into Direct, Adjacent, and Emerging
- **Movement Vectors**: Which direction each competitor is trending

Competitor tier definitions:
- **Direct**: Same product category, same target market, compete in deals
- **Adjacent**: Different product but same buyer, or same product but different market
- **Emerging**: New entrants, startups, or big tech moves that could disrupt

### Part 3: Individual Competitor Profiles
For each competitor analyzed, provide a structured profile:

```
| Dimension | Assessment |
|-----------|-----------|
| Threat Level | [Low/Med/High] |
| Primary Strength | [One sentence] |
| Primary Weakness | [One sentence] |
| Pricing Position | [Below/At/Above market] |
| Growth Trajectory | [Accelerating/Stable/Decelerating] |
| Win Rate Against | [%] (if known) |
```

Include a 3-sentence summary of each competitor's strategy and trajectory.

### Part 4: Cross-Competitor Analysis
Analyze patterns across all competitors:

**Feature Parity Matrix**:
```
| Feature | You | Comp A | Comp B | Comp C | Market Coverage |
|---------|-----|--------|--------|--------|----------------|
```

**Pricing Landscape**:
- Price range across the market (low to high)
- Pricing model distribution (per-seat, usage, flat-rate)
- Free tier prevalence and strategy

**Technology Comparison**:
- Common tech stack patterns
- Technology sophistication distribution
- Integration ecosystem overlap

**Content & Marketing Intensity**:
- Content volume comparison
- Channel strategy comparison
- Advertising intensity comparison

### Part 5: Strategic Implications
Translate findings into strategic guidance:

**Where You Win**:
- Dimensions where you have clear advantages
- Segments where you are the preferred choice
- Messaging angles that are uniquely yours

**Where You Are Vulnerable**:
- Competitor strengths that threaten your position
- Market trends that favor competitors
- Feature or pricing gaps that need addressing

**Market Whitespace**:
- Underserved segments or use cases
- Positioning angles no competitor owns
- Emerging needs that no one addresses yet

**Competitive Threats to Monitor**:
- Competitor moves that could disrupt your position
- New entrants to track
- Technology shifts that change the competitive landscape

### Part 6: Action Plan
Prioritized recommendations with clear ownership and timelines:

```
| Priority | Action | Owner | Timeline | Expected Impact | Effort |
|----------|--------|-------|----------|----------------|--------|
| P1 | | | | | |
| P2 | | | | | |
| P3 | | | | | |
```

Categorize actions by function:
- **Product**: Features to build, gaps to close
- **Sales**: Battlecard updates, training needs, competitive plays
- **Marketing**: Positioning changes, content priorities, messaging updates
- **Pricing**: Pricing adjustments, packaging changes, offer strategy
- **Strategy**: Market moves, partnership opportunities, M&A considerations

### Part 7: Appendix
Supporting data and methodology:
- Data sources used with access dates
- Confidence levels for key data points
- Methodology notes and limitations
- Raw data tables and supporting evidence
- Glossary of terms and abbreviations

## Output Template

```markdown
# Competitive Intelligence Report
**Prepared for**: [Company Name]
**Date**: [YYYY-MM-DD]
**Competitors Analyzed**: [List]
**Analyst**: Claude Code CI Skill
**Classification**: [Internal / Confidential]

---

## Executive Brief

### Market Context
[2-3 sentences on market dynamics]

### Competitive Landscape
[Summary of competitive environment]

### Top Findings
1. [Finding + implication]
2. [Finding + implication]
3. [Finding + implication]

### Recommended Actions
1. [Action + expected impact]
2. [Action + expected impact]
3. [Action + expected impact]

### Overall Threat Assessment: [Level]

---

## Competitive Landscape Map

### Positioning Matrix
[2x2 map with competitors plotted]

### Competitor Tiers
| Tier | Competitors | Threat Level |
|------|------------|-------------|
| Direct | | |
| Adjacent | | |
| Emerging | | |

---

## Competitor Profiles

### [Competitor A]
[Structured profile]

### [Competitor B]
[Structured profile]

---

## Cross-Competitor Analysis

### Feature Parity
[Matrix]

### Pricing Landscape
[Comparison]

### Technology Comparison
[Summary]

---

## Strategic Implications

### Where You Win
[Advantages]

### Where You Are Vulnerable
[Risks]

### Market Whitespace
[Opportunities]

---

## Action Plan
| Priority | Action | Owner | Timeline | Impact | Effort |
|----------|--------|-------|----------|--------|--------|

---

## Appendix
### Data Sources
[List with dates]

### Confidence Assessment
[Data quality notes]

### Methodology
[How the analysis was conducted]
```

## Best Practices
1. Start with the executive brief and make it stand alone. If a CEO reads nothing else, the brief should convey the key messages.
2. Use consistent competitor names and abbreviations throughout the report to avoid confusion.
3. Date-stamp everything. Competitive intelligence decays rapidly. A report from 3 months ago may already be outdated.
4. Distinguish clearly between facts and inferences. Use confidence tags throughout.
5. Include a "so what" for every finding. Raw data without interpretation wastes the reader's time.
6. Keep the main report under 10 pages. Use the appendix for supporting detail.
7. Schedule a quarterly refresh cadence. The first report is the hardest; updates are faster because you have the framework in place.
8. Track which recommendations were implemented and what resulted. CI is only valuable if it drives action.
