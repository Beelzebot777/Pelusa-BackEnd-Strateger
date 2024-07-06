#Path: app/strateger/routes/backtesting.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_estrategias
from app.strateger.schemas.backtesting import BacktestCreate, BacktestUpdate, Backtest
from app.strateger.crud import backtesting as crud_backtesting

router = APIRouter()

@router.post("/", response_model=Backtest)
async def create_backtest(backtest: BacktestCreate, db: AsyncSession = Depends(get_db_estrategias)):
    return await crud_backtesting.create_backtest(db, backtest)

# Agrega más endpoints relacionados con 'backtesting'
