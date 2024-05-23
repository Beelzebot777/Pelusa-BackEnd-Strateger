# Path: app/strateger/utils.py
# Description: Util functions for strateger

from app.bingx.api import make_order, close_all_positions
from app.bingx.util import extract_order_variables
from app.strateger.crud import save_order
from loguru import logger

from datetime import datetime

async def crear_operacion(db_ordenes, variables):
    # Lo primero que deberia hacer esta funcion es checkear la variable['Strategy'] y actuar en consecuencia
    
    type_operation = variables.get('Order', '').lower()
    quantity = variables.get('Quantity')
    
    logger.info(f"Creando operación type_operation: {variables['Order']}")
    
    if type_operation == 'open long':
        result = await make_order("100", "BTC-USDT", "BUY", "LONG", "MARKET", "0.001")        
        logger.info(f"Resultado de la orden: {result}")
        
        data = extract_order_variables(result)
        
        data['orderOpenTime'] = datetime.now()
        data['orderCloseTime'] = None
        save_order(db_ordenes, data)  # Utilizar la versión asíncrona
        
    elif type_operation == 'open short':
        result = await make_order("100", "BTC-USDT", "SELL", "SHORT", "MARKET", "0.001")        
        logger.info(f"Resultado de la orden: {result}")
        
        data = extract_order_variables(result)
        
        data['orderOpenTime'] = datetime.now()
        data['orderCloseTime'] = None
        save_order(db_ordenes, data)  # Utilizar la versión asíncrona
        
    elif type_operation == 'close long':
        result = await close_all_positions("BTC-USDT")
        #data['orderOpenTime'] = None
        #data['orderCloseTime'] = datetime.now()
        logger.info(f"Resultado de cerrar todas las posiciones: {result}")
        
    elif type_operation == 'close short':
        result = await close_all_positions("BTC-USDT")
        #data['orderOpenTime'] = None
        #data['orderCloseTime'] = datetime.now()
        logger.info(f"Resultado de cerrar todas las posiciones: {result}")
        
    else:
        logger.warning(f"Orden no reconocida: {variables['Order']}")
