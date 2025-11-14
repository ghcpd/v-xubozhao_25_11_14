from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from buggy_model import score_user

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "test_data.json"
SCRIPT_PATH = Path(__file__).resolve().parent.parent / "scripts" / "generate_test_data.py"


def _ensure_test_data() -> dict:
    if not DATA_PATH.exists():
        subprocess.run([sys.executable, str(SCRIPT_PATH)], check=True)
    return json.loads(DATA_PATH.read_text())


@pytest.fixture(scope="module")
def test_data() -> dict:
    return _ensure_test_data()


def test_valid_scores(test_data):
    for case in test_data["valid"]:
        assert score_user(case["age"], case["credits"]) == case["expected"]


def test_invalid_scores(test_data):
    for case in test_data["invalid"]:
        with pytest.raises(ValueError) as excinfo:
            score_user(case["age"], case["credits"])
        assert case["error_contains"] in str(excinfo.value)


def test_type_errors():
    with pytest.raises(TypeError):
        score_user(20.5, 100)
    with pytest.raises(TypeError):
        score_user(20, "100")


def test_score_matches_formula_and_cap():
    sample_inputs = [(0, 0), (20, 100), (100, 5000), (120, 10000)]
    for age, credits in sample_inputs:
        expected = min(age * 2 + credits // 10, 5000)
        assert score_user(age, credits) == expected
