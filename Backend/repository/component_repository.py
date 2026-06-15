from sqlalchemy import select

from models.component import Component
from models.tower_case import TowerCase
from models.form_factor import FormFactor

#GET
def get_all(session):
    return session.execute(select(Component)).scalars().all()

def get_by_id(session, component_id):
    return session.get(Component, component_id)

def get_by_type(session, component_class):
    return session.execute(select(component_class)).scalars().all()

def get_by_attributes(session, component_class, filters): 
    return session.execute(select(component_class).filter_by(**filters)).scalars().all()

def get_case_by_form_factor(session, form_factor):
    return session.execute(select(TowerCase).join(TowerCase.form_factors).where(FormFactor.form_factor_type == form_factor)).scalars().all()

#CREATE
def create(session, component):
    session.add(component)
    session.commit()
    session.refresh(component)
    return component

#DELETE
def delete_by_id(session, component):
    session.delete(component)
    session.commit()

#PUT
def update(session, component):
    component = session.merge(component)
    session.commit()
    session.refresh(component)
    return component