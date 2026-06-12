from sqlalchemy import Column, Integer, ForeignKey, Boolean
from models.component import Component
class CpuCooler(Component):
    __tablename__ = "cpu_cooler"

    id_component = Column(Integer, ForeignKey("component.id_component"), primary_key=True)
    fan_rpm = Column(Integer, nullable=False)
    water_cooled = Column(Boolean, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "cpu_cooler"
    }

    def __repr__(self):
        return f"Cpu_cooler(id = {self.id_component}, price = {self.price}, manufacturer = {self.manufacturer}, model = {self.model}, fan_rpm = {self.fan_rpm}, water_cooled = {self.water_cooled})"

    def __str__(self):
        return f"{super().__str__()} - {self.fan_rpm} - {self.water_cooled}"
    
    def to_dict(self):
        return {
            "id_component": self.id_component,
            "type": self.type,
            "manufacturer": self.manufacturer,
            "price": self.price,
            "model": self.model,
            "fan_rpm": self.fan_rpm,
            "water_cooled": self.water_cooled
        }
    
    def blueprint():
        return ["manufacturer", "model", "fan_rpm", "water_cooled", "price"]