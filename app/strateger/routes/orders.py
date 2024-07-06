#Path: app/strateger/routes/orders.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_estrategias
from app.strateger.schemas.orders import OrderCreate, OrderUpdate, Order
from app.strateger.crud import orders as crud_orders

router = APIRouter()

@router.post("/", response_model=Order)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db_estrategias)):
    return await crud_orders.create_order(db, order)

# Agrega más endpoints relacionados con 'orders'
