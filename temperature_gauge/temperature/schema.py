import graphene

from temperature import sensor


TemperatureUnitGQL = graphene.Enum.from_enum(sensor.TemperatureUnit)


class TemperatureReadingGQLType(graphene.ObjectType):

    timestamp = graphene.Float()
    value = graphene.Float()
    unit = TemperatureUnitGQL()


class Query(graphene.ObjectType):

    currentTemperature = graphene.Field(TemperatureReadingGQLType)

    def resolve_currentTemperature(self, info, **kwargs):
        return sensor.TemperatureReading(0, 0, sensor.TemperatureUnit.KELVIN)
