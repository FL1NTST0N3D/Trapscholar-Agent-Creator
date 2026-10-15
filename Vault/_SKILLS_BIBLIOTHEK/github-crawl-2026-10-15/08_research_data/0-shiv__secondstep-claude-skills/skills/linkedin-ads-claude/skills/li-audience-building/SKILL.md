# Audience Building Sub-Skill

## Purpose

Audit and optimize LinkedIn Matched Audiences configuration. Evaluate website retargeting setup, contact list uploads, lookalike audience strategy, event audiences, and audience expansion settings. Ensure retargeting pools are properly built and maintained.

## LinkedIn Matched Audiences Overview

Matched Audiences are custom audience segments built from your own data sources. They consistently outperform pure demographic targeting because they leverage known intent signals.

**Types of Matched Audiences:**
1. Website Retargeting (Insight Tag)
2. Contact List Targeting (email/company upload)
3. Lookalike Audiences
4. Event Audiences
5. Lead Gen Form Retargeting
6. Video Viewing Audiences
7. Company Page Audiences
8. Single Image Ad Audiences

## Website Retargeting

### Setup Requirements
- LinkedIn Insight Tag installed on all website pages
- Minimum audience size: 300 members (LinkedIn requirement to serve ads)
- Recommended minimum: 1,000+ members for meaningful delivery

### Retargeting Segments to Create

