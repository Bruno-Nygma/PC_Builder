from repository import component_repository
from models.gpu import Gpu

from persistence.db_config import get_session

#TODO controlli 


def get_all():
    with get_session() as session:
        return component_repository.get_by_type(session, Gpu)

def create(data):
    with get_session() as session:
        gpu = Gpu(
            price = data["price"],
            manufacturer = data["manufacturer"],
            model = data["model"],
            tdp = data["tdp"],
            vram = data["vram"]
        )
        return component_repository.create(session, gpu)

#TODO update