from sqlalchemy import Column, Integer, ForeignKey, String
from models.component import Component
class Storage(Component):
    __tablename__ = "storage"

    id_component = Column(Integer, ForeignKey("component.id_component"), primary_key=True)
    capacity = Column(String(10), nullable=False)
    storage_type = Column(String(10), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "storage"
    }

    def __repr__(self):
        return f"Storage(id = {self.id_component}, manufacturer = {self.manufacturer}, model = {self.model}, capacity = {self.capacity}, type = {self.type})"
    
    def __str__(self):
        return f"{super().__str__()} - {self.type} - {self.capacity}"
    
    def to_dict(self):
        return  {
            "id_component": self.id_component,
            "price": self.price,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "capacity": self.capacity,
            "storage_type": self.storage_type
        }