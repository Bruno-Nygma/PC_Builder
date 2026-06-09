from flask import Blueprint, jsonify, request

from persistence.db_config import get_session
from service import cpu_cooler_service

cpu_cooler_bp = Blueprint("cpu_cooler", __name__, url_prefix="/api/cpu_cooler")

@cpu_cooler_bp.route("/list", methods = ["GET"])
def get_all():
    session = get_session()
    cpu_cooler_list = cpu_cooler_service.get_all(session)
    return jsonify([c.to_dict() for c in cpu_cooler_list])

@cpu_cooler_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()
    session = get_session()

    try:
        new_cpu_cooler = cpu_cooler_service.create(session, data)
        return jsonify(new_cpu_cooler.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
