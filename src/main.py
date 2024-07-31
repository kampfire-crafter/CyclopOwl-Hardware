# import psutil
# import os
# process = psutil.Process(os.getpid())
# print(f"Memory usage: {process.memory_info().rss / 1024 / 1024} MB")

# from rpyc.utils.server import ThreadedServer
# from rpcs.servos_rpc import ServosRpc
# from sockets.camera import init_camera

from sockets.camera_socket import CameraSocket
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s - %(name)s : %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger('Main')

camera_socket = CameraSocket()

try:
    if __name__ == "__main__":
        logger.info("CyclopOwl - Start")
        camera_socket.start()

        while True:
            logger.debug("CyclopOwl - Running")
            if not camera_socket.is_alive():
                camera_socket = CameraSocket()
                camera_socket.start()
            time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    logger.info("Stop server")
