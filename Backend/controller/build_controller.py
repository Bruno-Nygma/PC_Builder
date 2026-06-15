from flask import Blueprint, jsonify, request
from service import build_service
from controller.auth_controller import token_required, me

build_bp = Blueprint("build", __name__, url_prefix="/api/build")

@build_bp.route('/publish', methods = ['POST'])
@token_required
def publish():
    build = request.get_json()
    return jsonify(build_service.create(build).to_dict())

@build_bp.route('/list', methods = ['GET'])
@token_required
def get_list():
    # builds_list = build_service.get_by_user()
    # result = []
    # for build in builds_list:
    #     list = []
    #     for comp in build:
    #         list.append(comp.to_dict())
    #     result.append(list)
    data = build_service.get_by_user()

    return jsonify(data)