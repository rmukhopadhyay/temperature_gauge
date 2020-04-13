import graphene
import graphql
import rx

from temperature import random_sensor
from temperature import sensor_interface

temperature_sensor = random_sensor.RandomTemperatureSensor()

TemperatureUnitGQL = graphene.Enum.from_enum(sensor_interface.TemperatureUnit)


class TemperatureReadingGQLType(graphene.ObjectType):

    timestamp = graphene.Float()
    value = graphene.Float()
    unit = TemperatureUnitGQL()


class Query(graphene.ObjectType):

    current_temperature = graphene.Field(TemperatureReadingGQLType, unit=TemperatureUnitGQL())

    def resolve_current_temperature(
            self, info, unit=TemperatureUnitGQL.KELVIN.value, **kwargs) -> sensor_interface.TemperatureReading:
        # Instead of passing an enum, the framework passes an enum value
        try:
            unit_enum = sensor_interface.TemperatureUnit(unit)
        except ValueError as e:
            raise graphql.GraphQLError(f'Unsupported temperature unit: {e}')

        return temperature_sensor.read(unit_enum)


class Subscription(graphene.ObjectType):
    current_temperature_subscribe = graphene.Field(TemperatureReadingGQLType, unit=TemperatureUnitGQL())

    def resolve_current_temperature_subscribe(
            self, info, unit=TemperatureUnitGQL.KELVIN.value, **kwargs) -> rx.Observable:
        # Instead of passing an enum, the framework passes an enum value
        try:
            unit_enum = sensor_interface.TemperatureUnit(unit)
        except ValueError as e:
            raise graphql.GraphQLError(f'Unsupported temperature unit: {e}')

        return rx.Observable.interval(1000).map(lambda i: temperature_sensor.read(unit_enum))
