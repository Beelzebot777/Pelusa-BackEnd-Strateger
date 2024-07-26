# Path: app/klinedata/schemas.py

from pydantic import BaseModel

class KlineDataCreate(BaseModel):
    symbol: str
    open: float
    close: float
    high: float
    low: float
    volume: float
    time: int

    class Config:
        from_attributes = True
