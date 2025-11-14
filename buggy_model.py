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

    # --- enforce constraint handling and use the intended formula ---
    if not isinstance(age, int) or not isinstance(credits, int):
        raise TypeError("age and credits must be integers")

    if not (0 <= age <= 120):
        raise ValueError("age must be between 0 and 120")

    if not (0 <= credits <= 10000):
        raise ValueError("credits must be between 0 and 10000")

    score = age * 2 + credits // 10
    return min(score, 5000)
