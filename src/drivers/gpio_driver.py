from drivers.gpio_driver_interface import GPIODriverInterface
import pigpio
import logging

logger = logging.getLogger("GPIODriver")

class GPIODriver(GPIODriverInterface):
    def __init__(self, pin):
        self._pin = pin

    def set_servo_pulse_width(self, width):
        logger.debug(f"Set pulse width {width} on pin {self._pin}")
        pi = pigpio.pi()
        pi.set_servo_pulsewidth(self._pin, width)
        pi.stop()

