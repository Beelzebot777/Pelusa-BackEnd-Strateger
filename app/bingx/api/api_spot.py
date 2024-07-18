# Description: Spot account functions for BingX exchange
import time
from .api_utils import send_request, parse_param

async def get_balance_spot():
    """
    Envia una solicitud asíncrona para obtener el balance de cuenta en el mercado spot.

    Parámetros de la Solicitud:
    --------------------------
    La solicitud utiliza el método GET y envía los siguientes parámetros de consulta:

    - recvWindow (int64, opcional): Timestamp de inicio de la solicitud, Unidad: milisegundos.
    - timestamp (int64, requerido): Valor de ventana de tiempo válido de la solicitud, Unidad: milisegundos.

    Cuerpo de la Solicitud:
    -----------------------
    El cuerpo de la solicitud está vacío ({}).

    Endpoint:
    ---------
    /openApi/spot/v1/account/balance

    Respuesta:
    ----------
    La respuesta contiene un array de balances de activos con los siguientes campos:

    - asset (string): Nombre del activo.
    - free (string): Activo disponible.
    - locked (string): Activo congelado.

    Ejemplo de Respuesta:
    ---------------------
    {
        "balances": [
            {
                "asset": "BTC",
                "free": "0.001",
                "locked": "0.000"
            },
            {
                "asset": "ETH",
                "free": "0.100",
                "locked": "0.010"
            }
        ]
    }

    Códigos de Estado de Respuesta:
    -------------------------------
    - 200 OK: La solicitud se ha procesado correctamente.
    - 400 Bad Request: La solicitud contiene un error (por ejemplo, timestamp no válido).
    - 401 Unauthorized: La solicitud no está autorizada.
    - 500 Internal Server Error: Error del servidor.
    
    """
    payload = {}
    path = '/openApi/spot/v1/account/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)


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
