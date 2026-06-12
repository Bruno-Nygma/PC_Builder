from repository import component_repository
from models.gpu import Gpu

from persistence.db_config import get_session

#TODO controlli 


def get_all():
    with get_session() as session:
        return component_repository.get_by_type(session, Gpu)
    
def get_blueprint():
    return Gpu.blueprint()

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


def update(gpu_id, data):
    with get_session() as session:

        gpu = component_repository.get_by_id(session, gpu_id).to_dict()


        for k,v in data.items():
            gpu[k] = v

        gpu = Gpu(**gpu)
    
        return component_repository.update(session, gpu)