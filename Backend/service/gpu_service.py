from repository import component_repository
from models.gpu import Gpu

#TODO controlli 


def get_all(session):
    return component_repository.get_by_type(session, Gpu)

def create(session, data):
    gpu = Gpu(
        price = data["price"],
        manufacturer = data["manufacturer"],
        model = data["model"],
        tdp = data["tdp"],
        vram = data["vram"]
    )
    return component_repository.create(session, gpu)

#TODO update