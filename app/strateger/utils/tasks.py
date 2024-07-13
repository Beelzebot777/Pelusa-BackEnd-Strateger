# Path: app/strateger/utils/tasks.py

import asyncio
from app.bingx.api.api_usdtm import get_positions_usdtm
from app.bingx.api.api_coinm import get_positions_perp_coinm
from app.siteground.database import get_db_positions
from app.strateger.models.positions import Position
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
import json

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
            )
            db.add(db_position)
        await db.commit()
    except Exception as e:
        logger.error(f"Error fetching or saving USDT-M positions: {e}")

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
            )
            db.add(db_position)
        await db.commit()
    except Exception as e:
        logger.error(f"Error fetching or saving COIN-M positions: {e}")

async def background_tasks():
    while True:
        async for db in get_db_positions():
            await fetch_and_save_positions_usdtm(db)
            await fetch_and_save_positions_coinm(db)
        await asyncio.sleep(3600)  # Esperar 1 hora
