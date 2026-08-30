"""Модуль с функциями по работе с бд"""
from logger import logger, log_function

from .config import db
from .model import User, Request


def create_db() -> None:
    """Создание бд и таблиц"""

    logger.debug(f"Создание базы данных...")
    db.connect()
    db.create_tables([User, Request])


@log_function
def create_user(vk_id: int, name: str, surname: str, phone: str) -> User:
    """Создает пользователя по параметрам"""
    user = User.create(
        vk_id=vk_id,
        name=name,
        surname=surname,
        phone=phone
    )
    return user
    

@log_function
def create_user_request(user_id: int, request: str) -> Request:
    """Создает запрос пользователя по параметрам"""
    user_request = Request.create(user=user_id, request=request)
    return user_request


if __name__ == '__main__':

    user = User.get(id=1)
    print(f"ПОЛЬЗОВАТЕЛЬ: {user.get_full_info()}")

    for request in user.requests:
        print(request.request)

