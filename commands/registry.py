"""Модуль содержит еестр зарегестрированных команд и функция по работе с реестром"""
import inspect

from typing import Callable, Dict, Optional, Tuple

_COMMANDS: Dict[str, Callable] = {}  # Реестр


def get_command(name: str, user_id: int) -> Tuple[str, Optional[str]]:
    """
    Функция ищет введенную пользователем команду в реестре зарегистрированных команд.
    Если функция принимает id пользователя, то передает id в функцию
    """
    name = name.lower().strip()

    # Если команда не в списке зарегестрированных
    if name not in _COMMANDS:
        return f"Неизвестная команда {name}. Напишите 'помощь'.", None

    command = _COMMANDS[name]

    # Если команда содержит параметр 'user_id' - id пользователя
    if "user_id" in inspect.signature(command).parameters:
        return command(user_id=user_id)
    else:
        command()



