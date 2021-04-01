from main.entities.crypto_predict import CryptoPredict
from main.service.crypto_predict_service import CryptoPredictService
from main.client.predict.predict_client import PredictClient

class RCryptoPredictService(CryptoPredictService):

    def __init__ (self, client: PredictClient):
        self.client = client

    async def crypto_predict (self, product: str, current_price: float) -> CryptoPredict:
        return await self.client.crypto_predict(product, current_price)