from main.entities.crypto_predict import CryptoPredict

class PredictClient:
    """Interface for a client which fetch a forecasted price for a crypto asset"""
    async def crypto_predict (self, product: str, current_price: float) -> CryptoPredict:
        pass

    async def is_healthy (self) -> bool:
        pass