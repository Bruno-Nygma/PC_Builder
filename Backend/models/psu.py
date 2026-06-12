from sqlalchemy import Column, Integer, ForeignKey
from models.component import Component
class Psu(Component):
    __tablename__ = "psu"

    id_component = Column(Integer, ForeignKey("component.id_component"), primary_key=True)
    wattage = Column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "psu"
    }

    def __repr__(self):
        return f"Psu(id = {self.id_component}, manufacturer = {self.manufacturer}, model = {self.model}, wattage = {self.wattage})"
    
    def __str__(self):
        return f"{super().__str__()} - {self.wattage}W"
    
    def to_dict(self):
        return {
            "id_component": self.id_component,
            "type": self.type,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "price": self.price,
            "wattage": self.wattage
        }
    
    def blueprint():
        return ["manufacturer", "model", "wattage", "price"]