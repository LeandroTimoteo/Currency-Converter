# Currency Converter Web App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Mobile-friendly](https://img.shields.io/badge/Mobile-friendly-brightgreen.svg)](https://github.com/LeandroTimoteo/Currency-Converter)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/LeandroTimoteo/Currency-Converter/graphs/commit-activity)

A modern and efficient currency converter web application built with Flask. Features real-time conversion between major currencies and popular cryptocurrencies through an intuitive, mobile-friendly interface.

## Key Features

- 💱 Real-time conversion of major world currencies
- ₿ Support for popular cryptocurrencies (BTC, ETH, TRX)
- 📱 Responsive, mobile-friendly interface
- 🚀 Simple and intuitive REST API
- ⚡ Fast and efficient performance
- 🔒 Secure and reliable conversions
- 🌐 Easy cloud platform deployment

## Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/LeandroTimoteo/Currency-Converter.git
cd Currency-Converter
```

2. **Set up Python environment:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Launch the application:**
```bash
python main.py
```

The application will automatically open in your default browser at `http://localhost:5000`

## REST API

### Convert Currency
```http
POST /api/convert
Content-Type: application/json
```

**Request:**
```json
{
    "amount": 100,
    "from": "USD",
    "to": "EUR"
}
```

**Response:**
```json
{
    "result": 93.0,
    "from": "USD",
    "to": "EUR"
}
```

## Deployment

### Option 1: Render (Recommended)
1. Create a free account at [Render](https://render.com)
2. Connect your GitHub repository
3. Create a new Web Service with:
   - Branch: `main`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn main:app`

### Option 2: Alternative Platforms
- **Railway:** Create project, connect repository, use `gunicorn main:app`
- **Replit:** Create Python Repl, upload files, set run command to `gunicorn main:app`

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

Please ensure your PR adheres to our coding standards and includes appropriate tests.

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

## Planned Improvements

These are the current issues we're tracking for future development:

1. Real-time Exchange Rates Integration
   - Integrate with exchange rate API (e.g., exchangerate.host)
   - Replace hardcoded rates with live data
   - Add fallback mechanism for API failures
   
2. Enhanced Security Features
   - Implement rate limiting
   - Add request validation
   - Implement API key authentication for REST endpoints

3. Additional Features
   - Add historical exchange rate charts
   - Support more cryptocurrencies
   - Implement currency conversion history
   - Add favorite currencies feature

4. Testing and Documentation
   - Add unit tests for API endpoints
   - Implement integration tests
   - Improve API documentation with Swagger/OpenAPI
   
Want to contribute? Pick an issue and submit a pull request!

## Development Notes

### Important Information
- Exchange rates are currently hardcoded in `main.py`
- For production, integrate with an exchange rate API (e.g., exchangerate.host, openexchangerates)
- Browser auto-launch feature enabled for local development
- Supports international number formats (both decimal point and comma)

### Key Files
- `requirements.txt`: Project dependencies
- `Procfile`: Cloud platform configuration
- `runtime.txt`: Python version specification
- `main.py`: Core application logic
- `templates/`: HTML templates

## Author

**Leandro Timoteo Silva**  
Senior Systems Analyst

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leandro-timóteo-ads)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/LeandroTimoteo)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:leandrinhots6@gmail.com)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5583987830223)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who have helped shape this project
- Special thanks to the Flask community for the excellent framework
- Developed by Leandro Timoteo
