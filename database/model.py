"""Модуль описывающий модели бота"""
from datetime import datetime

from peewee import CharField, DateTimeField, Model

from .config import db


class BaseModel(Model):
    """Базовый модель с привязкой к бд"""

    class Meta:
        database = db


class User(BaseModel):
    """Модель пользователя бота"""

    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    phone = CharField(max_length=20)
    date_joined = DateTimeField(default=datetime.now)

    def get_full_name(self):
        """Функция отображения полного имени"""
        full_name = f"{self.name} {self.surname}"
        return full_name

    def get_full_info(self):
        """Функция отображения полного имени"""
        full_name = f"{self.name} {self.surname} | {self.phone}"
        return full_name

