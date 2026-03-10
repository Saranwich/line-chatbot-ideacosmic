from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class Task (SQLModel, table = True):

    __tablename__ = "tasks"

    id : Optional[int] = Field(primary_key=True,default=None)
    user_id : Optional[int] = Field(foreign_key="users.id")
    title : str = Field(default="Notification!")
    status : str = Field(default="OPEN")
    image_url : Optional[str] = None