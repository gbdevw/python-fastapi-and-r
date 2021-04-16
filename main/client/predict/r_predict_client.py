import requests
import logging

from fastapi import HTTPException
from main.client.predict.predict_client import PredictClient
from main.entities.crypto_predict import CryptoPredict

class RPredictClient(PredictClient):
    """Fetch prediction on an external API"""
    def __init__ (self, http_scheme: str, host: str, port: int):
        self.base_url = http_scheme + '://' + host + ':' + str(port)

    async def crypto_predict (self, product: str, current_price: float) -> CryptoPredict:
        response = requests.post(self.base_url + '/crypto/' + product + '/predict', json={"current_price": current_price})
        if response.status_code != 200:
            logging.error('RPredictClient returned ' + str(response.status_code))
            raise HTTPException(status_code=503, detail="Downstream service unavailable")
        return CryptoPredict(product, current_price, response.json()['forecasted_price'])

    async def is_healthy (self) -> bool:
        try:
            response = requests.get(self.base_url + '/health')
            if response.status_code != 200:
                logging.error('R Health returned ' + str(response.status_code))
                raise HTTPException(status_code=503, detail="Downstream service unavailable")
            return True
        except Exception as e:
            logging.error('Error during downstream healthcheck')
            raise HTTPException(status_code=503, detail="Downstream service unavailable")