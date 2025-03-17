# Используем официальный образ Python
FROM python:3.13

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt ./
COPY localextensions/ ./localextensions/
COPY example-plate/ ./example-plate/
RUN apt update && apt install -y netcat-openbsd
RUN pip install --no-cache-dir -r requirements.txt


# Копируем код приложения
COPY backend /app

# Разрешаем выполнение скрипта
RUN chmod +x /app/docker-entrypoint.sh

# Запускаем FastAPI через Gunicorn
CMD ["/app/docker-entrypoint.sh"]
