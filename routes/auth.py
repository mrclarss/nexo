from flask import Blueprint, request, jsonify

# Criação do Blueprint para autenticação
auth_bp = Blueprint("auth", __name__)

from flask import Blueprint, request, jsonify

# Criação do Blueprint para autenticação
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Exemplo de validação simples
    if username == "admin" and password == "1234":
        return jsonify({"token": "seu_token_jwt"}), 200
    return jsonify({"error": "Credenciais inválidas"}), 401