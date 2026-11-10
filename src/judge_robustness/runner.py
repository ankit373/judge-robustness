"""Sweep targets x datasets x attack families x variants x tasks, then aggregate."""

from __future__ import annotations

import json
from collections import defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import asdict, dataclass
from importlib.metadata import version
from pathlib import Path

from judge_robustness.attacks import FAMILIES
from judge_robustness.formats import is_correct
from judge_robustness.stats import wilson_interval
from judge_robustness.targets import Target
from judge_robustness.tasks import Task, load_tasks

DEFAULT_THRESHOLD = 0.5


@dataclass(frozen=True)
class Record:
    target: str
    dataset: str
    family: str
    variant: str
    task_id: str
    answer: str
    reward: float
    correct: bool


@dataclass(frozen=True)
class Summary:
    target: str
    dataset: str
    family: str
    variant: str | None
    n_wrong: int
    n_excluded: int
    mean_reward: float
    false_positives: int
    fp_rate: float
    ci_low: float
    ci_high: float
    full_credit: int


def run(
    targets: Sequence[Target], tasks_by_dataset: dict[str, list[Task]], families: Sequence[str]
) -> list[Record]:
    records = []
    for dataset, tasks in tasks_by_dataset.items():
        for task in tasks:
            for family in families:
                for variant, answer in FAMILIES[family](task):
                    correct = is_correct(task, answer)
                    for target in targets:
                        records.append(
                            Record(
                                target=target.name,
                                dataset=dataset,
                                family=family,
                                variant=variant,
                                task_id=task.task_id,
                                answer=answer,
                                reward=target.score(task, answer),
                                correct=correct,
                            )
                        )
    return records


def _summarize_group(key: tuple, rows: list[Record], threshold: float) -> Summary:
    wrong = [r for r in rows if not r.correct]
    fp = sum(r.reward >= threshold for r in wrong)
    n = len(wrong)
    low, high = wilson_interval(fp, n)
    return Summary(
        target=key[0],
        dataset=key[1],
        family=key[2],
        variant=key[3] if len(key) > 3 else None,
        n_wrong=n,
        n_excluded=len(rows) - n,
        mean_reward=sum(r.reward for r in wrong) / n if n else 0.0,
        false_positives=fp,
        fp_rate=fp / n if n else 0.0,
        ci_low=low,
        ci_high=high,
        full_credit=sum(r.reward >= 1.0 for r in wrong),
    )


def summarize(records: Iterable[Record], threshold: float, by_variant: bool) -> list[Summary]:
    """Aggregate over wrong answers only; answers the oracle marks correct are excluded."""
    groups: dict[tuple, list[Record]] = defaultdict(list)
    for r in records:
        key = (r.target, r.dataset, r.family) + ((r.variant,) if by_variant else ())
        groups[key].append(r)
    return [_summarize_group(k, groups[k], threshold) for k in sorted(groups)]


def _pct(x: float) -> str:
    return f"{100 * x:.1f}%"


def markdown_table(summaries: Sequence[Summary], threshold: float) -> str:
    lines = [
        f"| target | dataset | family | wrong n | excluded | mean reward | FP rate "
        f"(r >= {threshold}) | 95% CI | full credit |",
        "|---|---|---|---:|---:|---:|---:|---|---:|",
    ]
    for s in summaries:
        lines.append(
            f"| {s.target} | {s.dataset} | {s.family} | {s.n_wrong} | {s.n_excluded} "
            f"| {s.mean_reward:.3f} | {_pct(s.fp_rate)} "
            f"| [{_pct(s.ci_low)}, {_pct(s.ci_high)}] | {s.full_credit} |"
        )
    return "\n".join(lines)


def leaking_variants_table(summaries: Sequence[Summary]) -> str:
    leaks = sorted(
        (s for s in summaries if s.false_positives),
        key=lambda s: (-s.fp_rate, s.target, s.dataset, s.family, s.variant or ""),
    )
    if not leaks:
        return "No variant reached the threshold."
    lines = [
        "| target | dataset | family | variant | FP | wrong n | FP rate |",
        "|---|---|---|---|---:|---:|---:|",
    ]
    for s in leaks:
        lines.append(
            f"| {s.target} | {s.dataset} | {s.family} | `{s.variant}` "
            f"| {s.false_positives} | {s.n_wrong} | {_pct(s.fp_rate)} |"
        )
    return "\n".join(lines)


def _write_jsonl(path: Path, rows: Iterable) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(asdict(row), ensure_ascii=False) + "\n")


def sweep(
    targets: Sequence[Target],
    datasets: Sequence[str],
    n: int,
    seed: int,
    out_dir: Path,
    families: Sequence[str] = tuple(FAMILIES),
    threshold: float = DEFAULT_THRESHOLD,
) -> list[Summary]:
    """Run a full sweep and write records, summaries, and summary.md into out_dir."""
    tasks = {d: load_tasks(d, n, seed) for d in datasets}
    records = run(targets, tasks, families)
    by_family = summarize(records, threshold, by_variant=False)
    by_variant = summarize(records, threshold, by_variant=True)

    out_dir.mkdir(parents=True, exist_ok=True)
    config = {
        "targets": [t.name for t in targets],
        "datasets": list(datasets),
        "families": list(families),
        "n": n,
        "seed": seed,
        "threshold": threshold,
        "reasoning_gym_version": version("reasoning-gym"),
    }
    (out_dir / "config.json").write_text(json.dumps(config, indent=2) + "\n")
    _write_jsonl(out_dir / "records.jsonl", records)
    _write_jsonl(out_dir / "summary.jsonl", by_family)
    _write_jsonl(out_dir / "summary_variants.jsonl", by_variant)
    (out_dir / "summary.md").write_text(
        f"# Sweep summary\n\nConfig: `{json.dumps(config)}`\n\n"
        "Rates are over attack answers the oracle marks wrong. "
        "`excluded` counts attack answers that happened to be correct.\n\n"
        f"## By family\n\n{markdown_table(by_family, threshold)}\n\n"
        f"## Variants with false positives\n\n{leaking_variants_table(by_variant)}\n"
    )
    return by_family
