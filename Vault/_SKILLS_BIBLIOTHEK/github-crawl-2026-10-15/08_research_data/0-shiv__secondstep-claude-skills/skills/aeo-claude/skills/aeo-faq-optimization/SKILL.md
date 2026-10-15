# AEO FAQ Optimization — FAQ Strategy for AI Citation

## Description

The FAQ optimization sub-skill analyzes and optimizes FAQ content for maximum AI citation potential. AI-powered search engines are fundamentally question-answering systems — users ask questions, and AI engines find and cite the best answers. FAQ sections that match how users naturally ask questions to AI engines become high-probability citation targets.

FAQ optimization contributes to the Content Structure dimension (20% weight) of the AEO Visibility Score and has outsized impact on citability (25% weight) because FAQ answers are inherently self-contained passages.

## Command

```
/aeo faq <url|topic> [--generate] [--count <N>]
```

- `--generate` — Generate optimized FAQ content for the topic
- `--count` — Number of FAQ questions to generate (default: 10)

## Why FAQ Content Gets Cited by AI

AI-powered search engines have a structural preference for FAQ content because:

1. **Direct question-answer mapping** — The user's query maps directly to a question in the FAQ, and the answer is a self-contained passage ready for citation
2. **Concise, extractable answers** — Well-written FAQ answers (50-100 words) fit perfectly into AI response patterns
3. **Question diversity** — FAQs cover multiple question variants, increasing the surface area for citation
4. **Semantic clarity** — The question provides context that makes the answer unambiguous
5. **Featured snippet alignment** — FAQ content optimized for AI also captures Google Featured Snippets

## What Gets Measured

### 1. Question Format Analysis (25 points)

How users ask questions to AI engines differs from how they type into Google:

- **Conversational tone** — "How do I optimize my content for ChatGPT?" beats "ChatGPT content optimization"
- **Complete sentences** — Full question sentences, not keyword fragments
- **Question word diversity** — Mix of what, how, why, when, where, who, which, can, should, does
- **Specificity level** — Questions specific enough to have definitive answers
- **Natural language patterns** — Questions that match how people talk to AI assistants
- **Avoiding jargon in questions** — Questions use plain language even if answers are technical

**Scoring:**
- Keyword-style questions or no FAQ = 0-5 points
- Some conversational questions = 6-12 points
- Mostly conversational with good word diversity = 13-18 points
- Fully conversational, diverse, specific questions = 19-25 points

### 2. Answer Quality (25 points)

Answer quality directly determines citation probability:

- **Length sweet spot** — 50-100 words per answer is ideal for AI extraction. Under 30 words lacks substance; over 150 words gets truncated or skipped
- **Self-containment** — Each answer makes sense without reading the question (AI engines sometimes extract answers without the question)
- **Factual density** — Answers include specific numbers, dates, or verifiable claims when relevant
- **Actionable content** — Answers tell the reader what to do, not just what to know
- **Source attribution** — Claims backed by named sources or data
- **Definition inclusion** — Answers that define key terms score higher

**Scoring:**
- Answers too short (<30 words) or too long (>200 words) = 0-5 points
- Moderate quality, inconsistent length = 6-12 points
- Good length, self-contained, some facts = 13-18 points
- Optimal length, factual, actionable, attributed = 19-25 points

### 3. Question Clustering (25 points)

Strategic question selection maximizes topic coverage and citation surface area:

- **Topic clusters** — Questions grouped by subtopic (not random order)
- **Funnel coverage** — Questions spanning awareness, consideration, and decision stages
- **Question hierarchy** — Broad questions first, specific questions after
- **Semantic coverage** — Questions cover all major aspects of the topic
- **Long-tail targeting** — Includes specific, niche questions that have less competition
- **No redundancy** — Each question addresses a distinct user need

**Scoring:**
- Random, unorganized questions = 0-5 points
- Some logical grouping = 6-12 points
- Clear clusters with good topic coverage = 13-18 points
- Strategic clusters covering full funnel with long-tail = 19-25 points

### 4. Technical Implementation (25 points)

How the FAQ is technically implemented affects AI engine extraction:

- **FAQ schema markup** — `@type: FAQPage` with `Question` and `Answer` entities
- **Proper HTML structure** — Questions in headings or `<dt>`, answers in `<p>` or `<dd>`
- **Visible on page** — Not hidden behind JavaScript accordions that crawlers cannot render
- **Not duplicated** — FAQ content is unique, not copied from other pages
- **Mobile accessible** — FAQ renders and is readable on mobile devices
- **Page positioning** — FAQ section placement (bottom of content pages is standard)

**Scoring:**
- No schema, poor HTML, hidden content = 0-5 points
- Partial schema or visible but unstructured = 6-12 points
- Full schema, proper HTML, visible = 13-18 points
- Complete implementation with all best practices = 19-25 points

## Output Format

```markdown
## FAQ Optimization Score: [XX]/100

### Page: [URL or Topic]
### Questions Analyzed: [N]

### Question Format
- Conversational questions: [N]/[Total] ([%])
- Question word distribution: What [N], How [N], Why [N], When [N], Other [N]
- Average question length: [N] words
- Jargon-free: [N]/[Total]

### Answer Quality
- Average answer length: [N] words
- In sweet spot (50-100 words): [N]/[Total]
- Self-contained: [N]/[Total]
- Contains facts/data: [N]/[Total]
- Actionable: [N]/[Total]

### Question Strategy
- Topic clusters: [N]
- Funnel coverage: [Awareness/Consideration/Decision]
- Redundant questions: [N]
- Long-tail questions: [N]

### Technical
- FAQ schema: [Present/Missing]
- HTML structure: [Good/Issues]
- Visible without JS: [Yes/No]

### Top Performing Questions
1. Q: "[Question]" — Score: [X]/10 — [Why it works]
2. Q: "[Question]" — Score: [X]/10 — [Why it works]

### Questions to Improve
1. Q: "[Question]" — Issue: [What's wrong] — Fix: [How to fix]

### Recommendations
1. [Highest-impact improvement]
2. [Second improvement]
3. [Third improvement]
```

## FAQ Generation

When using `--generate`, the skill produces optimized FAQ content:

```markdown
## Generated FAQ: [Topic]

### Cluster 1: [Subtopic — Awareness]

**Q: What is [topic] and why does it matter for businesses?**
A: [50-100 word answer with definition pattern, specific statistic, and actionable insight]

**Q: How does [topic] differ from [related concept]?**
A: [50-100 word answer with comparison, specific differences, and practical example]

### Cluster 2: [Subtopic — Consideration]

**Q: How much does [topic] typically cost?**
A: [50-100 word answer with price ranges, factors affecting cost, and ROI context]

### Cluster 3: [Subtopic — Decision]

**Q: What should I look for when choosing a [topic] provider?**
A: [50-100 word answer with checklist-style criteria]
```

## People Also Ask (PAA) Alignment

The skill identifies People Also Ask questions from search engines and maps them to your FAQ coverage:

- **PAA questions found** for the topic
- **Coverage gaps** — PAA questions not addressed in your FAQ
- **Suggested additions** — New FAQ questions based on PAA data
- **Ranking opportunities** — PAA questions where your content is most competitive

## Integration

This sub-skill contributes to both the Content Structure dimension (20%) and Citability dimension (25%) of the composite AEO Visibility Score, making it one of the highest-impact individual optimizations.

Well-optimized FAQ content can be responsible for 30-50% of a page's total AI citations because each Q&A pair is an independent citation target.
