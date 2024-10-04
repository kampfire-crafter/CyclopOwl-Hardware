import env
import logging
from container import Container

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(name)s : %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('Main')

try:
    if __name__ == "__main__":
        # Start the socket listening
        logger.info("CyclopOwl - Start")
        main_socket = Container.main_socket
        main_socket.listen()

except KeyboardInterrupt:
    pass

finally:
    logger.info("Stop server")
    main_socket.stop()
