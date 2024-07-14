from rpyc.utils.server import ThreadedServer
from rpc.servos_rpc import ServosRpc

server = ThreadedServer(ServosRpc, port = 18812)

try:
    if __name__ == "__main__":
        print("[main] Start server")
        server.start()

except KeyboardInterrupt:
    print("[main] Stop server")
    server.close()

finally:
    print("[main] Stop server")
    server.close()
