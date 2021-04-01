import logging

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from main.service.crypto_stats_service import CryptoStatsService
from main.dependencies.crypto_stats_service import crypto_stats_service
from main.service.crypto_predict_service import CryptoPredictService
from main.dependencies.crypto_predict_service import crypto_predict_service
from main.entities.crypto_stats import CryptoStats

router = APIRouter()

@router.get('/crypto/{product}/stats')
async def get_crypto_stats (product: str = 'btc-usd', service: CryptoStatsService = Depends(crypto_stats_service)):
    logging.debug('Fetching stats')
    stats = await service.get_crypto_stats(product)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(stats))

@router.get('/crypto/{product}/predict')
async def get_crypto_predict (product: str = 'btc-usd', crypto_stats_service: CryptoStatsService = Depends(crypto_stats_service), crypto_predict_service: CryptoPredictService = Depends(crypto_predict_service)):
    logging.debug('Fetching prediction')
    stats = await crypto_stats_service.get_crypto_stats(product)
    prediction = await crypto_predict_service.crypto_predict(product, stats.last)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(prediction))