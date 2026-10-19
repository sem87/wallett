#!/bin/bash

DIR="/home/sem/py/script"
echo "=== $DIR ==="
cd "$DIR" || { echo "Ошибка пути"; exit 1; }
docker-compose down
echo "ЗАВЕРШИНО"

# chmod +x wallet_down.sh   сделать исполняемым
#    ./stop.sh    вызвать файл
