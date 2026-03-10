from datetime import datetime, time
from sqlmodel import Field, SQLModel
from typing import Optional

class Reminder (SQLModel, table = True):

    __tablename__ = "reminders"

    id : Optional[int] = Field(primary_key=True, default=None)
    task_id : Optional[int] = Field(foreign_key="tasks.id")
    remind_time : time
    is_active : bool = Field(default=True)
    repeat_days : Optional[str] = Field(default="", description="Comma-separated days e.g. '1,2,3'")
    last_sent_at : Optional[datetime] = None