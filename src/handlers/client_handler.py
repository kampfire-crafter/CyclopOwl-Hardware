import logging
import socket
import struct
import io
from handlers.client_handler_interface import ClientHandlerInterface
from services.camera_service_interface import CameraServiceInterface

logger = logging.getLogger("ClientHandler")

class ClientHandler(ClientHandlerInterface):
    def __init__(self, camera_service: CameraServiceInterface) -> None:
        self._camera_service = camera_service

    def handle(self, conn: socket.socket, addr: str) -> None:
        logger.info("Start to send streaming to %s", addr)
        try:
            self._camera_service.start()

            for stream in self._camera_service.record():
                self._send_stream_data(conn, stream)

        except Exception as e:
            logger.error(e)
            self._camera_handler.stop()

    def _send_stream_data(self, conn: socket.socket, stream: io.BytesIO) -> None:
        size = struct.pack('<L', stream.tell())
        stream.seek(0)
        read = stream.getvalue()
        conn.send(size)
        conn.send(read)
