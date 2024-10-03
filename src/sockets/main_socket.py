from socket_handlers.socket_client_handler_interface import SocketClientHandlerInterface
import logging
import socket

logger = logging.getLogger('MainSocket')


class MainSocket:
    """Receive the client connection, then transfer the client to the handler"""

    def __init__(self, host: str, port: int, socket_client_handler: SocketClientHandlerInterface) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()
        self.socket_client_handler = socket_client_handler
        self.is_running = True

    def listen(self) -> None:
        """Listen and wait for a client connection"""

        try:
            self._wait_new_client()

        except (BrokenPipeError, ConnectionResetError):
            logger.info("Client disconnected")

    def _wait_new_client(self):
        """Wait for a client connection then handle it"""
        while self.is_running:
            conn, addr = self.socket.accept()
            logger.info("Client connected : %s", addr)

            with conn:
                self.socket_client_handler.handle(conn, addr)

    def stop(self) -> None:
        """Stop waiting a client connection"""
        # self.socket.shutdown(socket.SHUT_RDWR)
        self.is_running = False
        self.socket_client_handler.release()
        self.socket.close()
        self.socket.detach()
