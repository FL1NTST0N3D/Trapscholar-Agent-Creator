# Lead Gen Forms Sub-Skill

## Purpose

Audit and optimize LinkedIn Lead Gen Forms (LGFs) for maximum form completion rate and lead quality. Evaluate field selection, pre-fill utilization, CTA configuration, post-submission experience, and hidden field tracking.

## LinkedIn Lead Gen Forms Overview

Lead Gen Forms are native LinkedIn forms that appear in-feed without redirecting users to a landing page. Because fields are pre-filled from LinkedIn profile data, they dramatically reduce friction and increase completion rates.

**Key Stats:**
- Average form completion rate: 13% (all forms)
- Document Ads + LGF completion rate: 22.73%
- Pre-filled fields complete 5x faster than manual entry
- LGF CPL is typically 30-50% lower than landing page CPL
- LinkedIn keeps lead data for 90 days (download or CRM sync before expiration)

## Field Selection Strategy

### Available Field Types

**Pre-Fillable Fields (Recommended -- highest completion rates):**
| Field | Auto-Filled From | Recommended? |
|-------|-----------------|-------------|
| First Name | Profile | Always include |
| Last Name | Profile | Always include |
| Email Address | Profile (work email) | Always include |
| Phone Number | Profile | Use sparingly |
| Job Title | Profile | High value, include |
| Company Name | Profile | High value, include |
| Company Size | Profile | Good for qualification |
| Seniority | Profile | Good for qualification |
| Industry | Profile | Situational |
| Work Phone | Profile | Rarely available |

**Custom Questions (Manual Entry -- increases friction):**
| Type | Use Case | Impact on Completion |
|------|----------|---------------------|
| Single-line text | Budget, timeline, specific need | -5-10% per field |
| Single select dropdown | Product interest, company stage | -3-5% per field |
| Multiple select checkboxes | Topics of interest, pain points | -3-5% per field |
| Hidden fields | UTM tracking, campaign ID | No impact (invisible) |

### The 3-4 Field Rule

**Optimal form: 3-4 fields total**
- 3 fields: ~15-20% completion rate
- 4 fields: ~12-17% completion rate
- 5 fields: ~9-13% completion rate
- 6+ fields: ~5-8% completion rate (avoid)

**Recommended Default Form:**
1. First Name (pre-filled)
2. Last Name (pre-filled)
3. Work Email (pre-filled)
4. Company Name (pre-filled)

**Enhanced Qualification Form (5 fields max):**
1. First Name (pre-filled)
2. Work Email (pre-filled)
3. Company Name (pre-filled)
4. Company Size (pre-filled)
5. "What is your primary challenge?" (single select dropdown)

### Lead Quality vs Volume Trade-off

| Strategy | Fields | Completion Rate | Lead Quality | Best For |
|----------|--------|----------------|-------------|----------|
| Maximum Volume | 3 (name + email) | 18-22% | Lower | TOFU content downloads |
| Balanced | 4-5 (+ company + title) | 12-17% | Medium | MOFU gated content |
| Maximum Quality | 5-6 (+ custom questions) | 7-12% | Higher | BOFU demo requests |

## CTA Button Selection

LinkedIn offers these CTA button options for Lead Gen Forms:

| CTA Text | Best For | Expected Impact |
|----------|----------|----------------|
| Sign Up | Newsletter, webinar registration | High volume |
| Subscribe | Ongoing content series | Medium volume |
| Download | Whitepapers, ebooks, guides | Highest completion for content |
| Get Quote | Pricing, custom solutions | Lower volume, higher intent |
| Learn More | General information requests | Medium volume |
| Apply Now | Job-related or program enrollment | Contextual |
| Register | Events, webinars, conferences | High volume |
| Request Demo | Product demonstrations | Lowest volume, highest intent |

**CTA Selection Rule:** Match CTA to the offer. "Download" for content, "Request Demo" for BOFU, "Register" for events. Mismatched CTAs reduce trust and completion.

## Post-Submission Experience

### Thank-You Page Configuration

The thank-you page is your immediate next-step opportunity. Configure it correctly:

1. **Thank You Message** (required, 300 char max)
   - Confirm what they will receive
   - Set expectation for next contact
   - Example: "Thanks! Your guide is ready to download. Our team will reach out within 24 hours to discuss how we can help."

2. **Landing Page URL** (required)
   - Link to the actual content asset (PDF, webinar replay, etc.)
   - Do NOT link to your homepage -- deliver the promised content
   - Use a tracked URL (UTM parameters)

