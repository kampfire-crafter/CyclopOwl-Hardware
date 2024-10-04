from abc import ABC, abstractmethod

class GPIOServiceInterface(ABC):
    """Interface for GPIO service."""

    @abstractmethod
    def __init__(self) -> None:
        """Initializes the GPIO service interface."""

    @abstractmethod
    def move(self, angles: tuple[int, int]) -> None:
        """Rotate the GPIO service to a specific position."""
