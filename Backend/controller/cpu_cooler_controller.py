from flask import Blueprint, jsonify, request

from service import cpu_cooler_service

cpu_cooler_bp = Blueprint("cpu_cooler", __name__, url_prefix="/api/cpu_cooler")

@cpu_cooler_bp.route("/list", methods = ["GET"])
def get_all():
    cpu_cooler_list = cpu_cooler_service.get_all()
    return jsonify([c.to_dict() for c in cpu_cooler_list])

@cpu_cooler_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()

    try:
        new_cpu_cooler = cpu_cooler_service.create(data)
        return jsonify(new_cpu_cooler.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@cpu_cooler_bp.route("/<int:component_id>", methods = ["PUT"])
def update(component_id):
    try:
        data = request.get_json()
        updated = cpu_cooler_service.update(component_id, data)
        return jsonify(updated.to_dict())
    except Exception as e:
        return str(e)
