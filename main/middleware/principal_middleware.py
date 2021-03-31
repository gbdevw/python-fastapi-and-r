from starlette.middleware.base import BaseHTTPMiddleware

# Middleware that extracts principal from API key
class PrincipalMiddleware (BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    # Add a transaction ID
    async def dispatch (self, request, call_next):

        # Extract principal from API Key
        request.state.principal = 'UNKNOWN'

        # Next middleware
        response = await call_next(request)

        # Return response
        return response