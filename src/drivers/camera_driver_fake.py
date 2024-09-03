import logging
from drivers.camera_driver_interface import CameraDriverInterface

logger = logging.getLogger('CameraFake')


class CameraDriverFake(CameraDriverInterface):
    def __init__(self) -> None:
        pass

    def start(self) -> None:
        pass

    def record(self):
        pass

    def stop(self) -> None:
        pass
