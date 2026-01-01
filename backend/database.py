from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./career.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    query = Column(String)
    response = Column(String)


Base.metadata.create_all(bind=engine)
