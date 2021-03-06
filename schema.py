import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Incident as IncidentModel

class Incident(SQLAlchemyObjectType):
    class Meta:
        model = IncidentModel
        interfaces = (relay.Node, )

class IncidentConnection(relay.Connection):
    class Meta:
        node = Incident

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    incidents = SQLAlchemyConnectionField(IncidentConnection)

schema = graphene.Schema(query=Query)

