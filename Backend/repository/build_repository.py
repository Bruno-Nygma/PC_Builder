from sqlalchemy import select

from models.build import Build

def get_by_user(session, user):
    return session.execute(select(Build).where(id_account = user)).scalars().all()

def create(session, build):
    session.add(build)
    session.commit()
    session.refresh(build)
    return build