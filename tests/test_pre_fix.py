import os
import sys
import pytest

# Ensure the project root is on sys.path so tests can import modules from the repository
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buggy_model_original import score_user


def test_pre_fix_wrong_formula_example():
    # Original (wrong) implementation returns age + credits
    result = score_user(20, 100)
    assert result == 20 + 100, "Pre-fix snapshot should use wrong formula age+credits"


def test_pre_fix_negative_age_ignored():
    # Original incorrectly ignores invalid negative age and returns sum
    result = score_user(-10, 50)
    assert result == -10 + 50


def test_pre_fix_no_constraints_on_credits():
    # Original accepts large credit values and returns sum without cap
    result = score_user(30, 200000)
    assert result == 30 + 200000
