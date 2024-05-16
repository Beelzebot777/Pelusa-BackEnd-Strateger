import json

def extract_order_variables(json_string):
    try:
        parsed_data = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        return None

    order_data = parsed_data.get("data", {}).get("order", {})

    variables = {
        'Order ID': order_data.get('orderId'),
        'Symbol': order_data.get('symbol'),
        'Position Side': order_data.get('positionSide'),
        'Side': order_data.get('side'),
        'Type': order_data.get('type'),
        'Price': order_data.get('price'),
        'Quantity': order_data.get('quantity'),
        'Stop Price': order_data.get('stopPrice'),
        'Working Type': order_data.get('workingType'),
        'Client Order ID': order_data.get('clientOrderID'),
        'Time In Force': order_data.get('timeInForce'),
        'Price Rate': order_data.get('priceRate'),
        'Stop Loss': order_data.get('stopLoss'),
        'Take Profit': order_data.get('takeProfit'),
        'Reduce Only': order_data.get('reduceOnly'),
        'Activation Price': order_data.get('activationPrice'),
        'Close Position': order_data.get('closePosition'),
        'Stop Guaranteed': order_data.get('stopGuaranteed')
    }

    return variables

