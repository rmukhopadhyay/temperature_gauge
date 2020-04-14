import graphene

from temperature import schema as temperature_schema


class Query(temperature_schema.Query):
    pass


class Subscription(temperature_schema.Subscription):
    pass


schema = graphene.Schema(query=Query, subscription=Subscription)
