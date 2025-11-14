import os
import sys
import pytest

# Ensure the project root is on sys.path so tests can import modules from the repository
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buggy_model import score_user


# Valid scoring tests

def test_score_calculation_basic():
    assert score_user(20, 100) == 20 * 2 + 100 // 10


def test_score_minimum_and_max_inputs():
    assert score_user(0, 0) == 0 * 2 + 0 // 10
    assert score_user(120, 10000) == 120 * 2 + 10000 // 10


# Input validation tests

def test_invalid_age_negative():
    with pytest.raises(ValueError):
        score_user(-1, 10)


def test_invalid_age_too_large():
    with pytest.raises(ValueError):
        score_user(121, 10)


def test_invalid_credits_negative():
    with pytest.raises(ValueError):
        score_user(30, -1)


def test_invalid_credits_too_large():
    with pytest.raises(ValueError):
        score_user(30, 10001)


def test_non_int_age_raises():
    with pytest.raises(TypeError):
        score_user(20.5, 100)


def test_non_int_credits_raises():
    with pytest.raises(TypeError):
        score_user(20, 100.0)


def test_score_never_exceeds_cap():
    # Even if inputs are within allowed limits, ensure final score is capped at 5000
    # The current allowed inputs produce <= 5000, but the function must assert this invariant
    assert score_user(120, 10000) <= 5000
