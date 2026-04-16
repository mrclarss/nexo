from app.extensions import db
from app.models.team import Team
from app.schemas.team_schema import TeamSchema
from app.utils.response import success_response


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)


def listar_equipe():
    teams = Team.query.all()
    return success_response(teams_schema.dump(teams))


def criar_equipe(data):
    dados_validados = team_schema.load(data)

    novo_team = Team(**dados_validados)

    db.session.add(novo_team)
    db.session.commit()

    return success_response(team_schema.dump(novo_team),201)

def atualizar_equipe(id, data):
    equipe = Team.query.get_or_404(id)

    dados_validados = team_schema.load(data, partial=True)

    for campo, valor in dados_validados.items():
        setattr(equipe, campo, valor)

    db.session.commit()

    return success_response(team_schema.dump(equipe))

def deletar_equipe():
    equipe = Team.query.get_or_404(id)

    db.session.delete(equipe)
    db.session.commit()

    return "", 204