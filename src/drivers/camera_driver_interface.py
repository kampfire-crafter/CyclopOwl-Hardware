from abc import ABC, abstractmethod

class CameraDriverInterface(ABC):
    """Interface for the camera driver."""
    
    @abstractmethod
    def __init__(self) -> None:
        """Initializes the camera driver interface."""

    @abstractmethod
    def start(self) -> None:
        """Starts the camera."""

    @abstractmethod
    def stop(self) -> None:
        """Stops the camera."""

    @abstractmethod
    def record(self):
        """Records frames from the camera."""
