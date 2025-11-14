# Bug Bash: Fixing `score_user` in `buggy_model.py`

This workspace demonstrates identifying and fixing functional bugs in `buggy_model.py`, including missing input validation, incorrect formula, and missing score capping. It includes a pre-fix snapshot (`buggy_model_original.py`), test suites for both the pre-fix and fixed code, environment setup, and reproducible run scripts.

## What I changed
- Implemented strict type checks and value-range validation for `age` and `credits`.
- Corrected the formula to `age * 2 + credits // 10`.
- Enforced a maximum score cap of 5000.
- Created a snapshot file `buggy_model_original.py` to capture the original incorrect behavior.
- Added `tests/test_pre_fix.py` and `tests/test_post_fix.py` to demonstrate broken vs fixed behavior.
- Added setup scripts and run scripts to reproduce the tests and coverage.

## How to reproduce locally (Windows - PowerShell)

1. Create a virtual environment and install dependencies:

   .\run_pre_fix_tests.ps1

2. Run pre-fix tests to capture incorrect behavior:

   .\run_pre_fix_tests.ps1

3. Run scripts to compare outputs around specific inputs:

   python scripts/compare_outputs.py

4. Run post-fix tests and coverage report:

   .\run_tests.ps1

## How to reproduce on macOS/Linux

1. Create venv and install dependencies:

   ./run_tests.sh

2. Optionally run pre-fix tests:

   ./run_pre_fix_tests.sh

## Files added/changed
- `buggy_model.py` - Fixed implementation
- `buggy_model_original.py` - Snapshot of the original broken file
- `tests/test_pre_fix.py` - Tests asserting old/wrong behavior
- `tests/test_post_fix.py` - Tests asserting correct behavior after fix
- `scripts/compare_outputs.py` - Print original vs fixed outputs for sample cases
- `requirements.txt` - Test dependencies
- `run_pre_fix_tests.ps1`, `run_tests.ps1`, `run_all.ps1`, `run_tests.sh`, `run_pre_fix_tests.sh` - Scripts to run tests

## Test coverage
Post-fix tests show coverage for `buggy_model.py`; run `./run_tests.ps1` to see a human-friendly coverage summary.

---
Notes:
- The fixed function enforces strict types and will raise `TypeError` for non-int inputs and `ValueError` for out-of-range values.
- The maximum allowed score: `5000`.
