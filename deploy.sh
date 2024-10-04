#!/bin/bash

read -sp "Enter password: " PASSWORD
echo

sshpass -p $PASSWORD ssh cyclopowl "docker compose -f /home/pi/CyclopOwl-Hardware/docker-compose.production.yaml down"
sshpass -p $PASSWORD ssh cyclopowl sudo rm -r /home/pi/CyclopOwl-Hardware/*
sshpass -p $PASSWORD scp -r ./* cyclopowl:/home/pi/CyclopOwl-Hardware
sshpass -p $PASSWORD ssh cyclopowl "docker compose -f /home/pi/CyclopOwl-Hardware/docker-compose.production.yaml up --build"
