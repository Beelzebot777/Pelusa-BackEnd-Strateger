# Path: app/strateger/models/positions.py

from sqlalchemy import Column, String, Boolean, Integer, Float, BigInteger
from app.siteground.base import BasePositions

class Position(BasePositions):
    __tablename__ = 'tbl_positions'

    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String(50), nullable=False)  # Puede ser: Main, Subaccount, etc.
    account_type = Column(String(50), nullable=False)  # Del tipo: 'Perp USDT-M', 'Perp COIN-M', 'Spot'
    symbol = Column(String(50), nullable=False)
    positionId = Column(String(50), nullable=False)
    positionSide = Column(String(50), nullable=False)
    isolated = Column(Boolean, nullable=False)
    positionAmt = Column(String(50), nullable=False)
    availableAmt = Column(String(50), nullable=False)
    unrealizedProfit = Column(String(50), nullable=False)
    realisedProfit = Column(String(50), nullable=True)  # Campo adicional
    initialMargin = Column(String(50), nullable=False)
    margin = Column(String(50), nullable=True)  # Campo adicional
    avgPrice = Column(String(50), nullable=False)
    liquidationPrice = Column(Float, nullable=False)
    leverage = Column(Integer, nullable=False)
    positionValue = Column(String(50), nullable=True)  # Campo adicional
    markPrice = Column(String(50), nullable=False)
    riskRate = Column(String(50), nullable=False)
    maxMarginReduction = Column(String(50), nullable=False)
    pnlRatio = Column(String(50), nullable=True)  # Campo adicional
    updateTime = Column(BigInteger, nullable=False)
