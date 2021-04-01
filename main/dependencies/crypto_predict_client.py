from main.configuration.settings import settings
from main.client.predict.predict_client import PredictClient
from main.client.predict.r_predict_client import RPredictClient

def crypto_predict_client () -> PredictClient:
    return RPredictClient(http_scheme=settings.rpredict_scheme, host=settings.rpredict_host, port=settings.rpredict_port)
