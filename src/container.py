from dependency_injector import containers, providers
from drivers.camera import Camera
from services.camera_service import CameraService
from handlers.client_handler import ClientHandler
from sockets.main_socket import MainSocket

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    camera = providers.Singleton(Camera)
    camera_service = providers.Singleton(CameraService, camera=camera)
    client_handler = providers.Singleton(ClientHandler, camera_service=camera_service)
    main_socket = providers.Singleton(MainSocket, host=config.host, port=config.port, client_handler=client_handler)
