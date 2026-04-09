from flask import Blueprint, jsonify, request

from app.controllers.team_controller import criar_equipe, listar_equipe


team_bp = Blueprint("teams", __name__)


@team_bp.route("/", methods=["GET"])
def get_team():
    response, status = listar_equipe()
    return jsonify(response), status


@team_bp.route("/", methods=["POST"])
def post_team():
    data = request.get_json()
    response, status = criar_equipe(data)
    return jsonify(response), status