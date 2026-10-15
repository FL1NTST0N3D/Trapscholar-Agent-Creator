# AEO Citability — Content Citation Scoring & Optimization

## Description

The citability sub-skill analyzes content to determine how likely it is to be selected, extracted, and cited by AI-powered search engines. AI engines do not rank pages — they extract **passages**. This skill scores content based on the specific characteristics that make passages extractable and citable by large language models.

Citability is the single most important dimension of AEO, carrying 25% of the total AEO Visibility Score. Content that scores poorly on citability will not be cited regardless of how well it performs on other dimensions.

## Command

```
/aeo citability <url|file_path|raw_content>
```

## What Gets Measured

### 1. Passage Self-Containment (30 points)

AI engines extract passages of **134-167 words** that must make sense without surrounding context. The citability scorer identifies every potential extraction passage in the content and evaluates whether each passage:

- **Stands alone** — Can a reader understand this passage without reading anything before or after it?
- **Contains a complete thought** — Does the passage make a claim, provide evidence, and reach a conclusion?
- **Avoids dangling references** — No "as mentioned above," "see below," "this," or "the previous section" without clear antecedents
- **Hits the sweet spot** — Passages between 134-167 words score highest. Shorter passages lack sufficient context; longer passages get truncated

**Scoring:** Each passage is scored 0-10 on self-containment. The page score is the average of all passage scores, normalized to 30 points.

### 2. Factual Density (25 points)

AI engines preferentially cite content with **verifiable, specific claims**. Vague content ("many companies are adopting AI") is never cited. Specific content ("73% of Fortune 500 companies adopted generative AI tools in 2025, according to McKinsey") gets cited repeatedly.

The factual density scorer counts and categorizes:

- **Statistics** — Percentages, dollar amounts, growth rates, comparisons with numbers
- **Dates and timeframes** — Specific years, quarters, date ranges
- **Named sources** — "According to [Source]," "Research by [Institution] found"
- **Verifiable claims** — Statements that can be fact-checked against external data
- **Unique data** — Original research, proprietary statistics, first-party survey results

**Scoring formula:**
```
Factual Density = (fact_count / word_count) × 1000
```
- 0-5 facts per 1000 words = 0-5 points
- 6-10 facts per 1000 words = 6-15 points
- 11-15 facts per 1000 words = 16-22 points
- 16+ facts per 1000 words = 23-25 points

### 3. Quotable Statements (20 points)

AI engines look for **definitive statements** that directly answer user questions. Quotable statements follow specific patterns:

- **Definition patterns** — "AEO is the practice of optimizing content for AI-powered search engines"
- **Causal claims** — "Brand mentions correlate 3x more with AI visibility than backlinks because..."
- **Comparative statements** — "Unlike traditional SEO, AEO focuses on passage extraction rather than page ranking"
- **Prescriptive statements** — "To optimize for AI citation, structure content in 134-167 word self-contained passages"
- **Superlative claims with evidence** — "The most effective AEO strategy is... according to [data]"

**Scoring:** Count of quotable statements per 1000 words, normalized to 20 points.

### 4. Clear Attribution (15 points)

Content that cites its own sources is more likely to be cited by AI engines. Attribution patterns include:

- **Named expert quotes** — "John Smith, CEO of Example Corp, stated..."
- **Research citations** — "A 2025 study by Stanford University found..."
- **Data source attribution** — "According to Statista, the market reached $850M in 2024"
- **Methodology transparency** — "Based on analysis of 10,000 search queries..."
- **Author credentials** — Author bio with relevant expertise, title, and experience

**Scoring:** Attribution quality and frequency, normalized to 15 points.

### 5. Structural Quotability (10 points)

Some content formats are inherently more citable:

- **Numbered lists** — "The 5 key factors are: 1) ..."
- **Comparison tables** — Side-by-side comparisons with clear headers
- **Step-by-step processes** — "Step 1: ... Step 2: ..."
- **Pro/con lists** — Balanced evaluations that AI engines can extract
- **Summary blocks** — TL;DR sections, key takeaways, executive summaries

**Scoring:** Presence and quality of structural elements, normalized to 10 points.

## Output Format

```markdown
## Citability Score: [XX]/100

### Passage Analysis
- Total extractable passages: [N]
- Self-contained passages: [N] ([%])
- Average passage length: [N] words
- Passages in sweet spot (134-167 words): [N]

### Factual Density
- Total verifiable facts: [N]
- Facts per 1000 words: [N]
- Statistics: [N] | Named sources: [N] | Unique data: [N]

### Quotable Statements
- Total quotable statements: [N]
- Definition patterns: [N]
- Comparative statements: [N]
- Prescriptive statements: [N]

### Attribution Quality
- Cited sources: [N]
- Expert quotes: [N]
- Author credentials: [Present/Missing]

### Top 3 Most Citable Passages
1. "[Passage text]" — Score: [X]/10
2. "[Passage text]" — Score: [X]/10
3. "[Passage text]" — Score: [X]/10

### Recommendations
1. [Highest-impact recommendation]
2. [Second recommendation]
3. [Third recommendation]
```

## Optimization Strategies

### Quick Wins (15 minutes)
- Add statistics with sources to vague claims
- Break long paragraphs into 134-167 word self-contained passages
- Add a "Key Takeaways" section at the top
- Add author bio with credentials

### Medium Effort (1-2 hours)
- Rewrite passages to eliminate dangling references ("this," "as above")
- Add comparison tables for any comparative discussion
- Convert prose explanations into numbered step-by-step processes
- Add FAQ section with 50-100 word answers

### High Effort (1-2 days)
- Conduct original research or surveys to create unique data points
- Add expert quotes from named sources
- Create comprehensive definition sections for key terms
- Build out topic authority with supporting articles

## Integration

This sub-skill feeds the Citability dimension (25% weight) of the composite AEO Visibility Score. It can be run standalone or as part of `/aeo audit`.

The Python implementation is available at `scripts/citability_scorer.py` for batch processing.
