"""Command line entry point."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from judge_robustness.attacks import FAMILIES
from judge_robustness.runner import DEFAULT_THRESHOLD, sweep
from judge_robustness.targets import TARGETS
from judge_robustness.tasks import DATASET_FORMATS

DEFAULT_TARGETS = ("reasoning-gym", "mock-judge-naive", "mock-judge-strict")


def _csv(value: str) -> list[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="judge-robustness", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    run = sub.add_parser("run", help="run a sweep")
    run.add_argument("--targets", type=_csv, default=list(DEFAULT_TARGETS))
    run.add_argument("--datasets", type=_csv, default=list(DATASET_FORMATS))
    run.add_argument("--families", type=_csv, default=list(FAMILIES))
    run.add_argument("--n", type=int, default=50, help="tasks per dataset")
    run.add_argument("--seed", type=int, default=42)
    run.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    run.add_argument("--out", type=Path, default=Path("results/latest"))
    sub.add_parser("list", help="list targets, datasets, and families")
    args = parser.parse_args(argv)

    if args.cmd == "list":
        for name, make in TARGETS.items():
            print(f"target  {name:20} {'ready' if make().available() else 'stub'}")
        for name, fmt in DATASET_FORMATS.items():
            print(f"dataset {name:20} {fmt}")
        for name in FAMILIES:
            print(f"family  {name}")
        return 0

    unknown = [t for t in args.targets if t not in TARGETS]
    unknown += [d for d in args.datasets if d not in DATASET_FORMATS]
    unknown += [f for f in args.families if f not in FAMILIES]
    if unknown:
        parser.error(f"unknown names: {', '.join(unknown)}")
    targets = [TARGETS[t]() for t in args.targets]
    stubs = [t.name for t in targets if not t.available()]
    if stubs:
        parser.error(f"targets not available yet: {', '.join(stubs)}")

    sweep(targets, args.datasets, args.n, args.seed, args.out, args.families, args.threshold)
    print((args.out / "summary.md").read_text())
    return 0


if __name__ == "__main__":
    sys.exit(main())
