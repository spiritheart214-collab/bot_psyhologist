"""Модуль с функциями по работе с бд"""
from .config import db
from .model import User


def create_db() -> None:
    """Создание бд и таблиц"""
    db.connect()
    db.create_tables([User])


def create_user(name: str, surname: str, phone: str) -> User:
    """Создает пользователя по параметрам"""
    user = User.create(
        name=name,
        surname=surname,
        phone=phone
    )

    return user


if __name__ == '__main__':
    create_db()
    user = create_user(name="Pavel", surname="Khabalashwili", phone="89032315963")
    print(user.get_full_info())
