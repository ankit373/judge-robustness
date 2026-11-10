"""Prime Intellect `verifiers` rubric adapter. Stub: rubrics may call judge models."""

from __future__ import annotations

from judge_robustness.tasks import Task


class PrimeVerifiersTarget:
    name = "prime-verifiers"

    def available(self) -> bool:
        return False

    def score(self, task: Task, answer: str) -> float:
        # TODO(week 2): load an environment, call its rubric offline; judge rubrics use JudgeClient.
        raise NotImplementedError("Prime verifiers adapter is a stub; see README 'Targets'.")
