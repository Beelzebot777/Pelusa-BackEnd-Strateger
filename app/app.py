from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

def extract_variables(data):
    """
    Función para extraer variables de los datos JSON.
    :param data: Datos JSON
    :return: Diccionario con las variables extraídas
    """
    try:
        # Intenta parsear los datos como JSON
        parsed_data = json.loads(data)
    except json.JSONDecodeError:
        # Retorna None si los datos no son JSON
        return None

    # Convertir 'Time Alert' a un objeto datetime
    if 'Time Alert' in parsed_data:
        time_str = parsed_data['Time Alert'].replace('_', ' ')
        try:
            parsed_data['Time Alert'] = datetime.strptime(time_str, '%H:%M:%S %d/%m/%Y')
        except ValueError as e:
            print(f"Error al convertir el tiempo: {e}")
            return None

    # Extraer las variables
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

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Intenta parsear el contenido como JSON
        data = request.get_json(force=True)
        print("Datos recibidos como JSON:")
        print(data)
    except:
        return "Error: Datos no válidos", 400

    # Procesar la información recibida
    result = procesar(data)
    
    # Retornar el resultado del parseo
    return jsonify(result), 200

def procesar(data):
    # Ejecutar extract_variables y obtener las variables
    variables = extract_variables(json.dumps(data))
    if not variables:
        return "Error: Datos no válidos o falta de variables"

    # Imprimir las variables por separado
    print("Variables extraídas:")
    for key, value in variables.items():
        print(f"{key}: {value}")

    # Convertir 'Time Alert' de vuelta a una cadena antes de retornar
    if 'Time Alert' in variables and isinstance(variables['Time Alert'], datetime):
        variables['Time Alert'] = variables['Time Alert'].strftime('%H:%M:%S %d/%m/%Y')
    
    # Puedes realizar más procesamiento aquí si es necesario
    return variables

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
