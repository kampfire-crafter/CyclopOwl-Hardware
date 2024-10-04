from drivers.gpio_driver_interface import GPIODriverInterface
import pigpio
import logging

logger = logging.getLogger("GPIODriver")

class GPIODriver(GPIODriverInterface):

    def set_servo_pulse_width(self, pin, width):
        logger.debug(f"Set pulse width {width} on pin {pin}")
        pi = pigpio.pi()
        pi.set_servo_pulsewidth(pin, width)
        pi.stop()

