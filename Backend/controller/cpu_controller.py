from flask import Blueprint, jsonify, request

from service import cpu_service

cpu_bp = Blueprint("cpu", __name__, url_prefix="/api/cpu")

@cpu_bp.route("/list", methods = ["GET"])
def get_all():
    cpu_list = cpu_service.get_all()
    return jsonify([c.to_dict() for c in cpu_list])

@cpu_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()

    try:
        new_cpu = cpu_service.create(data)
        return jsonify(new_cpu.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
