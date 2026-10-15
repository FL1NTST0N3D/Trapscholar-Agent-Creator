---
name: audit-landing-pages
description: Evaluates landing page quality including message match to ads, page load speed, mobile responsiveness, CTA visibility, form field analysis, trust signals, social proof, keyword-intent relevance, and conversion path clarity.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Landing Page Audit

## Overview

The landing page is where clicks become conversions — or bounce. Google Ads can deliver the most perfectly targeted traffic, but if the landing page fails, the entire investment is wasted. Landing page quality also directly impacts Quality Score (Landing Page Experience component), which affects CPC and ad position.

**The conversion equation:** Conversion Rate = f(Traffic Relevance x Landing Page Quality x Offer Strength). Even perfect traffic converts at 0% on a bad landing page.

**Google's Landing Page Experience factors:**
- Relevant, useful, and original content
- Easy navigation and transparent business practices
- Fast load speed (especially mobile)
- Mobile-friendly design
- Matching the promise of the ad

## Audit Checks (15 Total)

### Message Match (3 checks)

**Check 1: Ad Headline to Landing Page Headline Match**
- Pass: The primary headline on the landing page reflects or directly matches the ad headline the user clicked; the user immediately sees relevance
- Fail: Landing page headline is generic ("Welcome to Our Site") or doesn't match the ad's promise
- Scoring: 10 points
- Benchmark: Message match can improve conversion rates by 30-50%
- Method: Compare the top 3 ad headlines (by impression share) to the landing page H1 for each ad group. They should share key terms and intent alignment.
- Example (Good): Ad: "Custom Kitchen Cabinets — Free Design Consultation" → LP H1: "Get Your Free Custom Kitchen Design Consultation"
- Example (Bad): Ad: "Custom Kitchen Cabinets — Free Design Consultation" → LP H1: "Welcome to ABC Home Improvements"

**Check 2: Ad Description to Landing Page Body Match**
- Pass: Key promises in ad descriptions are substantiated on the landing page (pricing, offers, features, benefits mentioned in ad copy)
- Fail: Ad promises not reflected on landing page (bait-and-switch or inconsistency)
- Scoring: 5 points

**Check 3: Keyword Intent to Page Content Match**
- Pass: Landing page content directly addresses the search intent behind the triggering keywords (informational intent gets info, transactional intent gets action)
- Fail: Mismatched intent (e.g., transactional keyword "buy X" lands on a blog post; informational "how to X" lands on pricing page)
- Scoring: 5 points

### Page Performance (3 checks)

**Check 4: Page Load Speed (Mobile)**
- Pass: Mobile page loads in under 3 seconds (LCP - Largest Contentful Paint)
- Fail: Mobile load time > 5 seconds
- Scoring: 8 points
- Benchmark: Every 1-second delay in mobile page load reduces conversions by 7-20% (Google data)
  - < 2s: Excellent
  - 2-3s: Good
  - 3-5s: Below average (losing conversions)
  - > 5s: Poor (losing 30%+ of mobile visitors)
- Measurement: Google PageSpeed Insights, GTmetrix, Lighthouse, WebPageTest
- Key metrics: LCP < 2.5s, FID < 100ms, CLS < 0.1 (Core Web Vitals)

**Check 5: Page Load Speed (Desktop)**
- Pass: Desktop page loads in under 2 seconds
- Fail: Desktop load time > 4 seconds
- Scoring: 4 points

**Check 6: Mobile Responsiveness**
- Pass: Page is fully mobile-optimized — readable without zooming, buttons easily tappable (min 44x44px), no horizontal scrolling, forms work on mobile
- Fail: Non-responsive design, tiny text, unusable forms, or horizontal scrolling on mobile
- Scoring: 8 points
- Benchmark: 60%+ of Google Ads clicks come from mobile; non-mobile-optimized pages lose majority of this traffic
- Test: Google's Mobile-Friendly Test tool, Chrome DevTools device emulation

### CTA & Conversion Path (4 checks)

**Check 7: Above-the-Fold CTA Visibility**
- Pass: Primary CTA (button, form, phone number) visible without scrolling on both desktop and mobile
- Fail: CTA buried below the fold, requiring scroll to find the conversion action
- Scoring: 8 points
- Best practice: CTA button should be high-contrast color, action-oriented text ("Get Free Quote" not "Submit"), and visible within the first viewport
- Phone number (if call-driven): Clickable and prominent in mobile view

**Check 8: CTA Clarity & Specificity**
- Pass: CTA button text is specific and value-oriented ("Get My Free Quote" vs "Submit"; "Start 14-Day Free Trial" vs "Sign Up")
- Fail: Generic CTA text ("Submit", "Click Here", "Learn More")
- Scoring: 5 points
- Benchmark: Specific CTAs outperform generic ones by 30-40% in conversion rate

