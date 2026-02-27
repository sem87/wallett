FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Добавляем текущую директорию в PYTHONPATH
ENV PYTHONPATH=/app
# Запуск скрипта
CMD ["python", "main.py"]
