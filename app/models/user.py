from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class User (SQLModel, table = True) :
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    line_user_id : str = Field(index=True, unique=True)
    display_name : Optional[str] = None
    timezone : str = Field(default='Asia/Bangkok')
    create_at : datetime = Field(default_factory=datetime.now)