from drivers.gpio_driver_interface import GPIODriverInterface
import pigpio
import logging

logger = logging.getLogger("GPIODriver")

class GPIODriver(GPIODriverInterface):
    _MIN_PULSE_WIDTH = 500
    _MAX_PULSE_WIDTH = 2500

    def set_servo_pulse_width(self, pin, position):
        logger.debug("Set position %s on pin %s", position, pin)

        pulse_width = self._MIN_PULSE_WIDTH + ((position / 180.0) * (self._MAX_PULSE_WIDTH - self._MIN_PULSE_WIDTH))

        pi = pigpio.pi()
        pi.set_servo_pulsewidth(pin, pulse_width)
        pi.stop()

