from sqlalchemy import Column, Integer, ForeignKey, String
from models.component import Component
class Mobo(Component):
    __tablename__ = "mobo"

    id_component = Column(Integer, ForeignKey("component.id_component"), primary_key=True)
    form_factor = Column(String(20), nullable=False)
    socket = Column(String(10), nullable=False)
    chipset = Column(String(10), nullable=False)
    memory_type = Column(String(10), nullable=False)
    memory_slots = Column(Integer, nullable=False)
    pcie_slots = Column(Integer, nullable=False)

    __mapper_args__ = {
        "polimorphic_identity": "mobo"
    }

    def __repr__(self):
        return f"Mobo(id = {self.id_component}, manufacturer = {self.manufacturer}, model = {self.model}, form_factor = {self.form_factor}, socket = {self.socket}, chipset = {self.chipset}, memory_type = {self.memory_type}, memory_slots = {self.memory_slots}, pcie_slots = {self.pcie_slots})"
    
    def __str__(self):
        return f"{super().__str__()} - {self.form_factor} - {self.socket} - {self.chipset} - {self.memory_slots} slots {self.memory_type} - PCIE x{self.pcie_slots}"