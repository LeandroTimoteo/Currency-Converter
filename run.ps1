# PowerShell script: create a venv (if missing), install deps, run the app
$venvPath = Join-Path $PSScriptRoot '.venv'
if (-not (Test-Path $venvPath)) {
    python -m venv .venv
    & .venv\Scripts\pip.exe install --upgrade pip
    & .venv\Scripts\pip.exe install -r requirements.txt
}

Write-Output 'Activating virtual environment...'
. .venv\Scripts\Activate.ps1

Write-Output 'Starting app (development server)...'
python main.py
