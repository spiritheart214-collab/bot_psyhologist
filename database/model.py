"""Модуль описывающий модели бота"""
from datetime import datetime

from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField, Model, TextField

from .config import db


class BaseModel(Model):
    """Базовый модель с привязкой к бд"""

    class Meta:
        database = db


class User(BaseModel):
    """Модель пользователя бота"""
    vk_id = IntegerField(null=False, index=True, unique=True, verbose_name="id_vk", help_text="Введите айди вк: ")
    name = CharField(max_length=30, null=False, verbose_name="Имя", help_text="Введите имя: ")
    surname = CharField(max_length=30, null=False, index=True, verbose_name="Фамилия", help_text="Введите фамилию: ")
    phone = CharField(max_length=20, null=False, unique=True, index=True)
    date_joined = DateTimeField(default=datetime.now,  verbose_name="Дата создания", help_text="Дата и время")

    def get_full_name(self):
        """Функция отображения полного имени"""
        full_name = f"{self.name} {self.surname}"
        return full_name

    def get_full_info(self):
        """Функция отображения полного имени"""
        full_name = f"{self.name} {self.surname} | {self.phone}"
        return full_name


class Request(BaseModel):
    """Модель запросов пользователей к психологу"""
    user = ForeignKeyField(User, backref="requests")
    request = TextField(null=False, verbose_name="Запрос", help_text="Введите запрос: ")
    date = DateTimeField(default=datetime.now, verbose_name="Дата создания", help_text="Дата и время")

    def save(self, *args, **kwargs):
        if len(self.request) > 1000:
            raise ValueError("Текст не может быть длиннее 1000 символов")
        super().save(*args, **kwargs)

