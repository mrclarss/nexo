from app.extensions import db
from app.models.team import Team
from app.schemas.team_schema import TeamSchema
from app.utils.response import success_response


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)


def listar_usuarios():
    teams = Team.query.all()
    return success_response(teams_schema.dump(teams))


def criar_usuario(data):
    dados_validados = team_schema.load(data)

    novo_team = Team(**dados_validados)

    db.session.add(novo_team)
    db.session.commit()