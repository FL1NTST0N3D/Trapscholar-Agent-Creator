# Cross-Campaign Negative Keyword Strategy

## Command: /negatives cross-campaign

Prevent your own campaigns from competing with each other. Use negative keywords strategically to control which campaign serves each query, ensuring branded traffic goes to brand campaigns, non-branded to non-branded, and geographic campaigns stay in their lanes.

## Why Cross-Campaign Negatives Matter

When you run multiple campaigns targeting overlapping audiences, Google decides which campaign serves each query. That decision is based on Ad Rank — not your intent. This means your cheap brand campaign might lose a query to your expensive non-brand campaign, or your high-CPA top-of-funnel campaign might steal traffic from your efficient bottom-of-funnel campaign.

Cross-campaign negatives give you control. Instead of letting Google's auction dynamics decide, you explicitly route traffic to the right campaign using negative keywords as traffic signals.

Without cross-campaign negatives, you get:
- Brand terms triggering non-brand campaigns (paying 3-5x more per click than necessary)
- High-intent terms leaking into awareness campaigns (wasted budget on low-converting campaign settings)
- Geographic overlap (Phoenix campaign stealing Tucson queries)
- Funnel stage confusion (top-funnel campaign serving bottom-funnel queries with wrong landing pages)

## Cross-Campaign Strategy Patterns

### Pattern 1: Branded vs Non-Branded Separation

The most common and most impactful cross-campaign negative strategy.

**Setup:**
- Campaign A: "Brand" — targets branded keywords (your company name, product names, branded terms)
- Campaign B: "Non-Brand" — targets generic/category keywords

**Negatives needed:**
- Campaign B (Non-Brand): Add ALL brand terms as phrase match negatives
  - Your company name and variations
  - Your product names
  - Common misspellings of your brand
  - Your domain name
  - Your app name
  - Abbreviated versions of your brand

**Why:** Brand clicks are 60-80% cheaper than non-brand clicks. If a branded search term triggers your non-brand campaign, you pay non-brand CPCs for what should be a cheap branded click. Over a month, this can waste thousands.

**Example:**
```
Company: Acme CRM

Non-Brand Campaign negatives (phrase match):
"acme"
"acme crm"
"acmecrm"
"acme software"
"acme.com"
"acme app"
"acme pricing"
"acme login"
"acme support"
```

### Pattern 2: Geographic Campaign Isolation

When you run separate campaigns for different regions, cities, or territories.

**Setup:**
- Campaign A: "Phoenix" — targets Phoenix metro area
- Campaign B: "Tucson" — targets Tucson metro area
- Campaign C: "National" — targets rest of country

**Negatives needed:**
- Campaign A (Phoenix): Add Tucson city/area terms as phrase negatives
- Campaign B (Tucson): Add Phoenix city/area terms as phrase negatives
- Campaign C (National): Add ALL city-specific terms as phrase negatives

**Why:** Geographic campaigns have different budgets, bids, and landing pages. If Phoenix queries leak into the National campaign, they get the wrong landing page and wrong bid strategy.

**Example:**
```
Phoenix Campaign negatives:
"tucson"
"tucson az"
"sierra vista"
"green valley"
"oro valley"

Tucson Campaign negatives:
"phoenix"
"phoenix az"
"scottsdale"
"tempe"
"mesa"
"chandler"
"gilbert"
```

### Pattern 3: Funnel-Stage Separation

When you run different campaigns for different stages of the buyer journey.

**Setup:**
- Campaign A: "Awareness" — broad keywords, educational content, blog landing pages
- Campaign B: "Consideration" — comparison keywords, product pages
- Campaign C: "Decision" — high-intent keywords, pricing/demo pages

**Negatives needed:**
- Campaign A (Awareness): Add decision-stage terms as negatives
  - "pricing", "cost", "buy", "purchase", "demo", "trial", "sign up", "get started"
- Campaign C (Decision): Add awareness-stage terms as negatives
  - "what is", "how does", "guide", "tutorial", "tips", "learn about", "introduction"

**Why:** Awareness campaigns typically have lower bids and broader targeting. If a high-intent "buy now" query triggers your awareness campaign, the user sees educational content instead of a pricing page — killing your conversion rate.

### Pattern 4: Product/Service Line Separation

When you sell multiple products and run separate campaigns for each.

**Setup:**
- Campaign A: "CRM Software"
- Campaign B: "Email Marketing Software"
- Campaign C: "Project Management Software"

**Negatives needed:**
- Campaign A: Add Campaign B and C product terms as negatives
- Campaign B: Add Campaign A and C product terms as negatives
- Campaign C: Add Campaign A and B product terms as negatives

**Why:** If someone searches "email marketing software" and your CRM campaign triggers (because "software" is a shared keyword), they see a CRM ad — irrelevant, low CTR, low Quality Score, wasted click.

### Pattern 5: Match Type Tier Separation (Alpha/Beta Structure)

Advanced structure where you use negative exact match to control query routing between broad and exact match campaigns.

**Setup:**
- Campaign A (Alpha): Exact match keywords — your proven, converting terms
- Campaign B (Beta): Broad/phrase match keywords — your discovery/expansion terms

**Negatives needed:**
- Campaign B (Beta): Add ALL Campaign A exact match keywords as exact match negatives
- This forces known-good queries to always trigger the exact match campaign (higher Quality Score, better CPC)
- New queries that don't match any exact keyword flow to the broad/phrase campaign for discovery

**Why:** Exact match campaigns have higher Quality Scores and lower CPCs for known queries. Broad match campaigns are for finding NEW queries. Mixing them loses the efficiency advantage.

## Implementation Checklist

1. Map your campaign structure (what is each campaign's purpose?)
2. Identify overlap points (where could queries leak between campaigns?)
3. Create negative keyword lists for each separation pattern
4. Use shared negative keyword lists for efficiency (one list per separation pattern)
5. Test: run a search terms report after 7 days to verify traffic routing
6. Monitor: check monthly for new leakage terms

## Common Mistakes

- **Adding too many cross-campaign negatives**: Can create gaps where NO campaign serves a query. Always verify coverage.
- **Using wrong match type**: Broad negative in cross-campaign context can be too aggressive. Prefer phrase or exact.
- **Forgetting misspellings**: Brand negatives need to include common misspellings of your brand.
- **Static lists**: Cross-campaign negatives need updating as you add new keywords and campaigns.
- **Ignoring shared lists**: Managing cross-campaign negatives at the campaign level creates maintenance nightmares. Use shared lists.

## Usage

```bash
# Analyze cross-campaign overlap
/negatives cross-campaign

# Check brand vs non-brand separation
/negatives cross-campaign --type brand

# Check geographic isolation
/negatives cross-campaign --type geo

# Check funnel stage separation
/negatives cross-campaign --type funnel

# Generate cross-campaign negative lists
/negatives cross-campaign --generate-lists
```

## Integration with Other Skills

- Uses `/negatives conflict` to verify cross-campaign negatives don't block desired traffic
- Feeds into `/negatives report` for campaign structure analysis
- References `/negatives match-types` for match type selection in cross-campaign context
- May leverage `/negatives lists` for industry-standard cross-campaign patterns
