#!/bin/bash

DIR="/home/sem/py/news"
echo "=== $DIR ==="
cd "$DIR" || { echo "Ошибка пути"; exit 1; }
docker-compose down
echo "ЗАВЕРШЕНО"

# chmod +x news_down.sh   сделать исполняемым
#    ./news_down.sh    вызвать файл
