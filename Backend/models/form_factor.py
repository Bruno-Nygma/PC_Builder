from sqlalchemy import Column, Integer, String, Table, ForeignKey
from persistence.db_config import Base
from sqlalchemy.orm import relationship

compatible_with = Table(
    "compatible_with",
    Base.metadata,
    Column("id_form_factor", Integer, ForeignKey("form_factor.id_form_factor"), primary_key=True),
    Column("id_component", Integer, ForeignKey("tower_case.id_component"), primary_key=True)
)

class FormFactor(Base):
    __tablename__ = "form_factor"

    id_form_factor = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(15), nullable=False)

    tower_cases = relationship("TowerCase", secondary= compatible_with, back_populates="form_factors")


    def __repr__(self):
        return f"FormFactor(id = {self.id_form_factor}, type = {self.type})"
    
    def __str__(self):
        return f"{self.type}"
    
    def to_dict(self):
        return {
            "id_form_factor": self.id_form_factor,
            "type": self.type
        }