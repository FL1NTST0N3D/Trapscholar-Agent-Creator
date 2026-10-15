"""
Watch mode: re-run evaluation automatically when the dataset or judge prompts change.

Usage:
  python watch.py --once                  # process anything new, then exit
  python watch.py --interval 10           # poll every 10 seconds

What counts as "new":
  - A new example in the dataset (harness.py caches by example hash).
  - A changed judge prompt, rubric, or attribution prompt (rubric hash bumps, all
    examples re-run against that rubric).

This is the automation layer requested: drop a new example into your dataset and the
next poll cycle runs the whole pipeline for that example only. Judge scores +
step attributions are emitted without re-judging anything already cached.

No external dependencies (no watchdog, no inotify). Pure polling so it runs anywhere.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path


# Files whose mtime triggers a re-run.
WATCH_PATHS = [
    Path("./evals/dataset.jsonl"),      # or wherever your dataset lives
    Path("./evals/judges"),             # directory of judge prompts
    Path("./evals/rubric.md"),
]


def fingerprint(paths: list[Path]) -> tuple:
    """Compound mtime fingerprint over all watched paths (recursive for dirs)."""
    prints: list[tuple[str, float]] = []
    for p in paths:
        if not p.exists():
            continue
        if p.is_file():
            prints.append((str(p), p.stat().st_mtime))
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.is_file():
                    prints.append((str(f), f.stat().st_mtime))
    return tuple(prints)


def run_eval() -> int:
    print(f"\n=== eval triggered at {time.strftime('%H:%M:%S')} ===")
    return subprocess.call([sys.executable, "run_eval.py"])


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--once", action="store_true",
                   help="Run once and exit.")
    p.add_argument("--interval", type=int, default=10,
                   help="Poll interval in seconds (default 10).")
    args = p.parse_args()

    if args.once:
        sys.exit(run_eval())

    last = None
    print(f"Watching {len(WATCH_PATHS)} paths. Polling every {args.interval}s. "
          f"Ctrl-C to stop.")
    try:
        while True:
            fp = fingerprint(WATCH_PATHS)
            if fp != last:
                rc = run_eval()
                print(f"=== eval finished (exit {rc}) ===")
                last = fp
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nstopped.")


if __name__ == "__main__":
    main()
