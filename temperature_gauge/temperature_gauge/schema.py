import graphene

class Query(graphene.ObjectType):
    helloWorld = graphene.String()

    def resolve_helloWorld(self, info, **kwargs):
        return 'Hello world!'

schema = graphene.Schema(query=Query)
