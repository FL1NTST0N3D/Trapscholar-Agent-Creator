# AEO Crawlers — AI Crawler Access Verification

## Description

The crawlers sub-skill verifies whether AI-powered search engines can actually access and index your content. Even perfectly optimized content is invisible to AI engines if their crawlers are blocked by robots.txt, IP restrictions, or JavaScript rendering requirements. This skill checks access for 11 known AI crawlers and provides actionable configuration recommendations.

Technical access carries 15% of the total AEO Visibility Score. While it has a lower weight than content-focused dimensions, it is a **binary gate** — if crawlers are blocked, all other optimization is wasted.

## Command

```
/aeo crawlers <url>
```

## AI Crawlers Analyzed

The skill checks access for the following 11 AI crawlers, covering all major AI-powered search engines and LLM training pipelines:

### Tier 1: Critical (block any = major visibility loss)

| Crawler | Operator | Purpose |
|---------|----------|---------|
| **GPTBot** | OpenAI | Crawls content for ChatGPT's browsing feature and training data |
| **ClaudeBot** | Anthropic | Crawls content for Claude's web access capabilities |
| **PerplexityBot** | Perplexity AI | Crawls content for Perplexity's AI search results |
| **Google-Extended** | Google | Controls Gemini/Bard access to your content (separate from Googlebot) |

### Tier 2: Important (blocking reduces visibility)

| Crawler | Operator | Purpose |
|---------|----------|---------|
| **Bingbot** | Microsoft | Crawls for Bing + Copilot AI features |
| **Applebot** | Apple | Crawls for Siri, Apple Intelligence, and Safari AI features |
| **anthropic-ai** | Anthropic | Secondary Anthropic crawler for training data |
| **cohere-ai** | Cohere | Crawls for Cohere's enterprise AI products |

### Tier 3: Contextual (block/allow based on strategy)

| Crawler | Operator | Purpose |
|---------|----------|---------|
| **Bytespider** | ByteDance | Crawls for TikTok and ByteDance AI products |
| **CCBot** | Common Crawl | Open dataset used by many AI training pipelines |
| **Meta-ExternalAgent** | Meta | Crawls for Meta AI features across Facebook, Instagram, WhatsApp |

## What Gets Checked

### 1. robots.txt Analysis (40 points)

The skill fetches and parses the target domain's `robots.txt` file, checking for:

- **Explicit Allow directives** for each AI crawler
- **Explicit Disallow directives** for each AI crawler
- **Wildcard rules** (`User-agent: *`) that may inadvertently block AI crawlers
- **Crawl-delay directives** that may slow AI indexing
- **Sitemap references** that help AI crawlers discover content
- **Missing robots.txt** — defaults to allow-all, which is fine for AEO

**Common mistakes detected:**
- Blocking GPTBot while allowing Googlebot (loses ChatGPT visibility)
- Using `Disallow: /` for `User-agent: *` without explicit AI crawler allows
- Blocking CCBot (blocks Common Crawl which feeds many AI training sets)
- No sitemap directive (AI crawlers rely on sitemaps for discovery)

### 2. Sitemap Availability (20 points)

- **sitemap.xml exists** and is accessible
- **Sitemap references in robots.txt** are present and valid
- **Sitemap freshness** — last modified date is recent
- **Content coverage** — key pages are included in the sitemap
- **Sitemap format** — valid XML, proper URL structure

### 3. Page Accessibility (20 points)

- **HTTP status codes** — pages return 200 (not 301/302/403/404/500)
- **JavaScript rendering requirements** — content behind JS is invisible to most AI crawlers
- **Login/paywall barriers** — content behind authentication is not crawlable
- **Rate limiting** — aggressive rate limiting may cause AI crawlers to give up
- **CDN/WAF blocking** — CloudFlare and similar services may block AI crawlers by default

### 4. Meta Directives (20 points)

- **Meta robots tags** — `noindex`, `nofollow`, `nosnippet` directives
- **X-Robots-Tag headers** — HTTP header-level directives
- **Canonical URLs** — proper canonicalization prevents duplicate content confusion
- **AI-specific meta tags** — emerging `noai` and `noimageai` directives

## Output Format

```markdown
## Crawler Access Report

### Overall Technical Access Score: [XX]/100

### Crawler Status Matrix

| Crawler | Status | robots.txt | Accessible | Notes |
|---------|--------|-----------|------------|-------|
| GPTBot | ALLOWED/BLOCKED | Allow/Disallow/No rule | Yes/No | [details] |
| ClaudeBot | ALLOWED/BLOCKED | Allow/Disallow/No rule | Yes/No | [details] |
| ... | ... | ... | ... | ... |

### robots.txt Analysis
- File status: [Found/Missing/Error]
- AI crawler rules: [N] explicit, [N] implicit
- Sitemap referenced: [Yes/No]
- Issues found: [N]

### Critical Issues
1. [Issue] — [Impact] — [Fix]

### Recommendations
1. [Highest-priority fix]
2. [Second fix]
3. [Third fix]

### Recommended robots.txt Additions
```
[Generated robots.txt rules]
```
```

## Recommended robots.txt Configuration

### Maximum AI Visibility (recommended for most sites)

```
# AI Crawlers — Allow for AEO visibility
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Applebot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: CCBot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: Meta-ExternalAgent
Allow: /

Sitemap: https://example.com/sitemap.xml
```

### Selective Access (protect premium content)

```
# Allow AI crawlers on public content only
User-agent: GPTBot
Allow: /blog/
Allow: /resources/
Disallow: /premium/
Disallow: /members/

User-agent: ClaudeBot
Allow: /blog/
Allow: /resources/
Disallow: /premium/
Disallow: /members/
```

### Block Training, Allow Search (emerging use case)

Some publishers want AI engines to cite their content in search but not use it for model training. Currently, there is no reliable technical mechanism for this distinction. The closest approach:

1. Allow Tier 1 crawlers (they power AI search features)
2. Block CCBot (primarily used for training datasets)
3. Use TOS/licensing to restrict training use
4. Monitor the evolving `ai.txt` and `tdmrep.json` standards

## Integration

This sub-skill feeds the Technical Access dimension (15% weight) of the composite AEO Visibility Score. It can be run standalone or as part of `/aeo audit`.

The Python implementation is available at `scripts/crawler_checker.py` for automated monitoring.
