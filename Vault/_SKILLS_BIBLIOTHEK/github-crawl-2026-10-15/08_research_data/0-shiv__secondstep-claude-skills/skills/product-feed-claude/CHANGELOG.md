# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-15

### Added
- Master orchestrator skill (SKILL.md) routing 8 `/feed` commands
- Sub-skill: Feed Title Optimization (`/feed titles`) — category-specific title formulas, scoring, templates
- Sub-skill: Feed Description (`/feed descriptions`) — keyword-rich copy, policy compliance, templates
- Sub-skill: Feed Images (`/feed images`) — image compliance audit, size/format/content validation
- Sub-skill: Feed Attributes (`/feed attributes`) — required + recommended attribute validation, GTIN checks
- Sub-skill: Feed Custom Labels (`/feed labels`) — custom_label_0-4 strategy for campaign segmentation
- Sub-skill: Feed Disapprovals (`/feed disapprovals`) — root cause diagnosis, fix plans, prevention
- Sub-skill: Feed Supplemental (`/feed supplemental`) — supplemental feed setup for overrides and enrichment
- Sub-skill: Feed Report (`/feed report`) — comprehensive health report with weighted scoring
- Agent: Feed Quality (agents/feed-quality.md) — title/description/image quality analysis
- Agent: Feed Compliance (agents/feed-compliance.md) — policy violation and disapproval specialist
- Script: feed_analyzer.py — CSV/TSV feed parser with product-level scoring
- Script: feed_report.py — formatted health report generator with trend tracking
- Documentation: INSTALLATION.md, COMMANDS.md, SCORING.md
- Configuration: CLAUDE.md, .gitignore, LICENSE (MIT), install.sh, uninstall.sh
- Weighted scoring model: Title (30%), Attributes (25%), Images (20%), Description (15%), Accuracy (10%)
- Grade scale: A (90-100) through F (0-49)
- GTIN check-digit validation (UPC-12, EAN-13, GTIN-14)
