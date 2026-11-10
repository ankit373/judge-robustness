from __future__ import annotations

import pytest

from judge_robustness.tasks import DATASET_FORMATS, Task, load_tasks


@pytest.fixture(scope="session")
def tasks() -> dict[str, list[Task]]:
    return {d: load_tasks(d, 20, seed=7) for d in DATASET_FORMATS}
