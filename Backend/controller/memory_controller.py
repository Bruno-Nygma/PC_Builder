from flask import Blueprint, jsonify, request

from persistence.db_config import get_session
from service import memory_service

memory_bp = Blueprint("memory", __name__, url_prefix="/api/memory")

@memory_bp.route("/list", methods = ["GET"])
def get_all():
    session = get_session()
    memory_list = memory_service.get_all(session)
    return jsonify([m.to_dict() for m in memory_list])

@memory_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()
    session = get_session()

    try:
        new_memory = memory_service.create(session, data)
        return jsonify(new_memory.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
