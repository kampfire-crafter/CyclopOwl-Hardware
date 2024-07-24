from rpyc.utils.server import ThreadedServer
from rpcs.servos_rpc import ServosRpc
import logging

logging.basicConfig(level=logging.DEBUG, 
                    format='[%(asctime)s] %(levelname)s - %(name)s : %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

logger  = logging.getLogger('Main')

server = ThreadedServer(ServosRpc, port = 18812)

try:
    if __name__ == "__main__":
        logger.info("Start server")
        server.start()

except KeyboardInterrupt:
    logger.info("Stop server")
    server.close()

finally:
    logger.info("Stop server")
    server.close()
