import logging
from sockets.main_socket import MainSocket

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s - %(name)s : %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger('Main')

main_socket = MainSocket()

try:
    if __name__ == "__main__":
        logger.info("CyclopOwl - Start")
        main_socket.listen()

except KeyboardInterrupt:
    pass

finally:
    logger.info("Stop server")
