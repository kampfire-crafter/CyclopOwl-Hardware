import pytest
import time
import socket
import io
from unittest.mock import MagicMock, call
from socket_handlers.socket_client_handler import SocketClientHandler
from socket_handlers.io.camera_streaming_to_client_interface import CameraStreamingToClientInterface
from services.camera_service_interface import CameraServiceInterface

# Mock de l'enregistrement
def mocked_record():
    return [io.BytesIO(str(i).encode('utf-8')) for i in range(0, 9)]

# Mock du service de caméra
class CameraServiceMock(CameraServiceInterface):
    def __init__(self):
        self.is_running = False

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def record(self):
        for stream in mocked_record():
            yield stream
            time.sleep(0.1)

# Mock de la classe de streaming à la caméra
class CameraStreamingToClientMock(CameraStreamingToClientInterface):
    def __init__(self, conn: socket.socket, camera_service: CameraServiceInterface) -> None:
        self._camera_service = camera_service
        self._conn = conn

    def run(self):
        # Remplace la méthode 'run' par un mock
        self._camera_service.start()
        for stream in self._camera_service.record():
            self._send_stream_data(stream)
        self._camera_service.stop()

    def _send_stream_data(self, stream: io.BytesIO) -> None:
        size = struct.pack('<L', stream.tell())
        stream.seek(0)
        read = stream.getvalue()
        self._conn.send(size)
        self._conn.send(read)

@pytest.fixture
def camera_service():
    return CameraServiceMock()

@pytest.fixture
def camera_streaming_to_client_factory():
    # Factory qui retourne des instances de CameraStreamingToClientMock
    def factory(conn: socket.socket) -> CameraStreamingToClientInterface:
        return CameraStreamingToClientMock(conn, CameraServiceMock())
    return factory

def test_client_handler(camera_service, camera_streaming_to_client_factory):
    mock_socket = MagicMock(spec=socket.socket)
    mock_socket.send = MagicMock()

    # Utilisation de la factory pour le client handler
    client_handler = SocketClientHandler(camera_streaming_to_client_factory)
    client_handler.handle(mock_socket, "127.0.0.2")

    # Vérifier que le service a démarré et arrêté
    assert camera_service.is_running is True
    assert mock_socket.send.call_count == len(mocked_record()) * 2  # Chaque appel send est fait pour la taille et le contenu
