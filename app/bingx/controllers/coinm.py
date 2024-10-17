# Path: app/bingx/controllers/coinm_controller.py

from app.bingx.api.api_coinm import get_balance_perp_coinm, get_positions_perp_coinm
from app.utils.ip_check import is_ip_allowed
from fastapi import HTTPException
from loguru import logger


async def get_balance_controller(client_ip: str):
    """
    Get asset information of user‘s PERP COIN-M Account.
    """

    logger.info(f"Fetching balance from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_balance_perp_coinm()
        return result
    except Exception as e:
        logger.error(f"Error fetching PERP COIN-M balance: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


async def get_positions_perp_coinm_controller(client_ip: str):
    """
    Get user's coin-m account positions information.
    """

    logger.info(f"Fetching positions from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_positions_perp_coinm()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
