import logging
import socket
import struct
from threading import Thread
from drivers.camera import Camera

logger = logging.getLogger('CameraSocket')


class MainSocket:
    def __init__(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(("0.0.0.0", 8000))
        self._socket.listen()
        self._camera = Camera()
    
    def listen(self):
        try:
            conn, addr = self._socket.accept()

            with conn:
                logger.info("Client connected : %s", addr)
                camera_thread = Thread(target=self._camera_record, args=(conn,))

                camera_thread.start()
                    
        except (BrokenPipeError, ConnectionResetError):
            logger.info("Client disconnected")

        finally:
            conn.close()
            self._socket.close()
            self._camera.stop()

    def _gpio_management(self):
        pass

    def _camera_record(self, conn):
        self._camera.start()

        for stream in self._camera.record():
            self._send_stream_data(conn, stream)

    def _send_stream_data(self, conn, stream):
        size = struct.pack('<L', stream.tell())
        stream.seek(0)
        read = stream.getvalue() # read = stream.read()
        conn.send(size)
        conn.send(read)