import socket

class ClientHandlerInterface:
    """Defines the interface for handling client connections and their lifecycle."""

    def handle(self, conn: socket.socket, addr: str) -> None:
        """Manages client connection and processes its requests."""
        pass

    def release(self) -> None:
        """Performs cleanup and releases resources."""
        pass
