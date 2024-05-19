from app.bingx.api import make_order, close_all_positions
from app.bingx.util import extract_order_variables
from app.logging.models import save_order_logs
from app.utils.services import enviar_data

def crear_operacion(variables):
    
    #Lo primero que deberia hacer esta funcion es checkear la variable['Strategy'] y actuar en consecuencia
    
    order = variables.get('Order', '').lower()
    quantity = variables.get('Quantity')
    
    print("------------------------------------------------------------")
    print("Creando operación...")
    print(f"variables['Order']: {variables['Order']}")
    
    if order == 'open long':
        print("Abriendo posición Long...")
        result = make_order("100", "BTC-USDT", "BUY", "LONG", "MARKET", "0.01")
        print(f"Resultado de la orden: {result}")
        data = extract_order_variables(result)
        save_order_logs(data)
        #enviar_data(data, 'https://beelzebot.com/webhook')
    if order == 'open short':
        print("Abriendo posición Short...")
        result = make_order("100", "BTC-USDT", "SELL", "SHORT", "MARKET", "0.01")        
        print(f"Resultado de la orden: {result}")
        data = extract_order_variables(result)
        save_order_logs(data)
        #enviar_data(data, 'https://beelzebot.com/webhook')
    if order == 'close long':        
        print("Cerrando posiciónes en Long...")
        result = close_all_positions("BTC-USDT")
        print(f"Resultado de cerrar todas las posiciones: {result}")
        #enviar_data(result, 'https://beelzebot.com/webhook')
    if order == 'close short':       
        print("Cerrando posiciónes en Short...") 
        result = close_all_positions("BTC-USDT")
        data = extract_order_variables(result)
        print(f"Resultado de cerrar todas las posiciones: {result}")
        save_order_logs(data)
        #enviar_data(result, 'https://beelzebot.com/webhook')
