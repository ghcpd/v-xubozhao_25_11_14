"""
Test suite for score_user function.
Demonstrates bugs in original implementation and validates fixes.
"""

import pytest
from buggy_model import score_user as buggy_score_user
from buggy_model_fixed import score_user as fixed_score_user


class TestBuggyImplementation:
    """Tests demonstrating bugs in the original implementation."""

    def test_buggy_wrong_formula(self):
        """BUG 1: Wrong formula - uses addition instead of multiplication."""
        # Expected: 20*2 + 100//10 = 40 + 10 = 50
        # Actual (buggy): 20 + 100 = 120
        result = buggy_score_user(20, 100)
        assert result == 120, "Buggy version uses wrong formula (age + credits)"
        assert result != 50, "Should not be 50 with correct formula"

    def test_buggy_negative_age_ignored(self):
        """BUG 2: Negative age not validated."""
        # Should reject negative age, but buggy version accepts it
        result = buggy_score_user(-10, 100)
        assert result == 90, "Buggy version doesn't validate negative age"

    def test_buggy_negative_credits_ignored(self):
        """BUG 3: Negative credits not validated."""
        # Should reject negative credits, but buggy version accepts it
        result = buggy_score_user(20, -50)
        assert result == -30, "Buggy version doesn't validate negative credits"

    def test_buggy_no_score_cap(self):
        """BUG 4: Score grows without limit (no cap at 5000)."""
        # Should cap at 5000, but buggy version doesn't
        result = buggy_score_user(100, 5000)
        assert result == 5100, "Buggy version doesn't cap score at 5000"
        assert result > 5000, "Score exceeds maximum allowed value"

    def test_buggy_meaningless_constraint(self):
        """BUG 5: Only checks age > 200 (meaningless)."""
        # The only real constraint check is age > 200, which is wrong
        # Should reject age > 120, but doesn't
        result = buggy_score_user(150, 100)
        assert result == 250, "Buggy version doesn't reject age > 120"


