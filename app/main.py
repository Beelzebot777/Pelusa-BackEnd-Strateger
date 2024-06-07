from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from loguru import logger

from contextlib import asynccontextmanager
from app.siteground.database import get_db_alarmas, get_db_ordenes, close_db_connections

from app.utils.server_status import log_server_status
from app.utils.ip_check import is_ip_allowed
from app.middlewares import AllowedIPsMiddleware

from app.alarms.routes import router as alarms_router
from app.bingx.routes import router as bingx_router
from app.strateger.routes import router as strateger_router

#------------------------------------------------------- LOGGING -------------------------------------------------------

logger.add("logs/file_{time:YYYY-MM-DD}.log", rotation="00:00")

#------------------------------------------------------- ASYNC CONTEXT MANAGER -----------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.siteground.database import init_db_alarmas, init_db_ordenes
    try:
        logger.info("Initializing databases...")
        await init_db_alarmas()
        await init_db_ordenes()
        logger.info("Databases: OK")

        # Iniciar la tarea en segundo plano
        loop = asyncio.get_event_loop()
        loop.create_task(log_server_status())

        yield
    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise
    finally:
        logger.info("Shutting down...")
        await close_db_connections()  # Asegúrate de cerrar las conexiones aquí

#------------------------------------------------------- FASTAPI -------------------------------------------------------

app = FastAPI(lifespan=lifespan)

#------------------------------------------------------- MIDDLEWARE ----------------------------------------------------

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite solicitudes desde el frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Añadir el middleware de IPs permitidas
app.add_middleware(AllowedIPsMiddleware)

#------------------------------------------------------- EXCEPTION HANDLERS ----------------------------------------------

@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    client_ip = request.client.host
    requested_url = str(request.url)
    user_agent = request.headers.get('user-agent', 'unknown')
    logger.warning(f"404 Not Found: {requested_url} from IP: {client_ip} with User-Agent: {user_agent}")
    return JSONResponse(
        status_code=404,
        content={"Not Found"}
    )


@app.get("/status-server", tags=["health"])
async def health_check(request: Request, db_alarmas: AsyncSession = Depends(get_db_alarmas), db_ordenes: AsyncSession = Depends(get_db_ordenes)):
    
    client_ip = request.client.host
    logger.info(f"Alarm received from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        # Verificar conexión con la base de datos de alarmas
        await db_alarmas.execute(text("SELECT 1"))
        
        # Verificar conexión con la base de datos de órdenes
        await db_ordenes.execute(text("SELECT 1"))

        # Obtener la hora actual
        current_time = datetime.now()
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

        return JSONResponse(status_code=200, content={"status": "ok", "time": time_str})
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return JSONResponse(status_code=500, content={"status": "error", "detail": str(e)})


app.include_router(alarms_router, prefix="/alarms", tags=["alarms"])
app.include_router(bingx_router, prefix="/bingx", tags=["bingx"])
app.include_router(strateger_router, prefix="/strateger", tags=["strateger"])

