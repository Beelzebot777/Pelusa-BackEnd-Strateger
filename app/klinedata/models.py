# Path: app/klinedata/models.py

from sqlalchemy import Column, Integer, Float, String
from app.siteground.base import BaseKLineData

class KlineData(BaseKLineData):
    __tablename__ = 'tbl_kline_data_btc'
    
    id = Column(Integer, primary_key=True, index=True)
    intervals = Column(String(50), nullable=False)
    symbol = Column(String(50), index=True)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Float)
    time = Column(Integer, index=True)
