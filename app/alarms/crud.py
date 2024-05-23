# app/alarms/crud.py
from sqlalchemy.orm import Session
from app.alarms.models import Alarm

def save_alarm(db: Session, variables: dict, raw_data: str):
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
    db.commit()
    db.refresh(db_alarm)
    return db_alarm

def get_alarms(db: Session):
    alarms = db.query(Alarm).all()
    return [
        {
            "id": alarm.id,
            "Ticker": alarm.Ticker,
            "Temporalidad": alarm.Temporalidad,
            "Quantity": alarm.Quantity,
            "Entry_Price_Alert": alarm.Entry_Price_Alert,
            "Exit_Price_Alert": alarm.Exit_Price_Alert,
            "Time_Alert": alarm.Time_Alert,
            "Order": alarm.Order,
            "Strategy": alarm.Strategy
        }
        for alarm in alarms
    ]
