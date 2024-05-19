from flask import request, jsonify, render_template
from app.bingx import bingx
from app.bingx.api import make_order, close_all_positions
from app.logging.models import save_order_logs
from app.bingx.util import extract_order_variables

@bingx.route('/test-trade')
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
    
    
    save_order_logs(variables)
    
    return jsonify({"status": "order executed", "result": result})

@bingx.route('/test-close-all')
def close_all():
    symbol = "BTC-USDT"
    
    result = close_all_positions(symbol)
    print("----------------------------------------------------------------------------------------------------")
    print(result)
    print("----------------------------------------------------------------------------------------------------")       
    
    return jsonify({"status": "all positions closed", "result": result})

import sqlite3

'''
@bingx.route('/trades-history', methods=['GET'])
def show_trades():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tbl_trades ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    
    return render_template('trades_main.html', trades=rows)
'''