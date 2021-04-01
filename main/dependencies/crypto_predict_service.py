from main.service.r_crypto_predict_service import RCryptoPredictService
from main.service.crypto_predict_service import CryptoPredictService
from main.client.predict.predict_client import PredictClient
from main.dependencies.crypto_predict_client import crypto_predict_client
from fastapi import Depends

def crypto_predict_service (client: PredictClient = Depends(crypto_predict_client)) -> CryptoPredictService:
    """Return the dependency for CryptoStatsService"""
    return RCryptoPredictService(client)