3. **CTA Button Text** on thank-you page
   - "Download Now" for content offers
   - "Visit Website" for awareness campaigns
   - "View Schedule" for event registration

### Post-Submission Workflow

After form submission, leads should flow into your CRM within minutes:
1. **CRM Integration**: Use native LinkedIn integration (Salesforce, HubSpot, Marketo, Microsoft Dynamics) or Zapier/webhook
2. **Lead Routing**: Auto-assign leads based on company size, geography, or product interest
3. **Speed to Lead**: Contact within 5 minutes for BOFU leads (demo requests)
4. **Nurture Sequence**: Enroll TOFU/MOFU leads in email nurture within 1 hour

## Hidden Fields for Tracking

Hidden fields are invisible to the user but captured with every submission. Essential for attribution:

**Recommended Hidden Fields:**
| Field Name | Value | Purpose |
|------------|-------|---------|
| utm_source | linkedin | Channel attribution |
| utm_medium | paid_social | Medium tracking |
| utm_campaign | {campaign_name} | Campaign-level attribution |
| utm_content | {ad_name} | Ad-level attribution |
| li_campaign_id | {campaign_id} | LinkedIn campaign ID |
| li_form_id | {form_id} | Form-level tracking |
| funnel_stage | tofu/mofu/bofu | Funnel position |

## LGF vs Landing Page Decision Framework

| Factor | Lead Gen Form | Landing Page |
|--------|--------------|--------------|
| CPL | 30-50% lower | Higher |
| Completion Rate | 13-23% | 2-5% |
| Lead Quality | Lower (easy to submit) | Higher (more friction = more intent) |
| Content Delivery | Limited (thank-you page link) | Full page experience |
| Tracking | LinkedIn-native | Full analytics (GA4, heatmaps) |
| Personalization | Template-based | Fully customizable |
| Retargeting | LGF openers audience | Website visitor audience |
| CRM Integration | Native or Zapier | Form tool integration |
| A/B Testing | Limited (form vs form) | Full (page elements, layout) |

**Use LGF When:**
- CPL is the primary KPI
- Offer is simple (content download, webinar registration)
- You want maximum lead volume
- Your landing page has low conversion rate (<3%)

**Use Landing Page When:**
- Lead quality is the primary KPI
- Offer requires explanation (complex product, custom pricing)
- You need full analytics and heatmap data
- You want to retarget website visitors across all channels

## Audit Checklist

1. **Field Count & Selection** (4 pts)
   - Are forms using 3-5 fields (not 6+)?
   - Are pre-fillable fields prioritized over custom questions?
   - Is Work Email always included?
   - Are qualification fields appropriate for the funnel stage?

2. **Pre-Fill Utilization** (3 pts)
   - Are all available pre-fill fields being used?
   - Is the form not asking for information LinkedIn already has?
   - Are custom questions truly necessary and well-designed?

3. **CTA & Thank-You Page** (4 pts)
   - Does the CTA button match the offer?
   - Does the thank-you message confirm delivery and set expectations?
   - Does the landing page URL deliver the promised content?
   - Is the thank-you page URL tracked (UTMs)?

4. **Hidden Fields & Tracking** (4 pts)
   - Are hidden fields configured for UTM tracking?
   - Is campaign/ad-level attribution possible from form data?
   - Are leads flowing to CRM within minutes?
   - Is there a speed-to-lead process for BOFU submissions?

## Scoring

| Score | Rating | Meaning |
|-------|--------|---------|
| 13-15 | Elite | Optimized forms with full tracking and fast CRM flow |
| 10-12 | Strong | Good forms, minor tracking or CTA gaps |
| 7-9 | Average | Too many fields or missing hidden field tracking |
| 4-6 | Weak | Poor field selection, no post-submission workflow |
| 0-3 | Critical | No Lead Gen Forms or broken configuration |

## Common LGF Mistakes

1. **Too many fields** -- every field above 4 drops completion rate 3-5 percentage points
2. **Asking for information LinkedIn has** -- do not ask for job title in a text field when it is pre-fillable
3. **Generic thank-you page** -- linking to homepage instead of delivering the content asset
4. **No CRM integration** -- manually downloading CSV leads days after submission, destroying speed-to-lead
5. **No hidden fields** -- impossible to attribute leads to specific campaigns or ads
6. **Same form for all funnel stages** -- TOFU should have fewer fields than BOFU
7. **Not using Document Ads + LGF combo** -- this combination delivers the highest form completion rate (22.73%)
8. **Ignoring LGF openers audience** -- people who opened but did not submit are warm retargeting candidates
