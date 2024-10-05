<div style="text-align: justify;">
<div style="display: flex; align-items: center; justify-content: space-between;">
    <h1>CyclopOwl Project</h1>
    <img src="./docs/cyclopowl.png" alt="CycloOwlIcon" width="100"/>
</div>

## Project Description

CyclopOwl project is focuses on building a rotative camera system using a Raspberry Pi Zero W. The camera can be housed in a custom 3D-printed structure that accommodates two servo motors, allowing the camera to rotate. This setup provides a full range of motion in multiple directions. The system incorporates the following components (the below 3D printed structure is an example):

<div style="display: flex; align-items: center; justify-content: space-between;">

<div style="margin: 20px;">

- **3D-Printed Structure (brown)**: The camera's housing is custom-designed and 3D-printed, providing durability and a tailored fit for the components.
- **Raspberry Pi Zero W (green)**: It offers sufficient processing power for video streaming and motor control, along with built-in Wi-Fi for seamless wireless communication, making it ideal for remote monitoring and control.
- **PiCamera (green)**: A camera module specifically designed for use with Raspberry Pi, ensuring reliable video capture.
- **Cooling Fan (black)**: To maintain optimal operating temperatures for the Raspberry Pi, a cooling fan is integrated, preventing overheating during prolonged use.
- **Two Servo Motors (blue)**: These motors allow for precise control of the camera's orientation.

</div>
<img src="./docs/camera_360.gif" alt="CycloOwlIcon" width="250px" style="margin: 20px;"/>

</div>

## Setting Up the Project on Raspberry Pi Zero W

### Hardware

Connect the two servo motors to the Raspberry Pi GPIO pins as specified in your .env file (default pins are 12 and 13). Make sure to follow these connections:

#### Servo Motor 1 & 2

- Connect the **control wires** to GPIO pin 12 and 13 on the Raspberry Pi (or the ones you want, but do not forget to modify the values of PIN_SERVO_X and PIN_SERVO_Y in the .env file).
- Connect the **power wires** to 5V pins on the Raspberry Pi.
- Connect the **ground wires** to grounds (GND) pin on the Raspberry Pi.

#### Camera

Connect the Pi Camera to the Raspberry Pi using the camera interface (CSI) connector. Ensure that the camera is properly seated and the connector is locked in place.

### Software

Ensure you have a Raspberry Pi Zero W with Raspbian installed. You will need Docker and Docker Compose installed on your Raspberry Pi. If you haven't installed them yet, follow the official Docker installation guide and Docker Compose installation guide.

Clone the project repository to your Raspberry Pi using Git. Open a terminal and run:

```bash
git clone <repository_url>
cd <repository_directory>
```

#### Prepare Environment Variables

Create an .env file in the root directory of the project. This file should include the necessary environment variables (cp .env.example .env), such as the GPIO pins for the servos:

```
ENV="development"
HOST="0.0.0.0"
PORT=8000
PIN_SERVO_X=12
PIN_SERVO_Y=13
```

#### Build and start the Docker Container

In the terminal, navigate to the directory containing your docker-compose.yml file. Build the Docker container using:

```bash
docker compose -f /home/pi/CyclopOwl-Hardware/docker-compose.production.yaml up --build -d
```

The docker command will run the pigpiod daemon, which is required for GPIO control, and execute the main application script.

## How to interact with the camera

### Streaming

After the application is up and running, you can access the camera streaming by connecting a client throught the socket. Use python socket package :

```python
import socket

client = socket.socket()
client.connect(('192.168.1.23', 8000))

conn = client.makefile('rb')
```

Enable the streaming by sending this command :

```python
client.send('{"action":"ENABLE_STREAMING","args":[]}'.encode())
```

And listen the camera stream with :

```python
import io
import struct

size = struct.calcsize('<L')

while True:
    length_co = conn.read(size)
    # conn.flush()
    length = struct.unpack('<L', length_co)[0]
    image = io.BytesIO()
    image.write(conn.read(length))
    # conn.flush()
    ...
```

Then, it can be disabled by sending this command :

```python
client.send('{"action":"DISABLE_STREAMING","args":[]}'.encode())
```

### Rotation

To rotate the camera :

```python
import socket

client = socket.socket()
client.connect(('192.168.1.23', 8000))

conn = client.makefile('rb')

# change the args values -> [x,y]
client.send('{"action":"ROTATE","args":[0,0]}'.encode())
```
</div>