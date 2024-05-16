from flask import request, jsonify
from app.bingx import bingx
from app.bingx.api import make_order
from app.logging.models import save_order_logs
from app.bingx.util import extract_order_variables

@bingx.route('/trade')
def trade():
    # Aquí puedes manejar los datos enviados en la solicitud si es necesario
    result = make_order()
    print("----------------------------------------------------------------------------------------------------")
    print(result)
    print("----------------------------------------------------------------------------------------------------")
    
    variables = extract_order_variables(result)
    
    if not variables:
        return {"error": "Datos no válidos o falta de variables"}

    print("Variables extraídas:")
    for key, value in variables.items():
        print(f"{key}: {value}")
    
    
    save_order_logs(variables)
    
    return jsonify({"status": "order executed", "result": result})
