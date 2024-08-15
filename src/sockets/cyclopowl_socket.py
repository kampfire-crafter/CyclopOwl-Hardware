import socket
import logging
from threading import Thread
from handlers.cyclopowl_client_handler_interface import CyclopOwlClientHandlerInterface

logger = logging.getLogger('CyclopOwlSocket')

class CyclopOwlSocket:
    def __init__(self, host: str, port: int, handler: CyclopOwlClientHandlerInterface) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((host, port))
        self._socket.listen()
        self._handler = handler
        self._is_running = True

    def listen(self):
        try:
            while self._is_running:
                conn, addr = self._socket.accept()
                Thread(target=self._handler.handle, args=(conn, addr)).start()
                
        except (BrokenPipeError, ConnectionResetError, KeyboardInterrupt) as e:
            logger.error(e)

        finally:
            self._socket.close()
            # self._socket.shutdown(socket.SHUT_RDWR)
        
    def stop(self):
        self._is_running = False
        self._socket.close()
        # self._socket.shutdown(socket.SHUT_RDWR)
        