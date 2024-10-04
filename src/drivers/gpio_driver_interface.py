from abc import ABC, abstractmethod

class GPIODriverInterface(ABC):
    """Interface for the GPIO driver."""

    @abstractmethod
    def set_servo_pulse_width(self, pin: int, position: float) -> None:
        """Sets the pulse width for a servo connected to a specific GPIO pin."""
