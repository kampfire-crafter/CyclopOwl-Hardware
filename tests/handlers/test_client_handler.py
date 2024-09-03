import pytest
import time
import socket
import io
from socket_handlers.socket_client_handler import SocketClientHandler
from services.camera_service_interface import CameraServiceInterface
from unittest.mock import MagicMock

def mocked_record():
    return [io.StringIO(str(i)) for i in range(0, 9)]

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

@pytest.fixture
def camera_service():
    return CameraServiceMock()

class TestClientHandler:
    def test_client_handler(self, camera_service):
        mock_socket = MagicMock(spec=socket.socket)
        mock_socket.send = MagicMock()

        client_handler = SocketClientHandler(camera_service)
        client_handler.handle(mock_socket, "127.0.0.2")

        assert camera_service.is_running is True
        assert mock_socket.send.call_count == len(mocked_record()) * 2
