"""Task records and the reasoning-gym loader."""

from __future__ import annotations

import warnings
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class Format(StrEnum):
    YES_NO = "yes_no"
    INTEGER = "integer"
    EXPR24 = "expr24"
    GRID = "grid"
    LOGIC = "logic"


@dataclass(frozen=True)
class Task:
    task_id: str
    dataset: str
    question: str
    gold: str
    fmt: Format
    entry: dict[str, Any] = field(compare=False, repr=False)


DATASET_FORMATS: dict[str, Format] = {
    "syllogism": Format.YES_NO,
    "propositional_logic": Format.LOGIC,
    "puzzle24": Format.EXPR24,
    "game_of_life": Format.GRID,
    "number_sequence": Format.INTEGER,
}


def _gold(entry: dict[str, Any]) -> str:
    # propositional_logic has no single answer; it ships one valid example.
    if entry["answer"] is not None:
        return str(entry["answer"])
    return str(entry["metadata"]["example_answer"])


def load_tasks(dataset: str, n: int, seed: int) -> list[Task]:
    """Generate n tasks from a reasoning-gym dataset with its default config."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", SyntaxWarning)
        import reasoning_gym

    fmt = DATASET_FORMATS[dataset]
    ds = reasoning_gym.create_dataset(dataset, size=n, seed=seed)
    return [
        Task(
            task_id=f"{dataset}/{seed}/{i}",
            dataset=dataset,
            question=entry["question"],
            gold=_gold(entry),
            fmt=fmt,
            entry=entry,
        )
        for i, entry in enumerate(ds)
    ]
