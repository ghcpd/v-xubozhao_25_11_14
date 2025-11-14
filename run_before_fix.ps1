# Demonstrates buggy behavior by running pre_fix_demo.py and saving output to before_fix.log
$log = Join-Path $PSScriptRoot 'before_fix.log'
python pre_fix_demo.py | Out-File -FilePath $log -Encoding utf8
Write-Host "Wrote pre-fix log to $log"