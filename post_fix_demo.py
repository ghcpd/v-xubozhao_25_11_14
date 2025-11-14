"""
Demonstrates outputs from the corrected implementation in "buggy_model.py".
"""
from buggy_model import score_user

cases = [
    (20, 100),
    (0, 0),
    (120, 10000),
    (30, 95),
    (-5, 100),
    (25, 1000000),
]

if __name__ == "__main__":
    print("Fixed model outputs:")
    for age, credits in cases:
        try:
            result = score_user(age, credits)
            print(f"age={age}, credits={credits} -> {result}")
        except Exception as e:
            print(f"age={age}, credits={credits} -> raised {type(e).__name__}: {e}")
