# Campaign Structure Sub-Skill

## Purpose

Audit and optimize LinkedIn Ads campaign structure for full-funnel B2B demand generation. Evaluate campaign group organization, naming conventions, objective selection, and funnel alignment.

## Full-Funnel Campaign Architecture

### TOFU -- Top of Funnel (Awareness & Education)

**Objective:** Brand Awareness or Video Views

**Recommended Formats:**
- Sponsored Content (Single Image) -- thought leadership, industry insights
- Video Ads -- brand story, product explainers (15-30 seconds optimal)
- Document Ads -- ungated educational content to build trust

**Targeting:** Broad industry + seniority targeting. Audience size: 100,000-500,000+. Use Audience Expansion ON for TOFU campaigns to maximize reach at low cost.

**KPIs:** Impressions, Video View Rate (25-35% benchmark), Engagement Rate (>0.5%), CPM ($6-$12 target)

**Budget Allocation:** 20-30% of total LinkedIn spend. TOFU feeds the funnel -- underspending here means MOFU/BOFU audiences shrink over time.

### MOFU -- Middle of Funnel (Consideration & Engagement)

**Objective:** Website Visits, Engagement, or Lead Generation

**Recommended Formats:**
- Document Ads -- gated whitepapers, case studies, benchmarks (22.73% form completion rate)
- Carousel Ads -- product feature breakdowns, comparison guides (2x CTR vs single image)
- Video Ads -- customer testimonials, product demos (60-90 seconds)
- Conversation Ads -- multi-CTA content journeys with branching logic

**Targeting:** Retargeting TOFU engagers + refined prospecting. Audience size: 25,000-150,000. Layer company attributes (size, industry) with job attributes (seniority, function).

**KPIs:** CTR (0.5-0.8%), CPC ($3-$7), Content Downloads, Engagement Rate, CPL ($75-$200)

**Budget Allocation:** 50-60% of total LinkedIn spend. This is where LinkedIn excels -- gated content + Lead Gen Forms = qualified pipeline.

### BOFU -- Bottom of Funnel (Conversion & Decision)

**Objective:** Lead Generation or Website Conversions

**Recommended Formats:**
- Lead Gen Forms -- demo requests, consultation booking, free trial (pre-filled fields reduce friction)
- Message Ads -- personalized outreach to high-intent segments (50%+ open rate)
- Single Image -- direct response with strong CTA (lowest CPL at scale)
- Conversation Ads -- qualification flows that route leads to appropriate offers

**Targeting:** Retargeting website visitors (30/60/90 day windows), Lead Gen Form openers who did not submit, video viewers (50%+ completion). Audience size: 5,000-50,000. Use ABM company lists for named account targeting.

**KPIs:** CPL ($150-$600), Conversion Rate (2-5%), Lead-to-MQL rate, Cost per MQL, Pipeline influenced

**Budget Allocation:** 15-25% of total LinkedIn spend. Smaller audiences but highest intent = highest CPL but best ROI.

## Campaign Group Best Practices

### Naming Convention
Use a consistent, parseable naming convention across all campaign groups and campaigns:

```
[FunnelStage]_[Product/Service]_[Audience]_[Format]_[Date]
```

**Examples:**
- `TOFU_Platform_ITDirectors_Video_2026Q1`
- `MOFU_SecuritySuite_CISOs_Document_2026Q1`
- `BOFU_Demo_Retargeting_LeadGen_2026Q1`

### Campaign Group Organization

**Option A: By Funnel Stage (Recommended for most)**
```
Campaign Group: TOFU - Brand Awareness
  Campaign: TOFU_Video_ITLeaders_15s
  Campaign: TOFU_SingleImage_ThoughtLeadership

Campaign Group: MOFU - Content & Engagement
  Campaign: MOFU_Document_Whitepaper_CISOs
  Campaign: MOFU_Carousel_CaseStudy_VPs

Campaign Group: BOFU - Lead Generation
  Campaign: BOFU_LeadGen_DemoRequest_Retargeting
  Campaign: BOFU_Message_DirectOutreach_ABM
```

**Option B: By Product Line (For multi-product companies)**
```
Campaign Group: Product A - Full Funnel
  Campaign: ProdA_TOFU_Video_Awareness
  Campaign: ProdA_MOFU_Document_Whitepaper
  Campaign: ProdA_BOFU_LeadGen_Demo

Campaign Group: Product B - Full Funnel
  ...
```

**Option C: By Account Tier (For ABM-heavy strategies)**
```
Campaign Group: Tier 1 Accounts (Named)
Campaign Group: Tier 2 Accounts (Industry)
Campaign Group: Tier 3 Accounts (Broad)
```

## Audit Checklist

When auditing campaign structure, check these items:

1. **Campaign Group Organization** (3 pts)
   - Are campaign groups logically organized (by funnel, product, or account tier)?
   - Is there clear separation between prospecting and retargeting?
   - Are campaign groups named consistently?

2. **Naming Convention** (3 pts)
   - Is there a documented naming convention?
   - Does every campaign follow the convention?
   - Can you parse funnel stage, audience, and format from the name?

3. **Objective Alignment** (3 pts)
   - Are TOFU campaigns using Brand Awareness or Video Views?
   - Are MOFU campaigns using Engagement or Lead Generation?
   - Are BOFU campaigns using Lead Generation or Conversions?

4. **Funnel Coverage** (3 pts)
   - Does the account have campaigns at all three funnel stages?
   - Is there a clear retargeting chain (TOFU engagers to MOFU to BOFU)?
   - Are audience exclusions preventing funnel stage overlap?

5. **Campaign Volume** (3 pts)
   - Are there at least 2 ads per campaign for testing?
   - Are campaigns consolidated enough to exit learning phase?
   - Is budget not spread too thin across too many campaigns?

## Scoring

| Score | Rating | Meaning |
|-------|--------|---------|
| 13-15 | Elite | Textbook funnel structure |
| 10-12 | Strong | Minor naming or organization gaps |
| 7-9 | Average | Missing funnel stages or poor organization |
| 4-6 | Weak | No clear funnel strategy |
| 0-3 | Critical | Random campaign structure, no strategy |

## Common Mistakes

1. **No funnel differentiation** -- all campaigns target the same audience with the same objective
2. **Too many campaigns** -- budget spread across 15+ campaigns, none exits learning phase (LinkedIn needs ~15 conversions/week)
3. **Wrong objective for funnel stage** -- using Brand Awareness for BOFU or Conversions for TOFU
4. **No retargeting chain** -- TOFU and BOFU run independently with no audience flow
5. **Inconsistent naming** -- impossible to analyze performance by dimension without parsing campaign names
6. **No audience exclusions** -- existing customers seeing acquisition campaigns, wasting budget
