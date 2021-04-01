from unittest.mock import AsyncMock
from fastapi.testclient import TestClient
from main.app import app
from main.entities.crypto_stats import CryptoStats
from main.entities.crypto_predict import CryptoPredict
from main.client.cryptostats.crypto_stats_client import CryptoStatsClient
from main.dependencies.crypto_stats_client import crypto_stats_client
from main.client.predict.predict_client import PredictClient
from main.dependencies.crypto_predict_client import crypto_predict_client

client = TestClient(app)

# Override dependency with a mock
def override_crypto_stats_client () -> CryptoStatsClient:
    # Create the mock
    mock = CryptoStatsClient()
    mock.get_crypto_trading_stats = AsyncMock(return_value=CryptoStats(last=1.0))
    return mock

# Override R Client dependency with a mock
def override_crypto_predict_client () -> CryptoStatsClient:
    # Create the mock
    mock = PredictClient()
    mock.crypto_predict = AsyncMock(return_value=CryptoPredict(product='btc-usd', current_price='1.0', forecasted_price='2.0'))
    return mock

# Test with mocked client
def test_get_crypto_stats_mocked():
    # Override inside function code or in pre-test or you will have side effect in other tests
    app.dependency_overrides[crypto_stats_client] = override_crypto_stats_client

    response = client.get("/crypto/btc-usd/stats")
    assert response.status_code == 200
    payload = response.json()
    assert payload['last'] == 1.0

# Test with mocked client
def test_get_crypto_predict_mocked():
    # Override inside function code or in pre-test or you will have side effect in other tests
    app.dependency_overrides[crypto_stats_client] = override_crypto_stats_client
    app.dependency_overrides[crypto_predict_client] = override_crypto_predict_client

    response = client.get("/crypto/btc-usd/predict")
    assert response.status_code == 200
    payload = response.json()
    assert float(payload['forecasted_price']) == 2.0