---
name: llm-judge
version: 0.1.0
description: |
  Design and scaffold LLM-as-judge evaluations for agentic systems and LLM applications.
  Walks the user through rubric design, judge prompt construction, bias mitigation, and
  runnable Python harness generation. Use when the user wants to evaluate an agent, build
  an eval suite, add regression tests for an LLM system, design a judge for quality/safety/
  compliance, or audit an existing eval setup.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
---

# llm-judge

## What this skill does

Guides the user through building a rigorous LLM-as-judge evaluation for an agent or LLM
application. Produces:

1. A **rubric** with explicit, measurable criteria.
2. **Judge prompts** per criterion, with bias-mitigation built in.
3. A **runnable Python harness** that executes the judges against a dataset and emits
   structured JSON for regression tracking.
4. A **calibration plan** against a small human-labeled set.

The skill is framework-agnostic. The generated harness uses only the `anthropic` (or
`openai`) SDK by default. Notes on DeepEval and Inspect AI are included in `docs/` for
users who want to graduate to a heavier toolkit.

## When to invoke

Invoke when the user says anything like:
- "evaluate this agent"
- "build an eval" / "set up evaluation" / "write regression tests for this LLM system"
- "LLM as a judge" / "how do I grade these outputs"
- "audit my eval" / "review this evaluation setup"
- "design a rubric for <agent>"

## Workflow

Follow these phases in order. Do not skip. Each phase should produce concrete artefacts in
the user's working directory.

### Phase 1 — Scope the eval (ask before building)

Use `AskUserQuestion` if the user has not already given you:

1. **What is being evaluated?** A single-turn chatbot, a multi-step agent with tool use,
   a RAG system, a planner, or a specific workflow.
2. **What does "good" look like?** Task success, safety, compliance, efficiency, tone,
   factuality, tool-use correctness. The user should name 2–5 things they care about.
3. **What ground truth is available?** Gold answers, reference trajectories, human labels,
   or nothing (pure LLM judgment).
4. **What is the deployment context?** Research prototype, production pipeline, regulated
   industry (healthcare, finance, legal). This determines rigour level.

Only proceed when these four are answered. If the user says "just build something",
propose defaults and confirm.

### Phase 2 — Design the rubric

Load `templates/rubric.md` and adapt it to the user's context. For each criterion:

- Name it (one noun phrase, e.g. "Tool-call correctness").
- Define it operationally. What exactly does the judge check.
- Choose a scoring type:
  - **Binary** (pass/fail): use for safety, compliance, hard constraints.
  - **3-point** (fail/partial/pass): use for task success.
  - **5-point Likert**: use for quality, coherence, tone. Use sparingly because it's noisy.
- List the failure modes the criterion is meant to catch.
- Decide if the criterion is **step-level** (evaluated at each agent step) or
  **trajectory-level** (evaluated on the whole run).

For agents, always include at least:
- A task-success criterion (trajectory-level).
- A tool-use-correctness criterion (step-level, optional if no tools).
- A safety/compliance criterion (binary, trajectory-level).

Write the finalised rubric to `./evals/rubric.md` in the user's project.

### Phase 3 — Draft judge prompts

For each criterion, draft a judge prompt using `templates/judge-prompt.md` as the base.
Every judge prompt must include:

1. **Role line**: "You are a rigorous evaluator of [criterion]."
2. **Definition**: restate what the criterion means, in judge-facing language.
3. **Scoring scale**: explicit scale with anchors for each point.
4. **Input schema**: what the judge will see (input, output, and for agents, the
   trajectory).
5. **Bias controls**:
   - Force structured JSON output.
   - Require rationale BEFORE the score (chain-of-thought ordering).
   - For pairwise judging: instruct the judge to ignore position and length.
   - Do not reveal which model produced the output.
6. **Output schema**: strict JSON with `rationale` (string) and `score` (typed per scale).

Read `docs/biases.md` and flag any bias risk specific to this eval (e.g. if outputs are
going to be long, verbosity bias is a concern).

Save judge prompts as separate files in `./evals/judges/<criterion>.md`.

### Phase 4 — Generate the harness

Copy `templates/harness.py` to `./evals/run_eval.py`. Customise:

