"""Модуль с функциями по работе с бд"""
import os
from typing import Tuple

from logger import logger, log_create_request, log_created_user, log_function

from .config import db, DB_PATH
from .model import BaseModel, User, Request

MODELS: Tuple[BaseModel] = User, Request


@log_function
def create_db() -> None:
    """Создание бд и таблиц"""

    logger.info(f"Создание базы данных...")
    if db.is_closed():
        db.connect()
    db.create_tables(MODELS)
    logger.success(f"База данных созданна. Созданные модели: {[f'{model.__name__}' for model in MODELS]}")


@log_created_user
def create_user(vk_id: int, name: str, surname: str, phone: str) -> User:
    """Создает пользователя по параметрам"""
    user = User.create(
        vk_id=vk_id,
        name=name,
        surname=surname,
        phone=phone
    )
    return user


@log_create_request
def create_user_request(user_id: int, request: str) -> Request:
    """Создает запрос пользователя по параметрам"""
    user_request = Request.create(user=user_id, request=request)
    return user_request


@log_function
def find_user(vk_id: int) -> User:
    """
    Функция поиска пользователя по айди

    :param vk_id: vk id по которому будет производиться поиск
    :return: id пользователя в базе данных (объект пользователя)
    """
    #Todo функция в случае не найденного пользователя выдает ошибку
    user = User.get_or_none(vk_id=vk_id)
    return user


@log_function
def clean_bd() -> None:
    """Очистка бд"""
    db.drop_tables(models=(User, Request))
    logger.info(f"База данных очищена!")


@log_function
def delete_bd() -> None:
    """Удаление базы данных (файла БД)"""
    if not db.is_closed():
        db.close()
        logger.debug("Соединение с БД закрыто")

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        logger.success(f"Файл базы данных удалён: {DB_PATH}")
    else:
        logger.warning(f"Файл базы данных не найден: {DB_PATH}")


@log_function
def is_user(vk_id: int) -> bool:
    """
    Проверка на существование пользоватлея в бд

    :param vk_id: id ля поиска
    :return: True/False в зависимости от существования пользователя в бд
    """
    is_user_exist = User.get_or_none(vk_id=vk_id)
    if is_user_exist is not None:
        return True
    else:
        return False


if __name__ == '__main__':
    # python -m database.crud  - запуск
    create_db()

    user = create_user(vk_id=1, name="Pavel", surname="Khapalashwili", phone="89032315963")
    request = create_user_request(user_id=user, request="SOME USER REQUEST")
    request2 = create_user_request(user_id=user, request="SOME USER REQUEST 2")
    request3 = create_user_request(user_id=user, request="SOME USER REQUEST 3")

    finded_user = find_user(vk_id=1)
    print(user.get_full_name())

    print(is_user(vk_id=12))
    clean_bd()
    delete_bd()
