"""
Demonstrates outputs from the original buggy implementation saved as "buggy_model_original.py".
"""
from buggy_model_original import score_user as original_score

cases = [
    (20, 100),
    (0, 0),
    (120, 10000),
    (30, 95),
    (-5, 100),
    (25, 1000000),
]

if __name__ == "__main__":
    print("Original buggy model outputs:")
    for age, credits in cases:
        try:
            result = original_score(age, credits)
            print(f"age={age}, credits={credits} -> {result}")
        except Exception as e:
            print(f"age={age}, credits={credits} -> raised {type(e).__name__}: {e}")
