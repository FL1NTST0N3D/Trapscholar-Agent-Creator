---
name: pmax-url-expansion
description: "Analyze Performance Max URL expansion settings, final URL configuration, URL exclusion rules, page feed setup, and search themes. Ensures PMax traffic lands on the right pages."
allowed-tools:
  - Bash
  - Read
  - Grep
---

# PMax URL Expansion Skill

## Purpose

URL expansion is one of PMax's most misunderstood features. When enabled (the default), PMax can send traffic to ANY page on your website — not just the final URL you specified. This is powerful for discovery but dangerous if your site has pages that shouldn't receive paid traffic (blog posts, career pages, terms of service, etc.). This skill audits your URL expansion configuration to prevent wasted spend on irrelevant landing pages.

## Trigger

Activated by `/pmax urls` or as part of `/pmax audit`.

## Data Requirements

Ask the user for:
1. Final URL expansion setting (on/off) per asset group
2. URL exclusion list (if any)
3. Page feed configuration (if using)
4. Search themes configured per asset group
5. Website sitemap or page structure overview
6. Landing page performance data (bounce rate, conversion rate by page)

## Final URL Expansion — Deep Analysis

### What It Does
When Final URL Expansion is **ON** (default):
- PMax replaces your specified final URL with any URL on your domain
- Google's AI selects the "most relevant" landing page for each search/signal
- Your ad's headlines and descriptions may be dynamically generated to match the selected page
- You lose direct control over where paid traffic lands

### When to Keep It ON
- **E-commerce with large product catalog**: PMax can match users to specific product pages
- **Content-rich sites with good conversion paths**: Blog → product funnel works well
- **New campaigns needing discovery**: Let PMax find which pages convert best
- **Sites where ALL pages are relevant**: Every page has a conversion path

### When to Turn It OFF
- **Lead generation with single landing page**: You want all traffic on your optimized LP
- **Sites with irrelevant pages**: Blog posts, career pages, investor relations
- **Strict compliance requirements**: Financial services, healthcare, legal
- **Brand safety concerns**: Pages with user-generated content, forums
- **Small sites with 1-5 pages**: URL expansion adds no value

### Red Flags with URL Expansion ON
1. **High bounce rate pages receiving PMax traffic** — Pages not designed for paid traffic
2. **Non-converting pages in landing page report** — Blog posts, about pages getting clicks
3. **Career/jobs pages receiving ad traffic** — Common issue, wastes budget
4. **Old/archived content pages** — Outdated information getting promoted
5. **Duplicate content pages** — URL parameters creating multiple versions
6. **Login/account pages** — Existing customers landing on auth pages

## URL Exclusion Rules

When URL expansion is ON, exclusions are your safety net. Audit these carefully.

### Must-Exclude Pages
Every PMax campaign with URL expansion ON should exclude:
- `/careers`, `/jobs`, `/hiring` — Career/recruitment pages
- `/login`, `/account`, `/dashboard` — Authenticated pages
- `/terms`, `/privacy`, `/legal` — Legal pages
- `/sitemap`, `/robots.txt` — Technical pages
- `/cart`, `/checkout` — Transaction pages (user should arrive via product page)
- `/unsubscribe`, `/opt-out` — Email management pages
- `/404`, `/error` — Error pages
- `/admin`, `/wp-admin` — Admin pages
- `/tag/*`, `/category/*` — Taxonomy pages (usually thin content)
- `/author/*` — Author archive pages

### Conditional Exclusions
Consider excluding based on account type:
- **Lead gen**: Exclude all blog/content pages (or test separately)
- **E-commerce**: Exclude out-of-stock product pages
- **SaaS**: Exclude documentation/help pages
- **Local services**: Exclude service area pages outside target geo

### Exclusion Format
```
URL contains: /careers
URL contains: /login
URL contains: /terms
URL exact: https://example.com/old-promo
URL regex: /blog/20(1[0-9]|2[0-3])/ (old blog posts)
```

### Common Exclusion Mistakes
1. **No exclusions at all** — Guaranteed budget waste on irrelevant pages
2. **Too many exclusions** — Defeats the purpose of URL expansion; consider turning it off
3. **Excluding high-converting pages accidentally** — Test before excluding
4. **Not excluding URL parameters** — `/product?color=red` and `/product` are different URLs
5. **Forgetting subdomains** — `blog.example.com` may not be covered by `example.com` exclusions

## Page Feed Setup

Page feeds give you a middle ground between full URL expansion and no expansion.

### What Is a Page Feed?
A spreadsheet of URLs you upload to Google Ads that defines which pages PMax can use. Only pages in the feed are eligible for URL expansion.

