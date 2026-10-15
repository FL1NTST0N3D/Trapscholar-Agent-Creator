# QS Landing Page Experience Analysis

## Command
`/qs landing-pages`

## Purpose

Analyze the Landing Page Experience component of Quality Score across all keywords. Identify which landing pages are dragging down QS, diagnose the specific issues (speed, mobile, content, navigation, trust), and produce a prioritized fix plan that improves QS for the maximum number of keywords with the minimum number of page changes.

## Landing Page Experience Factors

Google evaluates landing page experience based on six primary factors. Each factor contributes to the overall Above Average / Average / Below Average rating:

### 1. Page Speed (Critical)

**Target: Largest Contentful Paint (LCP) < 2.5 seconds**

Page speed is the most measurable and often the most impactful factor. Google has explicitly stated that page speed affects Quality Score, and their Core Web Vitals framework provides clear benchmarks.

| Metric | Good | Needs Improvement | Poor |
|:--|:--:|:--:|:--:|
| LCP (Largest Contentful Paint) | < 2.5s | 2.5s - 4.0s | > 4.0s |
| FID (First Input Delay) | < 100ms | 100ms - 300ms | > 300ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.1 - 0.25 | > 0.25 |
| TTFB (Time to First Byte) | < 200ms | 200ms - 500ms | > 500ms |

**Common speed killers:**
- Unoptimized images (not using WebP/AVIF, no lazy loading)
- Render-blocking JavaScript and CSS
- No CDN (Content Delivery Network)
- Slow server response time (cheap hosting)
- Too many third-party scripts (chat widgets, analytics, pixel overload)
- No browser caching headers
- Uncompressed resources (no gzip/brotli)

### 2. Mobile Responsiveness (Critical)

**Target: Full functionality on all screen sizes, touch-friendly elements**

With 60%+ of Google searches on mobile, landing page experience on mobile devices is weighted heavily. Google uses mobile-first indexing, and your landing page must work flawlessly on phones.

**What Google checks:**
- Viewport meta tag configured correctly
- Text readable without pinch-zoom (minimum 16px font)
- Tap targets adequately sized and spaced (minimum 48x48px)
- No horizontal scrolling required
- Forms are mobile-friendly (appropriate input types, autocomplete)
- Content not wider than screen
- No Flash or unsupported technologies

### 3. Content Relevance (High Impact)

**Target: Landing page content directly addresses the keyword's intent**

The landing page must deliver on the promise of the ad. If the keyword is "emergency plumber," the landing page should be about emergency plumbing services, not a general homepage or a page about bathroom remodeling.

**What Google evaluates:**
- Keyword (or close variants) present in page heading (H1)
- Keyword theme reflected in body content
- Content depth (substantive information, not just a form)
- Unique content (not duplicated from other pages on your site or other sites)
- Content matches the specific intent (informational, transactional, navigational)

**Red flags:**
- Sending all keywords to the homepage
- Landing page content does not mention the keyword or its topic
- Thin pages with just a form and no supporting content
- Exact duplicate content across multiple landing pages (only URL changes)

### 4. Easy Navigation (Medium Impact)

**Target: Clear path to desired action, no dead ends, logical page structure**

Users who click an ad should immediately understand where they are and what to do next. Navigation should not be confusing, and the page should not trap users.

**What Google evaluates:**
- Clear call-to-action (CTA) above the fold
- Logical page structure (heading hierarchy, sections)
- Working internal links
- Back button works as expected (no redirect traps)
- No excessive pop-ups or interstitials blocking content
- Search functionality available on content-heavy sites
- Breadcrumbs or clear navigation path

### 5. Transparent Business Information (Medium Impact)

**Target: Users can easily verify the business is legitimate and trustworthy**

Google rewards pages that help users trust the business. This is especially important for industries where trust matters: healthcare, legal, financial services, e-commerce.

