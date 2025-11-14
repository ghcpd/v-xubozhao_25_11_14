import json
from pathlib import Path

import pytest

from buggy_model import score_user


DATA_PATH = Path(__file__).parent / "data" / "score_cases.json"

with DATA_PATH.open("r", encoding="utf-8") as stream:
    CASES = json.load(stream)


@pytest.mark.parametrize("age,credits,expected", [
    (case["age"], case["credits"], case["expected"])
    for case in CASES["valid_cases"]
])
def test_score_user_valid_cases(age, credits, expected):
    assert score_user(age, credits) == expected


@pytest.mark.parametrize("age,credits", [
    (case["age"], case["credits"])
    for case in CASES["invalid_cases"]
])
def test_score_user_rejects_invalid_inputs(age, credits):
    with pytest.raises(ValueError):
        score_user(age, credits)


@pytest.mark.parametrize(
    "age,credits",
    [
        ("20", 300),
        (40, 15.5),
    ],
)
def test_score_user_rejects_non_integer_values(age, credits):
    with pytest.raises(TypeError):
        score_user(age, credits)


def test_score_user_caps_output():
    """Guardrail to ensure future formula changes cannot exceed the hard cap."""
    capped_value = score_user(120, 10000)
    assert capped_value <= 5000
