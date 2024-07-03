# Path: app/bingx/api.py
# Description: API functions for BingX exchange

import time
import requests
import hmac
from hashlib import sha256
import os
from dotenv import load_dotenv
from datetime import datetime
from loguru import logger

# Cargar variables de entorno
load_dotenv()

APIURL = os.getenv("APIURL")
APIKEY = os.getenv("APIKEY")
SECRETKEY = os.getenv("SECRETKEY")

#!----------------------------------------------------------------------------------
#!----------------------- Main Functions USDT-M Perp Futures -----------------------
#!----------------------------------------------------------------------------------

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
        "startTime": date_to_milliseconds(start_time),  # Tiempo de inicio en milisegundos
        "endTime": date_to_milliseconds(end_time)  # Tiempo de fin en milisegundos
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_balance_perp_usdtm():
    """
    Get asset information of users Perpetual Account

    Returns:
        The balance of the user.
    """
    payload = {}
    path = '/openApi/swap/v2/user/balance'
    method = "GET"
    paramsMap = {
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_positions():
    """
    Retrieves the user's positions.

    Returns:
        The response from the API call.
    """
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
    """
    Retrieves the income account information.
    If neither startTime nor endTime is sent, only the data of the last 7 days will be returned.
    If the incomeType is not sent, return all types of account profit and loss fund flow.
    Only keep the last 3 months data.

    Returns:
        The response from the API call.
    """
    payload = {}
    path = '/openApi/swap/v2/user/income'
    method = "GET"
    paramsMap = {    
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

async def get_all_orders(limit: int, offset: int):
    """
    Query the user's historical orders (order status is completed or canceled).
    The maximum query time range shall not exceed 7 days.
    Query data within the last 7 days by default.

    Args:
        limit (int): The number of orders to fetch.
        offset (int): The offset for pagination.

    Returns:
        The response from the API call.
    """
    payload = {}
    path = '/openApi/swap/v2/trade/allOrders'
    method = "GET"

    # Obtener el timestamp actual
    timestamp = str(int(time.time() * 1000))

    # Calcular el rango de tiempo basado en el offset
    end_time = timestamp
    start_time = str(int(time.time() * 1000) - 24 * 60 * 60 * 1000 * 7 * (offset + 1))  # Offset en semanas

    paramsMap = {
        "limit": str(limit),
        "startTime": start_time,
        "endTime": end_time,
        "timestamp": timestamp
    }
    paramsStr = parse_param(paramsMap)
    logger.debug(f"")
    return send_request(method, path, paramsStr, payload)

async def get_full_all_orders(limit: int, offset: int):
    """
    Query the user's historical orders (order status is fully executed, pending, newly created, partially executed, or cancelled.).

    Args:
        limit (int): The number of orders to fetch.
        offset (int): The offset for pagination.

    Returns:
        The response from the API call.
    """
    payload = {}
    path = '/openApi/swap/v1/trade/fullOrder'
    method = "GET"

    # Obtener el timestamp actual
    timestamp = str(int(time.time() * 1000))

    # Obtener el tiempo de inicio y fin basado en el offset
    end_time = timestamp
    start_time = str(int(time.time() * 1000) - 24 * 60 * 60 * 1000 * (offset + 1))  # Offset en días

    paramsMap = {
        "limit": str(limit),        
        "timestamp": timestamp
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

#!----------------------------------------------------------------------------------
#!----------------------- Main Functions SPOT --------------------------------------
#!----------------------------------------------------------------------------------

async def get_balance_spot():
    payload = {}
    path = '/openApi/spot/v1/account/balance'
    method = "GET"
    paramsMap = {        
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)




#------------------------------------------------------------
#------------------- Funciones auxiliares -------------------
#------------------------------------------------------------

def date_to_milliseconds(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return int(dt.timestamp() * 1000)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature

def send_request(method, path, urlpa, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlpa, get_sign(SECRETKEY, urlpa))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parse_param(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsStr = "&".join(["%s=%s" % (x, paramsMap[x]) for x in sortedKeys])
    if paramsStr != "": 
        return paramsStr + "&timestamp=" + str(int(time.time() * 1000))
    else:
        return paramsStr + "timestamp=" + str(int(time.time() * 1000))

if __name__ == '__main__':
    pass

    