**What Google evaluates:**
- Contact information easily findable (phone, email, address)
- About page with real business information
- Privacy policy present and linked
- Terms of service present
- Physical address for local businesses
- Business registration or licensing info where applicable
- Customer reviews or testimonials
- SSL certificate (HTTPS)

### 6. Original Content (Medium Impact)

**Target: Unique, substantive content that provides genuine value**

Google penalizes landing pages that are thin, duplicated, or scraped from other sources. The page should provide information that helps the user make a decision.

**What makes content "original":**
- Written specifically for your audience (not generic template text)
- Provides information not easily found elsewhere
- Includes proprietary data, case studies, or original research
- Has sufficient depth (not just a headline and a form)
- Updated regularly (not stale content from 2019)

## Analysis Methodology

### Step 1: Map Keywords to Landing Pages

Create a mapping of all keywords to their final URLs. Group keywords by landing page:

```
Landing Page Inventory
=======================
/services/plumbing     → 45 keywords | Avg QS: 4.2 | LP Status: 38 Below Avg, 7 Avg
/services/hvac         → 28 keywords | Avg QS: 6.1 | LP Status: 12 Below Avg, 16 Avg
/contact               → 12 keywords | Avg QS: 3.8 | LP Status: 12 Below Avg
/homepage              → 8 keywords  | Avg QS: 4.0 | LP Status: 6 Below Avg, 2 Avg
/services/electrical   → 22 keywords | Avg QS: 7.2 | LP Status: 2 Avg, 20 Above Avg
```

### Step 2: Prioritize by Impact

Rank landing pages by: number of keywords affected multiplied by average QS gap multiplied by total spend on those keywords.

### Step 3: Diagnose Each Landing Page

For each priority landing page, run through the six factors checklist. Use available tools:
- PageSpeed Insights (speed metrics)
- Mobile-Friendly Test
- Manual content review
- Trust signal inventory

### Step 4: Produce Fix Plan

For each landing page, produce specific, actionable fixes:

```
Landing Page: /services/plumbing
Keywords affected: 45
Monthly spend: $12,400
Current avg QS: 4.2 → Target: 7.0
Estimated monthly savings: $5,200

Issues Found:
1. [CRITICAL] LCP = 5.2s (target: < 2.5s)
   Fix: Compress hero image, defer non-critical JS, enable CDN
   Effort: Low | Timeline: 1-2 days

2. [HIGH] No mobile responsiveness below 480px
   Fix: Add responsive breakpoints, fix tap target sizes
   Effort: Medium | Timeline: 3-5 days

3. [MEDIUM] Content does not mention "plumbing" until paragraph 3
   Fix: Rewrite H1 and intro paragraph to lead with plumbing services
   Effort: Low | Timeline: 1 day

4. [LOW] No customer reviews on page
   Fix: Add 3-5 Google review snippets with schema markup
   Effort: Low | Timeline: 1 day
```

## Special Cases

### Single Landing Page Accounts
Some accounts send all traffic to one page. This creates a ceiling on Landing Page Experience because the page cannot be relevant to all keywords. Recommendation: create 3-5 dedicated landing pages for top keyword themes.

### Dynamic Landing Pages
Accounts using dynamic content (e.g., location insertion, keyword insertion) may show inconsistent Landing Page Experience ratings. Analyze by keyword theme, not just URL.

### Redirect Chains
Landing pages with multiple redirects (301 → 302 → final URL) add latency and can confuse Google's crawler. Ensure final URLs are direct with no redirect chains.

## Output Format

1. **Landing Page Health Summary** — Table of all landing pages with keyword count, avg QS, and LP Experience distribution
2. **Priority Ranking** — Landing pages sorted by total monthly waste
3. **Per-Page Diagnosis** — Six-factor checklist for each priority page
4. **Fix Plan** — Specific actions per page with effort level and timeline
5. **Estimated Impact** — Monthly savings if landing page fixes achieve target QS
