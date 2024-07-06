#Path: app/strateger/routes/diary.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.siteground.database import get_db_estrategias
from app.strateger.schemas.diary import DiaryEntryCreate, DiaryEntryUpdate, DiaryEntry
from app.strateger.crud import diary as crud_diary

router = APIRouter()

@router.post("/", response_model=DiaryEntry)
async def create_diary_entry(entry: DiaryEntryCreate, db: AsyncSession = Depends(get_db_estrategias)):
    return await crud_diary.create_diary_entry(db, entry)

# Agrega más endpoints relacionados con 'diary'
