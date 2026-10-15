# Skill: Tech Stack Detection (`/comp tech`)

## Purpose
Identify and analyze the technology stack a competitor uses across their web presence, marketing operations, and product infrastructure. Technology choices reveal a company's maturity level, engineering philosophy, operational investment, and strategic priorities. A company running Salesforce Enterprise with Marketo signals very different things than one running HubSpot Free with Mailchimp. Tech stack intelligence informs competitive positioning, integration strategy, and even hiring and partnership decisions.

## When to Use
- Building integrations and need to know what competitors connect with
- Evaluating a competitor's operational maturity and investment level
- Identifying potential technology-driven competitive advantages or limitations
- Preparing for technical sales conversations where buyer's existing stack matters
- Assessing whether a competitor can rapidly build certain capabilities based on their stack
- Understanding hiring priorities based on technology choices

## Framework: Technology Stack Audit

### Category 1: Website & CMS
Detect the content management and web infrastructure:
- **CMS**: WordPress, Webflow, Contentful, Ghost, Sanity, custom-built
- **Static Site Generator**: Next.js, Gatsby, Hugo, Astro, Nuxt
- **Hosting/CDN**: Vercel, Netlify, Cloudflare, AWS CloudFront, Fastly, Akamai
- **Domain Registrar**: GoDaddy, Namecheap, Cloudflare, Google Domains
- **SSL Certificate**: Let's Encrypt, DigiCert, Cloudflare, Comodo

**Detection Methods:**
- HTTP response headers (`X-Powered-By`, `Server`, `Via`)
- HTML source inspection (`meta generator`, framework-specific patterns)
- JavaScript file names and paths (e.g., `/_next/`, `/wp-content/`, `/webflow.js`)
- Cookie names and patterns (e.g., `wp-settings-*`, `__cf_bm`)
- DNS records (CNAME, A records pointing to hosting providers)
- robots.txt and sitemap.xml patterns

### Category 2: Analytics & Tracking
- **Web Analytics**: Google Analytics (GA4/UA), Adobe Analytics, Mixpanel, Amplitude, Plausible, Fathom
- **Tag Management**: Google Tag Manager, Tealium, Segment, Adobe Launch
- **Heatmaps/Session Recording**: Hotjar, Microsoft Clarity, FullStory, LogRocket
- **A/B Testing**: Optimizely, VWO, Google Optimize, LaunchDarkly, Split.io
- **Attribution**: Triple Whale, Northbeam, Rockerbox, AppsFlyer

**Detection Methods:**
- Script tags in HTML source (`gtag`, `gtm`, `analytics.js`, `mixpanel`, `amplitude`)
- Network requests to tracking domains
- Cookie patterns associated with tracking tools
- Data layer objects (`dataLayer`, `analytics`, custom event objects)

### Category 3: Marketing Automation & CRM
- **CRM**: Salesforce, HubSpot, Pipedrive, Close, Zoho
- **Marketing Automation**: Marketo, Pardot, HubSpot, ActiveCampaign, Klaviyo
- **Email Service**: SendGrid, Mailgun, Amazon SES, Postmark
- **Chat/Messaging**: Intercom, Drift, Zendesk Chat, Crisp, Freshchat
- **Forms**: Typeform, JotForm, native CRM forms, custom forms
- **Scheduling**: Calendly, Chili Piper, HubSpot Meetings, SavvyCal

**Detection Methods:**
- Script tags and embedded widgets
- Form action URLs and hidden fields (e.g., HubSpot form IDs, Marketo munchkin)
- Chat widget scripts and DOM elements
- Email header analysis (SPF, DKIM records reveal sending infrastructure)
- Tracking parameters in URLs (`utm_`, `hsa_`, custom params)

### Category 4: Advertising Platforms
- **Search**: Google Ads, Microsoft Ads, Apple Search Ads
- **Social**: Meta Ads, LinkedIn Ads, Twitter/X Ads, TikTok Ads, Pinterest Ads
- **Display/Programmatic**: Google Display Network, The Trade Desk, Criteo, AdRoll
- **Retargeting**: Google Remarketing, Meta Pixel, LinkedIn Insight Tag, AdRoll
- **Affiliate**: Impact, ShareASale, CJ Affiliate, PartnerStack

