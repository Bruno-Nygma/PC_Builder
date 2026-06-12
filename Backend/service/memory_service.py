from repository import component_repository
from models.memory import Memory

from persistence.db_config import get_session

#TODO controlli 


def get_all():
    with get_session() as session:
        return component_repository.get_by_type(session, Memory)
    
def get_blueprint():
    return Memory.blueprint()

def create(data):
    with get_session() as session:
        memory = Memory(
            price = data["price"],
            manufacturer = data["manufacturer"],
            model = data["model"],
            form_factor = data["form_factor"],
            speed = data["speed"]
        )
        return component_repository.create(session, memory)


def update(memory_id, data):
    with get_session() as session:

        mem = component_repository.get_by_id(session, memory_id).to_dict()


        for k,v in data.items():
            mem[k] = v

        mem = Memory(**mem)

        return component_repository.update(session, mem)