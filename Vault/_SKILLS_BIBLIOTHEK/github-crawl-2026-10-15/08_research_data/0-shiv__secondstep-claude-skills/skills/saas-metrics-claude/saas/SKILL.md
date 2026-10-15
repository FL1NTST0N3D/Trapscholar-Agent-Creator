# SaaS Metrics — Root Skill

> Every SaaS metric, calculated and benchmarked. MRR, ARR, churn, LTV, CAC, NRR, payback period, magic number & more.

## Trigger
`/saas` followed by a sub-command: `mrr`, `churn`, `ltv-cac`, `nrr`, `cohort`, `unit-economics`, `benchmarks`, `forecast`, `report`.

## Overview

This is the root skill for the SaaS Metrics suite. It routes to 9 specialized sub-skills that cover every metric a SaaS operator needs to track, calculate, and benchmark.

## Sub-Skills

| Command | Skill | What It Does |
|---|---|---|
| `/saas mrr` | saas-mrr | MRR movements waterfall, ARR, growth rate |
| `/saas churn` | saas-churn | Customer & revenue churn with benchmarks |
| `/saas ltv-cac` | saas-ltv-cac | LTV:CAC ratio, payback period |
| `/saas nrr` | saas-nrr | Net & Gross Revenue Retention |
| `/saas cohort` | saas-cohort | Cohort retention curves & heatmaps |
| `/saas unit-economics` | saas-unit-economics | ARPU, margins, Rule of 40 |
| `/saas benchmarks` | saas-benchmarks | Stage-specific industry benchmarks |
| `/saas forecast` | saas-forecast | Revenue forecasting & scenarios |
| `/saas report` | saas-report | Full dashboard report |

## How to Use

1. Provide your data (CSV, JSON, or describe it inline)
2. Run a command: `/saas mrr` with your monthly subscription data
3. Get calculations, benchmarks, and actionable insights

## Data Format

The skill accepts data in these formats:
- **Inline**: Describe your numbers in natural language
- **CSV**: Upload or paste a CSV with columns like `customer_id, mrr, start_date, end_date`
- **JSON**: Structured data with `customers`, `revenue`, `dates` fields

## Agents

Three specialized agents support deeper analysis:
- **metrics-analyst** — Calculates all metrics from raw data
- **benchmark-advisor** — Compares your metrics to industry standards
- **forecast-modeler** — Builds revenue forecasts with scenarios

## Python Scripts

For programmatic calculation:
- `scripts/mrr_calculator.py` — MRR waterfall engine
- `scripts/churn_analyzer.py` — Multi-dimensional churn analysis
- `scripts/ltv_cac_calculator.py` — LTV, CAC, and payback computations
