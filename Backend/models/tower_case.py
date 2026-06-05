from sqlalchemy import Column, Integer, ForeignKey, String
from models.component import Component
from sqlalchemy.orm import relationship
from models.form_factor import compatible_with

class TowerCase(Component):
    __tablename__ = "tower_case"

    id_component = Column(Integer, ForeignKey("component.id_component"), primary_key=True)
    type = Column(String(20), nullable=False)
    max_video_card_length = Column(Integer, nullable=False)

    __mapper_args__ = {
        "polimorphic_identity": "tower_case"
    }

    form_factors = relationship("FormFactor", secondary=compatible_with, back_populates="tower_cases")

    def __repr__(self):
        return f"TowerCase(id = {self.id_component}, manufacturer = {self.manufacturer}, model = {self.model}, type = {self.type}, max_video_card_length = {self.max_video_card_length})"
    
    def __str__(self):
        return f"{super().__str__()} - {self.type} - max video card length: {self.max_video_card_length}"