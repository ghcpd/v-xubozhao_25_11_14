# Run pre-fix tests against the snapshot and then run post-fix tests after the fix
.\run_pre_fix_tests.ps1
# Pause to allow reviewing logs
Read-Host -Prompt 'Press Enter to continue to run post-fix tests after the fix has been applied'
.\run_tests.ps1
