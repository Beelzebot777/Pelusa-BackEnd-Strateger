# Path: app/strateger/utils.py
# Description: Util functions for strateger

from app.bingx.api import make_order, close_all_positions

from loguru import logger


async def crear_operacion(variables):
    type_operation = variables.get('Order', '').lower()
    quantity = variables.get('Quantity')
    
    logger.info(f"Creando operación type_operation: {variables['Order']}")

    if type_operation == 'order open long':
        result = await make_order("100", "BTC-USDT", "BUY", "LONG", "MARKET", "0.001")
        logger.info(f"Operacion ejecutada")
        logger.debug(f"Resultado de la orden: {result}")
   
        
    elif type_operation == 'order open short':
        result = await make_order("100", "BTC-USDT", "SELL", "SHORT", "MARKET", "0.001")
        logger.info(f"Operacion ejecutada")
        logger.info(f"Resultado de la orden: {result}")
     
    elif type_operation == 'order close long':
        result = await close_all_positions("BTC-USDT")
        logger.info("Cerrando todas las operaciones ")
        logger.debug(f"Resultado de cerrar todas las posiciones: {result}")
        
    elif type_operation == 'order close short':
        result = await close_all_positions("BTC-USDT")
        logger.info("Cerrando todas las operaciones ")
        logger.debug(f"Resultado de cerrar todas las posiciones: {result}")
        
    else:
        logger.warning(f"Orden no reconocida: {variables['Order']}")
