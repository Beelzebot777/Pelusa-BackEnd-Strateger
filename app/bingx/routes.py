# Path: app/bingx/routes.py
# Description: Routes for BingX exchange

from fastapi import APIRouter, Depends, HTTPException, Request
from app.bingx.api import get_k_line_data, get_balance, get_positions, get_income_acc, get_all_orders, get_full_all_orders
from loguru import logger
from app.utils.ip_check import is_ip_allowed

router = APIRouter()

@router.get('/get-k-line-data')
async def get_k_line_data_endpoint(request: Request, symbol: str, interval: str, limit: str, start_date: str, end_date: str):
    """
    Fetches K-Line data for a given symbol within a specified interval.

    Parameters:
    - request: The request object.
    - symbol: The symbol for which to fetch K-Line data.
    - interval: The interval of the K-Line data (e.g., '1m', '1h', '1d').
    - limit: The maximum number of data points to fetch.
    - start_date: The start date of the data range.
    - end_date: The end date of the data range.

    Returns:
    - The fetched K-Line data.

    Raises:
    - HTTPException: If an error occurs while fetching the data.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching K-Line data for {symbol} from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:       
        data = await get_k_line_data(symbol, interval, limit, start_date, end_date)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get('/get-balance')
async def get_balance_endpoint(request: Request):
    """
    Get asset information of user‘s Perpetual Account

    Args:
        request (Request): The incoming request object.

    Returns:
        The balance result.
        

    Raises:
        HTTPException: If an error occurs while fetching the balance.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching balance from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_balance()    
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get('/get-positions')
async def get_positions_endpoint(request: Request):
    """
    Get user's positions information

    Args:
        request (Request): The incoming request object.

    Returns:
        The position information.
        

    Raises:
        HTTPException: If an error occurs while fetching the position information.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching positions from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_positions()        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get('/get-income-acc')
async def get_income_acc_endpoint(request: Request):
    """
    Get user's income account information

    Args:
        request (Request): The incoming request object.

    Returns:
        The income account information.
        

    Raises:
        HTTPException: If an error occurs while fetching the income account information.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching income account information from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_income_acc()        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/get-all-orders')
async def get_all_orders_endpoint(request: Request):
    """
    Get user's historical orders information

    Args:
        request (Request): The incoming request object.

    Returns:
        The historical orders information.
        

    Raises:
        HTTPException: If an error occurs while fetching the historical orders information.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching historical orders information from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_all_orders()        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/get-all-full-orders')
async def get_full_all_orders_endpoint(request: Request):
    """
    Get user's historical orders information

    Args:
        request (Request): The incoming request object.

    Returns:
        The historical orders information.
        

    Raises:
        HTTPException: If an error occurs while fetching the historical orders information.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching historical orders information from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_full_all_orders()        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
