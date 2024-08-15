import io
import time
import picamera
import logging

logger = logging.getLogger('Camera')


class Camera:
    def __init__(self) -> None:
        self._camera = picamera.PiCamera()
        self._camera.resolution = (640, 480)

    def start(self) -> None:
        logger.info('Start and warm up the camera')
        self._camera.start_preview()
        time.sleep(2)

    def record(self):
        stream = io.BytesIO()
        for frame in self._camera.capture_continuous(stream, 'jpeg'):
            yield frame
            frame.seek(0)
            frame.truncate()

    def stop(self) -> None:
        logger.info('Stop the camera')
        self._camera.stop_preview()
        self._camera.close()
