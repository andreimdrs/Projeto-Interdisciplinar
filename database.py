from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
import os


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
