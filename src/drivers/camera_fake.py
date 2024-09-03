import logging
from drivers.camera_interface import CameraInterface

logger = logging.getLogger('CameraFake')


class CameraFake(CameraInterface):
    def __init__(self) -> None:
        pass

    def start(self) -> None:
        pass

    def record(self):
        pass

    def stop(self) -> None:
        pass
