import graphene

from temperature import schema as temperature_schema


class Query(temperature_schema.Query, graphene.ObjectType):
    helloWorld = graphene.String()

    def resolve_helloWorld(self, info, **kwargs):
        return 'Hello world!'


schema = graphene.Schema(query=Query)
