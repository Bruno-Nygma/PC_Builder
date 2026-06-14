from flask import Blueprint, jsonify, request

from service import memory_service

memory_bp = Blueprint("memory", __name__, url_prefix="/api/memory")

@memory_bp.route("/list", methods = ["POST"])
def get_filters():
    filters = {}
    build = request.get_json()

    if "mobo" in build:
        filters["form_factor"] = build["mobo"]["memory_type"]

    memory_list = memory_service.get_filtered(filters)
    return jsonify([m.to_dict() for m in memory_list])

@memory_bp.route("/blueprint", methods = ["GET"])
def get_blueprint():
    return memory_service.get_blueprint()

@memory_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()

    try:
        new_memory = memory_service.create(data)
        return jsonify(new_memory.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@memory_bp.route("/<int:component_id>", methods = ["PUT"])
def update(component_id):
    try:
        data = request.get_json()
        updated = memory_service.update(component_id, data)
        return jsonify(updated.to_dict())
    except Exception as e:
        return str(e)