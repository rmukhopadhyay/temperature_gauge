import enum
import typing


class TemperatureUnit(enum.Enum):
    CELSIUS = 'C'
    KELVIN = 'K'
    FAHRENHEIT = 'F'


class TemperatureReading(typing.NamedTuple):
    timestamp: float
    value: float
    unit: TemperatureUnit


class TemperatureSensorInterface:

    def read_kelvin(self) -> TemperatureReading:
        raise NotImplementedError()

    def read_celsius(self) -> TemperatureReading:
        reading_k = self.read_kelvin()
        return TemperatureReading(
            timestamp=reading_k.timestamp,
            value=reading_k.value - 273.15,
            unit=TemperatureUnit.CELSIUS,
        )

    def read_fahrenheit(self) -> TemperatureReading:
        reading_k = self.read_kelvin()
        return TemperatureReading(
            timestamp=reading_k.timestamp,
            value=reading_k.value * 1.8 - 459.67,
            unit=TemperatureUnit.FAHRENHEIT,
        )
