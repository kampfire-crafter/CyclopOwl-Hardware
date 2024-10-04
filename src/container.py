import env
import os
import socket
from typing import Any
from sockets.main_socket import MainSocket
from handlers.client_handler import ClientHandler

from drivers.camera_driver import CameraDriver
from services.camera_service import CameraService
from services.camera_service_interface import CameraServiceInterface

from drivers.gpio_driver import GPIODriver
from services.gpio_service import GPIOService
from services.gpio_service_interface import GPIOServiceInterface

from handlers.io.camera_streaming_to_client import CameraStreamingToClientFactory
from handlers.io.client_setpoint_to_gpio import ClientSetpointToGPIOFactory

class Container:
    camera_driver = CameraDriver()
    camera_service = CameraService(camera_driver)
    cam_streaming_factory = CameraStreamingToClientFactory(camera_service)

    gpio_driver = GPIODriver()
    gpio_service = GPIOService(gpio_driver, int(os.getenv('PIN_SERVO_X') or 0), int(os.getenv('PIN_SERVO_Y') or 1))
    gpio_factory = ClientSetpointToGPIOFactory(gpio_service)

    client_handler = ClientHandler(cam_streaming_factory, gpio_factory)

    main_socket = MainSocket(host=os.getenv('HOST'), port=int(os.getenv('PORT')), client_handler=client_handler)
