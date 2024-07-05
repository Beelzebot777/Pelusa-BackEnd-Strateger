# Path: app/siteground/database.py
# Description: Database functions for siteground

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.siteground.base import BaseAlarmas, BaseEstrategias
from app.alarms.models import Alarm
from app.strateger.models import Strategy  # Asegúrate de que este import funcione correctamente

import asyncio

# Configuración de las bases de datos
engine_alarmas = create_async_engine(
    settings.DATABASE_URL_DESARROLLO_ALARMAS,
    pool_recycle=3600,
    pool_pre_ping=True
)

SessionLocalAlarmas = sessionmaker(autocommit=False, autoflush=False, bind=engine_alarmas, class_=AsyncSession)

engine_estrategias = create_async_engine(
    settings.DATABASE_URL_DESARROLLO_ESTRATEGIAS,
    pool_recycle=3600,
    pool_pre_ping=True
)

SessionLocalEstrategias = sessionmaker(autocommit=False, autoflush=False, bind=engine_estrategias, class_=AsyncSession)

async def get_db_alarmas():
    async with SessionLocalAlarmas() as db:
        yield db

async def get_db_estrategias():
    async with SessionLocalEstrategias() as db:
        yield db

async def init_db_alarmas():
    async with engine_alarmas.begin() as conn:
        await conn.run_sync(BaseAlarmas.metadata.create_all)

async def init_db_estrategias():
    async with engine_estrategias.begin() as conn:
        await conn.run_sync(BaseEstrategias.metadata.create_all)

async def close_db_connections():
    await engine_alarmas.dispose()
    await engine_estrategias.dispose()
