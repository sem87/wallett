FROM python:3.11-slim

# Объявляем аргументы для прокси (передаются только при сборке)
ARG HTTP_PROXY
ARG HTTPS_PROXY

# Передаем их в переменные окружения для pip и системных утилит
ENV HTTP_PROXY=$HTTP_PROXY
ENV HTTPS_PROXY=$HTTPS_PROXY
ENV http_proxy=$HTTP_PROXY
ENV https_proxy=$HTTPS_PROXY

WORKDIR /app

# Копируем только requirements.txt для эффективного кэширования слоев
COPY requirements.txt .

# Устанавливаем зависимости через прокси с игнорированием SSL-инспекции прокси
RUN pip install --no-cache-dir -r requirements.txt \
    --trusted-host opensource.tbank.ru \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org

# Копируем весь остальной код
COPY . .

# Добавляем текущую директорию в PYTHONPATH
ENV PYTHONPATH=/app

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD python -c "print('OK')" || exit 1

# Запуск скрипта
CMD ["python", "main.py"]


# RUN apt-get update && apt-get install -y docker.io docker-compose-plugin   для управления скриптами
# СТРОИМ ИМЕЙДЖ
# docker build --no-cache \
#   --build-arg HTTP_PROXY="http://yUBkUP:xUoCe5@186.179.61.140:9768" \
#   --build-arg HTTPS_PROXY="http://yUBkUP:xUoCe5@186.179.61.140:9768" \
#   -t sem87sem/wallett:latest .
# Повершелл
# docker build --no-cache --build-arg HTTP_PROXY="http://yUBkUP:xUoCe5@186.179.61.140:9768" --build-arg HTTPS_PROXY="http://yUBkUP:xUoCe5@186.179.61.140:9768" -t sem87sem/wallett:latest .
# ПУШИМ В ДОКЕР ХАБ
# docker push sem87sem/wallett:latest

