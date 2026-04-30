from app.extensions import db
from app.models.participante import Participante
from app.schemas.participante_schema import ParticipanteSchema
from app.utils.response import success_response


participant_schema = ParticipanteSchema()
participants_schema = ParticipanteSchema(many=True)


def listar_participants():
    participants = Participante.query.all()
    return success_response(participants_schema.dump(participants))

def criar_participants(data):
    dados_validados = participant_schema.load(data)

    novo_participante = Participante(**dados_validados)

    db.session.add(novo_participante)
    db.session.commit()

    return success_response(participant_schema.dump(novo_participante), 201)