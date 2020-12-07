from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(
    SQLALCHEMY_DATABASE_URI
)
SessionMaker = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.bind = engine


def get_session():
    session = SessionMaker()
    return session
