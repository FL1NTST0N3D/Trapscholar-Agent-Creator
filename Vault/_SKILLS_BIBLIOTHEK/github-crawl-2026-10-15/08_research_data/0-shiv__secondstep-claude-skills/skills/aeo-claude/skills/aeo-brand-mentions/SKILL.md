# AEO Brand Mentions — Brand Authority Signal Scanning

## Description

The brand mentions sub-skill scans for brand mentions across the platforms that AI engines use as training data and retrieval sources. Brand mentions correlate **3x more strongly** with AI visibility than traditional backlinks. AI engines learn brand authority from the breadth, depth, and sentiment of brand discussions across the open web — not from hyperlinks.

Brand Authority carries 20% of the total AEO Visibility Score. Unlike traditional SEO where you can build authority through link building, AEO authority requires genuine brand presence across platforms where real humans discuss, recommend, and evaluate products and services.

## Command

```
/aeo brands <brand_name> [--domain <domain>] [--competitors <brand1,brand2>]
```

## Platforms Scanned

### Tier 1: Highest AI Training Signal

| Platform | Why It Matters | Signal Type |
|----------|---------------|-------------|
| **Reddit** | Massive training dataset for most LLMs. Subreddit discussions, recommendations, and comparisons are heavily weighted. | Discussion volume, sentiment, subreddit diversity |
| **Wikipedia** | Gold standard for entity recognition. Having a Wikipedia page = entity status. | Page existence, content depth, citation quality |
| **YouTube** | Second-largest search engine. Video titles, descriptions, and transcripts feed AI training. | Mention frequency, channel authority, comment sentiment |

### Tier 2: Strong Authority Signal

| Platform | Why It Matters | Signal Type |
|----------|---------------|-------------|
| **LinkedIn** | Professional authority signal. Company pages, employee posts, thought leadership. | Company page completeness, employee advocacy, article mentions |
| **Quora** | Direct Q&A format mirrors how AI engines serve information. | Answer frequency, upvotes, expert endorsements |
| **Medium** | Long-form content platform indexed by most AI crawlers. | Article mentions, publication quality, clap counts |
| **Industry Forums** | Niche authority in vertical-specific communities. | Thread mentions, expert recommendations, sticky posts |

### Tier 3: Supporting Signal

| Platform | Why It Matters | Signal Type |
|----------|---------------|-------------|
| **Podcasts** | Transcript data increasingly feeds AI training. | Episode mentions, guest appearances, show authority |
| **News Sites** | Press coverage creates entity authority. | Article mentions, publication tier, recency |
| **Review Platforms** | G2, Capterra, Trustpilot, Yelp — structured review data. | Rating, review volume, response rate |

## What Gets Measured

### 1. Mention Volume (25 points)

Raw count of brand mentions across all platforms, normalized by industry and brand size:

- **Total mentions found** across all platforms
- **Mention velocity** — mentions per month (trend direction matters)
- **Platform coverage** — number of distinct platforms with mentions
- **Unique contexts** — mentions in genuinely different discussions (not spam/duplicates)

**Scoring:**
- 0-5 mentions across platforms = 0-5 points
- 6-20 mentions = 6-12 points
- 21-50 mentions = 13-18 points
- 51-100 mentions = 19-22 points
- 100+ mentions = 23-25 points

### 2. Platform Diversity (25 points)

AI engines trust brands that appear across **multiple independent platforms**. A brand mentioned only on its own blog and website scores poorly. A brand discussed on Reddit, YouTube, LinkedIn, and industry forums scores highly.

- **Platform count** — how many distinct platforms have mentions
- **Platform tier mix** — mentions on Tier 1 platforms weighted 3x
- **Context diversity** — different types of mentions (recommendations, comparisons, tutorials, reviews)
- **Geographic diversity** — mentions from different regions/languages

### 3. Sentiment Quality (25 points)

Not all mentions are equal. AI engines weight positive and neutral mentions far more than negative ones:

- **Positive mentions** — Recommendations, endorsements, success stories
- **Neutral mentions** — Factual references, comparisons, feature descriptions
- **Negative mentions** — Complaints, negative reviews, criticism
- **Sentiment ratio** — (positive + neutral) / total mentions

**Scoring:**
- Sentiment ratio < 0.5 = 0-5 points
- Sentiment ratio 0.5-0.7 = 6-12 points
- Sentiment ratio 0.7-0.85 = 13-18 points
- Sentiment ratio 0.85-0.95 = 19-22 points
- Sentiment ratio > 0.95 = 23-25 points

### 4. Recency (25 points)

AI engines weight recent mentions more heavily. Brand authority decays without ongoing mention activity:

- **Mentions in last 30 days** — Highly weighted
- **Mentions in last 90 days** — Moderately weighted
- **Mentions in last 12 months** — Baseline weight
- **Mention trend** — Increasing, stable, or declining

## Output Format

```markdown
## Brand Authority Score: [XX]/100

### Brand: [Brand Name]
### Domain: [domain.com]

### Mention Summary
- Total mentions found: [N]
- Platforms with mentions: [N]/11
- Mention velocity: [N]/month ([trend])
- Overall sentiment: [Positive/Neutral/Mixed/Negative] ([ratio])

### Platform Breakdown

| Platform | Mentions | Sentiment | Top Context | Recency |
|----------|----------|-----------|-------------|---------|
| Reddit | [N] | [+/-/~] | [context] | [date] |
| YouTube | [N] | [+/-/~] | [context] | [date] |
| Wikipedia | [Present/Absent] | N/A | [context] | [date] |
| ... | ... | ... | ... | ... |

### Key Mentions
1. [Platform] — "[Quote or summary]" — [URL] — [Date]
2. [Platform] — "[Quote or summary]" — [URL] — [Date]
3. [Platform] — "[Quote or summary]" — [URL] — [Date]

### Competitive Comparison (if competitors provided)
| Metric | [Your Brand] | [Competitor 1] | [Competitor 2] |
|--------|-------------|----------------|----------------|
| Total mentions | [N] | [N] | [N] |
| Platform coverage | [N] | [N] | [N] |
| Sentiment ratio | [X] | [X] | [X] |

### Recommendations
1. [Highest-impact recommendation for building brand mentions]
2. [Second recommendation]
3. [Third recommendation]

### Brand Mention Building Strategy
- **Reddit:** [Specific subreddits to engage in]
- **YouTube:** [Content collaboration opportunities]
- **LinkedIn:** [Thought leadership actions]
- **Wikipedia:** [Eligibility status and path to a page]
```

## Brand Authority Building Strategies

### Quick Wins (1-2 weeks)
- Respond to existing Reddit threads mentioning your industry
- Create a comprehensive LinkedIn company page with regular posting
- Ask satisfied customers to mention you on relevant forums
- Publish a Medium article about your industry expertise

### Medium Effort (1-3 months)
- Launch a YouTube channel with educational content
- Guest on 3-5 industry podcasts
- Write Quora answers about your area of expertise
- Pursue industry award nominations and press coverage

### High Effort (3-6 months)
- Build Wikipedia notability through press coverage and citations
- Create original research that others cite and discuss
- Establish a subreddit community around your topic area
- Develop a thought leadership program for employees on LinkedIn

## Integration

This sub-skill feeds the Brand Authority dimension (20% weight) of the composite AEO Visibility Score. It can be run standalone or as part of `/aeo audit`.

The Python implementation is available at `scripts/brand_mention_scanner.py` for automated scanning.
