FROM python:3.10-slim

RUN pip install pigpio rpyc pytest

RUN apt update && apt install python3-numpy -y
WORKDIR /app

COPY . /app
