from fastapi import APIRouter, Request, HTTPException
from app.bingx.api.api_main import get_ticker, get_k_line_data
from app.utils.ip_check import is_ip_allowed

from loguru import logger

router = APIRouter()

#! main
@router.get('/get-ticker')
async def get_ticker_endpoint(request: Request, symbol: str):
    """           
    Get information about a specific trading symbol.

    Returns:
    - code: Status code of the response (0 indicates success).
    - msg: Message associated with the response (usually empty if successful).
    - data: Contains the following fields:
        - symbol: The trading pair (e.g., BTC-USDT).
        - priceChange: The price change.
        - priceChangePercent: The percentage price change.
        - lastPrice: The last price.
        - lastQty: The last quantity.
        - highPrice: The highest price.
        - lowPrice: The lowest price.
        - volume: The trading volume.
        - quoteVolume: The quote volume.
        - openPrice: The opening price.
        - openTime: The opening time (timestamp).
        - closeTime: The closing time (timestamp).
        - askPrice: The ask price.
        - askQty: The ask quantity.
        - bidPrice: The bid price.
        - bidQty: The bid quantity.
    """    
    
    client_ip = request.client.host
    
    logger.info(f"Getting data for {symbol} from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:
        result = await get_ticker(symbol)
        return result
    except Exception as e:
        logger.error(f"Error fetching ticker information: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

#! main
@router.get('/get-k-line-data')
async def get_k_line_data_endpoint(request: Request, symbol: str, interval: str, limit: str, start_date: str, end_date: str):
    """
    Fetches K-Line data for a given symbol within a specified interval.

    Parameters:
    - request: The request object.
    - symbol: The symbol for which to fetch K-Line data.
    - interval: The interval of the K-Line data (e.g., '1m', '1h', '1d').
    - limit: The maximum number of data points to fetch.
    - start_date: The start date of the data range.
    - end_date: The end date of the data range.

    Returns:
    - The fetched K-Line data.

    Raises:
    - HTTPException: If an error occurs while fetching the data.
    """
    client_ip = request.client.host
    
    logger.info(f"Fetching K-Line data for {symbol} from {client_ip}")

    # Verificar si la IP está permitida
    await is_ip_allowed(client_ip)
    
    try:       
        data = await get_k_line_data(symbol, interval, limit, start_date, end_date)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))