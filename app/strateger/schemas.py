# Path: app/siteground/schemas.py
# Description: Pydantic schemas for orders

from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    orderOpenTime: str
    orderId: int
    symbol: str
    positionSide: str
    side: str
    type: str
    price: Optional[float] = None
    quantity: Optional[float] = None
    stopPrice: Optional[float] = None
    workingType: Optional[str] = None
    clientOrderID: Optional[str] = None
    timeInForce: Optional[str] = None
    priceRate: Optional[float] = None
    stopLoss: Optional[float] = None
    takeProfit: Optional[float] = None
    reduceOnly: Optional[bool] = None
    activationPrice: Optional[float] = None
    closePosition: Optional[str] = None
    stopGuaranteed: Optional[str] = None

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    orderOpenTime: str
    orderId: int
    symbol: str
    positionSide: str
    side: str
    type: str
    price: Optional[float] = None
    quantity: Optional[float] = None
    stopPrice: Optional[float] = None
    workingType: Optional[str] = None
    clientOrderID: Optional[str] = None
    timeInForce: Optional[str] = None
    priceRate: Optional[float] = None
    stopLoss: Optional[float] = None
    takeProfit: Optional[float] = None
    reduceOnly: Optional[bool] = None
    activationPrice: Optional[float] = None
    closePosition: Optional[str] = None
    stopGuaranteed: Optional[str] = None

    class Config:
        orm_mode = True
