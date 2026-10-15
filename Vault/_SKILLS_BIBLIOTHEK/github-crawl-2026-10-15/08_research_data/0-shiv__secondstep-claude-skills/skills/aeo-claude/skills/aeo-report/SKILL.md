# AEO Report — Comprehensive AEO Audit Report Generation

## Description

The report sub-skill generates a comprehensive AEO audit report combining all dimension scores, detailed findings, and prioritized recommendations. This is the primary output artifact of an AEO engagement — a document that can be shared with clients, stakeholders, or used as an internal optimization roadmap.

The report synthesizes data from all other sub-skills into a single, actionable document with clear scoring, priority rankings, and implementation timelines.

## Command

```
/aeo report <url> [--format md|html|pdf] [--depth quick|standard|comprehensive]
```

- `--format` — Output format (default: markdown)
- `--depth quick` — Score-only summary (5 minutes)
- `--depth standard` — Full analysis with recommendations (15 minutes)
- `--depth comprehensive` — Deep dive with competitor comparison and content roadmap (30 minutes)

## Report Structure

### Section 1: Executive Summary

```markdown
## AEO Audit Report
### [Website/Brand Name]
### Date: [YYYY-MM-DD]
### Audit Depth: [Quick/Standard/Comprehensive]

---

## Executive Summary

**AEO Visibility Score: [XX]/100 — [Invisible/Low/Moderate/Strong/Dominant]**

[2-3 sentence summary of overall position, biggest strength, and most critical gap]

### Score Breakdown
| Dimension | Weight | Score | Rating |
|-----------|--------|-------|--------|
| Citability | 25% | [XX]/100 | [band] |
| Brand Authority | 20% | [XX]/100 | [band] |
| Content Structure | 20% | [XX]/100 | [band] |
| Technical Access | 15% | [XX]/100 | [band] |
| Entity Recognition | 10% | [XX]/100 | [band] |
| Knowledge Graph | 10% | [XX]/100 | [band] |
| **Composite** | **100%** | **[XX]/100** | **[band]** |

### Top 3 Priority Actions
1. **[Action]** — Expected impact: +[N] points — Effort: [Low/Medium/High]
2. **[Action]** — Expected impact: +[N] points — Effort: [Low/Medium/High]
3. **[Action]** — Expected impact: +[N] points — Effort: [Low/Medium/High]
```

### Section 2: Citability Analysis

Detailed citability findings from `/aeo citability`:

- Passage self-containment analysis with examples
- Factual density scoring with specific gaps identified
- Quotable statement inventory
- Top 5 most citable passages highlighted
- Top 5 least citable passages with rewrite suggestions
- Citability score trend (if historical data available)

### Section 3: Brand Authority Map

Detailed brand mention findings from `/aeo brands`:

- Platform-by-platform mention inventory
- Sentiment analysis across platforms
- Competitive brand mention comparison
- Brand mention velocity trend
- Key mentions with quotes and links
- Brand mention building opportunities

### Section 4: Content Structure Audit

Detailed structural findings from `/aeo structure`:

- Header hierarchy analysis
- List usage and optimization opportunities
- Definition pattern inventory
- Table presence and quality
- FAQ section analysis
- Author credential presence
- Page-by-page structural scores for top pages

### Section 5: Technical Access Report

Detailed crawler access findings from `/aeo crawlers`:

- robots.txt analysis with per-crawler status
- Sitemap accessibility and coverage
- Page accessibility issues
- Meta directive analysis
- Recommended robots.txt configuration
- Implementation checklist

### Section 6: Entity Recognition Status

Detailed entity findings from `/aeo entity`:

- Knowledge Panel status
- Wikidata presence and completeness
- NAP consistency audit
- Schema.org markup analysis
- Entity disambiguation status
- Recommended schema.org markup template

### Section 7: Knowledge Graph Position

Detailed knowledge graph findings from `/aeo knowledge`:

- Topic authority cluster analysis
- Semantic connection mapping
- Internal linking architecture review
- External authority signal inventory
- Topic gap analysis
- Content roadmap for authority building

### Section 8: Implementation Roadmap

Prioritized action plan organized by effort and impact:

```markdown
## Implementation Roadmap

### Week 1-2: Quick Wins (Low Effort, High Impact)
- [ ] [Action] — Dimension: [X] — Expected: +[N] points
- [ ] [Action] — Dimension: [X] — Expected: +[N] points
- [ ] [Action] — Dimension: [X] — Expected: +[N] points

### Week 3-4: Technical Fixes (Medium Effort, High Impact)
- [ ] [Action] — Dimension: [X] — Expected: +[N] points
- [ ] [Action] — Dimension: [X] — Expected: +[N] points

### Month 2: Content Optimization (Medium Effort, Medium Impact)
- [ ] [Action] — Dimension: [X] — Expected: +[N] points
- [ ] [Action] — Dimension: [X] — Expected: +[N] points

### Month 3-6: Authority Building (High Effort, Long-term Impact)
- [ ] [Action] — Dimension: [X] — Expected: +[N] points
- [ ] [Action] — Dimension: [X] — Expected: +[N] points

### Projected Score After Implementation
| Dimension | Current | Projected | Change |
|-----------|---------|-----------|--------|
| Citability | [XX] | [XX] | +[N] |
| Brand Authority | [XX] | [XX] | +[N] |
| Content Structure | [XX] | [XX] | +[N] |
| Technical Access | [XX] | [XX] | +[N] |
| Entity Recognition | [XX] | [XX] | +[N] |
| Knowledge Graph | [XX] | [XX] | +[N] |
| **Composite** | **[XX]** | **[XX]** | **+[N]** |
```

### Section 9: Monitoring & Next Steps

- Recommended re-audit frequency (monthly for active optimization, quarterly for maintenance)
- Key metrics to track between audits
- AI search landscape changes to monitor
- Emerging opportunities (new AI platforms, standard changes)

## Report Depth Levels

### Quick (5 minutes)
- Executive summary with composite score
- Per-dimension scores without detailed analysis
- Top 3 priority actions
- No competitor comparison

### Standard (15 minutes)
- Full executive summary
- Detailed analysis for each dimension
- Priority actions with effort/impact ratings
- Basic implementation roadmap
- No competitor comparison

### Comprehensive (30 minutes)
- Everything in Standard plus:
- Competitor comparison across all dimensions
- Page-by-page analysis of top 10 pages
- Content gap analysis with roadmap
- Projected scores after implementation
- Historical trend analysis (if previous reports exist)

## Output Formats

### Markdown (default)
Standard markdown file suitable for GitHub, Notion, or any markdown renderer.

### HTML
Styled HTML report with Second Step branding (dark theme, orange accents) suitable for client delivery.

### PDF
PDF version generated from HTML, suitable for formal client presentations.

## Integration

This sub-skill aggregates all other sub-skill outputs into a unified report. It requires running all dimension analyses first (either individually or through `/aeo audit` which runs them all).

The report template is available at `templates/aeo-audit-template.md` for customization.

Reports can be generated programmatically using the Python scripts in the `scripts/` directory for batch processing across multiple client sites.
