from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from models.component import Component
class Cpu(Component):
    __tablename__ = "cpu"

    id_component = Column(Integer, ForeignKey("component.id_component"), primary_key=True)
    clock = Column(String(20), nullable=False)
    integrated_graphics = Column(Boolean, nullable=False)
    tdp = Column(Integer, nullable=False)
    socket = Column(String(50), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "cpu"
    }

    def __repr__(self):
        return f"Cpu(id = {self.id_component}, manufacturer = {self.manufacturer}, model = {self.model}, clock = {self.clock}, integrated_graphics = {self.integrated_graphics}, tdp = {self.tdp}, socket = {self.socket})"
    
    def __str__(self):
        return f"{super().__str__()} - {self.clock}GHz - {self.tdp}W - socket:{self.socket}"
    
    def to_dict(self):
        return {
            "id_component": self.id_component,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "price": self.price,
            "clock": self.clock,
            "integrated_graphics": self.integrated_graphics,
            "tdp": self.tdp,
            "socket": self.socket
        }