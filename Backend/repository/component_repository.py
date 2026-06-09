from sqlalchemy import select

from models.component import Component

#GET
def get_all(session):
    return session.execute(select(Component)).scalars().all()

def get_by_type(session, component_class):
    return session.execute(select(component_class)).scalars().all()

def get_by_attributes(session, component_class, filters): 
    return session.execute(select(component_class).filter_by(**filters)).scalars().all()

#CREATE
def create(session, component):
    session.add(component)
    session.commit()
    return component

#DELETE
def delete_by_id(session, component):
    session.delete(component)
    session.commit()

#PUT
def update(session, component):
    #component = session.merge(component)
    session.commit()
    #session.refresh(component)
    return component