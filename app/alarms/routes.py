from flask import request, jsonify
from app.alarms import alarms
from app.alarms.util import extract_variables
from app.logging.models import save_alarm_logs
import sqlite3
from datetime import datetime
import requests


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
    
    return variables

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
