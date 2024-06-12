# Path: app/siteground/schemas.py
# Description: Pydantic schemas for orders

from pydantic import BaseModel
from typing import Optional

class StrategyBase(BaseModel):
    name: str
    isOn:  Optional[bool] = None
    apiKey: Optional[str] = None
    secretKey: Optional[str] = None
    ticker: Optional[str] = None
    resultadoAcc: Optional[str] = None
    description: Optional[str] = None
    longEntryOrder: Optional[str] = None
    longCloseOrder: Optional[str] = None
    longEntryIndicator: Optional[str] = None
    longCloseIndicator: Optional[str] = None
    longPyramiding: Optional[int] = None
    longLeverage: Optional[float] = None
    longQuantity: Optional[float] = None
    longTPPerOrder: Optional[float] = None
    longTPGeneral: Optional[float] = None
    longSLPerOrder: Optional[float] = None
    longSLGeneral: Optional[float] = None
    shortEntryOrder: Optional[str] = None
    shortCloseOrder: Optional[str] = None
    shortEntryIndicator: Optional[str] = None
    shortCloseIndicator: Optional[str] = None
    shortPyramiding: Optional[int] = None
    shortLeverage: Optional[float] = None
    shortQuantity: Optional[float] = None
    shortTPPerOrder: Optional[float] = None
    shortTPGeneral: Optional[float] = None
    shortSLPerOrder: Optional[float] = None
    shortSLGeneral: Optional[float] = None

class StrategyCreate(StrategyBase):
    pass

class StrategyUpdate(StrategyBase):
    pass

class StrategyInDBBase(StrategyBase):
    id: int

    class Config:
        from_attributes = True

class Strategy(StrategyInDBBase):
    pass

class StrategyInDB(StrategyInDBBase):
    pass


