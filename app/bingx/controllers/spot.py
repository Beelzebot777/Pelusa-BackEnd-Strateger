#Path: app/bingx/controllers/spot_controller.py

from fastapi import HTTPException
from app.bingx.api.api_spot import get_balance_spot, get_spot_deposit_records
from loguru import logger

async def get_balance_spot_controller(client_ip: str):
    logger.info(f"Fetching balance from {client_ip}")
    try:
        result = await get_balance_spot()
        return result
    except Exception as e:
        logger.error(f"Error fetching spot balance: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

async def get_spot_deposit_records_controller(client_ip: str):
    logger.info(f"Fetching spot deposit records from {client_ip}")
    try:
        result = await get_spot_deposit_records()
        return result
    except Exception as e:
        logger.error(f"Error fetching spot deposit records: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
