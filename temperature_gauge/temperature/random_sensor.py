import random
import time

from temperature import sensor_interface


class RandomTemperatureSensor(sensor_interface.TemperatureSensorInterface):
    """Implements a mock temperature sensor with pseudo-random values.

    Values will range from 0 K to 10,000 K.
    """

    MAX_TEMP_K = 10000.0

    def __init__(self):
        random.seed()

    def read_kelvin(self) -> sensor_interface.TemperatureReading:
        temperature_k = random.uniform(0.0, self.MAX_TEMP_K)
        return sensor_interface.TemperatureReading(
            timestamp=time.time(),
            value=temperature_k,
            unit=sensor_interface.TemperatureUnit.KELVIN,
        )
