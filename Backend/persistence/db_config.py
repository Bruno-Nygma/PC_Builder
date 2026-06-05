from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine("postgresql://postgres:admin@localhost/PC_builder", echo=True)

SessionLocal = sessionmaker(bind=engine)

def init_db():

    print("[LOG] - Creazione Database")

    # Base.metadata.drop_all(bind=engine) # Didattico
    # Base.metadata.create_all(bind=engine)

def get_session():
    return SessionLocal()