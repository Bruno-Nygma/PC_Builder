from sqlalchemy import select

from models.account import Account

def create(session, account):
    session.add(account)
    session.commit()
    session.refresh(account)
    return account

def get_by_id(session, user_id):
    return session.get(user_id)

def get_all(session):
    return session.execute(select(Account)).scalars().all()

def get_by_email(session, email):
    return session.execute(select(Account).filter_by(email = email)).scalars().first()