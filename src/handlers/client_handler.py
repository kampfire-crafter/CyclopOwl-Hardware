from typing import Callable
import logging
import socket
import threading
from handlers.client_handler_interface import ClientHandlerInterface
from handlers.io.camera_streaming_to_client_interface import CameraStreamingToClientInterface
from handlers.io.client_setpoint_to_gpio_interface import ClientSetpointToGPIOInterface

logger = logging.getLogger("SocketClientHandler")

class ClientHandler(ClientHandlerInterface):
    """Handle the client"""
    
    def __init__(self, 
                 cam_stream_factory: Callable[[socket.socket], CameraStreamingToClientInterface],
                 gpio_factory: Callable[[socket.socket], ClientSetpointToGPIOInterface]
                ) -> None:
        self.cam_stream_factory = cam_stream_factory
        self.cam_stream_thread = None
        self.gpio_factory = gpio_factory
        self.gpio_thread = None

    def handle(self, conn: socket.socket, addr: str) -> None:
        logger.info("Handle the client %s", addr)
        self.cam_stream_thread = self.cam_stream_factory(conn=conn)
        self.gpio_thread = self.gpio_factory(conn=conn)
        self.cam_stream_thread.start()
        self.gpio_thread.start()
    
    def release(self):
        logger.info("Release the client")
        self.cam_stream_thread.stop()
        self.gpio_thread.stop()
