FROM arm32v6/python:3.8-alpine

RUN apk add alpine-sdk

RUN wget --output-document=download.zip https://github.com/joan2937/pigpio/archive/master.zip \
    && mkdir download \
    && unzip -d download download.zip \
    && cd /download/* \
    && sed -i -e 's/ldconfig/echo ldconfig disabled/g' Makefile \
    && make \
    && make install

# Installer les dépendances Python
RUN pip install pigpio rpyc

# Copier le script de contrôle du servo dans le conteneur
WORKDIR /app
COPY . /app

# Exposer le port pour pigpiod
EXPOSE 8888

# Démarrer pigpiod et le script Python
# CMD ["sh", "-c", "sleep 30000"]

CMD ["sh", "-c", "pigpiod && sleep 2 && python /app/src/main.py > /dev/stdout 2>&1"]