from repository import component_repository
from models.cpu_cooler import CpuCooler

from persistence.db_config import get_session

#TODO controlli 


def get_all():
    with get_session() as session:
        return component_repository.get_by_type(session, CpuCooler)

def create(data):
    with get_session() as session:
        cpu_cooler = CpuCooler(
            price = data["price"],
            manufacturer = data["manufacturer"],
            model = data["model"],
            fan_rpm = data["fan_rpm"],
            water_cooled = data["water_cooled"]
        )
        return component_repository.create(session, cpu_cooler)

#TODO update
    