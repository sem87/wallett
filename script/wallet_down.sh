#!/bin/bash

DIR="/home/sem/py/wallet"
echo "=== $DIR ==="
cd "$DIR" || { echo "Ошибка пути"; exit 1; }
docker-compose down
echo "ЗАВЕРШЕНО"

# chmod +x wallet_down.sh   сделать исполняемым
#    ./wallet_down.sh    вызвать файл
