import pytest
import socket
import io
from unittest.mock import MagicMock, call
from handlers.client_handler import ClientHandler
from handlers.io.camera_streaming_to_client_interface import CameraStreamingToClientInterface
from handlers.io.client_setpoint_to_gpio_interface import ClientSetpointToGPIOInterface

def mocked_record():
    return [io.BytesIO(str(i).encode('utf-8')) for i in range(0, 9)]

class CameraStreamingToClientMock(CameraStreamingToClientInterface):
    def __init__(self, conn):
        self.is_running = False

    def start(self):
        self.is_running = True

class ClientToGPIOMock(ClientSetpointToGPIOInterface):
    def __init__(self, conn):
        self.is_running = False

    def start(self):
        self.is_running = True

class TestClientHandler:
    @pytest.fixture(autouse=True)
    def setup_fixture(self):
        self.conn = MagicMock(spec=socket.socket)
        self.conn.send = MagicMock()
        self.streaming = CameraStreamingToClientMock(self.conn)
        self.gpio = ClientToGPIOMock(self.conn)

    @pytest.fixture
    def camera_streaming_to_client_factory(self):
        def factory(conn: socket.socket) -> CameraStreamingToClientInterface:
            return self.streaming
        return factory

    @pytest.fixture
    def client_to_gpio_factory(self):
        def factory(conn: socket.socket) -> ClientSetpointToGPIOInterface:
            return self.streaming
        return factory

    def test_client_handler(self, camera_streaming_to_client_factory, client_to_gpio_factory):
        client_handler = ClientHandler(camera_streaming_to_client_factory, client_to_gpio_factory)
        client_handler.handle(self.conn, "127.0.0.2")

        assert self.streaming.is_running is True
