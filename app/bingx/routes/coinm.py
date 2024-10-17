# Path: app/bingx/routes/coinm.py

from fastapi import APIRouter, Request

from app.bingx.controllers.coinm import get_balance_controller, get_positions_perp_coinm_controller

router = APIRouter()

@router.get('/get-balance-perp-coinm')
async def get_balance_endpoint(request: Request):
    """
    Get asset information of user‘s PERP COIN-M Account.
    """
    client_ip = request.client.host
    return await get_balance_controller(client_ip)


@router.get('/get-positions-coinm')
async def get_positions_endpoint(request: Request):
    """
    Get user's coin-m account positions information.
    """
    client_ip = request.client.host
    return await get_positions_perp_coinm_controller(client_ip)
