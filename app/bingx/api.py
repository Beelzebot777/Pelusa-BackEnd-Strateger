import time
import requests
import hmac
from hashlib import sha256
import os
from dotenv import load_dotenv

# Cargar variables de entorno
#load_dotenv()

#APIURL = os.getenv("APIURL")
#APIKEY = os.getenv("APIKEY")
#SECRETKEY = os.getenv("SECRETKEY")

APIURL = "https://open-api.bingx.com"       
APIKEY = "xYSF77x4hjrLvJxdTfbZCfgP2wLnaL0aETXAajLth7MSKBkFI3HesHqIVTZcpeIspJ5Fsm2S9sU8ok360tjCQ"    #Deberian estar como variables de entorno
SECRETKEY = "wDmTupwxFfVqP5E1FG9oZU1KmhX8JsUMxzSB4fIOnSrvRUnFMV11XRrEOPNgIkdieLFQZ9p7a83uEkhGWVw"   #Deberian estar como variables de entorno


def make_order():
    payload = {}
    path = '/openApi/swap/v2/trade/order'
    method = "POST"
    paramsMap = {
        "leverage": "5",
        "symbol": "BTC-USDT",
        "side": "BUY",
        "positionSide": "LONG",
        "type": "MARKET",
        "quantity": 0.0002 
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, payload)

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
    print("demo:", make_order())
