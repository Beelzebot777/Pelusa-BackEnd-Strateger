# Description: USDT-M Perp Futures functions for BingX exchange
import time
from .api_utils import send_request, parse_param, date_to_milliseconds

async def make_order(leverage, symbol, side, positionSide, order_type, quantity):
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

async def get_positions():
    payload = {}
    path = '/openApi/swap/v2/user/positions'
    method = "GET"
    paramsMap = {
        "recvWindow": "0",
        "timestamp": str(int(time.time() * 1000))
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
