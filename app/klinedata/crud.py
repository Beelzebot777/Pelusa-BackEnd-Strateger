# Path: app/klinedata/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.klinedata.models import KlineData

async def save_kline_data(db: AsyncSession, kline_data: dict):
    db_kline_data = KlineData(**kline_data)
    db.add(db_kline_data)
    await db.commit()
    await db.refresh(db_kline_data)
    return db_kline_data

async def get_kline_data(db: AsyncSession, symbol: str, limit: int = 100):
    query = select(KlineData).where(KlineData.symbol == symbol).order_by(KlineData.time.desc()).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()
