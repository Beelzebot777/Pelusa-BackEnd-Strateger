# Path: app/alarms/routes.py

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_alarmas, get_db_ordenes
from app.alarms.schemas import AlarmCreate, AlarmResponse
from app.alarms.crud import save_alarm, get_alarms
from app.strateger.utils import crear_operacion
from loguru import logger
from typing import List

router = APIRouter()

@router.post("/webhook", response_model=AlarmResponse)
async def webhook(request: Request, alarm_data: AlarmCreate, db: AsyncSession = Depends(get_db_alarmas), db_ordenes: AsyncSession = Depends(get_db_ordenes)):
    try:
        client_ip = request.client.host
        logger.info(f"Alarm received from {client_ip}: {alarm_data.json()}")

        variables = alarm_data.dict()
        raw_data = alarm_data.json()

        saved_alarm = await save_alarm(db, variables, raw_data)
        logger.info(f"ID Alarm saved: {saved_alarm.id}")

        await crear_operacion(db_ordenes, variables)

        return AlarmResponse.from_orm(saved_alarm)
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        raise HTTPException(status_code=500, detail="There was an error processing the alarm")

@router.get("/alarms", response_model=List[AlarmResponse])
async def get_alarms_endpoint(db: AsyncSession = Depends(get_db_alarmas)):
    try:
        alarms = await get_alarms(db)
        return [AlarmResponse.from_orm(alarm) for alarm in alarms]
    except Exception as e:
        logger.error(f"Error fetching alarms: {e}")
        raise HTTPException(status_code=500, detail="There was an error fetching the alarms")
