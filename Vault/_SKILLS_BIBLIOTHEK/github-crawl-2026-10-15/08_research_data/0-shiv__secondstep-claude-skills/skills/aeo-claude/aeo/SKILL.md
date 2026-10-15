# AEO — AI Engine Optimization

## Description

AEO (AI Engine Optimization) is the practice of optimizing web content so that AI-powered search engines — ChatGPT, Perplexity, Gemini, Claude, and others — cite, quote, and attribute your content in their responses. Unlike traditional SEO which focuses on ranking in link-based algorithms, AEO focuses on making content **selectable by large language models** as authoritative source material.

This skill provides a comprehensive framework for auditing and optimizing content across every dimension that influences AI citation probability: citability, crawler access, brand authority, entity recognition, content structure, FAQ strategy, and knowledge graph positioning.

## Commands

- `/aeo audit <url>` — Run a full AEO audit across all 7 dimensions. Produces a composite AEO Visibility Score (0-100) with per-dimension breakdowns and prioritized recommendations. This is the primary entry point for most users.

- `/aeo citability <url|content>` — Analyze content for AI citation potential. Scores self-contained passages (134-167 word ideal length), factual density (statistics, dates, verifiable claims), unique data presence, clear attribution patterns, structured claims, and quotable statements. Returns a per-page citability score 0-100.

- `/aeo crawlers <url>` — Check whether AI crawlers can access your content. Analyzes robots.txt for GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Bingbot, Applebot, Bytespider, CCBot, anthropic-ai, cohere-ai, and Meta-ExternalAgent. Provides recommendations for allowing or blocking specific crawlers based on your use case.

- `/aeo llmstxt <url>` — Generate an `llms.txt` file following the emerging standard for communicating site structure and preferred citation format to AI engines. Includes site description, key pages, content hierarchy, and attribution preferences.

- `/aeo brands <brand> [domain]` — Scan for brand mentions across YouTube, Reddit, Wikipedia, LinkedIn, Quora, Medium, industry forums, podcasts, and news sites. Calculates a Brand Authority Signal score that correlates with AI citation frequency.

- `/aeo entity <url|brand>` — Optimize entity recognition to ensure AI engines treat your business as a distinct, recognized entity. Checks Knowledge Panel signals, Wikidata presence, NAP consistency across the web, and schema.org Organization markup.

- `/aeo structure <url|content>` — Analyze content formatting for AI parsability. Evaluates header hierarchy (H2/H3), bulleted lists, definition patterns ("X is Y"), comparison tables, FAQ sections, statistics with sources, and author bio with credentials.

- `/aeo faq <url|topic>` — Optimize FAQ content for AI citation. Analyzes conversational question formats (how AI users actually ask), answer comprehensiveness (50-100 word sweet spot), question clustering, featured snippet targeting, and People Also Ask alignment.

- `/aeo knowledge <url|topic>` — Optimize Knowledge Graph positioning through entity relationships, topic authority clusters, semantic connections, internal linking for topic authority, and external authority signal analysis.

- `/aeo report <url>` — Generate a comprehensive AEO audit report combining all dimension scores, crawler access status, brand mention map, entity recognition status, and prioritized content optimization recommendations. Outputs as structured markdown.

## AEO Visibility Score

The AEO Visibility Score is a composite metric (0-100) calculated from 7 weighted dimensions:

| Dimension | Weight | Scoring Criteria |
|-----------|--------|-----------------|
| Citability | 25% | Passage self-containment, factual density, quotable statements, unique data |
| Brand Authority | 20% | Mention volume, platform diversity, sentiment, recency |
| Content Structure | 20% | Header hierarchy, list usage, definition patterns, tables, FAQ presence |
| Technical Access | 15% | AI crawler permissions, robots.txt configuration, sitemap availability |
| Entity Recognition | 10% | Knowledge Panel, Wikidata, NAP consistency, schema markup |
| Knowledge Graph | 10% | Topic clusters, semantic links, internal authority, external citations |

### Score Bands

- **0-30 (Invisible):** Content is not structured for AI citation. AI engines will not select this content as a source. Requires fundamental restructuring.
- **31-50 (Low):** Some positive signals present but major gaps in multiple dimensions. AI engines may occasionally reference but not cite.
- **51-70 (Moderate):** Competitive foundation established. Targeted optimization in weak dimensions can yield significant gains.
- **71-85 (Strong):** Content is regularly cited by one or more AI engines. Fine-tuning and monitoring recommended.
- **86-100 (Dominant):** Authoritative source across multiple AI platforms. Focus on maintaining position and expanding topic coverage.

## Workflow

1. **Audit** — Start with `/aeo audit` to get baseline scores across all dimensions
2. **Prioritize** — Focus on the lowest-scoring dimensions with highest weight (Citability > Brand Authority > Content Structure)
3. **Optimize** — Use individual sub-skills to deep-dive and fix specific dimensions
4. **Generate** — Create `llms.txt` and update technical configurations
5. **Monitor** — Re-run audit monthly to track score changes and identify new opportunities

## Key Principles

### The Citability Threshold
AI engines extract passages of 134-167 words. Content must be written in self-contained blocks that make sense without surrounding context. Each passage should contain at least one verifiable fact, statistic, or unique insight.

### The Brand Authority Loop
AI engines learn from the open web. Brand mentions on Reddit, YouTube, Wikipedia, and authoritative forums create training signal. More mentions = higher citation probability = more mentions. First-mover advantage compounds.

### The Entity Clarity Principle
AI engines must recognize your business as a distinct entity before they can cite it. This requires consistent naming, structured data (schema.org), Knowledge Panel signals, and Wikidata presence. Entity confusion (multiple businesses with similar names) suppresses citation.

### The Structure Tax
Poorly structured content costs you AI visibility even if the information is excellent. AI engines preferentially extract from content with clear headers, definition patterns, comparison tables, and FAQ sections. Restructuring existing content often yields 20-40% citability improvement with zero new content creation.

## Sub-Skills

| Sub-Skill | File | Purpose |
|-----------|------|---------|
| aeo-citability | `skills/aeo-citability/SKILL.md` | Content citability scoring and optimization |
| aeo-crawlers | `skills/aeo-crawlers/SKILL.md` | AI crawler access verification |
| aeo-llmstxt | `skills/aeo-llmstxt/SKILL.md` | llms.txt file generation |
| aeo-brand-mentions | `skills/aeo-brand-mentions/SKILL.md` | Brand mention scanning and scoring |
| aeo-entity-recognition | `skills/aeo-entity-recognition/SKILL.md` | Entity optimization for AI recognition |
| aeo-content-structure | `skills/aeo-content-structure/SKILL.md` | Content formatting for AI parsability |
| aeo-faq-optimization | `skills/aeo-faq-optimization/SKILL.md` | FAQ strategy for AI citation |
| aeo-knowledge-graph | `skills/aeo-knowledge-graph/SKILL.md` | Knowledge Graph positioning |
| aeo-report | `skills/aeo-report/SKILL.md` | Comprehensive audit report generation |
