# Path: app/bingx/routes.py
# Description: Routes for BingX exchange

from fastapi import APIRouter, Depends, HTTPException, Request
from app.bingx.api import (
    get_ticker, get_k_line_data, get_balance_spot,
    get_balance_perp_coinm, get_balance_perp_usdtm,
    get_positions, get_income_acc, get_all_orders, get_full_all_orders
)
from loguru import logger
from app.utils.ip_check import is_ip_allowed

router = APIRouter()

@router.get('/get-ticker')
async def get_ticker_endpoint(request: Request, symbol: str):
    """           
    Get information about a specific trading symbol.

    Returns:
    - code: Status code of the response (0 indicates success).
    - msg: Message associated with the response (usually empty if successful).
    - data: Contains the following fields:
        - symbol: The trading pair (e.g., BTC-USDT).
        - priceChange: The price change.
        - priceChangePercent: The percentage price change.
        - lastPrice: The last price.
        - lastQty: The last quantity.
        - highPrice: The highest price.
        - lowPrice: The lowest price.
        - volume: The trading volume.
        - quoteVolume: The quote volume.
        - openPrice: The opening price.
        - openTime: The opening time (timestamp).
        - closeTime: The closing time (timestamp).
        - askPrice: The ask price.
        - askQty: The ask quantity.
        - bidPrice: The bid price.
        - bidQty: The bid quantity.
    """    
    
    client_ip = request.client.host
    
    logger.info(f"Getting data for {symbol} from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_ticker(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching ticker information: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

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

@router.get('/get-balance-perp-coinm')
async def get_balance_perp_coinm_endpoint(request: Request):
    """
    Get asset information of user‘s PERP COIN-M Account
    """
    
    client_ip = request.client.host
    
    logger.info(f"Fetching balance from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_balance_perp_coinm()
        return result
    except Exception as e:
        logger.error(f"Error fetching PERP COIN-M balance: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
    
    
@router.get('/get-balance-spot')
async def get_balance_spot_endpoint(request: Request):
    """
    Get asset information of user‘s Spot Account
    """
    
    client_ip = request.client.host
    
    logger.info(f"Fetching balance from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
 
    try:
        result = await get_balance_spot()    
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@router.get('/get-balance-perp-usdtm')
async def get_balance_endpoint(request: Request):
    """
    Get asset information of user‘s Perpetual Account

    Args:
        request (Request): The incoming request object.

    Returns:
        The balance result.
    
    Example Return:
        - Balance Information:
        - User ID: 875046285523701766
        - Asset: USDT
        - Balance: 252.9224 USDT
        - Equity: 233.5737 USDT
        - Unrealized Profit: -19.3487 USDT
        - Realized Profit: -0.5324 USDT
        - Available Margin: 127.3871 USDT
        - Used Margin: 125.5353 USDT
        - Freezed Margin: 0.0000 USDT
        - Short UID: 5816495        

    Raises:
        HTTPException: If an error occurs while fetching the balance.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching balance from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_balance_perp_usdtm()    
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
async def get_all_orders_endpoint(request: Request, limit: int = 500, offset: int = 0):
    """
    Get user's historical orders information

    Args:
        request (Request): The incoming request object.
        limit (int): The number of orders to fetch.
        offset (int): The offset for pagination.

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
        result = await get_all_orders(limit, offset)
        logger.debug(f"result: {result}")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/get-all-full-orders')
async def get_full_all_orders_endpoint(request: Request, limit: int = 500, offset: int = 0):
    """
    Get user's historical orders information

    Args:
        request (Request): The incoming request object.
        limit (int): The number of orders to fetch.
        offset (int): The offset for pagination.

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
        result = await get_full_all_orders(limit, offset)     
        logger.debug(f"result: {result}")  
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
