from services.camera_service_interface import CameraServiceInterface
from drivers.camera_interface import CameraInterface

class CameraService(CameraServiceInterface):
    def __init__(self, camera: CameraInterface) -> None:
        self._camera = camera

    def start(self) -> None:
        self._camera.start()

    def stop(self) -> None:
        self._camera.stop()

    def record(self):
        return self._camera.record()