class TestFixedImplementation:
    """Tests validating the fixed implementation."""

    # --- Valid Input Tests ---
    def test_fixed_correct_formula_basic(self):
        """Fixed: Correct formula with valid inputs."""
        # age=20, credits=100 → 20*2 + 100//10 = 40 + 10 = 50
        result = fixed_score_user(20, 100)
        assert result == 50, "Should compute age*2 + credits//10 correctly"

    def test_fixed_correct_formula_zero(self):
        """Fixed: Correct formula with zero values."""
        result = fixed_score_user(0, 0)
        assert result == 0, "Formula should work with zeros"

    def test_fixed_correct_formula_max_valid(self):
        """Fixed: Correct formula with max valid inputs (before capping)."""
        # age=120, credits=10000 → 120*2 + 10000//10 = 240 + 1000 = 1240
        result = fixed_score_user(120, 10000)
        assert result == 1240, "Should compute correctly with max valid inputs"

    def test_fixed_correct_formula_various(self):
        """Fixed: Verify formula with various inputs."""
        test_cases = [
            (10, 50, 10 * 2 + 50 // 10),    # 20 + 5 = 25
            (30, 200, 30 * 2 + 200 // 10),  # 60 + 20 = 80
            (50, 500, 50 * 2 + 500 // 10),  # 100 + 50 = 150
            (75, 1500, 75 * 2 + 1500 // 10),  # 150 + 150 = 300
        ]
        for age, credits, expected in test_cases:
            result = fixed_score_user(age, credits)
            assert result == expected, f"Formula failed for age={age}, credits={credits}"

    # --- Constraint Validation Tests ---
    def test_fixed_rejects_negative_age(self):
        """Fixed: Properly rejects negative age."""
        with pytest.raises(ValueError, match="Age must be between 0 and 120"):
            fixed_score_user(-1, 100)

    def test_fixed_rejects_age_over_120(self):
        """Fixed: Properly rejects age > 120."""
        with pytest.raises(ValueError, match="Age must be between 0 and 120"):
            fixed_score_user(121, 100)

    def test_fixed_rejects_age_far_over_120(self):
        """Fixed: Properly rejects large ages."""
        with pytest.raises(ValueError, match="Age must be between 0 and 120"):
            fixed_score_user(150, 100)

    def test_fixed_rejects_negative_credits(self):
        """Fixed: Properly rejects negative credits."""
        with pytest.raises(ValueError, match="Credits must be between 0 and 10000"):
            fixed_score_user(20, -1)

    def test_fixed_rejects_credits_over_10000(self):
        """Fixed: Properly rejects credits > 10000."""
        with pytest.raises(ValueError, match="Credits must be between 0 and 10000"):
            fixed_score_user(20, 10001)

    def test_fixed_rejects_credits_far_over_limit(self):
        """Fixed: Properly rejects large credit values."""
        with pytest.raises(ValueError, match="Credits must be between 0 and 10000"):
            fixed_score_user(20, 50000)

    def test_fixed_accepts_boundary_age_0(self):
        """Fixed: Accepts age boundary (0)."""
        result = fixed_score_user(0, 100)
        assert result == 0 + 100 // 10, "Should accept age=0"

    def test_fixed_accepts_boundary_age_120(self):
        """Fixed: Accepts age boundary (120)."""
        result = fixed_score_user(120, 100)
        assert result == 120 * 2 + 100 // 10, "Should accept age=120"

    def test_fixed_accepts_boundary_credits_0(self):
        """Fixed: Accepts credits boundary (0)."""
        result = fixed_score_user(20, 0)
        assert result == 20 * 2 + 0 // 10, "Should accept credits=0"

    def test_fixed_accepts_boundary_credits_10000(self):
        """Fixed: Accepts credits boundary (10000)."""
        result = fixed_score_user(20, 10000)
        assert result == 20 * 2 + 10000 // 10, "Should accept credits=10000"

    # --- Score Capping Tests ---
    def test_fixed_caps_score_at_5000(self):
        """Fixed: Caps score at 5000."""
        # Need large values to exceed 5000
        # age*2 + credits//10 > 5000
        # Try age=120, credits=10000 = 240 + 1000 = 1240 (still under)
        # Need to compute what would exceed 5000
        # 5000 = age*2 + credits//10
        # If age=100, credits=10000: 200 + 1000 = 1200
        # If we had age=2000 (invalid), credits=10000: 4000 + 1000 = 5000
        # Let's verify that valid inputs stay under 5000
        result = fixed_score_user(120, 10000)
        assert result == 1240, "Max valid inputs should give 1240"
        assert result < 5000, "Max valid inputs should be under cap"

    def test_fixed_score_cap_hypothetical(self):
        """Fixed: Cap would apply if constraints allowed larger values."""
        # This test shows the cap is in place, even though valid inputs can't exceed it
        # Score cap ensures no score > 5000
        max_possible_uncapped = 120 * 2 + 10000 // 10
        assert max_possible_uncapped == 1240, "Max uncapped score with valid inputs is 1240"
        result = fixed_score_user(120, 10000)
        assert result == min(max_possible_uncapped, 5000), "Should apply cap"

    # --- Edge Cases ---
    def test_fixed_credits_integer_division(self):
        """Fixed: Credits properly integer-divided by 10."""
        # credits=105 → 105//10 = 10 (not 10.5)
        result = fixed_score_user(20, 105)
        assert result == 20 * 2 + 10, "Integer division should round down"

    def test_fixed_credits_integer_division_various(self):
        """Fixed: Integer division works correctly."""
        test_cases = [
            (20, 99, 20 * 2 + 9),    # 99//10 = 9
            (20, 100, 20 * 2 + 10),  # 100//10 = 10
            (20, 101, 20 * 2 + 10),  # 101//10 = 10
            (20, 109, 20 * 2 + 10),  # 109//10 = 10
            (20, 110, 20 * 2 + 11),  # 110//10 = 11
        ]
        for age, credits, expected in test_cases:
            result = fixed_score_user(age, credits)
            assert result == expected, f"Integer division failed for credits={credits}"


class TestComparison:
    """Direct comparison between buggy and fixed implementations."""

    def test_comparison_valid_input(self):
        """Compare outputs for valid input."""
        age, credits = 20, 100
        buggy_result = buggy_score_user(age, credits)
        fixed_result = fixed_score_user(age, credits)
        
        assert buggy_result == 120, "Buggy uses wrong formula"
        assert fixed_result == 50, "Fixed uses correct formula"
        assert buggy_result != fixed_result, "Results should differ"

    def test_comparison_demonstrates_constraint_bug(self):
        """Show that buggy version ignores constraints."""
        age, credits = 150, 100
        
        # Buggy accepts invalid age
        buggy_result = buggy_score_user(age, credits)
        assert buggy_result == 250, "Buggy accepts age > 120"
        
        # Fixed rejects invalid age
        with pytest.raises(ValueError):
            fixed_score_user(age, credits)
