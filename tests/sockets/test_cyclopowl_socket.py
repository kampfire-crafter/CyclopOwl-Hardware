import pytest
import socket
import time
from threading import Thread
from sockets.cyclopowl_socket import CyclopOwlSocket
from handlers.cyclopowl_client_handler import CyclopOwlClientHandler
from handlers.cyclopowl_client_handler_interface import CyclopOwlClientHandlerInterface

class CyclopOwlClientHandlerMock(CyclopOwlClientHandlerInterface):
    def __init__(self):
        self.handled = False

    def handle(self, conn, addr):
        self.handled = True

@pytest.fixture
def client_handler():
    return CyclopOwlClientHandlerMock()

class TestCyclopOwlSocket:

    def test_cyclopowl_socket(self, client_handler):
        # Create the server
        cyclopowl_socket = CyclopOwlSocket("127.0.0.1", 8080, client_handler)
        Thread(target=cyclopowl_socket.listen).start()
        
        # Connect a client to the server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 8080))
        time.sleep(1)

        assert client_handler.handled == True

        client.close()
        cyclopowl_socket.stop()
        