#!/usr/bin/env pwsh
# Setup script for bug bash testing environment

Write-Host "=" -ForegroundColor Cyan
Write-Host "Setting up Bug Bash Testing Environment" -ForegroundColor Cyan
Write-Host "=" -ForegroundColor Cyan

# Check Python is available
Write-Host "`n[1] Checking Python installation..." -ForegroundColor Yellow
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Python not found. Please install Python 3.7+" -ForegroundColor Red
    exit 1
}

# Install requirements
Write-Host "`n[2] Installing test dependencies..." -ForegroundColor Yellow
pip install --quiet -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install requirements" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Dependencies installed" -ForegroundColor Green

Write-Host "`n[3] Environment setup complete" -ForegroundColor Green
Write-Host "`nYou can now run:" -ForegroundColor Cyan
Write-Host "  - .\run_tests.ps1    (Run all tests with coverage)" -ForegroundColor Cyan
Write-Host "  - python demonstrate_bugs.py" -ForegroundColor Cyan
Write-Host "  - python demonstrate_fixes.py" -ForegroundColor Cyan
