from sqlalchemy import select

from models.build import Build
from models.component import Component

def get_by_user(session, user_id):
    return session.execute(select(Build).where(Build.id_account == user_id)).scalars().all()

def get_by_id(session, build_id):
    return session.execute(select(Component).join(Component.builds).where(Build.id_build == build_id)).scalars().all()

def create(session, build):
    session.add(build)
    session.commit()
    session.refresh(build)
    return build