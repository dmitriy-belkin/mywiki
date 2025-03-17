#!/bin/bash

echo "⏳ Ожидание доступности PostgreSQL..."
until nc -z -v -w30 db 5432; do
    echo "Ожидание PostgreSQL..."
    sleep 1
done
echo "✅ PostgreSQL доступен."

# 🚀 Выполняем миграции
echo "🔄 Запуск миграций БД..."
alembic upgrade headd

# 🌐 Запуск сервера FastAPI
echo "🚀 Запускаем FastAPI..."
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
