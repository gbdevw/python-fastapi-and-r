from main.service.coinbase_crypto_stats_service import CoinbaseCryptoStatsService
from main.service.crypto_stats_service import CryptoStatsService
from main.client.cryptostats.crypto_stats_client import CryptoStatsClient
from main.dependencies.crypto_stats_client import crypto_stats_client
from fastapi import Depends

def crypto_stats_service (client: CryptoStatsClient = Depends(crypto_stats_client)) -> CryptoStatsService:
    """Return the dependency for CryptoStatsService"""
    return CoinbaseCryptoStatsService(client)