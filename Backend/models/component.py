from sqlalchemy import Column, Integer, Numeric, String
from persistence.db_config import Base
from sqlalchemy.orm import relationship
from models.build import includes

class Component(Base):
    __tablename__ = "component"

    id_component = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Numeric(6, 2), nullable=False)
    type = Column(String(20), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)

    #maybe __mapped_args__

    __mapper_args__ = {
        "polymorphic_identity": "component",
        "polymorphic_on": type
    }

    builds = relationship("Build", secondary=includes, back_populates="components")

    def __repr__(self):
        return f"Component(id = {self.id_component}, type = {self.type}, price = {self.price}, manufacturer = {self.manufacturer}, model = {self.model})"
    
    def __str__(self):
        return f"{self.type} - {self.price} - {self.manufacturer} - {self.model}"
