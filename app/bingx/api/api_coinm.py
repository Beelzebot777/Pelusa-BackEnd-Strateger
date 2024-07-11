# Description: COIN-M Perp Futures functions for BingX exchange
import time
from .api_utils import send_request, parse_param

async def get_balance_perp_coinm():
    payload = {}
    path = '/openApi/cswap/v1/user/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000)),
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

#! CURRENTLY NOT IMPLEMENTED AND ROUTED
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

