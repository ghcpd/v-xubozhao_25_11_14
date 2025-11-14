# Buggy Model Fix and Test Suite

This repository contains a simple demo function `score_user(age, credits)` in `buggy_model.py` with an intentionally buggy implementation. The goal is to fix the function, add tests, and create reproducible scripts for verification.

Files added/modified:
- `buggy_model.py` — fixed implementation
- `buggy_model_original.py` — copy of the original broken implementation (unchanged)
- `tests/test_score_user.py` — pytest test suite
- `requirements.txt` — project dependencies
- `setup_env.ps1` — venv creation & install script (PowerShell for Windows)
- `run_tests.ps1` — script to run tests and generate coverage (PowerShell)
- `pre_fix_demo.py` / `post_fix_demo.py` — demo prints to show behavior before and after fix
- `run_before_fix.ps1`, `run_after_fix.ps1` — scripts to run demos and save logs

Quick commands (Windows PowerShell):

1. Create & activate virtualenv and install dependencies:
   .\setup_env.ps1

2. Run the pre-fix demonstration (reads `buggy_model_original.py`):
   .\run_before_fix.ps1

3. Run the test suite with coverage:
   .\run_tests.ps1

4. Run the post-fix demonstration (reads `buggy_model.py`):
   .\run_after_fix.ps1

Note: The run scripts will create log files `before_fix.log` and `after_fix.log` in the repository root to compare outputs.
