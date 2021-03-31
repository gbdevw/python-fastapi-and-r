from main.client.cryptostats.coinbase_crypto_stats_client import CoinbaseCryptoStatsClient
from main.client.cryptostats.crypto_stats_client import CryptoStatsClient
from main.configuration.settings import settings

def crypto_stats_client () -> CryptoStatsClient:
    """Return the dependency for the CryptoStatsClient"""
    return CoinbaseCryptoStatsClient(settings.coinbase_url)
