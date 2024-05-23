# Path: app/siteground/database.py
# Description: Database functions for siteground

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.siteground.base import BaseAlarmas, BaseOrdenes
from app.alarms.models import Alarm
from app.strateger.models import Order

# Configuración de las bases de datos
engine_alarmas = create_engine(
    settings.DATABASE_URL_DESARROLLO_ALARMAS,
    pool_recycle=3600,
    pool_pre_ping=True
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
    # Crear sólo las tablas relacionadas con Alarm en DATABASE_URL_DESARROLLO_ALARMAS
    BaseAlarmas.metadata.create_all(bind=engine_alarmas)

def init_db_ordenes():
    # Crear sólo las tablas relacionadas con Order en DATABASE_URL_DESARROLLO_ORDENES
    BaseOrdenes.metadata.create_all(bind=engine_ordenes)
