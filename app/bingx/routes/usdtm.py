#Path: app/bingx/routes/usdtm.py

from fastapi import APIRouter, Request
from app.bingx.controllers.usdtm import (
    get_full_all_orders_controller, 
    make_order_usdtm_controller, 
    get_balance_perp_controller, 
    get_income_acc_controller, 
    get_all_orders_controller, 
    get_positions_controller
)

router = APIRouter()

@router.get('/get-all-full-orders')
async def get_full_all_orders_endpoint(request: Request, limit: int = 500, offset: int = 0):
    client_ip = request.client.host    
    return await get_full_all_orders_controller(client_ip, limit, offset)

@router.post('/make-order-usdtm')
async def make_order_usdtm_endpoint(request: Request, leverage: int, symbol: str, side: str, positionSide: str, order_type: str, quantity: float):
    client_ip = request.client.host    
    return await make_order_usdtm_controller(client_ip, leverage, symbol, side, positionSide, order_type, quantity)

@router.get('/get-balance-perp-usdtm')
async def get_balance_perp_endpoint(request: Request):
    client_ip = request.client.host    
    return await get_balance_perp_controller(client_ip)

@router.get('/get-income-acc')
async def get_income_acc_endpoint(request: Request):
    client_ip = request.client.host    
    return await get_income_acc_controller(client_ip)

@router.get('/get-all-orders')
async def get_all_orders_endpoint(request: Request, limit: int = 500, offset: int = 0):
    client_ip = request.client.host    
    return await get_all_orders_controller(client_ip, limit, offset)

@router.get('/get-positions-usdtm')
async def get_positions_endpoint(request: Request):
    client_ip = request.client.host    
    return await get_positions_controller(client_ip)
