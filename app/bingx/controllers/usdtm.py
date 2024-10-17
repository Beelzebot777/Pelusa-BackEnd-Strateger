#Path: app/bingx/controllers/usdtm.py

from fastapi import HTTPException
from app.bingx.api.api_usdtm import (
    get_balance_perp, 
    get_income_acc, 
    get_all_orders, 
    get_full_all_orders, 
    get_positions, 
    make_order
)
from loguru import logger
from app.utils.ip_check import is_ip_allowed

async def get_full_all_orders_controller(client_ip: str, limit: int, offset: int):
    logger.info(f"Fetching historical orders information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_full_all_orders(limit, offset)
        logger.debug(f"result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error fetching historical orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

async def make_order_usdtm_controller(client_ip: str, leverage: int, symbol: str, side: str, positionSide: str, order_type: str, quantity: float):
    logger.info(f"Making order request from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await make_order(leverage, symbol, side, positionSide, order_type, quantity)
        return result
    except Exception as e:
        logger.error(f"Error making order: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

async def get_balance_perp_controller(client_ip: str):
    logger.info(f"Fetching balance information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_balance_perp()
        return result
    except Exception as e:
        logger.error(f"Error fetching balance information: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

async def get_income_acc_controller(client_ip: str):
    logger.info(f"Fetching income account information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_income_acc()
        return result
    except Exception as e:
        logger.error(f"Error fetching income account information: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

async def get_all_orders_controller(client_ip: str, limit: int, offset: int):
    logger.info(f"Fetching historical orders information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_all_orders(limit, offset)
        logger.debug(f"result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error fetching all orders: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

async def get_positions_controller(client_ip: str):
    logger.info(f"Fetching positions information from {client_ip}")
    await is_ip_allowed(client_ip)
    try:
        result = await get_positions()
        return result
    except Exception as e:
        logger.error(f"Error fetching positions: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
