from sqlalchemy import Column, Integer, ForeignKey
from models.component import Component
class Gpu(Component):
    __tablename__ = "gpu"

    id_component = Column(Integer, ForeignKey("component.id_component"), primary_key=True)
    tdp = Column(Integer, nullable=False)
    VRAM = Column(Integer, nullable=False)

    __mapper_args__ = {
        "polimorphic_identity": "gpu"
    }

    def __repr__(self):
        return f"Gpu(id = {self.id_component}, manufacturer = {self.manufacturer}, model = {self.model}, tdp = {self.tdp}, vram = {self.VRAM})"
    
    def __str__(self):
        return f"{super().__str__()} - {self.tdp}W - {self.VRAM}MB"