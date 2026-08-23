import time
from functools import wraps
from typing import Any, Callable

from  colorama import Fore

from .logger_setup import logger
from .utils import _args_to_str, _kwargs_to_str, _extract_context


def log_message(func: Callable) -> Callable:
    """Декоратор логирующий входящие сообщения"""

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Находит пользователя, выводит сообщения, ФИО, статус регистрации"""

        # Вне зависимости как обьект context был передан (через арги или кварги) контекст будет извлечен
        context = _extract_context(*args, **kwargs)
        user_name = context.bot.get_user_name(context.user_id)

        logger.info(f"НОВОЕ СООБЩЕНИЕ!\n"
                    f"\tПОЛЬЗОВАТЕЛЬ: {user_name} [ID: {context.user_id}]\n"
                    f"\tСтатус: {Fore.YELLOW } ЗАРЕГЕСТРИРОВАН/НЕ ЗАРЕГЕСТРИРОВАН {Fore.RESET}\n"
                    f"\tСООБЩЕНИЕ: {context.text}")

        result = func(*args, **kwargs)
        return result

    return wrapper


def log_command(func: Callable) -> Callable:
    """Декоратор логирующий вызов команды"""

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Логирует вызванную команду бота и пользщователя"""
        context = _extract_context(*args, **kwargs)
        user_name = context.bot.get_user_name(context.user_id)
        logger.info(f"Пользователем  {user_name} [ID: {context.user_id}] вызвана команда: {func.__name__}")
        logger.debug(f"Документация {func.__name__}: {func.__doc__}")

        result = func(*args, **kwargs)
        return result
    return wrapper


def log_function(func: Callable) -> Callable:
    """Декоратор логирующий вызов функции и ее параметры"""

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Логирует параметры и время работы функции"""
        log_args = _args_to_str(arguments=args)
        log_kwargs = _kwargs_to_str(keyword_args=kwargs)
        coma = ", " if args and kwargs else ""

        logger.info(f"Вызов функции {func.__name__}")
        logger.debug(f"Функция: {func.__name__}({log_args}{coma}{log_kwargs})")
        logger.debug(f"Документация: \t{func.__doc__}")

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        result_time = end_time - start_time

        if result:
            logger.debug(f"Ответ функции: {func.__name__} = {result}")

        logger.info(f"Завершение функции: {func.__name__}. (Время работы функции: {result_time:.6f})")

        return result

    return wrapper
