# Path: app/strateger/models/positions.py

from sqlalchemy import Column, String, Boolean, Integer, Float, BigInteger
from app.siteground.base import BasePositions

class Position(BasePositions):
    __tablename__ = 'tbl_positions'

    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String(50), nullable=False)  # Puede ser: Main, Subaccount, etc.
    account_type = Column(String(50), nullable=False)  # Del tipo: 'Perp USDT-M', 'Perp COIN-M', 'Spot'
    symbol = Column(String(50), nullable=False)  # Añadido longitud
    positionId = Column(String(50), nullable=False)  # Añadido longitud
    positionSide = Column(String(50), nullable=False)  # Añadido longitud
    isolated = Column(Boolean, nullable=False)
    positionAmt = Column(String(50), nullable=False)  # Añadido longitud
    availableAmt = Column(String(50), nullable=False)  # Añadido longitud
    unrealizedProfit = Column(String(50), nullable=False)  # Añadido longitud
    initialMargin = Column(String(50), nullable=False)  # Añadido longitud
    liquidationPrice = Column(Float, nullable=False)
    avgPrice = Column(String(50), nullable=False)  # Añadido longitud
    leverage = Column(Integer, nullable=False)
    markPrice = Column(String(50), nullable=False)  # Añadido longitud
    riskRate = Column(String(50), nullable=False)  # Añadido longitud
    maxMarginReduction = Column(String(50), nullable=False)  # Añadido longitud
    updateTime = Column(BigInteger, nullable=False)
