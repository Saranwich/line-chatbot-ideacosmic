from sqlmodel import Session, create_engine
from app import config

engine = create_engine(config.DATABASE_URL, echo=True)

def get_session ():
    with Session(engine) as session :
        yield session