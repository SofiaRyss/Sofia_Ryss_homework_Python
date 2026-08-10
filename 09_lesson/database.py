"""
Настройка подключения к БД и определение моделей.
Работаем с существующей таблицей student из БД Test 19.
"""
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Получаем данные для подключения из "сейфа".env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# Формируем строку подключения
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Создаём "движок" для связи с БД
engine = create_engine(DATABASE_URL)

# Фабрика сессий
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# Базовый класс для моделей
Base = declarative_base()


# Модель для существующей таблицы student
class Student(Base):
    """Модель студента (существующая таблица)."""
    __tablename__ = "student"
    __table_args__ = {'schema': 'public'}

    user_id = Column(Integer, primary_key=True, index=True)
    level = Column(String, index=True)
    education_form = Column(String)
    subject_id = Column(Integer)
