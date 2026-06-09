from repository import component_repository
from models.tower_case import TowerCase

from persistence.db_config import get_session

#TODO controlli 


def get_all():
    with get_session() as session:
        return component_repository.get_by_type(session, TowerCase)

def create(data):
    with get_session() as session:
        case = TowerCase(
            price = data["price"],
            manufacturer = data["manufacturer"],
            model = data["model"],
            case_type = data["case_type"],
            max_video_card_length = data["max_video_card_length"]
        )
        return component_repository.create(session, case)


def update(case_id, data):
    with get_session() as session:

        case = component_repository.get_by_id(session, case_id).to_dict()


        for k,v in data.items():
            case[k] = v

        case = TowerCase(**case)

        return component_repository.update(session, case)