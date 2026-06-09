from repository import component_repository
from models.cpu_cooler import CpuCooler

#TODO controlli 


def get_all(session):
    return component_repository.get_by_type(session, CpuCooler)

def create(session, data):
    cpu_cooler = CpuCooler(
        price = data["price"],
        manufacturer = data["manufacturer"],
        model = data["model"],
        fan_rpm = data["fan_rpm"],
        water_cooled = data["water_cooled"]
    )
    return component_repository.create(session, cpu_cooler)

#TODO update
    