# Path: app/bingx/routes.py
# Description: Routes for BingX exchange

from fastapi import APIRouter, Depends, HTTPException, Request
from app.bingx.api import get_k_line_data
from loguru import logger
from app.utils.ip_check import is_ip_allowed

router = APIRouter()

@router.get('/get-k-line-data')
async def get_k_line_data_endpoint(request: Request, symbol: str, interval: str, limit: str, start_date: str, end_date: str):
    client_ip = request.client.host
    
    logger.info(f"Fetching K-Line data for {symbol} from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:       
        data = await get_k_line_data(symbol, interval, limit, start_date, end_date)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
