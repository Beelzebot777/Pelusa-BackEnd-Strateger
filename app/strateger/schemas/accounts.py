# Path: app/strateger/schemas/accounts.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AccountBalanceBase(BaseModel):
    accountName: str
    accountType: str
    asset: str
    balance: float
    equity: Optional[float] = None
    unrealizedProfit: Optional[float] = None
    realizedProfit: Optional[float] = None
    dateTime: datetime
    availableMargin: Optional[float] = None
    usedMargin: Optional[float] = None

class AccountBalanceCreate(AccountBalanceBase):
    pass

class AccountBalanceInDB(AccountBalanceBase):
    id: int

    class Config:
        orm_mode = True

class AccountBalanceResponse(BaseModel):
    code: int
    msg: str
    timestamp: int
    data: Optional[AccountBalanceInDB]

    class Config:
        orm_mode = True
