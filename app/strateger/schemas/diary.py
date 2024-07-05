from pydantic import BaseModel
from typing import Optional

class DiaryEntryBase(BaseModel):
    entry_id: int
    strategy_id: int
    ticker: str
    note: str
    timestamp: str

class DiaryEntryCreate(DiaryEntryBase):
    pass

class DiaryEntryUpdate(DiaryEntryBase):
    pass

class DiaryEntryInDBBase(DiaryEntryBase):
    id: int

    class Config:
        from_attributes = True

class DiaryEntry(DiaryEntryInDBBase):
    pass

class DiaryEntryInDB(DiaryEntryInDBBase):
    pass
