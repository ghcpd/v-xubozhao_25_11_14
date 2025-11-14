# Run full demonstration: pre-fix demo, tests, post-fix
Write-Host 'Setting up environment and installing dependencies...'
.\setup_env.ps1

Write-Host 'Running pre-fix demo to show broken behavior...'
.\run_before_fix.ps1

Write-Host 'Running tests (this will validate fixed behavior)...'
.\run_tests.ps1

Write-Host 'Running post-fix demo to show corrected behavior...'
.\run_after_fix.ps1

Write-Host 'Completed.'
