# app/alarms/models.py
from sqlalchemy import Column, Integer, String, DateTime
from app.siteground.base import Base

class Alarm(Base):
    __tablename__ = 'tbl_alarms'
    
    id = Column(Integer, primary_key=True, index=True)
    Ticker = Column(String(50), index=True)
    Temporalidad = Column(String(50))
    Quantity = Column(String(50))
    Entry_Price_Alert = Column(String(50))
    Exit_Price_Alert = Column(String(50))
    Time_Alert = Column(String(50))  # Adjusted to string to match format
    Order = Column(String(50))
    Strategy = Column(String(50))
    raw_data = Column(String(500))
