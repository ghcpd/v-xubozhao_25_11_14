# Run the post-fix pytest suite and generate a coverage report
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q --cov=./ --cov-report=term-missing
