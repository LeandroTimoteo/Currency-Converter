@echo off
REM Create venv and deps if missing, then start the app in a new window (background)
IF NOT EXIST .venv (
    python -m venv .venv
    .venv\Scripts\pip install --upgrade pip
    .venv\Scripts\pip install -r requirements.txt
)

REM Use START to run in a new window so the current terminal is freed
start "MOEDA.PY" cmd /c ".venv\Scripts\python main.py"
