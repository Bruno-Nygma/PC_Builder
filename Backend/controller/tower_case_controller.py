from flask import Blueprint, jsonify, request

from service import tower_case_service

tower_case_bp = Blueprint("tower_case", __name__, url_prefix="/api/tower_case")

@tower_case_bp.route("/list", methods = ["POST"])
def get_all():
    build = request.get_json()
    if "mobo" in build:
        form_factor = build["mobo"]["form_factor"]
    else:
        form_factor = False
    case_list = tower_case_service.get_filtered(form_factor)
    return jsonify([c.to_dict() for c in case_list])

@tower_case_bp.route("/blueprint", methods = ["GET"])
def get_blueprint():
    return tower_case_service.get_blueprint()

@tower_case_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()

    try:
        new_case = tower_case_service.create(data)
        return jsonify(new_case.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@tower_case_bp.route("/<int:component_id>", methods = ["PUT"])
def update(component_id):
    try:
        data = request.get_json()
        updated = tower_case_service.update(component_id, data)
        return jsonify(updated.to_dict())
    except Exception as e:
        return str(e)