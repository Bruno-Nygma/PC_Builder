from repository import component_repository
from models.cpu import Cpu

from persistence.db_config import get_session

#TODO controlli 


def get_all():
    with get_session() as session:
        return component_repository.get_by_type(session, Cpu)

def create(data):
    with get_session() as session:
        cpu = Cpu(
            price = data["price"],
            manufacturer = data["manufacturer"],
            model = data["model"],
            clock = data["clock"],
            integrated_graphics = data["integrated_graphics"],
            tdp = data["tdp"],
            socket = data["socket"]
        )
        return component_repository.create(session, cpu)

def update(cpu_id, data):
    with get_session() as session:

        cpu = component_repository.get_by_id(session, cpu_id).to_dict()


        for k,v in data.items():
            cpu[k] = v

        cpu = Cpu(**cpu)
    
        return component_repository.update(session, cpu)