from main.entities.crypto_stats import CryptoStats

class CryptoStatsClient:
    """Interface for CryptoStatsClient : Client which fetch crypto trading stats"""

    async def get_crypto_trading_stats (self, product_id: str) -> CryptoStats:
        """Get trading stats for a currency pair (ex : for BTC-USD, use btc-usd as product_id)"""
        pass