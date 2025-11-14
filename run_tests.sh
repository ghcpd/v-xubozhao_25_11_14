#!/usr/bin/env bash
set -euo pipefail
python scripts/generate_test_data.py
coverage run --branch -m pytest
coverage report -m | tee coverage_report.txt
