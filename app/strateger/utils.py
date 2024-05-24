# Path: app/strateger/utils.py
# Description: Util functions for strateger

from app.bingx.api import make_order, close_all_positions
from app.bingx.util import extract_order_variables
from app.strateger.crud import save_order
from loguru import logger
from datetime import datetime

async def crear_operacion(db_ordenes, variables):
    type_operation = variables.get('Order', '').lower()
    quantity = variables.get('Quantity')
    
    logger.info(f"Creando operación type_operation: {variables['Order']}")

    if type_operation == 'open long':
        result = await make_order("100", "BTC-USDT", "BUY", "LONG", "MARKET", "0.001")
        logger.info(f"Operacion ejecutada")
        logger.debug(f"Resultado de la orden: {result}")
        data = extract_order_variables(result)
        data['orderOpenTime'] = datetime.now()
        data['orderCloseTime'] = None
        await save_order(db_ordenes, data)  # Use await
        
    elif type_operation == 'open short':
        result = await make_order("100", "BTC-USDT", "SELL", "SHORT", "MARKET", "0.001")
        logger.info(f"Operacion ejecutada")
        logger.info(f"Resultado de la orden: {result}")
        data = extract_order_variables(result)
        data['orderOpenTime'] = datetime.now()
        data['orderCloseTime'] = None
        await save_order(db_ordenes, data)  # Use await
        
    elif type_operation == 'close long':
        result = await close_all_positions("BTC-USDT")
        logger.info("Cerrando todas las operaciones ")
        logger.debug(f"Resultado de cerrar todas las posiciones: {result}")
        
        #data['orderOpenTime'] = None
        #data['orderCloseTime'] = datetime.now()
        #await save_order(db_ordenes, data)  # Use await
        
    elif type_operation == 'close short':
        result = await close_all_positions("BTC-USDT")
        logger.info("Cerrando todas las operaciones ")
        logger.debug(f"Resultado de cerrar todas las posiciones: {result}")
        
        #data['orderOpenTime'] = None
        #data['orderCloseTime'] = datetime.now()
        #await save_order(db_ordenes, data)  # Use await
        
    else:
        logger.warning(f"Orden no reconocida: {variables['Order']}")