**Check 9: Single Primary Conversion Goal**
- Pass: Page has one clear primary conversion action; no competing CTAs that confuse the user
- Fail: Multiple competing CTAs of equal visual weight (e.g., "Buy Now" next to "Watch Video" next to "Download Guide" — user doesn't know what to do)
- Scoring: 4 points
- Exception: Having a primary CTA + secondary CTA (e.g., "Call Us" as primary + "Request Callback" as secondary) is acceptable if clearly hierarchical

**Check 10: Conversion Path Simplicity**
- Pass: User can convert in 1-2 steps from landing (no unnecessary pages between ad click and conversion action)
- Fail: Multi-step conversion path without clear progress indicators, or unnecessary intermediate pages
- Scoring: 3 points

### Form Analysis (2 checks)

**Check 11: Form Field Count (Lead Gen)**
- Pass: Form has 3-5 fields for lead gen (Name, Email, Phone, and 1-2 qualifying questions)
- Fail: Form has 7+ fields (every additional field reduces conversion rate by ~7-10%)
- Scoring: 7 points
- Benchmarks:
  - 3 fields: ~25% conversion rate (best)
  - 5 fields: ~20% conversion rate
  - 7 fields: ~15% conversion rate
  - 10+ fields: ~10% or lower
- Exception: Higher-intent forms (e.g., mortgage applications, insurance quotes) can justify more fields if qualified leads are valuable enough
- Tip: Use multi-step forms (show 3 fields, then reveal more) to reduce perceived friction

**Check 12: Form Functionality**
- Pass: Form works on all devices, validation is clear (inline errors), submission triggers proper thank-you page/conversion tracking
- Fail: Form broken on mobile, unclear error messages, no form validation, or no confirmation after submission
- Scoring: 4 points

### Trust & Social Proof (3 checks)

**Check 13: Trust Signals Present**
- Pass: Page includes at least 3 trust signals: client logos, certifications, awards, BBB rating, security badges, industry memberships, years in business, number of customers served
- Fail: No trust signals on the page
- Scoring: 5 points
- Impact: Trust signals can improve conversion rates by 15-30%
- Placement: Above the fold or immediately below; near the CTA for maximum impact

**Check 14: Testimonials / Reviews / Social Proof**
- Pass: Customer testimonials, case studies, or third-party reviews (Google Reviews, Trustpilot) displayed prominently
- Fail: No social proof on the landing page
- Scoring: 5 points
- Best practice: Include name, photo, and company (if B2B) for credibility. Star ratings are highly effective. Video testimonials outperform text.
- Numbers as social proof: "10,000+ businesses trust us", "4.8/5 stars from 500+ reviews", "Processing $2B+ annually"

**Check 15: Privacy & Transparency**
- Pass: Privacy policy linked, clear data handling disclosure, no deceptive practices
- Fail: No privacy policy, unclear data usage, or misleading claims
- Scoring: 3 points
- Note: Google requires landing pages to have a privacy policy for lead gen ads; non-compliance can result in ad disapproval

## Scoring Rubric

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| 90-100 | Excellent | High-converting landing pages with strong message match and trust |
| 75-89 | Good | Solid landing pages with specific optimization opportunities |
| 60-74 | Average | Functional pages but significant conversion rate improvements possible |
| 40-59 | Below Average | Landing pages actively hurting conversion rates and QS |
| 0-39 | Poor | Landing pages need complete redesign |

**Total possible points: 84** (normalized to 100-point scale)

## Benchmark Data

| Metric | Excellent | Good | Average | Poor |
|--------|-----------|------|---------|------|
| Message match score | > 90% | 70-90% | 50-70% | < 50% |
| Mobile load speed (LCP) | < 2s | 2-3s | 3-5s | > 5s |
| Landing page CVR (Search) | > 8% | 5-8% | 2-5% | < 2% |
| Landing page CVR (lead gen) | > 15% | 8-15% | 3-8% | < 3% |
| Form fields (lead gen) | 3-4 | 5-6 | 7-8 | 9+ |
| Bounce rate (Search traffic) | < 30% | 30-50% | 50-70% | > 70% |
| Mobile-friendly score | 100/100 | 90-99 | 70-89 | < 70 |

## Output Format

```markdown
## Landing Page Audit Results

**Overall Score: [X]/100 — [Rating]**

### Landing Page Assessment Matrix
| Landing Page URL | Message Match | Load Speed | Mobile | CTA | Form | Trust | Score |
|-----------------|--------------|-----------|--------|-----|------|-------|-------|
| example.com/page1 | Good/Poor | Xs | Pass/Fail | Above fold | X fields | 3/5 signals | X/100 |

### Critical Issues
1. [Pages with message mismatch]
2. [Pages loading > 5 seconds]
3. [Non-mobile-responsive pages]

### Page Speed Details
| URL | Mobile LCP | Desktop LCP | CLS | FID | Mobile Score |
|-----|-----------|------------|-----|-----|-------------|
| ... | ... | ... | ... | ... | ... |

### Form Analysis
| URL | Fields | Multi-step | Mobile Works | Validation | Est. CVR Impact |
|-----|--------|-----------|-------------|-----------|----------------|
| ... | ... | ... | ... | ... | ... |

### Recommendations (Priority Order)
1. [Fix mobile speed for X pages]
2. [Improve message match on Y pages]
3. [Reduce form fields on Z pages]
4. [Add trust signals to W pages]

### Estimated Conversion Rate Improvement: [X-Y]%
```
