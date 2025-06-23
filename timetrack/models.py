from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field


class TimeEntry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    entry_date: date
    hours: float = 0.0
    overtime: bool = False
