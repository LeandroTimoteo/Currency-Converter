import json
import os
import sys

# Garantir que o diretório do projeto esteja no path para importar main
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from main import app


def test_api_convert_success():
    client = app.test_client()
    payload = {"amount": 100, "from": "BRL", "to": "USD"}
    resp = client.post('/api/convert', data=json.dumps(payload), content_type='application/json')
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'result' in data


def test_api_convert_bad_params():
    client = app.test_client()
    payload = {"amount": "abc", "from": "BRL", "to": "USD"}
    resp = client.post('/api/convert', data=json.dumps(payload), content_type='application/json')
    assert resp.status_code == 400
