from main.service.crypto_stats_service import CryptoStatsService
from main.client.cryptostats.crypto_stats_client import CryptoStatsClient
from main.entities.crypto_stats import CryptoStats

class CoinbaseCryptoStatsService(CryptoStatsService):
    """Service which provide crypto trading stats from Coinbase"""
    def __init__ (self, client: CryptoStatsClient):
        self.client = client

    async def get_crypto_stats (self, product_id: str = 'btc-usd') -> CryptoStats:
        return await self.client.get_crypto_trading_stats(product_id)