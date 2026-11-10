"""Attack families. Each maps a task to deterministic (variant_id, answer) pairs."""

from __future__ import annotations

from collections.abc import Callable

from judge_robustness.attacks import (
    constant,
    empty_filler,
    forged_delimiters,
    hedged,
    verdict_tokens,
)
from judge_robustness.tasks import Task

Generator = Callable[[Task], list[tuple[str, str]]]

FAMILIES: dict[str, Generator] = {
    "empty_filler": empty_filler.generate,
    "verdict_tokens": verdict_tokens.generate,
    "forged_delimiters": forged_delimiters.generate,
    "hedged": hedged.generate,
    "constant": constant.generate,
}
