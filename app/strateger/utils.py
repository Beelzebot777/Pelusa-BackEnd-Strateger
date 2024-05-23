#Path: app/strateger/utils.py
#Description: Util functions for strateger

from app.bingx.api import make_order, close_all_positions
from loguru import logger

async def crear_operacion(variables):
    # Lo primero que deberia hacer esta funcion es checkear la variable['Strategy'] y actuar en consecuencia
    
    type_operation = variables.get('Order', '').lower()
    quantity = variables.get('Quantity')
    
    logger.info(f"Creando operación type_operation: {variables['Order']}")
    
    if type_operation == 'open long':        
        result = await make_order("100", "BTC-USDT", "BUY", "LONG", "MARKET", "0.001")
        logger.info(f"Resultado de la orden: {result}")
        # data = extract_order_variables(result)
        # save_order_logs(data)
        # await enviar_data(data, 'https://beelzebot.com/webhook')
        
    elif type_operation == 'open short':        
        result = await make_order("100", "BTC-USDT", "SELL", "SHORT", "MARKET", "0.001")
        logger.info(f"Resultado de la orden: {result}")
        # data = extract_order_variables(result)
        # save_order_logs(data)
        # await enviar_data(data, 'https://beelzebot.com/webhook')
        
    elif type_operation == 'close long':        
        result = await close_all_positions("BTC-USDT")
        logger.info(f"Resultado de cerrar todas las posiciones: {result}")
        # save_order_logs(data)
        # await enviar_data(result, 'https://beelzebot.com/webhook')
        
    elif type_operation == 'close short':        
        result = await close_all_positions("BTC-USDT")
        logger.info(f"Resultado de cerrar todas las posiciones: {result}")
        # save_order_logs(data)
        # await enviar_data(result, 'https://beelzebot.com/webhook')
        
    else:
        logger.warning(f"Orden no reconocida: {variables['Order']}")
