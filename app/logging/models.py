import sqlite3

#------------------------------------------------------------ ESTO DEBERIA IR EN logging ------------------------------------------------------------

def init_db_logs_tbl_alarms():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tbl_alarms (
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

def init_db_logs_tbl_trades():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tbl_trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            orderOpenTime TEXT,           
            orderId INTEGER,
            symbol TEXT,
            positionSide TEXT,
            side TEXT,
            type TEXT,
            price REAL,
            quantity REAL,
            stopPrice REAL,
            workingType TEXT,
            clientOrderID TEXT,
            timeInForce TEXT,
            priceRate REAL,
            stopLoss TEXT,
            takeProfit TEXT,
            reduceOnly BOOLEAN,
            activationPrice REAL,
            closePosition TEXT,
            stopGuaranteed TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_alarm_logs(variables, raw_data):
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO tbl_alarms (
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
    
def save_order_logs(variables):
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO tbl_trades (
            orderId, symbol, positionSide, side, type, price, quantity, 
            stopPrice, workingType, clientOrderID, timeInForce, priceRate, stopLoss, 
            takeProfit, reduceOnly, activationPrice, closePosition, stopGuaranteed
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', (
        variables.get('Order ID'), variables.get('Symbol'), variables.get('Position Side'), 
        variables.get('Side'), variables.get('Type'), variables.get('Price'), 
        variables.get('Quantity'), variables.get('Stop Price'), 
        variables.get('Working Type'), variables.get('Client Order ID'), 
        variables.get('Time In Force'), variables.get('Price Rate'), 
        variables.get('Stop Loss'), variables.get('Take Profit'), 
        variables.get('Reduce Only'), variables.get('Activation Price'), 
        variables.get('Close Position'), variables.get('Stop Guaranteed')
    ))
    conn.commit()
    conn.close()