from drivers.gpio_driver_interface import GPIODriverInterface
import pigpio
import logging

logger = logging.getLogger("GPIODriver")

class GPIODriver(GPIODriverInterface):
    """Implements the GPIO driver interface for controlling servo motors."""

    _MIN_PULSE_WIDTH = 500  # Minimum pulse width in microseconds
    _MAX_PULSE_WIDTH = 2500  # Maximum pulse width in microseconds

    def set_servo_pulse_width(self, pin: int, position: float) -> None:
        """Sets the servo pulse width for a given pin and position."""
        logger.debug("Set position %s on pin %s", position, pin)

        pulse_width = self._MIN_PULSE_WIDTH + ((position / 180.0) * (self._MAX_PULSE_WIDTH - self._MIN_PULSE_WIDTH))

        pi = pigpio.pi()  # Connect to pigpio daemon
        pi.set_servo_pulsewidth(pin, pulse_width)  # Set the pulse width for the servo
        pi.stop()  # Disconnect from pigpio daemon
