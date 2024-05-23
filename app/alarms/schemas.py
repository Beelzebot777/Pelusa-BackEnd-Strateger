# app/alarms/schemas.py
from pydantic import BaseModel
from typing import Optional

class AlarmData(BaseModel):
    Ticker: str
    Temporalidad: str
    Quantity: Optional[str] = None
    Entry_Price_Alert: Optional[str] = None
    Exit_Price_Alert: Optional[str] = None
    Time_Alert: str
    Order: str
    Strategy: Optional[str] = None
    
    class Config:
        from_attributes = True

class AlarmResponse(BaseModel):
    id: int
    Ticker: str
    Temporalidad: str
    Quantity: Optional[str] = None
    Entry_Price_Alert: Optional[str] = None
    Exit_Price_Alert: Optional[str] = None
    Time_Alert: str
    Order: str
    Strategy: Optional[str] = None
    
    class Config:
        from_attributes = True
