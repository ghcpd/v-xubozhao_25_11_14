# Demonstrates fixed behavior by running post_fix_demo.py and saving output to after_fix.log
$log = Join-Path $PSScriptRoot 'after_fix.log'
python post_fix_demo.py | Out-File -FilePath $log -Encoding utf8
Write-Host "Wrote post-fix log to $log"