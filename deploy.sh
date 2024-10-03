#!/bin/bash

sshpass -p '9911' ssh cyclopowl "docker compose -f /home/pi/CyclopOwl-Hardware/docker-compose.production.yaml down"
sshpass -p '9911' ssh cyclopowl sudo rm -r /home/pi/CyclopOwl-Hardware/*
sshpass -p '9911' scp -r ./* cyclopowl:/home/pi/CyclopOwl-Hardware
sshpass -p '9911' ssh cyclopowl "docker compose -f /home/pi/CyclopOwl-Hardware/docker-compose.production.yaml up --build"
