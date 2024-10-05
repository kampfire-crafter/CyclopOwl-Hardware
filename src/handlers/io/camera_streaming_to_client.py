import logging
import io
import socket
import struct
import threading
from services.camera_service_interface import CameraServiceInterface


logger = logging.getLogger("CameraStreamingToClient")


class CameraStreamingToClient(threading.Thread):
    """Handles camera streaming to a connected client in a separate thread."""

    def __init__(self, conn: socket.socket, camera_service: CameraServiceInterface) -> None:
        """Initializes the streaming thread with socket connection and camera service."""
        super().__init__()
        self.camera_service = camera_service
        self.conn = conn
        self.is_running = True

    def run(self) -> None:
        """Executes the main streaming loop."""
        logger.info("Start to send streaming to client")
        self.camera_service.start()
        try:
            self._stream()
        except Exception as e:
            logger.error(e)
        finally:
            self.camera_service.stop()

    def _stream(self) -> None:
        """Manages the continuous streaming of camera data to the client."""
        for stream in self.camera_service.record():
            self._send_stream_data(stream)
            if not self.is_running:
                break

    def _send_stream_data(self, stream: io.BytesIO) -> None:
        """Sends a single frame of stream data with its size header."""
        size = struct.pack('<L', stream.tell())
        stream.seek(0)
        data = stream.getvalue()
        self.conn.send(size)
        self.conn.send(data)

    def stop(self) -> None:
        """Signals the streaming thread to stop."""
        logger.info("Stop the streaming to client")
        self.is_running = False


class CameraStreamingToClientFactory:
    """Factory to create CameraStreamingToClient instances."""

    def __init__(self, camera_service: CameraServiceInterface) -> None:
        """Initializes the factory with a camera service."""
        self.camera_service = camera_service

    def __call__(self, conn: socket.socket) -> CameraStreamingToClient:
        """Creates and returns a new instance."""
        return CameraStreamingToClient(conn, self.camera_service)