from sqlalchemy import Column, Integer, ForeignKey, Numeric, Table
from persistence.db_config import Base
from sqlalchemy.orm import relationship

includes = Table(
    "includes",
    Base.metadata,
    Column("id_build", Integer, ForeignKey("build.id_build"), primary_key=True),
    Column("id_component", Integer, ForeignKey("component.id_component"), primary_key=True),
    Column("number", Integer, nullable=False)
)

class Build(Base):
    __tablename__ = "build"

    id_build = Column(Integer, autoincrement=True, primary_key=True)
    id_account = Column(Integer, ForeignKey("account.id_account"))
    price = Column(Numeric(7, 2), nullable=False)

    accounts = relationship("Account", back_populates="builds")
    components = relationship("Component", secondary=includes, back_populates="builds")

    def __repr__(self):
        return f"Build(id = {self.id_build}, id_account = {self.id_account}, price = {self.price})"
    
    def __str__(self):
        return f"{self.price}"