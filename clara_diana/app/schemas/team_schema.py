from marshmallow import fields, validate

from app.extensions import ma
from app.models.user import Team


class TeamSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Team

    id = ma.auto_field(dump_only=True)
    nome = ma.auto_field(required=True)