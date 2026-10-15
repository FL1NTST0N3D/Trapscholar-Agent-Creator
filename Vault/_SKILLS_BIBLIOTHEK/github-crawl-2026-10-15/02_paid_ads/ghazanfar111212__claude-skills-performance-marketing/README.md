# Claude Skills for Performance Marketers

25 Claude Skills for people who run paid media, build funnels and win clients for agencies.

Each skill is a folder with a `SKILL.md` file (and sometimes reference files) that teaches Claude how an experienced practitioner approaches a specific job: auditing a Google Ads account, structuring a Meta account, building a Sales Navigator search, writing a LinkedIn sequence, designing a landing page for paid traffic, and so on. Claude loads a skill automatically when your request matches it.

Built from five years of hands-on paid media work across Pakistan, MENA and APAC markets, plus US service-business verticals (dental, home services, hardscaping, healthcare SaaS).

## The skills

### Paid media and measurement

| Skill | What it does |
|---|---|
| [google-ads-expert](skills/google-ads-expert) | Campaign structure, bidding, PMax, Shopping, keywords, RSAs, troubleshooting and reporting |
| [meta-ads-expert](skills/meta-ads-expert) | Account structure, Advantage+, audiences, CAPI, attribution, creative testing and scaling |
| [google-tag-manager-expert](skills/google-tag-manager-expert) | Tags, triggers, dataLayer, GA4, consent mode, server-side tagging and debugging |
| [looker-studio-expert](skills/looker-studio-expert) | Client-ready dashboards, blended data, calculated fields, multi-currency reporting |

### Landing pages and conversion

| Skill | What it does |
|---|---|
| [landing-page-designer](skills/landing-page-designer) | Conversion structure for paid traffic pages, with vertical-specific templates |
| [landing-page-visual-standards](skills/landing-page-visual-standards) | A visual quality bar so pages don't look AI-generated: banned defaults, design systems, checklist |
| [design-qa](skills/design-qa) | Screenshot a built page at mobile and desktop widths, critique, fix and re-render (Claude Code) |

### Client acquisition and outbound

| Skill | What it does |
|---|---|
| [icp-filter-architect](skills/icp-filter-architect) | Turns a vague ICP into exact filters for Sales Navigator, Apollo, Clay and similar tools |
| [linkedin-outreach-architect](skills/linkedin-outreach-architect) | Designs LinkedIn sequences and writes connection notes and DMs for any ICP |
| [clay-enrichment-architect](skills/clay-enrichment-architect) | Clay table design: waterfall enrichment, Claygent columns, credit control, export |
| [outreach-message-critic](skills/outreach-message-critic) | Red-teams drafted outreach from the recipient's point of view before you send |
| [cold-email-outreach](skills/cold-email-outreach) | Cold email infrastructure, deliverability, list building, copy and sequences |
| [seo-client-outreach](skills/seo-client-outreach) | Landing SEO clients on LinkedIn with a free-audit hook |
| [linkedin-post-writer](skills/linkedin-post-writer) | LinkedIn posts that earn engagement from a target audience and sound human |
| [case-study-writer](skills/case-study-writer) | Problem-Action-Result case studies for pitches, landing pages and outreach |

### Agency strategy and operations

| Skill | What it does |
|---|---|
| [agency-positioning-expert](skills/agency-positioning-expert) | Niche selection, offer design, ICP definition, pricing and positioning statements |
| [chief-marketing-officer](skills/chief-marketing-officer) | Budget allocation, channel mix, marketing org design, measurement and board reporting |
| [email-marketing](skills/email-marketing) | Lifecycle strategy, deliverability, segmentation, flows and measurement |

### Automation and CRM

| Skill | What it does |
|---|---|
| [go-high-level-expert](skills/go-high-level-expert) | GoHighLevel pipelines, workflows, funnels, reputation, SaaS mode and integrations |
| [ghl-snapshot-builder](skills/ghl-snapshot-builder) | Industry-specific GHL snapshots packaged for resale |
| [n8n-workflow-expert](skills/n8n-workflow-expert) | n8n workflows: webhooks, API chaining, AI agents, error handling |

### Content and research

| Skill | What it does |
|---|---|
| [content-market-intelligence](skills/content-market-intelligence) | Finds underserved content demand, scores opportunities and builds a content plan |
| [instagram-content-creator](skills/instagram-content-creator) | Researches trends and gaps, then writes full Reels production packages |
| [youtube-gap-finder](skills/youtube-gap-finder) | Finds YouTube topics with real demand and weak supply |
| [youtube-video-ideation](skills/youtube-video-ideation) | Turns a niche into packaged video ideas with titles, thumbnails and hooks |

## Installing

**Claude apps (web, desktop, mobile):** zip a skill folder (for example `google-ads-expert/`) and upload it in the Skills section of Claude's settings. Skills must be enabled for your account.

**Claude Code:** copy skill folders into `~/.claude/skills/` to use them everywhere, or into `.claude/skills/` inside a project to use them only there.

```bash
git clone https://github.com/ghazanfar111212/claude-skills-performance-marketing.git
cp -r claude-skills-performance-marketing/skills/* ~/.claude/skills/
```

**Claude API:** upload skills through the Skills API and attach them to your requests. See Anthropic's documentation for the current endpoints.

## Using them

You don't call skills by name. Ask normally and Claude picks the right one:

- "Audit the structure of this Google Ads account" loads `google-ads-expert`
- "Build me a Sales Navigator search for dental practice owners in Texas" loads `icp-filter-architect`
- "Would a founder actually reply to this DM?" loads `outreach-message-critic`

Some skills work best together. For landing pages, use `landing-page-designer` for structure and `landing-page-visual-standards` for the visual bar. For outbound, run `icp-filter-architect`, then `linkedin-outreach-architect`, then `outreach-message-critic`.

A few skills mention companion skills that are not in this repo (for example `frontend-design` or `swipe-file`). They work fine without them.

## Contributing

Issues and pull requests are welcome, especially platform changes that make advice out of date. Paid media platforms change often, so please include a source when correcting something.

## License

MIT
