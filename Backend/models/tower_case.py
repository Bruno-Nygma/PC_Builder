from sqlalchemy import Column, Integer, ForeignKey, String
from models.component import Component
from sqlalchemy.orm import relationship
from models.form_factor import compatible_with

class TowerCase(Component):
    __tablename__ = "tower_case"

    id_component = Column(Integer, ForeignKey("component.id_component"), primary_key=True)
    case_type = Column(String(20), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "tower_case"
    }

    form_factors = relationship("FormFactor", secondary=compatible_with, back_populates="tower_cases")

    def __repr__(self):
        return f"TowerCase(id = {self.id_component}, manufacturer = {self.manufacturer}, model = {self.model}, type = {self.type})"
    
    def __str__(self):
        return f"{super().__str__()} - {self.type}"
    
    def to_dict(self):
        return {
            "id_component": self.id_component,
            "type": self.type,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "price": self.price,
            "case_type": self.case_type
        }
    
    def blueprint():
        return ["manufacturer", "model", "case_type", "price"]