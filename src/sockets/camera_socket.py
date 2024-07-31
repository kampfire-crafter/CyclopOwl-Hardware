import logging
import socket
from drivers.camera import Camera
# import io
import struct
# import time
from threading import Thread

logger = logging.getLogger('CameraSocket')


class CameraSocket(Thread):
    def __init__(self) -> None:
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("0.0.0.0", 8000))
        self.socket.listen()
    
    def run(self):
        try:
            conn, addr = self.socket.accept()

            with conn:
                logger.info(f"Client connected : {addr}")
                
                camera = Camera()
                camera.start()

                for stream in camera.record():
                    logger.debug(stream)
                    #conn.send(stream.getvalue())
                    size = struct.pack('<L', stream.tell())
                    stream.seek(0)
                    # read = stream.read()
                    read = stream.getvalue()
                    conn.send(size)
                    conn.send(read)
                    

        except (BrokenPipeError, ConnectionResetError):
            logger.info("Client disconnected")

        finally:
            conn.close()
            self.socket.close()
            camera.stop()
