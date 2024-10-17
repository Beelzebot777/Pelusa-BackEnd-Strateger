#Path: app/bingx/routes/spot.py

from fastapi import APIRouter, Request
from app.bingx.controllers.spot import get_balance_spot_controller, get_spot_deposit_records_controller
from app.utils.ip_check import is_ip_allowed

router = APIRouter()

@router.get('/get-balance-spot')
async def get_balance_spot_endpoint(request: Request):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_balance_spot_controller(client_ip)

@router.get('/get-spot-deposit-records')
async def get_spot_deposit_records_endpoint(request: Request):
    client_ip = request.client.host
    await is_ip_allowed(client_ip)
    return await get_spot_deposit_records_controller(client_ip)
