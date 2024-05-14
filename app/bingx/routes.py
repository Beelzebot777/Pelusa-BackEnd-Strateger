from flask import request, jsonify
from app.bingx import bingx
from app.bingx.api import make_order

@bingx.route('/trade')
def trade():
    # Aquí puedes manejar los datos enviados en la solicitud si es necesario
    result = make_order()
    return jsonify({"status": "order executed", "result": result})
