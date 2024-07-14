from services.servos_service import ServosService
import rpyc

class ServosRpc(rpyc.Service):
    _servos_service: ServosService = None

    def __init__(self) -> None:
        self._servos_service = ServosService()

    def exposed_set_servo_angle(self, angle_x, angle_y) -> None:
        self._servos_service.set_servos_angles(angle_x, angle_y)
