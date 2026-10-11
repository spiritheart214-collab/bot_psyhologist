"""Декораторы для бота"""
from functools import wraps
from typing import Any, Callable, List

from colorama import Fore

from database import is_user
from logger import logger
from logger.utils import _extract_context
from vk_bot import MessageContext
from .registry import _COMMANDS


def command(names: List[str]):
    """Декоратор для регистрации команд"""

    def decorator(func):
        for name in names:
            logger.debug(f"Регистрация команды: {Fore.LIGHTMAGENTA_EX + name}")
            _COMMANDS[name.lower()] = func
        return func

    return decorator


def is_user_exist(func: Callable) -> Callable:
    """
    Проверяет, зарегистрирован ли пользователь.
    Если пользователь зарегистрирован — выполняет функцию.
    Если нет — возвращает сообщение о необходимости регистрации.
    """

    @wraps(func)
    def wrapper(context: MessageContext) -> Any:
        from database import is_user

        is_registered = is_user(vk_id=context.user_id)

        if not is_registered:
            logger.info(
                f"Команда {func.__name__} запрещена "
                f"незарегистрированному пользователю "
                f"[ID: {context.user_id}]"
            )

            return (
                "Чтобы пользоваться этой командой, "
                "вам необходимо зарегистрироваться!",
                None,
            )

        return func(context)

    return wrapper


def log_message(func: Callable) -> Callable:
    """Декоратор логирующий входящие сообщения"""

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Находит пользователя, выводит сообщения, ФИО, статус регистрации"""

        # Вне зависимости как обьект context был передан (через арги или кварги) контекст будет извлечен
        context = _extract_context(*args, **kwargs)
        user_name = context.bot.get_user_name(context.user_id)
        is_registered = is_user(vk_id=context.user_id)

        logger.info(
            f"НОВОЕ СООБЩЕНИЕ!\n"
            f"\tПОЛЬЗОВАТЕЛЬ: {user_name} [ID: {context.user_id}]\n"
            f"\tСТАТУС: {Fore.GREEN + "ЗАРЕГЕСТРИРОВАН" if is_registered else Fore.YELLOW + "НЕ ЗАРЕГЕСТРИРОВАН" + 
                                                                              Fore.RESET}\n"
            f"\tСООБЩЕНИЕ: {context.text}")

        result = func(*args, **kwargs)
        return result

    return wrapper
