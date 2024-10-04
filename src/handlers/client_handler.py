from typing import Callable, List, Union
import logging
import socket
import json

from handlers.client_handler_interface import ClientHandlerInterface
from handlers.io.camera_streaming_to_client_interface import CameraStreamingToClientInterface
from services.gpio_service_interface import GPIOServiceInterface
from enums.command_action import CommandAction
from custom_types.command import Command


logger = logging.getLogger("SocketClientHandler")


class ClientHandler(ClientHandlerInterface):
    """Handles client connections and processes their commands."""

    def __init__(
        self,
        gpio_service: GPIOServiceInterface,
        cam_stream_factory: Callable[[socket.socket], CameraStreamingToClientInterface]
    ) -> None:
        """Sets up the client handler with GPIO service and camera stream factory."""
        self.gpio_service = gpio_service
        self.cam_stream_factory = cam_stream_factory
        self.cam_stream_thread = None
        self.is_running = True

    def handle(self, conn: socket.socket, addr: str) -> None:
        """Manages the main client communication loop."""
        logger.info("Handle the client %s", addr)
        self.is_running = True

        while self.is_running:
            command = conn.recv(1024).decode('utf-8').strip()
            self._handle_command(command, conn)

    def _handle_command(self, command: str, conn: socket.socket) -> None:
        """Processes and validates incoming client commands."""
        logger.info("Handle command : %s", command)

        if command == "":
            self.release()
            return
        
        decoded_command: Command = json.loads(command)
        try:
            action = CommandAction(decoded_command["action"])
        except ValueError:
            logger.info("Action unknown")
            return
        
        self._handle_action(action, decoded_command["args"], conn)

    def _handle_action(
        self,
        action: CommandAction,
        args: List[Union[str, bool, int]],
        conn: socket.socket
    ) -> None:
        """Executes the action based on client command."""
        match action:
            case CommandAction.ENABLE_STREAMING:
                self.cam_stream_thread = self.cam_stream_factory(conn=conn)
                self.cam_stream_thread.start()

            case CommandAction.DISABLE_STREAMING:
                self.cam_stream_thread.stop()
                self.cam_stream_thread = None

            case CommandAction.ROTATE:
                self.gpio_service.move(args)
    
    def release(self) -> None:
        """Cleans up resources."""
        logger.info("Release the client")
        if self.cam_stream_thread:
            self.cam_stream_thread.stop()
            self.cam_stream_thread = None

        self.is_running = False
    