from typing import Callable
import logging
import socket
from socket_handlers.socket_client_handler_interface import SocketClientHandlerInterface
from socket_handlers.io.camera_streaming_to_client_interface import CameraStreamingToClientInterface

logger = logging.getLogger("SocketClientHandler")

class SocketClientHandler(SocketClientHandlerInterface):
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
