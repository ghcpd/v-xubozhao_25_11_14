"""
Script to demonstrate the bugs in the original implementation.
This script shows incorrect behavior before fixes are applied.
"""

from buggy_model import score_user as buggy_score_user

def demonstrate_bugs():
    """Show all bugs in the original implementation."""
    
    print("=" * 80)
    print("DEMONSTRATING BUGS IN ORIGINAL IMPLEMENTATION")
    print("=" * 80)
    
    print("\n[BUG 1] Wrong Formula - Uses addition instead of multiplication")
    print("-" * 80)
    age, credits = 20, 100
    result = buggy_score_user(age, credits)
    print(f"Input:    age={age}, credits={credits}")
    print(f"Buggy:    age + credits = {age} + {credits} = {result}")
    print(f"Expected: age*2 + credits//10 = {age}*2 + {credits}//10 = {age*2 + credits//10}")
    print(f"❌ WRONG: Got {result}, expected {age*2 + credits//10}")
    
    print("\n[BUG 2] Negative Age Not Validated")
    print("-" * 80)
    age, credits = -10, 100
    result = buggy_score_user(age, credits)
    print(f"Input:    age={age}, credits={credits}")
    print(f"Result:   {result}")
    print(f"❌ WRONG: Accepted negative age (should reject)")
    
    print("\n[BUG 3] Negative Credits Not Validated")
    print("-" * 80)
    age, credits = 20, -50
    result = buggy_score_user(age, credits)
    print(f"Input:    age={age}, credits={credits}")
    print(f"Result:   {result}")
    print(f"❌ WRONG: Accepted negative credits (should reject)")
    
    print("\n[BUG 4] Score Not Capped at 5000")
    print("-" * 80)
    age, credits = 100, 5000
    result = buggy_score_user(age, credits)
    print(f"Input:    age={age}, credits={credits}")
    print(f"Result:   {result}")
    print(f"❌ WRONG: Score {result} exceeds max of 5000")
    
    print("\n[BUG 5] Meaningless Constraint Check (age > 200)")
    print("-" * 80)
    age, credits = 150, 100
    result = buggy_score_user(age, credits)
    print(f"Input:    age={age}, credits={credits}")
    print(f"Result:   {result}")
    print(f"❌ WRONG: Accepts age=150 (should limit to 120)")
    print(f"  Only checks age > 200, which is meaningless")
    
    print("\n" + "=" * 80)
    print("All bugs confirmed in original implementation")
    print("=" * 80)

if __name__ == "__main__":
    demonstrate_bugs()
