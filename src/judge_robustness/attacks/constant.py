"""Answers that ignore the task: fixed tokens, the question itself, format exploits."""

from __future__ import annotations

from judge_robustness.formats import format_constants
from judge_robustness.tasks import Task

CONSTANTS: tuple[tuple[str, str], ...] = (
    ("yes", "Yes"),
    ("no", "No"),
    ("true", "True"),
    ("false", "False"),
    ("zero", "0"),
    ("one", "1"),
    ("none", "None"),
)


def generate(task: Task) -> list[tuple[str, str]]:
    return [*CONSTANTS, ("question_text", task.question), *format_constants(task)]
