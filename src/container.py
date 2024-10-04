import os
from sockets.main_socket import MainSocket
from handlers.client_handler import ClientHandler
from drivers.camera_driver import CameraDriver
from services.camera_service import CameraService
from drivers.gpio_driver import GPIODriver
from services.gpio_service import GPIOService
from handlers.io.camera_streaming_to_client import CameraStreamingToClientFactory

class Container:
    """Container for managing the application's services and dependencies."""
    
    camera_driver = CameraDriver()
    camera_service = CameraService(camera_driver)
    cam_streaming_factory = CameraStreamingToClientFactory(camera_service)

    gpio_driver = GPIODriver()
    gpio_service = GPIOService(
        gpio_driver,
        int(os.getenv('PIN_SERVO_X') or 12),
        int(os.getenv('PIN_SERVO_Y') or 13)
    )

    client_handler = ClientHandler(gpio_service, cam_streaming_factory)

    main_socket = MainSocket(
        host=os.getenv('HOST'),
        port=int(os.getenv('PORT')),
        client_handler=client_handler
    )
