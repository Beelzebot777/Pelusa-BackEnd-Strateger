# Path: app/strateger/routes/accounts.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.siteground.database import get_db_accounts  # Cambiado a get_db_accounts
from app.strateger.schemas.accounts import AccountBalanceCreate, AccountBalanceResponse
from app.strateger.models.accounts import AccountBalance
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=AccountBalanceResponse)
async def create_account_balance(account_balance: AccountBalanceCreate, db: AsyncSession = Depends(get_db_accounts)):  # Cambiado a get_db_accounts
    db_account_balance = AccountBalance(**account_balance.dict())
    db.add(db_account_balance)
    await db.commit()
    await db.refresh(db_account_balance)
    return AccountBalanceResponse(code=200, msg="Success", timestamp=int(datetime.utcnow().timestamp()), data=db_account_balance)

@router.get("/{account_id}", response_model=AccountBalanceResponse)
async def get_account_balance(account_id: int, db: AsyncSession = Depends(get_db_accounts)):  # Cambiado a get_db_accounts
    db_account_balance = await db.get(AccountBalance, account_id)
    if not db_account_balance:
        raise HTTPException(status_code=404, detail="Account balance not found")
    return AccountBalanceResponse(code=200, msg="Success", timestamp=int(datetime.utcnow().timestamp()), data=db_account_balance)

@router.get("/", response_model=AccountBalanceResponse)
async def list_account_balances(db: AsyncSession = Depends(get_db_accounts)):  # Cambiado a get_db_accounts
    result = await db.execute(select(AccountBalance).order_by(AccountBalance.id))
    account_balances = result.scalars().all()
    return AccountBalanceResponse(code=200, msg="Success", timestamp=int(datetime.utcnow().timestamp()), data=account_balances)
