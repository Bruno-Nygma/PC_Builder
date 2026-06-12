import datetime

import bcrypt
import jwt

from models.account import Account
from repository import account_repository
from persistence.db_config import get_session

SECRET_KEY = "some-weird-ass-string"

def register(data):

    for field in ["name", "surname", "email", "password"]:
        if field not in data or len(str(data[field]).strip()) == 0:
            raise ValueError(f"Field {field} is mandatory!")
        
    if len(data["password"]) < 8:
        raise ValueError("Password too short! Has to be minimum 8 characters")

    with get_session() as session:
        if account_repository.get_by_email(session, data["email"]) is not None:
            raise ValueError("Email already registered")
        
        password_hash = bcrypt.hashpw(
            data["password"].encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

        new_account = Account(
            name = data["name"],
            surname = data["surname"],
            email = data["email"],
            password = password_hash,
            role = data.get("role", "user")
        )

        return account_repository.create(session, new_account)
    
def login(data):
    
    if "email" not in data or "password" not in data:
        raise ValueError("Email and password are mandatory!")
    
    with get_session() as session:
        account = account_repository.get_by_email(session, data["email"])

        if account is None:
            raise ValueError("Credentials are incorrect")
        
        valid_password = bcrypt.checkpw(
            data["password"].encode("utf-8"), account.password.encode("utf-8")
        )

        if not valid_password:
            raise ValueError("Credentials are incorrect")
        
        payload = {
            "account_id": account.id_account,
            "email": account.email,
            "role": account.role,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm = "HS256")

        return token, account
    
def validate_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = ["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Expired token!")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token!")
