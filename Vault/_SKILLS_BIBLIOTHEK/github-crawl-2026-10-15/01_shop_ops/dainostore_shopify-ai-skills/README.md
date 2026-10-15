# Shopify AI Skills for Claude Code

**15 production-tested Claude Code skills for Shopify store automation.**

Built from real operations running across multiple Shopify stores. Every skill is a structured methodology file that Claude Code reads and executes — turning hours of manual work into minutes.

## Quick Start

```bash
# 1. Clone this repo
git clone https://github.com/dainostore/shopify-ai-skills.git
cd shopify-ai-skills

# 2. Open Claude Code in this directory
claude

# 3. Run any skill
/store-health-check
/product-research "wireless earbuds under $30"
/margin-analyzer
```

Or copy the skills into any existing project:
```bash
cp -r shopify-ai-skills/.claude/commands/* your-project/.claude/commands/
```

## The 15 Skills

### Pillar 1: Product Intelligence

| Skill | What it does |
|-------|-------------|
| `/product-research` | Discover and validate product opportunities using market signals, trend scoring, and margin analysis |
| `/product-launcher` | Full product launch execution — listing, pricing, inventory, and marketing in one pass |
| `/competitor-spy` | Analyze competitor products, pricing strategy, and positioning gaps |

### Pillar 2: Pricing & Margins

| Skill | What it does |
|-------|-------------|
| `/margin-analyzer` | Audit margins across your entire catalog, flag underperformers, and find profit leaks |
| `/pricing-optimizer` | Generate data-driven pricing recommendations based on margins, velocity, and competition |
| `/bulk-price-update` | Batch pricing operations with safety rails — preview before apply, rollback support |

### Pillar 3: Order & Fulfillment

| Skill | What it does |
|-------|-------------|
| `/order-autopilot` | Automated order triage — prioritize, flag issues, and batch-fulfill ready orders |
| `/refund-handler` | Smart refund processing with reason analysis and customer retention offers |
| `/supplier-scorecard` | Evaluate and rank suppliers on reliability, cost, speed, and quality |

### Pillar 4: Store Analytics

| Skill | What it does |
|-------|-------------|
| `/store-health-check` | Complete store diagnostic across 6 layers — revenue, conversion, inventory, customers, fulfillment, and marketing |
| `/sales-dashboard` | Revenue and performance analytics with period comparison and trend detection |
| `/customer-segments` | RFM segmentation — identify champions, at-risk, and lost customers with action plans |

### Pillar 5: Marketing & Content

| Skill | What it does |
|-------|-------------|
| `/marketing-copy` | Generate product descriptions, ad copy, and social posts from product data |
| `/campaign-builder` | Build email campaigns with audience targeting, subject line variants, and send scheduling |
| `/content-engine` | Multi-channel content generation — blog posts, social captions, email sequences from one brief |

## How the Flywheel Works

```
Product Research → finds what to sell
        ↓
Product Launcher → gets it listed fast
        ↓
Pricing Optimizer → sets the right price
        ↓
Marketing Copy → drives traffic
        ↓
Sales Dashboard → shows what's working
        ↓
Customer Segments → reveals who's buying
        ↓
Competitor Spy → sharpens positioning
        ↓
Margin Analyzer → protects profits
        ↓
(back to Product Research — each cycle is smarter)
```

Every skill feeds context to the next. Your product research informs your pricing. Your sales data sharpens your marketing. Your customer segments improve your product research. **Each cycle compounds.**

## How It Works

Each skill is a structured markdown file that Claude Code reads and executes. The skills contain:

- **Named frameworks** (TREND, SELL, OPTIMAL, SHIP, SCORE, etc.) — structured decision models
- **Scoring rubrics** — specific thresholds and classification rules
- **API call patterns** — ready-to-use with the Shopify Admin API
- **Output templates** — every run produces a formatted, actionable report

### Connecting to your Shopify store

These skills work with the **Shopify Admin API** out of the box. When you run a skill for the first time, Claude Code will ask for your store URL and credentials — no config files needed.

Both auth methods are supported:
- **Access token** (`shpat_xxx`) — recommended for new custom apps
- **API key + secret** — for legacy private apps (Basic Auth)

#### Required API Scopes

Your app must have the following scopes enabled in **Shopify Admin → Settings → Apps → Develop apps → Configuration → Admin API integration**:

| Scope | Used for |
|-------|----------|
| `read_products` | Fetching product data (all product-related skills) |
| `write_products` | Updating product descriptions, prices, and listings |
| `read_orders` | Order analytics, sales dashboards, refund processing |
| `write_orders` | Order fulfillment and refund execution |
| `read_customers` | Customer segmentation and campaign targeting |
| `read_inventory` | Inventory levels for stock checks and health diagnostics |
| `write_inventory` | Inventory adjustments during product launches |

**How to set up:**
1. Go to **Shopify Admin** → **Settings** → **Apps and sales channels** → **Develop apps**
2. Click your app (or create one)
3. Go to **Configuration** → **Admin API integration**
4. Enable all required scopes listed above
5. Click **Save** → **Install** the app
6. Copy the **Admin API access token** (`shpat_xxx`) from the **API credentials** tab

> **Note:** If you update scopes on an existing app, you must re-install it and copy the new access token. The old token will not have the new permissions.

### Skill Reference

Each skill maps to Shopify Admin API resources:

| Category | Shopify API | Used by |
|----------|-------------|---------|
| Products | `/admin/api/products.json` | Product Research, Product Launcher, Competitor Spy |
| Orders | `/admin/api/orders.json` | Order Autopilot, Refund Handler, Sales Dashboard |
| Customers | `/admin/api/customers.json` | Customer Segments, Campaign Builder |
| Inventory | `/admin/api/inventory_levels.json` | Store Health Check, Product Launcher |
| Analytics | Computed from orders + products data | Sales Dashboard, Store Health Check, Margin Analyzer |
| Variants | `/admin/api/variants/{id}.json` | Pricing Optimizer, Bulk Price Update |
| Inventory Items | `/admin/api/inventory_items.json` | Margin Analyzer, Competitor Spy |

> **Want the full autopilot experience?** [DainoStore](https://dainostore.com) wraps these skills into 42 autonomous tools with AI agents that run on autopilot — auto-pricing, auto-fulfillment, smart refunds, and more. The skills you see here are the open-source methodology behind it.

## Requirements

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed
- A Shopify store with Admin API access

## License

MIT — use these however you want.
