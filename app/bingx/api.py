# Path: app/bingx/api.py
# Description: API functions for BingX exchange

import time
import requests
import hmac
from hashlib import sha256
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

APIURL = os.getenv("APIURL")
APIKEY = os.getenv("APIKEY")
SECRETKEY = os.getenv("SECRETKEY")

#--------------------------------------------------------------
#----------------------- Main Functions -----------------------
#--------------------------------------------------------------

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


#------------------------------------------------------------
#------------------- Funciones auxiliares -------------------
#------------------------------------------------------------

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
    print("demo:", make_order("5", "BTC-USDT", "BUY", "LONG", "MARKET", 0.0002))
    
