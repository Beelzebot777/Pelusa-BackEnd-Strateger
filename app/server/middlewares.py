#Path: app/server/middlewares.py

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.responses import JSONResponse
from app.config import settings
from loguru import logger
import json

class AllowedIPsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host        
        if client_ip not in settings.ALLOWED_IPS:
            logger.warning(f"Unauthorized IP {client_ip} attempted to access the service")
            return JSONResponse({"detail": "Access forbidden: Your IP is not allowed"}, status_code=403)
        response = await call_next(request)
        return response

class InvalidRequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            client_ip = request.client.host
            requested_url = str(request.url)
            user_agent = request.headers.get('user-agent', 'unknown')
            logger.warning(
                f"Invalid HTTP request received from IP: {client_ip}, URL: {requested_url}, "
                f"User-Agent: {user_agent}, Error: {exc}"
            )
            return Response(content=json.dumps({"detail": "Invalid request"}), status_code=400, media_type="application/json")