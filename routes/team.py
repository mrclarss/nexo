from flask import Blueprint, jsonify, request

from app.controllers.team_controller import (
    criar_equipe, 
    listar_equipe,
    atualizar_equipe,
    deletar_equipe
)


team_bp = Blueprint("teams", __name__)


@team_bp.route("/listar_equipe", methods=["GET"])
def get_team():
    response, status = listar_equipe()
    return jsonify(response), status


@team_bp.route("/criar_equipe", methods=["POST"])
def post_team():
    data = request.get_json()
    response, status = criar_equipe(data)
    return jsonify(response), status

@team_bp.route("/<int:id>/atualizar_equipe", methods=["PATCH"])
def patch_team(id):
    data = request.get_json()
    response, status = atualizar_equipe(id,data)
    return jsonify(response), status

@team_bp.route("/<int:id>/deletar_equipe", methods=["DELETE"])
def delete_team(id):
    response, status = deletar_equipe(id)
    return jsonify(response), status