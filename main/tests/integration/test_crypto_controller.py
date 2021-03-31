from fastapi.testclient import TestClient
from main.app import app

client = TestClient(app)

def test_get_crypto_stats():
    response = client.get("/crypto/btc-usd/stats")
    assert response.status_code == 200
    payload = response.json()
    assert payload['last'] >= 40000
