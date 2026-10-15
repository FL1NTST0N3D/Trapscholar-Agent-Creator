# claude-evals

**Native eval harness for Claude Agent SDK workflows.** Built by [Tribe AI](https://tribe.ai).

Every enterprise team building Claude-powered workflows hits the same wall: *"how do we know if a model upgrade broke something, and how do we find the cheapest model that's still good enough?"* No existing open-source tool answers this for Claude Agent SDK workflows specifically. `claude-evals` fills that gap.

## What makes this different

- **Native Claude Agent SDK integration** — hooks into `PreToolUse`, `PostToolUse`, and `SubagentStop` lifecycle events, not just the final output
- **Evaluates agentic behavior** — tool selection, multi-step task completion, context retention, cost efficiency
- **Ships with a real golden dataset** — 50 calibrated test cases for contract review / document intelligence
- **Implements Anthropic's published eval patterns** — deterministic graders, LLM-as-judge, and human review queue from ["Demystifying Evals for AI Agents"](https://www.anthropic.com/engineering/evaluating-ai-agents)

## Quick Start

```bash
pip install claude-evals
export ANTHROPIC_API_KEY=your-key

# Run the full eval suite
claude-evals run --suite datasets/contract-review --model claude-sonnet-4-6

# Run a specific category
claude-evals run --suite datasets/contract-review --category clause_extraction

# Compare two runs for regressions
claude-evals compare --baseline ./results/baseline --candidate ./results/new-run --fail-on high
```

### From Python

```python
import asyncio
from claude_evals.runner import EvalRunner
from claude_evals.report.terminal import print_terminal_report

async def main():
    runner = EvalRunner(
        suite_path="datasets/contract-review",
        model="claude-sonnet-4-6",
    )
    run = await runner.run()
    print_terminal_report(run)

asyncio.run(main())
```

## The Golden Dataset

The reference dataset covers **contract review / document intelligence** — the most common enterprise AI use case. It includes 50 test cases across 5 categories, built from 10 realistic source contracts:

| Category | Cases | Grader | What it tests |
|----------|-------|--------|---------------|
| Clause Extraction | 20 | Deterministic | Find and extract specific clauses verbatim |
| Single-Term Review | 15 | LLM Judge | Answer interpretive questions about contract terms |
| Multi-Term Reasoning | 10 | LLM Judge | Synthesize information across multiple sections |
| Risk Classification | 5 | Deterministic | Classify clauses as standard/elevated/high risk |
| Missing Clause Detection | 5 | Deterministic | Identify which standard clauses are absent |

Source contracts include mutual and one-way NDAs, enterprise and startup SaaS agreements, professional services agreements, employment contracts, a complex MSA, and a software license. Each is 800-2,000 words of realistic but original legal text.

### Extending the dataset

Add your own test cases by creating JSON files in `datasets/contract-review/cases/`:

```json
{
    "id": "ce-021",
    "category": "clause_extraction",
    "description": "Extract the force majeure clause",
    "contract_path": "contracts/your-contract.txt",
    "prompt": "Extract the force majeure clause verbatim.",
    "expected_output": {
        "clause_text": "Neither party shall be liable for..."
    },
    "grader_type": "deterministic",
    "grader_config": {
        "check_type": "clause_present",
        "field": "clause_text",
        "partial_credit": true,
        "similarity_threshold": 0.6
    },
    "difficulty": "medium",
    "tags": ["force-majeure"]
}
```

Validate your dataset:

```bash
claude-evals validate-dataset --dataset datasets/contract-review
```

## Grader Types

### Deterministic

Fastest, cheapest, most reliable. Use whenever the correct answer can be verified programmatically.

- **exact_match** — output equals expected string
- **contains** — output contains expected substring
- **clause_present** — extracted clause matches expected text (with partial credit via string similarity)
- **classification** — output is the correct class (e.g., risk level)
- **clause_list_match** — F1 score on set comparison (for missing clause detection)
- **json_field_match** — specific JSON field matches expected value
- **regex** — output matches a pattern
- **not_contains** — hallucination check (output must NOT contain forbidden strings)

### LLM Judge

For subjective tasks where deterministic checks can't capture quality. Uses Claude Sonnet as the judge with:

- Structured rubric with weighted criteria
- Reference-based scoring (ground truth always included)
- Variance reduction: runs twice, takes median of 3 if scores differ by >0.2
- Random delimiters to prevent prompt injection

### Human Review Queue (v0.2)

Exports uncertain cases to JSONL for human review when the LLM judge score is ambiguous (0.4-0.6) or has high variance.

## CI Integration

Add to your GitHub Actions workflow:

```yaml
- name: Run eval suite
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
  run: |
    claude-evals run \
      --suite datasets/contract-review \
      --model claude-sonnet-4-6 \
      --output ./eval-results/candidate

- name: Regression check
  run: |
    claude-evals compare \
      --baseline ./eval-results/baseline \
      --candidate ./eval-results/candidate \
      --fail-on high
```

See `.github/workflows/ci.yml` for a complete workflow with baseline management and artifact caching.

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | All tasks passed (or no regressions found) |
| 1 | Some tasks failed (or HIGH/CRITICAL regressions) |
| 2 | Suite error (agent crashed, API error, budget exceeded) |
| 3 | Dataset validation error |

## CLI Commands

```bash
# Run eval suite
claude-evals run --suite <path> --model <model> [--output <dir>] [--category <cat>] [--runs <k>]

# Compare two runs
claude-evals compare --baseline <path> --candidate <path> [--fail-on <severity>]

# Validate dataset
claude-evals validate-dataset --dataset <path>

# Show previous results
claude-evals show --run <path> [--format terminal|json|markdown]
```

## Regression Detection

The regression detector compares two eval runs and classifies changes:

| Severity | Trigger | Recommendation |
|----------|---------|----------------|
| CRITICAL | >20% of tasks regressed, or critical-tagged task failed | **Block** deployment |
| HIGH | >10% regressed, or hard task went pass→fail | **Review** required |
| MEDIUM | 5-10% regressed | **Review** recommended |
| LOW | <5% regressed | **Deploy** |

```python
from claude_evals.regression import RegressionDetector

detector = RegressionDetector(significance_threshold=0.1)
result = detector.compare(baseline_run, candidate_run)

print(f"Severity: {result.severity}")       # e.g. "high"
print(f"Recommendation: {result.recommendation}")  # "block" | "review" | "deploy"
print(f"Regressions: {len(result.regressions)}")
```

## Cost Guardrails

Every task has a `max_budget_usd` ceiling (default: $0.50). If an agent exceeds it, the task is aborted and marked as errored. This prevents runaway costs during eval runs.

```bash
claude-evals run --suite datasets/contract-review --max-budget 0.25
```

## What This Doesn't Do

- **Runtime monitoring** — this is an offline eval harness, not a production observability tool
- **Obfuscated failure detection** — it can't find bugs that don't surface in test outputs
- **Non-Claude models** — the harness is built on the Claude Agent SDK specifically
- **Real-time alerting** — use this in CI, not as a monitoring daemon

## Roadmap (v0.2)

- [ ] Model sweep command (`claude-evals sweep`) — run same suite on Opus/Sonnet/Haiku
- [ ] Human review queue grader — export uncertain cases for human labeling
- [ ] GitHub PR comment generation — post eval results as PR comments
- [ ] Agent behavior metrics — tool selection accuracy, step count, efficiency
- [ ] Statistical significance testing in regression detector
- [ ] Additional datasets — RFP response review, policy document analysis

## Anthropic Resources

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/evaluating-ai-agents) — the engineering post this framework implements
- [Claude Agent SDK Documentation](https://platform.claude.com/docs/en/agent-sdk/overview) — the SDK this harness hooks into
- [Anthropic Cookbook: Evals](https://github.com/anthropics/anthropic-cookbook/tree/main/misc/building_evals) — additional eval patterns

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## License

Apache 2.0 — see [LICENSE](LICENSE).

Built by [Tribe AI](https://tribe.ai) as part of the Anthropic partner launch program.
