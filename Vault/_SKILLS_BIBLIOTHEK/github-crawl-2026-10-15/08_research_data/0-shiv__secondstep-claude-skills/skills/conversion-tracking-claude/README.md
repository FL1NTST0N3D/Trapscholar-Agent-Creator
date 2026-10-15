# Conversion Tracking Claude

**Broken conversion tracking = flying blind. This skill validates your entire tracking stack across Google, Meta, LinkedIn, TikTok & server-side.**

---

## Why This Exists

- **41% of conversion tracking implementations have errors** — misconfigured tags, missing events, broken data layers
- **Broken tracking wastes an average of $2,400/mo** in misattributed ad spend per advertiser
- **67% of advertisers don't use Enhanced Conversions** — leaving 15-30% of conversion data on the table
- **Cross-platform attribution gaps** cause duplicate counting, inflated ROAS, and bad budget decisions

This Claude Code skill audits, validates, and fixes conversion tracking across every major ad platform — from basic pixel installation to server-side implementations and offline conversion imports.

---

## Tracking Health Score (0-100)

Every audit generates a **Tracking Health Score** from 0 to 100:

| Score | Rating | Meaning |
|-------|--------|---------|
| 90-100 | Excellent | Full tracking coverage, EC active, server-side in place |
| 70-89 | Good | Core tracking works, minor gaps in advanced features |
| 50-69 | Needs Work | Significant gaps — missing EC, no server-side, event issues |
| 30-49 | Poor | Major tracking failures — lost conversion data |
| 0-29 | Critical | Tracking is fundamentally broken or missing |

---

## Commands

| Command | Description |
|---------|-------------|
| `/track audit` | Full cross-platform tracking audit with Health Score |
| `/track google-tag` | Validate Google Tag (gtag.js) installation and conversion actions |
| `/track ec` | Audit Enhanced Conversions (Web + Leads/EC4L) |
| `/track server-side` | Validate server-side GTM (sGTM) setup |
| `/track offline` | Check offline conversion import pipeline |
| `/track meta-pixel` | Audit Meta Pixel installation and events |
| `/track capi` | Validate Meta Conversions API and EMQ score |
| `/track linkedin` | Check LinkedIn Insight Tag and conversions |
| `/track tiktok` | Audit TikTok Pixel and Events API |
| `/track attribution` | Analyze attribution model setup across platforms |
| `/track report` | Generate comprehensive tracking audit report |

---

## Quick Start

```bash
# Install
git clone https://github.com/0-shiv/conversion-tracking-claude.git
cd conversion-tracking-claude
chmod +x install.sh && ./install.sh

# Run a full audit
claude "/track audit"

# Check specific platform
claude "/track google-tag"
claude "/track meta-pixel"
claude "/track ec"
```

---

## What Gets Checked

### Google Ads
- Google Tag (gtag.js) present on all pages
- Conversion actions configured correctly (counting, value, window)
- Enhanced Conversions for Web (user data hashing, diagnostic status)
- Enhanced Conversions for Leads / EC4L (GCLID capture, offline import)
- Server-side GTM container health
- Offline conversion import pipeline

### Meta Ads
- Meta Pixel firing on all pages
- Standard events configured (PageView, ViewContent, AddToCart, Purchase, Lead)
- Custom events and parameters
- Conversions API (CAPI) active with EMQ 6.0+
- Event deduplication between Pixel and CAPI

### LinkedIn Ads
- Insight Tag installation
- Conversion tracking (event-specific and URL-based)
- LinkedIn CAPI setup

### TikTok Ads
- TikTok Pixel installation
- Standard events configured
- Events API setup
- Advanced matching parameters

### Cross-Platform
- Attribution model analysis per platform
- Cross-platform deduplication
- Conversion window alignment
- Data freshness and latency checks

---

## Repository Structure

```
conversion-tracking-claude/
├── SKILL.md                          # Main skill — command routing & orchestration
├── README.md                         # This file
├── CLAUDE.md                         # Claude Code project instructions
├── CONTRIBUTING.md                   # Contribution guidelines
├── CHANGELOG.md                      # Version history
├── LICENSE                           # MIT License
├── install.sh                        # Installation script
├── uninstall.sh                      # Uninstallation script
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Git ignore rules
├── tracking/                         # Core tracking logic and validators
│   └── tracking_config.yaml          # Platform configuration
├── skills/                           # 10 sub-skills
│   ├── track-google-tag/SKILL.md
│   ├── track-enhanced-conversions/SKILL.md
│   ├── track-server-side/SKILL.md
│   ├── track-offline-import/SKILL.md
│   ├── track-meta-pixel/SKILL.md
│   ├── track-meta-capi/SKILL.md
│   ├── track-linkedin-insight/SKILL.md
│   ├── track-tiktok-pixel/SKILL.md
│   ├── track-attribution/SKILL.md
│   └── track-report/SKILL.md
├── agents/                           # 4 specialized agents
│   ├── audit_orchestrator.md
│   ├── tag_inspector.md
│   ├── data_quality_agent.md
│   └── report_generator.md
├── scripts/                          # 4 Python validation scripts
│   ├── tag_validator.py
│   ├── ec_checker.py
│   ├── pixel_auditor.py
│   └── generate_tracking_report.py
├── templates/                        # Report and config templates
│   ├── audit_report.md
│   ├── tracking_checklist.md
│   └── platform_config.yaml
├── docs/                             # 5 documentation files
│   ├── google-tracking-guide.md
│   ├── meta-tracking-guide.md
│   ├── server-side-guide.md
│   ├── attribution-models.md
│   └── troubleshooting.md
└── assets/                           # Static assets
    └── .gitkeep
```

---

## Requirements

- Claude Code CLI
- Python 3.8+ (for validation scripts)
- Access to Google Ads, Meta Business Manager, LinkedIn Campaign Manager, or TikTok Ads Manager as needed
- Google Tag Manager access (recommended)

---

## License

MIT License - Shivendra Rawat 2026

---

Built for [Second Step](https://getsecondstep.com) | Conversion tracking expertise from $2M+ in managed ad spend
