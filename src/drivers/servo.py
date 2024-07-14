import pigpio
import logging

logger = logging.getLogger("Servo")

class Servo:
    _pin: int

    def __init__(self, pin) -> None:
        logger.debug(f"Initialize on pin {pin}")
        self._pin = pin

    def set_servo_pulsewidth(self, pulse_width) -> None:
        logger.debug(f"Set pulse width {pulse_width} on pin {self._pin}")
        pi = pigpio.pi()
        pi.set_servo_pulsewidth(self._pin, pulse_width)
        pi.stop()
