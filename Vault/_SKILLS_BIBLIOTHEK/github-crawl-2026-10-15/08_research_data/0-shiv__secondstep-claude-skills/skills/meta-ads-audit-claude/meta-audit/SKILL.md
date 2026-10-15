# Meta Ads Audit — Master Orchestrator

## Skill Definition

This is the master skill for running comprehensive Meta (Facebook/Instagram) Ads audits. It routes commands to specialized sub-skills, coordinates parallel agents, and produces a unified health score.

## Command Routing

| Command | Routes To | Description |
|---------|-----------|-------------|
| `/meta audit` | All sub-skills | Full 150+ point audit |
| `/meta pixel` | `meta-pixel-health` | Pixel & event tracking |
| `/meta capi` | `meta-capi-check` | Conversions API validation |
| `/meta creative` | `meta-creative-fatigue` | Creative fatigue & diversity |
| `/meta audiences` | `meta-audience-overlap` | Audience overlap & strategy |
| `/meta budget` | `meta-budget-optimization` | Budget & bidding health |
| `/meta advantage` | `meta-advantage-plus` | Advantage+ configuration |
| `/meta copy` | `meta-ad-copy` | Ad copy quality scoring |
| `/meta placements` | `meta-placements` | Placement analysis |
| `/meta report` | `meta-report` | Report generation |

## Orchestration Flow

When `/meta audit` is triggered, the following orchestration runs:

### Phase 1: Data Collection (Parallel)
```
┌─────────────────────────────────────────────────┐
│                DATA INGESTION                    │
│                                                  │
│  1. Parse Meta Ads Manager CSV/JSON export       │
│  2. Extract campaign structure (Campaign →       │
│     Ad Set → Ad hierarchy)                       │
│  3. Identify date range and account currency     │
│  4. Load industry benchmarks for comparison      │
└─────────────────────────────────────────────────┘
```

### Phase 2: Parallel Agent Execution
Five agents run simultaneously to maximize speed:

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  TRACKING    │  │  CREATIVE    │  │  AUDIENCE     │
│  AGENT       │  │  AGENT       │  │  AGENT        │
│              │  │              │  │               │
│  • Pixel     │  │  • Fatigue   │  │  • Overlap    │
│  • CAPI      │  │  • Copy      │  │  • Lookalikes │
│  • Events    │  │  • Formats   │  │  • Exclusions │
└──────┬───────┘  └──────┬───────┘  └──────┬────────┘
       │                 │                  │
┌──────┴───────┐  ┌──────┴───────┐         │
│  BUDGET      │  │  REPORTING   │         │
│  AGENT       │  │  AGENT       │◄────────┘
│              │  │              │
│  • CBO/ABO   │  │  • Scores    │
│  • Learning  │  │  • Findings  │
│  • Advantage+│  │  • Actions   │
└──────────────┘  └──────────────┘
```

### Phase 3: Score Calculation
Each dimension produces a sub-score (0-100). The composite Meta Ads Health Score is calculated using weighted averages:

| Dimension | Weight | Sub-skill |
|-----------|--------|-----------|
| Pixel & Tracking | 20% | meta-pixel-health |
| Conversions API | 15% | meta-capi-check |
| Creative Health | 20% | meta-creative-fatigue + meta-ad-copy |
| Audience Strategy | 15% | meta-audience-overlap |
| Budget & Bidding | 10% | meta-budget-optimization |
| Advantage+ Config | 10% | meta-advantage-plus |
| Ad Copy & Placements | 10% | meta-ad-copy + meta-placements |

### Phase 4: Report Generation
The reporting agent compiles all findings into a structured report with:
- Executive summary with health score
- Dimension-by-dimension breakdown
- Top 10 critical findings
- Prioritized action plan (Quick Wins / Medium-term / Strategic)
- Industry benchmark comparison

## Meta Ads Industry Benchmarks (2025-2026)

These benchmarks are used as comparison baselines throughout the audit:

| Industry | CPM | CTR | CPC | Conv Rate | ROAS Target |
|----------|-----|-----|-----|-----------|-------------|
| E-commerce | $11.20 | 1.32% | $0.85 | 3.26% | 4.0x |
| Real Estate | $8.35 | 0.98% | $0.85 | 2.88% | 3.0x |
| Finance | $13.50 | 0.56% | $2.41 | 4.11% | 5.0x |
| Healthcare | $7.86 | 0.83% | $0.95 | 3.54% | 3.5x |
| Education | $6.73 | 1.05% | $0.64 | 5.62% | 4.0x |
| SaaS/Tech | $15.20 | 0.78% | $1.95 | 2.31% | 5.0x |
| Travel/Hospitality | $7.50 | 1.15% | $0.65 | 2.95% | 6.0x |
| Automotive | $9.80 | 0.80% | $1.22 | 2.14% | 3.5x |
| Retail | $10.45 | 1.21% | $0.86 | 3.05% | 3.5x |
| B2B Services | $14.80 | 0.46% | $3.22 | 2.62% | 4.0x |

## Meta-Specific Quality Signals

### Pixel Health Thresholds
- **Event Match Quality (EMQ)**: Target 6.0+ out of 10
- **Event Deduplication Rate**: Should be < 5% duplicate events
- **PageView to Purchase Funnel Drop**: Normal is 95%+ drop; flag if > 99.5%
- **Custom Event Coverage**: At least 3 custom events beyond standard 7

### Creative Performance Signals
- **Frequency Cap (Prospecting)**: Alert if > 3.0 in 7 days
- **Frequency Cap (Retargeting)**: Alert if > 5.0 in 7 days
- **CTR Decline Threshold**: Flag if CTR drops > 20% from first 3 days
- **Creative Format Mix**: Minimum 3 formats active (static, video, carousel)
- **Video Thumbstop Rate**: Target > 25% (3-second video plays / impressions)

### Audience Health Signals
- **Overlap Threshold**: Flag audience pairs with > 30% overlap
- **Audience Size (Prospecting)**: Warning if < 500K or > 50M
- **Lookalike Source Size**: Minimum 1,000 source audience; optimal 5,000-50,000
- **Custom Audience Refresh**: Flag if not updated in > 30 days

### Budget & Delivery Signals
- **Learning Phase**: Need 50 optimization events per ad set per week
- **Budget Utilization**: Flag if < 70% of daily budget is spent
- **CBO Distribution**: Flag if any ad set gets < 10% of campaign budget
- **Bid Cap Usage**: Warn if bid cap is set but no cost cap comparison tested

## Data Input Formats

The skill accepts data in these formats:
1. **Meta Ads Manager CSV Export** — Campaign, Ad Set, and Ad level reports
2. **Meta Marketing API JSON** — Raw API response data
3. **Meta Business Suite Export** — Business-level performance data
4. **Meta Events Manager Export** — Pixel and CAPI event data
5. **Manual Data Entry** — User provides key metrics in conversation

## Output Format

All audit results follow this structure:
```
## [Dimension Name] Audit Results

**Score: XX/100** (Grade: X)

### Critical Findings (P0)
- [Finding with specific data points]

### High Priority (P1)
- [Finding with specific data points]

### Medium Priority (P2)
- [Finding with specific data points]

### Recommendations
1. [Specific action item with expected impact]
2. [Specific action item with expected impact]
```

## Error Handling

- If data is incomplete, the skill will audit available dimensions and note gaps
- If no data is provided, the skill will generate a checklist-based self-audit
- If API access is unavailable, the skill falls back to CSV/manual data analysis
