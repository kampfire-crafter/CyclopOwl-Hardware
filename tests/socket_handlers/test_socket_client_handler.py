import pytest
import socket
import io
from unittest.mock import MagicMock, call
from socket_handlers.socket_client_handler import SocketClientHandler
from socket_handlers.io.camera_streaming_to_client_interface import CameraStreamingToClientInterface

def mocked_record():
    return [io.BytesIO(str(i).encode('utf-8')) for i in range(0, 9)]

class CameraStreamingToClientMock(CameraStreamingToClientInterface):
    def __init__(self, conn):
        self.is_running = False

    def start(self):
        self.is_running = True

class TestSocketClientHandler:
    @pytest.fixture(autouse=True)
    def setup_fixture(self):
        self.conn = MagicMock(spec=socket.socket)
        self.conn.send = MagicMock()
        self.streaming = CameraStreamingToClientMock(self.conn)

    @pytest.fixture
    def camera_streaming_to_client_factory(self):
        def factory(conn: socket.socket) -> CameraStreamingToClientInterface:
            return self.streaming
        return factory

    def test_client_handler(self, camera_streaming_to_client_factory):
        client_handler = SocketClientHandler(camera_streaming_to_client_factory)
        client_handler.handle(self.conn, "127.0.0.2")

        assert self.streaming.is_running is True
