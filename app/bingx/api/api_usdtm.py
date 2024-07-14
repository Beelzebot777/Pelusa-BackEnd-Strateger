# Description: USDT-M Perp Futures functions for BingX exchange
import time
from .api_utils import send_request, parse_param, date_to_milliseconds

async def make_order_usdtm(leverage, symbol, side, positionSide, order_type, quantity):
    payload = {}
    path = '/openApi/swap/v2/trade/order'
    method = "POST"
    paramsMap = {
        "leverage": leverage,
        "symbol": symbol,
        "side": side,
        "positionSide": positionSide,
        "type": order_type,
        "quantity": quantity
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def close_all_positions(symbol):
    payload = {}
    path = '/openApi/swap/v2/trade/closeAllPositions'
    method = "POST"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_k_line_data(symbol, interval, limit, start_time, end_time):
    payload = {}
    path = '/openApi/swap/v3/quote/klines'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
        "startTime": date_to_milliseconds(start_time),
        "endTime": date_to_milliseconds(end_time)
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_balance_perp_usdtm():
    payload = {}
    path = '/openApi/swap/v2/user/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000)),
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_income_acc():
    payload = {}
    path = '/openApi/swap/v2/user/income'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_all_orders(limit: int, offset: int):
    payload = {}
    path = '/openApi/swap/v2/trade/allOrders'
    method = "GET"
    timestamp = str(int(time.time() * 1000))
    end_time = timestamp
    start_time = str(int(time.time() * 1000) - 24 * 60 * 60 * 1000 * 7 * (offset + 1))
    paramsMap = {
        "limit": str(limit),
        "startTime": start_time,
        "endTime": end_time,
        "timestamp": timestamp
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_full_all_orders(limit: int, offset: int):
    payload = {}
    path = '/openApi/swap/v1/trade/fullOrder'
    method = "GET"
    timestamp = str(int(time.time() * 1000))
    end_time = timestamp
    start_time = str(int(time.time() * 1000) - 24 * 60 * 60 * 1000 * (offset + 1))
    paramsMap = {
        "limit": str(limit),
        "timestamp": timestamp
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_positions_usdtm():
    """
    Fetches the user's positions for USDT-M perpetual futures.

    Request Parameters:
    - symbol (string, optional): Trading pair symbol with a hyphen, e.g., BTC-USDT.
    - timestamp (int64, required): Request timestamp in milliseconds.
    - recvWindow (int64, optional): Request valid time window value in milliseconds.

    Response:
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
    """
    payload = {}
    path = '/openApi/swap/v2/user/positions'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)