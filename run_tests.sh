#!/usr/bin/env bash
set -euo pipefail
python -m pytest --cov=buggy_model --cov-report=term-missing --cov-report=xml "$@"