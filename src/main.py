# from rpyc.utils.server import ThreadedServer
# from rpcs.servos_rpc import ServosRpc
# from sockets.camera import init_camera
from sockets.camera_socket import CameraSocket

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s - %(name)s : %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger('Main')

# camera = Camera()
camera_socket = CameraSocket()

try:
    if __name__ == "__main__":
        logger.info("Start server")
        # camera.start()
        # for stream in camera.record():
        #     logger.info(stream)
        camera_socket.listen()

        
except KeyboardInterrupt:
    pass

finally:
    logger.info("Stop server")
    # camera.stop()
    # server.close()
