from app.extensions import db
from app.models.participante import Participante
from app.schemas.participante_schema import ParticipanteSchema
from app.utils.response import success_response


participant_schema = ParticipanteSchema()
participants_schema = ParticipanteSchema(many=True)


def listar_participants():
    participants = Participante.query.all()
    return success_response(participants_schema.dump(participants))