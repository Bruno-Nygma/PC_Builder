from repository import component_repository
from models.memory import Memory

#TODO controlli 


def get_all(session):
    return component_repository.get_by_type(session, Memory)

def create(session, data):
    memory = Memory(
        price = data["price"],
        manufacturer = data["manufacturer"],
        model = data["model"],
        form_factor = data["form_factor"],
        speed = data["speed"]
    )
    return component_repository.create(session, memory)

#TODO update
    