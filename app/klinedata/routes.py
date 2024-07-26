# Path: app/klinedata/routes.py

from fastapi import APIRouter, Depends, HTTPException, Request, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.siteground.database import get_db_kline_data
from app.klinedata.schemas import KlineDataCreate
from app.klinedata.crud import save_kline_data, get_kline_data
from app.utils.ip_check import is_ip_allowed
from loguru import logger

router = APIRouter()

@router.post("/kline_data", response_model=KlineDataCreate)
async def create_kline_data(kline_data: KlineDataCreate, db: AsyncSession = Depends(get_db_kline_data)):
    try:
        saved_kline_data = await save_kline_data(db, kline_data.dict())
        return saved_kline_data
    except Exception as e:
        logger.error(f"Error saving kline data: {e}")
        raise HTTPException(status_code=500, detail="Error saving kline data")

@router.get("/kline_data", response_model=List[KlineDataCreate])
async def get_kline_data_endpoint(
    symbol: str, 
    db: AsyncSession = Depends(get_db_kline_data), 
    limit: int = Query(default=100, ge=1)
):
    try:
        kline_data = await get_kline_data(db, symbol, limit)
        return kline_data
    except Exception as e:
        logger.error(f"Error fetching kline data: {e}")
        raise HTTPException(status_code=500, detail="Error fetching kline data")
