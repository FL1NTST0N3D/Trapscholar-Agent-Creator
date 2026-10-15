# AEO Content Structure — Formatting Content for AI Parsability

## Description

The content structure sub-skill analyzes how content is formatted and organized for AI engine parsability. AI engines extract information from content based on structural patterns — clear headers, bulleted lists, definition patterns, comparison tables, and FAQ sections are dramatically easier for LLMs to parse, extract, and cite than unstructured prose.

Content Structure carries 20% of the total AEO Visibility Score. Restructuring existing content often yields a **20-40% citability improvement** with zero new content creation — making it one of the highest-ROI AEO activities.

## Command

```
/aeo structure <url|file_path|raw_content>
```

## What Gets Measured

### 1. Header Hierarchy (20 points)

Proper header structure creates a semantic outline that AI engines use to understand content organization and locate specific information:

- **H1 presence and uniqueness** — Single H1 that clearly describes the page topic
- **H2 structure** — Logical H2 sections that break content into distinct subtopics
- **H3 nesting** — H3s properly nested under H2s for sub-section detail
- **Header descriptiveness** — Headers that contain keywords and summarize section content (not clever/vague headers like "The Bottom Line" or "Let's Dive In")
- **Header density** — One H2 every 200-400 words is optimal for AI extraction
- **Skip-level detection** — H1 to H3 without H2 confuses structural parsing

**Scoring:**
- No headers or single header = 0-4 points
- Headers present but irregular = 5-10 points
- Logical hierarchy with descriptive headers = 11-16 points
- Perfect hierarchy with keyword-rich, regularly spaced headers = 17-20 points

### 2. List Usage (20 points)

Bulleted and numbered lists are among the most extractable content formats for AI engines:

- **Bulleted lists** for unordered information (features, benefits, examples)
- **Numbered lists** for ordered information (steps, rankings, priorities)
- **List item length** — 1-2 sentences per item (not single words, not full paragraphs)
- **List context** — Lists preceded by introductory sentences that explain what follows
- **Nested lists** — Used sparingly for hierarchical information
- **List density** — At least 1 list per 500 words of content

**Common issues:**
- Long paragraphs that should be lists
- Lists without context (no introductory sentence)
- Lists with inconsistent formatting (mixing sentences and fragments)
- Overuse of nested lists creating complexity

### 3. Definition Patterns (20 points)

AI engines heavily weight **"X is Y"** definition patterns because they directly answer "what is" questions:

- **Explicit definitions** — "AEO is the practice of optimizing content for AI-powered search engines."
- **Contextual definitions** — "AI Engine Optimization (AEO), also known as Generative Engine Optimization (GEO), refers to..."
- **First-paragraph definitions** — Key terms defined in the opening paragraph
- **Glossary sections** — Dedicated terminology sections for technical content
- **Inline definitions** — Key terms defined on first use

**Scoring:**
- No definition patterns = 0-4 points
- Some definitions present = 5-10 points
- Key terms defined with clear "X is Y" patterns = 11-16 points
- Comprehensive definitions + glossary = 17-20 points

### 4. Comparison Tables (20 points)

Comparison tables are the single most extractable content format for AI engines answering comparison questions:

- **Table presence** — At least one comparison table in comparison-type content
- **Table structure** — Clear headers, consistent columns, parseable cells
- **Table completeness** — All compared items have values for all columns
- **Table context** — Tables accompanied by explanatory text
- **Data tables** — Statistical data presented in table format rather than prose
- **Responsive design** — Tables that render properly (not broken on mobile)

**Scoring:**
- No tables in content that would benefit from them = 0-4 points
- Tables present but poorly structured = 5-10 points
- Well-structured comparison tables = 11-16 points
- Multiple tables with clear headers and complete data = 17-20 points

### 5. FAQ and Summary Sections (20 points)

FAQ sections and content summaries directly map to AI engine query patterns:

- **FAQ section present** — Dedicated FAQ with question-answer format
- **Question format** — Questions written in natural language (how users ask AI)
- **Answer length** — 50-100 words per answer (sweet spot for AI extraction)
- **Question coverage** — Covers "what," "how," "why," "when," "where," and "who"
- **Key takeaways** — Summary section at top or bottom with main points
- **TL;DR** — Brief summary for quick extraction
- **Statistics with sources** — Data points attributed to named sources
- **Author bio** — Author credentials establishing expertise

**Scoring:**
- No FAQ, no summary, no author bio = 0-4 points
- Partial elements present = 5-10 points
- FAQ section + summary + attributed statistics = 11-16 points
- Complete FAQ + takeaways + sourced stats + author bio = 17-20 points

## Output Format

```markdown
## Content Structure Score: [XX]/100

### Page: [URL or Title]
### Word Count: [N]

### Header Analysis
- H1: [Present/Missing] — "[H1 text]"
- H2 count: [N] (every [N] words)
- H3 count: [N]
- Hierarchy: [Valid/Issues]
- Descriptiveness: [Good/Needs improvement]

### List Analysis
- Bulleted lists: [N]
- Numbered lists: [N]
- Average items per list: [N]
- Lists per 500 words: [N]
- Context quality: [Good/Missing intros]

### Definition Patterns
- Explicit definitions: [N]
- Key terms undefined: [list]
- First-paragraph definition: [Present/Missing]

### Tables
- Tables present: [N]
- Comparison tables: [N]
- Data tables: [N]
- Structure quality: [Good/Issues]

### FAQ & Summary
- FAQ section: [Present/Missing]
- Questions: [N]
- Average answer length: [N] words
- Summary/takeaways: [Present/Missing]
- Author bio: [Present/Missing]
- Sourced statistics: [N]

### Content Restructuring Recommendations
1. [Highest-impact structural change]
2. [Second change]
3. [Third change]

### Suggested Header Outline
```
[Generated optimal header structure for this content]
```

### Missing Elements
- [ ] [Element that should be added]
- [ ] [Element that should be added]
```

## Content Structure Templates

### Informational Article Template
```
H1: [Topic] — [Key Qualifier]
  Intro paragraph with definition pattern
  Key Takeaways (bulleted list, 3-5 items)

H2: What is [Topic]?
  Definition paragraph ("X is Y")
  Context and significance

H2: How [Topic] Works
  H3: Step 1 — [Description]
  H3: Step 2 — [Description]
  H3: Step 3 — [Description]

H2: [Topic] vs [Alternative]
  Comparison table
  Explanatory text

H2: Benefits of [Topic]
  Bulleted list with 1-2 sentence items

H2: Frequently Asked Questions
  Q: [Natural language question]?
  A: [50-100 word answer]

Author Bio with credentials
```

### Product/Service Page Template
```
H1: [Product Name] — [Value Proposition]
  Definition + key statistic

H2: Key Features
  Feature comparison table

H2: How It Works
  Numbered steps with descriptions

H2: Pricing
  Pricing comparison table

H2: [Product] vs [Competitors]
  Comparison table

H2: FAQ
  5-8 questions with 50-100 word answers
```

## Integration

This sub-skill feeds the Content Structure dimension (20% weight) of the composite AEO Visibility Score. It can be run standalone or as part of `/aeo audit`.

Content structure improvements amplify citability — a well-structured page with the same content can score 20-40% higher on citability than an unstructured version.
