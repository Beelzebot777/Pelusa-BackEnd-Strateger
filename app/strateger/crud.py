# Path: app/strateger/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.strateger.models import Order
from datetime import datetime

async def save_order(db: AsyncSession, variables: dict):
    db_order = Order(
        orderOpenTime=variables.get('orderOpenTime'),
        orderCloseTime=variables.get('orderCloseTime'),
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
    db.add(db_order)
    await db.commit()  # Use await
    await db.refresh(db_order)  # Use await
    return db_order

async def get_orders(db: AsyncSession, limit: int = 10, offset: int = 0, latest: bool = False):
    query = select(Order).offset(offset).limit(limit)
    if latest:
        query = query.order_by(Order.id.desc())
    result = await db.execute(query)
    return result.scalars().all()
    
