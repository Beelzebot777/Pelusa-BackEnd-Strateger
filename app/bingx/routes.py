# Path: app/bingx/routes.py
# Description: Routes for BingX exchange

from fastapi import APIRouter, Depends, HTTPException, Request
from app.bingx.util import extract_order_variables
from app.bingx.api import make_order, close_all_positions

router = APIRouter()

@router.route('/test-trade')
def trade():
    # Aquí puedes manejar los datos enviados en la solicitud si es necesario
    
    leverage = "50"
    symbol = "BTC-USDT"
    side = "BUY"
    positionSide = "LONG"
    order_type = "MARKET"
    quantity = 0.0002
    
    result = make_order(leverage, symbol, side, positionSide, order_type, quantity)
    print("----------------------------------------------------------------------------------------------------")
    print(result)
    print("----------------------------------------------------------------------------------------------------")
    
    variables = extract_order_variables(result)
    
    if not variables:
        return {"error": "Datos no válidos o falta de variables"}

    print("Variables extraídas:")
    for key, value in variables.items():
        print(f"{key}: {value}")        
    
    return ({"status": "order executed", "result": result})

@router.route('/test-close-all')
def close_all():
    symbol = "BTC-USDT"
    
    result = close_all_positions(symbol)
    print("----------------------------------------------------------------------------------------------------")
    print(result)
    print("----------------------------------------------------------------------------------------------------")       
    
    return ({"status": "all positions closed", "result": result})

