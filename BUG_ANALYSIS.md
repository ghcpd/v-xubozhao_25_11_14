# Bug Bash Analysis: Machine Learning Utility Function

## Executive Summary

This document details the comprehensive analysis, testing, and remediation of functional bugs in the `score_user()` machine learning utility function. Five critical bugs were identified, fixed, and validated through a comprehensive pytest test suite with 100% code coverage.

---

## Bug Analysis

### 🐛 Bug 1: Incorrect Formula (Logic Error)

**Severity:** CRITICAL  
**Category:** Functional Logic Error

**Problem:**
```python
# BUGGY:
score = age + credits  # Wrong formula
```

**Expected Formula:**
```
score = age * 2 + credits // 10
```

**Impact:**
- For input `age=20, credits=100`:
  - **Buggy output:** 120 (20 + 100)
  - **Correct output:** 50 (20*2 + 100//10 = 40 + 10)
  - **Error magnitude:** 240% incorrect

**Root Cause:** Simple arithmetic operation error - used addition instead of multiplication for age component, and didn't divide credits by 10.

---

### 🐛 Bug 2: Missing Negative Age Validation

**Severity:** HIGH  
**Category:** Constraint Violation

**Problem:**
Accepts negative age values without validation.

**Evidence:**
```python
# Input: age=-10, credits=100
# Buggy output: 90 ❌ (should raise error)
# Fixed output: ValueError: Age must be between 0 and 120 ✅
```

**Impact:**
- Allows semantically invalid inputs (people don't have negative age)
- No defensive validation against constraint violations

---

### 🐛 Bug 3: Missing Negative Credits Validation

**Severity:** HIGH  
**Category:** Constraint Violation

**Problem:**
Accepts negative credits values without validation.

**Evidence:**
```python
# Input: age=20, credits=-50
# Buggy output: -30 ❌ (should raise error)
# Fixed output: ValueError: Credits must be between 0 and 10000 ✅
```

**Impact:**
- Produces negative scores from invalid inputs
- No guard against semantically invalid credit values

---

### 🐛 Bug 4: Missing Score Upper Bound Cap

**Severity:** MEDIUM  
**Category:** Constraint Violation

**Problem:**
Score can exceed the specified maximum of 5000.

**Evidence:**
```python
# Input: age=100, credits=5000
# Buggy output: 5100 ❌ (exceeds max of 5000)
# Fixed output: min(score, 5000) ensures cap ✅
```

**Impact:**
- Violates the specified constraint `score cannot exceed 5000`
- Can produce unbounded outputs

---

### 🐛 Bug 5: Meaningless Constraint Check

**Severity:** HIGH  
**Category:** Logic Error

**Problem:**
```python
# BUGGY:
if age > 200:  # meaningless check
    score = -1
```

**Issues:**
- Only checks if `age > 200`, but constraint requires `age <= 120`
- Allows `age=150` to pass (violates constraint)
- Returns -1 only for ages over 200 (wrong sentinel value)

**Evidence:**
```python
# Input: age=150, credits=100
# Buggy output: 250 ❌ (should reject: age > 120)
# Fixed output: ValueError ✅
```

---

## Fixed Implementation

### Corrected Code

```python
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
        Computed score capped at 5000

    Raises:
        ValueError: If inputs violate constraints
    """

    # FIX 1: Proper constraint checks for valid ranges
    if age < 0 or age > 120:
        raise ValueError(f"Age must be between 0 and 120, got {age}")
    
    if credits < 0 or credits > 10000:
        raise ValueError(f"Credits must be between 0 and 10000, got {credits}")

    # FIX 2: Correct formula: age * 2 + credits // 10
    score = age * 2 + credits // 10

    # FIX 3: Cap score at maximum value of 5000
    score = min(score, 5000)

    return score
```

### Changes Summary

| Aspect | Buggy | Fixed |
|--------|-------|-------|
| **Formula** | `age + credits` | `age * 2 + credits // 10` |
| **Age validation** | None | 0-120 range check |
| **Credits validation** | None | 0-10000 range check |
| **Score cap** | None | `min(score, 5000)` |
| **Error handling** | Returns -1 for age>200 | Raises ValueError for constraint violations |

---

## Test Coverage

### Test Suite Statistics

```
Total Tests:        25
Passed:             25 (100%)
Failed:             0
Coverage:           100% (8/8 statements)
```

### Test Categories

#### 1. **Buggy Implementation Tests** (5 tests)
Demonstrate all 5 bugs in original code:
- `test_buggy_wrong_formula()` - Shows 120 instead of 50
- `test_buggy_negative_age_ignored()` - Accepts age=-10
- `test_buggy_negative_credits_ignored()` - Accepts credits=-50
- `test_buggy_no_score_cap()` - Score reaches 5100
- `test_buggy_meaningless_constraint()` - Accepts age=150

#### 2. **Fixed Implementation Tests** (17 tests)
Validate all fixes:

**Formula Tests (4):**
- Basic formula correctness
- Zero values
- Maximum valid inputs
- Various input combinations

**Constraint Validation (9):**
- Negative age rejection
- Age > 120 rejection
- Negative credits rejection
- Credits > 10000 rejection
- Boundary acceptance (0 and max values)

**Score Capping (2):**
- Cap enforcement
- Hypothetical overflow prevention

**Integer Division (2):**
- Proper floor division of credits

#### 3. **Comparison Tests** (3 tests)
Direct buggy vs. fixed comparisons:
- Different outputs for valid inputs
- Constraint bug demonstration

---

## Test Execution Results

### All Tests Pass

```
============================= test session starts =============================
test_score_user.py::TestBuggyImplementation::test_buggy_wrong_formula PASSED
test_score_user.py::TestBuggyImplementation::test_buggy_negative_age_ignored PASSED
test_score_user.py::TestBuggyImplementation::test_buggy_negative_credits_ignored PASSED
test_score_user.py::TestBuggyImplementation::test_buggy_no_score_cap PASSED
test_score_user.py::TestBuggyImplementation::test_buggy_meaningless_constraint PASSED
test_score_user.py::TestFixedImplementation::test_fixed_correct_formula_basic PASSED
test_score_user.py::TestFixedImplementation::test_fixed_correct_formula_zero PASSED
test_score_user.py::TestFixedImplementation::test_fixed_correct_formula_max_valid PASSED
test_score_user.py::TestFixedImplementation::test_fixed_correct_formula_various PASSED
test_score_user.py::TestFixedImplementation::test_fixed_rejects_negative_age PASSED
test_score_user.py::TestFixedImplementation::test_fixed_rejects_age_over_120 PASSED
test_score_user.py::TestFixedImplementation::test_fixed_rejects_age_far_over_120 PASSED
test_score_user.py::TestFixedImplementation::test_fixed_rejects_negative_credits PASSED
test_score_user.py::TestFixedImplementation::test_fixed_rejects_credits_over_10000 PASSED
test_score_user.py::TestFixedImplementation::test_fixed_rejects_credits_far_over_limit PASSED
test_score_user.py::TestFixedImplementation::test_fixed_accepts_boundary_age_0 PASSED
test_score_user.py::TestFixedImplementation::test_fixed_accepts_boundary_age_120 PASSED
test_score_user.py::TestFixedImplementation::test_fixed_accepts_boundary_credits_0 PASSED
test_score_user.py::TestFixedImplementation::test_fixed_accepts_boundary_credits_10000 PASSED
test_score_user.py::TestFixedImplementation::test_fixed_caps_score_at_5000 PASSED
test_score_user.py::TestFixedImplementation::test_fixed_score_cap_hypothetical PASSED
test_score_user.py::TestFixedImplementation::test_fixed_credits_integer_division PASSED
test_score_user.py::TestFixedImplementation::test_fixed_credits_integer_division_various PASSED
test_score_user.py::TestComparison::test_comparison_valid_input PASSED
test_score_user.py::TestComparison::test_comparison_demonstrates_constraint_bug PASSED

============================= 25 passed in 0.10s ==============================
```

### Coverage Report

```
---------- coverage: platform win32, python 3.13.9-final-0 -----------
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
buggy_model_fixed.py       8      0   100%
----------------------------------------------------
TOTAL                      8      0   100%
```

**Interpretation:** Every line of fixed code is executed by the test suite.

---

## Behavior Comparison: Before vs After

### Example 1: Standard Input

```
Input: age=20, credits=100

BUGGY:    20 + 100 = 120 ❌ (240% error)
FIXED:    20*2 + 100//10 = 40 + 10 = 50 ✅
```

### Example 2: Negative Age

```
Input: age=-10, credits=100

BUGGY:    -10 + 100 = 90 ❌ (accepts invalid constraint)
FIXED:    ValueError: Age must be between 0 and 120 ✅
```

### Example 3: Negative Credits

```
Input: age=20, credits=-50

BUGGY:    20 + (-50) = -30 ❌ (produces negative score)
FIXED:    ValueError: Credits must be between 0 and 10000 ✅
```

### Example 4: Large Values

```
Input: age=100, credits=5000

BUGGY:    100 + 5000 = 5100 ❌ (exceeds cap of 5000)
FIXED:    min(200 + 500, 5000) = min(700, 5000) = 700 ✅
```

### Example 5: Out-of-range Age

```
Input: age=150, credits=100

BUGGY:    150 + 100 = 250 ❌ (age > 120 allowed)
FIXED:    ValueError: Age must be between 0 and 120 ✅
```

---

## Files Produced

### Core Files
- **`buggy_model.py`** - Original buggy implementation (provided)
- **`buggy_model_fixed.py`** - Fixed implementation with all corrections

### Test Files
- **`test_score_user.py`** - Comprehensive pytest suite (25 tests, 100% coverage)

### Demonstration Files
- **`demonstrate_bugs.py`** - Shows all 5 bugs with evidence
- **`demonstrate_fixes.py`** - Shows all fixes working correctly

### Infrastructure Files
- **`requirements.txt`** - Python dependencies (pytest, pytest-cov)
- **`setup.ps1`** - Environment setup script
- **`run_tests.ps1`** - Test execution script with coverage

### Documentation
- **`BUG_ANALYSIS.md`** - This comprehensive analysis document

---

## Reproducibility Instructions

### Quick Start

```powershell
# 1. Set up environment
.\setup.ps1

# 2. Run all tests with coverage and demonstrations
.\run_tests.ps1
```

### Individual Commands

```powershell
# Install dependencies
pip install -r requirements.txt

# Demonstrate original bugs
python demonstrate_bugs.py

# Run test suite
pytest test_score_user.py -v

# Run with coverage report
pytest test_score_user.py --cov=buggy_model_fixed --cov-report=term-missing

# Demonstrate fixes
python demonstrate_fixes.py
```

---

## Conclusion

All five functional bugs in the `score_user()` function have been:

1. ✅ **Identified** - Logic errors and constraint violations documented
2. ✅ **Fixed** - Corrected implementation with proper validation
3. ✅ **Tested** - 25 comprehensive tests with 100% code coverage
4. ✅ **Validated** - Clear evidence of incorrect vs. corrected behavior
5. ✅ **Reproducible** - Complete environment setup and test infrastructure

The fixed implementation now correctly:
- Applies the right formula: `age * 2 + credits // 10`
- Validates age range: 0-120
- Validates credits range: 0-10000
- Caps score at maximum: 5000
- Handles all edge cases and boundary conditions

