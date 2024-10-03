class SocketClientHandlerInterface:
    def handle(self, conn, addr):
        pass
    def release(self):
        pass