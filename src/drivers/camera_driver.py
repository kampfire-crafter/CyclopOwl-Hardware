import io
import time
import picamera
import logging
from drivers.camera_driver_interface import CameraDriverInterface

logger = logging.getLogger('Camera')

class CameraDriver(CameraDriverInterface):
    """Driver for controlling the pi camera."""
    _RESOLUTION = (640, 480)
    _WARM_UP_DELAY = 2

    def __init__(self) -> None:
        """Initializes the pi camera"""
        self.camera = picamera.PiCamera()
        self.camera.resolution = self._RESOLUTION

    def start(self) -> None:
        """Starts the camera preview and warms it up."""
        logger.info('Start and warm up the camera')
        self.camera.start_preview()
        time.sleep(self._WARM_UP_DELAY)

    def record(self):
        """Yields frames captured continuously from the camera."""
        stream = io.BytesIO()
        for frame in self.camera.capture_continuous(stream, 'jpeg'):
            yield frame
            frame.seek(0)
            frame.truncate()

    def stop(self) -> None:
        """Stops the camera preview."""
        logger.info('Stop the camera')
        self.camera.stop_preview()
