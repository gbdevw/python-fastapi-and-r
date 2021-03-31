import logging
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

# Middle that logs requests and responses
class LoggingMiddleware (BaseHTTPMiddleware):
    
    def __init__(self, app):
        super().__init__(app)
        self.logger = logging.getLogger()
        
    async def dispatch (self, request, call_next):

        # Log the request
        correlation_id = request.state.correlation_id
        transaction_id = request.state.transaction_id
        principal = request.state.principal
        self.logger.info("Request", extra={'correlation-id':correlation_id, 'transaction-id':transaction_id, 'type':'api-request', 'method':str(request.method).upper(), 'url':str(request.url), 'principal':principal})
        # Next middleware
        response = await call_next(request)
        
        # Log the response
        self.logger.info("Response sent", extra={'correlation-id':correlation_id, 'transaction-id':transaction_id, 'type':'api-response', 'code':response.status_code})
        
        # Return response
        return response