**Detection Methods:**
- Pixel and tracking scripts (Meta Pixel `fbq`, LinkedIn `_linkedin_data`, Google Ads `gtag`)
- Conversion tracking snippets in page source
- Ad tag parameters on landing pages
- Third-party cookie domains in network requests

### Category 5: Product & Application Stack
- **Frontend Framework**: React, Vue, Angular, Svelte, vanilla JS
- **Backend Signals**: API endpoint patterns, error pages, response headers
- **Database Signals**: Query parameter patterns, pagination styles
- **Authentication**: Auth0, Okta, Firebase Auth, custom
- **Payments**: Stripe, Braintree, PayPal, Chargebee, Recurly
- **Infrastructure**: AWS, GCP, Azure (from DNS, IPs, error pages)

**Detection Methods:**
- JavaScript framework detection (React devtools patterns, Vue signature, Angular modules)
- API endpoint URL patterns (`/api/v1/`, `/graphql`, REST vs GraphQL)
- Payment form inspection (Stripe.js elements, Braintree drop-in)
- Cloud provider IP ranges and DNS patterns
- Error page signatures

### Category 6: Developer & Engineering Tools
- **Source Control**: GitHub, GitLab, Bitbucket (from job postings, public repos)
- **CI/CD**: GitHub Actions, CircleCI, Jenkins, GitLab CI (from job postings)
- **Monitoring**: Datadog, New Relic, Sentry, PagerDuty, Grafana
- **Feature Flags**: LaunchDarkly, Split.io, Flagsmith, custom
- **Documentation**: GitBook, ReadMe, Docusaurus, Mintlify

**Detection Methods:**
- Job postings (most reliable for internal tooling)
- Public GitHub organization activity
- Error tracking scripts (Sentry DSN, Bugsnag API keys)
- Status page technology (Statuspage.io, Better Uptime, Instatus)
- Documentation site technology

## Output Template

```markdown
# Tech Stack Analysis: [Competitor Name]
**Date**: [YYYY-MM-DD]
**Domain**: [URL]
**Detection Methods**: [BuiltWith, manual inspection, job postings, etc.]

## Executive Summary
- [Overall technology maturity assessment: Early-Stage / Growth / Enterprise-Grade]
- [Key technology advantage or limitation identified]
- [Integration or compatibility insight for your strategy]

## Technology Stack

### Website & Infrastructure
| Category | Technology | Confidence | Evidence |
|----------|-----------|------------|---------|
| CMS | | Confirmed/Likely/Possible | |
| Hosting | | | |
| CDN | | | |

### Analytics & Tracking
| Category | Technology | Confidence | Evidence |
|----------|-----------|------------|---------|

### Marketing & CRM
| Category | Technology | Confidence | Evidence |
|----------|-----------|------------|---------|

### Advertising
| Category | Technology | Confidence | Evidence |
|----------|-----------|------------|---------|

### Product Stack
| Category | Technology | Confidence | Evidence |
|----------|-----------|------------|---------|

### Developer Tools
| Category | Technology | Confidence | Evidence |
|----------|-----------|------------|---------|

## Stack Maturity Assessment
| Dimension | Rating (1-5) | Notes |
|-----------|-------------|-------|
| Marketing Ops Sophistication | | |
| Engineering Maturity | | |
| Data Infrastructure | | |
| Security Posture | | |
| Scalability Readiness | | |

## Strategic Implications
1. [What their stack reveals about their operational investment]
2. [Integration compatibility with your product]
3. [Technology-driven competitive advantage or limitation]

## Hiring Signals
[What their job postings reveal about technology direction]

## Sources
- [BuiltWith report, date]
- [Manual inspection, what was checked]
- [Job postings analyzed, date range]
```

## Best Practices
1. Use multiple detection methods — no single source catches everything. BuiltWith and Wappalyzer are starting points, not complete answers.
2. Job postings are the most reliable signal for internal tooling (databases, CI/CD, monitoring) that is not visible externally.
3. Technology detection has false positives. A tracking script on the page does not mean they actively use that tool. Confirm with multiple signals.
4. Check quarterly — tech stacks evolve as companies grow. A migration from HubSpot to Salesforce signals an important maturity shift.
5. Compare tech sophistication to company stage. An early startup on enterprise tools may be over-investing; a large company on free tools may be under-investing.
6. Map competitor tech choices to your integration strategy — being compatible with the tools your prospects already use reduces switching friction.
