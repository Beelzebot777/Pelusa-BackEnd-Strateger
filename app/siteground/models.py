# Path: app/siteground/models.py
# Description: SQLAlchemy models for siteground

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from app.siteground.base import Base  # Importar Base desde base.py

class Trade(Base):
    __tablename__ = 'tbl_trades'
    
    id = Column(Integer, primary_key=True, index=True)
    orderOpenTime = Column(String(50))  # Definir longitud para VARCHAR
    orderId = Column(Integer)
    symbol = Column(String(50))  # Definir longitud para VARCHAR
    positionSide = Column(String(50))  # Definir longitud para VARCHAR
    side = Column(String(50))  # Definir longitud para VARCHAR
    type = Column(String(50))  # Definir longitud para VARCHAR
    price = Column(Float)
    quantity = Column(Float)
    stopPrice = Column(Float)
    workingType = Column(String(50))  # Definir longitud para VARCHAR
    clientOrderID = Column(String(50))  # Definir longitud para VARCHAR
    timeInForce = Column(String(50))  # Definir longitud para VARCHAR
    priceRate = Column(Float)
    stopLoss = Column(Float)
    takeProfit = Column(Float)
    reduceOnly = Column(Boolean)
    activationPrice = Column(Float)
    closePosition = Column(String(50))  # Definir longitud para VARCHAR
    stopGuaranteed = Column(String(50))  # Definir longitud para VARCHAR
