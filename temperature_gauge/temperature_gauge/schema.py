import graphene

from temperature import schema as temperature_schema


class Query(temperature_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
