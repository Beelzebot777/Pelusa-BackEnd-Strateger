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
