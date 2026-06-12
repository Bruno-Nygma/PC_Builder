from repository import component_repository
from models.storage import Storage

from persistence.db_config import get_session

#TODO controlli 


def get_all():
    with get_session() as session:
        return component_repository.get_by_type(session, Storage)
    
def get_blueprint():
    return Storage.blueprint()

def create(data):
    with get_session() as session:
        storage = Storage(
            price = data["price"],
            manufacturer = data["manufacturer"],
            model = data["model"],
            capacity = data["capacity"],
            storage_type = data["storage_type"]
        )
        return component_repository.create(session, storage)


def update(storage_id, data):
    with get_session() as session:

        storage = component_repository.get_by_id(session, storage_id).to_dict()


        for k,v in data.items():
            storage[k] = v

        storage = Storage(**storage)

        return component_repository.update(session, storage)