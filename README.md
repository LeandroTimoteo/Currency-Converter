# Conversor de Moedas - Web

Este repositório contém uma versão web simples (Flask) do conversor de moedas.

## Como rodar localmente

1. Crie um ambiente virtual (recomendado):

```bat
python -m venv .venv
.venv\Scripts\activate
```

2. Instale dependências:

```bat
pip install -r requirements.txt
```

3. Rode a aplicação:

```bat
python main.py
```

Acesse http://localhost:5000

## Deploy gratuito (opções)

Opção 1 — Render (recomendado pela simplicidade):
- Crie uma conta grátis em https://render.com
- Conecte seu repositório GitHub e crie um novo Web Service
- Branch: `main`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn main:app`
- Render seleciona automaticamente a versão Python via `runtime.txt`.

Opção 2 — Railway / Fly / Replit:
- Railway: crie um projeto, conecte o repositório e use `gunicorn main:app` como start command.
- Replit: crie um Repl Python, faça upload/commit dos arquivos e configure o run command para `gunicorn main:app`.

## API

POST /api/convert
Content-Type: application/json
Body example:

```json
{"amount":100, "from":"BRL", "to":"USD"}
```

Response:

```json
{"result": 19.6078, "from":"BRL", "to":"USD"}
```

## Observações
- As taxas estão hardcoded no arquivo `main.py`. Para produção recomendo integrar com um serviço de câmbio (ex: exchangerate.host, openexchangerates).
- Arquivos importantes: `requirements.txt`, `Procfile`, `runtime.txt`.
