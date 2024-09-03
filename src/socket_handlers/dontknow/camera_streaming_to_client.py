import logging
import io
# import socket
import struct

logger = logging.getLogger("CameraStreamingToClient")

class CameraStreamingToClient:
    def __init__(self, conn, camera_service) -> None:
        self._camera_service = camera_service
        self._conn = conn

    def run(self):
        logger.info("Start to send streaming to client")
        try:
            self._camera_service.start()

            for stream in self._camera_service.record():
                self._send_stream_data(stream)

        except Exception as e:
            logger.error(e)

        finally:
            self._camera_service.stop()

    def _send_stream_data(self, stream: io.BytesIO) -> None:
        size = struct.pack('<L', stream.tell())
        stream.seek(0)
        read = stream.getvalue()
        self._conn.send(size)
        self._conn.send(read)
