from unittest.mock import AsyncMock
from fastapi.testclient import TestClient
from main.app import app
from main.entities.crypto_stats import CryptoStats
from main.client.cryptostats.crypto_stats_client import CryptoStatsClient
from main.dependencies.crypto_stats_client import crypto_stats_client

client = TestClient(app)

# Override dependency with a mock
def override_crypto_stats_client () -> CryptoStatsClient:
    # Create the mock
    mock = CryptoStatsClient()
    mock.get_crypto_trading_stats = AsyncMock(return_value=CryptoStats(last=1.0))
    return mock

# Test with mocked client
def test_get_crypto_stats_mocked():
    # Override inside function code or in pre-test or you will have side effect in other tests
    app.dependency_overrides[crypto_stats_client] = override_crypto_stats_client

    response = client.get("/crypto/btc-usd/stats")
    assert response.status_code == 200
    payload = response.json()
    assert payload['last'] == 1.0