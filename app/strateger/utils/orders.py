#Path: app/strateger/utils/orders.py

from app.bingx.api.api_usdtm import make_order_usdtm, close_all_positions
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from app.strateger.crud import get_strategy_by_name_and_ticker
from app.alarms.crud import get_latest_alarm_with_entry
from app.strateger.models.strategies import Strategy  # Asegúrate de importar el modelo Strategy correctamente

async def crear_operacion(variables: dict, db_alarmas: AsyncSession, db_estrategias: AsyncSession):
    """
    Esta función se encarga de crear una operación en el exchange, dependiendo de la orden que se reciba.

    Parameters:
        - variables (dict): Diccionario de la alarma con las variables necesarias para crear una operación en el exchange.
        - db_alarmas (AsyncSession): Sesión de base de datos para consultar alarmas.
        - db_estrategias (AsyncSession): Sesión de base de datos para consultar estrategias.
    Returns:
        - None
    """
    type_operation = variables.get('Order', '').lower()
    ticker = variables.get('Ticker')
    strategy_name = variables.get('Strategy')
    temporalidad = variables.get('Temporalidad')

    # Si la orden es un indicador de apertura o cierre, no se realiza ninguna operación
    if type_operation in ['indicator open long', 'indicator open short', 'indicator close long', 'indicator close short']:
        logger.info(f"Operación de tipo indicador no requiere acción: {variables['Order']}")
        return

    # Obtener la estrategia de la base de datos de estrategias
    strategy = await get_strategy_by_name_and_ticker(db_estrategias, strategy_name, ticker)

    if not strategy:
        logger.warning(f"Estrategia no encontrada para el nombre: {strategy_name} O por el ticker: {ticker}")
        return

    if strategy.isOn == False:
        logger.warning(f"La estrategia {strategy.name} está apagada.")
        return

    #! Checkear la apiKey y la secretKey, ambas deberían estar encriptadas en la base de datos.
    #! Al parecer la tabla de estrategias debería tener una columna más llamada currentLongPyramiding y currentShortPyramiding.

    if type_operation in ['order open long']:
        if strategy.longEntryOrder == temporalidad:
            ultima_alarm_indicator_open_long = await get_latest_alarm_with_entry(db_alarmas, strategy.name, strategy.ticker, 'indicator open long', strategy.longEntryIndicator)
            ultima_alarm_indicator_close_long = await get_latest_alarm_with_entry(db_alarmas, strategy.name, strategy.ticker, 'indicator close long', strategy.longCloseIndicator)

            logger.debug(f"Ultima alarma con indicador de apertura de posición larga: {ultima_alarm_indicator_open_long.id}")
            logger.debug(f"Ultima alarma con indicador de cierre de posición larga: {ultima_alarm_indicator_close_long.id}")

            if int(ultima_alarm_indicator_open_long.id) > int(ultima_alarm_indicator_close_long.id):
                logger.info(f"Significa que se encontró primero una alarma de apertura de posición larga y luego una de cierre de posición larga.")
                logger.info(f"Se procede a abrir una posición larga.")

                result = await make_order_usdtm(strategy.longLeverage, convert_ticker(ticker), "BUY", "LONG", "MARKET", strategy.longQuantity)
                logger.debug(f"Resultado de abrir una posición larga: {result}")

            else:
                logger.warning(f"La última alarma de apertura de posición larga es mayor que la última alarma de cierre de posición larga.")
                logger.warning(f"Esto significa que en base a nuestra estrategia aún no se puede abrir una posición larga.")
                return
        else:
            logger.warning(f"La orden no es válida para la estrategia")
            return

    elif type_operation in ['order open short']:
        if strategy.shortEntryOrder == temporalidad:
            ultima_alarm_indicator_open_short = await get_latest_alarm_with_entry(db_alarmas, strategy.name, strategy.ticker, 'indicator open short', strategy.shortEntryIndicator)
            ultima_alarm_indicator_close_short = await get_latest_alarm_with_entry(db_alarmas, strategy.name, strategy.ticker, 'indicator close short', strategy.shortCloseIndicator)

            logger.debug(f"Ultima alarma con indicador de apertura de posición corta: {ultima_alarm_indicator_open_short.id}")
            logger.debug(f"Ultima alarma con indicador de cierre de posición corta: {ultima_alarm_indicator_close_short.id}")

            if int(ultima_alarm_indicator_open_short.id) > int(ultima_alarm_indicator_close_short.id):
                logger.info(f"Significa que se encontró primero una alarma de apertura de posición corta y luego una de cierre de posición corta.")
                logger.info(f"Se procede a abrir una posición corta.")
                result = await make_order_usdtm(strategy.shortLeverage, convert_ticker(ticker), "SELL", "SHORT", "MARKET", strategy.shortQuantity)
                logger.debug(f"Resultado de abrir una posición corta: {result}")

            else:
                logger.warning(f"La última alarma de apertura de posición corta es mayor que la última alarma de cierre de posición corta.")
                logger.warning(f"Esto significa que en base a nuestra estrategia aún no se puede abrir una posición corta.")
                return

    elif type_operation in ['order close long']:
        if strategy.longCloseOrder == temporalidad:
            logger.info(f"Se procede a cerrar todas las posiciones largas.")
            result = await close_all_positions(convert_ticker(ticker))  # ! ESTO SOLO DEBERÍA CERRAR LAS POSICIONES LARGAS NO TODAS LAS POSICIONES
            logger.info(f"Cerrando todas las operaciones para {ticker}")
            logger.debug(f"Resultado de cerrar todas las posiciones: {result}")

    elif type_operation in ['order close short']:
        if strategy.shortCloseOrder == temporalidad:
            logger.info(f"Se procede a cerrar todas las posiciones cortas.")
            result = await close_all_positions(convert_ticker(ticker))  # ! ESTO SOLO DEBERÍA CERRAR LAS POSICIONES CORTAS NO TODAS LAS POSICIONES
            logger.info(f"Cerrando todas las operaciones para {ticker}")
            logger.debug(f"Resultado de cerrar todas las posiciones: {result}")
    else:
        logger.error(f"La orden no es válida para la estrategia")
        return

def convert_ticker(ticker):
    if ticker == 'BTCUSDT.PS':
        return 'BTC-USDT'
    return ticker
