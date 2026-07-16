from flask import Flask
from app.routes.auth import auth_bp  # Certifique-se de que este import está correto

def create_app():
    app = Flask(__name__)

    # Registre o Blueprint de auth
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app