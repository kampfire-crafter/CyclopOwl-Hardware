FROM arm32v6/python:3.8-alpine

RUN apk add alpine-sdk cmake openssl

RUN wget --output-document=download.zip https://github.com/joan2937/pigpio/archive/master.zip \
    && mkdir download \
    && unzip -d download download.zip \
    && cd /download/* \
    && sed -i -e 's/ldconfig/echo ldconfig disabled/g' Makefile \
    && make \
    && make install

# RUN pip install wheel
# RUN pip install cmake
RUN pip install pigpio rpyc opencv-python==4.5.5.64

WORKDIR /app
COPY . /app

# EXPOSE 8888

# Démarrer pigpiod et le script Python
# CMD ["sh", "-c", "sleep 30000"]

CMD ["sh", "-c", "pigpiod && sleep 2 && python /app/src/main.py > /dev/stdout 2>&1"]
