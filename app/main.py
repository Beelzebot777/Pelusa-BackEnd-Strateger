# Path: app/main.py

from fastapi import FastAPI
from app.alarms.routes import router as alarms_router
from loguru import logger
from contextlib import asynccontextmanager

# Configuración de Loguru
logger.add("logs/file_{time}.log")

@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.siteground.database import init_db_alarmas, init_db_ordenes
    try:
        logger.info("Initializing databases...")
        init_db_alarmas()
        #init_db_ordenes()
        logger.info("Databases: OK")
        yield
    except Exception as e:
        logger.error(f"Error during startup: {e}")
        raise
    finally:
        logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

# Incluir las rutas de alarms
app.include_router(alarms_router, prefix="/alarms", tags=["alarms"])
