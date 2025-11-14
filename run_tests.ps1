#!/usr/bin/env pwsh
# Test execution script with coverage reporting

Write-Host "=" -ForegroundColor Cyan
Write-Host "Running Test Suite with Coverage" -ForegroundColor Cyan
Write-Host "=" -ForegroundColor Cyan

# Demonstrate original bugs
Write-Host "`n[1] DEMONSTRATING ORIGINAL BUGS" -ForegroundColor Yellow
Write-Host "-" * 80
python demonstrate_bugs.py

# Run tests
Write-Host "`n[2] RUNNING PYTEST SUITE" -ForegroundColor Yellow
Write-Host "-" * 80
pytest test_score_user.py -v --tb=short --cov=buggy_model_fixed --cov-report=term-missing --cov-report=html

# Show coverage report location
Write-Host "`n[3] COVERAGE REPORT GENERATED" -ForegroundColor Green
Write-Host "HTML coverage report: htmlcov/index.html" -ForegroundColor Green

# Demonstrate fixes
Write-Host "`n[4] DEMONSTRATING FIXED IMPLEMENTATION" -ForegroundColor Yellow
Write-Host "-" * 80
python demonstrate_fixes.py

Write-Host "`n" -ForegroundColor Cyan
Write-Host "=" -ForegroundColor Cyan
Write-Host "Test execution complete!" -ForegroundColor Green
Write-Host "=" -ForegroundColor Cyan