- The dataset loader (point it at the user's data).
- The judges list (one entry per criterion, each referencing a prompt file).
- The system-under-test adapter (a function that takes an input and returns an
  output/trajectory — the user fills this in if they haven't given you the agent code).
- The output path for the JSON results.

Do not hard-code API keys. Read them from environment variables. Remind the user to set
`ANTHROPIC_API_KEY` or `OPENAI_API_KEY`.

### Phase 4b — Step attribution

For agent evals, scoring steps in isolation is not enough: the user also wants to know
which steps *caused* the final outcome. Copy `templates/attribution.md` to
`./evals/judges/attribution.md` and set `ATTRIBUTION_PROMPT_PATH` in the harness.

Two modes are supported:

- **blame** (default): one extra judge call per trajectory per criterion. The judge
  reads the trajectory and the final verdict, then assigns a weight in [-1.0, 1.0] per
  step plus a `critical_step` index. Cheap, soft — correlation not causation.
- **counterfactual**: for each step N, re-run the agent from step N with the step
  masked/modified, and measure how much the final score changes. The delta IS the
  causal influence. Rigorous but expensive, and requires the user's agent to support
  `resume_from_step`. Opt-in.

Document which mode is active and why in the rubric.

### Phase 4c — Incremental / automatic re-eval

The harness caches verdicts by `(example_hash, rubric_hash)`:
- `example_hash` covers `id + input + reference`.
- `rubric_hash` covers `judge_model + every judge prompt + attribution prompt`.

Consequences:
- Adding a new example → only that example runs.
- Editing a judge prompt → rubric_hash changes → everything re-runs against the new
  judge.
- Nothing stale ever ships: the cache key is content-addressed, not name-based.

`templates/watch.py` is a dependency-free polling watcher that re-invokes `run_eval.py`
whenever the dataset or judge prompts change. Copy it to `./evals/watch.py` and run
either `python watch.py --once` (one-shot) or `python watch.py --interval 10`
(continuous). This is the "automatic" layer: drop a new example into the dataset file
and the next cycle evaluates it without touching anything else.

### Phase 5 — Calibration plan

Explain the calibration loop:

1. The user should hand-label 20–50 examples with the rubric.
2. Run the judges on those examples.
3. Compute per-criterion agreement (Cohen's kappa for categorical, Spearman for ordinal).
4. If agreement is low (<0.6 kappa, <0.7 Spearman), iterate on the prompt or anchors.
5. Re-check whenever the judge model changes or the rubric is updated.

Generate `./evals/calibrate.py` that takes a CSV of human labels and the judge output JSON
and prints per-criterion agreement.

### Phase 6 — Report back

Summarise in plain language:

- What was evaluated.
- What rubric you proposed.
- What bias risks you flagged.
- What files you created.
- What the user needs to do next (fill in the system adapter, add the dataset, run
  calibration).

Do NOT run the harness yourself unless the user asks. The harness will call paid APIs.

## Agentic system extensions

For evaluating agents specifically, additionally:

- **Trajectory representation**: serialise the agent run as a list of steps, each with
  `role`, `content`, `tool_calls`, `tool_results`. The judge sees this structured trace.
- **Step-level vs trajectory-level**: step-level judges score individual tool calls or
  reasoning steps; trajectory-level judges score the whole run. Use both.
- **Cost/efficiency metrics**: track step count, token count, tool-call count, wall-clock
  time. These are not LLM-judged — compute them programmatically.
- **Environment state**: if the agent acts on external state (DB, filesystem, API),
  checkpoint the state before and after and include a `state_diff` criterion.

## What this skill does NOT do (by design)

- Does not fine-tune judges. Use Prometheus-style fine-tuned judges only when LLM-as-judge
  with a strong base model has been shown insufficient.
- Does not commit to a specific vendor framework. If the user wants DeepEval or Inspect
  AI, read `docs/patterns.md` and point them there.
- Does not replace human evaluation. The calibration step is mandatory for any
  production use.

## References

- Zheng et al. 2023, "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" — established
  position/verbosity/self-enhancement biases.
- Liu et al. 2023, "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment" —
  chain-of-thought + form-filling judge pattern.
- Yao et al. 2024, "τ-bench: A Benchmark for Tool-Agent-User Interaction" — agent eval
  benchmark design.
- Anthropic Evals cookbook, UK AISI Inspect documentation, OpenAI Evals repo.
