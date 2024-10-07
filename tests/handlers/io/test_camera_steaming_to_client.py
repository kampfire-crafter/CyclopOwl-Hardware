import pytest
import socket
import struct
import io
from unittest.mock import MagicMock
from threading import Thread
from services.camera_service_interface import CameraServiceInterface
from handlers.io.camera_streaming_to_client import CameraStreamingToClient

class CameraServiceMock(CameraServiceInterface):
    def __init__(self):
        self.is_running = False

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def record(self):
        yield io.BytesIO("frame".encode())


class TestCameraStreamingToClient:
    @pytest.fixture(autouse=True)
    def setup_fixture(self):
        self.conn = MagicMock(spec=socket.socket)
        self.camera_service = CameraServiceMock()
        self.camera_streaming = CameraStreamingToClient(self.conn, self.camera_service)

    def test_start_stop_streaming(self):
        """Test de démarrage et arrêt du streaming."""
        self.camera_streaming.start()
        assert self.camera_streaming.is_running is True

        self.camera_streaming.stop()
        assert self.camera_streaming.is_running is False

    def test_send_stream_data(self):
        """Test l'envoi de données du flux vidéo via le socket."""
        content = b"test_frame_data"
        stream = io.BytesIO(content)
        
        self.camera_streaming._send_stream_data(stream)
        
        assert self.conn.send.call_count == 2
        self.conn.send.assert_any_call(content)
