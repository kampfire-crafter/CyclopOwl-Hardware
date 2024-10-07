import pytest
import socket
import json
from threading import Thread
from unittest.mock import MagicMock
from typing import Callable
from handlers.client_handler import ClientHandler
from handlers.io.camera_streaming_to_client_interface import CameraStreamingToClientInterface
from services.gpio_service_interface import GPIOServiceInterface
from enums.command_action import CommandAction

class CameraStreamingToClientMock(CameraStreamingToClientInterface):
    def __init__(self, conn):
        self.is_running = False
        self.conn = conn

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def run(self):
        # Simulated logic for streaming if needed
        pass

class GPIOMock(GPIOServiceInterface):
    def __init__(self):
        self.last_move_args = None

    def move(self, args):
        self.last_move_args = args

class TestClientHandler:
    @pytest.fixture(autouse=True)
    def setup_fixture(self):
        self.conn = MagicMock(spec=socket.socket)
        self.conn.recv = MagicMock(return_value=b'')
        self.gpio_service = GPIOMock()
        self.streaming = CameraStreamingToClientMock(self.conn)

        self.cam_stream_factory: Callable[[socket.socket], CameraStreamingToClientInterface] = \
            lambda conn: self.streaming

        self.client_handler = ClientHandler(self.gpio_service, self.cam_stream_factory)

    def test_handle_empty_command(self):
        self.conn.recv.return_value = b''  # Simule une commande vide

        self.client_handler.handle(self.conn, "127.0.0.1")

        assert self.client_handler.is_running is False  # La boucle devrait s'arrêter

    def test_handle_command_enable_and_disable_streaming(self):
        command = {"action": CommandAction.ENABLE_STREAMING.name,"args": []}
        self.conn.recv.return_value = json.dumps(command).encode('utf-8')

        Thread(target=lambda: self.client_handler.handle(self.conn, "127.0.0.1")).start()

        assert self.client_handler.is_running is True
        assert self.streaming.is_running is True 

        self.client_handler.release()

        assert self.client_handler.is_running is False
        assert self.streaming.is_running is False

    def test_handle_command_rotate(self):
        command = {"action": CommandAction.ROTATE.name,"args": [0, 1]}
        self.conn.recv.return_value = json.dumps(command).encode('utf-8')

        Thread(target=lambda: self.client_handler.handle(self.conn, "127.0.0.1")).start()

        assert self.gpio_service.last_move_args == [0, 1]  # Vérifie que les arguments ont été passés correctement

        self.client_handler.release()
        