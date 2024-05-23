# Path: app/strateger/routes.py

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.siteground.database import get_db_ordenes
from app.strateger.schemas import OrderResponse
from app.strateger.crud import get_orders

from loguru import logger
from typing import List

router = APIRouter()

@router.get("/orders", response_model=List[OrderResponse])
async def get_orders_endpoint(db_orders: Session = Depends(get_db_ordenes)):
    try:
        orders = get_orders(db_orders)
        return [OrderResponse.model_validate(order) for order in orders]
    except Exception as e:
        logger.error(f"Error fetching orders: {e}")
        raise HTTPException(status_code=500, detail="There was an error fetching the orders")   