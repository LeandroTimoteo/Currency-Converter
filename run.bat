@echo off
REM Create a venv (if missing), install requirements and run the Flask app (foreground)
IF NOT EXIST .venv (
    python -m venv .venv
    .venv\Scripts\pip install --upgrade pip
    .venv\Scripts\pip install -r requirements.txt
)

@echo Activating virtual environment...
call .venv\Scripts\activate

@echo Starting app (development server)...
python main.py
