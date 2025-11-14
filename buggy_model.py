"""
A simple scoring function for demonstration.
BUGS are intentionally included for functional bug testing.
"""

def score_user(age: int, credits: int) -> int:
    """
    Compute a user score.
    
    Constraints (INTENDED, but NOT correctly implemented):
    - age must be between 0 and 120
    - credits must be between 0 and 10000
    - final score = age * 2 + credits // 10
    - score cannot exceed 5000

    Known issues to detect:
    ❌ Missing constraint checks
    ❌ Wrong formula
    ❌ Ignores invalid negative inputs
    ❌ Does not cap the score at the maximum
    
    Example intended behavior:
    age=20, credits=100 → score = 20*2 + 100//10 = 40 + 10 = 50
    """

    # --- BUG 1: negative values ignored ---
    # --- BUG 2: wrong formula (using + instead of *) ---
    # --- BUG 3: score grows without limit ---
    # --- BUG 4: credits mis-handled if large values appear ---

    score = age + credits  # completely wrong formula

    # intentional broken “constraint handling”
    if age > 200:  # meaningless check
        score = -1

    return score
