from flask import request, jsonify
from app.alarms import alarms
from app.alarms.util import extract_variables, save_to_db
import sqlite3
from datetime import datetime


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
    
    save_to_db(variables, data)
    return variables


