from flask import request, jsonify, render_template

from app.alarms import alarms
from app.alarms.util import extract_variables       #Cambiar nombre a extract_variables

from app.logging.models import save_alarm_logs

from app.utils.services import enviar_data

from datetime import datetime

from app.strateger.utils import crear_operacion

import sqlite3



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
        
    #enviar_data(data, 'https://beelzebot.com/webhook')         #Deberia hacer asincrono
    
    crear_operacion(variables)
    
    return variables
                        
@alarms.route('/main', methods=['GET'])
def show_alarms():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tbl_alarms ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    
    return render_template('alarms_main.html', alarms=rows)
