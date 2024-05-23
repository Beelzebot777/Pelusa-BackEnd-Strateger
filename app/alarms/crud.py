# Path: app/alarms/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.alarms.models import Alarm

async def save_alarm(db: AsyncSession, variables: dict, raw_data: str):
    db_alarm = Alarm(
        Ticker=variables.get('Ticker'),
        Temporalidad=variables.get('Temporalidad'),
        Quantity=variables.get('Quantity'),
        Entry_Price_Alert=variables.get('Entry_Price_Alert'),
        Exit_Price_Alert=variables.get('Exit_Price_Alert'),
        Time_Alert=variables.get('Time_Alert'),
        Order=variables.get('Order'),
        Strategy=variables.get('Strategy'),
        raw_data=raw_data
    )
    db.add(db_alarm)
    await db.commit()
    await db.refresh(db_alarm)
    return db_alarm

async def get_alarms(db: AsyncSession):
    result = await db.execute(select(Alarm))
    alarms = result.scalars().all()
    return alarms
