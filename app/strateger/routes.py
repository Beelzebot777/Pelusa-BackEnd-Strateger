# Path: app/strateger/routes.py

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.siteground.database import get_db_ordenes
from app.strateger.schemas import OrderResponse
from app.strateger.crud import get_orders
from app.utils.ip_check import is_ip_allowed

from loguru import logger
from typing import List

router = APIRouter()

@router.get("/orders", response_model=List[OrderResponse])
async def get_orders_endpoint(request: Request, db_orders: Session = Depends(get_db_ordenes)):
    client_ip = request.client.host
    # Verificar si la IP está permitida
    
    await is_ip_allowed(client_ip)
    
    try:
        orders = get_orders(db_orders)
        return [OrderResponse.model_validate(order) for order in orders]
    except Exception as e:
        logger.error(f"Error fetching orders: {e}")
        raise HTTPException(status_code=500, detail="There was an error fetching the orders")   