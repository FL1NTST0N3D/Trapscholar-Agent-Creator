# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2026-03-15

### Added
- Main skill router (`SKILL.md`) with `/ga4` command routing
- 10 sub-skills covering all GA4 audit dimensions:
  - Data Streams — stream config, enhanced measurement, filters
  - Events — event coverage, naming conventions, parameter validation
  - Conversions — conversion setup, counting method, Google Ads import
  - Audiences — audience creation, predictive audiences, Ads export
  - Attribution — model selection, lookback windows, conversion paths
  - E-commerce — purchase funnel events, revenue tracking
  - Custom Dimensions — dimension registration, quota usage
  - Reporting — report configuration, exploration setup
  - Integrations — Google product linking (Ads, Search Console, BigQuery)
  - Report — final audit report compilation with Health Score
- 4 agent definitions:
  - Audit Orchestrator — full audit flow coordinator
  - Event Validator — event naming and parameter checks
  - E-commerce Debugger — e-commerce funnel debugging
  - Report Generator — report compilation and formatting
- Python utility scripts:
  - `health_score.py` — weighted Health Score calculator (0-100)
  - `event_validator.py` — event naming convention validator
  - `report_generator.py` — audit report generator
- Reference documentation:
  - GA4 event reference (all event categories and parameters)
  - Audit methodology
  - Common GA4 misconfigurations
- Installation and uninstallation scripts
- Project documentation (README, CLAUDE.md, CONTRIBUTING.md)
