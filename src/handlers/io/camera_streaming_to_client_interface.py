import io
import socket
import threading
from abc import ABC, abstractmethod


class CameraStreamingToClientInterface(threading.Thread, ABC):
    """Defines the interface for camera streaming thread implementations."""

    @abstractmethod
    def __init__(self, conn: socket.socket, camera_service: 'CameraServiceInterface') -> None:
        """Initializes the streaming thread with required dependencies."""
        super().__init__()

    @abstractmethod
    def run(self) -> None:
        """Executes the main streaming loop."""

    @abstractmethod
    def stop(self) -> None:
        """Stops the streaming thread gracefully."""
