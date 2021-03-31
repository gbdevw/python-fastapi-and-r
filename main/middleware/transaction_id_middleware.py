import uuid

from starlette.middleware.base import BaseHTTPMiddleware

# Middleware that adds a UUID to the request for logging purpose
class TransactionIdMiddleware (BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    # Add a transaction ID
    async def dispatch (self, request, call_next):

        # Add transaction ID
        request.state.transaction_id = str(uuid.uuid4())

        # Next middleware
        response = await call_next(request)

        # Return response
        return response