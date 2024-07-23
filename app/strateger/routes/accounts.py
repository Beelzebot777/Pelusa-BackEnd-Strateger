# Path: app/strateger/routes/accounts.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from app.siteground.database import get_db_accounts
from app.strateger.schemas.accounts import AccountListResponse
from app.strateger.crud.accounts import get_all_accounts
from datetime import datetime

router = APIRouter()

@router.get("/get-all-data", response_model=AccountListResponse)
async def get_all_accounts_endpoint(db: AsyncSession = Depends(get_db_accounts)):
    try:
        accounts = await get_all_accounts(db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return AccountListResponse(code=200, msg="Success", timestamp=int(datetime.utcnow().timestamp()), data=accounts)
