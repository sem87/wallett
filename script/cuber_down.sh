#!/bin/bash

DIR="/home/sem/py/cuber"
echo "=== $DIR ==="
cd "$DIR" || { echo "Ошибка пути"; exit 1; }
docker-compose down
echo "ЗАВЕРШЕНО"

# chmod +x cuber_down.sh   сделать исполняемым
#    ./news_down.sh    вызвать файл
