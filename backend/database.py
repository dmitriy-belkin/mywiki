from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Загружаем конфигурацию из .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Подключение к базе данных
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()

async def get_db_session():
    """Dependency для получения сессии БД."""
    async with SessionLocal() as session:
        yield session
