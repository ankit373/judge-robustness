"""reasoning-gym's shipped score_answer, default dataset configs."""

from __future__ import annotations

import warnings
from collections.abc import Callable
from functools import cache
from typing import Any

from judge_robustness.tasks import Task

ScoreFn = Callable[[str | None, dict[str, Any]], float]


@cache
def _score_fn(dataset: str) -> ScoreFn:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SyntaxWarning)
        from reasoning_gym import get_score_answer_fn
    return get_score_answer_fn(dataset)


class ReasoningGymTarget:
    name = "reasoning-gym"

    def available(self) -> bool:
        return True

    def score(self, task: Task, answer: str) -> float:
        return float(_score_fn(task.dataset)(answer, task.entry))
