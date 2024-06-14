# Path: app/alarms/routes.py

from fastapi import APIRouter, Depends, HTTPException, Request, Query       #FastAPI           
from sqlalchemy.ext.asyncio import AsyncSession                             #Base de datos        
from app.siteground.database import get_db_alarmas, get_db_estrategias      #Base de datos
from app.alarms.schemas import AlarmCreate, AlarmResponse                   #Schemas   
from app.alarms.crud import save_alarm, get_alarms                          #Base de datos
from app.utils.ip_check import is_ip_allowed                                #Seguridad
from loguru import logger                                                   #Logging
from typing import List                                                     #Tipado         
from app.strateger.orders import crear_operacion                            #Operaciones                        

router = APIRouter()

@router.post("/webhook", response_model=AlarmResponse)
async def webhook(request: Request, alarm_data: AlarmCreate, db_alarmas: AsyncSession = Depends(get_db_alarmas), db_estrategias: AsyncSession = Depends(get_db_estrategias)):
    try:
        client_ip = request.client.host
        logger.info(f"Alarm received from {client_ip}")

        # Verificar si la IP está permitida
        await is_ip_allowed(client_ip)

        logger.debug(f"Alarm Data: {alarm_data.json()}")

        variables = alarm_data.dict()
        raw_data = alarm_data.json()

        saved_alarm = await save_alarm(db_alarmas, variables, raw_data)
        logger.info(f"Alarm saved in DB, with Id: {saved_alarm.id}")

        await crear_operacion(variables, db_alarmas, db_estrategias)

        return AlarmResponse.from_orm(saved_alarm)
    except HTTPException:
        raise  # Re-lanzar la excepción HTTP
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        raise HTTPException(status_code=500, detail="There was an error processing the alarm")

@router.get("/alarms", response_model=List[AlarmResponse])
async def get_alarms_endpoint(
    request: Request,
    db: AsyncSession = Depends(get_db_alarmas),
    limit: int = Query(default=10, ge=1),  # Limit para el número de resultados por página
    offset: int = Query(default=0, ge=0),   # Offset para el desplazamiento
    latest: bool = Query(default=False)     # Parámetro para obtener las últimas alarmas
):
    client_ip = request.client.host
    # Verificar si la IP está permitida
    logger.info(f"Fetching alarms from {client_ip}")
    await is_ip_allowed(client_ip)
    
    try:
        alarms = await get_alarms(db, limit=limit, offset=offset, latest=latest)
        return [AlarmResponse.from_orm(alarm) for alarm in alarms]
    except Exception as e:
        logger.error(f"Error fetching alarms: {e}")
        raise HTTPException(status_code=500, detail="There was an error fetching the alarms")