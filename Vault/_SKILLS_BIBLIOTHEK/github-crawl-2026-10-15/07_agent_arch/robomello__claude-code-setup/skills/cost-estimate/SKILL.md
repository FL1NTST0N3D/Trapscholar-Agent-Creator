---
name: cost-estimate
description: >
  This skill should be used when the user asks "cost estimate", "ROI",
  "how much code", "productivity report", "lines of code",
  "how much did Claude write", "developer cost comparison", "cost savings",
  "value of Claude", or "cost-estimate". Analyzes Claude Code productivity
  and compares against senior developer benchmarks.
  DO NOT trigger on: general pricing questions about Claude plans,
  API token cost calculations, questions about other AI tools' pricing.
---

# Claude Code ROI Estimator

Analyze Claude Code productivity and compare against senior developer benchmarks.

## Instructions

Run `python3 ~/commander/projects/cost_estimate.py` with the appropriate flags.

### Default: Full report with verbose breakdown
```bash
python3 ~/commander/projects/cost_estimate.py -v
```

### Specific time period
```bash
python3 ~/commander/projects/cost_estimate.py --days 30 -v
python3 ~/commander/projects/cost_estimate.py --days 7 -v
```

### Specific repo
```bash
python3 ~/commander/projects/cost_estimate.py --repo ~/Internal App -v
```

### JSON output (for sharing, piping, dashboards)
```bash
python3 ~/commander/projects/cost_estimate.py --json
```

### CSV output (for spreadsheets)
```bash
python3 ~/commander/projects/cost_estimate.py --csv
```

### Custom benchmarks
```bash
python3 ~/commander/projects/cost_estimate.py --senior-rate 120 --senior-loc 40 --subscription 200 -v
```

### Faster report (skip session JSONL parsing)
```bash
python3 ~/commander/projects/cost_estimate.py --no-sessions -v
```

After running, present the output to the user. If they ask to share it, run with `--json` and save to a file.

## What It Analyzes

1. **Git history**: All repos under ~/ for Claude-authored commits (`Co-Authored-By` tag)
2. **Lines of code**: Insertions, deletions, net LOC, files changed per repo
3. **Session time**: JSONL session files with 30-min idle-gap filtering
4. **Senior dev estimate**: Equivalent human hours at 50 LOC/hr (configurable)
5. **Cost comparison**: Subscription vs senior dev hourly rate vs API pay-per-token
6. **Language breakdown**: File types touched (`-v` flag)

## Benchmarks

| Benchmark | Default | Flag | Rationale |
|-----------|---------|------|-----------|
| Senior dev LOC/hr | 50 | `--senior-loc` | Production-quality code (not prototype). Industry average for reviewed, tested code. |
| Senior dev rate | $100/hr | `--senior-rate` | US market average for senior software engineers (2026). |
| Subscription | $200/mo | `--subscription` | Claude Max plan cost. |

## Interpreting Results

- **Speed multiplier 2.5x** = Claude produced code 2.5x faster than a senior dev would at 50 LOC/hr
- **ROI 5.0x** = The code Claude produced would have cost 5x more if done by a senior dev at $100/hr
- **ROI < 1.0** = Claude cost more than a human dev would have (rare for active usage)

## Data Sources

- Git repos: Auto-discovered under ~/ (excludes .nvm, node_modules, ai-toolkit, gpu-burn)
- Session data: `~/.claude/projects/*/*.jsonl`
- Stats cache: `~/.claude/stats-cache.json`
- Idle gap: 30 min (gaps > this excluded from active time)

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| No Claude-authored commits found | Missing `Co-Authored-By: Claude` in commit messages | Ensure git commits include the Co-Authored-By tag |
| Zero hours despite commits | Ran with `--no-sessions` | Re-run without `--no-sessions` to include time analysis |
| Files not found | Missing session data | Verify `~/.claude/projects/*.jsonl` files exist |
| Stale results | Cached data | Delete `~/.claude/stats-cache.json` and re-run |
