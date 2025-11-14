"""Generate test cases by parsing buggy_model.py and creating reproducible inputs."""
from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import buggy_model

DATA_PATH = BASE_DIR / "tests" / "test_data.json"
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

EXAMPLE_PATTERN = re.compile(r"age=(\d+), credits=(\d+)")

def _parse_docstring_example() -> List[Dict[str, Any]]:
    doc = buggy_model.score_user.__doc__ or ""
    matches = EXAMPLE_PATTERN.findall(doc)
    examples: List[Dict[str, Any]] = []
    for age_str, credits_str in matches:
        age = int(age_str)
        credits = int(credits_str)
        expected = min(age * 2 + credits // 10, 5000)
        examples.append({"age": age, "credits": credits, "expected": expected})
    return examples


def _build_invalid_cases() -> List[Dict[str, Any]]:
    return [
        {
            "age": -1,
            "credits": 50,
            "error_contains": "age must be between 0 and 120",
        },
        {
            "age": 121,
            "credits": 0,
            "error_contains": "age must be between 0 and 120",
        },
        {
            "age": 20,
            "credits": -10,
            "error_contains": "credits must be between 0 and 10000",
        },
        {
            "age": 20,
            "credits": 10001,
            "error_contains": "credits must be between 0 and 10000",
        },
    ]


def _build_random_valid_cases(seed: int = 0, count: int = 3) -> List[Dict[str, Any]]:
    rng = random.Random(seed)
    cases: List[Dict[str, Any]] = []
    for _ in range(count):
        age = rng.randint(0, 120)
        credits = rng.randint(0, 10000)
        cases.append(
            {
                "age": age,
                "credits": credits,
                "expected": buggy_model.score_user(age, credits),
            }
        )
    return cases


def main() -> None:
    valid_cases: List[Dict[str, Any]] = []
    valid_cases.extend(_parse_docstring_example())
    for age, credits in [(0, 0), (120, 10000)]:
        valid_cases.append(
            {"age": age, "credits": credits, "expected": min(age * 2 + credits // 10, 5000)}
        )
    valid_cases.extend(_build_random_valid_cases())

    data = {
        "valid": valid_cases,
        "invalid": _build_invalid_cases(),
    }

    DATA_PATH.write_text(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
