from drivers.gpio_driver_interface import GPIODriverInterface


class GPIODriver(GPIODriverInterface):
    def __init__(self, pin):
        self._pin = pin

    def set_servo_pulse_width(self, pin, width):

