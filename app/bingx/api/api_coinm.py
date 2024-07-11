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
