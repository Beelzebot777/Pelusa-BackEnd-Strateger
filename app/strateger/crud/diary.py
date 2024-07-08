# Path: app/strateger/crud/diary.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.strateger.models.diary import DiaryEntry
from app.strateger.schemas.diary import DiaryEntryCreate, DiaryEntryUpdate

async def get_diary_entry(db: AsyncSession, entry_id: str):
    result = await db.execute(select(DiaryEntry).where(DiaryEntry.id == entry_id))
    return result.scalars().first()

async def get_diary_entries(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(DiaryEntry).offset(skip).limit(limit))
    return result.scalars().all()

async def create_diary_entry(db: AsyncSession, entry: DiaryEntryCreate):
    db_entry = DiaryEntry(**entry.dict())
    db.add(db_entry)
    await db.commit()
    await db.refresh(db_entry)
    return db_entry

async def update_diary_entry(db: AsyncSession, entry_id: str, entry: DiaryEntryUpdate):
    db_entry = await get_diary_entry(db, entry_id)
    if not db_entry:
        return None
    for key, value in entry.dict().items():
        setattr(db_entry, key, value)
    await db.commit()
    await db.refresh(db_entry)
    return db_entry

async def delete_diary_entry(db: AsyncSession, entry_id: str):
    db_entry = await get_diary_entry(db, entry_id)
    if not db_entry:
        return None
    await db.delete(db_entry)
    await db.commit()
    return db_entry
