from flask import Blueprint, jsonify, request

from service import storage_service

storage_bp = Blueprint("storage", __name__, url_prefix="/api/storage")

@storage_bp.route("/list", methods = ["POST"])
def get_all():
    storage_list = storage_service.get_all()
    return jsonify([s.to_dict() for s in storage_list])

@storage_bp.route("/blueprint", methods = ["GET"])
def get_blueprint():
    return storage_service.get_blueprint()

@storage_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()

    try:
        new_storage = storage_service.create(data)
        return jsonify(new_storage.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@storage_bp.route("/<int:component_id>", methods = ["PUT"])
def update(component_id):
    try:
        data = request.get_json()
        updated = storage_service.update(component_id, data)
        return jsonify(updated.to_dict())
    except Exception as e:
        return str(e)