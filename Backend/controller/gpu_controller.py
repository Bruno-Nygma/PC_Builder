from flask import Blueprint, jsonify, request

from service import gpu_service

gpu_bp = Blueprint("gpu", __name__, url_prefix="/api/gpu")

@gpu_bp.route("/list", methods = ["GET"])
def get_all():
    gpu_list = gpu_service.get_all()
    return jsonify([g.to_dict() for g in gpu_list])

@gpu_bp.route("/new", methods = ["POST"])
def create():
    data = request.get_json()

    try:
        new_gpu = gpu_service.create(data)
        return jsonify(new_gpu.to_dict()), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
