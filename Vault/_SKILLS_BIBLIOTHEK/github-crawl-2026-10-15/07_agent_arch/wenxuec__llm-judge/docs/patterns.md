# Eval patterns and framework comparison

This skill gives you a minimal, framework-agnostic harness. That is deliberate: most eval
failures are rubric failures, not tooling failures, and it is easier to debug a 300-line
harness than a plugin graph. But you may want to graduate to a heavier toolkit once the
rubric stabilises. This doc helps you pick.

## Common eval patterns

### Pointwise scoring
One judge, one output, one score. Simplest and most debuggable. Use for most criteria.

### Pairwise preference
Judge picks A or B (or tie). Higher signal per judgment than pointwise, at the cost of
quadratic scaling in candidates. Use for head-to-head model comparisons.

### Reference-based
Judge sees a gold answer and compares. Good for factuality and code correctness. Prone to
sycophancy on the reference.

### Rubric-based (reference-free)
Judge scores against explicit criteria without a gold. Works when gold answers are
expensive or there are many valid answers. Prone to bias drift without good anchors.

### Trajectory vs step
- **Step-level**: score individual actions (tool calls, reasoning steps).
- **Trajectory-level**: score the whole run.
- Use both for agents. Step-level catches local bugs; trajectory catches strategic
  failures (giving up, going in circles).

### Ensembling
Aggregate multiple judges (different models, different prompts) via majority vote or
score averaging. Reduces single-judge bias at the cost of API calls. Worth it for
high-stakes decisions.

## Agentic eval patterns

### τ-bench style (Yao et al. 2024)
Agent talks to a simulated user while hitting a tool API against a real database.
Evaluates both task completion (database state diff) and policy compliance (rule
violations). Good template for customer-service-style agents.

### SWE-bench style
Task is derived from a real GitHub issue; success is defined by the project's own unit
tests passing. Works only when you have automatable ground truth. No LLM judge needed for
the success metric — use judges for secondary criteria (code quality, tool-use efficiency).

### WebArena / AgentBench
Agent operates a live (sandboxed) web/OS environment. Success is measured by environment
state. Good for tool-use and planning evals.

### State-diff evaluation
For agents that modify external state, checkpoint before and after, and judge the diff.
Avoids the judge re-reading the whole trajectory.

## Framework comparison

| Framework       | Good for                              | Caveats                            |
|-----------------|---------------------------------------|------------------------------------|
| Hand-rolled     | Full control, small rubrics, debugging| You write the reporting yourself.  |
| DeepEval        | Python-first, pytest integration      | Opinionated metric catalogue.      |
| Inspect AI      | UK AISI, safety evals, task grammars  | Steeper learning curve.            |
| promptfoo       | YAML-driven, CI-friendly              | Less flexible for agents.          |
| LangSmith       | If already on LangChain               | Vendor lock-in.                    |
| Langfuse        | Self-host observability + eval        | Newer, smaller ecosystem.          |
| Arize Phoenix   | Production trace analysis             | Heavier, infra-oriented.           |
| RAGAS           | RAG-specific metrics                  | Narrow scope.                      |
| OpenAI Evals    | Simple graded completions             | Minimal agent support.             |

## When to graduate from the hand-rolled harness

Graduate when at least two of these are true:

- You have more than ~5 criteria and ~500 examples per run.
- You need parallel execution with retry/backoff across thousands of calls.
- You need a web UI for non-engineers to inspect verdicts.
- You need to integrate with an existing trace/observability platform.
- You are running this in CI and need structured reports for regression gates.

For graduation: **Inspect AI** if safety/regulated context matters, **DeepEval** if your
team is already Python+pytest heavy, **promptfoo** if the rubric fits YAML and you want
CI-first ergonomics.

## Where LLM-as-judge is the wrong tool

- **Exact-answer tasks** (math, code, factual retrieval): use programmatic checks.
- **Ranking a huge candidate pool**: use embeddings + retrieval, not O(n²) pairwise.
- **Low-level syntax**: use a linter or compiler, not an LLM.
- **Security-critical decisions**: always have a human in the loop; never ship LLM judge
  verdicts as the sole gate.

LLM-as-judge is right when the criterion requires reading and interpretation (quality,
tone, reasoning soundness, nuanced compliance), and when programmatic checks are not
expressive enough to capture what you care about.
