# Run the pre-fix tests showing failing or incorrect behavior
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q tests/test_pre_fix.py --maxfail=1
