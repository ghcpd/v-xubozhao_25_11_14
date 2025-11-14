#!/usr/bin/env bash
set -e
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pytest --maxfail=1 --disable-warnings -q --cov=.
pytest --disable-warnings --maxfail=1 --cov=. --cov-report=term-missing:skip-covered --cov-report=xml --cov-report=html
