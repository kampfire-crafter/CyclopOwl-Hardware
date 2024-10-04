FROM python:3.11-slim

RUN pip install pigpio rpyc pytest dependency-injector python-dotenv

RUN apt update && apt install python3-numpy -y
WORKDIR /app

COPY . /app

CMD ["/bin/bash", "-c", "sleep 100000"]
