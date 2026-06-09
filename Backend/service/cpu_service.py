from repository import component_repository
from models.cpu import Cpu

#TODO controlli 


def get_all(session):
    return component_repository.get_by_type(session, Cpu)

def create(session, data):
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

#TODO update