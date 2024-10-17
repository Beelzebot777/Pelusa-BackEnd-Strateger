from fastapi import APIRouter, Request, HTTPException

from app.bingx.api.api_coinm import get_balance_perp_coinm, get_positions_perp_coinm

from app.utils.ip_check import is_ip_allowed
from loguru import logger

router = APIRouter()

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

@router.get('/get-positions-coinm')
async def get_positions_endpoint(request: Request):
    """
    Get user's coin-m account positions information

    Args:
    - request (Request): The incoming request object.
    
    Return:
    - code (int32): Status code.
    - msg (string): Description information.
    - timestamp (int64): Response generation time point in milliseconds.
    - data (List[Data]): List of positions.

    Data Fields:
    - symbol (string): Trading pair.
    - positionId (string): Position number.
    - positionSide (string): Holding direction, bi-directional position can only be LONG or SHORT.
    - isolated (bool): Indicates if it is per position mode. True: per position mode, False: full position.
    - positionAmt (string): Holding quantity.
    - availableAmt (string): Quantity that can be closed.
    - unrealizedProfit (string): Unrealized profit.
    - initialMargin (string): Initial margin.
    - liquidationPrice (float64): Force liquidation price.
    - avgPrice (string): Opening average price.
    - leverage (int32): Leverage.
    - markPrice (string): Mark price.
    - riskRate (string): Risk rate.
    - maxMarginReduction (string): Maximum reduction of margin.
    - updateTime (int64): Position update time in milliseconds.            

    Raises:
        HTTPException: If an error occurs while fetching the position information.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching positions from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_positions_perp_coinm()        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))