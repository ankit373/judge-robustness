from __future__ import annotations

import json
import time

from judge_robustness.attacks import FAMILIES
from judge_robustness.runner import sweep
from judge_robustness.targets import TARGETS

DATASETS = ["syllogism", "puzzle24"]
TARGET_NAMES = ["reasoning-gym", "mock-judge-naive", "mock-judge-strict"]


def test_two_dataset_sweep_under_a_minute(tmp_path):
    start = time.monotonic()
    targets = [TARGETS[t]() for t in TARGET_NAMES]
    summaries = sweep(targets, DATASETS, n=20, seed=1, out_dir=tmp_path)
    assert time.monotonic() - start < 60

    assert len(summaries) == len(TARGET_NAMES) * len(DATASETS) * len(FAMILIES)
    for name in ("config.json", "records.jsonl", "summary.jsonl", "summary.md"):
        assert (tmp_path / name).stat().st_size > 0
    first = json.loads((tmp_path / "records.jsonl").read_text().splitlines()[0])
    assert {"target", "family", "variant", "reward", "correct"} <= first.keys()


def test_sweep_is_reproducible(tmp_path):
    targets = [TARGETS["reasoning-gym"]()]
    for sub in ("a", "b"):
        sweep(targets, ["puzzle24"], n=5, seed=3, out_dir=tmp_path / sub)
    a = (tmp_path / "a" / "records.jsonl").read_text()
    assert a == (tmp_path / "b" / "records.jsonl").read_text()
