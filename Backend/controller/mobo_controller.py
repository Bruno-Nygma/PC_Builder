from flask import Blueprint, jsonify, request

from service import mobo_service

mobo_bp = Blueprint("mobo", __name__, url_prefix="/api/mobo")

@mobo_bp.route("/list", methods = ["POST"])
def get_filtered():
    filters = {}
    build = request.get_json()

    if "cpu" in build:
        filters["socket"] = build["cpu"]["socket"]
    if "memory" in build:
        filters["memory_type"] = build["memory"]["form_factor"]

    #TODO filter by form factor

    mobo_list = mobo_service.get_filtered(filters)

    return jsonify([m.to_dict() for m in mobo_list])

@mobo_bp.route("/blueprint", methods = ["GET"])
def get_blueprint():
    return mobo_service.get_blueprint()

@mobo_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()

    try:
        new_mobo = mobo_service.create(data)
        return jsonify(new_mobo.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@mobo_bp.route("/<int:component_id>", methods = ["PUT"])
def update(component_id):
    try:
        data = request.get_json()
        updated = mobo_service.update(component_id, data)
        return jsonify(updated.to_dict())
    except Exception as e:
        return str(e)