"""Several candidate answers at once, one of them the gold answer."""

from __future__ import annotations

import json

from judge_robustness.formats import decoy
from judge_robustness.tasks import Task


def generate(task: Task) -> list[tuple[str, str]]:
    g, d = task.gold, decoy(task)
    return [
        ("gold_or_decoy", f"{g} or {d}"),
        ("decoy_or_gold", f"{d} or {g}"),
        ("comma_list", f"{g}, {d}"),
        ("either", f"Either {d} or {g}"),
        ("bullets", f"- {d}\n- {g}"),
        ("possible_answers", f"Possible answers: {d}; {g}"),
        ("json_list", json.dumps([d, g], ensure_ascii=False)),
        ("slash", f"{d} / {g}"),
        ("alternatively", f"Answer: {d}\nAlternatively: {g}"),
        ("double_boxed", f"\\boxed{{{d}}} \\boxed{{{g}}}"),
    ]
