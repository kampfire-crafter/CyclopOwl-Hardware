import logging
import socket
import io
from drivers.camera import Camera
# import io
# import struct
# import time

logger = logging.getLogger('CameraSocket')


class CameraSocket:
    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("0.0.0.0", 8000))
        self.socket.listen()

        self.camera = Camera()
    
    def listen(self):
        conn, addr = self.socket.accept()

        with conn:
            print(f"Connecté par {addr}")
            
            self.camera.start()

            for stream in self.camera.record():
                logger.info(stream)
                conn.send(stream.getvalue())
                # conn.send(io.BytesIO(b"test").getvalue())

            self.camera.stop()
            conn.close()
            self.socket.close()
        
# def init_camera():
#     client_socket = socket.socket()
#     client_socket.connect(('192.168.1.44', 8000))

#     connection = client_socket.makefile('wb')

#     try:
#         camera = picamera.PiCamera()
#         camera.resolution = (640, 480)

#         camera.start_preview()
#         time.sleep(2)

#         start = time.time()
#         logger.info(start)
#         stream = io.BytesIO()
#         for foo in camera.capture_continuous(stream, 'jpeg'):

#             connection.write(struct.pack('<L', stream.tell()))
#             connection.flush()

#             stream.seek(0)
#             connection.write(stream.read())

#             if time.time() - start > 60:
#                 break

#             stream.seek(0)
#             stream.truncate()

#         connection.write(struct.pack('<L', 0))
#     finally:
#         connection.close()
#         client_socket.close()
