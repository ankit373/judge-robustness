"""Binomial interval used for every reported rate."""

from __future__ import annotations

import math

Z95 = 1.959963984540054


def wilson_interval(successes: int, n: int, z: float = Z95) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion; (0, 1) when n is 0."""
    if not 0 <= successes <= n:
        raise ValueError(f"need 0 <= successes <= n, got {successes}/{n}")
    if n == 0:
        return (0.0, 1.0)
    p = successes / n
    z2 = z * z
    denom = 1 + z2 / n
    center = (p + z2 / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n)) / denom
    # The bounds are exactly 0 and 1 at the edges; pin them against float error.
    low = 0.0 if successes == 0 else max(0.0, center - half)
    high = 1.0 if successes == n else min(1.0, center + half)
    return (low, high)
