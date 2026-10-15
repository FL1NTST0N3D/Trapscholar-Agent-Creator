# loop-engineer

[![Support me on Patreon](https://img.shields.io/badge/Patreon-Support%20my%20work-FF424D?style=flat&logo=patreon&logoColor=white)](https://www.patreon.com/AndersBjarby)

A Claude Code **skill + subagent** for setting up and administering *agentic
loops* — the 2026 "loop engineering" paradigm where the developer's object of
attention shifts **source code → agent → loop**.

> "I don't prompt Claude anymore. I have loops running that prompt Claude… My job
> is to write loops." — Boris Cherny, creator of Claude Code (Anthropic)

The loop primitives now exist in Claude Code (`claude -p`, `/loop`, `/goal`,
Tasks, cloud Routines), but nothing helps you **choose, scaffold, and guard** a
loop. This does. Every loop it produces ships with non-negotiable guardrails so it
can't "loopmaxx" — run forever against a vague objective and burn money.

## What's inside

```
.claude/
├── skills/loop-engineer/        # the knowledge pack
│   ├── SKILL.md                 # decision tree + 5-point guardrail checklist
│   ├── reference/
│   │   ├── primitives.md        # claude -p, /loop, /goal, Tasks, Routines, cost gating
│   │   ├── taxonomy.md          # the 5 patterns + when to use each + nesting
│   │   └── guardrails.md        # failure modes + mitigations (with the real numbers)
│   └── templates/               # runnable, guardrailed scaffolds
│       ├── headless-loop.sh         # single agentic loop around `claude -p`
│       ├── evaluator-optimizer.sh   # generator + SEPARATE critic
│       ├── meta-prompt-refine.sh    # a loop that refines the prompt another loop runs
│       ├── fanout-orchestrator.sh   # orchestrator-workers fan-out + verify
│       └── goal-loop.md             # first-party /goal and /loop recipes
├── agents/
│   ├── loop-architect.md        # interactive loop designer (scaffolds)
│   └── loop-teacher.md          # interactive tutor (explains how to think in loops)
└── commands/                    # slash-command shortcuts
    ├── new-loop.md              # /new-loop <goal>   → design + scaffold a loop
    ├── loop-audit.md            # /loop-audit <file> → audit a loop vs. guardrails
    └── learn-loops.md           # /learn-loops       → learn loop engineering interactively
```

> Note: Claude Code already ships a built-in `/loop` command (interval/self-paced
> repetition), so these shortcuts are namespaced `/new-loop` and `/loop-audit` to
> avoid the collision.

## The five patterns

| Pattern | Use when | Scaffold |
|---|---|---|
| **Headless while-loop** | one binary check, one agent | `headless-loop.sh` / `/goal` |
| **Evaluator-optimizer** | quality is a judgment call | `evaluator-optimizer.sh` |
| **Meta / prompt-refinement** | you're improving the *prompt* itself | `meta-prompt-refine.sh` |
| **Orchestrator fan-out** | subtasks can't be predicted up front | `fanout-orchestrator.sh` / Workflow tool |
| **Scheduled / triggered** | run on an interval or with the machine off | `/loop` / cloud Routine |

Nest them: an orchestrator can spawn evaluator-optimizer inner loops; a meta-loop
wraps a headless loop and rewrites its prompt between runs.

## The one rule that prevents most disasters

**No binary, verifiable exit condition → no loop.** "Improve the UX" has no
pass/fail and produces infinite loops + large API bills. "Make `npm test` exit 0"
does. A real 4-agent loop once ran 11 days and cost ~$47,000 for lack of this.

Every scaffold enforces the **five-point guardrail checklist**:

1. **Verifiable exit condition** — checked each iteration.
2. **Max-iteration cap** — a hard bound in code, not in the prompt.
3. **Budget cap in code** — sum `total_cost_usd`, stop *before* the next call.
   (Alerts are not enforcement.)
4. **Sandbox** — worktree/container/branch, never unattended on `main`.
5. **Human checkpoint** — for any push/deploy/send/irreversible action.

## Install

Drop the skill and agent into a project's `.claude/`, or into `~/.claude/` to make
them available everywhere:

```bash
# project-local
git clone https://github.com/fltman/loop-engineer.git
cp -r loop-engineer/.claude/skills/loop-engineer  /path/to/your/project/.claude/skills/
cp -r loop-engineer/.claude/agents/loop-architect.md /path/to/your/project/.claude/agents/

# or globally
cp -r loop-engineer/.claude/skills/loop-engineer  ~/.claude/skills/
cp -r loop-engineer/.claude/agents/loop-architect.md ~/.claude/agents/
```

## Use

- **Just describe the loop** and the `loop-engineer` skill triggers and scaffolds
  it: *"set up a loop that runs until the tests pass, max 10 iterations, under $5."*
- **Design it interactively** with the `loop-architect` subagent — it interrogates
  the goal, forces it to be binary, picks the pattern, scaffolds the files, and
  wires the guardrails.
- **Learn the mental model** with the `loop-teacher` subagent — it teaches loop
  engineering Socratically against your own task (no scaffolding, just
  understanding), then hands off to `loop-architect` when you're ready.
- **Use the slash shortcuts** for comfort:
  - `/new-loop <goal>` — design + scaffold a guardrailed loop for a goal
  - `/loop-audit <file>` — audit an existing loop against the five guardrails
  - `/learn-loops` — learn how to think about loops interactively

Run a scaffold directly, e.g.:

```bash
EXIT_CHECK='npm test --silent' \
TASK_PROMPT='Make all unit tests pass. Run the suite to verify.' \
MAX_ITERS=10 BUDGET_USD=5.00 \
.claude/skills/loop-engineer/templates/headless-loop.sh
```

> The templates parse `claude -p --output-format json`. Field names
> (`result`/`response`, per-call vs. cumulative `total_cost_usd`) can vary by
> version — verify against your Claude Code before unattended runs.

## Provenance & honest attribution

Distilled from a multi-source, adversarially fact-checked research pass. The
architecture taxonomy comes from Anthropic's
[Building Effective Agents](https://www.anthropic.com/research/building-effective-agents);
the meta-loop lineage from *Self-Taught Evaluators* (Wang et al., arXiv 2408.02666).
Shell fan-out / headless-CI loops are **community patterns, not official Anthropic
endorsements** — and are labeled as such throughout.

## License

MIT — see [LICENSE](LICENSE).
