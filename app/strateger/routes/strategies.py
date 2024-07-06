#Path: app/strateger/routes/strategies.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_estrategias
from app.strateger.crud.strategies import get_strategy, get_strategies, create_strategy, update_strategy, delete_strategy
from app.strateger.schemas.strategies import StrategyCreate, StrategyUpdate, Strategy

router = APIRouter()

@router.get("/get/{strategy_id}", response_model=Strategy)
async def read_strategy(strategy_id: int, db: AsyncSession = Depends(get_db_estrategias)):
    db_strategy = await get_strategy(db, strategy_id)
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return db_strategy

@router.get("/list", response_model=list[Strategy])
async def read_strategies(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db_estrategias)):
    return await get_strategies(db, skip=skip, limit=limit)

@router.post("/insert", response_model=Strategy)
async def create_strategy(strategy: StrategyCreate, db: AsyncSession = Depends(get_db_estrategias)):
    return await create_strategy(db, strategy)

@router.put("/update/{strategy_id}", response_model=Strategy)
async def update_strategy(strategy_id: int, strategy: StrategyUpdate, db: AsyncSession = Depends(get_db_estrategias)):
    db_strategy = await get_strategy(db, strategy_id)
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return await update_strategy(db, strategy_id, strategy)

@router.delete("/delete/{strategy_id}", response_model=Strategy)
async def delete_strategy(strategy_id: int, db: AsyncSession = Depends(get_db_estrategias)):
    db_strategy = await get_strategy(db, strategy_id)
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return await delete_strategy(db, strategy_id)
