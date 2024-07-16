import asyncio
from app.bingx.api.api_usdtm import get_positions_usdtm
from app.bingx.api.api_coinm import get_positions_perp_coinm
from app.siteground.database import get_db_positions
from app.strateger.models.positions import Position
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
import json
from datetime import datetime
import os

def get_fecha_hora_actual():
    """Retorna la fecha y hora actual en formato MM:HH DD/MM/YYYY"""
    ahora = datetime.now()
    return ahora.strftime("%H:%M %d/%m/%Y")

async def fetch_and_save_positions_usdtm(db: AsyncSession):
    try:
        response = await get_positions_usdtm()
        response_json = json.loads(response)
        positions_data = response_json.get('data', [])

        for position in positions_data:
            db_position = Position(
                account_name="Main Account",
                account_type="Perp USDT-M",
                symbol=position['symbol'],
                positionId=position['positionId'],
                positionSide=position['positionSide'],
                isolated=position['isolated'],
                positionAmt=position['positionAmt'],
                availableAmt=position['availableAmt'],
                unrealizedProfit=position['unrealizedProfit'],
                realisedProfit=position.get('realisedProfit', '0.0'),  # Valor por defecto
                initialMargin=position['initialMargin'],
                margin=position.get('margin', '0.0'),  # Valor por defecto
                avgPrice=position['avgPrice'],
                liquidationPrice=position['liquidationPrice'],
                leverage=position['leverage'],
                positionValue=position.get('positionValue', '0.0'),  # Valor por defecto
                markPrice=position['markPrice'],
                riskRate=position['riskRate'],
                maxMarginReduction=position['maxMarginReduction'],
                pnlRatio=position.get('pnlRatio', '0.0'),  # Valor por defecto
                updateTime=position['updateTime'],
                dateTime=get_fecha_hora_actual()  # Nueva columna con la fecha y hora actual
            )
            db.add(db_position)
        await db.commit()
        logger.info("Successfully fetched and saved USDT-M positions.")
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

async def fetch_and_save_positions_coinm(db: AsyncSession):
    try:
        response = await get_positions_perp_coinm()
        response_json = json.loads(response)
        positions_data = response_json.get('data', [])

        for position in positions_data:
            db_position = Position(
                account_name="Main Account",
                account_type="Perp COIN-M",
                symbol=position['symbol'],
                positionId=position['positionId'],
                positionSide=position['positionSide'],
                isolated=position['isolated'],
                positionAmt=position['positionAmt'],
                availableAmt=position['availableAmt'],
                unrealizedProfit=position['unrealizedProfit'],
                realisedProfit=position.get('realisedProfit', '0.0'),  # Valor por defecto
                initialMargin=position['initialMargin'],
                margin=position.get('margin', '0.0'),  # Valor por defecto
                avgPrice=position['avgPrice'],
                liquidationPrice=position['liquidationPrice'],
                leverage=position['leverage'],
                positionValue=position.get('positionValue', '0.0'),  # Valor por defecto
                markPrice=position['markPrice'],
                riskRate=position['riskRate'],
                maxMarginReduction=position['maxMarginReduction'],
                pnlRatio=position.get('pnlRatio', '0.0'),  # Valor por defecto
                updateTime=position['updateTime'],
                dateTime=get_fecha_hora_actual()  # Nueva columna con la fecha y hora actual
            )
            db.add(db_position)
        await db.commit()
        logger.info("Successfully fetched and saved COIN-M positions.")
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

async def background_tasks():
    interval = int(os.getenv('FETCH_INTERVAL', 3600))  # Fetch interval in seconds, default is 1 hour
    while True:
        try:
            async for db in get_db_positions():
                await asyncio.gather(
                    fetch_and_save_positions_usdtm(db),
                    fetch_and_save_positions_coinm(db)
                )
            logger.info("Sleeping for {} seconds.".format(interval))
            await asyncio.sleep(interval)
        except Exception as e:
            logger.error(f"Unexpected error in background_tasks: {e}")
