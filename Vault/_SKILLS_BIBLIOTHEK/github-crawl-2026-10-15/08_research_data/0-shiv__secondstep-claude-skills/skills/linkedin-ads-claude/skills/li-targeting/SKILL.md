# Targeting Sub-Skill

## Purpose

Audit and optimize LinkedIn Ads targeting configuration. Evaluate audience layering strategy, company and job attribute selection, exclusion logic, ABM list quality, and audience size appropriateness.

## LinkedIn Targeting Taxonomy

### Company Attributes

| Attribute | Description | Best For |
|-----------|-------------|----------|
| Company Name | Target specific companies (ABM) | Named account programs |
| Company Industry | 148 industries available | Industry-specific solutions |
| Company Size | 1-10, 11-50, 51-200, 201-500, 501-1000, 1001-5000, 5001-10000, 10000+ | Enterprise vs SMB segmentation |
| Company Revenue | Annual revenue ranges | Value-based targeting |
| Company Growth Rate | Fast-growing companies | Scaling companies need solutions |
| Company Connections | 1st-degree connections of employees | Warm audiences |
| Company Followers | Followers of specific company pages | Competitor conquest |

### Job Attributes

| Attribute | Description | Best For |
|-----------|-------------|----------|
| Job Title | Exact or keyword match | Precise role targeting |
| Job Function | 26 functions (IT, Marketing, Finance, etc.) | Broad functional reach |
| Job Seniority | Entry, Senior, Manager, Director, VP, CXO, Owner/Partner | Decision-maker targeting |
| Skills | 35,000+ skills from profiles | Capability-based targeting |
| Years of Experience | 1-2, 3-5, 6-8, 9-12, 12+ | Experience-level filtering |
| Member Groups | LinkedIn Groups membership | Interest/community targeting |

### Demographics & Education

| Attribute | Use Case |
|-----------|----------|
| Location | Country, state/region, metro area, city (required) |
| Age | 18-24, 25-34, 35-54, 55+ (limited for employment ads) |
| Gender | Male, Female (limited availability) |
| Schools | Target alumni of specific universities |
| Degrees | Associate, Bachelor, Master, Doctorate |
| Fields of Study | Engineering, Business, Computer Science, etc. |

## Targeting Layer Strategy

### The Golden Rule: 2-3 Layers Maximum

Layering means combining targeting attributes using AND logic. Each additional layer narrows the audience. LinkedIn recommends 2-3 layers for optimal performance.

**Effective Layering Examples:**

```
Layer 1 (Company): Industry = Software & IT Services
Layer 2 (Job): Seniority = Director, VP, CXO
Layer 3 (Job): Function = Information Technology
Result: IT leaders at software companies (~50,000-150,000)
```

```
Layer 1 (Company): Size = 201-5000 employees
Layer 2 (Job): Title contains "security" OR "CISO" OR "InfoSec"
Result: Security professionals at mid-market companies (~30,000-80,000)
```

**Over-Layering Mistake:**
```
Industry + Size + Seniority + Function + Skills + Years of Experience
Result: Audience of 2,000 -- too small, high CPMs, won't exit learning
```

### Ideal Audience Sizes by Format

| Format | Minimum | Ideal | Maximum |
|--------|---------|-------|---------|
| Sponsored Content | 25,000 | 50,000-300,000 | 500,000+ |
| Message/Conversation Ads | 15,000 | 30,000-100,000 | 200,000 |
| Text Ads | 50,000 | 100,000-500,000 | 1,000,000+ |
| Dynamic Ads | 25,000 | 50,000-300,000 | 500,000+ |

### ABM (Account-Based Marketing) Targeting

**Company Name Targeting:**
- Upload CSV with company names and domains
- Match rate target: >70% (below 70% = data quality issue)
- Maximum list size: 300,000 companies
- Combine with seniority/function to reach decision-makers at target accounts

**ABM Tiering Strategy:**
```
Tier 1 (Top 50 accounts):
  - Company Name targeting
  - All seniorities + functions
  - Highest budget per account
  - Personalized creative

Tier 2 (Next 200 accounts):
  - Company Name targeting
  - Director+ seniority
  - Specific functions only
  - Segment-level creative

Tier 3 (Industry/firmographic):
  - Industry + Size + Seniority targeting
  - No named accounts
  - Lowest CPL, highest volume
  - Generic value-prop creative
```

### Exclusion Strategy (Critical)

Always exclude these audiences:
1. **Existing customers** -- upload customer list, exclude from all acquisition campaigns
2. **Current employees** -- exclude your own company name
3. **Competitors** -- exclude competitor company names (prevents intel leaking)
4. **Recent converters** -- exclude people who submitted a Lead Gen Form in last 30-90 days
5. **Disqualified leads** -- upload disqualified lead list, exclude globally

## Audit Checklist

When auditing targeting, check these items:

1. **Audience Size Appropriateness** (4 pts)
   - Is each campaign audience within the ideal range for its format?
   - Are audiences large enough to exit learning phase?
   - Are there no audiences below 10,000 (except ABM Tier 1)?
   - Is the total addressable audience sufficient for the budget?

2. **Layer Depth & Quality** (4 pts)
   - Are campaigns using 2-3 targeting layers (not 1, not 5+)?
   - Are layers logically combined (company + job attributes)?
   - Is Job Title targeting using OR logic for synonymous titles?
   - Are Skills used as a supplementary layer, not primary?

3. **Exclusion Logic** (4 pts)
   - Are existing customers excluded from acquisition campaigns?
   - Are employees and competitors excluded?
   - Are recent converters excluded to prevent fatigue?
   - Is there a disqualified lead exclusion list?

4. **ABM Configuration** (4 pts)
   - Is there a company list uploaded for named account targeting?
   - Is the match rate above 70%?
   - Are ABM campaigns layered with seniority/function?
   - Is there a tiered ABM strategy (not one-size-fits-all)?

5. **Geographic Targeting** (4 pts)
   - Is location targeting specific enough (not just "United States")?
   - Are irrelevant regions excluded?
   - Is Audience Expansion OFF for MOFU/BOFU campaigns?
   - Are there separate campaigns for different geos if needed?

## Scoring

| Score | Rating | Meaning |
|-------|--------|---------|
| 18-20 | Elite | Sophisticated layering with full exclusions and ABM |
| 14-17 | Strong | Good targeting with minor gaps in exclusions or ABM |
| 10-13 | Average | Basic targeting, missing exclusions or poor audience sizes |
| 6-9 | Weak | Single-layer targeting, no exclusions, random audience sizes |
| 0-5 | Critical | No targeting strategy, audience too broad or too narrow |

## Common Targeting Mistakes

1. **Job Title only** -- misses people with non-standard titles. Use Function + Seniority as backup.
2. **Audience too narrow** -- under 10,000 audience for Sponsored Content = sky-high CPMs and no delivery.
3. **Audience too broad** -- 2M+ audience with no layers = wasted spend on irrelevant impressions.
4. **No exclusions** -- serving ads to existing customers is the #1 budget waste on LinkedIn.
5. **Audience Expansion ON for BOFU** -- LinkedIn adds similar-but-not-matching profiles, diluting BOFU quality.
6. **Ignoring Skills targeting** -- Skills are self-reported and highly indicative of buying intent for technical products.
7. **Not splitting by company size** -- Enterprise and SMB need different messaging; combined targeting = generic creative.
8. **Stale ABM lists** -- company lists not updated in 6+ months miss new target accounts and include churned ones.
