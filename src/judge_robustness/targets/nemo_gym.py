"""NeMo Gym verifier adapter. Stub: needs a running NeMo Gym resource server."""

from __future__ import annotations

from judge_robustness.tasks import Task


class NemoGymTarget:
    name = "nemo-gym"

    def available(self) -> bool:
        return False

    def score(self, task: Task, answer: str) -> float:
        # TODO(week 2): start a resource server, confirm its verify API from NeMo Gym docs.
        raise NotImplementedError("NeMo Gym adapter is a stub; see README 'Targets'.")
