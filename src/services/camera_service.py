from services.camera_service_interface import CameraServiceInterface
from drivers.camera_driver_interface import CameraDriverInterface


class CameraService(CameraServiceInterface):
    """Implements the camera service interface to manage camera operations."""

    def __init__(self, camera_driver: CameraDriverInterface) -> None:
        """Initializes the CameraService with a camera driver."""
        self._camera_driver = camera_driver

    def start(self) -> None:
        """Starts the camera driver."""
        self._camera_driver.start()

    def stop(self) -> None:
        """Stops the camera driver."""
        self._camera_driver.stop()

    def record(self):
        """Records frames from the camera driver."""
        return self._camera_driver.record()
