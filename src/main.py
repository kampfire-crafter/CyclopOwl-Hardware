# from rpyc.utils.server import ThreadedServer
# from rpcs.servos_rpc import ServosRpc
# from sockets.camera import init_camera
from sockets.camera_socket import Camera
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s - %(name)s : %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger('Main')

camera = Camera()

# server = ThreadedServer(ServosRpc, port = 18812)

try:
    if __name__ == "__main__":
        logger.info("Start server")
        camera.start()
        for stream in camera.record():
            logger.info(stream)
        # server.start()
        # init_camera()
except KeyboardInterrupt:
    pass

finally:
    logger.info("Stop server")
    camera.stop()
    # server.close()
