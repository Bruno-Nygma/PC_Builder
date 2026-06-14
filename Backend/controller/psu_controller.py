from flask import Blueprint, jsonify, request

from service import psu_service

psu_bp = Blueprint("psu", __name__, url_prefix="/api/psu")

@psu_bp.route("/list", methods = ["POST"])
def get_filtered():
    build = request.get_json()

    psu_list = psu_service.get_filtered(build)
    return jsonify([p.to_dict() for p in psu_list])

@psu_bp.route("/blueprint", methods = ["GET"])
def get_blueprint():
    return psu_service.get_blueprint()

@psu_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()

    try:
        new_psu = psu_service.create(data)
        return jsonify(new_psu.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@psu_bp.route("/<int:component_id>", methods = ["PUT"])
def update(component_id):
    try:
        data = request.get_json()
        updated = psu_service.update(component_id, data)
        return jsonify(updated.to_dict())
    except Exception as e:
        return str(e)