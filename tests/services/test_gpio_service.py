import pytest
from unittest.mock import MagicMock
from drivers.gpio_driver_interface import GPIODriverInterface
from services.gpio_service import GPIOService


class TestGPIOService:
    _PIN_X = 12
    _PIN_Y = 13
    
    @pytest.fixture
    def gpio_driver(self):
        return MagicMock(spec=GPIODriverInterface)

    @pytest.fixture
    def gpio_service(self, gpio_driver):
        return GPIOService(gpio_driver, pin_x=self._PIN_X, pin_y=self._PIN_Y)

    def test_move(self, gpio_service, gpio_driver):
        angles = (90, 45)

        gpio_service.move(angles)

        gpio_driver.set_servo_pulse_width.assert_any_call(self._PIN_X, 90)
        gpio_driver.set_servo_pulse_width.assert_any_call(self._PIN_Y, 45)

        assert gpio_driver.set_servo_pulse_width.call_count == 2
