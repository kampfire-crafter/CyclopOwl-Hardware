from abc import ABC, abstractmethod

class CameraServiceInterface(ABC):
    """Interface for camera service."""

    @abstractmethod
    def start(self) -> None:
        """Starts the camera service."""

    @abstractmethod
    def stop(self) -> None:
        """Stops the camera service."""

    @abstractmethod
    def record(self) -> None:
        """Records using the camera service."""
