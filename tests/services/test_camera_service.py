import pytest
import io
from drivers.camera_interface import CameraInterface
from services.camera_service import CameraService

def stream_mock():
    return [io.StringIO(str(i)) for i in range(0, 9)]

class CameraMock(CameraInterface):
    def __init__(self):
        self.is_running = False

    def start(self) -> None:
        self.is_running = True

    def stop(self) -> None:
        self.is_running = False

    def record(self):
        for i in stream_mock():
            yield i

@pytest.fixture
def camera_mock():
    return CameraMock()


class TestCameraService:
    def test_camera_start_stop(self, camera_mock):
        camera_service = CameraService(camera_mock)

        camera_service.start()
        assert camera_mock.is_running is True
        
        camera_service.stop()
        assert camera_mock.is_running is False
        

    def test_camera_record(self, camera_mock):
        camera_service = CameraService(camera_mock)
        camera_service.start()

        records = [i for i in camera_service.record()]
        assert all([a.getvalue() == b.getvalue() for a, b in zip(records, stream_mock())])