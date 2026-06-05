from sqlalchemy import Column, Integer, String
from persistence.db_config import Base
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__ = "account"

    id_account = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable = False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    role = Column(String(20), nullable=False, default="user")

    builds = relationship("Build", back_populates="accounts")

    def __repr__(self):
        return f"Account(id = {self.id_account}, name = {self.name}, surname = {self.surname}, email = {self.email}, role = {self.role})"

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.email}"
