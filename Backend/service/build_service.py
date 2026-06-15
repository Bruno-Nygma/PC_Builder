from repository import build_repository, account_repository, component_repository
from flask import g
from models.build import Build

from persistence.db_config import get_session

def create(data):
    with get_session() as session:
        account = account_repository.get_by_id(session, g.account_id).to_dict()
        price = 0
        for component in data:
            if data[component]['price']:
                price += float(data[component]['price'])
        build = Build(
            id_account = account['id_account'],
            price = price
        )
        for component in data:
            if data[component]['id_component']:
                new_component = component_repository.get_by_id(session, data[component]['id_component'])
                build.components.append(new_component)
        return build_repository.create(session, build)

def get_by_user():
    with get_session() as session:
        account = account_repository.get_by_id(session, g.account_id).to_dict()
        raw_builds = build_repository.get_by_user(session, account['id_account'])
        final_result = []    
        for build in raw_builds:
            components = build_repository.get_by_id(session,build.id_build)

            serialized_components = [comp.to_dict() for comp in components]

            final_result.append(serialized_components)
        return final_result