# Description: Main functions generic for BingX exchange
import time
from .api_utils import send_request, parse_param

async def get_ticker(symbol: str):
    path = '/openApi/swap/v2/quote/ticker'
    method = "GET"
    paramsMap = {
        "symbol": symbol,
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parse_param(paramsMap)
    return send_request(method, path, paramsStr, {})
