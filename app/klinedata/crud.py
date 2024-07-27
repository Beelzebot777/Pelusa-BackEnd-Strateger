#Path: app/klinedata/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.klinedata.models import KlineData
from app.klinedata.schemas import KlineDataCreate
from fastapi import HTTPException
from loguru import logger

async def save_kline_data(db: AsyncSession, kline_data: KlineDataCreate):
    try:
        db_kline_data = KlineData(**kline_data.model_dump())
        db.add(db_kline_data)
        await db.commit()
        await db.refresh(db_kline_data)
        return db_kline_data
    except IntegrityError:
        await db.rollback()
        logger.warning(f"K-line data already exists: {kline_data}")
        return None
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error saving K-line data: {str(e)}")

async def get_kline_data(db: AsyncSession, symbol: str, limit: int = 100):
    try:
        query = select(KlineData).where(KlineData.symbol == symbol).order_by(KlineData.time.desc()).limit(limit)
        result = await db.execute(query)
        return result.scalars().all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving K-line data: {str(e)}")
