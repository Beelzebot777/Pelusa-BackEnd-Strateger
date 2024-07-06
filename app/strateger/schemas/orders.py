#Path: app/strateger/schemas/orders.py

from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    order_id: int
    strategy_id: int
    ticker: str
    order_type: str
    quantity: float
    price: float
    timestamp: str

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class OrderInDBBase(OrderBase):
    id: int

    class Config:
        from_attributes = True

class Order(OrderInDBBase):
    pass

class OrderInDB(OrderInDBBase):
    pass
