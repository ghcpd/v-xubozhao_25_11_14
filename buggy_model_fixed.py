"""
A simple scoring function for demonstration.
FIXED version with all constraints properly implemented.
"""

def score_user(age: int, credits: int) -> int:
    """
    Compute a user score with proper constraint handling.
    
    Constraints:
    - age must be between 0 and 120
    - credits must be between 0 and 10000
    - final score = age * 2 + credits // 10
    - score cannot exceed 5000

    Args:
        age: User's age (must be 0-120)
        credits: User's credits (must be 0-10000)

    Returns:
        Computed score capped at 5000, or -1 if constraints violated

    Raises:
        ValueError: If inputs violate constraints

    Example:
        age=20, credits=100 → score = 20*2 + 100//10 = 40 + 10 = 50
    """

    # FIX 1: Add proper constraint checks for valid ranges
    if age < 0 or age > 120:
        raise ValueError(f"Age must be between 0 and 120, got {age}")
    
    if credits < 0 or credits > 10000:
        raise ValueError(f"Credits must be between 0 and 10000, got {credits}")

    # FIX 2: Correct formula: age * 2 + credits // 10 (not age + credits)
    score = age * 2 + credits // 10

    # FIX 3: Cap score at maximum value of 5000
    score = min(score, 5000)

    return score
