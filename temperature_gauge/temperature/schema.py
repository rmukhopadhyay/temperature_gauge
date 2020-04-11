import graphene
import graphql

from temperature import random_sensor
from temperature import sensor_interface

temperature_sensor = random_sensor.RandomTemperatureSensor()

TemperatureUnitGQL = graphene.Enum.from_enum(sensor_interface.TemperatureUnit)


class TemperatureReadingGQLType(graphene.ObjectType):

    timestamp = graphene.Float()
    value = graphene.Float()
    unit = TemperatureUnitGQL()


class Query(graphene.ObjectType):

    currentTemperature = graphene.Field(
        TemperatureReadingGQLType, unit=TemperatureUnitGQL())

    def resolve_currentTemperature(self, info, unit=TemperatureUnitGQL.KELVIN.value, **kwargs):
        # TODO (Rishi): Figure out why we are being sent the enum value instead of the enum
        if unit == TemperatureUnitGQL.KELVIN.value:
            return temperature_sensor.read_kelvin()
        elif unit == TemperatureUnitGQL.CELSIUS.value:
            return temperature_sensor.read_celsius()
        elif unit == TemperatureUnitGQL.FARENHEIT.value:
            return temperature_sensor.read_farenheit()
        else:
            raise graphql.GraphQLError('Unsupported temperature unit')
