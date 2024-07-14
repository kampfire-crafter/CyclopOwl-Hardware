import pigpio

# pi = pigpio.pi()

# if not pi.connected:
#     exit()

class Servo:
    _pin: int

    def __init__(self, pin) -> None:
        self._pin = pin

    def set_servo_pulsewidth(self, pulse_width) -> None:
        pi = pigpio.pi()
        pi.set_servo_pulsewidth(self._pin, pulse_width)
        pi.stop()

    def __del__(self):
        print(f"[main] Stop servo on pin ${self._pin}")
        # pi.stop()
