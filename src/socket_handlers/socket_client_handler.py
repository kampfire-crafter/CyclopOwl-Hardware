import logging
import socket
import struct
import io
from socket_handlers.socket_client_handler_interface import SocketClientHandlerInterface
from services.camera_service_interface import CameraServiceInterface

logger = logging.getLogger("ClientHandler")


class SocketClientHandler(SocketClientHandlerInterface):
    def __init__(self, camera_service: CameraServiceInterface) -> None:
        self._camera_service = camera_service

    def handle(self, conn: socket.socket, addr: str) -> None:
        logger.info("Handle the client %s", addr)
        # Ici Threads ?
        # self._stream_camera_to_client(conn)
        # self._listen_event_message(conn)

    # def _stream_camera_to_client(self, conn):
    #     logger.info("Start to send streaming to client")
    #     try:
    #         self._camera_service.start()

    #         for stream in self._camera_service.record():
    #             self._send_stream_data(conn, stream)

    #     except Exception as e:
    #         logger.error(e)

    #     finally:
    #         self._camera_service.stop()

    # def _listen_event_message(self, conn):
    #     pass

    # def _send_stream_data(self, conn: socket.socket, stream: io.BytesIO) -> None:
    #     size = struct.pack('<L', stream.tell())
    #     stream.seek(0)
    #     read = stream.getvalue()
    #     conn.send(size)
    #     conn.send(read)
