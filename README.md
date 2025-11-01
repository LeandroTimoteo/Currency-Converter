# Currency Converter - Web

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

A simple web-based currency converter built with Flask. Convert between major currencies and cryptocurrencies with an intuitive interface.

## Getting Started

1. Clone the repository:
```bat
git clone https://github.com/LeandroTimoteo/Currency-Converter.git
cd Currency-Converter
```

2. Create a virtual environment (recommended):
```bat
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bat
pip install -r requirements.txt
```

4. Run the application:
```bat
python main.py
```

The app will automatically open in your default browser at http://localhost:5000

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## Deployment Options

Option 1 — Render (recommended for simplicity):
- Create a free account at https://render.com
- Connect your GitHub repository and create a new Web Service
- Branch: `main`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn main:app`
- Render automatically selects Python version from `runtime.txt`

Option 2 — Railway / Fly / Replit:
- Railway: create a project, connect repository, and use `gunicorn main:app` as start command
- Replit: create a Python Repl, upload/commit files, and set run command to `gunicorn main:app`

## API

POST /api/convert  
Content-Type: application/json  
Body example:

```json
{"amount":100, "from":"USD", "to":"EUR"}
```

Response:

```json
{"result": 93.0, "from":"USD", "to":"EUR"}
```

## Features
- Convert between major currencies (USD, EUR, GBP, JPY, etc.)
- Support for cryptocurrencies (BTC, ETH, TRX)
- Mobile-friendly interface
- Simple REST API
- Easy deployment to cloud platforms

## Notes
- Exchange rates are hardcoded in `main.py`. For production use, integrate with an exchange rate service (e.g., exchangerate.host, openexchangerates)
- Key files: `requirements.txt`, `Procfile`, `runtime.txt`
- The app automatically opens in your default browser when run locally
- Supports both decimal point and comma as decimal separators

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Leandro Timoteo - [@LeandroTimoteo](https://github.com/LeandroTimoteo)

Project Link: [https://github.com/LeandroTimoteo/Currency-Converter](https://github.com/LeandroTimoteo/Currency-Converter)
