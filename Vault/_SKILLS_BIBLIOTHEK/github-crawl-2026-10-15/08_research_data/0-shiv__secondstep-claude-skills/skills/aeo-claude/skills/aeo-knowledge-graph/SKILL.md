# AEO Knowledge Graph — Topic Authority & Semantic Positioning

## Description

The Knowledge Graph sub-skill optimizes your content's position within the semantic knowledge structures that AI engines use to understand topic relationships, entity connections, and authority hierarchies. AI engines do not evaluate pages in isolation — they evaluate how a page fits within a broader web of interconnected topics, entities, and authority signals.

Knowledge Graph positioning carries 10% of the total AEO Visibility Score. While lower-weighted individually, it has a **multiplier effect** on other dimensions — strong knowledge graph positioning amplifies citability, brand authority, and entity recognition simultaneously.

## Command

```
/aeo knowledge <url|domain|topic> [--depth <1-3>] [--competitors <domain1,domain2>]
```

- `--depth` — Analysis depth: 1 (surface), 2 (standard), 3 (comprehensive)
- `--competitors` — Compare knowledge graph positioning against competitors

## How AI Engines Use Knowledge Graphs

AI engines build internal knowledge representations that map:

1. **Entity relationships** — "Company A" is a "SaaS platform" in the "supply chain" industry, founded by "Person B," competing with "Company C"
2. **Topic hierarchies** — "AEO" is a subtopic of "digital marketing," related to "SEO," "content marketing," and "AI search"
3. **Authority attribution** — "Source X" is authoritative on "Topic Y" based on content depth, citation frequency, and entity signals
4. **Semantic connections** — Topics that frequently co-occur, support each other, or share conceptual frameworks

Your content's position in these knowledge structures determines whether AI engines consider you authoritative enough to cite on a given topic.

## What Gets Measured

### 1. Topic Authority Clusters (30 points)

Topic authority is built through comprehensive coverage of related subtopics, not through a single page:

- **Content depth** — Multiple pages covering different aspects of your core topic
- **Subtopic coverage** — Breadth of subtopics addressed within your topic cluster
- **Content freshness** — Regular updates and new content on the topic
- **Cornerstone content** — One or more definitive, comprehensive guides on the core topic
- **Content interconnection** — Pages within a cluster link to and reference each other
- **Consistent terminology** — Same terms and definitions used across all cluster content

**Scoring:**
- Single page on topic, no cluster = 0-6 points
- 3-5 pages on related subtopics = 7-14 points
- 6-10 pages with clear cluster structure = 15-22 points
- 10+ pages with cornerstone content, full subtopic coverage = 23-30 points

### 2. Semantic Connections (25 points)

AI engines understand content through semantic relationships between concepts:

- **Co-occurrence patterns** — Your content naturally connects related concepts
- **Contextual framing** — Content explains how topics relate to each other
- **Cross-topic bridges** — Content connects your expertise to adjacent topic areas
- **Semantic richness** — Varied vocabulary covering synonyms, related terms, and technical language
- **Conceptual frameworks** — Original frameworks or models that organize knowledge

**Scoring:**
- Isolated content with no semantic connections = 0-5 points
- Some topic connections present = 6-12 points
- Clear semantic relationships across content = 13-18 points
- Rich semantic network with original frameworks = 19-25 points

### 3. Internal Linking Architecture (25 points)

Internal links are the primary mechanism for signaling topic relationships and authority hierarchy to AI crawlers:

- **Hub-and-spoke structure** — Cornerstone pages link to and from all subtopic pages
- **Contextual links** — Links embedded in relevant content (not sidebar/footer navigation)
- **Anchor text quality** — Descriptive anchor text that signals linked page topic
- **Link depth** — Important pages reachable within 2-3 clicks from homepage
- **Bidirectional links** — Subtopic pages link back to cornerstone content
- **Orphan page detection** — Pages with no internal links pointing to them

**Scoring:**
- No intentional linking structure = 0-5 points
- Some internal links but no clear hierarchy = 6-12 points
- Clear hub-and-spoke with contextual links = 13-18 points
- Comprehensive architecture with bidirectional, contextual linking = 19-25 points

### 4. External Authority Signals (20 points)

External sources citing your content reinforces knowledge graph positioning:

- **Inbound citations** — Other authoritative sites referencing your content
- **Expert contributions** — Guest posts, quotes, or interviews on authoritative sites
- **Research citations** — Academic or industry publications citing your data
- **Social proof** — Content shared and discussed by recognized experts
- **Directory presence** — Listed in authoritative industry directories and databases
- **Co-citation patterns** — You are cited alongside recognized authorities on the topic

**Scoring:**
- No external authority signals = 0-4 points
- Some directory listings and social shares = 5-10 points
- Inbound citations from authoritative sources = 11-16 points
- Research citations + expert co-citation = 17-20 points

## Output Format

```markdown
## Knowledge Graph Score: [XX]/100

### Domain/Topic: [URL or Topic]

### Topic Authority Clusters
- Core topic: [Identified primary topic]
- Content pages in cluster: [N]
- Subtopics covered: [list]
- Subtopics missing: [list]
- Cornerstone content: [URL or "Missing"]
- Content freshness: [Last updated date]

### Semantic Analysis
- Key entities identified: [list]
- Semantic connections: [N] unique topic relationships
- Vocabulary richness: [score]
- Original frameworks: [N]
- Adjacent topic bridges: [list]

### Internal Linking
- Total internal links analyzed: [N]
- Hub pages: [N] (pages with 10+ inbound internal links)
- Average link depth: [N] clicks from homepage
- Orphan pages: [N]
- Anchor text quality: [Good/Needs improvement]

### External Authority
- Inbound citations detected: [N]
- Authoritative sources citing you: [list]
- Co-cited with: [list of authorities]
- Directory presence: [N] directories

### Topic Gap Analysis
| Subtopic | Your Coverage | Competitor 1 | Competitor 2 | Priority |
|----------|--------------|--------------|--------------|----------|
| [Topic] | [Yes/No] | [Yes/No] | [Yes/No] | [High/Med/Low] |

### Recommendations
1. [Highest-impact action for knowledge graph positioning]
2. [Second action]
3. [Third action]

### Content Roadmap
- **Create next:** [Subtopic] — [Why this fills the biggest gap]
- **Update:** [Existing page] — [What to add/change]
- **Link:** [Page A] to [Page B] — [Anchor text suggestion]
```

## Knowledge Graph Building Strategy

### Phase 1: Foundation (Month 1)
- Identify your core topic and map all subtopics
- Create or update cornerstone content (3,000+ words, comprehensive)
- Implement hub-and-spoke internal linking
- Ensure consistent terminology across all content

### Phase 2: Expansion (Months 2-3)
- Create subtopic pages for each identified gap
- Build semantic bridges to adjacent topic areas
- Develop original frameworks or models
- Pursue guest contributions on authoritative sites

### Phase 3: Authority (Months 4-6)
- Conduct original research to create citable data
- Build expert network for quotes and co-citation
- Pursue industry directory and database listings
- Monitor and expand semantic coverage based on emerging subtopics

## Integration

This sub-skill feeds the Knowledge Graph dimension (10% weight) of the composite AEO Visibility Score. It has a multiplier effect on Citability (+5-15% indirect boost) and Brand Authority (+5-10% indirect boost) through improved topic positioning.

Strong knowledge graph positioning is a **long-term competitive moat** — it takes months to build but is extremely difficult for competitors to replicate quickly.
