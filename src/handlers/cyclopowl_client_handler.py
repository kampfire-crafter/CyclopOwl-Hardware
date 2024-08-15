import logging
from handlers.cyclopowl_client_handler_interface import CyclopOwlClientHandlerInterface

logger = logging.getLogger("CyclopOwlClientHandler")

class CyclopOwlClientHandler(CyclopOwlClientHandlerInterface):
    def handle(self, conn, addr):
        logging.info("test")
        logging.info(conn)
        logging.info(addr)
