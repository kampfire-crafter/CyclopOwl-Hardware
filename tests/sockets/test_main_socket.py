import pytest
import socket
import time
from threading import Thread
from sockets.main_socket import MainSocket
from socket_handlers.socket_client_handler_interface import SocketClientHandlerInterface

class ClientHandlerMock(SocketClientHandlerInterface):
    def __init__(self):
        self.handled = False

    def handle(self, conn, addr):
        self.handled = True

@pytest.fixture
def client_handler():
    return ClientHandlerMock()

class TestMainSocket:
    def test_cyclopowl_socket(self, client_handler):
        # Create the server
        server = MainSocket("127.0.0.1", 8080, client_handler)
        Thread(target=server.listen).start()
        
        # Connect a client to the server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 8080))
        server.stop()
        time.sleep(1)

        assert client_handler.handled is True

        client.close()
