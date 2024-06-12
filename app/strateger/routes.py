# Path: app/strateger/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_estrategias
from app.strateger import crud
from app.strateger.schemas import StrategyCreate, StrategyUpdate, Strategy

router = APIRouter()

@router.post("/insert", response_model=Strategy)
async def create_strategy(strategy: StrategyCreate, db: AsyncSession = Depends(get_db_estrategias)):
    return await crud.create_strategy(db, strategy)

@router.get("/get/{strategy_id}", response_model=Strategy)
async def read_strategy(strategy_id: int, db: AsyncSession = Depends(get_db_estrategias)):
    db_strategy = await crud.get_strategy(db, strategy_id)
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return db_strategy

@router.get("/list", response_model=list[Strategy])
async def read_strategies(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db_estrategias)):
    return await crud.get_strategies(db, skip=skip, limit=limit)

@router.put("/update/{strategy_id}", response_model=Strategy)
async def update_strategy(strategy_id: int, strategy: StrategyUpdate, db: AsyncSession = Depends(get_db_estrategias)):
    db_strategy = await crud.get_strategy(db, strategy_id)
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return await crud.update_strategy(db, strategy_id, strategy)

@router.delete("/delete/{strategy_id}", response_model=Strategy)
async def delete_strategy(strategy_id: int, db: AsyncSession = Depends(get_db_estrategias)):
    db_strategy = await crud.get_strategy(db, strategy_id)
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return await crud.delete_strategy(db, strategy_id)
