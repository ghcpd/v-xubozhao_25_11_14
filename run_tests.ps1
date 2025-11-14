# Powershell script to set up a venv and run tests with coverage
$venvPath = Join-Path $PSScriptRoot ".venv"

if (-Not (Test-Path $venvPath)) {
    python -m venv $venvPath
}

$python = Join-Path $venvPath "Scripts\python.exe"
$pip = Join-Path $venvPath "Scripts\pip.exe"

& $pip install --upgrade pip
& $pip install -r "$(Join-Path $PSScriptRoot 'requirements.txt')"

# Run pytest with coverage and write outputs to files
$covReport = Join-Path $PSScriptRoot "coverage_report.txt"
$testReport = Join-Path $PSScriptRoot "pytest_output.txt"

& $python -m pytest --maxfail=1 --disable-warnings -q --cov=. | Tee-Object -FilePath $testReport
& $python -m pytest --disable-warnings --maxfail=1 --cov=. --cov-report=term-missing:skip-covered --cov-report=xml --cov-report=html

Write-Host "Coverage report: $covReport"