| Segment | Definition | Audience Window | Use Case |
|---------|-----------|----------------|----------|
| All Visitors | Any page visit | 30 days | Broad retargeting |
| All Visitors | Any page visit | 90 days | Larger pool for small sites |
| All Visitors | Any page visit | 180 days | Maximum reach retargeting |
| Pricing Page | /pricing URL | 30 days | High-intent BOFU |
| Product Pages | /product/* URLs | 60 days | MOFU consideration |
| Blog Readers | /blog/* URLs | 90 days | TOFU content consumers |
| Demo/Contact | /demo or /contact | 30 days | Highest intent |
| Converters | /thank-you URL | 180 days | Exclusion list |

### Retargeting Best Practices
- Create overlapping windows (30/60/90/180 days) for frequency and recency control
- Always exclude converters from acquisition retargeting
- Segment by page category for message relevance
- Combine website retargeting with job attribute targeting for precision
- Minimum 1,000 matched members per segment for reliable delivery

## Contact List Targeting

### Upload Options

| List Type | Match Field | Match Rate (Typical) | Best For |
|-----------|------------|---------------------|----------|
| Email List | Work email | 60-80% | CRM-based targeting |
| Company List | Company name + domain | 70-90% | ABM targeting |
| Combined | Email + company | 70-85% | Highest precision |

### Contact List Strategy

**Lists to Maintain:**
1. **Customer List** -- for exclusion AND cross-sell/upsell campaigns
2. **Open Opportunities** -- active pipeline, reinforce with ads
3. **Lost/Closed-Lost** -- re-engagement after 90+ days
4. **MQL/SQL List** -- nurture with mid-funnel content
5. **Event Attendees** -- follow-up campaigns post-event
6. **Newsletter Subscribers** -- retarget with premium content
7. **Target Account List** -- ABM company targeting

### Upload Best Practices
- Refresh lists every 30 days (stale lists = wasted spend on churned contacts)
- Use work emails, not personal (LinkedIn matches on work email)
- Include company domain alongside email for better match rates
- Segment lists by stage/intent for tailored messaging
- Minimum list size: 1,000 emails for reliable matching (300 minimum matched)

## Lookalike Audiences

### How LinkedIn Lookalikes Work
LinkedIn analyzes your source audience (contact list, website visitors, or company list) and finds members with similar professional attributes: job titles, skills, industries, company sizes, and more.

### Lookalike Configuration

| Setting | Options | Recommendation |
|---------|---------|----------------|
| Source Audience | Contact list, website audience, company list | Use highest-quality source (customers > MQLs > all leads) |
| Country | Required selection | Match campaign targeting geography |
| Audience Size | Not configurable (LinkedIn determines) | Typically 15-30x source size |

### Lookalike Best Practices
- Use customer list as seed (not all leads) for highest quality
- Create separate lookalikes per segment (enterprise customers vs SMB customers)
- Do NOT use lookalikes for BOFU -- they are prospecting audiences
- Combine lookalike with 1-2 targeting layers for precision
- Refresh source audience quarterly to keep lookalike current
- Exclude source audience from lookalike campaign to avoid overlap

## Event & Engagement Audiences

### Event Audiences
- Created from LinkedIn Events (webinars, live events)
- Target: Registered, Attended, or No-Show segments
- Great for post-event nurture campaigns
- Persist for 365 days

### Lead Gen Form Audiences
| Segment | Definition | Use Case |
|---------|-----------|----------|
| Form Openers | Opened but did not submit | Retarget with simplified offer |
| Form Submitters | Completed submission | Exclude from same offer, upsell |

### Video Viewing Audiences
| Segment | Definition | Use Case |
|---------|-----------|----------|
| 25% Viewers | Watched 25%+ | Mild interest, MOFU retarget |
| 50% Viewers | Watched 50%+ | Moderate interest |
| 75% Viewers | Watched 75%+ | High interest, BOFU retarget |
| Completers | Watched 97%+ | Highest intent |

### Company Page Audiences
- Page visitors (30/60/90/180/365 days)
- Followers
- Non-followers who visited

## Audience Expansion Settings

### What Audience Expansion Does
When enabled, LinkedIn automatically expands your targeting to include members similar to your defined audience, even if they do not match your targeting criteria exactly.

### Expansion Recommendations

| Campaign Type | Expansion Setting | Rationale |
|--------------|-------------------|-----------|
| TOFU Awareness | ON | Maximize reach at low cost |
| MOFU Content | OFF | Maintain targeting precision |
| BOFU Lead Gen | OFF (always) | Never dilute BOFU quality |
| Retargeting | OFF (always) | Retargeting IS your audience |
| ABM | OFF (always) | Named accounts only |

**Warning:** Audience Expansion is ON by default for new campaigns. Always check and turn OFF for MOFU/BOFU campaigns.

## Audit Checklist

1. **Website Retargeting Setup** (3 pts)
   - Are retargeting segments created with multiple time windows?
   - Is the Insight Tag firing on all relevant pages?
   - Are high-intent pages (pricing, demo, contact) segmented separately?

2. **Contact List Strategy** (3 pts)
   - Are customer, prospect, and exclusion lists uploaded and current (<30 days)?
   - Is match rate above 60% for email lists and 70% for company lists?
   - Are lists segmented by funnel stage or intent level?

3. **Lookalike Audiences** (2 pts)
   - Are lookalikes built from high-quality seed audiences (customers, not all leads)?
   - Are lookalikes used appropriately (TOFU/MOFU only, not BOFU)?

4. **Engagement Audiences** (1 pt)
   - Are video viewers, LGF openers, and event attendees being retargeted?

5. **Expansion Settings** (1 pt)
   - Is Audience Expansion OFF for all MOFU, BOFU, retargeting, and ABM campaigns?

## Scoring

| Score | Rating | Meaning |
|-------|--------|---------|
| 9-10 | Elite | Full retargeting setup, fresh lists, smart lookalikes |
| 7-8 | Strong | Good audience setup with minor gaps |
| 5-6 | Average | Basic retargeting, stale lists |
| 3-4 | Weak | Minimal matched audiences |
| 0-2 | Critical | No matched audiences configured |

## Common Audience Building Mistakes

1. **No retargeting** -- running only cold prospecting without retargeting warm visitors
2. **Stale contact lists** -- lists uploaded 6+ months ago with churned contacts
3. **Lookalike from all leads** -- seed audience should be best customers, not every lead
4. **Audience Expansion on BOFU** -- dilutes targeting quality for conversion-focused campaigns
5. **No converter exclusion** -- existing customers seeing acquisition ads wastes budget
6. **Single retargeting window** -- only using 30-day visitors misses people who visited 45 days ago
7. **Not using LGF openers** -- people who opened but did not submit are prime retargeting targets
8. **Ignoring video audiences** -- 75%+ video viewers have high intent but are rarely retargeted
