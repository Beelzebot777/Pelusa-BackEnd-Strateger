from fastapi import APIRouter, Depends, HTTPException, Request, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.siteground.database import get_db_kline_data
from app.klinedata.schemas import KlineDataCreate
from app.klinedata.crud import save_kline_data, get_kline_data
from app.utils.ip_check import is_ip_allowed
from loguru import logger
from app.bingx.api.api_main import get_k_line_data
from datetime import datetime

import json

router = APIRouter()

@router.post("/create_kline_data", response_model=KlineDataCreate)
async def create_kline_data(kline_data: KlineDataCreate, db: AsyncSession = Depends(get_db_kline_data)):
    try:
        saved_kline_data = await save_kline_data(db, kline_data)
        return saved_kline_data
    except HTTPException as e:
        logger.error(f"HTTP error saving kline data: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error saving kline data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/get_kline_data", response_model=List[KlineDataCreate])
async def get_kline_data_endpoint(
    symbol: str, 
    db: AsyncSession = Depends(get_db_kline_data), 
    limit: int = Query(default=100, ge=1)
):
    try:
        kline_data = await get_kline_data(db, symbol, limit)
        return kline_data
    except HTTPException as e:
        logger.error(f"HTTP error fetching kline data: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Error fetching kline data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get('/fill-kline-data-historical')
async def fill_kline_data_historical(
    request: Request,
    symbol: str,
    interval: str,
    start_date: str,
    end_date: str,
    db: AsyncSession = Depends(get_db_kline_data)
):
    client_ip = request.client.host
    
    logger.debug(f"Fetching historical K-Line data for {symbol} from {client_ip}")

    await is_ip_allowed(client_ip)
    
    try:
        start_time = datetime.strptime(start_date, '%Y-%m-%d')
        end_time = datetime.strptime(end_date, '%Y-%m-%d')

        kline_data = await get_k_line_data(symbol, interval, 1000, str(start_time), str(end_time))

        # Si kline_data es un string, intente convertirlo a JSON
        if isinstance(kline_data, str):
            try:
                kline_data = json.loads(kline_data)
            except json.JSONDecodeError as e:
                logger.error(f"Error decoding JSON: {e}")
                raise HTTPException(status_code=400, detail="Invalid JSON response")

        # Verifica que la estructura del JSON sea la esperada
        if 'data' not in kline_data or not isinstance(kline_data['data'], list):
            raise HTTPException(status_code=400, detail="Invalid response structure")        

        for data in kline_data['data']:
            logger.debug(f"Processing data: {data}")
            kline_record = KlineDataCreate(
                symbol=symbol,
                open=float(data.get('open', 0)),
                close=float(data.get('close', 0)),
                high=float(data.get('high', 0)),
                low=float(data.get('low', 0)),
                volume=float(data.get('volume', 0)),
                time=int(data.get('time', 0)),
                intervals=interval
            )
            await save_kline_data(db, kline_record)

        return {"message": "Historical K-Line data saved successfully."}
    except Exception as e:
        logger.error(f"Error fetching or saving historical K-Line data: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
