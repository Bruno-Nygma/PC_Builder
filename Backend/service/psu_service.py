from repository import component_repository
from models.psu import Psu

from persistence.db_config import get_session

#TODO controlli 


def get_filtered(build):
    with get_session() as session:
        required_wattage = 0
        if "cpu" in build:
            required_wattage += build["cpu"]["tdp"]
        if "gpu" in build:
            required_wattage += build["gpu"]["tdp"]
        required_wattage += required_wattage * 0.4
        psu_list = component_repository.get_by_type(session, Psu)
        for p in psu_list[:]:
            if p.wattage < required_wattage:
                psu_list.remove(p)
        return psu_list
            

def get_blueprint():
    return Psu.blueprint()
    
    
def create(data):
    with get_session() as session:
        psu = Psu(
            price = data["price"],
            manufacturer = data["manufacturer"],
            model = data["model"],
            wattage = data["wattage"]
        )
        return component_repository.create(session, psu)


def update(psu_id, data):
    with get_session() as session:

        psu = component_repository.get_by_id(session, psu_id).to_dict()


        for k,v in data.items():
            psu[k] = v

        psu = Psu(**psu)

        return component_repository.update(session, psu)