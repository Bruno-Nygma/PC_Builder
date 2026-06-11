from functools import wraps

from flask import Blueprint, g, jsonify, request

from repository import account_repository
from service import auth_service
from persistence.db_config import get_session

auth_bp = Blueprint("auth", __name__, url_prefix = "/api/auth")

@auth_bp.route("/register", methods = ["POST"])
def register():
    data = request.get_json()
    
    try:
        new_account = auth_service.register(data)
        return jsonify(new_account.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@auth_bp.route("/login", methods = ["POST"])
def login():
    data = request.get_json()

    try:
        token, account = auth_service.login(data)
        return jsonify({"token": token, "account": account.to_dict()})
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
    
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            parts = request.headers["Authorization"].split(" ")
            if len(parts) == 2 and parts[0] == "Bearer":
                token = parts[1]

        if token is None:
            return jsonify({"error": "Missing token!"}), 401
        
        try:
            payload = auth_service.validate_token(token)

            g.account_id = payload["account_id"]
            g.account_email = payload["email"]
            g.account_role = payload["role"]
        except ValueError as e:
            return jsonify({"error": str(e)}), 401
        
        return f(*args, **kwargs)
    return decorated

def role_required(*permitted_roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if g.account_role not in permitted_roles:
                return jsonify({"error": "Access denied! Role is not authorized."}), 403
            
            return f(*args, **kwargs)
        
        return decorated
    
    return decorator

@auth_bp.route("/me")
@token_required
@role_required("admin", "user")
def me():
    with get_session() as session:
        account = account_repository.get_by_id(session, g.account_id)
        return jsonify(account.to_dict())
    
@auth_bp.route("/users")
@token_required
@role_required("admin")
def get_all_accounts():
    with get_session() as session:
        accounts = account_repository.get_all(session)
        return jsonify([a.to_dict() for a in accounts])
        