from sqlmodel import Session, create_engine, SQLModel
from app import config
from app.models.reminder import Reminder
from app.models.task import Task
from app.models.user import User

engine = create_engine(config.DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session ():
    with Session(engine) as session :
        yield session