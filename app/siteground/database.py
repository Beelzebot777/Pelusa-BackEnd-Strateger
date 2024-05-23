# Path: app/siteground/database.py
# Description: Database functions for siteground

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config import settings
from app.siteground.base import Base

# Configuración de las bases de datos
engine_alarmas = create_engine(
    settings.DATABASE_URL_DESARROLLO_ALARMAS,
    pool_recycle=3600,  # Reciclar conexiones cada 3600 segundos
    pool_pre_ping=True  # Verificar conexiones antes de usarlas
)
engine_ordenes = create_engine(
    settings.DATABASE_URL_DESARROLLO_ORDENES,
    pool_recycle=3600,
    pool_pre_ping=True
)

SessionLocalAlarmas = sessionmaker(autocommit=False, autoflush=False, bind=engine_alarmas)
SessionLocalOrdenes = sessionmaker(autocommit=False, autoflush=False, bind=engine_ordenes)

def get_db_alarmas():
    db = SessionLocalAlarmas()
    try:
        yield db
    finally:
        db.close()

def get_db_ordenes():
    db = SessionLocalOrdenes()
    try:
        yield db
    finally:
        db.close()

def init_db_alarmas():
    from app.alarms.models import Alarm
    Base.metadata.create_all(bind=engine_alarmas)

def init_db_ordenes():
    from app.siteground.models import Trade
    Base.metadata.create_all(bind=engine_ordenes)


def save_order_logs(db: Session, variables: dict):
    from app.siteground.models import Trade  # Importar aquí para evitar circularidad
    db_trade = Trade(
        orderOpenTime=variables.get('orderOpenTime'),
        orderId=variables.get('Order ID'),
        symbol=variables.get('Symbol'),
        positionSide=variables.get('Position Side'),
        side=variables.get('Side'),
        type=variables.get('Type'),
        price=variables.get('Price'),
        quantity=variables.get('Quantity'),
        stopPrice=variables.get('Stop Price'),
        workingType=variables.get('Working Type'),
        clientOrderID=variables.get('Client Order ID'),
        timeInForce=variables.get('Time In Force'),
        priceRate=variables.get('Price Rate'),
        stopLoss=variables.get('Stop Loss'),
        takeProfit=variables.get('Take Profit'),
        reduceOnly=variables.get('Reduce Only'),
        activationPrice=variables.get('Activation Price'),
        closePosition=variables.get('Close Position'),
        stopGuaranteed=variables.get('Stop Guaranteed')
    )
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade
