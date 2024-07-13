# Path: app/strateger/schemas/positions.py

from pydantic import BaseModel
from typing import List, Optional

class PositionBase(BaseModel):
    symbol: str
    account_name: str
    account_type: str
    positionId: str
    positionSide: str
    isolated: bool
    positionAmt: str
    availableAmt: str
    unrealizedProfit: str
    initialMargin: str
    liquidationPrice: float
    avgPrice: str
    leverage: int
    markPrice: str
    riskRate: str
    maxMarginReduction: str
    updateTime: int

class PositionCreate(PositionBase):
    pass

class PositionUpdate(PositionBase):
    pass

class PositionInDB(PositionBase):
    id: int

    class Config:
        orm_mode = True

class PositionResponse(BaseModel):
    code: int
    msg: str
    timestamp: int
    data: List[PositionInDB]

    class Config:
        orm_mode = True
