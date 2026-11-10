"""The one interface every verifier adapter implements."""

from __future__ import annotations

from typing import Protocol

from judge_robustness.tasks import Task


class Target(Protocol):
    name: str

    def available(self) -> bool:
        """False when the target needs something not present (server, model, key)."""
        ...

    def score(self, task: Task, answer: str) -> float:
        """Reward the verifier gives this answer, as the extracted answer string."""
        ...
