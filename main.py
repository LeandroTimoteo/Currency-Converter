from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

# Taxas de câmbio em relação ao dólar americano (USD)
RATES = {
    "USD": 1.0,       # Dólar Americano
    "EUR": 0.93,      # Euro
    "BRL": 5.10,      # Real Brasileiro
    "GBP": 0.79,      # Libra Esterlina
    "JPY": 151.45,    # Iene Japonês
    "CAD": 1.37,      # Dólar Canadense
    "AUD": 1.53,      # Dólar Australiano
    "CNY": 7.23       # Yuan Chinês
}


def convert_value(amount: float, src: str, dst: str) -> float:
    """Converte `amount` de `src` para `dst` usando RATES."""
    src = src.upper()
    dst = dst.upper()
    if src not in RATES:
        raise ValueError(f"Moeda de origem não suportada: {src}")
    if dst not in RATES:
        raise ValueError(f"Moeda de destino não suportada: {dst}")
    if amount < 0:
        raise ValueError("O valor deve ser não negativo")

    # Converte para USD e depois para a moeda destino
    valor_em_usd = amount / RATES[src]
    resultado = valor_em_usd * RATES[dst]
    return resultado


@app.route("/")
def index():
    """Página principal com formulário simples."""
    return render_template("index.html", moedas=sorted(RATES.keys()))


@app.route("/convert", methods=["POST"])
def convert_form():
    origem = request.form.get("origem", "").upper()
    destino = request.form.get("destino", "").upper()
    valor_raw = request.form.get("valor", "")
    error = None
    resultado = None

    try:
        valor = float(valor_raw.replace(",", "."))
        resultado = convert_value(valor, origem, destino)
    except Exception as e:
        error = str(e)

    return render_template("result.html", origem=origem, destino=destino, valor=valor_raw, resultado=resultado, error=error)


@app.route("/api/convert", methods=["POST"])
def api_convert():
    """API JSON: {"amount": 10, "from": "BRL", "to": "USD"} -> {"result": 1.96} """
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "JSON inválido"}), 400

    try:
        amount = float(data.get("amount"))
        src = data.get("from", "").upper()
        dst = data.get("to", "").upper()
    except Exception:
        return jsonify({"error": "Parâmetros inválidos"}), 400

    try:
        result = convert_value(amount, src, dst)
        return jsonify({"result": result, "from": src, "to": dst})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# Serve a blank response for favicon requests so the browser tab doesn't show a default icon
@app.route('/favicon.ico')
def favicon():
    # Returning 204 No Content prevents browsers from showing a default favicon in many cases.
    return ('', 204)


import webbrowser
import threading

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    url = f"http://127.0.0.1:{port}"

    # Debug mode controlled by FLASK_DEBUG env var (1/true => on)
    debug_env = os.environ.get("FLASK_DEBUG", "0")
    debug = True if debug_env in ("1", "true", "True") else False

    # Evita abrir o navegador duas vezes quando o reloader está ativo.
    # O Werkzeug define WERKZEUG_RUN_MAIN="true" no processo filho.
    if debug and os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        threading.Timer(1.5, lambda: webbrowser.open(url)).start()

    # Em produção, execute via WSGI (gunicorn / waitress). Aqui usamos o servidor embutido.
    app.run(host="0.0.0.0", port=port, debug=debug)

