#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q --maxfail=1 --disable-warnings --color=yes "$@"
