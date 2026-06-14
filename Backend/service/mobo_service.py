from repository import component_repository
from models.mobo import Mobo

from persistence.db_config import get_session

#TODO controlli 


def get_filtered(filters):
    with get_session() as session:
        return component_repository.get_by_attributes(session, Mobo, filters)
    
def get_blueprint():
    return Mobo.blueprint()

def create(data):
    with get_session() as session:
        mobo = Mobo(
            price = data["price"],
            manufacturer = data["manufacturer"],
            model = data["model"],
            form_factor = data["form_factor"],
            socket = data["socket"],
            chipset = data["chipset"],
            memory_type = data["memory_type"],
            memory_slots = data["memory_slots"],
            pcie_slots = data["pcie_slots"]
        )
        return component_repository.create(session, mobo)


def update(mobo_id, data):
    with get_session() as session:

        mobo = component_repository.get_by_id(session, mobo_id).to_dict()


        for k,v in data.items():
            mobo[k] = v

        mobo = Mobo(**mobo)

        return component_repository.update(session, mobo)