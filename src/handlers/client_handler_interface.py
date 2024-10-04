import socket
from typing import Callable, List, Union
from handlers.io.camera_streaming_to_client_interface import CameraStreamingToClientInterface
from services.gpio_service_interface import GPIOServiceInterface
from enums.command_action import CommandAction
from custom_types.command import Command
from abc import ABC, abstractmethod

class ClientHandlerInterface(ABC):
    """Defines the interface for handling client connections and their lifecycle."""

    @abstractmethod
    def __init__(
        self,
        gpio_service: GPIOServiceInterface,
        cam_stream_factory: Callable[[socket.socket], CameraStreamingToClientInterface]
    ) -> None:
        """Sets up the client handler with GPIO service and camera stream factory."""

    @abstractmethod
    def handle(self, conn: socket.socket, addr: str) -> None:
        """Manages the main client communication loop."""

    @abstractmethod
    def release(self) -> None:
        """Performs cleanup and releases resources."""
