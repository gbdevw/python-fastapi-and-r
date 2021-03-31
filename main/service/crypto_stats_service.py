from main.entities.crypto_stats import CryptoStats

class CryptoStatsService:
    """Interface for the CryptoStatsService : Service which provides crypto stats"""
    async def get_crypto_stats (self, product_id: str = 'btc-usd') -> CryptoStats:
        pass