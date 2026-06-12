from sqlalchemy import Column, Integer, ForeignKey, String
from models.component import Component
class Memory(Component):
    __tablename__ = "memory"

    id_component = Column(Integer, ForeignKey("component.id_component"), primary_key=True)
    form_factor = Column(String(20), nullable=False)
    speed = Column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "memory"
    }

    def __repr__(self):
        return f"Memory(id = {self.id_component}, manufacturer = {self.manufacturer}, model = {self.model}, form_factor = {self.form_factor}, speed = {self.speed})"
    
    def __str__(self):
        return f"{super().__str__()} - {self.form_factor} - {self.speed}MHz"
    
    def to_dict(self):
        return  {
            "id_component": self.id_component,
            "type": self.type,
            "price": self.price,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "form_factor": self.form_factor,
            "speed": self.speed
        }