# Path: app/strateger/orders.py

from app.bingx.api import make_order, close_all_positions
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from app.strateger.crud import get_strategy_by_name_and_ticker
from app.alarms.crud import get_latest_alarm_with_entry
from app.strateger.models import Strategy  # Asegúrate de importar el modelo Strategy

async def crear_operacion(variables: dict, db_alarmas: AsyncSession, db_estrategias: AsyncSession):
    """
    Esta funcion se encarga de crear una operacion en el exchange, dependiendo de la orden que se reciba.

    Parameters:
        - variables (dict): Diccionario de la alarma con las variables necesarias para crear una operacion en el exchange.
        - db_alarmas (AsyncSession): Sesión de base de datos para consultar alarmas.
        - db_estrategias (AsyncSession): Sesión de base de datos para consultar estrategias.
    Returns:
        - None
    """
    type_operation = variables.get('Order', '').lower()
    ticker = variables.get('Ticker')
    strategy_name = variables.get('Strategy')

    logger.info(f"Creando operación: {variables['Order']} para la estrategia: {strategy_name} y el ticker: {ticker}")

    # Si la orden es un indicador de apertura o cierre, no se realiza ninguna operación
    if type_operation in ['indicator open long', 'indicator open short', 'indicator close long', 'indicator close short']:
        logger.info(f"Operación de tipo indicador no requiere acción: {variables['Order']}")
        return

    # Obtener la estrategia de la base de datos de estrategias
    strategy = await get_strategy_by_name_and_ticker(db_estrategias, strategy_name, ticker)
    logger.debug(f"Estrategia encontrada: {strategy}")
    if not strategy:
        logger.warning(f"Estrategia no encontrada para el nombre: {strategy_name} y el ticker: {ticker}")
        return

    if type_operation in ['order open long', 'order open short']:
        await open_order(variables, strategy, db_alarmas)
    elif type_operation in ['order close long', 'order close short']:
        await close_order(variables, strategy, db_alarmas)
    else:
        logger.warning(f"Orden no reconocida: {variables['Order']}")

async def open_order(variables: dict, strategy: Strategy, db_alarmas: AsyncSession):
    
    logger.info(f"Abriendo una operación para la estrategia: {strategy.name} y el ticker: {strategy.ticker}")
    
    #! APARTIR DE AQUI DEBERIAMOS CORREGIR EL CODIGO, YA QUE PARECE SER QUE LA LOGICA NO ESTA BIEN IMPLEMENTADA
    # Buscar la última alarma con la misma estrategia y ticker que tenga un Entry_Price_Alert no nulo
    latest_alarm = await get_latest_alarm_with_entry(db_alarmas, strategy.name, strategy.ticker, 'longEntryOrder')
    
    logger.debug(f"Última alarma con Entry_Price_Alert no nulo: {latest_alarm}")

    
    if latest_alarm and latest_alarm.Exit_Price_Alert is None:
        
        logger.info(f"La última alarma con Entry_Price_Alert no nulo no tiene Exit_Price_Alert: {latest_alarm}")
        
        leverage = strategy.longLeverage
        quantity = strategy.longQuantity
        ticker = strategy.ticker
        
        logger.debug(f"Leverage: {leverage}, Quantity: {quantity}, Ticker: {ticker}")

        if variables.get('Order').lower() == 'order open long':
            result = await make_order(leverage, ticker, "BUY", "LONG", "MARKET", quantity)
        else:
            result = await make_order(leverage, ticker, "SELL", "SHORT", "MARKET", quantity)

        logger.info(f"Operacion ejecutada: {variables['Order']} para {ticker}")
        logger.debug(f"Resultado de la orden: {result}")

async def close_order(variables: dict, strategy: Strategy, db_alarmas: AsyncSession):
    ticker = strategy.ticker
    result = await close_all_positions(ticker)
    logger.info(f"Cerrando todas las operaciones para {ticker}")
    logger.debug(f"Resultado de cerrar todas las posiciones: {result}")
