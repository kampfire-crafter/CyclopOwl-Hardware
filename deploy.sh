#!/bin/bash

sshpass -p '9911' ssh cyclopowl "docker compose -f ~/CyclopOwl-Hardware/docker-compose.yaml down"
sshpass -p '9911' ssh cyclopowl sudo rm -r /home/pi/CyclopOwl-Hardware/*
sshpass -p '9911' scp -r ./* cyclopowl:/home/pi/CyclopOwl-Hardware
sshpass -p '9911' ssh cyclopowl "docker compose -f ~/CyclopOwl-Hardware/docker-compose.yaml up -d --build"
