"""Verifier adapters, all behind Target.score(task, answer) -> float."""

from __future__ import annotations

from collections.abc import Callable

from judge_robustness.targets.base import Target
from judge_robustness.targets.judge import (
    LLMJudgeTarget,
    ScriptedJudgeClient,
    naive_parser,
    strict_parser,
)
from judge_robustness.targets.nemo_gym import NemoGymTarget
from judge_robustness.targets.prime_verifiers import PrimeVerifiersTarget
from judge_robustness.targets.reasoning_gym import ReasoningGymTarget

TARGETS: dict[str, Callable[[], Target]] = {
    "reasoning-gym": ReasoningGymTarget,
    "mock-judge-naive": lambda: LLMJudgeTarget(
        "mock-judge-naive", ScriptedJudgeClient(), naive_parser
    ),
    "mock-judge-strict": lambda: LLMJudgeTarget(
        "mock-judge-strict", ScriptedJudgeClient(), strict_parser
    ),
    "nemo-gym": NemoGymTarget,
    "prime-verifiers": PrimeVerifiersTarget,
}

__all__ = ["TARGETS", "Target"]
