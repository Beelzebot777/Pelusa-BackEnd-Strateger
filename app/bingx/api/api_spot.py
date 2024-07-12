# Description: Spot account functions for BingX exchange
import time
from .api_utils import send_request, parse_param

async def get_balance_spot():
    payload = {}
    path = '/openApi/spot/v1/account/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

#! CURRENTLY NOT IMPLEMENTED AND ROUTED
async def get_spot_deposit_records():
    """
    Obtiene los registros de depósitos spot.
    
    Parametros:    
        coin: string (opcional)         Nombre de la moneda.
        status: int (opcional)          Estado (0-En progreso, 6-Cadena cargada, 1-Completado).
        startTime: LONG (opcional)      Hora de inicio (en milisegundos).
        endTime: LONG (opcional)        Hora de finalización (en milisegundos).
        offset: int (opcional)          Desplazamiento, por defecto 0.
        limit: int (opcional)           Tamaño de página, por defecto 1000, no puede exceder 1000.
        recvWindow: LONG (opcional)     Tiempo de ventana de ejecución, no puede ser mayor a 60000.
        timestamp: LONG (obligatorio)   Timestamp actual.

    Returns  dict   Respuesta del API en formato JSON.    
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
    """
    payload = {}
    path = '/openApi/api/v3/capital/deposit/hisrec'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)
