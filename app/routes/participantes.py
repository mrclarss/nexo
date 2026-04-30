from flask import Blueprint, jsonify, request

from app.controllers.participants_controller import listar_participants, criar_participants


participants_bp = Blueprint("participants", __name__)


@participants_bp.route("/", methods=["GET"])
def get_():
    response, status = listar_participants()
    return jsonify(response), status

@participants_bp.route("/", methods=["POST"])
def post_participants():
    data = request.get_json()
    response, status = criar_participants(data)
    return jsonify(response), status