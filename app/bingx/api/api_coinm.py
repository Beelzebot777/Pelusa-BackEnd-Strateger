# Description: COIN-M Perp Futures functions for BingX exchange
import time
from .api_utils import send_request, parse_param
from loguru import logger

async def make_order_coinm(leverage, symbol, side, positionSide, order_type, quantity):

    payload = {}
    path = '/openApi/cswap/v1/trade/order'
    method = "POST"
    paramsMap = {
        "leverage": leverage,
        "symbol": symbol,
        "side": side,
        "positionSide": positionSide,
        "type": order_type,
        "quantity": quantity,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def close_all_positions_coinm(symbol):
    payload = {}
    path = '/openApi/cswap/v1/trade/closeAllPositions'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_balance_perp_coinm():
    """
    Envia una solicitud asíncrona para obtener el balance de cuenta en el mercado perpetuo de contratos coin-margined (COIN-M).

    Parámetros de la Solicitud:
    --------------------------
    La solicitud utiliza el método GET y envía los siguientes parámetros de consulta:

    - symbol (string, opcional): Par de trading, por ejemplo, BTC-USD, usar letras mayúsculas.
    - timestamp (int64, requerido): Marca de tiempo de la solicitud, Unidad: milisegundos.
    - recvWindow (int64, opcional): Valor de ventana de tiempo válido de la solicitud, Unidad: milisegundos.

    Cuerpo de la Solicitud:
    -----------------------
    El cuerpo de la solicitud está vacío ({}).

    Endpoint:
    ---------
    /openApi/cswap/v1/user/balance

    Respuesta:
    ----------
    La respuesta contiene los siguientes campos:

    - code (int32): Código de estado.
    - msg (string): Mensaje de descripción.
    - timestamp (int64): Marca de tiempo de generación de la respuesta, Unidad: milisegundos.
    - data (List[Data]): Lista de activos con los siguientes campos:

        - asset (string): Activo del usuario.
        - balance (string): Balance del activo.
        - equity (string): Valor neto del activo.
        - unrealizedProfit (string): Ganancia no realizada.
        - availableMargin (string): Margen disponible.
        - usedMargin (string): Margen usado.
        - freezedMargin (string): Margen congelado.
        - shortUid (string): UID del usuario.

    Ejemplo de Respuesta:
    ---------------------
    {
        "code": 200,
        "msg": "Success",
        "timestamp": 1627891234567,
        "data": [
            {
                "asset": "BTC",
                "balance": "0.500",
                "equity": "0.505",
                "unrealizedProfit": "0.005",
                "availableMargin": "0.400",
                "usedMargin": "0.100",
                "freezedMargin": "0.000",
                "shortUid": "123456789"
            }
        ]
    }

    Códigos de Estado de Respuesta:
    -------------------------------
    - 200 OK: La solicitud se ha procesado correctamente.
    - 400 Bad Request: La solicitud contiene un error (por ejemplo, timestamp no válido).
    - 401 Unauthorized: La solicitud no está autorizada.
    - 500 Internal Server Error: Error del servidor.

    Notas Adicionales:
    ------------------
    - Asegúrate de que la marca de tiempo (timestamp) sea válida y esté en el rango permitido.
    - La función send_request debe manejar la firma y el envío de la solicitud al servidor.
    """
    payload = {}
    path = '/openApi/cswap/v1/user/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000)),
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_positions_perp_coinm():
    """
    Fetches the user's positions for COIN-M perpetual futures.

    Request Parameters:
    - symbol (string, optional): Trading pair, e.g., BTC-USD. Use uppercase letters.
    - timestamp (int64, required): Request time stamp in milliseconds.
    - recvWindow (int64, optional): Request valid time window value in milliseconds.

    Response:
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
    """
    payload = {}
    path = '/openApi/cswap/v1/user/positions'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000)),
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)
