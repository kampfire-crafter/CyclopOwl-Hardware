import socket
import threading
from services.camera_service_interface import CameraServiceInterface

class ClientSetpointToGPIOInterface(threading.Thread):
    def __init__(self, conn: socket.socket,  gpio_service: CameraServiceInterface) -> None:
        pass

    def run(self):
        pass

    def stop(self):
        pass