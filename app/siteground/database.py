# Path: app/siteground/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings
from loguru import logger
from app.siteground.base import BaseAlarmas, BaseEstrategias, BaseDiary, BasePositions

# Configuración de las bases de datos
engine_alarmas = create_async_engine(settings.DATABASE_URL_DESARROLLO_ALARMAS, pool_recycle=3600, pool_pre_ping=True)
SessionLocalAlarmas = sessionmaker(autocommit=False, autoflush=False, bind=engine_alarmas, class_=AsyncSession)

engine_estrategias = create_async_engine(settings.DATABASE_URL_DESARROLLO_ESTRATEGIAS, pool_recycle=3600, pool_pre_ping=True)
SessionLocalEstrategias = sessionmaker(autocommit=False, autoflush=False, bind=engine_estrategias, class_=AsyncSession)

engine_diary = create_async_engine(settings.DATABASE_URL_DESARROLLO_DIARY, pool_recycle=3600, pool_pre_ping=True)
SessionLocalDiary = sessionmaker(autocommit=False, autoflush=False, bind=engine_diary, class_=AsyncSession)

engine_positions = create_async_engine(settings.DATABASE_URL_DESARROLLO_POSITIONS, pool_recycle=3600, pool_pre_ping=True)
SessionLocalPositions = sessionmaker(autocommit=False, autoflush=False, bind=engine_positions, class_=AsyncSession)

async def get_db_alarmas():
    async with SessionLocalAlarmas() as db:
        yield db

async def get_db_estrategias():
    async with SessionLocalEstrategias() as db:
        yield db
        
async def get_db_diary():
    async with SessionLocalDiary() as db:
        yield db

async def get_db_positions():
    async with SessionLocalPositions() as db:
        yield db

async def init_db_alarmas():
    async with engine_alarmas.begin() as conn:
        await conn.run_sync(BaseAlarmas.metadata.create_all)

async def init_db_estrategias():
    async with engine_estrategias.begin() as conn:
        await conn.run_sync(BaseEstrategias.metadata.create_all)

async def init_db_diary():
    async with engine_diary.begin() as conn:
        await conn.run_sync(BaseDiary.metadata.create_all)

async def init_db_positions():
    async with engine_positions.begin() as conn:        
        await conn.run_sync(BasePositions.metadata.create_all)
        

async def close_db_connections():
    await engine_alarmas.dispose()
    await engine_estrategias.dispose()
    await engine_diary.dispose()
    await engine_positions.dispose()
