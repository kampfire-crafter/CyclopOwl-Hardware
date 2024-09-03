import time # time.sleep(0.01)
import pigpio
import rpyc

from rpyc.utils.server import ThreadedServer

pi = pigpio.pi()
server = ThreadedServer(MyService, port = 18812)

if not pi.connected:
    exit()

SERVO_PIN = 12

MIN_PULSE_WIDTH = 500
MAX_PULSE_WIDTH = 2500

def set_servo_angle(angle):
    pulse_width = MIN_PULSE_WIDTH + (angle / 180.0) * (MAX_PULSE_WIDTH - MIN_PULSE_WIDTH)
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

try:
    class MyService(rpyc.Service):
        def exposed_set_servo(self, angle):
            set_servo_angle(angle)

    if __name__ == "__main__":
        server.start()

except KeyboardInterrupt:
    pass
finally:
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    pi.stop()
    server.close()
