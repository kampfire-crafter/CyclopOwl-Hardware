import logging
import io
import socket
import struct
import threading
from services.camera_service_interface import CameraServiceInterface

logger = logging.getLogger("CameraStreamingToClient")

class CameraStreamingToClient(threading.Thread):
    def __init__(self, conn: socket.socket,  camera_service: CameraServiceInterface) -> None:
        super().__init__()
        self.camera_service = camera_service
        self.conn = conn
        self.is_running = True

    def run(self):
        logger.info("Start to send streaming to client")
        try:
            self._stream()
        except Exception as e:
            logger.error(e)
        finally:
            self.camera_service.stop()

    def _stream(self):
        self.camera_service.start()
        
        for stream in self.camera_service.record():
            self._send_stream_data(stream)
            if not self.is_running:
                break
        
    def _send_stream_data(self, stream: io.BytesIO) -> None:
        size = struct.pack('<L', stream.tell())
        stream.seek(0)
        read = stream.getvalue()
        self.conn.send(size)
        self.conn.send(read)

    def stop(self):
        self.is_running = False