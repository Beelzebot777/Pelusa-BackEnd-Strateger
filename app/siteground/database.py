# Path: app/siteground/database.py
# Description: Database functions for siteground

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.siteground.base import BaseAlarmas, BaseOrdenes
from app.alarms.models import Alarm
from app.strateger.models import Order
import asyncio

# Configuración de las bases de datos
engine_alarmas = create_async_engine(
    settings.DATABASE_URL_DESARROLLO_ALARMAS,
    pool_recycle=3600,
    pool_pre_ping=True
)
engine_ordenes = create_async_engine(
    settings.DATABASE_URL_DESARROLLO_ORDENES,
    pool_recycle=3600,
    pool_pre_ping=True
)

SessionLocalAlarmas = sessionmaker(autocommit=False, autoflush=False, bind=engine_alarmas, class_=AsyncSession)
SessionLocalOrdenes = sessionmaker(autocommit=False, autoflush=False, bind=engine_ordenes, class_=AsyncSession)

async def get_db_alarmas():
    async with SessionLocalAlarmas() as db:
        yield db

async def get_db_ordenes():
    async with SessionLocalOrdenes() as db:
        yield db

async def init_db_alarmas():
    async with engine_alarmas.begin() as conn:
        await conn.run_sync(BaseAlarmas.metadata.create_all)

async def init_db_ordenes():
    async with engine_ordenes.begin() as conn:
        await conn.run_sync(BaseOrdenes.metadata.create_all)

async def close_db_connections():
    await engine_alarmas.dispose()
    await engine_ordenes.dispose()
