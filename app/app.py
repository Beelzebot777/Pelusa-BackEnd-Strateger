from flask import Flask, request, jsonify
from datetime import datetime
import json
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('logging.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tbl_logging (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            temporalidad TEXT,
            quantity TEXT,
            entry_price_alert TEXT,
            exit_price_alert TEXT,
            time_alert TEXT,
            orden TEXT,
            strategy TEXT,
            raw_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def extract_variables(data):
    try:
        parsed_data = json.loads(data)
    except json.JSONDecodeError:
        return None

    if 'Time Alert' in parsed_data:
        time_str = parsed_data['Time Alert'].replace('_', ' ')
        try:
            parsed_data['Time Alert'] = datetime.strptime(time_str, '%H:%M:%S %d/%m/%Y')
        except ValueError as e:
            print(f"Error al convertir el tiempo: {e}")
            return None

    variables = {
        'Ticker': parsed_data.get('Ticker'),
        'Temporalidad': parsed_data.get('Temporalidad'),
        'Quantity': parsed_data.get('Quantity'),
        'Entry Price Alert': parsed_data.get('Entry Price Alert'),
        'Exit Price Alert': parsed_data.get('Exit Price Alert'),
        'Time Alert': parsed_data.get('Time Alert'),
        'Order': parsed_data.get('Order'),
        'Strategy': parsed_data.get('Strategy')
    }

    return variables

def save_to_db(variables, raw_data):
    conn = sqlite3.connect('logging.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO tbl_logging (
            ticker, temporalidad, quantity, entry_price_alert, exit_price_alert, 
            time_alert, orden, strategy, raw_data
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        variables.get('Ticker'), variables.get('Temporalidad'), variables.get('Quantity'), 
        variables.get('Entry Price Alert'), variables.get('Exit Price Alert'), 
        variables.get('Time Alert'), variables.get('Order'), variables.get('Strategy'), 
        raw_data
    ))
    conn.commit()
    conn.close()

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        print("Datos recibidos como JSON:")
        print(data)
    except:
        return "Error: Datos no válidos", 400

    result = procesar(data)
    return jsonify(result), 200

def procesar(data):
    variables = extract_variables(json.dumps(data))
    if not variables:
        return "Error: Datos no válidos o falta de variables"

    print("Variables extraídas:")
    for key, value in variables.items():
        print(f"{key}: {value}")

    if 'Time Alert' in variables and isinstance(variables['Time Alert'], datetime):
        variables['Time Alert'] = variables['Time Alert'].strftime('%H:%M:%S %d/%m/%Y')
    
    save_to_db(variables, json.dumps(data))
    return variables

@app.route('/logs', methods=['GET'])
def view_logs():
    conn = sqlite3.connect('logging.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tbl_logging')
    rows = c.fetchall()
    conn.close()
    
    logs = []
    for row in rows:
        logs.append({
            'id': row[0],
            'ticker': row[1],
            'temporalidad': row[2],
            'quantity': row[3],
            'entry_price_alert': row[4],
            'exit_price_alert': row[5],
            'time_alert': row[6],
            'orden': row[7],
            'strategy': row[8],
            'raw_data': row[9]
        })
    
    return jsonify(logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
