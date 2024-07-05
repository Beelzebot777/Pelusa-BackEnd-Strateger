from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_estrategias
from app.strateger.crud import strategies as crud_strategies
from app.strateger.schemas.strategies import StrategyCreate, StrategyUpdate, Strategy

router = APIRouter()

@router.get("/{strategy_id}", response_model=Strategy)
async def read_strategy(strategy_id: int, db: AsyncSession = Depends(get_db_estrategias)):
    db_strategy = await crud_strategies.get_strategy(db, strategy_id)
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return db_strategy

@router.get("/", response_model=list[Strategy])
async def read_strategies(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db_estrategias)):
    return await crud_strategies.get_strategies(db, skip=skip, limit=limit)

@router.post("/", response_model=Strategy)
async def create_strategy(strategy: StrategyCreate, db: AsyncSession = Depends(get_db_estrategias)):
    return await crud_strategies.create_strategy(db, strategy)

@router.put("/{strategy_id}", response_model=Strategy)
async def update_strategy(strategy_id: int, strategy: StrategyUpdate, db: AsyncSession = Depends(get_db_estrategias)):
    db_strategy = await crud_strategies.get_strategy(db, strategy_id)
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return await crud_strategies.update_strategy(db, strategy_id, strategy)

@router.delete("/{strategy_id}", response_model=Strategy)
async def delete_strategy(strategy_id: int, db: AsyncSession = Depends(get_db_estrategias)):
    db_strategy = await crud_strategies.get_strategy(db, strategy_id)
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return await crud_strategies.delete_strategy(db, strategy_id)
