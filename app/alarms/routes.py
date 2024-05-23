# Path: app/alarms/routes.py

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.siteground.database import get_db_alarmas
from app.alarms.schemas import AlarmCreate, AlarmResponse
from app.alarms.crud import save_alarm, get_alarms

from app.strateger.utils import crear_operacion

from loguru import logger
from typing import List

router = APIRouter()

@router.post("/webhook", response_model=AlarmResponse)
async def webhook(request: Request, alarm_data: AlarmCreate, db: Session = Depends(get_db_alarmas)):
    try:
        client_ip = request.client.host
        logger.info(f"Alarm received from {client_ip}: {alarm_data.model_dump_json()}")
        
        variables = alarm_data.model_dump()  # Utilizando model_dump()
        raw_data = alarm_data.model_dump_json()  # Utilizando model_dump_json()

        saved_alarm = save_alarm(db, variables, raw_data)
        logger.info(f"ID Alarm saved: {saved_alarm.id}")
        
        await crear_operacion(variables)
        
        # Crear y devolver AlarmResponse usando model_validate
        return AlarmResponse.model_validate(saved_alarm)
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        raise HTTPException(status_code=500, detail="There was an error processing the alarm")

@router.get("/alarms", response_model=List[AlarmResponse])
async def get_alarms_endpoint(db: Session = Depends(get_db_alarmas)):
    try:
        alarms = get_alarms(db)
        return [AlarmResponse.model_validate(alarm) for alarm in alarms]
    except Exception as e:
        logger.error(f"Error fetching alarms: {e}")
        raise HTTPException(status_code=500, detail="There was an error fetching the alarms")
    
