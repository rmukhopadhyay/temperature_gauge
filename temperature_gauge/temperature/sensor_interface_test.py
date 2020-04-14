import math
import time

from temperature import sensor_interface


class MockTemperatureSensor(sensor_interface.TemperatureSensorInterface):
    """Test implementation of TemperatureSensorInterface to test conversion functions

    returns a constant value supplied at construction
    """

    def __init__(self, timestamp: float, temperature_k: float):
        self.timestamp = timestamp
        self.temperature_k = temperature_k

    def read_kelvin(self) -> sensor_interface.TemperatureReading:
        return sensor_interface.TemperatureReading(
            timestamp=self.timestamp,
            value=self.temperature_k,
            unit=sensor_interface.TemperatureUnit.KELVIN,
        )


def assert_nearly_equal(
        t1: sensor_interface.TemperatureReading,
        t2: sensor_interface.TemperatureReading,
        desired_accuracy: float = .0001):
    assert t1.unit == t2.unit
    assert t1.timestamp == t2.timestamp
    assert math.fabs(t1.value - t2.value) <= desired_accuracy


class TestTemperatureConversions:
    timestamp = time.time()
    sensor_absolute_zero = MockTemperatureSensor(timestamp, 0.0)
    sensor_freezing_point_h2o = MockTemperatureSensor(timestamp, 273.15)

    def test_read_default_abs_0(self):
        t = self.sensor_absolute_zero.read()
        expected_t = sensor_interface.TemperatureReading(
            timestamp=self.timestamp,
            value=0.0,
            unit=sensor_interface.TemperatureUnit.KELVIN,
        )
        assert_nearly_equal(expected_t, t)

    def test_read_default_freezing(self):
        t = self.sensor_freezing_point_h2o.read()
        expected_t = sensor_interface.TemperatureReading(
            timestamp=self.timestamp,
            value=273.15,
            unit=sensor_interface.TemperatureUnit.KELVIN,
        )
        assert_nearly_equal(expected_t, t)

    def test_read_kelvin_abs_0(self):
        t = self.sensor_absolute_zero.read(unit=sensor_interface.TemperatureUnit.KELVIN)
        expected_t = sensor_interface.TemperatureReading(
            timestamp=self.timestamp,
            value=0.0,
            unit=sensor_interface.TemperatureUnit.KELVIN,
        )
        assert_nearly_equal(expected_t, t)
        t = self.sensor_absolute_zero.read_kelvin()
        assert_nearly_equal(expected_t, t)

    def test_read_kelvin_freezing(self):
        t = self.sensor_freezing_point_h2o.read(unit=sensor_interface.TemperatureUnit.KELVIN)
        expected_t = sensor_interface.TemperatureReading(
            timestamp=self.timestamp,
            value=273.15,
            unit=sensor_interface.TemperatureUnit.KELVIN,
        )
        assert_nearly_equal(expected_t, t)
        t = self.sensor_freezing_point_h2o.read_kelvin()
        assert_nearly_equal(expected_t, t)

    def test_read_celsius_abs_0(self):
        t = self.sensor_absolute_zero.read(unit=sensor_interface.TemperatureUnit.CELSIUS)
        expected_t = sensor_interface.TemperatureReading(
            timestamp=self.timestamp,
            value=-273.15,
            unit=sensor_interface.TemperatureUnit.CELSIUS,
        )
        assert_nearly_equal(expected_t, t)
        t = self.sensor_absolute_zero.read_celsius()
        assert_nearly_equal(expected_t, t)

    def test_read_celsius_freezing(self):
        t = self.sensor_freezing_point_h2o.read(unit=sensor_interface.TemperatureUnit.CELSIUS)
        expected_t = sensor_interface.TemperatureReading(
            timestamp=self.timestamp,
            value=0,
            unit=sensor_interface.TemperatureUnit.CELSIUS,
        )
        assert_nearly_equal(expected_t, t)
        t = self.sensor_freezing_point_h2o.read_celsius()
        assert_nearly_equal(expected_t, t)

    def test_read_fahrenheit_abs_0(self):
        t = self.sensor_absolute_zero.read(unit=sensor_interface.TemperatureUnit.FAHRENHEIT)
        expected_t = sensor_interface.TemperatureReading(
            timestamp=self.timestamp,
            value=-459.67,
            unit=sensor_interface.TemperatureUnit.FAHRENHEIT,
        )
        assert_nearly_equal(expected_t, t)
        t = self.sensor_absolute_zero.read_fahrenheit()
        assert_nearly_equal(expected_t, t)

    def test_read_fahrenheit_freezing(self):
        t = self.sensor_freezing_point_h2o.read(unit=sensor_interface.TemperatureUnit.FAHRENHEIT)
        expected_t = sensor_interface.TemperatureReading(
            timestamp=self.timestamp,
            value=32.0,
            unit=sensor_interface.TemperatureUnit.FAHRENHEIT,
        )
        assert_nearly_equal(expected_t, t)
        t = self.sensor_freezing_point_h2o.read_fahrenheit()
        assert_nearly_equal(expected_t, t)
