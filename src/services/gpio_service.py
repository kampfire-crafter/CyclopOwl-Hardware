import logging
from drivers.gpio_driver_interface import GPIODriverInterface

logger = logging.getLogger("SocketClientHandler")

class GPIOService:
    """Service for managing GPIO operations using a specific GPIO driver."""

    def __init__(self, gpio_driver: GPIODriverInterface, pin_x: int, pin_y: int) -> None:
        """Initializes the GPIO service with the specified driver and pins."""
        self.gpio_driver = gpio_driver
        self.pin_x = pin_x
        self.pin_y = pin_y

    def move(self, angles: tuple[int, int]) -> None:
        """Rotate the servos to the specified angles."""
        logger.debug("Set angles %s", angles)
        self.gpio_driver.set_servo_pulse_width(self.pin_x, angles[0])
        self.gpio_driver.set_servo_pulse_width(self.pin_y, angles[1])
