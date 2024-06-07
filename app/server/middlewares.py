#Path: app/server/middlewares.py

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.responses import JSONResponse
from starlette.types import ASGIApp
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

class LogResponseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        try:
            response_text = json.loads(response_body.decode())
        except Exception:
            response_text = response_body.decode()

        # Log the response details
        client_ip = request.client.host
        method = request.method
        url = str(request.url)
        status_code = response.status_code

        logger.info(f"Response to {client_ip} - {method} {url} - Status: {status_code} - Response: {response_text}")

        return Response(content=response_body, status_code=status_code, headers=dict(response.headers))