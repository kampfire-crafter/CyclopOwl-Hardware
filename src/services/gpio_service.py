import logging
from drivers.gpio_driver_interface import GPIODriverInterface

logger = logging.getLogger("SocketClientHandler")

class GPIOService:
    def __init__(self, gpio_driver: GPIODriverInterface, pin_x: int, pin_y: int) -> None:
        self.gpio_driver = gpio_driver
        self.pin_x = pin_x
        self.pin_y = pin_y

    def calibrate(self):
        pass

    def move(self, positions: tuple[int, int]):
        logger.debug("Received positions %s", positions)
        self.gpio_driver.set_servo_pulse_width(self.pin_x, positions[0])
        self.gpio_driver.set_servo_pulse_width(self.pin_y, positions[1])
        