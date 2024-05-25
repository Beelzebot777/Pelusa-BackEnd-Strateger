# Path: app/bingx/routes.py
# Description: Routes for BingX exchange

from fastapi import APIRouter, Depends, HTTPException, Request
from app.bingx.api import get_k_line_data

router = APIRouter()

@router.get('/get-k-line-data')
async def get_k_line_data_endpoint(symbol: str, interval: str, limit: str, start_date: str, end_date: str):
    try:       
        data = await get_k_line_data(symbol, interval, limit, start_date, end_date)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
