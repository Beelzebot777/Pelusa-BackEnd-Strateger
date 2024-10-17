from fastapi import APIRouter, Request, HTTPException

from app.bingx.api.api_spot import get_balance_spot, get_spot_deposit_records
from app.utils.ip_check import is_ip_allowed
from loguru import logger

router = APIRouter()

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
  
@router.get('/get-spot-deposit-records')
async def get_positions_endpoint(request: Request):
    """
    Get user's positions information

    Args:
        request (Request): The incoming request object.

     Returns:
        amount: DECIMAL                 Monto de recarga.
        coin: string                    Nombre de la moneda.
        network: string                 Red de recarga.
        status: int                     Estado (0-En progreso, 6-Cadena cargada, 1-Completado).
        address: string                 Dirección de recarga.
        addressTag: string              Observación.
        txId: LONG                      ID de la transacción.
        insertTime: LONG                Hora de la transacción.
        transferType: LONG              Tipo de transacción (0 = Recarga).
        unlockConfirm: LONG             Confirmaciones para desbloqueo.
        confirmTimes: LONG              Confirmaciones de la red.
        sourceAddress: string           Dirección de origen.            

    Raises:
        HTTPException: If an error occurs while fetching the position information.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching positions from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_spot_deposit_records()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))