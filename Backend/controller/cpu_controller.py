from flask import Blueprint, jsonify, request

from service import cpu_service

cpu_bp = Blueprint("cpu", __name__, url_prefix="/api/cpu")

@cpu_bp.route("/list", methods = ["POST"])
def get_filtered():

    filters = {}
    build = request.get_json()
    if "mobo" in build:
        filters["socket"] = build["mobo"]["socket"]

    cpu_list = cpu_service.get_filtered(filters)
    return jsonify([c.to_dict() for c in cpu_list])

@cpu_bp.route("/blueprint", methods = ["GET"])
def get_blueprint():
    return jsonify(cpu_service.get_blueprint())

@cpu_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()

    try:
        new_cpu = cpu_service.create(data)
        return jsonify(new_cpu.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@cpu_bp.route("/<int:component_id>", methods = ["PUT"])
def update(component_id):
    try:
        data = request.get_json()
        updated = cpu_service.update(component_id, data)
        return jsonify(updated.to_dict())
    except Exception as e:
        return str(e)