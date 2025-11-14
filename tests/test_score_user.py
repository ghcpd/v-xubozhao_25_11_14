import sys
import pathlib

# Ensure the project root is on sys.path so pytest can import top-level modules
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import pytest

from buggy_model import score_user
from buggy_model_original import score_user as score_user_original


def expected_score(age, credits):
    return age * 2 + credits // 10


@pytest.mark.parametrize("age,credits,expected", [
    (20, 100, 50),
    (0, 0, 0),
    (120, 10000, 120 * 2 + 10000 // 10),
    (30, 95, 30 * 2 + 95 // 10),
])
def test_valid_scores(age, credits, expected):
    assert score_user(age, credits) == expected



@pytest.mark.parametrize("age,credits", [
    (-1, 10),
    (10, -10),
    (121, 0),
    (0, 10001),
])
def test_invalid_range_raises(age, credits):
    with pytest.raises(ValueError):
        score_user(age, credits)


def test_invalid_types_raise():
    with pytest.raises(TypeError):
        score_user(20.5, 100)
    with pytest.raises(TypeError):
        score_user(20, "100")


def test_original_has_incorrect_behavior():
    # The original (saved) implementation returns age + credits, which is incorrect for general cases.
    assert score_user_original(20, 100) == 120  # wrong: intended 50
    assert score_user_original(120, 10000) == 10120  # wrong and unbounded
    assert score_user_original(-5, 100) == 95  # wrong: negative age ignored
