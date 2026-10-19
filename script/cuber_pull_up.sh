#!/bin/bash

DIR="/home/sem/py/cuber"
echo "=== $DIR ==="
cd "$DIR" || { echo "Ошибка пути"; exit 1; }

echo "⏳ Останавливаем контейнер..."
docker-compose down
sleep 10

echo "⏳ Скачиваем актуальный образ с Docker Hub..."
docker-compose pull
sleep 10

echo "⏳ Запускаем контейнер..."
docker-compose up -d
sleep 10

echo "✅ ЗАВЕРШЕНО"
