from typing import Callable
import logging
import socket
from handlers.client_handler_interface import ClientHandlerInterface
from handlers.io.camera_streaming_to_client_interface import CameraStreamingToClientInterface

logger = logging.getLogger("SocketClientHandler")

class ClientHandler(ClientHandlerInterface):
    """Handle the client"""
    
    def __init__(self, camera_streaming_to_client_factory: Callable[[socket.socket], CameraStreamingToClientInterface]) -> None:
        self.camera_streaming_to_client_factory = camera_streaming_to_client_factory
        self.camera_streaming_thread = None

    def handle(self, conn: socket.socket, addr: str) -> None:
        logger.info("Handle the client %s", addr)
        # Ici Threads ?
        self.camera_streaming_thread = self.camera_streaming_to_client_factory(conn=conn)
        self.camera_streaming_thread.start()

    def release(self):
        logger.info("Release the client")
        self.camera_streaming_thread.stop()
