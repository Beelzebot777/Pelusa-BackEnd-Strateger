from fastapi import FastAPI
from app.alarms.routes import router as alarms_router
from app.bingx.routes import router as bingx_router
from app.strateger.routes import router as strateger_router
from loguru import logger
from contextlib import asynccontextmanager
from app.siteground.database import close_db_connections
import asyncio
from app.utils.server_status import log_server_status

logger.add("logs/file_{time:YYYY-MM-DD}.log", rotation="00:00")

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

app = FastAPI(lifespan=lifespan)

app.include_router(alarms_router, prefix="/alarms", tags=["alarms"])
app.include_router(bingx_router, prefix="/bingx", tags=["bingx"])
app.include_router(strateger_router, prefix="/strateger", tags=["strateger"])

