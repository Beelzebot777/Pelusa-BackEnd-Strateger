from flask import request, jsonify
from app.logging import logging
import sqlite3

@logging.route('/get_alarms', methods=['GET'])
def view_logs():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tbl_alarms')
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
