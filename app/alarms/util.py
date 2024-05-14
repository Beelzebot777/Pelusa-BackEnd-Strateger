import json
import sqlite3
from datetime import datetime

def extract_variables(parsed_data):
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

#------------------------------------------------------------ ESTO DEBERIA IR EN logging ------------------------------------------------------------

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
        str(raw_data)
    ))
    conn.commit()
    conn.close()
