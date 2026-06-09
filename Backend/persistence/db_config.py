from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine("postgresql://postgres:admin@localhost/PC_builder", echo=True)

SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()