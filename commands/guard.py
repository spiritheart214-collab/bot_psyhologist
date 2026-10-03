from functools import wraps
from typing import Callable, Any

from logger import logger
from vk_bot import MessageContext


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
