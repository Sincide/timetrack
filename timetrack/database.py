from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path

DATABASE_URL = "sqlite:///timetrack.db"
engine = create_engine(DATABASE_URL, echo=False)


def init_db():
    """Create database and tables."""
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
