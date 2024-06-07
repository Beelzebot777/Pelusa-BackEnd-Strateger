from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.config import settings
from loguru import logger

class AllowedIPsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        if client_ip not in settings.ALLOWED_IPS:
            logger.warning(f"Unauthorized IP {client_ip} attempted to access the service")
            return JSONResponse({"detail": "Access forbidden: Your IP is not allowed"}, status_code=403)
        response = await call_next(request)
        return response
