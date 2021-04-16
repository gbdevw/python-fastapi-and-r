import logging
import json

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from main.client.predict.predict_client import PredictClient
from main.dependencies.crypto_predict_client import crypto_predict_client

router = APIRouter()

@router.get('/health')
async def get_health_check (downstream: PredictClient = Depends(crypto_predict_client)):
    logging.debug('Health check')
    status = 200
    content = 'Downstream services OK'
    if not await downstream.is_healthy():
        status = 503
        content = 'Downstream service not available'
    return JSONResponse(status_code=status, content=json.dumps({'status_code': status, 'message': content}))
