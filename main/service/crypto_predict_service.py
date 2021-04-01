from main.entities.crypto_predict import CryptoPredict

class CryptoPredictService:
    """Interface for the CryptoPredictService : Service which provides crypto predictions"""
    async def crypto_predict (self, product: str, current_price: float) -> CryptoPredict:
        pass