# llm-judge

A Claude Code skill for designing and scaffolding LLM-as-judge evaluations for agentic
systems and LLM applications.

## What it does

Walks you through the full eval design loop, then emits runnable artefacts:

1. A **rubric** with explicit, measurable criteria.
2. **Judge prompts** per criterion, with bias-mitigation built in.
3. A **Python harness** that runs the judges against your dataset and writes structured
   JSON you can diff across runs. Ships with **incremental re-eval** (cache keyed by
   content hash — new examples run, unchanged examples skip) and a **watch mode**
   (`watch.py`) that re-triggers on dataset or prompt changes.
4. **Step attribution** per trajectory: for each criterion, a per-step influence weight
   and a `critical_step`. Blame mode (cheap, judge-based) is default; counterfactual
   mode (rigorous, ablation rollout) is opt-in and needs the agent to support midpoint
   resume.
5. A **calibration script** that measures judge/human agreement (Cohen's kappa,
   Spearman).

The harness is framework-agnostic and only needs the `anthropic` SDK by default. Notes on
DeepEval, Inspect AI, and promptfoo are in `docs/patterns.md` for when you want to
graduate to a heavier toolkit.

## Install as a Claude Code skill

```bash
git clone https://github.com/<you>/llm-judge.git ~/projects/llm-judge
mkdir -p ~/.claude/skills
ln -s ~/projects/llm-judge ~/.claude/skills/llm-judge
```

Then inside Claude Code, start a conversation with anything like:

- "evaluate this agent"
- "build an eval for my RAG pipeline"
- "design a rubric for my customer-support agent"
- "audit my existing eval setup"

The skill will guide you through six phases: scope, rubric design, judge prompts, harness
generation, calibration, and a final summary.

## Use standalone (without Claude Code)

The templates and docs are readable on their own.

```bash
cp templates/rubric.md ./evals/rubric.md
cp templates/judge-prompt.md ./evals/judges/task_success.md  # then fill it in
cp templates/harness.py ./evals/run_eval.py                  # then customise
cp templates/calibrate.py ./evals/calibrate.py
export ANTHROPIC_API_KEY=...
python ./evals/run_eval.py
python ./evals/calibrate.py --human human_labels.csv --judge ./evals/results.json
```

## Directory layout

```
llm-judge/
  SKILL.md                 Claude Code skill entrypoint (read first)
  templates/
    rubric.md              Rubric skeleton with minimum criteria for agents
    judge-prompt.md        Bias-mitigating judge prompt template
    attribution.md         Step-attribution judge prompt template
    harness.py             Eval runner with caching + attribution integration
    attribution.py         Blame / counterfactual step attribution
    watch.py               Polling watcher for automatic re-eval
    calibrate.py           Judge/human agreement scoring
  docs/
    biases.md              Position, length, self-preference, halo, and more
    patterns.md            Pointwise vs pairwise, agent patterns, framework comparison
  examples/
    example-agent-eval.py  Runnable toy demo with a stub agent
```

## Design principles

- **Rubric first, prompt second.** Most eval failures are underspecified criteria, not
  bad prompts.
- **Rationale before score.** Forces chain-of-thought ordering; reduces rationalisation.
- **Structured output.** Judges emit strict JSON. No free-text verdicts.
- **Calibration is mandatory.** A judge that doesn't agree with humans on a small
  labelled set is not a judge.
- **Humans stay in the loop for safety.** LLM judges gate quality signals, not
  production releases.

## References

- Zheng et al. 2023, "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena."
- Liu et al. 2023, "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment."
- Yao et al. 2024, "τ-bench: A Benchmark for Tool-Agent-User Interaction."
- Anthropic Evals cookbook, UK AISI Inspect documentation.

## License

MIT. See [LICENSE](LICENSE).
