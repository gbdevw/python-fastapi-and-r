import requests
import logging

from main.client.cryptostats.crypto_stats_client import CryptoStatsClient
from main.entities.crypto_stats import CryptoStats

class CoinbaseCryptoStatsClient(CryptoStatsClient):
    """Fetch crypto trading stats from Coinbase"""

    def __init__ (self, base_url: str = 'https://api-public.sandbox.pro.coinbase.com'):
        self.base_url = base_url

    async def get_crypto_trading_stats(self, product_id: str) -> CryptoStats:
        # Make the request to Coinbase Pro API
        logging.debug('Sending stats request to ' + self.base_url + ' for ' + product_id.lower())
        response = requests.get(self.base_url + '/products/' + product_id.lower() + '/stats')
        # Check response
        if response.status_code != 200:
            raise Exception('An error occured during request')
        # Extract JSON payload
        payload = response.json()
        # Return response
        return CryptoStats(
            open=float(payload.get('open', 0.0)),
            high=float(payload.get('high', 0.0)),
            low=float(payload.get('low', 0.0)),
            volume=float(payload.get('volume', 0.0)),
            last=float(payload.get('last', 0.0)),
            volume30d=float(payload.get('volume_30day', 0.0)))
