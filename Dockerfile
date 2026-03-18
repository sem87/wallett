FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Добавляем текущую директорию в PYTHONPATH
ENV PYTHONPATH=/app
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD python -c "print('OK')" || exit 1
# Запуск скрипта
CMD ["python", "main.py"]
