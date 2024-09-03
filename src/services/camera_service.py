from services.camera_service_interface import CameraServiceInterface
from drivers.camera_driver_interface import CameraDriverInterface


class CameraService(CameraServiceInterface):
    def __init__(self, camera_driver: CameraDriverInterface) -> None:
        self._camera_driver = camera_driver

    def start(self) -> None:
        self._camera_driver.start()

    def stop(self) -> None:
        self._camera_driver.stop()

    def record(self):
        return self._camera_driver.record()
