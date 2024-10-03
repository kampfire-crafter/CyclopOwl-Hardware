import logging
from container import Container

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s - %(name)s : %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger('Main')

try:
    if __name__ == "__main__":
        container = Container()
        container.config.host.from_env("HOST", as_=str, default="0.0.0.0")
        container.config.port.from_env("PORT", as_=int, default=8000)
        container.wire(modules=[__name__])

        logger.info("CyclopOwl - Start")
        main_socket = container.main_socket()
        main_socket.listen()

except KeyboardInterrupt:
    pass

finally:
    logger.info("Stop server")
    main_socket.stop()
