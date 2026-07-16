from flask import Blueprint, jsonify, request

from app.controllers.participants_controller import listar_participants


participants_bp = Blueprint("participants", __name__)


@participants_bp.route("/listar_participants", methods=["GET"])
def get_():
    response, status = listar_participants()
    return jsonify(response), status