### When to Use Page Feeds
- **Large e-commerce sites**: Feed your product pages but exclude blog/support
- **Multi-location businesses**: Feed location-specific landing pages
- **Service businesses**: Feed individual service pages
- **Content sites**: Feed only high-converting content pages

### Page Feed Best Practices
- **Include**: Product pages, service pages, high-converting landing pages
- **Exclude**: Blog posts (unless proven converters), support pages, thin content
- **Format**: CSV with columns: Page URL, Custom Label (optional)
- **Update frequency**: Weekly for e-commerce (product availability), monthly for services
- **Custom labels**: Use to segment pages by category, priority, or test group

### Page Feed Audit Checklist
- [ ] Feed contains only relevant, converting pages
- [ ] No 404/redirect URLs in feed
- [ ] No duplicate URLs (with/without trailing slash, www vs non-www)
- [ ] Feed updated within last 30 days
- [ ] All URLs have proper tracking parameters
- [ ] Custom labels used for segmentation
- [ ] Feed covers all key product/service categories

## Search Themes

Search themes (introduced 2023) give you additional control over PMax's search matching.

### What Are Search Themes?
Keywords you add to an asset group to tell PMax what searches are relevant to that group. Similar to keywords in Search campaigns but function as signals, not strict matching.

### Search Theme Specifications
- **Maximum**: 25 search themes per asset group
- **Format**: Short phrases (similar to broad match keywords)
- **Match behavior**: Broad — PMax uses these as guidance, not restrictions

### Search Theme Best Practices
- **Use 10-25 themes per asset group** — Provide enough guidance without over-constraining
- **Include your top Search campaign keywords** — Reinforce what you know works
- **Add discovery terms** — Terms you don't bid on in Search but are relevant
- **Segment by asset group** — Different themes for different product/service groups
- **Review quarterly** — Update based on Search Terms report insights
- **Don't duplicate across asset groups** — Each group should have unique themes

### Search Theme Audit Checklist
- [ ] Search themes configured (not left blank)
- [ ] 10-25 themes per asset group
- [ ] Themes are specific and relevant (not overly broad)
- [ ] No duplicate themes across asset groups
- [ ] Themes align with the asset group's intended audience
- [ ] Updated within last 90 days

## Scoring Rubric (0-100)

### URL Expansion Configuration (0-40 points)

| Criteria | Points |
|---|---|
| URL expansion setting is intentional (not just default) | 10 |
| Setting matches account type (on for e-commerce, off for lead gen LP) | 15 |
| Landing page report reviewed for irrelevant pages | 10 |
| No high-bounce/non-converting pages receiving significant traffic | 5 |

### URL Exclusions (0-25 points)

| Criteria | Points |
|---|---|
| Exclusion list exists (if expansion is on) | 10 |
| Must-exclude pages are excluded (careers, login, legal) | 8 |
| No accidental exclusion of converting pages | 4 |
| Exclusions reviewed and updated within 90 days | 3 |

### Page Feed (0-15 points)

| Criteria | Points |
|---|---|
| Page feed configured (if applicable) | 5 |
| Feed contains only relevant, active pages | 5 |
| Feed updated within last 30 days | 3 |
| Custom labels used for segmentation | 2 |

### Search Themes (0-20 points)

| Criteria | Points |
|---|---|
| Search themes configured per asset group | 8 |
| 10-25 themes per asset group | 5 |
| Themes are specific and relevant | 4 |
| No duplicate themes across asset groups | 3 |

## Output Format

```
## URL Expansion Audit Results

### URL & Search Theme Score: XX/100

### Configuration Overview
| Setting | Value | Recommendation | Status |
|---|---|---|---|
| URL Expansion | ON/OFF | [Recommendation] | OK/WARNING/CRITICAL |
| URL Exclusions | X rules | [Recommendation] | OK/WARNING/CRITICAL |
| Page Feed | Yes/No | [Recommendation] | OK/WARNING |
| Search Themes | X themes/group | [Recommendation] | OK/WARNING |

### URL Expansion Analysis
- Setting appropriate for account type: YES/NO
- Irrelevant pages receiving traffic: [list if any]
- Estimated wasted spend on wrong pages: $X/month

### Exclusion Audit
- Missing critical exclusions: [list]
- Unnecessary exclusions: [list]
- Recommended additions: [list]

### Search Theme Review
- Coverage: X/Y asset groups have themes configured
- Average themes per group: X
- Duplicate themes found: [list]

### Critical Issues
- [List findings]

### Recommendations
1. [Prioritized action items]
```
