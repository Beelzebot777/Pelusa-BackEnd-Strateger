from fastapi import APIRouter, Request, HTTPException

from app.bingx.api.api_usdtm import get_balance_perp, get_income_acc, get_all_orders, get_full_all_orders, get_positions, make_order
from app.utils.ip_check import is_ip_allowed

from loguru import logger

router = APIRouter()

#!----------------------------------- Account Endpoints -----------------------------------!#

#!------------------------------------ Trades Endpoints -----------------------------------!#

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

@router.post('/make-order-usdtm')
async def make_order_usdtm_endpoint(request: Request, leverage: int, symbol: str, side: str, positionSide: str, order_type: str, quantity: float):
    """
    Endpoint para realizar una orden en USDT-M.

    Parameters:
    - leverage: Leverage para la orden.
    - symbol: Símbolo de trading.
    - side: Lado de la orden (BUY/SELL).
    - positionSide: Lado de la posición (LONG/SHORT).
    - order_type: Tipo de la orden (ej. MARKET).
    - quantity: Cantidad de la orden.
    """
    client_ip = request.client.host
    
    logger.info(f"Make order request from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await make_order(leverage, symbol, side, positionSide, order_type, quantity)
        return result
    except Exception as e:
        logger.error(f"Error making order: {str(e)}")
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
        result = await get_balance_perp()    
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
    
@router.get('/get-positions-usdtm')
async def get_positions_endpoint(request: Request):
    """
    Fetches the user's positions for USDT-M perpetual futures.    

    Args:
        request (Request): The incoming request object.

    Returns:
    - symbol (string): Trading pair, e.g., BTC-USDT.
    - positionId (string): Position ID.
    - positionSide (string): Position direction, can be LONG or SHORT.
    - isolated (bool): Indicates if it is isolated margin mode. True: isolated margin mode, False: cross margin.
    - positionAmt (string): Position amount.
    - availableAmt (string): Available amount.
    - unrealizedProfit (string): Unrealized profit and loss.
    - realisedProfit (string): Realized profit and loss.
    - initialMargin (string): Initial margin.
    - margin (string): Margin.
    - avgPrice (string): Average opening price.
    - liquidationPrice (float64): Liquidation price.
    - leverage (int): Leverage.
    - positionValue (string): Position value.
    - markPrice (string): Mark price.
    - riskRate (string): Risk rate. When the risk rate reaches 100%, it will force liquidation or position reduction.
    - maxMarginReduction (string): Maximum margin reduction.
    - pnlRatio (string): Unrealized P&L ratio.
    - updateTime (int64): Position update time in milliseconds.
    
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