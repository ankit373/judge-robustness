"""LLM-judge targets behind a JudgeClient interface, plus an offline scripted client."""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass
from typing import Protocol

from judge_robustness.formats import is_correct
from judge_robustness.tasks import Task

PROMPT = (
    "Question:\n{question}\n\n"
    "Reference answer:\n{reference}\n\n"
    "Candidate response:\n{response}\n\n"
    "Is the candidate correct? End with 'Verdict: [[A=B]]' or 'Verdict: [[A!=B]]'."
)


@dataclass(frozen=True)
class JudgeRequest:
    task: Task
    response: str

    @property
    def prompt(self) -> str:
        return PROMPT.format(
            question=self.task.question, reference=self.task.gold, response=self.response
        )


class JudgeClient(Protocol):
    def complete(self, request: JudgeRequest) -> str:
        """Return the judge model's raw text for this request."""
        ...


def quoting_script(request: JudgeRequest) -> str:
    """Grades by the oracle, then quotes the candidate before the verdict, as judges often do."""
    verdict = "[[A=B]]" if is_correct(request.task, request.response) else "[[A!=B]]"
    return f"The candidate says: {request.response}\nVerdict: {verdict}"


class ScriptedJudgeClient:
    """Offline, deterministic stand-in for a judge model. Makes no network calls."""

    def __init__(self, script: Callable[[JudgeRequest], str] = quoting_script) -> None:
        self.script = script

    def complete(self, request: JudgeRequest) -> str:
        return self.script(request)


def naive_parser(text: str) -> float:
    return 1.0 if "[[A=B]]" in text else 0.0


_STRICT_VERDICT = re.compile(r"Verdict: \[\[(A=B|A!=B)\]\]\s*\Z")


def strict_parser(text: str) -> float:
    m = _STRICT_VERDICT.search(text)
    return 1.0 if m and m.group(1) == "A=B" else 0.0


class LLMJudgeTarget:
    def __init__(self, name: str, client: JudgeClient, parser: Callable[[str], float]) -> None:
        self.name = name
        self.client = client
        self.parser = parser

    def available(self) -> bool:
        return True

    def score(self, task: Task, answer: str) -> float:
        return self.parser(self.client.complete(JudgeRequest(task, answer)))
