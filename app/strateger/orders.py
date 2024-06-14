#Path: app/strateger/orders.py

from app.bingx.api import make_order, close_all_positions

from loguru import logger


async def crear_operacion(variables):
    '''
    Esta funcion se encarga de crear una operacion en el exchange, dependiendo de la orden que se reciba.
    
    Parameters:
        - variables (dict): Diccionario de la alarma con las variables necesarias para crear una operacion en el exchange.
    Returns:
        - None
    '''
    
    #TODO Si el 'order' de la alarma es 'indicator open long' o 'indicator open short'. NO se realizara ninguna operacion. Solo guarda la alarma
    #TODO Si el 'order' de la alarma es 'indicator close long' o 'indicator close short'. NO se realizara ninguna operacion. Solo guarda la alarma
    
    #TODO en el caso de 'order' de la alarma sea 'order...' Se realizara una Operacion y se guardara la alarma en la BD.
            
    
    #TODO Si el 'order' de la alarma es 'order open long' o 'order open short' se INTENTARA abrir una operacion en la direccion del 'order', bajo las siguientes condiciones:
        #! resultado_tbl_strategies = !Extraer de 'BD Desarrollo-Estrategias' todas las variable de la tabla: 'tbl_strategies' filtradas por ''lower('name')'' y por 'ticker'. siendo 'name' el nombre de la estrategia en la BD.
        
        #! resultado_alarma_indicador = Buscar la ultima alarma con el mismo 'name' (Strategy), 'ticker', 'Long Entry Order' de la estrategia y guardar sus variables.
        #   *si en resultado_alarma_indicador Tenemos una alarma con 'Exit_Price_Alert' no NULL, entonces NO se realiza la operacion.
        #   *si en resultado_alarma_indicador Tenemos una alarma con 'Entry_Price_Alert' no NULL, entonces SI se realiza la operacion.
        
        #? Para abrir la operacion utilizaremos la informacion guardada en la estrategia.
        
        #? Ejemplo de funcion: make_order("100", "BTC-USDT", "BUY", "LONG", "MARKET", "0.001") Donde los parametros son: Leverage, Ticker, Side, Type, Order, Quantity.
        #? Esta informacion esta en resultado_tbl_strategies y son los valores de:
            #?- 'longLeverage': Es el Leverage
            #?- 'longQuantity': Es el Quantity
            #?- 


    
    #TODO Si el 'order' de la alarma es 'order close long' o 'order close short' se INTENTARA cerrar todas las operaciones abiertas en la direccion del 'order', bajo las siguientes condiciones.
        # Se cerraran todas las operaciones de la estrategia.
    
    
    
    
    
    
    
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
