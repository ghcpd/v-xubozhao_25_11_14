import os
import sys

# Ensure repo root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from buggy_model_original import score_user as original_score
from buggy_model import score_user as fixed_score

cases = [
    (20, 100),
    (-10, 50),
    (30, 200000),
]

for age, credits in cases:
    try:
        o = original_score(age, credits)
    except Exception as e:
        o = f"ERROR: {type(e).__name__}: {e}"

    try:
        f = fixed_score(age, credits)
    except Exception as e:
        f = f"ERROR: {type(e).__name__}: {e}"

    print(f"Input: age={age}, credits={credits} -> original: {o} | fixed: {f}")
