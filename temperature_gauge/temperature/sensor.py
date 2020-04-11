import enum
import typing

class TemperatureUnit(enum.Enum):
    CELSIUS = 'C'
    KELVIN = 'K'
    FARENHEIT = 'F'

class TemperatureReading(typing.NamedTuple):
    timestamp: float
    value: float
    unit: TemperatureUnit
