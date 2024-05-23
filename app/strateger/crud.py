# Path: app/strateger/crud.py

from sqlalchemy.orm import Session
from app.strateger.models import Order

def save_order(db: Session, variables: dict):    
    db_order = Order(
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
    db.add(db_order)
    db.commit()
    db.refresh(db_order)    
    return db_order

def get_orders(db: Session):
    orders = db.query(Order).all()
    return [
        {
            "id": order.id,
            "orderOpenTime": order.orderOpenTime,
            "orderId": order.orderId,
            "symbol": order.symbol,
            "positionSide": order.positionSide,
            "side": order.side,
            "type": order.type,
            "price": order.price,
            "quantity": order.quantity,
            "stopPrice": order.stopPrice,
            "workingType": order.workingType,
            "clientOrderID": order.clientOrderID,
            "timeInForce": order.timeInForce,
            "priceRate": order.priceRate,
            "stopLoss": order.stopLoss,
            "takeProfit": order.takeProfit,
            "reduceOnly": order.reduceOnly,
            "activationPrice": order.activationPrice,
            "closePosition": order.closePosition,
            "stopGuaranteed": order.stopGuaranteed
        }
        for order in orders
    ]