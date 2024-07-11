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
