import logging

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from main.service.crypto_stats_service import CryptoStatsService
from main.dependencies.crypto_stats_service import crypto_stats_service

router = APIRouter()

@router.get('/crypto/{product}/stats')
async def get_crypto_stats (product: str = 'btc-usd', service: CryptoStatsService = Depends(crypto_stats_service)):
    logging.debug('Fetching stats')
    stats = await service.get_crypto_stats(product)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(stats))