from drivers.servo import Servo

class ServosService:
    _PIN_X = 12
    _PIN_Y = 13

    _MIN_PULSE_WIDTH = 500
    _MAX_PULSE_WIDTH = 2500
    
    _servo_x: Servo = None
    _servo_y: Servo = None

    def __init__(self) -> None:
        self._servo_x = Servo(self._PIN_X)
        self._servo_y = Servo(self._PIN_Y)

    def set_servos_angles(self, angle_x, angle_y) -> None:
        pulse_width_x = self._MIN_PULSE_WIDTH + (angle_x / 180.0) * (self._MAX_PULSE_WIDTH - self._MIN_PULSE_WIDTH)
        pulse_width_y = self._MIN_PULSE_WIDTH + (angle_y / 180.0) * (self._MAX_PULSE_WIDTH - self._MIN_PULSE_WIDTH)
        
        self._servo_x.set_servo_pulsewidth(pulse_width_x)
        self._servo_y.set_servo_pulsewidth(pulse_width_y)