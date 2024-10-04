import logging
import socket
import threading
from services.gpio_service_interface import GPIOServiceInterface

logger = logging.getLogger("ClientSetpointToGPIO")

class ClientSetpointToGPIO(threading.Thread):
    def __init__(self, conn: socket.socket,  gpio_service: GPIOServiceInterface) -> None:
        super().__init__()
        self.gpio_service = gpio_service
        self.conn = conn
        self.is_running = True

    def run(self):
        logger.info("Start waiting for setpoint from client")
        while self.is_running:
            setpoint = self.conn.recv(1024)
            logger.debug(setpoint)
            if not setpoint:
                self.stop()

    def stop(self):
        logger.info("Stop waiting for setpoint from client")
        self.is_running = False


class ClientSetpointToGPIOFactory:
    def __init__(self, gpio_service: GPIOServiceInterface) -> None:
        self.gpio_service = gpio_service

    def __call__(self, conn: socket.socket) -> None:
        return ClientSetpointToGPIO(conn, self.gpio_service)
