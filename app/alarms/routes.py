from flask import request, jsonify
from app.alarms import alarms
from app.alarms.util import extract_variables       #Cambiar nombre a extract_variables
from app.bingx.util import extract_order_variables

from app.logging.models import save_alarm_logs
from app.logging.models import save_order_logs

import sqlite3
from datetime import datetime
import requests


from app.bingx.api import make_order, close_all_positions


@alarms.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        print("Datos recibidos como JSON:")
        print(data)
    except Exception as e:
        print(f"Error: {e}")
        return "Error: Datos no válidos", 400

    result = procesar(data)
    return jsonify(result), 200

def procesar(data):
    variables = extract_variables(data)
    if not variables:
        return "Error: Datos no válidos o falta de variables"

    print("Variables extraídas:")
    for key, value in variables.items():
        print(f"{key}: {value}")

    if 'Time Alert' in variables and isinstance(variables['Time Alert'], datetime):
        variables['Time Alert'] = variables['Time Alert'].strftime('%H:%M:%S %d/%m/%Y')
    
    save_alarm_logs(variables, data)
        
    enviar_data(data, 'https://beelzebot.com/webhook')   
    
    crear_operacion(variables)
    
    return variables

def crear_operacion(variables):
    
    #Lo primero que deberia hacer esta funcion es checkear la variable['Strategy'] y actuar en consecuencia
    
    if variables['Order'] == 'Open Long':
        result = make_order("5", "BTC-USDT", "BUY", "LONG", "MARKET", variables['Quantity'])
        data = extract_order_variables(result)
        save_order_logs(data)
        enviar_data(data, 'https://beelzebot.com/webhook')
    if variables['Order'] == 'Open Short':
        result = make_order("5", "BTC-USDT", "SELL", "SHORT", "MARKET", variables['Quantity'])        
        data = extract_order_variables(result)
        save_order_logs(data)
        enviar_data(data, 'https://beelzebot.com/webhook')
    if variables['Order'] == 'Close Long':        
        result = close_all_positions("BTC-USDT")                
        enviar_data(result, 'https://beelzebot.com/webhook')
    if variables['Order'] == 'Close Short':        
        result = close_all_positions("BTC-USDT")
        enviar_data(result, 'https://beelzebot.com/webhook')
        
        
        
    

def enviar_data(data, webhook_url):
    headers = {
        'Content-Type': 'text/plain; charset=utf-8',
        'User-Agent': 'PRUEBAS_TURBIAS/1.0'
    }
    try:
        response = requests.post(webhook_url, headers=headers, data=data, allow_redirects=False)        
        response.raise_for_status()        
        print(f"Data: {data}")
        print(f"response.text:{response.text}")
        print(f"response.status_code:{response.status_code}")
        print(f"response.headers:{response.headers}")
        print(f"response.request.headers:{response.request.headers}")
        print(f"response.request.body:{response.request.body}")
        print(f"response.request.url:{response.request.url}")
        print(f"response.request.method:{response.request.method}")
        print("Datos enviados al webhook externo correctamente.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error enviando datos al webhook externo: {e}")        
