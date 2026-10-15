"""
Attribution: per-step causal influence on the final outcome.

Two modes:

  blame         — judge-based attribution. One extra API call per (trajectory, criterion).
                  Cheap. Returns a weight in [-1.0, 1.0] per step. Default.

  counterfactual — ablation rollout. For each step N (or a sampled subset), re-run the
                   agent from step N with the step masked/modified, then re-score.
                   The change in final score IS the causal influence of step N.
                   Expensive: cost scales as steps x trajectories x agent cost.
                   Requires the system-under-test adapter to implement `resume_from_step`.

Call `attribute_trajectory()` from run_eval.py after the per-criterion verdicts are
computed. The result appends an `attributions` field to each record.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable

from harness import (
    Example,
    JudgeVerdict,
    RunResult,
    Step,
    _build_judge_user_message,
    _parse_judge_response,
    _serialise_trajectory,
    JUDGE_MAX_TOKENS,
    JUDGE_MODEL,
    JUDGE_TEMPERATURE,
)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class StepWeight:
    step_index: int
    weight: float
    reason: str


@dataclass
class Attribution:
    criterion: str
    mode: str                    # "blame" or "counterfactual"
    rationale: str
    critical_step: int | None
    ambiguous: bool
    weights: list[StepWeight] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Mode 1: blame (judge-based)
# ---------------------------------------------------------------------------

def _build_attribution_user_message(
    example: Example,
    result: RunResult,
    criterion: str,
    outcome: JudgeVerdict,
) -> str:
    parts = [
        "## Input",
        example.input,
        "",
        "## Trajectory",
        _serialise_trajectory(result.trajectory),
        "",
        f"## Criterion: {criterion}",
        "",
        "## Outcome",
        f"score: {outcome.score}",
        f"rationale: {outcome.rationale}",
    ]
    return "\n".join(parts)


def attribute_blame(
    client,
    attribution_prompt: str,
    example: Example,
    result: RunResult,
    criterion: str,
    outcome: JudgeVerdict,
) -> Attribution:
    user_msg = _build_attribution_user_message(example, result, criterion, outcome)
    resp = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=JUDGE_MAX_TOKENS,
        temperature=JUDGE_TEMPERATURE,
        system=attribution_prompt,
        messages=[{"role": "user", "content": user_msg}],
    )
    raw = "".join(
        b.text for b in resp.content if getattr(b, "type", None) == "text"
    )
    # Reuse harness JSON parser.
    parsed = _parse_judge_response(raw, criterion)
    try:
        obj = json.loads(parsed.raw[parsed.raw.find("{"):parsed.raw.rfind("}") + 1])
    except (ValueError, json.JSONDecodeError):
        obj = {}
    weights = [
        StepWeight(
            step_index=int(w.get("step_index", i)),
            weight=float(w.get("weight", 0.0)),
            reason=str(w.get("reason", "")),
        )
        for i, w in enumerate(obj.get("weights", []) or [])
    ]
    return Attribution(
        criterion=criterion,
        mode="blame",
        rationale=obj.get("rationale", parsed.rationale),
        critical_step=obj.get("critical_step"),
        ambiguous=bool(obj.get("ambiguous", parsed.ambiguous)),
        weights=weights,
    )


# ---------------------------------------------------------------------------
# Mode 2: counterfactual (ablation rollout)
# ---------------------------------------------------------------------------

def attribute_counterfactual(
    example: Example,
    result: RunResult,
    criterion: str,
    baseline_score: Any,
    resume_adapter: Callable[[Example, list[Step], int], RunResult],
    rescore: Callable[[Example, RunResult], JudgeVerdict],
    step_indices: list[int] | None = None,
) -> Attribution:
    """Counterfactual attribution by re-running from each step.

    Required of caller:
      - `resume_adapter(example, prefix_trajectory, start_from)` re-runs the agent
        starting at step `start_from`, given the prefix trajectory, and returns a new
        RunResult. The adapter decides how to mask/modify the step: simplest is to drop
        it and let the agent re-plan from the previous state.
      - `rescore(example, run_result)` returns the JudgeVerdict for the criterion.

    If your agent doesn't support resume, use blame attribution instead.
    """
    steps = list(range(len(result.trajectory))) if step_indices is None else step_indices
    weights: list[StepWeight] = []

    def _score_to_float(s: Any) -> float:
        if isinstance(s, (int, float)):
            return float(s)
        mapping = {"fail": 0.0, "partial": 0.5, "pass": 1.0}
        return mapping.get(str(s).lower(), 0.0)

    base = _score_to_float(baseline_score)

    for idx in steps:
        prefix = result.trajectory[:idx]
        try:
            new_result = resume_adapter(example, prefix, idx)
            new_verdict = rescore(example, new_result)
            delta = base - _score_to_float(new_verdict.score)
        except Exception as e:
            weights.append(StepWeight(idx, 0.0, f"resume error: {e}"))
            continue
        weights.append(StepWeight(
            step_index=idx,
            weight=max(-1.0, min(1.0, delta)),
            reason=(
                f"Removing step changed score from {baseline_score} to {new_verdict.score} "
                f"(delta={delta:+.2f})"
            ),
        ))

    critical = max(weights, key=lambda w: abs(w.weight)).step_index if weights else None
    return Attribution(
        criterion=criterion,
        mode="counterfactual",
        rationale=(
            f"Counterfactual rollout over {len(steps)} steps. "
            f"Baseline score: {baseline_score}."
        ),
        critical_step=critical,
        ambiguous=not weights,
        weights=weights,
    )


# ---------------------------------------------------------------------------
# Glue: attach attributions to the record
# ---------------------------------------------------------------------------

def attributions_to_json(attrs: list[Attribution]) -> list[dict[str, Any]]:
    out = []
    for a in attrs:
        d = asdict(a)
        out.append(d)
    return out
