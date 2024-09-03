from dependency_injector import containers, providers
from services.camera_service import CameraService
from socket_handlers.socket_client_handler import SocketClientHandler
from sockets.main_socket import MainSocket
from drivers.camera_driver import CameraDriver
from socket_handlers.io.camera_streaming_to_client import CameraStreamingToClient

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    camera_driver = providers.Singleton(CameraDriver)
    camera_service = providers.Singleton(CameraService, camera=camera_driver)
    camera_streaming_to_client_factory = providers.Factory(CameraStreamingToClient,
                                                           camera_service=camera_service)
    
    client_handler = providers.Singleton(SocketClientHandler,
                                         camera_streaming_to_client_factory=camera_streaming_to_client_factory)
    
    main_socket = providers.Singleton(
        MainSocket, host=config.host, port=config.port, client_handler=client_handler)
