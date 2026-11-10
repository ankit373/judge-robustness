from __future__ import annotations

import math

import pytest

from judge_robustness.stats import Z95, wilson_interval


def test_half_successes_matches_reference():
    low, high = wilson_interval(5, 10)
    assert low == pytest.approx(0.236593, abs=1e-6)
    assert high == pytest.approx(0.763407, abs=1e-6)


def test_zero_and_all_successes_closed_form():
    n = 10
    z2 = Z95**2
    assert wilson_interval(0, n) == pytest.approx((0.0, z2 / (n + z2)))
    assert wilson_interval(n, n) == pytest.approx((n / (n + z2), 1.0))


def test_symmetry_and_containment():
    for k in range(0, 31):
        low, high = wilson_interval(k, 30)
        mirror = wilson_interval(30 - k, 30)
        assert low <= k / 30 <= high
        assert math.isclose(low, 1 - mirror[1], abs_tol=1e-12)


def test_empty_and_invalid():
    assert wilson_interval(0, 0) == (0.0, 1.0)
    with pytest.raises(ValueError):
        wilson_interval(3, 2)
