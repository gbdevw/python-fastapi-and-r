import uuid
import uvicorn

from mangum import Mangum

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from main.route import crypto_controller
from main.route import health_controller
from main.configuration.settings import settings
from main.monitoring import logging_config
from main.middleware.correlation_id_middleware import CorrelationIdMiddleware
from main.middleware.transaction_id_middleware import TransactionIdMiddleware
from main.middleware.logging_middleware import LoggingMiddleware
from main.middleware.principal_middleware import PrincipalMiddleware
from main.handler.exception_handler import exception_handler
from main.handler.http_exception_handler import http_exception_handler

###############################################################################
#   Application object                                                        #
###############################################################################

app = FastAPI()

###############################################################################
#   Logging configuration                                                     #
###############################################################################

logging_config.configure_logging(level=settings.logging_level, service=settings.application_name, instance=settings.application_instance)

###############################################################################
#   Error handlers configuration                                              #
###############################################################################

app.add_exception_handler(Exception, exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

###############################################################################
#   Middlewares configuration                                                 #
###############################################################################

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tip : middleware order : Principal > TransactionId > CorrelationId > Logging -> reverse order
# Logging middleware
app.add_middleware(LoggingMiddleware)
# Correlation ID middleware
app.add_middleware(CorrelationIdMiddleware)
# Transaction ID middleware
app.add_middleware(TransactionIdMiddleware)
# Principal middleware
app.add_middleware(PrincipalMiddleware)

###############################################################################
#   Routers configuration                                                     #
###############################################################################

app.include_router(crypto_controller.router, prefix=settings.application_root, tags=['crypto'])
app.include_router(health_controller.router, prefix=settings.application_root, tags=['health'])

###############################################################################
#   Handler for AWS Lambda                                                    #
###############################################################################

handler = Mangum(app)

###############################################################################
#   Run the self contained application                                        #
###############################################################################

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)