from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# 👤 Модель пользователя в БД
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Integer, default=0)  # "0" - обычный пользователь, "1" - администратор, "2" - с доступом ко всем статьям
    is_active = Column(Boolean, default=False)  # Нужно одобрение админа
