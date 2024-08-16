FROM balenalib/rpi-debian-python:3.11-buster

RUN pip install pigpio rpyc 

RUN apt update && apt install pigpio python3-numpy python-picamera python3-picamera
WORKDIR /app

COPY . /app

CMD ["sh", "-c", "pigpiod && sleep 2 && python /app/src/main.py > /dev/stdout 2>&1"]
